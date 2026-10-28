Covers every interactive state, forms, hit areas, overlays, keyboard behavior, navigation and feedback. Read when building or reviewing anything a user can click, type into, open or wait on. Semantics/ARIA/screen-reader detail is in `accessibility.md`; motion is in `frontend-motion-design`.

## State checklist

**Define every state a control can be in before calling it done.** Missing states are the most common gap. Walk: default, hover, focus-visible, active, disabled, loading, selected/checked, error, success, empty.
Check: a component with `hover:` styles but no `focus-visible:` or `disabled:` styles.

**Hover is a bonus, never the only path.** Touch has no hover, and `:hover` latches after a tap. Gate hover styling with `@media (hover: hover)` (Tailwind 4 `hover:` already does). Never hide essential actions behind hover; show them always, or on focus-within too.

**Give pressable things instant `:active` feedback.** A `scale(0.96)`-`0.98` (or 1px translate) on press tells the user the click registered. Never go below `0.95`. Offer an opt-out on controls where it distracts (large cards, dense rows). Feedback must also have a static cue (color, icon, label); motion is never the only channel.
```tsx
<button className="active:scale-[0.97] transition-transform">Save</button>
```

**Style `:focus-visible`, not `:focus`.** Keyboard users get a ring, mouse users don't. Never `outline: none` without a replacement. Ring recipes: `accessibility.md`.

**Use semantic color + icon/text for status, never color alone.** Selected, error and success states need a second cue. Icons stay one `currentColor` SVG; states come from CSS color/opacity, outline = default, fill = active/selected.

**Keep disabled controls legible and explain them.** Native `disabled` for truly unavailable controls (leaves tab order, kills pointer events). A tooltip on a natively disabled control never opens for keyboard/touch, so put the reason in visible text beside it, or use `aria-disabled` (stays focusable; you must block activation in code). Never set both on one element. Cursor: `not-allowed` is optional; `default` is fine.

**Never disable submit until the form is valid.** Users can't discover why. Keep it enabled, validate on submit, focus the first error. Disable only once the request starts.

**Don't use custom cursors.** Hostile to accessibility and performance. Keep `cursor: pointer` for links/buttons only if the design system already does; never on non-interactive things.

## Loading

**Show structure-matching skeletons for content, spinners for actions.** Skeleton mirrors the final layout's shape so nothing jumps when data lands. Generic full-page spinners are a last resort. Reserve space (fixed aspect-ratio, min-height) to prevent layout shift.

**Name what is loading.** "Loading your projects..." beats a bare spinner. For long operations (>~10s) show progress or an estimate. Initial load, pagination, and refresh are three different states; design each.

**A busy button keeps its label.** Disable it, show a spinner beside the original text ("Save" + spinner), keep width stable. A bare spinner hides which button is busy.

**Avoid flash of loading.** If a request usually returns <~200ms, delay showing the skeleton/spinner (or keep it visible a minimum ~300ms once shown) so it doesn't flicker.

**Prevent double submission.** Disable or guard the handler while pending (also guard against Enter + click). Handle races: ignore stale responses, abort in-flight requests on unmount or new input.

**Use optimistic updates for low-risk, high-frequency actions** (toggle, like, reorder). Roll back and tell the user on failure. Not for payments or destructive actions.

**Debounce search-as-you-type (~300ms), throttle scroll/resize (~100ms).** Never use scroll listeners in React state; use IntersectionObserver, CSS scroll-driven features or a library.

## Empty states

**Treat every empty state as a first-use moment.** Never blank space. Include: what will appear here, why it's useful, one clear primary action (and optionally a template/import/example), and a small visual (icon or illustration, not a wall of text).
```
No projects yet
Projects keep your work and teammates in one place.
[Create project]  Start from template
```

**Pick the variant that matches the cause:**
- First use: emphasize value, offer a template.
- User cleared it: light touch, easy to recreate, maybe undo.
- No results (search/filter): echo the query, suggest broadening, offer "Clear filters".
- No permission: say why and how to request access.
- Load error: say what failed and offer retry (an error state, not an empty one).

**Don't show empty-state chrome while loading.** Skeleton first, empty state only after a confirmed empty response.

## Forms and inputs

