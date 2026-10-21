#!/usr/bin/env python3
"""Quick frontend-performance audit of a live URL (stdlib only).

Usage: python audit_url.py <url> [--json]

Reports TTFB, HTML size, compression, cache headers, protocol, cookies, and
scans the HTML for checklist issues (render-blocking scripts/CSS, unsized or
non-lazy images, base64 images, inline scripts/styles, iframes, font hints).
It checks the HTML document only; use Lighthouse/DevTools for sub-resources.
"""
import gzip
import json
import re
import sys
import time
import urllib.request
import zlib
from html.parser import HTMLParser

UA = "Mozilla/5.0 (frontend-performance audit)"


def fetch(url, accept_encoding):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": accept_encoding})
    start = time.perf_counter()
    resp = urllib.request.urlopen(req, timeout=30)
    first = resp.read(1)
    ttfb = time.perf_counter() - start
    body = first + resp.read()
    total = time.perf_counter() - start
    return resp, body, ttfb, total


def decode(body, encoding):
    if encoding == "gzip":
        return gzip.decompress(body)
    if encoding == "deflate":
        return zlib.decompress(body)
    if encoding == "br":
        try:
            import brotli  # optional
            return brotli.decompress(body)
        except ImportError:
            return None
    return body


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_head = False
        self.in_script = False
        self.cur_inline_script = False
        self.blocking_scripts, self.inline_scripts = [], 0
        self.blocking_css, self.stylesheets = [], 0
        self.style_blocks, self.style_bytes, self.style_attrs = 0, 0, 0
        self.in_style = False
        self.imgs = self.imgs_no_dims = self.imgs_no_lazy = 0
        self.base64_imgs = 0
        self.iframes = self.iframes_no_lazy = 0
        self.preconnects, self.preloads = [], []
        self.http_refs = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "style" in a:
            self.style_attrs += 1
        for k in ("src", "href"):
            v = a.get(k) or ""
            if v.startswith("http://"):
                self.http_refs.append(v)
        if tag == "head":
            self.in_head = True
        elif tag == "script":
            self.in_script = True
            if a.get("src"):
                if not ("async" in a or "defer" in a or a.get("type") == "module"):
                    self.blocking_scripts.append(a["src"])
                self.cur_inline_script = False
            else:
                t = (a.get("type") or "text/javascript").lower()
                self.cur_inline_script = "javascript" in t or t == "module"
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            if "stylesheet" in rel:
                self.stylesheets += 1
                media = (a.get("media") or "all").lower()
                if media in ("all", "screen", ""):
                    self.blocking_css.append(a.get("href"))
            if "preconnect" in rel:
                self.preconnects.append(a.get("href"))
            if "preload" in rel:
                self.preloads.append(f"{a.get('as')}: {a.get('href')}")
        elif tag == "style":
            self.in_style = True
            self.style_blocks += 1
        elif tag == "img":
            self.imgs += 1
            if not (a.get("width") and a.get("height")):
                self.imgs_no_dims += 1
            if (a.get("loading") or "").lower() != "lazy":
                self.imgs_no_lazy += 1
            if (a.get("src") or "").startswith("data:image"):
                self.base64_imgs += 1
        elif tag == "iframe":
            self.iframes += 1
            if (a.get("loading") or "").lower() != "lazy":
                self.iframes_no_lazy += 1

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False
        elif tag == "script":
            self.in_script = False
        elif tag == "style":
            self.in_style = False

    def handle_data(self, data):
        if self.in_script and self.cur_inline_script and data.strip():
            self.inline_scripts += 1
            self.cur_inline_script = False
        if self.in_style:
            self.style_bytes += len(data.encode())


def kb(n):
    return f"{n / 1024:.1f} KB"


