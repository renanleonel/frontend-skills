Color: palette structure, token naming, formats (OKLCH, P3), contrast numbers, dark mode, gradients and how color is deployed. Read before building or changing any palette, theme token, or colored element.

## Ground rules

**Match the project's notation and tokens.** A second representation added to fix one value makes the palette harder to reason about; hex everywhere beats hex with stray `oklch()`. Only convert formats when asked or when a migration is the task.

**Measure, never estimate.** Color has exact answers. Compute contrast and lightness with a library (`culori`, `colorjs.io`, `chroma.js`); do not eyeball ramps or quote contrast you did not measure.

**Report failing pairs, don't silently repaint.** State the pair, measured value and threshold missed. Change colors only when asked, then remeasure.

**One palette per project.** Do not mix warm and cool grays; a warm border on a cool background is visible even when neither is nameable.

## System structure

**Build ramps, not one-off colors.** One neutral ramp, one accent ramp, and only the status ramps the product renders (`danger`, `warning`, `success`, `info`). An unused ramp is maintenance for zero pixels. A second accent hue is justified only when two things must be told apart at a glance.

**Give every ramp step a job.** Generate only steps a role consumes:

| Role | Tailwind | Radix |
| --- | --- | --- |
| Page background | 50 | 1 |
| Subtle background | 50 | 2 |
| Component bg / hover / active | 100 / 200 / 200 | 3 / 4 / 5 |
| Subtle border / border / strong border + focus ring | 200 / 300 / 400 | 6 / 7 / 8 |
| Solid fill / solid hover | 500 / 600 | 9 / 10 |
| Low-contrast text / high-contrast text | 700 / 900 | 11 / 12 |

Radix steps are defined by role (step 9 is the solid fill in light and dark); Tailwind steps are defined by lightness and invert in dark mode. Match what the project uses. For a new system prefer role-defined steps. On Tailwind keep `50`-`950` and put the role mapping in the semantic tier. Tailwind has 11 steps for 12 roles, so subtle border and hover collide; use 12 steps if they must differ.

**Neutrals carry 80-90% of the UI, so give them the most steps** (never fewer than the accent). Pure gray is a safe default. Tinting toward the accent hue is a style choice: a few percent of chroma, enough to measure, not enough to name. Warm hue reads editorial/approachable, cool reads technical.

**Status colors:** red danger, amber warning, green success by convention. Keep each distinct from the accent (brand red means danger moves to crimson; check side by side or destructive and primary are the same button). Status ramps need only four roles: background, border, solid, text.

**Max one accent color per page; lock it.** Once chosen, it is used everywhere (no teal badge in the footer of a rose site). Keep saturation moderate; desaturate accents so they sit with neutrals. Avoid neon outer glows and the default purple-to-blue AI gradient unless the brand is that color.

## Tokens and naming

**Two tiers: primitives name a value, semantics name a job.** Primitives (`--blue-500`, `--neutral-200`) are never used in components. Semantics (`--color-text-secondary`) point at primitives and are the only tier components reference. Dark mode, white-label themes and increased-contrast all repoint the semantic tier, leaving components untouched. Add a third component tier (`--color-button-danger-bg`) only for deliberate exceptions; twenty of them means semantic roles are missing.

**Cover the full role inventory up front:**

| Group | Roles |
| --- | --- |
| Surfaces | page bg, surface, raised (menus, popovers), sunken (inputs, wells), overlay scrim |
| Text | primary, secondary, disabled, inverse, on-accent |
| Borders | subtle, default, strong, focus ring, separator |
| Accent | subtle bg, border, solid, solid hover, text |
| Status | per status shipped: subtle bg, border, solid, text |

Separator (divides content) and border (encloses a control) are separate roles even if equal today.

**Use one grammar: `--color-{role}-{variant}-{state}`** (`--color-bg-surface`, `--color-accent-solid-hover`). One word per concept: `text` (not fg/ink), `bg` (not fill), `border` (not stroke/line), `accent` for brand. Reserve `primary` for "most prominent of its group" so `--color-primary` and `--color-text-primary` never collide.

**Bad names:** appearance at the semantic tier (`--color-blue-button`), first-use names (`--color-sidebar-gray`), lies in dark mode (`--color-light-gray`), numbered semantics (`--color-text-2`), hue mixed with state (`--color-gray-hover`).

