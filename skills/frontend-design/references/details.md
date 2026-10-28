Catalog of small product details distilled from [detail.design](https://detail.design) (curated by Rene Wang), paraphrased. Read when building or polishing a feature and you want the touches that make it feel considered; scan the category that matches the work. Entries marked *(inferred from title)* had no editor's note and are lower confidence. Each `Topic:` names the reference file the rule extends.

## Design

### Active State in Footer Navigation
`Design` · linear.app · https://detail.design/detail/active-state-also-works-in-footer
**Rule:** Mark the current page in footer navigation links too, not only in the header or sidebar.
**Why:** Users keep a sense of location wherever they navigate from.
**How:** `aria-current="page"` on the matching link, styled via `[aria-current=page]`.
**Topic:** interaction

### Anchored Scrolling
`Design` · n/a · https://detail.design/detail/anchored-scrolling
**Rule:** In keyboard-navigated lists, move only the highlight at first, pin it near ~70% of the viewport once it gets there, then scroll the list underneath, and release the pin at the end so the last item is reachable.
**Why:** A stable focus point is easier to track, and the release gives a clear sense of the boundary.
**How:** Track highlighted index; scroll the container only when the row passes the threshold; clamp the scroll at max. Keep the search input fixed by anchoring the panel's top rather than centering it, so it does not shift as the result count changes.
**Topic:** interaction

### Auto Naming for Screenshot Based on Context
`Design` · iOS · https://detail.design/detail/auto-naming-for-screenshot-based-on-context
**Rule:** Name exported or downloaded files from their content or context (title, body text) instead of generic counters.
**Why:** People search for files later by what they contained, not by `img-001`.
**How:** Slugify the item's title for `download` / `Content-Disposition` filenames, with a sensible fallback.
**Topic:** copy

### Avoid Using WebP for OG Images
`Design` · n/a · https://detail.design/detail/avoid-using-webp-for-og
**Rule:** Use PNG or JPEG for Open Graph images and keep key content within a central safe area (about 1000x500px).
**Why:** Several social platforms support WebP inconsistently, and each crops differently.
**How:** `<meta property="og:image" content="/og.png">` at 1200x630, text and logos centered.
**Topic:** edge-cases

### Better Render for Arrow Input
`Design` · Notion · https://detail.design/detail/better-render-for-arrow-input
**Rule:** In text inputs, convert typed sequences like `->` into a real arrow glyph.
**Why:** Typing two characters to get an arrow is awkward and renders poorly.
**How:** Replace on input in rich-text editors; keep it undoable with Backspace/Undo.
**Topic:** typography

### Blur Trick for the Optical Fit
`Design` · n/a · https://detail.design/detail/blur-trick-for-the-optical-fit
**Rule:** Check optical alignment by blurring the design; if an element looks off-center or unbalanced when blurred, nudge it by hand.
**Why:** Blur strips out edges and exposes visual weight, which geometric measurements miss.
**How:** Apply a temporary `filter: blur(4px)` in devtools or squint at a screenshot.
**Topic:** layout

### Blurred Gradient Edge
`Design` · from @rauno's work · https://detail.design/detail/blurred-gradient-edge
**Rule:** Fade the edge of scrollable content with a blur plus gradient mask, and extend the effect past the container edges when it does not span the full width.
**Why:** Soft edges signal more content and avoid hard clipping; an unbled edge shows a visible seam.
**How:** `mask-image: linear-gradient(to bottom, #000 calc(100% - 32px), transparent)`, optionally with a `backdrop-filter: blur()` overlay layer.
**Topic:** surfaces

### Bring Life to AI Features
`Design` · Notion, Claude Code, Obsidian · https://detail.design/detail/bring-life-to-ai-features
**Rule:** Give AI features a personality (customizable character, varied status verbs) so they feel alive rather than mechanical.
**Why:** A bit of character makes waiting and delegation feel more human and memorable.
**How:** Rotate through a list of progress verbs in loading states; let users pick an avatar.
**Topic:** ai-interfaces

### Collapse Instead of Close
`Design` · Linear, Vercel · https://detail.design/detail/collapse-instead-of-close
**Rule:** For persistent notices such as "what's new" popups, offer collapse instead of close so users feel they are hiding, not destroying.
**Why:** Hiding is gentler, and the content stays recoverable.
**How:** Collapse to a small pill/button that can reopen it; persist the state.
**Topic:** interaction

### Color String Preview
`Design` · n/a · https://detail.design/detail/color-string-preview
**Rule:** Show a small inline swatch next to any color value in text so it is recognizable at a glance.
**Why:** Hex strings are machine-readable; a swatch removes the mental decoding.
**How:** Inline `<span class="size-3 rounded-sm border" style="background:#3B82F6">` before the code; keep it adjacent (not hover-only), small, and with a subtle border so light colors stay visible.
**Topic:** color

### Convert Internal URLs to Rich Previews
`Design` · detail.design · https://detail.design/detail/convert-internal-urls-to-rich-previews
**Rule:** When a pasted or rendered link points to your own app, show a rich preview (title, icon, state) instead of a raw URL.
**Why:** You know what the target is, so a glance beats a string of text.
**How:** Match the origin/route pattern, resolve the entity, render a chip or card; fall back to a plain link.
**Topic:** interaction

### CSS Text-Box Trim
`Design` · n/a · https://detail.design/detail/css-text-box-trim
**Rule:** Trim the built-in leading above cap height and below the baseline so text boxes align exactly with neighboring elements.
**Why:** Removes the invisible space that makes vertical padding in buttons, badges and headings look uneven.
**How:** `text-box: trim-both cap alphabetic;` (older name `text-box-trim`); verify browser support and add a fallback.
**Topic:** typography

### Currency Detection in Photos
`Design` · iOS · https://detail.design/detail/ios-currency-detection-in-photos
**Rule:** Recognize convertible values (currency, units, times, dates) in content and make them tappable to reveal an instant conversion in a small popover.
**Why:** It removes the copy, switch-app, search loop and delivers value in context.
**How:** Parse values with a regex or library, wrap in a button that opens a Popover with the converted result (`Intl.NumberFormat`, `Intl.DateTimeFormat`).
**Topic:** interaction

### Custom Scrollbar
`Design` · n/a · https://detail.design/detail/custom-scrollbar
**Rule:** Style scrollbars with the standard properties so they stay slim and quiet.
**Why:** Default chunky scrollbars clash with refined UIs inside panels and lists.
**How:** `scrollbar-width: thin; scrollbar-color: gray transparent;`
**Topic:** surfaces

### Custom Video Player
`Design` · detail.design · https://detail.design/detail/custom-video-player
**Rule:** Build a custom video player controlled from a global style, covering toolbar styling, a blurred thumbnail before load, and playback speed control.
**Why:** The default toolbar looks inconsistent with the product and lacks useful controls.
**How:** Hide native `controls`, build your own with `HTMLMediaElement` (`playbackRate`), use a blurred `poster` as placeholder.
**Topic:** surfaces

### Delayed Close for Promotional Banners
`Design` · n/a · https://detail.design/detail/delay-close-action-for-promotional-info
**Rule:** Hold back the close button on promotional banners and "what's new" popups for a brief moment after they appear.
**Why:** It forces a moment of attention so the headline gets seen before dismissal.
**How:** Render the button disabled/hidden for ~1s then enable; keep keyboard Escape available if the popup is blocking.
**Topic:** interaction

### Detect Address in PDF
`Design` · apple.com · https://detail.design/detail/detect-address-in-pdf
**Rule:** Detect addresses (and similar entities) in displayed text and make them actionable (map, copy).
**Why:** Saves users from copying data between apps.
**How:** Regex or NER on rendered text, wrap matches in a link or menu trigger.
**Topic:** interaction

### Dynamic Favicon
`Design` · GitHub, LobeHub · https://detail.design/detail/dynamic-favicon
**Rule:** Update the favicon to reflect page status (pending, success, failure, merged) on pages that track a long-running state, and differentiate dev from production.
**Why:** Users with many tabs can read status at a glance without switching.
**How:** Swap `<link rel="icon">` href when state changes; use a separate dev icon in non-production builds.
**Topic:** interaction

### Dynamic Role of Enter Key
`Design` · Discord · https://detail.design/detail/dynamic-role-of-enter-key
**Rule:** Make Enter behave according to context: send the message normally, insert a newline inside a code block.
**Why:** The key does what the user most likely means in each state.
**How:** In the keydown handler, check the editor context (inside code fence, IME composing) before submitting; Shift+Enter always inserts a newline.
**Topic:** interaction

### Dynamic Theme Color
`Design` · n/a · https://detail.design/detail/dynamic-theme-color
**Rule:** Set the browser chrome color to match the page background and update it as the page or scroll position changes.
**Why:** The address bar blends into the app for an immersive feel.
**How:** `<meta name="theme-color" content="#0a0a0a" media="(prefers-color-scheme: dark)">`; update `content` from JS on route/scroll changes.
**Topic:** color

### Dynamic Visual Guideline
`Design` · Vercel · https://detail.design/detail/dynamic-visual-guideline
**Rule:** Show row/column guide lines in dense tables, but fade them out while the user hovers or selects so the active highlight is the only emphasis.
**Why:** Guides help scanning at rest and become noise once attention is on a specific cell.
**How:** Table-level `:hover` lowers guide opacity: `.table:hover .guide { opacity: 0 }` (or `group-hover:opacity-0`).
**Topic:** surfaces

### Easy-to-Reference ID
`Design` · Linear · https://detail.design/detail/easy-to-reference-id
**Rule:** Give user-visible identifiers a short, human-readable scheme (prefix plus number, or memorable words) instead of random strings.
**Why:** People quote, search and remember IDs out loud; internal keys can stay random.
**How:** Keep a separate display ID (`ENG-123`) from the database primary key.
**Topic:** copy

### Fade Edge Doesn't Override Scrollbar
`Design` · https://detail.design/detail/fade-edge-doesnt-override-scrollbar
**Rule:** When fading the edges of a scroll container, keep the fade from covering the scrollbar.
**Why:** An overlay on the scrollbar hides the control and makes it hard to grab.
**How:** Apply the fade with `mask-image` on an inner content wrapper (or inset the gradient pseudo-element by the scrollbar width) rather than on the scrolling element itself.
**Topic:** surfaces

### Glassy Button
`Design` · https://detail.design/detail/liquid-glass-button
**Rule:** Build frosted-glass surfaces from four layers: backdrop blur, low-alpha fill, thin translucent border, soft shadow.
**Why:** Each layer defines a different cue (translucency, edge, lift); omit one and the effect looks flat.
**How:** `backdrop-filter: blur(20px); background: rgb(255 255 255 / .1); border: 1px solid rgb(255 255 255 / .2); box-shadow: 0 8px 24px rgb(0 0 0 / .15)`.
**Topic:** surfaces

### Hold to Reveal Shortcut Hint
`Design` · https://detail.design/detail/hold-to-reveal-shortcut-hint
**Rule:** Reveal keyboard shortcut hints on the controls themselves while the modifier key is held, instead of only listing them in a help dialog.
**Why:** Hints shown in context are seen every time, so shortcuts actually get learned.
**How:** Track `keydown`/`keyup` for `Meta`/`Control` in a context or `data-` attribute on the root, and show `<kbd>` badges via CSS when set; clear on `blur`.
**Topic:** interaction

### Immersive Browser Tab Icon
`Design` · Dia (Browser Company) · https://detail.design/detail/immersive-browser-tab-icon
**Rule:** Let the active-tab chrome pick up the dominant color of the favicon so the tab feels part of the page.
**Why:** Matching surface to icon makes the active state read as one cohesive object.
**How:** Extract a dominant color from the icon at build or load time and apply it as the border/background token for the active item.
**Topic:** color

### Intelligent Cut and Paste
`Design` · Apple · https://detail.design/detail/intelligent-cut-and-paste
**Rule:** When text is cut or pasted, adjust the surrounding spaces so the result has exactly one space between words, only in space-delimited languages.
**Why:** Users shouldn't have to clean up double or missing spaces after moving words; the behavior dates to 1984 Macintosh guidelines.
**How:** In custom rich-text editors, handle `beforeinput` for `deleteByCut`/`insertFromPaste` and normalize adjacent whitespace; skip for languages like Thai, Chinese and Japanese.
**Topic:** interaction

### Keep State in URL
`Design` · mono.cards · https://detail.design/detail/keep-state-in-url
**Rule:** Store view state (filters, search, sort, view mode, selection, expanded sections, theme) in the URL so any link reproduces the exact view.
**Why:** Links become shareable, back/forward works, and bookmarks become useful snapshots; small one-way data needs no database.
**How:** Use `URLSearchParams` with `history.pushState`/`replaceState`, or a router search-param API (e.g. nuqs, TanStack Router search params). Keep it under roughly 2000 characters.
**Topic:** interaction

### Make the Page Portal-Proof
`Design` · https://detail.design/detail/make-the-page-portal-proof
**Rule:** Attach global listeners (keyboard shortcuts, resize, etc.) to the window that owns the component, not the global `window`, so they work in iframes, pop-out windows and portals.
**Why:** A listener bound to the parent window silently stops working when the UI renders in another document.
**How:** `const win = ref.current?.ownerDocument.defaultView ?? window; win.addEventListener("keydown", fn)`.
**Topic:** edge-cases

### Media Response to Theme Mode
`Design` · https://detail.design/detail/photo-response-to-theme-mode
**Rule:** Swap or adapt imagery (photos, illustrations, product shots) to match the active light or dark theme.
**Why:** Images that ignore the theme feel pasted-on; almost anything can respond to the mode.
**How:** `<picture>` with `<source media="(prefers-color-scheme: dark)">`, or two images toggled with `dark:hidden` / `hidden dark:block`.
**Topic:** color

### Natural Image Border
`Design` · https://detail.design/detail/natural-image-border
**Rule:** Outline images with a translucent inset ring, not a solid border.
**Why:** A semi-transparent ring blends with the picture's edge and looks softer than a hard line, and it works on any background.
**How:** `outline: 1px solid rgb(0 0 0 / .1); outline-offset: -1px` (Tailwind: `outline outline-1 -outline-offset-1 outline-black/10`), or `ring-1 ring-inset ring-black/10`; use white at low alpha in dark mode.
**Topic:** surfaces

### Outer and Inner Border Radius
`Design` · https://detail.design/detail/outer-and-inner-border-radius
**Rule:** For nested rounded shapes, set the inner radius to the outer radius minus the padding between them.
**Why:** Matching curves keeps the gap visually even; equal radii make corners look thick. Not applicable everywhere, so use judgment.
**How:** `border-radius: calc(var(--outer-radius) - var(--padding))`.
**Topic:** surfaces

### Overflow-Tolerant Input
`Design` · https://detail.design/detail/overflow-tolerant-input
**Rule:** Do not hard-block typing at a length limit; let people finish the thought, show the overflow, and flag the excess.
**Why:** Silent truncation or blocked keystrokes lose content and frustrate; users prefer to trim themselves.
**How:** Show a live counter that turns to the error color past the limit, mark the excess text, and validate on submit instead of using `maxLength`.
**Topic:** interaction

### Paste with Intent
`Design` · Obsidian · https://detail.design/detail/paste-with-intent
**Rule:** In contexts where intent is unambiguous (such as a canvas), turn a pasted URL directly into a rich embed with no confirmation step.
**Why:** Paste becomes a creation gesture and removes friction, provided the result is reversible and cheap.
**How:** Handle the `paste` event, read `clipboardData.getData("text/plain")`, and create the object if it parses as a URL; do not do this in plain text or code editors, and keep undo working.
**Topic:** interaction

### Prevent Continuous Click
`Design` · product not named · https://detail.design/detail/prevent-continous-click
**Rule:** Block repeat activations of an action while it is in flight so rapid clicks cannot fire it twice.
**Why:** Double submits create duplicate records, charges or toggles. (Page has no note; inferred from the title.)
**How:** Set `disabled`/`aria-busy` or ignore events while a pending flag is true; debounce non-idempotent handlers.
**Topic:** interaction

### Progressive Blur Edge
`Design` · product not named · https://detail.design/detail/progressive-blur-edge
**Rule:** Where content scrolls under a sticky bar, fade it with a graduated blur (stronger toward the edge) rather than a flat color gradient.
**Why:** A color fade washes out photos and saturated UI; blur removes detail instead of color and looks softer.
**How:** Stack ~6-7 absolutely positioned `pointer-events-none` layers, each with `backdrop-filter: blur(Npx)` (1px to 48px) and a `mask-image: linear-gradient(...)` limiting it to a band; add `-webkit-` prefixes.
**Topic:** surfaces

### Rich Previews for External URLs
`Design` · product not named · https://detail.design/detail/rich-previews-for-external-urls
**Rule:** Render pasted or linked external URLs as a preview (title, image, domain) instead of a bare string where context allows.
**Why:** Users can judge the destination without leaving the page. (Page has no note; inferred from the title.)
**How:** Fetch Open Graph tags server-side and render a compact card; keep the raw URL as fallback and show the hostname.
**Topic:** surfaces

### Scroll Landmark
`Design` · product not named · https://detail.design/detail/scroll-landmark
**Rule:** Give long scrolling views a visible, tappable shortcut to jump to the top that also remembers the previous position so the user can go back.
**Why:** The iOS status-bar tap only works on Apple devices, is undiscoverable and cannot be undone.
**How:** Show a small sticky "back to top" control after scrolling; store `scrollY` and offer "return" after the jump.
**Topic:** interaction

### Search by Context Instead of Just Keywords
`Design` · Linear · https://detail.design/detail/search-by-context-instead-of-name
**Rule:** Make search interpret intent and scope: map user phrasing to the right settings or entity, and bias results by where the user is.
**Why:** People search by what they want to do, not by the exact label the product uses.
**How:** Add synonym/alias keywords to command-palette and settings items (e.g. "change my password" matches "Security"); weight results by current section.
**Topic:** interaction

### Searchable Collapsed Content
`Design` · product not named · https://detail.design/detail/searchable-collapsed-content
**Rule:** Keep collapsed sections findable by browser find-in-page.
**Why:** `display:none` content is invisible to Cmd/Ctrl+F, forcing users to expand everything manually.
**How:** `<div hidden="until-found">` inside a disclosure; listen to the `beforematch` event to sync open state. Chromium-only; degrades to plain hidden elsewhere.
**Topic:** accessibility

### Smart Time Decision
`Design` · Siri · https://detail.design/detail/smart-time-decide
**Rule:** Resolve ambiguous relative dates and times using the user's likely mental model, and ask when unsure.
**Why:** Late at night "tomorrow at 9" usually means the coming morning, not the day after; literal parsing causes missed alarms.
**How:** When the picked time is already past or within the small hours, default to the next occurrence or show a confirm like "Did you mean 8 PM today?".
**Topic:** copy

### Smarter Word Break
`Design` · product not named · https://detail.design/detail/smarter-word-break
**Rule:** Make wrapping respect word boundaries in every language, including CJK, not just in English.
**Why:** Balanced-looking line breaks can still split Chinese or Japanese words mid-word because spaces do not guard meaning there.
**How:** Use `word-break: auto-phrase` (Chromium) for Japanese, `text-wrap: balance|pretty`, and set correct `lang` attributes; test with translated strings.
**Topic:** typography

### Special Icon Based on Folder Name
`Design` · macOS · https://detail.design/detail/special-icon-based-on-folder-name
**Rule:** Pick a contextual icon from the item's name or type (e.g. "Documents", "Downloads") instead of one generic glyph.
**Why:** Recognizable icons speed scanning and make lists feel considered.
**How:** Map known names/keywords to icons with a generic fallback; match case-insensitively.
**Topic:** surfaces

### Special Text Selection Style
`Design` · product not named · https://detail.design/detail/special-text-selection-style
**Rule:** Style `::selection` with brand-aware colors instead of the browser default.
**Why:** A small branded touch that costs nothing. (Page has no note; inferred from the title.)
**How:** `::selection { background: <accent>/30%; color: inherit }`; keep contrast legible.
**Topic:** color

### Sync Editing Content to Title
`Design` · GitHub · https://detail.design/detail/sync-editing-content-to-title
**Rule:** Mirror the text a user is editing into the surface that will display it (tab title, header) live, before save.
**Why:** It previews the result in context and tightens the feedback loop; skip it when the field is not the primary identifier or the change would be disorienting.
**How:** On input, set `document.title`; restore the saved value on cancel.
**Topic:** interaction

### Tap Tab Again to Reset State
`Design` · product not named · https://detail.design/detail/tap-tab-again-to-reset-state
**Rule:** Make re-selecting the active tab reset it: scroll to top, refresh data, or return to the root of its stack.
**Why:** It builds muscle memory and gives a safe, predictable home base.
**How:** In the tab click handler, if the tab is already active then `scrollTo({top:0})`, pop nested routes, or refetch.
**Topic:** interaction

### Text Overflow Cutoff
`Design` · product not named · https://detail.design/detail/text-overflow-cutoff
**Rule:** For fixed-width items like tabs, fade out the overflowing label with a gradient mask and/or end it with an ellipsis.
**Why:** A visible cue tells users the text continues instead of looking accidentally clipped.
**How:** `mask-image: linear-gradient(to right, black 80%, transparent)` with `overflow-hidden whitespace-nowrap`, or Tailwind `truncate`; expose the full text via `title` or tooltip.
**Topic:** typography

### Themed Favicon
`Design` · GitHub · https://detail.design/detail/themed-favicon
**Rule:** Provide light and dark favicon variants matching the browser theme.
**Why:** A single icon often disappears against a dark or light tab strip.
**How:** `<link rel="icon" href="/icon-dark.svg" media="(prefers-color-scheme: dark)">`; in Next.js use the `metadata.icons.icon` array with `media`.
**Topic:** color

### Themed Icon for PWA on Android
`Design` · product not named · https://detail.design/detail/themed-icon-for-pwa-on-android
**Rule:** Ship a monochrome icon in the web manifest so Android can apply themed (Material You) tinting.
**Why:** The installed PWA blends with the user's launcher instead of looking foreign.
**How:** Add `{ "src": "mono.png", "sizes": "196x196", "type": "image/png", "purpose": "monochrome" }` to `manifest.icons`.
**Topic:** surfaces

### Time-Based CTA
`Design` · Resend · https://detail.design/detail/time-based-cta
**Rule:** Tie call-to-action wording to the visitor's current time or season ("tonight", "this weekend", "by Christmas").
**Why:** It makes generic copy feel timely and personal.
**How:** Compute the label client-side from `new Date()`; render a neutral default on the server to avoid hydration mismatch.
**Topic:** copy

### Tinted Background Based on Active Media
`Design` · product not named · https://detail.design/detail/tinted-background-based-on-active-media
**Rule:** Tint the surrounding background with a color drawn from the media currently in view.
**Why:** The container feels tied to its content. (Page has no note; inferred from the title.)
**How:** Extract a dominant color (canvas sampling or precomputed token) and set it as a low-opacity background; recheck text contrast.
**Topic:** color

### Unified Login Field
`Design` · n/a · https://detail.design/detail/2-in-1-log-in-field
**Rule:** Offer one sign-in field that handles both passwordless and password login instead of forcing an upfront method choice.
**Why:** Fewer decisions and fewer screens before the user is authenticated.
**How:** Start with an email input; reveal a password field (or send a magic link) after submit based on the account's methods.
**Topic:** interaction

### Visual Alignment for Buttons with Icon
`Design` · product not named · https://detail.design/detail/visual-alignment-for-buttons-with-icon
**Rule:** Align icon buttons optically, not just by box size: compensate padding so the icon-plus-label group looks centered.
**Why:** Icons carry visual weight that makes mathematically even padding look off. (Inferred from title.)
**How:** Use less padding on the icon side (e.g. `pl-3 pr-4`), and nudge asymmetric glyphs by 1px.
**Topic:** surfaces

## Interactivity

### Auto Segment the Video
`Interactivity` · n/a · https://detail.design/detail/auto-segment-the-video
**Rule:** Detect natural boundaries in media and split it into segments automatically instead of asking users to cut by hand.
**Why:** Removes tedious manual scrubbing.
**How:** Analyze scene changes or transcript, propose segments on the timeline and let users adjust.
**Topic:** ai-interfaces

### Auto Snap to Component When Cropping Screenshot
`Interactivity` · iOS · https://detail.design/detail/auto-snap-to-component-when-cropping-screenshot
**Rule:** Snap crop handles to detected content edges when dragged near them.
**Why:** Saves pixel-peeping and yields clean results with little effort.
**How:** Compute candidate edges, snap when within a small pixel threshold, allow bypass with a modifier key.
**Topic:** interaction

### Avoid Browser Default Back Behavior
`Interactivity` · n/a · https://detail.design/detail/avoid-browser-default-back-behavior
**Rule:** Disable horizontal overscroll navigation on side-scrolling surfaces so swiping does not trigger browser back.
**Why:** Accidental history navigation destroys the user's place.
**How:** `overscroll-behavior-x: none;` on the scroller.
**Topic:** interaction

### Handle CJK Input Method Differently
`Interactivity` · Linear · https://detail.design/detail/handle-cjk-input-method-differently
**Rule:** Ignore Enter and single-letter key handlers while an IME composition is in progress.
**Why:** In Chinese Pinyin and Japanese Romaji the letters appear in the field while a candidate is pending, and Enter confirms the candidate, so submit or command shortcuts fire by mistake.
**How:** Check `e.nativeEvent.isComposing` (or `e.key === "Process"` / `keyCode === 229`) and return early; or track `compositionstart`/`compositionend`.
**Topic:** edge-cases

### Name-Derived Placeholder
`Interactivity` · https://detail.design/detail/name-derived-placeholder
**Rule:** Generate placeholder text from what the user already entered so the placeholder shows the expected format for their own data.
**Why:** A tailored example explains the expected input better than a generic one.
**How:** Compute the placeholder from the related field's value (e.g. a handle or email from the name) and update it as they type; keep a static fallback when the field is empty.
**Topic:** copy

### Overscroll Effect in Nested Scrollers
`Interactivity` · https://detail.design/detail/overscroll-nested-scrollers
**Rule:** Allow the browser's native overscroll effect on nested scrollable areas, now supported in Chrome, Safari and Firefox.
**Why:** It gives every scroll region a smooth, consistent edge response without custom code.
**How:** Avoid disabling it needlessly; use `overscroll-behavior` only when you need to stop scroll chaining to the parent.
**Topic:** interaction

### Recently Updated Apps Below Pending Updates
`Interactivity` · Apple App Store · https://detail.design/detail/recently-updated-apps-below-pending-updates
**Rule:** After a bulk action, show the completed items in a "recent" list in the same place so the result is visibly confirmed.
**Why:** Items vanishing from a pending list leaves doubt; seeing them reappear as done closes the loop and speeds follow-up actions like opening the app.
**How:** Move items from "Pending" to a "Recently completed" group in the same view instead of just removing them.
**Topic:** interaction

### Special Cursor Style While Hovering on People
`Interactivity` · product not named · https://detail.design/detail/special-cursor-style-while-hovering-on-people
**Rule:** Change the cursor on elements that reveal extra info (e.g. author or avatar areas) to signal what hovering does.
**Why:** A distinct cursor sets the expectation before the user commits to interacting.
**How:** `cursor: help` for info-on-hover regions, `cursor: pointer` only for real navigation.
**Topic:** interaction

## Accessibility

### Clicking the Input Label Focuses the Input Field
`Accessibility` · n/a · https://detail.design/detail/clicking-the-input-label-focus-the-input-field
**Rule:** Associate every visible label with its input so clicking the label focuses the field.
**Why:** It enlarges the hit area and helps assistive tech.
**How:** `<label htmlFor="email">` with a matching `id`, or wrap the input in the label.
**Topic:** accessibility

### File Path Truncating
`Accessibility` · https://detail.design/detail/file-path-truncating
**Rule:** When a file path must be truncated, keep the root folder and the file name visible and cut the middle.
**Why:** Those two parts carry the most identifying information; the filename (and its extension) is what people look for.
**How:** Render as segments: a `flex` row with the middle segment `min-w-0 truncate`, and the root and filename `shrink-0`; put the full path in `title` or a tooltip.
**Topic:** edge-cases

### Form Respects Keyboard
`Accessibility` · https://detail.design/detail/form-respects-keyboard
**Rule:** Make every form fully completable by keyboard alone, with logical tab order, Enter to submit and visible focus.
**Why:** Keyboard users and power users should never need a pointer to finish the task.
**How:** Use real `<form>`, `<label>`, `<button type="submit">`; avoid `tabindex` > 0; keep DOM order equal to visual order.
**Topic:** accessibility

### Keep Default Focus Ring
`Accessibility` · https://detail.design/detail/keep-default-focus-ring
**Rule:** Never remove the focus outline without replacing it; at minimum keep the default, and preferably restyle its color, offset and radius.
**Why:** Keyboard users rely on the ring to know which element Enter will activate.
**How:** `:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px }`; Tailwind `focus-visible:outline-2 focus-visible:outline-offset-2`. Never `outline: none` alone.
**Topic:** accessibility

### Larger Hit Area than It Appears
`Accessibility` · https://detail.design/detail/larger-hit-area-than-it-appears
**Rule:** Make small controls look refined but give them a larger invisible hit area: aim for 44px on touch and about 24px on desktop.
**Why:** Fitts's law: bigger targets are faster and more forgiving to hit.
**How:** Extend with a pseudo-element: `relative after:absolute after:-inset-2 after:content-['']`, or add padding with negative margin.
**Topic:** interaction

### Platform-Agnostic Shortcut Labels
`Accessibility` / `Design` · Vercel · https://detail.design/detail/no-cmd-or-ctrl-for-shortcuts
**Rule:** In non-text-entry, high-frequency tools, consider single-key shortcuts with no modifier, and disable them whenever a text field has focus.
**Why:** Dropping the modifier removes friction and rewards power users; it only works where typing text is not the main mode.
**How:** In the `keydown` handler, return early if `e.target` is an input/textarea/contenteditable, or any modifier or IME composition is active; show the key as a `<kbd>` hint.
**Topic:** interaction

### Reduced Animation for Frequently Used Features
`Accessibility` · Raycast · https://detail.design/detail/reduced-animation-for-frequently-used-feature
**Rule:** Strip or minimize transitions on tools opened many times a day, such as command palettes and launchers.
**Why:** Users in a goal-driven flow want zero friction, not delight, and repeated animation turns into wait time.
**How:** Make high-frequency overlays appear instantly or with a very short fade; respect `prefers-reduced-motion`.
**Topic:** accessibility

## Copywriting

### "Follow Us" Text Trick
`Copywriting` · Apple Support · https://detail.design/detail/follow-us-text-trick
**Rule:** Skip the "Follow us on X" label and show the handle itself as the link.
**Why:** The handle already says what and where, with less text.
**How:** `<a href="https://x.com/handle" aria-label="Follow us on X">@handle</a>`; keep an accessible name when only an icon or handle is visible.
**Topic:** copy

### Check Potential Problems in User Content
`Copywriting` · resend.com · https://detail.design/detail/check-potential-problem-in-user-content
**Rule:** Scan user-authored content for known omissions before the primary action and block it with a clear warning until fixed.
**Why:** Mistake-proofing removes a checklist burden and prevents consequences like deliverability or legal problems.
**How:** Run a validator on the content; disable "Send" with an inline message stating what is missing and how to fix it.
**Topic:** copy

### Confirm Newsletter Subscription
`Copywriting` · resend.com · https://detail.design/detail/confirm-newsletter-subscription
**Rule:** Use a confirmation email (double opt-in) for subscriptions and word the flow so users know to check their inbox.
**Why:** Protects recipients and keeps the list valid and deliverable.
**How:** After submit, show a "check your email" state with the address; activate only after the link is clicked.
**Topic:** copy

### Drop the WWW Prefix
`Copywriting` · n/a · https://detail.design/detail/drop-the-www-prefix
**Rule:** Show and use bare domains without the `www` prefix.
**Why:** It is a legacy convention and adds noise to URLs.
**How:** Serve the apex domain and redirect `www` to it.
**Topic:** copy

### Mailto Link
`Copywriting` · https://detail.design/detail/mailto-link
**Rule:** For an email address, make the text a `mailto:` link and offer a separate copy-to-clipboard icon next to it.
**Why:** Some users want to open their mail app, others want the address copied; support both.
**How:** `<a href="mailto:hi@x.com">hi@x.com</a>` plus a `<button aria-label="Copy email">` calling `navigator.clipboard.writeText`, with a brief "Copied" confirmation.
**Topic:** copy

### Pluralized Labels
`Copywriting` · https://detail.design/detail/pluralized-labels
**Rule:** Pluralize labels correctly by count ("1 item", "2 items") instead of using "(s)" or a generic form.
**Why:** Wording details signal care; this entry gives no more than the title.
**How:** `new Intl.PluralRules(locale).select(n)` or ICU MessageFormat `{n, plural, one {# item} other {# items}}`.
**Topic:** copy

### Poll Item Word Counter
`Copywriting` · product not named · https://detail.design/detail/poll-item-word-counter
**Rule:** Show length limits as a compact in-field indicator (e.g. a ring) that replaces the control once the user starts typing.
**Why:** Constraints appear exactly when relevant without extra UI.
**How:** SVG circle with `stroke-dasharray` driven by `value.length / max`; switch to a warning color near the limit.
**Topic:** copy

### Pre-filled Example Content
`Copywriting` · Notion · https://detail.design/detail/pre-filled-with-example-content-not-empty
**Rule:** Start new workspaces with realistic example content instead of blank screens, so users can edit rather than create.
**Why:** People copy and modify more readily than they author from scratch.
**How:** Seed templates/sample rows marked as examples and easy to delete in one action.
**Topic:** edge-cases

### Respect Brand Name
`Copywriting` · product not named · https://detail.design/detail/respect-brand-name
**Rule:** Write third-party and own brand names with their official casing (GitHub, macOS, iOS, iPhone, YouTube).
**Why:** Wrong casing reads as careless and erodes trust.
**How:** Centralize brand names in constants or a spellcheck dictionary.
**Topic:** copy

### Respect Platform Language
`Copywriting` · Linear · https://detail.design/detail/respect-platform-language
**Rule:** Use the terminology of the platform or integration the user is working in rather than generic or your own words.
**Why:** Matching vocabulary avoids translation effort for users. (Page has no note; inferred from the title.)
**How:** Keep a per-integration label map and use it in buttons, statuses and empty states.
**Topic:** copy

### Thoughtful What's New Message
`Copywriting` · product not named · https://detail.design/detail/thoughtful-whatsnew-message
**Rule:** Write release notes even for minor updates in a warm, specific voice instead of "bug fixes and improvements".
**Why:** The rarely read corners of a product still shape its personality.
**How:** Pick a short reassuring line per release; keep it one or two sentences.
**Topic:** copy

## Easter Egg

### Address on Mail App Icon
`Easter Egg` · Apple Mail · https://detail.design/detail/address-on-mail-app-icon
**Rule:** Use hidden content in small branded assets as a playful reward for close observers.
**Why:** Hidden details add charm and signal craft.
**Topic:** copy

### Cast Ending
`Easter Egg` · Linear · https://detail.design/detail/cast-ending
**Rule:** End the landing page with a credits-style sequence that acknowledges the people behind the product.
**Why:** A memorable finish adds polish and human warmth.
**Topic:** copy

### Color Name Invite Code
`Easter Egg` · Paper · https://detail.design/detail/color-name-invite-code
**Rule:** Make codes and identifiers human and memorable (for example a hex color plus its name) instead of random strings.
**Why:** Mundane tokens become something delightful and easy to remember.
**How:** Generate from a word list or a named-color table.
**Topic:** copy

### Colorful Cursor Blink
`Easter Egg` · Google AI search · https://detail.design/detail/colorful-cursor-blink
**Rule:** Reinforce brand in key input fields by letting the caret cycle through brand colors on each blink.
**Why:** It adds personality and marks a special mode.
**How:** Hide the native caret with `caret-color: transparent` and animate a custom caret; or animate `caret-color` with keyframes.
**Topic:** color

### Interactive 404 Page
`Easter Egg` · https://detail.design/detail/interactive-404-page
**Rule:** Treat the 404 page as a real part of the product and make it playful or interactive, not a dead end.
**Why:** People who land there are in a hidden corner of the site; polishing it shows care.
**How:** Keep a clear way home (link, search) alongside any game or illustration.
**Topic:** edge-cases

### Interactive Error Page
`Easter Egg` · https://detail.design/detail/interactive-error-page
**Rule:** Turn error pages into a small moment of delight to soften the frustration.
**Why:** Few users see them, but those who do are in a bad mood and benefit most.
**How:** Show the actual error and a retry action first, then add the play element.
**Topic:** edge-cases

### Not Available on Mobile Hint
`Easter Egg` · symbl.space · https://detail.design/detail/not-available-on-mobile-hint
**Rule:** If a screen is desktop-only, explain it with a friendly, witty message instead of a broken layout or a bare warning.
**Why:** It turns a limitation into a memorable moment.
**How:** Gate by `@media (max-width: …)` or `(pointer: coarse)` with a short message and an alternative (email me a link, continue on desktop).
**Topic:** edge-cases

### Shifting Emoji
`Easter Egg` · product not named · https://detail.design/detail/shifting-emoji
**Rule:** Add cheap hover surprises, like cycling an emoji button's icon, where a playful tone fits.
**Why:** Costs little and delights on every visit.
**How:** Swap the icon from a small array on `mouseenter`.
**Topic:** interaction

### Special Create Date
`Easter Egg` · Safari · https://detail.design/detail/special-create-date-for-files
**Rule:** Tuck nostalgic references into metadata nobody inspects, only where they cannot mislead or cause harm.
**Why:** Hidden nods reward curious users and express personality.
**Topic:** copy

### Text in the TextEdit App Icon
`Easter Egg` · macOS TextEdit · https://detail.design/detail/text-in-the-textedit-app-icon
**Rule:** Put meaningful placeholder copy in places like icons and sample documents that few will read closely.
**Why:** Rewards close inspection and shows craft.
**Topic:** copy

## Motion

_Motion entries: implementation belongs to `frontend-motion-design`._

### Animated Color Change in Icon Picker
`Motion` · Linear · https://detail.design/detail/animated-color-change-in-icon-picker
**Rule:** When a color selection changes, transition the preview progressively through the intermediate colors instead of switching instantly.
**Why:** Gives a smooth, tangible response to the choice.
**How:** Transition `color`/`fill` on the icon.
**Topic:** motion

### Animated State-Based Icons
`Motion` · Linear, Obsidian · https://detail.design/detail/animated-state-based-icon
**Rule:** Animate icons so they preview or mirror the action or state they control, sharing timing with the surface they affect.
**Why:** Icon motion that matches the outcome removes the gap between intent and feedback.
**How:** Drive icon state from the same boolean as the panel; animate on hover to hint at the next state.
**Topic:** motion

### ASCII Loaders
`Motion` · n/a · https://detail.design/detail/ascii-loaders
**Rule:** Consider text-character spinners as a distinctive loading indicator.
**Why:** Adds personality, especially for developer-focused products.
**How:** Cycle frames from a spinner set such as `cli-spinners`.
**Topic:** motion

### Blurred Image Appearing
`Motion` · n/a · https://detail.design/detail/blurred-image-appearing
**Rule:** Reveal images from a blurred state to sharp as they load.
**Why:** It makes image loading feel softer than a hard pop-in.
**How:** Blur-up placeholder fading to the sharp image on load.
**Topic:** motion

### Chat Minimap
`Motion` · n/a · https://detail.design/detail/chat-minimap
**Rule:** In long conversations, pin a small minimap that shows which section is in view and lets users jump between sections.
**Why:** Long transcripts make it hard to know where you are.
**How:** Sticky element with section markers driven by `IntersectionObserver`; indicator eases to the new anchor on scroll.
**Topic:** motion

### Closing Modal Respects Physics
`Motion` · Apple Music · https://detail.design/detail/closing-modal-respect-physics
**Rule:** When an expanded item closes back into a grid, return it to its origin even if the page scrolled during the transition.
**Why:** The item should land in its real slot, not where it used to be.
**How:** Read the origin rect at animation time, not at open time.
**Topic:** motion

### Cursor Style While Morphing
`Motion` · n/a · https://detail.design/detail/cursor-style-while-morphing
**Rule:** Enable form controls in a morphing element only after the transition ends, so the cursor style stays consistent during it.
**Why:** Controls appearing mid-transition flicker the cursor between styles.
**How:** `pointer-events: none` until the transition end.
**Topic:** motion

### Interruptible Animation
`Motion` · https://detail.design/detail/interruptible-animation
**Rule:** Let users trigger close, cancel or reverse immediately, without waiting for an in-flight animation to finish.
**Why:** Interfaces feel snappy and durable when input is never blocked by motion.
**How:** Prefer CSS transitions or springs that retarget; do not disable controls during the animation.
**Topic:** motion

### Music Player Layout Shift
`Motion` · macOS Tahoe · https://detail.design/detail/music-player-layout-shift
**Rule:** When content resizes, move neighbouring elements smoothly to their new positions rather than jumping.
**Why:** Choreographed layout shifts preserve spatial relationships so users can follow the change.
**How:** Animate layout changes (FLIP or a layout-animation library).
**Topic:** motion

### Prevent Layout Shift from Font Weight Change
`Motion` · product not named · https://detail.design/detail/prevent-layout-shift-from-font-weight-change
**Rule:** When an active or hover state makes text bolder, reserve the bold width so neighbors do not jump.
**Why:** Heavier weights are wider and shift the layout.
**How:** Add `::after { content: attr(data-text); font-weight: 600; height: 0; visibility: hidden; display: block; overflow: hidden }` on the label.
**Topic:** typography

### Reduce Edge Blur While Scrolling
`Motion` · product not named · https://detail.design/detail/reduce-edge-blur-while-scrolling
**Rule:** Lower backdrop blur radius while the user scrolls fast and restore it after scrolling settles.
**Why:** Heavy blur during movement hurts smoothness and GPU load.
**How:** On scroll set a small blur, debounce ~120ms, then restore the larger blur.
**Topic:** motion

### Screen Shaking Feedback
`Motion` · product not named · https://detail.design/detail/screen-shaking-feedback
**Rule:** Use a brief shake to signal a dead end or rejected action.
**Why:** It communicates "not possible" without a modal. (Page has no note; inferred from the title.)
**How:** Minimal; short horizontal keyframe shake, honoring `prefers-reduced-motion`.
**Topic:** motion

### Self-Explanatory Load Bar
`Motion` · product not named · https://detail.design/detail/self-explanatory-load-bar
**Rule:** Use restrained motion to explain a control's behavior, such as a load bar that visibly triggers a switch.
**Why:** Motion should clarify intent and give spatial context, not decorate.
**How:** Minimal.
**Topic:** motion

### Shake Disabled Button while Clicking
`Motion` · product not named · https://detail.design/detail/shake-disabled-button-while-clicking
**Rule:** Give a small shake when the user clicks a disabled button.
**Why:** It shows the click registered but the action is unavailable. (Inferred from title.)
**How:** Minimal; also explain why it is disabled.
**Topic:** motion

### Smooth Highlight Block Transition
`Motion` · product not named · https://detail.design/detail/smooth-highlight-block-transition
**Rule:** Animate a single highlight block moving between items instead of toggling each item's highlight.
**Why:** Continuous movement preserves spatial orientation. (Inferred from title.)
**How:** Minimal.
**Topic:** motion

### Staggered Animation for Event Order
`Motion` · product not named · https://detail.design/detail/stagger-for-the-event-order
**Rule:** When several elements move together, offset their start times to define an order.
**Why:** Simultaneous motion splits attention; a stagger tells the eye where to look next.
**How:** Minimal.
**Topic:** motion

### Tooltip in a Group
`Motion` · product not named · https://detail.design/detail/tooltip-in-a-group
**Rule:** When moving between adjacent tooltips, transition from one to the next instead of closing and reopening.
**Why:** Continuity feels smoother and skips repeated open delays.
**How:** Minimal; share a provider with a skip-delay (Radix `skipDelayDuration`).
**Topic:** motion

### Visibility Based Active Items in ToC
`Motion` · product not named · https://detail.design/detail/vibility-baesd-active-items-in-toc
**Rule:** Highlight table-of-contents entries for every section currently visible, not just the one anchor passed.
**Why:** Multiple highlights turn the ToC into a minimap of the viewport.
**How:** `IntersectionObserver` per section toggling `aria-current`/active state; move the highlight bar smoothly.
**Topic:** interaction
