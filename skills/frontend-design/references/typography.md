Font choice, type scale, line-height, measure, wrapping, truncation, numerals, OpenType/variable fonts, underlines, punctuation, input sizing. Read when picking fonts, setting text styles, or fixing text that wraps, shifts or clips.

## Fonts and pairing

**Use the product's existing type system unless asked to change it.** Never introduce a paid or proprietary face to satisfy a checklist; rendering details (smoothing, wrapping, tabular numbers) do not override the chosen family.

**Use as few families, sizes and weights as possible.** Rarely more than three families; every extra one needs a role only it can perform. Overuse of size and weight erodes hierarchy.

**Pair for contrast, not similarity.** Serif headline over sans body reads deliberate; two near-identical sans read as a mistake. Emphasize a word with italic or bold of the same family, never a random second family.

**Match category to job.**

| Category | Use |
| --- | --- |
| Sans | Default for interfaces |
| Serif | Long reading, editorial/luxury briefs that name it |
| Monospace | Code, data, measurement; not a costume for "technical" |
| Display | Large headlines only |

**"Display" in a font name means a size-specific cut.** Use the Display variant at large sizes and the Text variant at small sizes (SF Pro, optical-size families).

**Avoid the default-model fonts when direction is open.** Inter as an unexamined default and the LLM-favorite display serifs signal templating; start from Geist, Satoshi, Outfit, Cabinet Grotesk or a brand-appropriate face. Inter is fine when the brief asks for neutral/Linear-style, or for accessibility-first public-sector work. Direction-level taste: anti-slop.md.

**Thin weights are display-only.** Below 18px use weight 400+; weights 100-300 vanish at text sizes and on low-DPI screens. Use them at 28px+ and verify contrast there too.

**Different faces look different at the same `font-size`** because of x-height and cap height; compare optically, not by number.

**Fallback stacks are mandatory.**

```css
html { font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; } /* native feel */
html { font-family: "Brand Face", "Helvetica Neue", Arial, sans-serif; }                    /* brand face */
```

Serve `.woff2` on the web (loading strategy: `frontend-performance`).

## Type scale and roles

**Define a small set of sizes and deviate from it as little as possible.** Hard-coded sizes with no system break down at scale.

**Define roles, each pairing size + line-height + weight (+ tracking),** so styling a role is one decision. Starting point for a product UI:

| Role | Size | Line-height | Weight |
| --- | --- | --- | --- |
| Display | 2.25rem (36px) | 1.1 | 600 |
| Title | 1.5rem (24px) | 1.2 | 600 |
| Heading | 1.125rem (18px) | 1.3 | 600 |
| Body | 1rem (16px) | 1.5 | 400 |
| Caption | 0.8125rem (13px) | 1.4 | 400 |

**Name sizes by use on a team** (`text-body-sm`, not `text-sm`) so the rules outlive the author. Solo, Tailwind's default names are fine when usage rules are clear.

**Emphasis inside a role is one weight step (400 to 500), not a size change.**

**Repeated roles stay identical across screens and states.** Check: grep for one-off `text-[17px]`-style values.

**Heading levels map to descending scale steps.** A child heading must never outweigh its parent. Adjacent small levels may share a size if weight or spacing separates them. A heading is never smaller than body unless it is a deliberate label-style overline. Pick the heading element by document structure, then set size in CSS; never pick an element for its default size (semantics: accessibility.md).

```css
h1 { font-size: var(--text-2xl) } h2 { font-size: var(--text-xl) } h3 { font-size: var(--text-lg) }
```

**Control hierarchy with size, weight, spacing and tone together,** not raw scale. Oversized H1s that merely shout are a tell. Marketing display type may scale fluidly (`clamp()`) and reach max ~6rem; dense product UI stays spatially predictable with fixed role sizes.

**Hero sizing: plan type and imagery together.** A 4-line hero headline is a font-size error, not a copy error. Default `text-4xl md:text-5xl lg:text-6xl`; `text-6xl md:text-7xl` only for 3-5 word headlines.

## Size floors

| Text | Size |
| --- | --- |
| Long-form body | 16px (`1rem`); move off it only for a nameable reason (small x-height face, narrow measure, dense pro tool) |
| UI text (inputs, menus) | ~14px |
| Captions | 13px |
| Absolute floor | rarely below 12px |
| Form inputs on mobile | 16px (see Inputs) |

**Use rem, not px, for text** so browser font settings and zoom work. Type must survive 200% zoom, larger default font size and overridden line-height/letter-spacing. Contrast numbers: color.md.

