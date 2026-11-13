Taste and visual direction: how to avoid the templated "AI look", pick an aesthetic on purpose, and push a design bolder, quieter or leaner. Read before choosing a look for a new page or when a design feels generic, loud or cluttered. Motion: see `frontend-motion-design`.

## Read the brief before choosing a look

**Infer direction from the brief, not from habit.** Most generic output comes from jumping to a default aesthetic before reading the room. Collect six signals first:
- Surface kind (landing, portfolio, app screen, docs, editorial) and its mode (see below).
- Vibe words the user used ("calm", "Linear-like", "brutalist", "premium", "playful").
- References: links, screenshots, named products, competitors.
- Audience. The audience picks the aesthetic, not your taste.
- Brand assets that already exist (logo, color, type, photography). On a redesign these are material, not options.
- Quiet constraints: public sector, regulated, accessibility-first, kids, trust-first commerce. These override aesthetic preference.

**State a one-line design read before writing code.** Format: "Reading this as: [surface] for [audience], [vibe] language, leaning toward [system or aesthetic family]." It forces a decision and lets the user correct you cheaply.

**Ask at most one question, only if two plausible reads diverge** ("closer to Linear-clean or Awwwards-experimental?"). If context settles it, declare the read and proceed.

**An explicit brief beats this file.** If the user pins a font, palette, era or style, honor it even when it appears on a "default" list below. Redirecting a clear brief toward your own taste is a failure.

## Pick the mode, then the dials

**Choose the mode from the requested surface, not the product.** A tool's landing page is still Persuade.
- **Persuade** (landing, pricing, campaign): earn attention and action. Expression is the product.
- **Operate** (app UI, dashboards, settings, admin): the task wins. Scanability, consistency, native expectations beat expression; brand lives in precise details.
- **Read** (docs, articles, changelogs): structure for comprehension first, then make reading pleasant.
- **Experience** (portfolio, gallery, showcase): the work leads from the first viewport; the interface recedes.

**Set two dials from the read, on a 1-10 scale, and say the values.** Defaults 8 / 4 (variance / density) for marketing; lower variance for operate and trust-first surfaces.
- **Variance:** 1-3 symmetric grid, centered, predictable. 4-7 offsets, mixed aspect ratios, left-aligned heads over centered data. 8-10 asymmetric: fractional grid columns (`2fr 1fr 1fr`), large empty zones, overlaps. At variance 4+, every asymmetric layout collapses to one column below 768px.
- **Density:** 1-3 gallery-airy (big section gaps). 4-7 normal app spacing. 8-10 cockpit: tight padding, 1px lines instead of cards, mono numerals.

| Read | Variance | Density |
| --- | --- | --- |
| Minimal / calm / editorial | 5-6 | 2-3 |
| Premium consumer, luxury | 7-8 | 3-4 |
| Playful, agency, experimental | 9-10 | 3-4 |
| SaaS landing (default) | 7 | 4 |
| Developer portfolio | 6 | 4 |
| Public sector, regulated | 3-4 | 4-5 |
| Redesign, preserve | match existing | match existing |
| Redesign, overhaul | existing + 2 | match existing |

