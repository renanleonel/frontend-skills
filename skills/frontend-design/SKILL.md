---
name: frontend-design
description: >
  Renan's interface design playbook — layout, typography, color, surfaces (radius, shadows,
  icons), interaction states, forms, accessibility, product copy, worst-case data, AI-native
  UI patterns and a catalog of small product details. Use when building, designing or
  redesigning any UI (page, screen, component, dashboard, landing, form, empty state); when
  reviewing, auditing, critiquing or polishing one ("review this UI", "this feels off",
  "make it look better", "polish before shipping"); when stress-testing UI with long or
  missing data; when building chat, agent or AI features; or when asked about spacing,
  fonts, palettes, tokens, contrast, dark mode, focus, hit areas or microcopy. Not for motion
  (frontend-motion-design), load performance (frontend-performance), file structure and
  data fetching (frontend-architecture) or charts (dataviz).
---

# Frontend Design

Turn a UI request into a considered interface: read the brief, commit to a direction, decide in the right order, and finish with a pre-flight pass, not a vibe. Every rule lives in exactly one reference file; this file is the route.

## Pick the branch

| Request | Branch |
| --- | --- |
| Build, design, redesign, extend a surface | **Build** (below) |
| Review a diff, PR, file, screen or flow; audit; critique; "feels off" | **Review**: run [references/review.md](references/review.md) |
| "Polish this" / final pass before shipping | **Review** in polish mode: fixes applied, not a report |
| "Break it", "try the worst case", stress-test | [references/edge-cases.md](references/edge-cases.md) workflow |
| A narrow question (which font, this contrast, this radius) | Answer from the one reference file that owns it |

## References: one topic, one home

| File | Owns | Read when |
| --- | --- | --- |
| [layout.md](references/layout.md) | spacing scale, grouping, alignment, hierarchy, density, responsive, progressive disclosure | structuring any screen; "cluttered", "cramped", "messy" |
| [typography.md](references/typography.md) | font choice and pairing, scale, line-height, measure, wrapping, truncation, numerals, OpenType | setting type; picking fonts; text that wraps or truncates badly |
| [color.md](references/color.md) | palette, ramps, semantic tokens, OKLCH, contrast numbers, dark mode, design-system token extraction | choosing or auditing colors, theming, tokens |
| [surfaces.md](references/surfaces.md) | radius (concentric), borders vs shadows, elevation, glass, image outlines, optical alignment, icons, button and card polish | cards, buttons, icons, "looks flat" or "looks cheap" |
| [interaction.md](references/interaction.md) | every state, loading, empty, forms, hit areas, keyboard, overlays, feedback and undo, URL state, onboarding | anything clickable, typeable or async |
| [accessibility.md](references/accessibility.md) | semantics, ARIA, names, live regions, focus, APG keyboard patterns, zoom, user preferences | every build; any a11y question |
| [copy.md](references/copy.md) | buttons, labels, errors, empty states, tone, numbers and dates | writing or reviewing any visible string |
| [edge-cases.md](references/edge-cases.md) | worst-case data, truncate/wrap/clamp decisions, i18n, RTL, input boundaries | lists, tables, cards fed by user data; stress tests |
| [anti-slop.md](references/anti-slop.md) | reading the brief, mode and dials, choosing a direction, defaults to refuse, bolder / quieter / distill / delight, ambitious effects | any new surface; "looks generic / AI-made / templated"; tone shifts |
| [ai-interfaces.md](references/ai-interfaces.md) | thinking, streaming, approval, tool chips, task rows, prompt bar, diff tables, agent screens (from beautifului.dev) | chat, copilots, agents, any AI feature |
| [details.md](references/details.md) | ~100 small product details from detail.design, by category | the detail pass of a build; "make it feel considered" |
| [review.md](references/review.md) | review types, scope resolution, check order, P0–P3 severity, report format | every review branch |

Motion (easing, durations, enter/exit, stagger) is out of scope: design the structure that motion needs, then hand off to `frontend-motion-design`.

## Build

