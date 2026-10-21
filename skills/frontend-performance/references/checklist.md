# Frontend performance checklist

Each item: **Why** · **Check** · **Fix**. Thresholds come from the frontend-performance roadmap; treat them as targets, not laws.

## Contents
- [High priority](#high-priority) (H1–H19)
- [Medium priority](#medium-priority) (M1–M13)
- [Low priority](#low-priority) (L1–L8)

---

## High priority

### H1. Page weight < 1500 KB (ideally < 500 KB)
- **Why**: every byte costs time on mobile networks and data plans; weight is the root of most other metrics.
- **Check**: DevTools Network → "transferred" total with cache disabled; `audit_url.py` gives the HTML size, Lighthouse gives `total-byte-weight`.
- **Fix**: attack the biggest assets first — usually images, then JS bundles, then fonts. Sort the Network panel by size.

### H2. Load time < 3 seconds
- **Why**: abandonment rises sharply past ~3 s.
- **Check**: Lighthouse LCP / Speed Index on a throttled mobile profile; PageSpeed Insights field data if the site has traffic.
- **Fix**: this is an outcome — fix weight, TTFB, and render-blocking resources (H1, H7, H8, H11, H12).

### H3. GZIP / Brotli compression enabled
- **Why**: text assets (HTML, CSS, JS, JSON, SVG) shrink 70–90%.
- **Check**: response header `content-encoding: br` or `gzip` on text responses (`curl -sI -H 'Accept-Encoding: br, gzip' <url>`).
- **Fix**: most hosts (Vercel, Netlify, Cloudflare) do it automatically. nginx: `gzip on; gzip_types text/css application/javascript application/json image/svg+xml;` plus the brotli module. Express: `compression()`. Or pre-compress at build time (`vite-plugin-compression`). Don't compress already-compressed formats (JPEG, PNG, WOFF2).

### H4. Minimize HTTP requests
- **Why**: each request has overhead; on HTTP/1.1 browsers cap ~6 connections per host. HTTP/2+ reduces but doesn't remove the cost.
- **Check**: request count in DevTools / Lighthouse; look for many tiny icons, duplicate libraries, chains of imports.
- **Fix**: SVG sprites or icon components instead of many icon files, remove unused third-party tags, bundle small modules. Under HTTP/2, prefer sensible chunking over one giant bundle.

### H5. Compress images / keep image count low
- **Why**: images are typically the majority of page weight.
- **Check**: Network filtered to Img, sorted by size; Lighthouse "Efficiently encode images".
- **Fix**: compress (quality ~75–80 is rarely distinguishable), use `sharp`/Squoosh, a framework image component (`next/image`), or an image CDN. Replace decorative images with CSS where possible.

### H6. Set HTTP cache headers properly
- **Why**: repeat visits should cost almost nothing.
- **Check**: `cache-control` on each asset type.
- **Fix**: fingerprinted assets (`main.a1b2c3.js`) → `Cache-Control: public, max-age=31536000, immutable`. HTML → `no-cache` (revalidate with ETag) so deploys show up. Never long-cache un-hashed filenames.

### H7. Time To First Byte < 1.3 seconds
- **Why**: nothing can render until the first byte arrives.
- **Check**: `audit_url.py` TTFB; WebPageTest from several locations; DevTools → request → Timing → "Waiting for server response".
- **Fix**: CDN / edge caching of HTML, static generation or ISR instead of per-request SSR, slow server-side data fetches (cache or parallelize), fewer redirects.

### H8. Non-blocking JavaScript: use async / defer
- **Why**: a plain `<script src>` in `<head>` stops HTML parsing until it downloads and runs.
- **Check**: `<script src>` without `async`, `defer`, or `type="module"` before the content.
- **Fix**: `defer` for app scripts (preserves order, runs after parse); `async` for independent ones (analytics). Modules are deferred by default. Verify no inline script depends on a script you just deferred.

### H9. Minify JavaScript
- **Why**: removes whitespace/comments and shortens identifiers — commonly 30–50% smaller before compression.
- **Check**: open a production JS file; readable formatting = not minified.
- **Fix**: production builds of Vite/webpack/Next do this (esbuild/terser/SWC). Make sure the deployed artifact is the production build (`NODE_ENV=production`).

### H10. Minify CSS
- **Why**: same as JS, smaller gains but free.
- **Check**: production CSS has comments/whitespace.
- **Fix**: bundler CSS minification (Lightning CSS, cssnano, esbuild).

### H11. Inline the critical (above-the-fold) CSS
- **Why**: the browser can paint the first screen without waiting for the full stylesheet.
- **Check**: Lighthouse "Eliminate render-blocking resources"; large CSS file blocking first paint.
- **Fix**: `critters`/`beasties` (Next.js `experimental.optimizeCss`), `critical` npm package. Keep inlined CSS small (~14 KB budget fits in the first round trip). CSS-in-JS with SSR often covers this already.

### H12. CSS files are non-blocking
- **Why**: all `<link rel="stylesheet">` block rendering by default.
- **Check**: stylesheets not needed for first paint (print styles, below-the-fold widgets, third-party CSS).
- **Fix**: `media="print"` for print CSS; load non-critical CSS with `<link rel="preload" as="style" onload="this.rel='stylesheet'">` (with a `<noscript>` fallback) or lazy-import it with the component.

### H13. Use HTTPS
- **Why**: required for HTTP/2+, service workers, Brotli in browsers, and many modern APIs; also SEO and trust.
- **Check**: URL scheme, redirect from http → https, HSTS header.
- **Fix**: TLS via host / Let's Encrypt, `Strict-Transport-Security` header.

### H14. Choose the image format appropriately
- **Why**: the right format can cut size by half or more.
- **Check**: PNG photos, JPEG for graphics with flat colors, GIF animations.
- **Fix**: photos → AVIF/WebP (JPEG fallback via `<picture>`); flat graphics/icons/logos → SVG; transparency → WebP/PNG; animations → `<video>` (MP4/WebM) instead of GIF.

### H15. Avoid requesting unreachable files (404)
- **Why**: wasted round trips, sometimes blocking.
- **Check**: DevTools Network filtered by status 4xx; console errors; missing favicon/source maps/fonts.
- **Fix**: remove or correct the references.

### H16. Serve files from the same protocol
- **Why**: HTTP resources on an HTTPS page are blocked (mixed content) or trigger warnings, and http→https redirects add round trips.
- **Check**: `http://` URLs in HTML/CSS/JS on an HTTPS page.
- **Fix**: use `https://` or root-relative URLs.

### H17. Minimize the number of iframes
- **Why**: each iframe is a full document with its own resources and main-thread cost.
- **Check**: `<iframe>` count (YouTube embeds, maps, ads, chat widgets).
- **Fix**: remove what's not needed; `loading="lazy"` on below-the-fold iframes; facades (click-to-load thumbnail, e.g. `lite-youtube-embed`).

### H18. Avoid embedded / inline CSS
- **Why**: inline `style=""` and per-page `<style>` blocks can't be cached and duplicate across pages. (Deliberately inlined critical CSS from H11 is the exception.)
- **Check**: large `<style>` blocks or heavy `style` attributes in server HTML.
- **Fix**: move to cached stylesheets / CSS modules.

### H19. Analyse stylesheet complexity
- **Why**: huge or deeply nested selectors and massive rule counts slow style recalculation and bloat CSS.
- **Check**: CSS file size, rule count, specificity (Project Wallace / CSS Stats), DevTools Performance → "Recalculate Style" time.
- **Fix**: remove dead rules, flatten nesting, avoid universal/descendant-heavy selectors in hot paths.

---

## Medium priority

### M1. Minified HTML
- **Check/Fix**: production HTML with comments/whitespace → `html-minifier-terser` or framework option. Small gain once compression is on.

### M2. Use a Content Delivery Network
- **Why**: serves assets from near the user; cuts latency and offloads origin.
- **Check**: response headers (`cf-cache-status`, `x-vercel-cache`, `x-cache`, `server`), asset hostnames.
- **Fix**: host on Vercel/Netlify/Cloudflare or put a CDN in front of static assets.

### M3. Prefer vector images over bitmaps
- **Why**: SVG is tiny and sharp at any resolution for icons, logos, illustrations.
- **Fix**: replace PNG icons/logos with SVG (optimize with SVGO). Keep photos as raster.

### M4. Set width and height on images
- **Why**: reserves space so the layout doesn't jump (CLS).
- **Check**: `<img>` without `width`/`height` (or CSS `aspect-ratio`).
- **Fix**: add intrinsic dimensions; CSS `width:100%; height:auto` keeps it responsive.

### M5. Avoid Base64 images
- **Why**: ~33% larger than binary, uncacheable separately, and bloats the HTML/CSS that blocks rendering.
- **Check**: `data:image/` in HTML/CSS/JS.
- **Fix**: external files. Exception: tiny (<1–2 KB) placeholders or LQIP blurs.

### M6. Lazy-load offscreen images
- **Why**: don't download what the user may never scroll to.
- **Check**: below-the-fold `<img>` without `loading="lazy"`.
- **Fix**: `loading="lazy"` + `decoding="async"`. **Never** lazy-load the LCP/hero image — give it `fetchpriority="high"` instead.

### M7. Serve images close to their display size
- **Why**: a 3000 px image shown at 300 px wastes ~99% of its pixels.
- **Check**: Lighthouse "Properly size images"; compare natural vs rendered size in DevTools.
- **Fix**: `srcset` + `sizes`, framework image components, or an image CDN with resizing.

### M8. Avoid multiple inline `<script>` snippets
- **Why**: inline scripts are parser-blocking, uncacheable, and scattered tag snippets often load duplicate code.
- **Fix**: consolidate into a deferred external file; load third-party tags via a tag manager or `async`.

### M9. Keep dependencies up to date
- **Why**: newer versions often ship smaller builds, tree-shakable ESM, and perf fixes.
- **Check**: `npm outdated`.
- **Fix**: upgrade with care (changelogs, tests). Don't bulk-upgrade majors without the user's go-ahead.

### M10. Check for performance problems in your JavaScript
- **Why**: long tasks (>50 ms) block input and hurt INP/TBT.
- **Check**: DevTools Performance recording, Lighthouse TBT / "Reduce JavaScript execution time", Coverage tab for unused JS.
- **Fix**: code-split routes and heavy components (`import()`), debounce/throttle handlers, avoid layout thrashing (batch DOM reads/writes), move heavy work to a Web Worker.

### M11. Service Workers for caching / heavy tasks
- **Why**: instant repeat loads and offline support; workers keep heavy computation off the main thread.
- **Fix**: Workbox / `vite-plugin-pwa` / `@serwist/next` for caching strategies. Only suggest when repeat visits or offline matter — a service worker adds real complexity and cache-invalidation risk.

### M12. Cookie size < 4096 bytes
- **Why**: cookies are sent with every request to the domain, including static assets.
- **Check**: `Set-Cookie` sizes / DevTools Application → Cookies.
- **Fix**: store less in cookies (use an ID + server session); serve static assets from a cookieless domain/CDN.

### M13. Keep the cookie count < 20
- **Why**: same overhead, and browsers cap cookies per domain.
- **Fix**: consolidate; audit third-party scripts that set cookies.

---

## Low priority

### L1. Preload URLs where possible
- **Why**: tells the browser about critical late-discovered resources early (LCP image, key font, next route).
- **Fix**: `<link rel="preload" as="image|font|script">` for the few truly critical assets; `rel="prefetch"` for likely next navigations. Over-preloading competes for bandwidth — keep it to a handful.

### L2. Concatenate CSS into a single file
- **Why**: fewer requests on HTTP/1.1. On HTTP/2+ this matters much less, and per-route CSS splitting is often better. Recommend only when the site has many small stylesheets.

### L3. Remove unused CSS
- **Check**: DevTools Coverage, Lighthouse "Reduce unused CSS".
- **Fix**: Tailwind's content scanning already does it; otherwise PurgeCSS with a safelist for dynamic classes. Test carefully — dynamic class names get purged by mistake.

### L4. Use WOFF2 fonts
- **Why**: ~30% smaller than WOFF, supported everywhere modern.
- **Fix**: serve only WOFF2 (drop TTF/EOT/WOFF fallbacks unless legacy support is required).

### L5. Use preconnect to load fonts faster
- **Fix**: `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` for third-party font hosts — or better, self-host (`next/font`, Fontsource) and preload the main font file.

### L6. Keep web font size < 300 KB
- **Fix**: subset (`unicode-range`, `glyphhanger`, `pyftsubset`), fewer weights, a variable font instead of many static files.

### L7. Prevent Flash or Invisible Text (FOIT/FOUT)
- **Fix**: `font-display: swap` (or `optional` for non-brand text); match fallback metrics with `size-adjust` / `ascent-override` (`next/font` and Fontaine do this automatically) to avoid layout shift.

### L8. Keep an eye on the size of dependencies
- **Check**: bundle analyzer (`rollup-plugin-visualizer`, `@next/bundle-analyzer`, `source-map-explorer`); Bundlephobia before adding a package.
- **Fix**: replace heavy libs (moment → date-fns/dayjs, lodash → per-method imports or native), import only what you use, lazy-load rarely used heavy features.
