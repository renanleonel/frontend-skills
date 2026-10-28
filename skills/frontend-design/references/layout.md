Spacing, grouping, alignment, hierarchy, density, responsive layout, progressive disclosure and reading order. Read when building or fixing any page structure, or before touching margins and breakpoints.

## Diagnose before moving boxes

**Name the spatial thesis first.** Write down the primary task path, what belongs together, what leads vs supports, intended density, and how structure changes across viewports. Then pick the simplest structure that expresses it.

**Squint test.** Blur the screen mentally: primary element, secondary element and major groups must still be identifiable, in that order. If not, the problem is hierarchy, not decoration.

Check: every repeated card/column/section is genuinely equivalent content, not a framework default.

## Group with space, not lines

**Use negative space first, background shapes second, separator lines last.** Space is the cheapest grouping signal; lines and boxes add noise.
- Cards/filled containers: only where a group must read as one unit (selectable row, draggable item) or elevation encodes real hierarchy.
- Lines: dense data only (tables, long settings lists). Hairline, low contrast, one per boundary (not `border-t` + `border-b` on every row).

**Gap between groups >= 2x the gap inside a group.** 8px inside, 16px+ between, or the eye cannot find group edges.

```html
<div class="space-y-6">          <!-- between groups -->
  <div class="space-y-2">…</div> <!-- within group -->
  <div class="space-y-2">…</div>
</div>
```

**More space above a heading than below it.** The heading belongs to what follows. Check computed values, not intent.

**Use `gap` for sibling rhythm** instead of per-child margins; it expresses the relationship directly and survives reordering.

## Spacing scale and rhythm

**Use one documented spacing scale, never one-off values.** A 4px base gives the useful middle steps (4, 8, 12, 16, 24, 32, 48, 64) that an 8-only scale lacks. In Tailwind, stay on the default scale; no `mt-[13px]`.
Check: grep for arbitrary `[..px]` spacing and odd values (13, 22, 30).

**Build rhythm from contrast between tight and generous intervals.** One spacing value repeated everywhere gives everything equal weight and reads flat. Variation must carry meaning; repetition should aid recognition.

**One indent step per level of subordination** (16px is a good default); nested levels repeat the same step.

**Name reusable spacing/container roles semantically** (`--space-section`, `--gutter`) in the token layer.

## Density

**Match density to use frequency and task complexity.** Match the existing system before adding new values.

| Context | Spacing | Notes |
| --- | --- | --- |
| Marketing / airy | `py-24` to `py-48` between sections | Few elements, large gaps |
| Standard web app | `py-16` to `py-24` between sections, 16-24px inside cards | Default |
| Dense tool / data cockpit | 4-8px paddings, 1px dividers, no card boxes | Tabular/mono numerals (typography.md) |

Compact professional tools may sit below the clearances later in this file if hit areas stay distinct and never overlap (sizes: interaction.md). Do not inflate an established, usable density to match these numbers.

**Operate/read surfaces want predictable structure and stable density.** Persuade/portfolio surfaces may be asymmetric or disruptive when the concept earns it (anti-slop.md).

## Alignment

**Pick a few alignment edges and put everything on them.** The eye tracks straight edges; a stray edge reads as noise even when nobody can name it (icon 2px off the text edge, cards with different padding).

```css
/* Bad: three unrelated leading edges in one column */
.header { padding-inline-start: 20px } .item { padding-inline-start: 14px } .footer { padding-inline-start: 24px }
```

**Numbers align to the trailing edge, text to the leading edge** in tables (tabular figures: typography.md).

**Make optical corrections only after inspecting the render**; round-number alignment is not always optically aligned (icon/text pairs: surfaces.md).

**Use grid over flex percentage math.** `grid grid-cols-1 md:grid-cols-3 gap-6`, never `w-[calc(33%-1rem)]`.

## Logical properties for direction

**Use logical properties for anything direction-dependent** so layouts mirror under `dir="rtl"`. Physical only for truly physical geometry (notch, gesture direction).