### 1. Read the brief before any code

- **Classify:** new surface, extension of an existing one, redesign (keep or overhaul), or fix.
- **Mode comes from the surface, not the product:** Persuade (landing), Operate (app UI), Read (docs), Experience (portfolio). Mode sets the dials in `anti-slop.md`.
- **Inspect the repo:** Tailwind theme and CSS variables, component library, existing tokens, neighbouring screens. A coherent existing look *is* the brief.
- **State the design read** in one line before building: "Reading this as: [surface] for [audience], [vibe], leaning toward [direction]; variance [x], density [y]."

### 2. Choose a direction

- Pinned by the user or brand: use it as given.
- Established product: inherit it; a new section never earns its own identity.
- Free choice: derive it from the product and the audience's real context, run the guessability test in `anti-slop.md`, choose light or dark from the use context, then commit.
- Named design system (GOV.UK, Carbon, Fluent): use the official package.

### 3. Decide in this order

1. **Task and content:** what the user must do; real content at its min, typical and max.
2. **Structure:** one primary action, grouping, reading order, responsive collapse (`layout.md`).
3. **Interaction:** states, forms, keyboard, overlays (`interaction.md`); semantics (`accessibility.md`).
4. **Type → color and tokens → surfaces and icons** (`typography.md`, `color.md`, `surfaces.md`).
5. **Copy** (`copy.md`); AI patterns when relevant (`ai-interfaces.md`).
6. **Taste pass** against the refuse-list (`anti-slop.md`), **detail pass** (`details.md`), **worst-case data** (`edge-cases.md`).

Structure before style: a nicer palette never fixes an unclear hierarchy.

### 4. Build conventions

- Tokens first (CSS variables through the Tailwind theme), then components; reach for a token before an arbitrary value.
- Customize shadcn-style defaults so they carry the chosen direction.
- Build every state, not just the happy path. Use real images or labelled placeholder slots.
- File placement and data fetching: `frontend-architecture`.

### 5. Pre-flight (fix what fails; done = every box checked or marked unverified)

- [ ] Design read stated; direction passes the guessability test.
- [ ] One accent, one radius system, one icon set, applied consistently.
- [ ] Nothing from the refuse-list in `anti-slop.md` slipped in.
- [ ] Contrast passes for body, placeholder, controls and focus ring, in both themes.
- [ ] Keyboard-complete: tab order, visible `:focus-visible`, names on icon-only controls, Esc closes overlays.
- [ ] States built: hover, active, focus, disabled, loading, empty, error, success.
- [ ] Holds at 320px, a mid width, wide, and 200% zoom; no horizontal scroll; touch targets ≥ 44px.
- [ ] Worst-case data rendered: long strings, zero items, missing fields, non-Latin text.
- [ ] Every visible string re-read; no filler and no invented figures or claims.
- [ ] Browser defaults themed: selection, caret, scrollbar, `tabular-nums` where numbers align.
- [ ] Build, lint and typecheck clean; no console errors. Inspect desktop and mobile once, fix in one batch, confirm once.

### 6. Ask or decide

Ask, with one question offering options and a recommendation, only when: two directions diverge and nothing breaks the tie; a real asset, price, logo or claim is missing; the change alters IA, URLs, nav labels, form fields, brand marks or legal copy; or a heavy effect is proposed. Decide everything else yourself (spacing, scale, radius, states, icons, microcopy, responsive and empty or loading designs), asserting the likely reading and inviting correction.

### 7. Finish

Report what was built, the direction in one sentence, anything unverified, and the placeholders the user must replace.

## Sources

Distilled and paraphrased from impeccable, design-taste-frontend, emil-design-eng, make-interfaces-feel-better, jakubkrehel/skills (better-ui, better-layout, better-typography, better-colors, better-accessibility, better-writing, better-interface, interface-review) and emilkowalski/skills (break-ui), plus [detail.design](https://detail.design) by Rene Wang and [beautifului.dev](https://www.beautifului.dev) (MIT, © 2026 Shane Levine).