**Use a real design system when the brief names one; do not fake it.** Fluent, Carbon, Material 3, Polaris, Atlaskit, Primer, GOV.UK, USWDS: install the official package and use its tokens. Do not import a system and override 90% of it, and never mix two systems in one tree. With shadcn-style components (this stack's default), never ship the default look: customize radius, color, shadow and type to the project.

**Be honest when the brief is an aesthetic, not a system.** Glassmorphism, bento, brutalism, editorial, aurora gradients and "liquid glass" have no official package. Build them with CSS and label borrowed inspiration as approximation. Frosted glass needs a solid fallback under `prefers-reduced-transparency`.

## Choose a direction on purpose

**Run the guessability test.** If someone could name your aesthetic from the category alone (or from category-plus-avoidance), rework it until neither guess is obvious. Three looks that models converge on whatever the subject:
1. Warm cream ground + high-contrast serif display + terracotta/signal-red accent.
2. Near-black + one neon accent + glowing edges.
3. Broadsheet hairlines + italic display serif + small tracked mono labels.
All are legitimate when the brief calls for them. Landing on one by default means you did not decide.

**Derive the look from the product's world.** Name the product's one mechanism, the audience's real scene (who, where, under what light), and what it looked like before the web. List several concrete visual systems the audience already knows (notation, publications, identity programs, instrument panels), drawn from at least three material families, then commit to one. Near-duplicates count once.

**Pick light or dark from the use scene, not the category.** One sentence of physical scene ("night-shift dispatcher, dim room") forces the answer. Fintech is not automatically dark; a book brand is not automatically cream.

**Choose a color strategy before choosing colors.**
- Restrained: neutrals plus one accent. Default for operate and read.
- Committed: one saturated color covers 30-60% of the surface.
- Full palette: 3-4 named roles.
- Drenched: the surface is the color.
Persuade and experience surfaces may go bolder; commit at page scale (fields that own regions), not accents sprinkled on a neutral ground. Palette mechanics live in `color.md`.

**One accent, locked page-wide.** Max one accent, saturation under ~80%. Once chosen, it is used everywhere: no teal badge in the footer of a rose page. Tint neutrals toward the accent hue instead of mixing warm and cool grays.

**One theme per page.** Do not flip a section to the opposite theme mid-scroll. One deliberate full switch is allowed only as a designed device.

**One shape system.** Pick all-sharp, all-soft (12-16px) or pill-for-controls and apply it everywhere, or document the rule (buttons pill, cards 16px, inputs 8px). Radius mechanics: `surfaces.md`.

**Match the first viewport to a thesis, not a header.** Ask what someone would describe an hour after seeing only the first screen. If the honest answer is "a mood", the concept is not committed. Show the product doing its job instead of a headline over a gradient.

**Commit fully on the first build.** Later passes make the committed thing clearer; they must not dilute it. A stock component inside a committed look (default nav, default input) is a lapse; rebuild it in the look's vocabulary.

## Defaults to refuse (the AI look)

These are defaults, not laws: a brief can earn any of them. Reaching for one while the choice is free means you were not deciding.

### Layout scaffolds
- **Equal icon-heading-text cards as the page structure.** Three identical feature cards in a row is the signature slop. Use an asymmetric grid, a 2-column split, a pinned scene, a list with real hierarchy. Nested cards are always wrong.
- **Cards where space would do.** Use a card only when elevation encodes hierarchy; otherwise group with `border-t`, `divide-y` or whitespace. At density 8+, no card boxes for metrics.
- **Hero-metric template:** big number, small label, supporting stats, accent. Replace with one real proof.
- **Centered hero over a mesh gradient** at variance 4+. Use a split, an offset, or a pinned structure. Centered is fine for manifesto or launch pages where the message is the design.
- **Eyebrow labels above every heading** (small uppercase tracked text). Delete them; the heading carries itself. If one earns its place, no more than one per three sections. Conflict note: one source bans eyebrows outright, another rations them; the ration is the ceiling, the ban is the better default.
- **Section numbers** (`01 / 02 / 03`, `001 · Capabilities`), step labels ("Stage 1"), `01 / 4` image counters. Name the step with a verb ("Install", "Ship") or drop the label.
- **Split section headers:** big left headline plus small floating right paragraph. Stack headline over body (max 65ch) unless the right column holds something real.
- **Zigzag repetition.** Max two consecutive image+text splits; across a page of eight sections use at least four layout families, and use each family once.
- **Bento grid as the default feature section.** Use one only when the items genuinely differ in weight and each cell holds something real (screenshot, live component, data). Never with empty cells or white-on-white text tiles; N items get N cells, and at least two or three cells get real variation (image, tint, pattern).
- **Three pricing tiers with the middle one badged "Most popular".** Price the product the way it is actually sold: one plan, usage-based, or a comparison table. Real tiers are fine; the Free / Pro / Enterprise triptych by reflex is not.
- **Checkmark bullet lists** (green ✓ before every feature line). Write fewer, specific lines as plain text or a table; reserve check glyphs for real comparison (has / lacks).
- **A modal for a task that needs neither interruption nor protected focus.** Use inline or a popover.
- **Long lists as ten hairlined rows.** For more than five items use grouped chunks, a 2-column grid, tabs, a "view all" disclosure or featured-plus-rest. A `border-t` and `border-b` on every row of a spec table is the laziest layout.
- **Hero overload.** Max four text elements (optional eyebrow, headline, subtext, CTAs). Headline two lines, subtext about 20 words, CTAs visible without scrolling, top padding about 6rem max. Move trust strips, pricing teasers and tagline-under-CTA below the fold. A 4-line hero headline is a font-size error.
- **Nav on two lines or taller than 80px** at desktop.

### Surface habits
- **Gradient text.** Emphasize with weight or size.
- **Decorative glass/blur (incl. "liquid glass"),** neon outer glows, and AI-purple/blue glows. Use inner borders or a tinted soft shadow.
- **Radial orbs and blurred color blobs** floating behind the hero or sections. Background color comes from a committed field, an image, or nothing.
- **Generic soft drop shadows on everything.** Elevation only where it encodes hierarchy (see `surfaces.md`).
- **Colored `border-left`/`border-right` over 1px** on cards, callouts, alerts.
- **Hard offset shadows** (`4px 4px 0`) outside a genuinely neobrutalist look. A zero-offset colored halo is decoration, not depth. Shadows carry an offset and soft blur, tinted to the background hue; no pure-black drop shadow on light surfaces.
- **Ghost card:** a 1px border under a wide soft shadow. Declare elevation once, border or shadow (see `surfaces.md`).
- **Pure `#000` and pure `#fff` everywhere.** Use off-black/zinc-950 and a tinted near-white.
- **Sparklines, progress rings, soft rounded rectangles standing in for content.** Filled-track progress bars as comparison visuals on marketing pages too.
- **Monospace as a costume** for "technical". Use it for code, data, measurement.
- **Decorative lines and grids** (crosshairs, stripes, two-axis grid overlays) with no canvas, map or instrument under them. Textures must come from the subject's world.
- **Custom cursors.** Hostile to accessibility.
- **Hover animation on everything:** cards that lift and scale, arrows that nudge right on every CTA, glow on hover. Hover feedback is a color or background shift; movement only where it explains the interaction.
- **Sparkle icons (✨) to mean "AI".** Name the action ("Summarize", "Draft reply") with a functional icon or none.
- **Emoji or Unicode glyphs as icons.** Use one library in one stroke weight; never hand-drawn SVG paths for UI icons. Icon craft: `surfaces.md`.
- **Lucide as the unexamined default.** It is the shadcn/AI-template icon set and reads as such. Prefer Phosphor, Tabler, Radix Icons or HugeIcons in new work; keep Lucide only when an existing project already uses it.
- **Fake product previews built from styled divs** (fake dashboard, terminal, task list, version footer). Use a real screenshot, a generated image, a live mini component, or editorial photography.
- **Hand-drawn "sketch" SVG scenes and `feTurbulence` grain** imitating illustration. SVG doing geometry (diagrams, crisp shapes) is fine; SVG imitating a picture is not.
- **Geometric masks (circle, polygon cutout) faking a photo subject's outline.** Derive a real matte or omit.
- **Pills or tags overlaid on photos,** and decorative photo-credit captions ("Plate 03 · House archive"). Caption below the image in plain words, or skip.
- **Decoration strips** (`BRAND. MOTION. SPATIAL.`), scroll cues ("Scroll to explore"), rotated vertical text, version labels (`V0.6`, `BETA`) in the hero, locale/time/weather strips, live-stock counters, version footers on marketing pages. Allowed only when real content or the brief requires them.
- **Decorative status dots** before nav items, rows and badges. A dot appears only for real state (live, available), one per section at most. Middle-dot `·` as a universal separator: max one per metadata line.
- **Pages without real imagery.** Text-only is not minimalism, it is unfinished. Order: generated section-specific images, then real photography, then labeled placeholder slots plus a list of what the user must supply. Heroes need a real visual, not text over a blob.

### Typography and color reflexes
- **Inter, Geist or Space Grotesk as the default,** and `Inter + slate-900`. These are the model-default sans faces. Inter is fine when the brief asks for neutral/Linear-like or for public-sector. Otherwise pick a face for the product (Satoshi, Cabinet Grotesk, ABC Diatype, Söhne, General Sans, a brand serif).
- **Serif because it "feels premium/creative".** That reasoning is the tell. Use a serif only when the brief names one, or the family is genuinely editorial/luxury/heritage and you can say why this serif fits this brand. Fraunces and Instrument Serif are the overused defaults, along with Playfair, Cormorant, Lora, Newsreader and DM Serif; rotate and justify.
- **Mixed-family emphasis** (one serif word inside a sans headline). Emphasize with italic or bold of the same family.
- **Oversized shouting H1s.** Control hierarchy with weight and color, not just scale. Display tracking stops around -0.04em; -0.02 to -0.03em usually reads better. Details in `typography.md`.
- **Beige + brass/clay/oxblood + espresso** for premium-consumer briefs (cream grounds like `#f5f1ea`, brass `#b08947`, warm near-black `#1a1714`). Rotate to cold luxury (silver/chrome), forest + bone + amber, black + tan, cobalt + one neutral, terracotta + slate, or monochrome + one saturated accent, and do not reuse last project's family.
- **Gray text on a colored ground.** Tint secondary text from that background hue.
- **Purple on black** (violet/indigo accent on near-black) as the "tech" look. Pick the accent from the product's world.
- **Rainbow coloring:** a different hue per card, badge or section. One accent, locked page-wide (above).
- **Basic pastel palettes** (Tailwind `-100`/`-200` fills, mint, lavender, peach) as a free choice. Pastels need a reason (kids, wellness, a brand) and one deep anchor color.
- **System display faces** (Impact, Arial Black) as an own-world display voice. Source a face whose character matches.

### Content tells
- **Placeholder people and numbers:** "John Doe", "Acme", "Nexus", "SmartFlow", egg avatars, `99.99%`, `1234567`. Use realistic, locale-appropriate names and messy numbers (`47.2%`). Label invented figures as sample data; never fabricate customer names, prices, benchmarks or capabilities.
- **Filler verbs and poetry:** "Elevate", "Seamless", "Unleash", "Revolutionize"; "Quietly trusted by", "Field notes", "On our desks"; micro-sentences under headings explaining that the list is short on purpose. Use plain labels ("Testimonials", "Latest writing").
- **Em dashes as a stylistic crutch.** One source bans them entirely; at minimum avoid them in headlines, buttons, captions and quote attribution. Use a period, comma, colon or parentheses. Copy rules: `copy.md`.
- **Logo walls with category labels under each logo.** Logos only, real SVG marks (Simple Icons), placed below the hero, not inside it. Invented brands get an invented simple monogram, not a plain-text wordmark.
- **Quotes over three lines,** name-only attribution, straight ASCII quote marks. Attribute name + role (+ company) and use typographic quotes.
- **Two CTAs with the same intent** ("Get in touch", "Let's talk", "Contact us"). One label per intent, used everywhere. Labels fit one line at desktop.
- **"It's not X, it's Y"** and other contrast-framing ("Not just a tool. A partner."). State what it is. Copy rules: `copy.md`.
- **Fake testimonials:** invented quotes, stock headshots, "Sarah, Marketing Lead". Use real quotes with permission or a labeled placeholder slot; never ship invented social proof.
- **Missing legal pages:** footer links to Privacy and Terms that 404 or don't exist. Any page that collects data, sells, or has sign-up ships real Privacy Policy and Terms pages (or labeled placeholders the user must fill before launch).
- **Copy that sounds thoughtful but means nothing.** Re-read every visible string before shipping; if a phrase has no clear referent or is cute-but-wrong, replace it with a plain functional sentence.

## Redesign protocol

**Detect the mode first.** Redesign-preserve (modernize without breaking the brand), redesign-overhaul (new visual language, same content and IA), or greenfield. If unclear, ask once whether to preserve the brand or start visually fresh.

**Refinement preserves; replacement replaces.** Refinement keeps identity, behavior, copy and everything outside scope. A redesign treats the old look as evidence and anti-reference: do not split the difference with polish on the discarded look. A missing design doc does not make a project greenfield; read tokens, theme and components for the incumbent world first.

**Audit before touching.** Record brand tokens (colors, type, radii, logo), IA and page tree, content blocks that do work vs filler, patterns to keep (signature interaction, copy voice), patterns to retire (slop tells, broken mobile, generic stock), and the SEO baseline (titles, meta, structured data), which is the largest redesign risk.

**Modernize in this order and stop when the brief is met:** typography refresh, spacing and rhythm, color recalibration, motion layer (see `frontend-motion-design`), hero and key-section recomposition, full block replacement only when unsalvageable. Targeted evolution (first four) delivers most of the value at a fraction of the risk when IA and SEO are sound.

**Never change silently:** URL slugs, primary nav labels, form field names or order (breaks analytics and autofill), logo/wordmark, legal and consent copy, analytics event hooks. Never regress existing focus states, alt text, keyboard support or contrast.

## Bolder

**Scope is sovereign.** "Make this section bolder" touches only that section. Do not restyle neighbors, migrate the page to a new idea, or add colors, fonts, radii or shadows the system does not already own. If the system truly cannot express it, name the exact addition and ask.

**Find why it reads flat before adding anything.** Compare it with neighbors: usually the section opted out of the system's strongest moves (display type at full strength, the signature motif, density and pacing). Raise it to the level the rest of the page already reaches, in the system's own vocabulary. It should look more like the same brand, not less.

**Make one decisive move, then quiet the rest.** If everything gets louder the section gets flatter. Give it its own rhythm: a peak in the scroll, a change in density or scale versus its surroundings. More effects is the opposite of bold.

**Run the skeleton test.** Remove the copy and look at the bare structure: does hierarchy and the system's devices alone say what this section is and why it matters? If it only works once the words return, the boldness lives in text size, not design.

**Keep content true.** Do not add claims. If real evidence is essential, ask for it.

**Check:** everything outside the target is unchanged; no new color, font or primitive appeared; behavior still works.

## Quieter

**Reduce intensity without erasing personality.** Quiet without intent collapses into generic; think luxury, not laziness. Identify the sources first: saturation, contrast extremes, heavy weights everywhere, decoration, scale with no hierarchy, excess motion.

- **Color:** drop to roughly 70-85% saturation, fewer hues, neutrals dominant with accent around 10%, tinted grays over pure gray, high contrast only where it matters.
- **Weight:** 900 to 600, 700 to 500; hierarchy through size, weight and space rather than color and boldness.
- **Space:** more room, lower density; thinner or fainter borders, or remove them.
- **Decoration:** cut gradients, patterns, stacked shadows, glows, blur; flatten layering; tame extreme radii.
- **Scale:** smaller jumps between sizes; even out erratic spacing; realign stray elements to the grid.
- **Motion:** shorter distances, no bounce; remove flourishes (see `frontend-motion-design`).

**Mode matters.** Persuade/experience: more restraint, more air, the point of view stays. Operate/read: less noise, flatter cards, less color, the tool recedes into the task.

**Never:** equalize everything (hierarchy still matters), strip all color, remove all anchors, or sacrifice affordance clarity.

**Check:** tasks still easy, still distinctive, easier to read at length, the POV survives the cuts.

## Distill

**Remove what does not earn its place.** Simplicity removes obstacles between users and goals; it does not remove features. Find the one primary goal, the necessary 20%, then cut, hide or merge the rest.

- **Information:** one primary action, one or two secondary, the rest tertiary or hidden; cut repeated information; progressive disclosure behind clear entry points.
- **Visual:** 1-2 colors plus neutrals; one font family, 3-4 sizes, 2-3 weights; delete borders, shadows and backgrounds that do not serve hierarchy; flatten nesting; one spacing scale.
- **Layout:** linear flow beats complex grids; drop sidebars that hold secondary content; pick left or center alignment and keep it.
- **Interaction:** fewer choices, smart defaults, inline edit instead of modal flows, remove a step, one obvious next action.
- **Copy:** halve it, then halve again; active voice ("Save changes"); plain words; no headings that restate their intro. See `copy.md`.
- **Code:** delete dead CSS, unused components and one-off variants; 3 variants usually cover 90% of cases.

**Never:** remove needed functionality, drop accessibility labels, make things so bare they are unclear, delete info users need to decide, or erase hierarchy. Match simplicity to the real task complexity.

**Document what you removed** and whether it needs another access point.

## Delight

**Add personality only at moments that earn it.** First use, completion, recovery, mastery, long waits. Not every click. Operate/read surfaces concentrate delight at those moments; persuade/experience can carry it through voice and composition.

**State one delight thesis in a sentence:** what the user should feel and why it belongs to this product. Derive the treatment from the product's mechanism and world; a neighboring product must not be able to reuse it unchanged. Generic whimsy is worse than neutral clarity.

**Match intensity to frequency and consequence.** Big milestone, bigger response; routine save, simply certain. It must still please on the hundredth use.

**Protect the task.** Delight never blocks or delays the primary action, never fakes progress, never plays sound without consent, never overrides platform or accessibility behavior, never trivializes loss, money or privacy in errors. Empty and first-use states show the next action before personality.

**Check:** the moment improves comprehension, confidence or recovery; the interface is fast and obvious without it.

## Ambitious effects (overdrive) without kitsch

**Context defines "extraordinary".** A particle field on a creative portfolio is impressive; on a settings page it is embarrassing, while instant optimistic saves there can be remarkable. For functional UI, the wow is how it feels: a dialog that morphs from its trigger (View Transitions), 100k rows scrolling smoothly (virtualization), validation that feels instant. For marketing, it is sensory and tied to the product's story.

**Propose 2-3 directions with trade-offs and get a pick before building.** This is the command most likely to misfire; do not jump to implementation. Each option states look and feel, browser support, performance cost and complexity.

**Fix fundamentals first.** Technical ambition never masks weak hierarchy, type or spacing.

**Degrade gracefully.** Feature-detect (`@supports`, `'gpu' in navigator`), keep a CSS-only fallback that still looks good, target 60fps (simplify under ~50), initialize heavy resources (WebGL, WASM) lazily near the viewport, pause off-screen rendering, test on a mid-range device. No sound without opt-in.

**One extraordinary moment per surface.** Stacked showpieces create noise. Tools: View Transitions, scroll-driven CSS, WebGL/shaders, canvas and OffscreenCanvas, `@property`-animated gradients, virtualization, Web Workers. Choreography and easing specifics: `frontend-motion-design`.

**Check:** removal test (does anyone notice it's gone?), device test, context test (right for this brand and audience).

## Craft taste: what separates polished from assembled

**Taste is trained, not preference.** Study why the best interfaces feel right, inspect them, reverse engineer them. Many details are invisible by design: when everything behaves as expected, nobody thinks about it. The aggregate of invisible correctness is the differentiator when software is merely good enough.

**Theme the parts you did not draw.** Browser defaults carry no design: text selection color, caret color, scrollbars, focus rings, underline offset, tabular numerals. Style them from the palette. This is the cheapest signal a page was built rather than assembled, and the one most often skipped.

**Prove, don't claim.** Show the subject working: the interface in use, the mechanism dramatized, specifics a competitor could not paste. Sections that restate a claim in other words add length, not substance.

**Pace the page like a studio.** Vary density, scale, imagery and quiet inside one grammar; follow dense passages with a quiet one; end on a real close. One spacing rhythm, more space above a heading than below it.

**Author the assets.** Names, entries, covers, thumbnails and copy are material; invent them at production fidelity and label them as sample data, instead of gradients and icon tiles standing in for content. Commercial claims (prices, customers, benchmarks) are never invented.

**Match the stack's look to this project.** React + Tailwind + shadcn-style components: override tokens in the theme layer (CSS variables), not by sprinkling arbitrary values; keep one set of radii, one accent, one type pair.