def main():
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    if not args:
        sys.exit(__doc__)
    url = args[0]
    as_json = "--json" in sys.argv

    resp, raw, ttfb, total = fetch(url, "br, gzip, deflate")
    h = resp.headers
    enc = (h.get("Content-Encoding") or "").lower()
    html = decode(raw, enc)
    if html is None:  # brotli lib missing - refetch with gzip to parse
        _, raw2, _, _ = fetch(url, "gzip")
        html = gzip.decompress(raw2) if raw2[:2] == b"\x1f\x8b" else raw2
    text = html.decode(resp.headers.get_content_charset() or "utf-8", errors="replace")

    s = Scan()
    s.feed(text)
    cookies = h.get_all("Set-Cookie") or []
    base64_total = len(re.findall(r"data:image/[a-z+]+;base64", text))

    r = {
        "url": url,
        "final_url": resp.geturl(),
        "status": resp.status,
        "https": resp.geturl().startswith("https://"),
        "ttfb_s": round(ttfb, 3),
        "html_download_s": round(total, 3),
        "html_transferred": len(raw),
        "html_uncompressed": len(html),
        "content_encoding": enc or None,
        "cache_control": h.get("Cache-Control"),
        "etag": bool(h.get("ETag")),
        "hsts": bool(h.get("Strict-Transport-Security")),
        "cdn_hints": {k: h.get(k) for k in ("Server", "Via", "X-Cache", "CF-Cache-Status", "X-Vercel-Cache", "Age") if h.get(k)},
        "cookies": {"count": len(cookies), "max_bytes": max((len(c) for c in cookies), default=0)},
        "render_blocking_scripts": s.blocking_scripts,
        "inline_scripts": s.inline_scripts,
        "stylesheets": s.stylesheets,
        "render_blocking_css": s.blocking_css,
        "style_blocks": s.style_blocks,
        "inline_style_bytes": s.style_bytes,
        "style_attributes": s.style_attrs,
        "images": s.imgs,
        "images_without_width_height": s.imgs_no_dims,
        "images_not_lazy": s.imgs_no_lazy,
        "base64_images": base64_total,
        "iframes": s.iframes,
        "iframes_not_lazy": s.iframes_no_lazy,
        "preconnect": s.preconnects,
        "preload": s.preloads,
        "http_refs_on_https": s.http_refs if resp.geturl().startswith("https://") else [],
    }

    if as_json:
        print(json.dumps(r, indent=2))
        return

    def line(ok, label, detail):
        mark = "OK  " if ok is True else ("FAIL" if ok is False else "INFO")
        print(f"[{mark}] {label}: {detail}")

    print(f"Audit: {r['final_url']} (HTTP {r['status']})\n")
    line(r["https"], "HTTPS", "yes" if r["https"] else "no")
    line(r["hsts"] or None, "HSTS", "set" if r["hsts"] else "not set")
    line(r["ttfb_s"] < 1.3, "TTFB", f"{r['ttfb_s']} s (target < 1.3 s, single sample from this machine)")
    line(bool(enc), "Compression", enc or "none on HTML")
    line(None, "HTML size", f"{kb(r['html_transferred'])} transferred / {kb(r['html_uncompressed'])} uncompressed")
    line(None, "Cache-Control (HTML)", r["cache_control"] or "absent")
    line(None, "CDN hints", r["cdn_hints"] or "none detected")
    c = r["cookies"]
    line(c["count"] < 20 and c["max_bytes"] < 4096, "Cookies", f"{c['count']} set by HTML response, largest {c['max_bytes']} B")
    line(not s.blocking_scripts, "Render-blocking scripts", f"{len(s.blocking_scripts)} {s.blocking_scripts[:5]}")
    line(s.inline_scripts <= 2 or None, "Inline <script> blocks", s.inline_scripts)
    line(None, "Stylesheets", f"{s.stylesheets} ({len(s.blocking_css)} render-blocking)")
    line(None, "Inline <style>", f"{s.style_blocks} blocks, {kb(s.style_bytes)}; {s.style_attrs} style= attributes")
    line(s.imgs_no_dims == 0, "Images missing width/height", f"{s.imgs_no_dims} of {s.imgs}")
    line(None, "Images without loading=lazy", f"{s.imgs_no_lazy} of {s.imgs} (fine for above-the-fold/LCP)")
    line(base64_total == 0 or None, "Base64 images", base64_total)
    line(s.iframes == 0 or None, "Iframes", f"{s.iframes} ({s.iframes_no_lazy} not lazy)")
    line(None, "Preconnect", s.preconnects or "none")
    line(None, "Preload", s.preloads or "none")
    if r["http_refs_on_https"]:
        line(False, "Mixed-protocol refs", r["http_refs_on_https"][:5])
    print("\nHTML document only - run Lighthouse for page weight, images, JS/CSS sizes and LCP.")


if __name__ == "__main__":
    main()