## Line-height, tracking, measure

**Line-height by role, unitless.** Headings about 1.1 (display up to 1.2); body 1.5-1.6. Unitless scales with the font size; fixed `24px` does not.

**Anything that wraps to 3+ lines needs at least 1.4,** even in a height-constrained row (`leading-none` on a card description is a bug).

**Tune line-height inversely with measure and to the face:** wider lines and tall x-height faces need more leading. Light text on dark surfaces needs slightly more leading, a touch more tracking and sometimes one weight step up.

**Italic display needs descender room.** `leading-none` clips `y g j p q` in italic; use at least `leading-[1.1]` and a little bottom padding.

**Tracking by size.** Large headings: slightly negative (`-0.02em`); floor `-0.04em`, and `-0.02` to `-0.03em` usually reads best. Small uppercase labels: positive (`0.05em`). Body at reading sizes: none.

```css
.display-heading { letter-spacing: -0.02em }
.uppercase-label { text-transform: uppercase; letter-spacing: 0.05em }
```

**Kerning is built in;** disable (`font-kerning: none`) only deliberately.

**Cap the measure at 60-75 characters** (`max-w-[65ch]`, or `max-w-xl`/`max-w-2xl` at 16px). Any unit works as long as the cap exists. Recheck when body size changes. (Sources varied 45-75; use 65ch default.)

**Paragraph rhythm: spacing between paragraphs OR first-line indent, not both.**

**Do not justify text in interfaces.** `text-align: start` (justify only in specific editorial layouts). Long paragraphs in mixed-direction UI align to their own script: set `lang`/`dir` on the paragraph.

## Wrapping and truncation

**Four declarations, four jobs.**

| Property | Use |
| --- | --- |
| `text-wrap: balance` | Headings and short text, 6 lines or fewer (Chromium; 10 in Firefox); ignored beyond that |
| `text-wrap: pretty` | Default for paragraphs, descriptions, captions, list items; avoids a lone last word |
| `overflow-wrap: break-word` | Where a long word, URL or ID can escape the container |
| `white-space: nowrap` | Labels, badges, buttons where a break looks broken |

Skip balance and pretty on very long text (10+ lines) and code blocks. Tailwind: `text-balance`, `text-pretty`, `break-words`, `whitespace-nowrap`.

```css
h1, h2, h3 { text-wrap: balance }
p, li, figcaption, blockquote { text-wrap: pretty }
```

**CTA labels fit on one line at desktop.** If a button wraps, shorten the label (1-3 words) or widen the button; never cap its width.

**Truncate without losing content.** One line: `overflow:hidden; text-overflow:ellipsis; white-space:nowrap` (`truncate`). Multi-line: `line-clamp-*`. When the missing text matters, keep the full value reachable (tooltip, expand, detail view). In flex children add `min-w-0` or the ellipsis never triggers.

**Keep text natural-case in source;** style with `text-transform` so redesigns do not rewrite copy.

## Numerals

**Apply `tabular-nums` to any value that changes or aligns in columns:** counters, timers, prices that update, table number columns, dashboards. Prevents layout shift.

```tsx
<span className="tabular-nums">{count}</span>
```

Do not apply it to static display numbers, decorative large numbers, phone numbers, zip codes or version strings. Inter's tabular `1` becomes wider and centered; verify it looks right.

Other: `slashed-zero` to separate 0 from O in IDs and code. Dense data views: tabular or mono numerals everywhere.

## Variable fonts and OpenType

**Use CSS properties, not raw tags.** `font-weight: 650`, not `font-variation-settings: "wght" 650`; `font-optical-sizing: auto`; `font-variant-numeric: tabular-nums`. Properties still work when a non-variable fallback renders; raw tags silently do nothing. Reserve raw tags for custom axes (`"GRAD" 80`) and niche features (`"ss01" 1`).