| Avoid | Use | Tailwind |
| --- | --- | --- |
| `margin-left` | `margin-inline-start` | `ms-*` |
| `padding-right` | `padding-inline-end` | `pe-*` |
| `left: 0` | `inset-inline-start: 0` | `start-0` |
| `text-align: left` | `text-align: start` | `text-start` |
| `border-right` | `border-inline-end` | `border-e` |

Sequences that encode progression (steps, ratings, progress bars) mirror in RTL. Hand-positioned elements do not mirror automatically; flex/grid with logical props do. Digit order never reverses (bidi: typography.md).

## Reading order and hierarchy

**Most important content goes top and leading edge.** Reading flows top-to-bottom, leading-to-trailing; attention decays down and trailing. Within a row: identity first, metadata and actions trail.

**Never bury the one number the user came for.** Lead with the key fact, demote detail to secondary text, collapsed sections or detail views.

```html
<p class="text-2xl font-semibold">$4,320.00</p>
<p class="text-sm text-muted-foreground">Available balance</p>
```

**One primary action per view.** Group secondary actions in a menu once past two or three. The first screen is a table of contents: prefer a short view linking deeper over everything at level one. Color-enforced emphasis: color.md.

**Hierarchy comes from priority, not defaults.** Do not shout with raw scale; combine size, weight, space and tone (type roles: typography.md).

**DOM order and focus order must match visual order** at every breakpoint. `order-*` and grid placement can break this (accessibility.md).

## Keep controls distinct from content

**Give every interactive element a shape, border, underline or consistent control zone.** A control styled like adjacent static text is invisible; a non-clickable badge shaped like the buttons beside it collects dead clicks.

## Space between and around targets

Starting clearances when no density system exists:

| Between | Gap |
| --- | --- |
| Adjacent bordered/filled controls | 12px |
| Around borderless text/icon-only controls | 24px (nothing marks where a target ends) |
| Unrelated control groups | 24px+ (2x intra-group) |

Expanded hit areas must never overlap (hit-area sizes: interaction.md). Bad: three borderless icon buttons packed at `gap-1`.

## Edges, bleed and safe areas

**Inset buttons from viewport edges in content layouts**: about 16px inline margin on mobile plus bottom safe-area padding; the button can still span full content width with a visible radius. Edge-to-edge only when it is deliberate platform chrome that handles safe areas.

```css
.action-bar { padding-inline: 16px; padding-bottom: calc(16px + env(safe-area-inset-bottom)); }
```

**Content bleeds, controls float.** Backgrounds and hero media extend to viewport edges; text and controls stay within margins and safe areas. Full-bleed inside a constrained article:

```css
.article { display: grid; grid-template-columns: 1fr min(65ch, calc(100% - 48px)) 1fr; }
.article > * { grid-column: 2 }
.article > .full-bleed { grid-column: 1 / -1 }
```

**Enable safe areas**: `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`, then `env(safe-area-inset-*)`, with `max(1rem, env(...))` for fallbacks. Sticky headers and FABs add inset offsets too.

**Contain page width**: `max-w-7xl mx-auto` (or `max-w-[1400px]`); do not stretch to 4K. Nav bar height 64-72px, 80px max.

**Use `min-h-[100dvh]` for full-height sections, never `h-screen`** (iOS Safari address bar causes jumps).

## Responsive and adaptive layout

**Adaptation is rethinking, not scaling.** Decide per breakpoint what reorders, collapses, reflows, scrolls or stays fixed, based on what remains important.

**Write mobile-first.** Base styles for the narrowest case, layer complexity with `min-width` queries. `max-width` (desktop-first) ships unneeded styles to mobile.

**Breakpoints come from the content, not devices.** Stretch from narrow until the layout breaks, add a breakpoint there. Usually three suffice (Tailwind `sm 640`, `md 768`, `lg 1024`; `xl 1280`, `2xl 1536` if needed). Use `clamp()` for fluid values with no breakpoint.

**Collapse late.** Keep the expanded layout while it genuinely fits; premature collapse throws away space.

**Use container queries for components.** A card adapts to its column, not the viewport.

