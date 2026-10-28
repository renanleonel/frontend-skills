Covers semantics and ARIA, accessible names, screen readers and live regions, focus management, keyboard patterns, zoom/reflow and user preferences. Read when building custom widgets, reviewing for a11y, or touching focus, labels or announcements. Contrast numbers are in `color.md`; hit-area sizes and form UX are in `interaction.md`; motion is in `frontend-motion-design`.

Review as two walks: keyboard-only (every flow completes without a mouse), then screen reader (every control announces name, role, state). When unsure, take the platform default over a custom rebuild, and remove ARIA rather than add it.

## Native elements first

**Use the native element; ARIA is the fallback.** Native gives keyboard, focus and semantics for free; a wrong role is worse than none (no ARIA beats bad ARIA).

| Element | For | Gets you |
| --- | --- | --- |
| `<a href>` | Navigation (changes URL) | Cmd/Ctrl/middle-click, copy link, Enter |
| `<button>` | Actions (submit, toggle, open, delete) | Focus, Enter and Space, form semantics |
| `<div onClick>` | Nothing | No role, focus or keyboard |

```tsx
<div onClick={open}>Settings</div>   // invisible to keyboard and AT
<button onClick={open}>Settings</button>
```
Check: `onClick` on `div`/`span`; `<a>` without `href`; a `<button>` that navigates. Last-resort polyfill is `role="button"` + `tabindex="0"` + Enter and Space handlers.

**Five rules of ARIA:** (1) native beats ARIA; (2) don't change native semantics; (3) every interactive ARIA role must be keyboard-operable with the full model (a role is a promise); (4) never `role="presentation"` or `aria-hidden` on a focusable element; (5) every interactive element has an accessible name.

**Common ARIA mistakes:**
| Mistake | Problem |
| --- | --- |
| `aria-label` on a role-less `div`/`span` | Mostly ignored |
| `<button role="button">` | Redundant noise |
| `aria-hidden` on/above focusable content | Tab stops that don't exist for AT |
| `aria-labelledby`/`describedby` to a missing id | Silently no name |
| `role="menu"` on site navigation | Promises app-menu arrow keys; use `<nav>` + list |

## Structure and landmarks

**Expose one visible `<main>`, and use `<header>`, `<nav>`, `<aside>`, `<footer>`.** Label duplicates: `<nav aria-label="Primary">`, `<nav aria-label="Breadcrumbs">`.

**Headings describe sections and form an outline.** One `<h1>`, nest without skipping. Choose the tag by structure and style the size with CSS. Treat skipped levels as a concrete finding only when they hurt navigation or comprehension, not as a standalone WCAG failure.

**Add a "Skip to content" link as the first focusable element** when repeated chrome precedes `<main id="main">`. Visually hidden until focused. Give anchor targets `scroll-margin-top` (e.g. 80px) under sticky headers.
```css
.skip-link { position: absolute; inset-inline-start: -999px; }
.skip-link:focus { inset-inline-start: 16px; top: 16px; }
```

**`<title>` matches the current view, most specific first:** `Billing · Settings · Acme`. Set `lang` on `<html>` (and `lang` on foreign-language inline content).

**Mark non-translatable tokens `translate="no"`** (brand names, code, identifiers).

## Accessible names

**Name precedence:** `aria-labelledby` > `aria-label` > native label (`<label>`, content, `alt`) > `title`. Prefer visible text or `aria-labelledby`; `aria-label` is invisible, drifts out of sync and skips translation.

**Icon-only controls get a name; the icon is hidden.**
```tsx
<button aria-label="Delete"><TrashIcon aria-hidden="true" /></button>
<button><TrashIcon aria-hidden="true" /> Delete</button>
```

**Visible label text must be inside the accessible name** (WCAG 2.5.3). A "Send" button with `aria-label="Submit message"` breaks voice control ("click Send").