**Variable vs static.** One or two weights: static files can be smaller. Several weights, optical sizes or custom axes: variable usually wins. A font supports only the axes and features its designer shipped (Inter's variable file has only `wght` and `opsz`).

| Axis | Tag |
| --- | --- |
| Weight | `wght` |
| Optical size | `opsz` |
| Width | `wdth` |
| Slant | `slnt` |
| Custom (e.g. Roboto Flex) | `GRAD` |

| Feature | Tag / property |
| --- | --- |
| Tabular numbers | `tnum` / `font-variant-numeric: tabular-nums` |
| Slashed zero | `zero` / `slashed-zero` |
| Ligatures | `liga` |
| Real small caps | `font-variant-caps: small-caps` |
| Real super/subscript | `font-variant-position: super` or `sub` |
| Stylistic sets / variants | `ss01`-`ss20`, `cv01`-`cv99` (slot meaning differs per font; check the docs) |

**Load the real weights and styles the design uses.** Browsers synthesize missing bold/italic and distort the face. `font-synthesis: none` removes synthesis but also erases emphasis; set it only after confirming every bold, italic, small-cap and super/subscript form stays distinct across the whole fallback stack. Prefer longhands (`font-synthesis-weight`) when only one mode is unwanted, and avoid blanket `none` on body text.

**Text-box trim for optical centering** in buttons and badges: `text-box: trim-both cap alphabetic` (Chromium 133+, Safari 18.2+, no Firefox; progressive enhancement).

## Rendering and decoration

**Apply font smoothing once at the root.** macOS renders text heavier than intended.

```css
html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale }
```

Tailwind: `antialiased` on `<html>`/`<body>`. Never per component.

**Take underlines from the font.** `text-underline-position: from-font; text-decoration-thickness: from-font`, or tune with `text-underline-offset: 3px`, `text-decoration-thickness: 1px`, `text-decoration-skip-ink: auto`. A dotted underline (`abbr`, defined terms) signals extra info. Only the underline color animates reliably; for other effects build a separate element.

**Keep text selectable.** Use `user-select: none` only on drag or gesture surfaces, never across chrome. Brand `::selection` as long as the pair stays legible. Other pseudo-elements: `::placeholder`, `caret-color`, `::target-text` for link-to-text highlights.

**Decorative text:** `::first-letter` for drop caps, `initial-letter` (limited support), `background-clip: text`, `-webkit-text-stroke`, `text-shadow`. Strokes on variable fonts can show inner overlap lines; use a static font there. Never trade legibility for decoration.

## Inputs at 16px on mobile

**Inputs must render at 16px on mobile** or iOS Safari zooms the page on focus. Two fixes with different looks; ask which the design wants:

```tsx
<input className="text-base sm:text-sm" type="email" />   {/* size up on mobile */}
```

Or keep `font-size: 16px` and scale down, compensating the box. Wrapper draws the surface; input stays transparent (a background on the scaled element shrinks too):

```tsx
{/* 13px from 16px: 13/16 = 0.8125 */}
<div className="flex h-10 items-center rounded-[10px] bg-gray-300 px-2.5">
  <input className="h-full w-[calc(100%/0.8125)] origin-left scale-[0.8125] bg-transparent text-base leading-[calc(1.125/0.8125)] outline-none sm:w-full sm:scale-100 sm:text-[13px]" />
</div>
```

Use `origin-right` under RTL. Never disable zoom with `maximum-scale=1`.

## Punctuation and international text

**Use real typographic characters in rendered prose.**

| Instead of | Use |
| --- | --- |
| Straight quotes | Curly quotes (straight stay in code) |
| Hyphen in a range | En dash: `2010–2020` |
| Aside separator | Em dash character, sparingly (not as a design flourish in pull quotes) |
| `...` | `…` |
| Plain space in `16 px` | `&nbsp;` |
| Uncontrolled long-word breaks | `&shy;` |

**Set `lang` on the document and `dir` where direction changes.** Browsers use `lang` for quotes, hyphenation and pronunciation. Numbers keep digit order in RTL; wrap mixed number/text values in `<bdi>` to isolate them. Spatial mirroring: layout.md.

## Verify

Read the rendered page, not the code: bad wrapping, widows and truncation appear only at real content lengths. Check computed size/weight per heading level (descending), declared line-height and measure, truncation against realistic strings, 200% zoom, narrow containers, long headings, localization expansion and font fallback.

| Mistake | Fix |
| --- | --- |
| Orphan on last line | `text-wrap: pretty` |
| Lopsided two-line heading | `text-wrap: balance` |
| Child heading larger than parent | Descending scale steps |
| Thin/light weight on 14px UI text | Weight 400+ below 18px |
| `leading-none` on 3-line description | Line-height >= 1.4 |
| Numbers jitter as they update | `tabular-nums` |
| Synthesized bold/italic | Load the real faces |
| Underline cuts descenders | `skip-ink: auto` + `from-font` |
| Mobile input zooms on focus | 16px font-size |
| Selection disabled app-wide | Restore; limit to drag surfaces |
| Mixed-direction value in wrong order | Fix `lang`/`dir`; wrap in `<bdi>` |