```css
.card-list { container-type: inline-size }
@container (max-width: 400px) { .card { grid-template-columns: 1fr } }
```

**Declare the mobile fallback per multi-column section, in the same component.** Asymmetric or offset layouts above `md` collapse to a strict single column below 768px (`w-full px-4 py-8`).

**Detect input, not screen size.** Laptops have touch; tablets have keyboards.

```css
@media (pointer: coarse) { .button { padding: 12px 20px } }
@media (hover: hover) { .card:hover { /* hover-only polish */ } }
```

Never make functionality hover-dependent; gate hover styling behind `(hover: hover)`.

**Per-context patterns**

| Target | Do |
| --- | --- |
| Phone | Single column, stacked, full-width components, thumb-reach controls (bottom sheets over dropdowns, bottom or compact nav), 16px text min, 44x44 targets |
| Tablet | 2 columns, side panels, master-detail, support touch and pointer, handle orientation |
| Desktop | Multi-column, persistent side nav, hover/shortcuts/context menus, more information upfront, `max-width` cap |
| Print | Page breaks at logical points, drop nav and interactive chrome, expand hidden content (full URLs), mono or limited color |

**Navigation in three stages**: hamburger/drawer (mobile), compact horizontal (tablet), full labels (desktop). Same information architecture across contexts; core functionality is never hidden on mobile.

**Tables to cards on mobile** using `display:block` and `data-label` attributes; `<details>/<summary>` for sections that collapse on small screens.

**Test landscape, 320px minimum width, very wide screens and 200% zoom.** DevTools emulation misses real touch, CPU limits, font rendering and browser chrome; check at least one real phone.

## Progressive disclosure needs an affordance

**Every hidden or off-screen item needs a visible cue.** Content with zero cue might as well not exist.
- **Peeking**: in horizontal scrollers, let the next item show 16-32px past the edge; container padding creates the peek, snap points stay on the content edge.
- **Disclosure controls** say what is hidden: "Show 12 more results", not "More".
- **Truncated text** shows an ellipsis plus a way to expand (typography.md).

```html
<div class="flex gap-3 overflow-x-auto px-6 snap-x snap-mandatory [scroll-padding-inline:1.5rem]">
  <div class="w-[80%] shrink-0 snap-start">…</div>
  <div class="w-[80%] shrink-0 snap-start">…</div>
</div>
```

## Plan for growth and clipping

**No fixed width or height on text containers.** Use `max-width`, wrapping and `min-height`. Translation grows short strings proportionally most, so a one-word button label is the riskiest element. Do not budget a percentage; test with pseudo-localization plus one long-string locale.

```css
.button { padding-inline: 16px; white-space: nowrap }   /* label sets the size */
/* Bad */ .button { width: 96px; overflow: hidden }
```

**Never park a critical action where it can be clipped**: bottom of a resizable pane, below the fold of a fixed-height modal, behind the keyboard. Keep it in normal flow or stable chrome (sticky footer with safe-area padding, top of view). In a scrolling modal, the action row does not scroll.

**Reserve space for images and embeds** (`aspect-ratio`) so layout does not shift. Other extremes (long content, empty states): edge-cases.md.

## Verify

- Squint test holds; task path clear at every supported width.
- Check narrow, intermediate, wide, 200% zoom and the RTL mirror.
- Related content groups naturally; no containers compensating for weak proximity.
- No stray spacing values or physical-direction properties remain.
- Without a browser, only logical props, query lists and DOM order can be checked; report the rest as not verified.

| Mistake | Fix |
| --- | --- |
| `ml-4` / `pr-6` in localizable UI | `ms-4` / `pe-6` |
| Breakpoints at 768/1024 "because defaults" | Break where content stops fitting |
| Viewport media query on a card in a sidebar | Container query |
| Fixed-width text container sized to English | `max-w` + wrapping |
| Primary action at clip-prone bottom of pane | Sticky/stable chrome with safe-area padding |
| Same gap inside and between groups, plus lines | Gap ratio >= 2x, drop the lines |
