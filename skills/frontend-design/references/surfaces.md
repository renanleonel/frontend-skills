Surfaces and icons: border radius, borders vs shadows, elevation, image outlines, glass, optical alignment, and icon size/stroke/state/direction. Read when styling cards, buttons, containers, images or icons.

## Border radius

**Make nested radii concentric: outer radius = inner radius + padding.** Equal radii on nested surfaces is the most common cause of a UI that "feels off".

```tsx
// 8 (inner) + 8 (padding) = 16 (outer)
<div className="rounded-2xl p-2">
  <div className="rounded-lg">...</div>
</div>
```

Check: a child with the same `rounded-*` as a padded parent.

- Applies when layers share a visible, even inset. Past ~24px of padding treat them as separate surfaces and pick radii independently.
- Asymmetric padding or independent layers: keep the established component token.

**Use one radius scale per project and follow it everywhere.** Choose all-sharp (0), all-soft (12-16px), or all-pill for interactive controls. A mixed system needs a written rule ("buttons pill, cards 16px, inputs 8px") applied consistently. Pill buttons on square cards, or the reverse, reads as broken. Card radii stay 12-16px; pills are for small controls.

**Define radius as tokens** (`--radius-sm/md/lg`, or shadcn's `--radius`) and derive nested values from them, so concentric math survives a global change.

## Borders vs shadows

**Use layered transparent shadows for depth; keep borders for structure.** Shadows are translucent, so they adapt to any background, including images and varied fills, where a fixed border color fails.

| Shadow | Border |
| --- | --- |
| Cards and containers with depth | Dividers between list items |
| Bordered-style buttons | Table cell boundaries |
| Dropdowns, modals, elevated layers | Form input outlines (affordance + accessibility) |
| Elements over varied backgrounds | Hairline separators in dense UI |
| Hover/focus lift | Selected and focus states |

Never swap `border-t`/`border-b`/side dividers for shadows; their job is separation, not depth.

**Shadow-as-border, light mode.** Three layers: 1px ring, subtle lift, ambient depth.

```css
:root {
  --shadow-border:
    0 0 0 1px oklch(0 0 0 / 0.06),
    0 1px 2px -1px oklch(0 0 0 / 0.06),
    0 2px 4px 0 oklch(0 0 0 / 0.04);
  --shadow-border-hover:
    0 0 0 1px oklch(0 0 0 / 0.08),
    0 1px 2px -1px oklch(0 0 0 / 0.08),
    0 2px 4px 0 oklch(0 0 0 / 0.06);
}
```

**Dark mode: one white ring only.** Layered depth shadows vanish on dark surfaces. Apply through whatever theme mechanism the project uses:

```css
--shadow-border: 0 0 0 1px oklch(1 0 0 / 0.08);
--shadow-border-hover: 0 0 0 1px oklch(1 0 0 / 0.13);
```

```css
.card {
  box-shadow: var(--shadow-border);
  transition: box-shadow 150ms ease-out; /* list the property, never `all` */
}
.card:hover { box-shadow: var(--shadow-border-hover); }
```

**Declare elevation once: border or shadow, not both.** A 1px border under a wide soft shadow is the "ghost card". (If the ring is part of the shadow stack, you have not added a border.)

**Use cards only when elevation carries hierarchy.** Otherwise group with `border-t`, `divide-y` or whitespace. Same-size icon+heading+text cards as the page skeleton are the lazy container; nested cards are always wrong. In dense data views (high density), let metrics sit in plain layout rather than card boxes.

## Depth and elevation

**Give shadows an offset and a soft blur.** A zero-offset colored halo is decoration, not depth. Skip neon/outer glows by default; use inner borders or subtle tinted shadows. Hard offset block shadows (`4px 4px 0`) belong only to a deliberately neobrutalist world.

**Tint large soft shadows toward the background hue** instead of pure black on light backgrounds. The 1px ring layers above stay neutral black/white alpha, which already adapts to the surface.

**Raise surfaces by tone in dark mode.** Higher elevation = lighter surface (see color.md dark mode), with the ring for edges, since shadows barely show.

**Use a small, named shadow set.** One token per role (resting card, popover/menu, modal), with a stated use for each. Don't invent one-off shadow values per component.

**Never use a colored left/right border above 1px** as an accent stripe on cards, list items, callouts or alerts. Use a background tint, icon, or full border instead.

## Glass and blur

**Use glass for a specific reason, not as default decoration.** Suits premium-consumer or media-overlay surfaces; wrong for dashboards, public-sector and plain B2B. When used, go beyond `backdrop-blur`:

```tsx
<div className="backdrop-blur-xl bg-white/10 border border-white/10 shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]" />
```

- Add a 1px inner highlight border and a subtle inset shadow for a physical edge.
- Provide a solid fallback under `@media (prefers-reduced-transparency: reduce)`.
- Text on glass needs contrast measured against the worst content scrolling behind (see color.md).
- Do not call a CSS approximation "Apple Liquid Glass"; there is no official web package.

## Image outlines

**Give images a 1px inset outline at 10% opacity in pure black (light) or pure white (dark).** It separates the image edge from the surface with consistent depth.

```tsx
<img
  className="outline outline-1 -outline-offset-1 outline-black/10 dark:outline-white/10"
  src={src}
  alt={alt}
/>
```

```css
img { outline: 1px solid oklch(0 0 0 / 0.1); outline-offset: -1px; }
.dark img { outline-color: oklch(1 0 0 / 0.1); }
```

- **Never a tinted or near-black/white color** (slate-900, zinc-900, `#0a0a0a`, `#f5f5f7`) and never the accent. A tinted outline picks up the surface below and reads as dirt on the edge.
- **Use `outline`, not `border`:** it adds no width or height, and `-1px` offset draws it just inside so it follows the corner radius.

Check: `outline-slate-*`, `outline-zinc-*`, `outline-neutral-*`, or a border on `<img>`.

## Optical alignment

**Align optically when geometric centering looks off.** Trust the eye on icons, play triangles and carets.

- **Button with icon:** pad the icon side ~2px less than the text side (16px text side, 14px icon side). Use logical properties so it flips in RTL.

```tsx
<button className="ps-4 pe-3.5 flex items-center gap-2">
  <span>Continue</span><ArrowRightIcon />
</button>
```

- **Play triangles:** shift ~2px toward the point (`translate-x-0.5` on the glyph).
- **Asymmetric glyphs (stars, arrows, carets):** fix the SVG path/viewBox so every usage is centered. Fall back to a 1px translate on the wrapper only when you cannot edit the asset.

## Icons

### Choose and keep one set

**Use one icon library per project and one stroke weight per surface.** Mixed libraries have incompatible stroke and grid conventions. Use the project's existing set (shadcn defaults to Lucide; keep it if already present). In a new project prefer Phosphor, Tabler, Radix Icons or HugeIcons. Never hand-draw icon paths from scratch, and never use emoji or Unicode glyphs as icons. Standardize `strokeWidth` globally.

**Use an icon system for brands too.** Brand logos come from Simple Icons or devicon (`simple-icons` npm), and must render in light and dark (single-color via `currentColor` or a theme variable).

### Stroke, size, alignment

**Match icon stroke to the adjacent text weight.** A hairline icon beside semibold text looks broken; a heavy one beside regular text shouts.

| Adjacent text | Stroke (24px grid) |
| --- | --- |
| Regular 400, 14-16px | 1.5px |
| Medium/Semibold 500-600 | 2px |
| Bold 700 or emphasized standalone | 2.5px |

```tsx
<button className="flex items-center gap-2 font-semibold">
  <PlusIcon strokeWidth={2} className="size-4" /> New project
</button>
```

If the library lacks stroke variants, keep its native stroke and use size or color for emphasis.

**Size inline icons from the text:** `1em`-`1.25em` (cap height) so the pair scales together. Align with the text's centerline (`items-center`), not the baseline of a line box.

**Draw and test at render size.** An icon from a 48px design turns to mush at 16px.
- Check each icon at its smallest rendered size (often 16px).
- Prefer simplified glyphs for small contexts over scaled-down detail.
- Use the set's native grid sizes (16, 20, 24); fractional scaling renders soft.
- SVG only, never raster.

### State

**One SVG recolored per state.** Icons use `currentColor`; hover, selected and disabled come from CSS, never separate assets. Strip hardcoded `fill="#666"`/`stroke` when importing.

```html
<button class="text-zinc-500 hover:text-zinc-900 aria-pressed:text-blue-600 disabled:opacity-40">
  <BookmarkIcon />
</button>
```

In real code use semantic tokens (`text-muted-foreground hover:text-foreground`) rather than raw palette steps.

**Outline by default, filled for active.** Treat the two variants as a state pair: outline in toolbars, rows and inline text; fill for the active tab, toggled bookmark, liked heart. Filled icons everywhere remove the state signal.

```tsx
<TabIcon variant={isActive ? "solid" : "outline"} />
```

Animating the swap between variants: see `frontend-motion-design`.

**Icon-only controls and decorative icons:** accessible names and `aria-hidden` rules live in accessibility.md.

### RTL

**Flip only direction-dependent icons under `dir="rtl"`.**

| Flip | Do not flip |
| --- | --- |
| Back/forward arrows, navigation chevrons | Logos and brand marks |
| Alignment, list and indent glyphs | Checkmarks |
| Speaker/volume waves, "send" glyphs | Clocks, cups, pencils (physical objects) |
| | Media playback controls (tape convention stays LTR) |

```tsx
<ChevronRightIcon className="rtl:-scale-x-100" />
```

For composite icons, decide per part: a badge or slash overlay may keep its position while the base glyph flips.

## Visual polish of buttons and cards

- Buttons with an icon: apply the optical padding offset above; icon size `1em`-`1.25em`, stroke matched to label weight.
- Instant press feedback is an interaction state: `active:scale-[0.96]` (never below 0.95). Details of state coverage live in interaction.md; animation timing in `frontend-motion-design`.
- Card shell: concentric inner radius, one elevation method (ring shadow), tokenized radius, hover lift via ring shadow only on clickable cards. Static cards get no hover effect.
- Customize shadcn defaults: change radii, colors, shadows and typography to the project aesthetic rather than shipping the stock look.

## Browser-owned and decorative surfaces

- **Backgrounds are surfaces, textured only from the subject's world.** Stripe or grid overlays need a real canvas, map or blueprint metaphor underneath; otherwise skip them.
- **Skip fake-content decoration:** sparklines, progress rings or soft-shadowed rounded rectangles standing in for real content; filled progress tracks used as comparison visuals on landing pages (prefer a number plus a tiny trackless bar).
- **Bento/feature grids need variation:** at least a few cells with a real image, brand-appropriate gradient, pattern or tinted background, not a grid of identical white text cards.
- **No organic masks faked with geometry:** a circle or radial cutout approximating a photo subject's edge looks worse than omitting it. Use a real alpha matte or a cut-out asset.
- **Real illustration or none.** Sketchy SVG scenes imitating pictures read as amateur; crisp geometric vector, diagrams and shader effects are fine.

## Review checklist

| Violation | Fix |
| --- | --- |
| Same radius on parent and padded child | `outer = inner + padding` |
| Mixed radius scales with no rule | One scale, documented exceptions |
| Border used only to fake elevation | Layered translucent shadow; keep structural borders |
| Border plus wide shadow on one card | Declare elevation once |
| Colored side border stripe >1px | Tint, icon or full border |
| Tinted or solid-color image outline | `black/10` (light) and `white/10` (dark), inset |
| Equal padding beside an icon | 2px less on the icon side |
| Play/caret glyph looks off-center | Fix the SVG or nudge ~2px |
| Hairline icon beside bold text | Stroke 2px (semibold) / 2.5px (bold) |
| Two icon libraries on one surface | One set, one stroke |
| Separate icon assets per state | One `currentColor` SVG, states in CSS |
| Filled icons everywhere | Outline default, fill for active |
| Chevrons not flipped in RTL | `rtl:-scale-x-100` on directional icons only |
| Blur/glass with no fallback | Solid fill under `prefers-reduced-transparency` |

Severity: HIGH = state visible only through color or animation; MEDIUM = visible inconsistency in surfaces or icons; LOW = isolated polish.