**Every input has a visible `<label>`; placeholder is never the label.** Placeholder vanishes on typing and fails contrast. Label above the input, helper text optional (present in markup), error text below, consistent gap (~8px). A placeholder may show an example format in addition.
Check: `<input placeholder=...>` with no `<label>`/`aria-label`.

**One label = one hit target with its control.** Wrap or use `for`/`id`; no dead zone between checkbox and text.

**Pick the right `type`, `inputmode` and `autocomplete`.** It summons the right keyboard and enables autofill.
| Input | Use |
| --- | --- |
| Email / URL / phone | `type="email"` / `url` / `tel` |
| OTP, PIN, card number | `type="text" inputmode="numeric"` |
| Money, decimals | `type="text" inputmode="decimal"` |
| True quantity | `type="number"` (no scroll-wheel changes; avoid for IDs) |
| Name, address, card | `autocomplete="name"`, `street-address`, `postal-code`, `cc-number`, `cc-exp`, `cc-csc` |
| Login | `username`, `current-password`; signup/reset: `new-password`; 2FA: `one-time-code` |
`spellcheck="false"` on emails, codes, usernames. Use a section prefix when needed (`shipping postal-code`).

**Use at least 16px text in inputs.** iOS Safari force-zooms focused inputs below 16px. Never fix it by disabling zoom.

**Never fight the user's tools.** Allow paste everywhere (passwords, OTP). Keep real `<form>` elements so password managers and autofill work. No fake inputs, no blocking `onPaste`.

**Accept free text, validate after.** Don't filter characters or block typing; show a constraint hint instead. Trim whitespace before validating. Mark required via native `required` plus a visible marker explained once ("* required"). Set sensible `maxLength`/`pattern` hints, but validate on the server too, always.

**Validate on submit first, then on blur, then live once an error exists.** Don't scream at a field on the first keystroke. Once a field is invalid, re-validate as the user types so the error clears immediately.

**Show errors inline, specific, and recoverable.** Next to the field with an icon or text (never just a red border), saying what's wrong and how to fix it. Preserve everything the user typed. On submit failure, focus the first invalid field and scroll it into view below any sticky header. Wiring (`aria-invalid`, `aria-describedby`): `accessibility.md`.
- Bad: "Invalid input". Good: "Password needs at least 8 characters".
- Form-level failure (network, server): a banner at the top of the form, not a toast.

**Enter submits; in `<textarea>` Enter adds a newline and Cmd/Ctrl+Enter submits.** Show the shortcut hint near the button when it exists.

**Warn before losing work.** Unsaved changes + navigation/close = confirm (`beforeunload` and in-app route guard), or better, autosave drafts. Hydration and re-renders must never wipe typed input or drop focus.

**Group long forms; ask less.** Collect only what's needed now, explain why for sensitive fields (phone, birthday), use smart defaults, split long flows into steps with "Step 2 of 4" and let users go back without losing data.

**Choose the control by option count.** 2 options: toggle/radio/segmented. 3-7: radio group or select. 8+: searchable select/combobox. Many: async combobox with debounce. Checkbox = value submitted on save; switch = takes effect immediately. Don't mix the two semantics.

