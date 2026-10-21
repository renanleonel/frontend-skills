---
name: frontend-performance
description: Audit and fix frontend loading performance against a prioritized checklist — page weight, load time, TTFB, compression (gzip/brotli), cache headers, render-blocking JS/CSS, critical CSS, minification, image formats/sizing/lazy-loading, fonts (WOFF2, preconnect, FOIT/FOUT), cookies, iframes, third-party scripts and dependency/bundle size. Use whenever the user says a site or page is slow, wants a better Lighthouse/PageSpeed/Core Web Vitals score, asks for a performance audit or review, wants to shrink a bundle or page weight, or asks about caching, compression, image or font optimization for a website — even if they don't say "performance". Not for backend-only latency, database tuning, or React render/re-render profiling.
---

# Frontend Performance

Audit a site or codebase against a prioritized checklist, fix what matters most, and prove the improvement with numbers.

The checklist is ordered by impact. Work top-down: a 4 MB hero image or a missing `Cache-Control` header dwarfs anything in the low-priority list, so don't spend the user's time on unused CSS while the page ships uncompressed JavaScript.

## Workflow

### 1. Establish a baseline

You can't claim an improvement you didn't measure. Before changing anything, get numbers:

- **Live URL available**: run `python <this-skill-dir>/scripts/audit_url.py <url>` (bundled; add `--json` for machine-readable output). It reports TTFB, transfer size, compression, cache headers, protocol, cookies, and scans the HTML for render-blocking scripts/CSS, unsized or non-lazy images, base64 images, inline scripts/styles, iframes, and font hints. Also run Lighthouse if available: `npx lighthouse <url> --only-categories=performance --output=json --output-path=./lh.json --chrome-flags="--headless"`.
- **Codebase only**: build the production bundle and measure it (`dist/` sizes, `vite build` / `next build` output, `npx source-map-explorer` or the bundler's analyzer). Serve the build locally and run the script / Lighthouse against it.
- **Neither**: audit the code statically and say clearly that numbers are unverified.

Record the baseline: page weight, request count, TTFB, LCP / load time, and the largest assets.

### 2. Audit against the checklist

Read `references/checklist.md` — every item has *why it matters*, *how to check*, and *how to fix*. Go through the High priority section fully, then Medium, then Low. For each item mark it **pass**, **fail**, or **n/a** with the evidence (a header value, a file size, a line of code). Skip items that genuinely don't apply (no cookies, no fonts) rather than padding the report.

Locate where each fix belongs: server/CDN config (nginx, Vercel, Netlify, Cloudflare headers), build config (Vite, webpack, Next.js), or source (HTML, components, CSS). The framework usually handles some items already — Next.js minifies and code-splits by default, Vercel compresses — so check before recommending.

### 3. Fix, highest impact first

Only edit code if the user asked for fixes; otherwise deliver the report and offer to apply them. When fixing:

- Prefer the framework's built-in mechanism (`next/image`, `next/font`, Vite's `build.cssMinify`, the host's headers config) over hand-rolled solutions — it's maintained and less likely to regress.
- One concern per change, so a regression can be traced.
- Don't break behavior for a score. `defer` on a script that other inline code depends on, or lazy-loading the LCP image, makes things worse.

### 4. Re-measure

Run the same measurements as step 1 and show before → after. If something couldn't be re-measured (no live URL, no browser), say so.

## Report format

```markdown
# Frontend performance audit — <site/project>

## Baseline
| Metric | Value | Target |
|---|---|---|
| Page weight | 2.4 MB | < 1.5 MB (ideally < 500 KB) |
| Load time / LCP | 4.1 s | < 3 s |
| TTFB | 0.9 s | < 1.3 s |
| Requests | 87 | as few as practical |

## Findings
### High priority
- ❌ **Compression disabled** — `content-encoding` absent on main.js (812 KB). Fix: enable brotli in nginx (`brotli on;`) … 
- ✅ HTTPS — served over HTTPS, no mixed content.

### Medium priority
…
### Low priority
…

## Recommended order of fixes
1. … (expected saving: ~600 KB)

## After (if fixes applied)
| Metric | Before | After |
```

Keep findings to the evidence and the fix. List passes briefly — one line each — so the user sees coverage without wading through it.

## Tools to point the user to

- **PageSpeed Insights** (pagespeed.web.dev) — Lighthouse lab data plus real-user CrUX field data.
- **Lighthouse** — local lab audit (`npx lighthouse` or Chrome DevTools → Lighthouse).
- **WebPageTest** — filmstrip, waterfall, real devices/locations; best for diagnosing TTFB and request chains.
- **Chrome DevTools** — Network (sizes, caching, protocol, waterfall), Performance (main-thread long tasks), Coverage (unused JS/CSS).
- **Bundlephobia** (bundlephobia.com) — cost of an npm package before adding it.
- **Squoosh** (squoosh.app) — compress/convert images by hand; for batches use `sharp` or `@squoosh/cli`.