**Names must exist even when the design hides labels.** Links must make sense out of context: avoid "Click here"/"Read more" without a unique name (add sr-only context).

**Every form control has a programmatic label** (`<label for>` or wrapper). Placeholder is not a label. Group related controls with `<fieldset><legend>`. Details and `autocomplete` (WCAG 1.3.5): `interaction.md`.

## Forms and errors

**Wire errors so they announce with the field.**
```html
<label for="email">Email</label>
<input id="email" type="email" autocomplete="email"
       aria-invalid="true" aria-describedby="email-error" />
<p id="email-error">Enter a valid email address.</p>
```
- `aria-invalid="true"` on the failing field, removed when fixed.
- Inline text/icon error, never a red border alone.
- On submit, focus the first invalid field (the focus move is the announcement).
- Form-level failures not tied to a field: `role="alert"` summary.
- Success: polite `role="status"`.
- Keep the busy submit button's label visible beside its spinner so AT knows which control is busy.

**Disabled controls:** native `disabled` for truly unavailable controls; `aria-disabled="true"` only when it must stay focusable (then block pointer, keyboard and submit in code, style it explicitly including forced-colors, and explain why nearby). Never both. Tooltips on natively disabled controls don't reach keyboard/touch users. Disabled controls are exempt from contrast minimums; keep them legible anyway.

## Screen readers and live regions

**Choose the announcement mechanism top-down; stop at the first match:**
1. Focus moves there anyway (modal opens, first invalid field): nothing extra.
2. Tied to a control (field error, char count): `aria-describedby`.
3. Non-urgent, untied (toast, "Saved", result count, loading): polite live region, `role="status"`.
4. Urgent, untied (form-level failure, session expiry): `role="alert"`.

**Default to polite.** Assertive interrupts what the user is reading; it is for errors only.

**Render the live region before you change its text.** Inserting a new polite region with content is announced unreliably. Keep an empty, stable `role="status"` container and update its text. Dynamically inserted `role="alert"` mostly works but varies; test on your target screen readers.
```tsx
<div role="status" className="sr-only">{statusMessage}</div>
```

**Keep messages short and self-contained** (`aria-atomic` re-reads the whole region). Loading: `aria-busy="true"` on the updating region, announce "Loading...", then the outcome ("12 results").

**Never move focus to a toast.** Announce it and leave focus where the user works. Toasts with actions/errors persist until dismissed.

**Visually hidden text uses `.sr-only`, never `display:none`/`visibility:hidden`** (which hide from AT too). Keep a 1px box (some SRs skip 0) and `white-space: nowrap`. Tailwind: `sr-only`; skip link reveal: `focus:not-sr-only`. Use for context like "Opens in new tab", table captions, hidden labels.

**`aria-hidden="true"` is for decorative icons and visual duplicates only.** Never on or above anything focusable; hiding interactive content means removing it from the tab order too.

**Alt text by purpose:**
| Purpose | Alt |
| --- | --- |
| Decorative / redundant with adjacent text | `alt=""` (present but empty) |
| Informative | The meaning it adds |
| Functional (image is link/button) | The action: `alt="Search"`, not "magnifying glass" |
| Image of text | The exact text (better: real text) |
| Complex (chart, diagram) | Short summary + full data in a table/text nearby |
A missing `alt` is worse than empty (SRs read the filename).

**SVG:** decorative `aria-hidden="true" focusable="false"`; meaningful `role="img"` + `aria-label` (or `<title>` + `aria-labelledby`); simplest is `<img src="x.svg" alt="...">`.

**Media:** prerecorded video needs captions, audio needs transcripts; never autoplay with sound; always render controls.

**Tables:** real `<table>` with `<th scope>` and `<caption>`; don't use tables for layout, and don't build grid UIs from divs without `role="grid"` semantics.

## Focus