**Destructive and primary buttons are visually distinct and spaced apart.** Cancel is secondary/ghost; primary is the single most likely action. Order consistently across the product (don't flip Save/Cancel per dialog).

## Hit areas and touch

**Targets: 44x44px touch, 40x40px dense desktop; 24x24px is the WCAG 2.5.8 AA floor.** Visible size can be smaller; the clickable area is what counts. Everything that looks clickable must be clickable across its whole visual extent.

**Extend small targets with a pseudo-element on the wrapper**, not on replaced elements (`<input>`, `<img>`), which don't render `::before/::after` reliably.
```tsx
<button className="relative size-5 after:absolute after:top-1/2 after:left-1/2 after:size-11 after:-translate-1/2">
  <CheckIcon />
</button>
```
Or give real box size: `min-w-11 min-h-11 inline-grid place-items-center`.

**Two targets never overlap.** Where an extended area would collide, shrink it to the largest non-colliding size. Undersized targets pass the spacing exception if a 24px circle on each center touches no other target (20px targets need 4px gaps).

**Decorative layers must not eat clicks.** Scrims, glows, grain and full-bleed `::after` on top of controls get `pointer-events: none` (+ `aria-hidden`). A modal backdrop that dismisses on click is a control, so it keeps pointer events.
Check: a control that looks live and does nothing.

**Touch details:** `touch-action: manipulation` on controls (kills double-tap-zoom delay); `touch-action: none` only on custom pan/zoom/drag surfaces, never page-level; set `-webkit-tap-highlight-color` deliberately. Prefer big targets and clear affordances over tiny drag handles or precise hover zones. Ignore extra touch points once a drag starts.

## Keyboard

**Every pointer interaction needs a keyboard path.** Tab between widgets, arrows within composite widgets, Enter/Space activate, Escape dismisses the topmost layer. Full APG table: `accessibility.md`.

**Escape closes the last-opened layer only** (tooltip, then menu, then dialog), and returns focus to what opened it.

**Don't add animation to keyboard-initiated or very high-frequency actions** (command palette toggle, list navigation, shortcuts). They repeat hundreds of times a day and feel laggy. Instant response.

**Show shortcut hints where the action lives** (tooltip, menu item, placeholder like search box `Cmd K`). Never override browser/OS shortcuts (Cmd/Ctrl+F, +L, +T, +W); disable shortcuts while typing in inputs; document them in a `?` help.

**Make lists keyboard-navigable when they're primary content** (command palettes, tables with row actions): arrows move, Enter opens, type-ahead where natural.

## Overlays

**Pick the lightest overlay that fits.**
| Need | Use |
| --- | --- |
| Short label on hover/focus | Tooltip (never interactive content) |
| Rich or interactive content, anchored | Popover |
| List of actions | Dropdown menu |
| Pick a value | Select / combobox |
| Blocking decision or focused task | Modal dialog |
| Secondary panel, mobile-friendly task | Drawer / sheet |
| Passive result of an action | Toast |
Prefer inline UI (expand, undo) over a modal when the task doesn't need to block.

**Modals: native `<dialog>.showModal()` where possible.** It provides the focus trap, inert background and Escape. Otherwise `role="dialog"`, `aria-modal`, accessible name, `inert` on the rest. Initial focus on the first control, or the least-destructive button for confirmations. Return focus to the trigger on close. `overscroll-behavior: contain` so the page behind doesn't scroll. Lock body scroll without layout shift (`scrollbar-gutter: stable`).

**Always provide a visible close button plus Escape plus (for non-critical) backdrop click.** Don't close on backdrop click for forms with unsaved input or destructive confirmations. Modals stay centered; keep them under ~90vh with internal scroll; on mobile prefer a bottom sheet.

**Don't stack modals.** A modal opening a modal means the flow needs restructuring. Confirmation inside a modal is an inline step.

**Popovers and menus anchor to their trigger and flip/shift on collision.** Use a positioning library (Floating UI, Radix, Base UI), not hand-rolled math. Portal them to `body` to escape `overflow: hidden`; set the z-index from a documented scale, not arbitrary `z-[9999]`. Popovers scale from the trigger (transform-origin = anchor); modals from center.

**Tooltips: delay on first hover (~300-500ms), instant on the next adjacent one.** Show on keyboard focus too, dismiss on Escape and when the pointer leaves, and let hover move onto the tooltip body without closing. Never put essential info or actions only in a tooltip (touch has none).

**Menus: items are 36-40px tall min, with room for a disabled state and a submenu arrow.** Typeahead jumps to matches. Destructive items separated and styled distinctly, ideally last.

**Toasts: use for passive, non-blocking confirmation only.** One at a time or a small stack (cap ~3). Pause the timer on hover, focus and when the tab is hidden. Timer >=5s; anything with an action (Undo) or an error stays until dismissed. Never the only path to an action. Position consistently, away from primary actions, with swipe or close to dismiss. Never move focus into a toast.

## Feedback, confirmation and undo

**Every action gets visible feedback within ~100ms.** Pressed state instantly, then loading, then outcome. Silence feels broken.

**Prefer undo over confirm.** Reversible actions (archive, delete-to-trash, remove item) execute immediately with a toast "Deleted. Undo" lasting ~8-10s. It's faster and safer than "Are you sure?", which users click through by habit.

**Confirm only for irreversible or high-blast-radius actions**, and make the confirmation specific: title names the object ("Delete 'Q3 report'?"), body states the consequence, the confirm button repeats the verb ("Delete project", not "Yes"/"OK"), Cancel is the default focus. For the worst cases (delete account/workspace) require typing the name.

**Report outcomes at the right scale.** Field level: inline. Row/item level: inline status or small toast. Page level: banner. Don't toast validation errors and don't banner trivial saves.

**Success is quiet unless it's a milestone.** "Saved" is a toast or an inline "Saved just now"; reserve celebration for first success and rare moments.

**Handle failures by class** (copy: `copy.md`):
- Network/timeout/offline: explain, keep user data, retry button, auto-retry with backoff for background fetches, show offline indicator.
- 400 validation: map errors to fields. 401: send to sign-in and return after. 403: explain missing permission. 404: not-found state with a way home. 429: say to wait and for how long. 5xx: generic apology, retry, support link and a request id.
- One failing region must not block the whole screen. Contain with error boundaries per section, so the rest stays usable.

**Permission and read-only states are explicit.** Say why you can't edit and who can grant access; show the controls disabled with an explanation instead of silently removing them.

## Navigation and URL state

**Navigation is `<a href>`, actions are `<button>`.** Anything that changes the URL must be a real link: Cmd/Ctrl/middle-click, copy link, open in new tab, prefetch. A "button" that navigates is a styled link.

**Put shareable view state in the URL.** Filters, sort, search query, tab, pagination, selected item, open dialog that deserves a link. Use query params, debounce text input before writing, and replace instead of push for rapid changes (typing, slider) so Back isn't flooded.
```ts
router.replace(`?q=${encodeURIComponent(q)}`) // typing
router.push(`?tab=billing`)                   // discrete navigation
```

**Back must do what the user expects.** Closing a modal opened via URL should go back or clear its param; Back must not trap users in a redirect loop; restore scroll position on back/forward and scroll to top on new navigation. Don't push history entries for ephemeral UI (hover cards, accordions).

**Show where you are.** Current nav item has `aria-current="page"` and a visible active style that is not color-only. Breadcrumbs for depth >2. Page `<title>` updates per route, most specific first (`Billing · Settings · Acme`).

**Navigation stays predictable.** Same order and labels on every page; primary nav on one line at desktop (max ~80px tall, 64-72px typical); condense or collapse to a menu rather than wrap. Don't rename routes, anchors or primary labels during a redesign unless asked; they carry muscle memory and SEO.

**Use prefetching and instant transitions for perceived speed**, but keep link semantics intact. Pagination vs infinite scroll: pagination or "Load more" for content users must return to or reach the footer; infinite scroll only for feeds, with virtualization (don't render 10k rows) and preserved position on return.

**Tabs switch views, not pages.** Selected tab visible and exposed in the URL when the state is shareable. Long tab lists scroll horizontally with visible fade/arrows; don't wrap onto two rows.

## Onboarding and first run

**Get users to first value fast; don't teach everything.** Show the 20% that delivers 80%. Let experienced users skip; never block the product behind a tour. Real functionality with sample data beats a separate tutorial mode.

**Teach in context.** Prefer empty states, inline hints and first-use tooltips at the moment of need over upfront walkthroughs. Collect minimal account info first; explain why each item is asked; use smart defaults.

**Tours: 3-7 steps, skippable, replayable from help, workflow-focused** ("Create a project", not "This is the project button"). Spotlight the element but leave the UI interactive.

**Track dismissals and never repeat.** Persist "seen" per user (server-side when logged in; localStorage as fallback, wrapped in try/catch). Don't show the same tooltip or tour twice, and don't show first-run flows to returning users. New-feature announcements are dismissable and tryable immediately.

**Progressive disclosure keeps complexity gradual.** Unlock advanced options when needed; badge new/unused features sparingly. Show progress ("Step 2 of 3") in multi-step setup.

## Review checklist

- Every control: hover (gated), focus-visible, active, disabled, loading, error defined?
- Targets >= 44px touch / 40px desktop; no overlapping hit areas; decoratives `pointer-events-none`?
- Labels, types, `autocomplete`, paste allowed, submit never pre-disabled?
- Loading/empty/error/permission states exist for each data region; skeleton matches layout?
- Escape, focus return and background `inert` work for every overlay; no stacked modals?
- Destructive actions undoable or specifically confirmed?
- Shareable state in the URL; Back and scroll restoration behave?