**Use a token only in its role.** Never borrow a separator color for text or a text color for a background because the value fits today; when borders lighten, the text goes with them. No token for the role? Add one.

**Tailwind v4:** declare primitives and semantics in `@theme` (`--color-*` generates `bg-*`, `text-*`, `border-*`). Templates use semantic utilities (`bg-accent-solid`); a raw `bg-brand-500` in a component is the thing to flag. In shadcn-style setups, theme via the `--background`/`--foreground`/`--primary` variable pairs and keep raw palette classes out of components.

**Avoid alpha tokens under text.** `bg-accent/50` cannot be contrast-checked against a static background. Use solid tokens wherever text sits on top.

## Formats and gamut

| Notation | Use | Weakness |
| --- | --- | --- |
| Hex | Universal, what design tools export | Opaque, nothing editable by hand |
| `rgb()` | Same reach, readable alpha | Channels mean nothing to designers |
| `hsl()` | Looks like design controls | Lightness is not perceptual; hue drifts; ramps bunch |
| `oklch()` | Even lightness, stable hue, predictable ramps | Baseline 2023 |

**Default to `oklch(L C H)` for a brand-new system.** L 0-1, C 0 to ~0.4, hue 0-360, alpha after a slash (`oklch(0 0 0 / 0.1)`). Ramps stay even and fixed-hue stay fixed.

**Keep out-of-gamut colors from clipping.** Clipping flattens neighboring steps into one color. Cyans max out far lower than reds and purples, so a ramp can clip at some steps only. Lower chroma, holding L and H. Generate against sRGB, then enhance with P3 and always declare the sRGB value first:

```css
.accent { background: #3b82f6; }
@media (color-gamut: p3) { .accent { background: oklch(0.62 0.24 259); } }
```

A P3-only color with no sRGB fallback does not degrade, it fails. Use `@supports (color: oklch(0 0 0))` layering only if the browser matrix predates `oklch()` support.

**Computed color functions** (`color-mix()`, relative color `oklch(from var(--x) calc(l - 0.1) c h)`, opacity modifiers) resolve at render time. Handy for states; keep them out of the token layer and measure the rendered result. Do not chain three derivations in one token.

## Building a ramp

**Hold hue, step evenly in perceived lightness.** A well-formed ramp:
- Steps even in perceived lightness (OKLCH L or Lab), not HSL L.
- Constant hue end to end.
- Chroma peaks mid-ramp and falls toward both ends (a full-chroma 50 glows; a full-chroma 950 looks like spilled ink).
- Denser steps at the light end (50-200 close, 800-950 spread) so 50 and 100 read as two surfaces.
- Neither end touches pure black or white.
- No two adjacent steps visually identical; if 200 and 300 match, drop one.

**Interpolate ramps perceptually.** sRGB interpolation gives muddy mid-steps.

```js
import { formatHex, interpolate, samples } from 'culori'
const ramp = interpolate(['#eff6ff', '#3b82f6', '#172554'], 'lab')
const steps = samples(11).map((t) => formatHex(ramp(t)))
```

**Place the brand color on the solid-fill step** (500 / 9) so `bg-brand-500` is the real brand. Pin it if contractually fixed (ramp builds outward; one step spaces unevenly); otherwise snap it to the ramp. If it fails contrast under white text, it is still the brand color; use a darker step for interactive fills and never quietly darken the brand.

**Match ramps across hues by proportion, not number.** `danger-500` and `brand-500` should read equally bright. Match perceived lightness exactly; match chroma as a fraction of each hue's own maximum. Copying one chroma number across hues washes out yellows and cyans.

## Contrast

**Measure against the background the element actually renders on** (nearest painting ancestor, the card, not the page). Check every pair in every theme and in hover/disabled/selected states.

| Content | WCAG 2 AA | APCA minimum / preferred |
| --- | --- | --- |
| Body text | 4.5:1 (AAA 7:1) | Lc 75 / Lc 90 |
| Non-body text (labels, headlines) | 4.5:1 | Lc 60 / Lc 75 |
| Large text (>=24px, or >=18.5px bold; APCA >=36px) | 3:1 (AAA 4.5:1) | Lc 45 / Lc 60 |
| UI components, icons, focus indicators | 3:1 | Lc 30 |
| Disabled / placeholder | no WCAG requirement (placeholders still count as text, so aim for 4.5:1) | Lc 30 |