**Show a focus indicator at every stop, styled on `:focus-visible`.** Never `outline: none` without a verified replacement. Prefer the browser default ring plus `outline-offset: 2px`; it adapts to forced-colors automatically.
```css
:focus-visible { outline-offset: 2px; }                       /* default ring */
:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 2px; } /* custom */
```
```tsx
<button className="focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--focus-ring)]" />
```

**A custom ring uses a project token (not bare `currentColor`) and is checked against every adjacent color it crosses** (fills, surfaces, images, hover/selected states), at least a 2px perimeter. Contrast ratios: `color.md`. In `forced-colors: active` keep the default adjustment or use a system color like `Highlight`; use `forced-color-adjust: none` only after verifying.

**Use `:focus-within` to light up a wrapper** (search box with an inner icon).

**`tabindex`:** `0` joins the tab order (custom widgets only); `-1` is programmatic focus (headings, containers, roving members); positive values never (fix DOM order).

**Composite widgets use roving tabindex.** Tabs, menus, toolbars, radio groups are one Tab stop: active item `tabindex=0`, the rest `-1`, arrows move both focus and the 0.
```tsx
<button role="tab" tabIndex={i === active ? 0 : -1} aria-selected={i === active} onKeyDown={arrowKeys} />
```

**Focus must never be lost or trapped by accident.** If the focused element unmounts (delete row, close panel), move focus to the nearest logical neighbor or container. Never leave it on `<body>`. Avoid auto-focus on page load except for the primary input of a focused task (search, dialog).