Use WCAG 2 as the gate when claiming conformance; use APCA as the tiebreaker for design decisions. Lc is signed (negative = light on dark); compare the absolute value. APCA is polarity-aware, so a pair that passes in light mode can fail mirrored in dark.

**Fix contrast with lightness, not hue.** Move the foreground away from the background in perceived lightness, holding hue and chroma, then remeasure. Mid-tone backgrounds (~75% perceived lightness) cap even black text near Lc 60; the background has to move. Pushing lightness can leave the gamut, so reduce chroma.

**Light-or-dark text crossover is ~73% perceived lightness.** Above it use dark text; below it white text scores better, including at 60-73% where the background already looks light.

**Special cases:**
- Translucent surfaces (`backdrop-filter` headers, overlays): test against the lightest and darkest content that can scroll behind, or make the surface opaque enough.
- Text over images or gradients: no single background. Measure the worst region or add a scrim. Keep text off gradients where you can.
- On colored surfaces, derive secondary text from the surface hue or the foreground, not generic gray.
- Increased contrast (`prefers-contrast: more`): widen the foreground/background gap by at least 15 points of perceived lightness, then re-verify against Lc 90 body / Lc 75 non-body.
- Color is never the only signal; pair with icon, label, shape, or position (see accessibility.md).

## Dark mode

**Do not just reverse the light palette.** Swap semantic roles first, then tune by hand:

```css
:root { --color-bg: var(--brand-50);  --color-text: var(--brand-950); }
.dark { --color-bg: var(--brand-950); --color-text: var(--brand-50); }
```

- **Lower chroma.** An accent confident on white looks neon on near-black; drop it a step or two.
- **Widen the dark end.** Steps distinct as pale backgrounds collapse as dark surfaces, so give elevation levels clear separation (lighter surface = higher elevation).
- **Recheck every pair.** Contrast does not survive mirroring.
- **Avoid pure `#000` and `#fff`** for page surfaces and text; use off-black (zinc-950-ish) and off-white. Pure values flatten depth. Keep the brand recognizable; do not desaturate it into gray.
- **Hierarchy parity.** A CTA that pops in light must pop in dark.

**Pick one switching mechanism and use it everywhere.**
- `prefers-color-scheme` alone: no toggle, nothing to persist.
- `.dark` class / `data-theme`: required once users can override the system setting; the media query then only sets the initial value.
- `light-dark()`: both values in one declaration; needs `color-scheme: light dark`, and a class-based toggle must also set `color-scheme`.
Mixing (media query for some tokens, class for others) half-themes the page the moment a user overrides.

**Lock the theme per page.** A dark page stays dark in every section; no light-paper band mid-scroll. Tinted section backgrounds inside one theme family are fine (`zinc-950` beside `zinc-900`). Exception: one deliberate full theme switch.

**Choose light or dark from the use scene** (who, where, ambient light), not from the product category.

Theme-toggle transition suppression is motion-adjacent: see `frontend-motion-design`.

## Using color

**One color, one meaning.** Treat anything within ~15 degrees of hue as the same color. If the accent means interactive, accent-colored static text reads as a link, and an interactive element rendered neutral misleads just as much.

```css
a { color: var(--color-accent-text); }
.section-title { color: var(--color-text-primary); }
```

**Fill exactly one action per view.** The primary action gets the solid accent background; peers stay neutral. Put the color on the background, not the label (accent text on a neutral button reads as a link). Distinct states or categories may use several colored fills. Selected tabs and checked segments may use accent on glyph and label; that is state, not emphasis. Preserve an established hierarchy that signals emphasis another way instead of recoloring.

**Make color earn its place.** Every color needs a stable role (hierarchy, state, meaning) or a deliberate atmospheric purpose tied to the visual direction. The strongest color owns a deliberate region or role; do not scatter tiny accents. Dots, badges and tints with no semantic state are decoration (see anti-slop.md).

**Calibrate by mode.** Operate/read surfaces: color encodes action, selection, status and wayfinding, and rarity gives the accent force. Marketing/experience surfaces: color may carry the voice and own large regions.