**Modals trap and restore focus.** Prefer native `<dialog>` + `showModal()` (gives the trap, inert background, Escape). Custom overlay: `role="dialog"`, `aria-modal="true"`, `aria-labelledby`, `inert` on background content. On open focus the first control (least-destructive action for destructive confirms); on close return focus to the trigger (or nearest container if gone); `overscroll-behavior: contain`.
```ts
app.inert = true; dialog.querySelector("[autofocus], button, input")?.focus();
// close
app.inert = false; trigger.focus();
```
A keyboard trap anywhere else (e.g. an embedded editor/widget you can't Tab out of) is a HIGH issue; always provide an exit and document it.

**SPA route changes:** update `document.title`, then move focus to the new view's `<h1>` (`tabindex="-1"`) or `<main>`; restore scroll on back/forward, top on forward navigation. Announce navigation if focus can't move.

## Keyboard patterns (ARIA APG)

Custom widgets must implement these; native elements already do.
| Widget | Keys |
| --- | --- |
| Dialog | Tab/Shift+Tab cycle inside; Escape closes |
| Tabs | Arrows move (wrap); Home/End first/last; Tab exits to panel |
| Menu button | Enter/Space/ArrowDown opens, focus first; ArrowUp opens, focus last; arrows move; Escape closes, refocus button |
| Disclosure / accordion | Header is `<button aria-expanded>`; Enter/Space toggle |
| Combobox | ArrowDown opens/moves; Enter accepts; Escape closes, focus back to input; typing filters |
| Listbox / radio group | Arrows move selection; one Tab stop |

- Escape dismisses the most recent layer first (tooltip, menu, dialog).
- Arrows move within a widget; Tab moves between widgets.
- Tabs: automatic activation when panels are instant, manual (Enter/Space) when switching is costly.
- Enter submits a form; in `<textarea>` Cmd/Ctrl+Enter submits.
- Expose state: `aria-expanded`, `aria-selected`, `aria-pressed`, `aria-current`, `aria-controls` where they apply and stay in sync.
- Custom shortcuts must be single-key-safe: allow remap/disable, or require a modifier (WCAG 2.1.4).
- Drag interactions need a non-drag alternative (buttons or keyboard reorder) (WCAG 2.5.7); pointer gestures like pinch/swipe need single-pointer equivalents.

## Zoom, reflow and sizing

**Support 200% text zoom and reflow at 320px width with no horizontal scroll** (WCAG 1.4.4, 1.4.10; equals 400% on a 1280px viewport). Genuinely 2D content (tables, maps, code blocks) scrolls inside its own container.

**Never block zoom.** No `user-scalable=no` or `maximum-scale=1` in the viewport meta.

**Use `min-height`, not `height`, on anything with text** so containers grow. Fixed heights are what break under zoom.

**Units:** if the codebase uses rem, size `font-size`, text container `max-width`, spacing meant to scale, and media-query breakpoints in `rem`/`em`, so larger user font settings trigger the compact layout; keep `px` for borders, outlines, hairlines, shadows. If the project is px- or Tailwind-scale based, stay consistent and don't mix systems.

**Line/paragraph/word spacing overrides must not clip content** (WCAG 1.4.12): no fixed-height containers or `overflow:hidden` on text. Orientation: don't lock to portrait/landscape. Content on hover/focus (tooltips) must be dismissible, hoverable and persistent (WCAG 1.4.13).

## Reduced motion and user preferences

**Make motion opt-in.** Wrap animation in `@media (prefers-reduced-motion: no-preference)`; Tailwind: `motion-safe:` / `motion-reduce:`.
```css
@media (prefers-reduced-motion: no-preference) {
  .card { transition: transform 200ms ease-out; }
}
```
Legacy-codebase fallback: a global `@media (prefers-reduced-motion: reduce)` that sets animation/transition durations to `0.01ms` (not `none`, so `animationend` still fires), iteration count 1 and `scroll-behavior: auto`.

**Reduce, don't eliminate.** Disable: parallax, autoplay video/GIF, looping decoration, large travel, auto-rotating carousels (start paused). Replace slides/scales with opacity crossfades, smooth scroll with instant jump. Keep: spinners, progress, instant state changes (hover color, focus ring), brief press feedback.

**Anything moving, blinking or auto-updating for >5s needs a visible pause/stop** (WCAG 2.2.2), including muted looping hero videos. Nothing autoplays with sound.

**Timed UI:** never put critical info or the only path to an action in a timed element (a vanished Undo toast is data loss). Auto-dismiss only for low-stakes confirmations, at least 5s, paused on hover/focus.

**Respect other preferences:** `prefers-color-scheme` (details: `color.md`), `forced-colors` (keep focus and borders visible; don't rely on background-color alone for state), `prefers-contrast: more`, `prefers-reduced-transparency` for blur/glass effects, `prefers-reduced-data` for heavy media. Test with Windows High Contrast.

**Don't rely on color alone** for status, links in text (underline), required fields, chart series or selected state; pair with icon, text or shape.

## Verification and reporting

**Without a browser:** accessible name on every interactive element, key handlers on non-native controls, focus styles, reduced-motion guards, labels bound to inputs, no `outline: none`, no positive tabindex, no `aria-hidden` on focusables. **With a browser:** tab the whole flow in order, read computed name/role from the accessibility tree, confirm a visible indicator at each stop, run an automated audit (axe/Lighthouse; they catch ~30-40% only), test with VoiceOver or NVDA. Report anything not run as `Not verified`.

**Severity:** HIGH prevents a task, hides content from AT, or is systemic. MEDIUM makes an interaction meaningfully harder. LOW is isolated polish. Block when any HIGH remains.

**Common misses:**
| Mistake | Fix |
| --- | --- |
| Custom focus color assumed fine | Check against every adjacent color + forced-colors |
| Repeated polite update not announced | Stable empty `role="status"`, update its text |
| `aria-live="assertive"` for routine toasts | `polite` |
| `aria-hidden` on a focusable element | Remove it, or make non-focusable |
| Submit disabled until valid | Keep enabled; validate on submit; focus first error |
| Hover style stuck after tap | `@media (hover: hover)` |
| Tooltip on natively disabled control | Visible text, or `aria-disabled` |
| Heading chosen by size | Pick by outline, style with CSS |
| Focus lost after deleting/unmounting | Move to neighbor/container |