**Check culture for load-bearing color.** Red/green gain-loss flips in Chinese financial UIs (red = gain); white signals mourning in parts of East Asia. If the product ships to such markets, make gain/loss per-locale tokens.

**Theme the browser-owned surfaces.** Text selection (`::selection`), caret (`caret-color`), scrollbars, focus rings and `accent-color` default to colors no one chose. Set them from the palette.

## Gradients

**Pick the interpolation space deliberately; it is a look, not correctness.**

```css
background: linear-gradient(in oklab, #3b82f6, #ec4899);   /* even brightness, best default */
background: linear-gradient(in oklch, #3b82f6, #ec4899);   /* vivid, sweeps hues between stops */
background: linear-gradient(#3b82f6, #ec4899);             /* sRGB: darker, muted midpoint */
```

- Rectangular spaces (sRGB, oklab) interpolate in a straight line; two opposite hues pass near gray and the middle goes lifeless. Switch to a polar space (`in oklch`) or add a middle stop.
- Polar spaces take a hue path: `shorter hue` (default, usually right) or `longer hue` (sweeps most of the spectrum).
- Blue-to-pink in `oklch` routes through purple. That is either the look or a surprise.
- **Banding:** large low-contrast gradients step on 8-bit displays. Widen the contrast, shrink the area, or overlay subtle noise.
- **No gradient text** for large headings; emphasis comes from weight or size.
- Mesh/aurora gradients are layered radial gradients or SVG; no library needed.

## Auditing an existing palette

Before restructuring, inventory and report; consolidation changes rendered output across screens nobody asked about, so propose first.

1. Grep every literal: hex, `rgb(`, `hsl(`, `oklch(`, utility-class prefixes, SVG `fill`/`stroke`, chart configs, email templates.
2. Sort by perceived lightness within each hue family; near-duplicates surface as neighbors.
3. Collapse colors closer than ~one ramp step (keep the most used; never average).
4. Assign each survivor a role from the tables above. A color with no role is a missing token or a mistake; say which.
5. More than one ramp per role means the palette outgrew its structure.

## Extracting tokens into a design system

**Extract only what repeats.** A value or pattern used 3+ times with the same intent becomes a token or component; premature abstraction costs more than duplication. Two things that look alike but differ in intent stay separate. If no design system exists, ask where it should live before creating one.

**Find hard-coded values first:** grep for colors, spacing, type combos, shadows and radii in CSS variables, `tailwind.config`/`@theme`, CSS-in-JS themes, token JSON files and component variants. Sample computed styles from the rendered page when tokens miss values.

**Tokens need semantic meaning.** Do not tokenize every value. Name primitive vs semantic as above, document when to use each, then migrate every instance, test visual parity and delete the old code.

**When documenting the system (e.g. a `DESIGN.md`):** keep machine-readable tokens (colors, typography, rounded, spacing, components) in one place and prose as context only; never restate a token with a different value in prose. Group colors by role (primary, secondary, neutral), describe where and why each is used with the exact value alongside, omit sections the project does not have, and do not invent components or tokens. Non-token details (shadows, focus rings, motion, breakpoints) go in a sidecar. Never overwrite an existing doc without asking.

## Review checklist

| Violation | Fix |
| --- | --- |
| Raw value where a token exists | Reuse or add the role token in project notation |
| Primitive used in a component | Point a semantic token at it |
| Token named by look or first use | Rename by role |
| Semantic token used outside its role | Add the missing role token |
| Ramp built by varying HSL lightness | Rebuild in perceived lightness, constant hue |
| Same chroma number reused across hues | Match proportion of each hue's max |
| Status hue collides with accent | Move it until they read apart side by side |
| Dark mode = reversed light palette | Lower chroma, widen dark end, recheck pairs |
| Media query and `.dark` class both set tokens | Pick one mechanism |
| Contrast "fixed" by changing hue | Change lightness |
| P3 color with no sRGB fallback | sRGB first, P3 inside `@media (color-gamut: p3)` |
| Several solid-accent buttons side by side | One primary, others neutral |

Severity: HIGH = unreadable content or a misleading semantic color; MEDIUM = visible theme, token or gamut failure; LOW = isolated polish.
