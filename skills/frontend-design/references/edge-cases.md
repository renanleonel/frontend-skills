# Edge cases

Worst-case data stress testing: how to find what breaks when real data replaces demo data, the dataset to render, and the fix for each failure. Read when building a list/card/table/form, when asked to stress-test or harden a screen, or before shipping anything that renders user data. States (loading/error/empty UI) live in `interaction.md`; copy wording in `copy.md`.

## Posture

**Assume demo data was chosen to flatter the design.** Names that fit on one line, counts that need no separator, every optional field filled. Undo that choice field by field.

**Use plausible or schema-backed values, never random junk.** `"aaaa…"` x5000 gets dismissed as "never happens". Each value is either a realistic pattern (a long hyphenated surname, a plus-addressed email) or the real limit from the validation schema, DB column or API. If no limit exists, record "unbounded" as a finding and test something long but believable.

**Test the short and missing cases too, not only long text.** Orphaned dashes, missing avatars, "1 members", empty lists and translated badges ship more often than long names.

**Change the data, not the component.** Inject the worst case through the same boundary as demo data (fixture, mock, props, API stub). Hand-editing markup tests your edit.

**Mix failures across rows** (row 1 long name, row 2 long email, row 3 one-letter name). The first rows on screen matter most.

## Workflow

### 1. Map every rendered value

List each field with source, type, limit, optional?. Include easy-to-forget values: header counts, relative timestamps, badge/status text, data-driven button labels, tooltips, avatar images, and the list length itself.

| Field | Source | Type | Limit | Optional? |
| --- | --- | --- | --- | --- |
| `name` | `member.name` | string | 255 (schema) | no |
| `email` | `member.email` | string | none found | no |
| `status` | enum | active / invited / expired | n/a | no |

Find limits in Zod/Yup/Valibot schemas, migrations, API types and `maxLength` attributes. Where frontend and backend disagree (input 50, column 255), longer values will arrive via import or API.

### 2. Build the worst-case fixture

Create it beside the demo fixture, same type and shape. Pick values from the catalog below. Also prepare separate states that don't fit one dataset: **Empty** (0 items, no results), **One** (single item, every count at exactly 1), **Huge** (1,000+ rows if unpaginated).

### 3. Wire the "Demo data / Worst case" toggle

**Add a dev-only segmented control: `Demo data / Worst case`** (extra segments: `Empty`, `One`, `1,000 rows`). It swaps the fixture at the data boundary; never ships to production (gate behind `import.meta.env.DEV` or a prototype route). Fixed bottom-center, plain gray track, white active pill, system font, instant switch.

```tsx
const fixtures = { demo: demoMembers, worst: worstMembers, empty: [], one: worstMembers.slice(0, 1) };
const mode = new URLSearchParams(location.search).get("data") ?? "demo";
const members = import.meta.env.DEV ? fixtures[mode as keyof typeof fixtures] : demoMembers;
// toggle writes ?data=worst so a reload keeps the state
```

**Keep the worst-case fixture after fixing.** It is the regression test for the next change. Verify fixes in every toggle state, Demo included.

### 4. Break it

**Check in each of these:** the component's real container width (a sidebar list is not full-page), 320px, the widest supported layout, browser zoom 200% (or raised root font size), dark mode, and `dir="rtl"` on a wrapper if supported. Screenshot each state when tooling allows; otherwise say which findings were verified visually and which inferred from CSS.

### 5. Report, then stop

**List all breaks with a fix each and wait for the go-ahead.** Some are design decisions (truncate vs wrap, hide vs "n/a").

| # | Severity | Field | Worst-case value | What happens | Fix (`file:line`) |
| --- | --- | --- | --- | --- | --- |

Severity: **Broken** (unreadable, unreachable action, wrong data), **Ugly** (readable but visibly wrong), **Fragile** (fine now, one realistic step from breaking, e.g. no limit/fallback). Then: decisions needing the owner (with a recommendation), and "What held up" (cases already handled). Tone is matter-of-fact: the component was built against kind data, which is normal.

## Failure signatures and fixes

| What you see | Cause | Fix |
| --- | --- | --- |
| Avatar/icon squished to an oval | Flex child shrinking | `shrink-0` on avatar, icon, any fixed-size box |
| Text overflows instead of wrapping/truncating | Flex/grid child has `min-width: auto` | `min-w-0` on text column; `minmax(0,1fr)` in grid |
| Email/URL runs past the edge | No break opportunities | `overflow-wrap: anywhere` (`break-words` is weaker in flex; prefer `anywhere`) |
| Trailing action (menu, button) pushed off or clipped | Middle content took all the space | `min-w-0` on middle, `shrink-0` on action |
| Badge wraps to two lines | Badge allowed to shrink | `whitespace-nowrap shrink-0`; decide what yields instead |
| Avatar looks adrift beside a 3-line name | `items-center` on rows of varying height | `items-start` once text can wrap |
| Last row cut mid-glyph | Fixed-height box, no scroll/fade cue | Visible scroll or fade mask; confirm `overflow` is intended |
| Long word splits mid-word in heading | `word-break: break-all` | `overflow-wrap: anywhere` (breaks only when needed) |
| Wrong initials (`J`, `CI`, `�`) | `name.split(' ')[0][0]` | Grapheme clusters via `Intl.Segmenter`, first + last word, icon fallback |
| Orphaned `-` or blank line for missing field | Placeholder for absent optional value | Omit the line, or reserve its height on purpose |
| "1 members", "0 member" | Hardcoded plural | `Intl.PluralRules` or per-count strings |
| Numbers jitter, columns misalign | Proportional figures | `tabular-nums` |
| `1284`, `NaN`, `undefined`, `0.30000000000000004` | Raw value rendered | `Intl.NumberFormat` with user locale; guard null |
| Translated button label overflows | Fixed width | Content width + `min-w-*`, never fixed `w-*` on text |
| Vietnamese/Thai diacritics clipped | Tight `leading` + `overflow-hidden` | Looser line-height, no clipping on text boxes |
| Broken-image icon in avatar | No error fallback | `onError` to initials; `object-cover` for any aspect ratio |
| Ellipsis with no way to read the rest | Truncate only | `title`/tooltip, and full value in a detail view |
| 1,000 rows stutter | Every row rendered | Virtualize or paginate (state which) |
| Raw `<b>`, `&amp;`, `**x**` visible | Wrong escaping layer | Escape once at render; never `dangerouslySetInnerHTML` user data |
| Hover-only actions unreachable | Touch has no hover | Always show on touch (`@media (hover: none)`) |
| Layout shift as images load | No dimensions | Fixed size or `aspect-ratio` |

## Truncate, wrap or clamp (decide per field)

- **Wrap** text needed in full to identify something (names, detail-view titles). 2 lines is fine; 4 means the column is too narrow.
- **Truncate at the end** secondary metadata where the start carries meaning (role, description, preview). Always provide a way to see the full value.
- **Truncate in the middle** when items differ at the end: file names (`Q3-report…v12-final.pdf`), paths, hashes, emails sharing a long domain. End truncation makes them look identical.
- **Clamp** multi-line previews in cards (`line-clamp-2`) so card heights stay predictable.
- **Never truncate** numbers, amounts, dates or anything users compare.

```css
.truncate { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.clamp-3 { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
```

## Worst-case catalog

Use `example.com`/`.test` domains so fixtures never touch real inboxes. Pick rows that match the Phase 1 table.

### Names

| Value | Breaks |
| --- | --- |
| `Aleksandra Wiśniewska-Kowalczyk` | Long, hyphenated, diacritics; wraps at the hyphen |
| `Christopher Alexander Montgomery III` | Suffix; naive initials give `CI` |
| `Konstantin Oberhauser-Wettstein` | Compound; overflows single-line rows |
| `Jo` / `J` | Mostly empty column; single-char initials; tiny click target if name is the link |
| `Ólafur Darri Ólafsson` | Accented capital; uppercase/sort/initials |
| `Đặng Thị Ngọc Hân` | Stacked diacritics clipped by tight line-height |
| `王秀英` | CJK, no spaces: "first+last word" logic finds one word; breaks anywhere |
| `نور الهدى عبد الرحمن` | RTL; punctuation and icons land on the wrong side without `dir="auto"` |
| `María José de la Cruz y Fernández` | Lowercase particles; initials and last-name sort |
| `dana` | Lowercase; initials still need uppercase |
| `🦊 Fox`, `👩🏽‍💻 Priya` | Emoji first / ZWJ sequence: `charAt(0)` yields half a surrogate pair; slicing breaks the sequence |
| `  Sam   Lee ` | Leading/trailing/repeated spaces |
| missing name (email only) | Needs a fallback |

### Emails, URLs, identifiers (no break opportunities)

| Value | Breaks |
| --- | --- |
| `bartholomew.fitzgerald@northwind-industries-holdings.example.com` | Pushes siblings off the row |
| `a@b.co` | Shortest realistic; layout assuming long looks empty |
| `first.last+billing-notifications@example.com` | Plus-addressing rejected or truncated at the meaningful part |
| Long URL with query string | Overflow; end truncation hides the differing part |
| UUID `9f8e7d6c-5b4a-4c3d-8e2f-1a0b9c8d7e6f` | Monospace width; middle-truncation candidate |
| `Q3 Board Deck - FINAL (revised) v12 [approved by legal].pdf` | End truncation hides version and extension |
| `IMG_20250914_183022_HDR_portrait_edited_edited.HEIC` | Unbreakable; uppercase extension |
| `@a` / `@thisisaverylongusernamethatisallowed` | Handle extremes |

### Labels and copy from data

| Value | Breaks |
| --- | --- |
| `Senior Product Design Engineer, Platform Infrastructure` | 3-line wrap in a secondary slot |
| `Invitation expired 12 days ago` | Long badge squeezes the name column |
| `Benachrichtigungseinstellungen` | 30-char German compound, unbreakable |
| `Paramètres de confidentialité et de sécurité` | French runs ~30% longer than English |
| 12 tags on one item | Wall of tags; needs a `+8` overflow chip |
| One tag `customer-feedback-from-enterprise-onboarding` | Single tag wider than container |
| `Untitled` / empty / whitespace-only | Collapsed heading, zero-height row |
| `<script>alert(1)</script>`, `&amp;`, `**bold**` | Must render as literal text |
| Value containing a newline | Doubles row height or is silently dropped |
| 2,000-character pasted description | Clamp, "show more", textarea growth |

### Numbers and money

| Value | Breaks |
| --- | --- |
| `0` | "0 members", empty bar, divide-by-zero percentages |
| `1` | "1 members", "1 days ago" |
| `1284` | Needs `1,284` |
| `1000000` | Badge width; compact `1M` where precision doesn't matter |
| `12345678.9` as currency | `$12,345,678.90` overflows totals columns |
| `-42.5` | Sign, red-text logic, accounting parentheses |
| `0.1 + 0.2` | Float noise rendered raw |
| `142%`, `-3%` | Progress bars past bounds: clamp the fill |
| `null` / `undefined` / `NaN` | Rendered literally |
| `1.284` (de-DE) vs `1,284` (en-US) | Hardcoded separators wrong for half the world |
| Live value `99` to `100` | Width jump without `tabular-nums` |

### Collections

| Value | Breaks |
| --- | --- |
| 0 items | Missing empty state |
| 1 item | Grid looks broken with one card; "1 of 1" |
| Exactly page size, page size + 1 | Off-by-one "Showing 40 of 40"; empty page 2 |
| 1,000+ unpaginated | Scroll perf, memory; "Showing 40 of 1,284" copy |
| One item 10x larger than others | Masonry/grid rows stretch to tallest |
| Identical names | Name is the only distinguishing field |

### Time

| Value | Breaks |
| --- | --- |
| Now | "0 seconds ago" instead of "just now" |
| 12 days, 11 months, 3 years ago | Relative thresholds; go absolute after about a week |
| Future date | "in 3 days" vs "-3 days ago" |
| `1970-01-01` | Zero timestamp shown as real date |
| `2025-12-31T23:30:00-08:00` | Different day in UTC vs user timezone |
| `1,284 hours` | Duration never rolls up to days |

Use `Intl.RelativeTimeFormat` and `Intl.DateTimeFormat`, never hand-built strings.

### Images and media

| Value | Breaks |
| --- | --- |
| Avatar URL that 404s | Broken-image icon instead of initials |
| No avatar | Fallback size/color parity with real avatars |
| 4000x200 or 200x4000 image | Distortion without `object-cover`; tall image blows out card height |
| Transparent/dark logo in dark mode | Invisible |
| Slow image | Layout shift without dimensions/`aspect-ratio` |

### Data states

| Value | Breaks |
| --- | --- |
| Partial data (some optional fields filled) | Misaligned rows |
| Every enum status in one list | Varying badge widths |
| Raw API error text (`TypeError: Cannot read properties…`) | Leaks internals; see `copy.md` |
| No permission | Disabled actions change row layout |
| Current user in the list | "You" label; actions that shouldn't apply to self |

### Environment

| Condition | Breaks |
| --- | --- |
| Container 320px | Every overflow at once |
| Component reused in a 280px sidebar | Designed full-width |
| 2560px viewport | Lines too long, content stranded on one side |
| Zoom 200% / large text | Fixed heights clip growing text |
| Dark mode | Hardcoded colors, invisible borders/logos |
| `dir="rtl"` | Icons, chevrons, padding, trailing action order |
| Touch device | Hover-only actions unreachable |

## Internationalization

**Budget 30-40% extra width for translations** (German is often the longest, CJK the shortest but taller). Use content-sized flex/grid; no fixed widths on text containers.

```tsx
// Bad: assumes short English
<button className="w-24">Submit</button>
// Good: adapts to content
<button className="px-4 py-2">Submit</button>
```

**Use logical properties so RTL works without overrides:** `ms-4` / `me-4`, `ps-*`/`pe-*`, `border-e`, `text-start`, `margin-inline-start`, `padding-inline`, `border-inline-end`. Not `ml-*`, `pl-*`, `border-r`, `text-left`.

**Mirror directional icons in RTL** (arrows, chevrons, back/forward) but not logos, media controls or numbers: `[dir="rtl"] .arrow { transform: scaleX(-1); }`. Use `dir="auto"` on user-generated text of unknown direction.

**Use UTF-8 everywhere; test CJK, Cyrillic, Arabic, Hebrew and emoji in every text field.** Emoji span several code units: count graphemes with `Intl.Segmenter`, never `.length`, when limiting or slicing.

**Format via `Intl`, never hardcode separators:**

```ts
new Intl.NumberFormat(locale, { style: "currency", currency: "USD" }).format(1234.56); // $1,234.56
new Intl.DateTimeFormat("de-DE").format(date); // 15.1.2024
```

**Use proper plural rules, never `n !== 1`.** Some languages have 3-6 plural forms: `t("items", { count })`. Never concatenate translated fragments (see `copy.md`).

**Keep text containers expandable at 200% zoom;** min body size 16px on mobile (iOS Safari zooms focused inputs under 16px and breaks form layouts), 14px only for genuinely secondary text.

## Input boundaries

**Set a limit in both client and server, and make them match.** Client `maxLength` plus server validation; show the limit near the field (`aria-describedby` hint). Never trust client validation alone.

**Prevent double submission:** disable or guard the button while pending, and make the mutation idempotent where possible. Test by clicking submit 10 times fast.

**Don't block the whole screen when one component errors;** contain failures in error boundaries and keep the rest interactive.

## Verification checklist

Names 100+ chars; emoji in every text field; Arabic/Hebrew and CJK strings; empty and one-item lists; 1,000+ items; offline and throttled network; forced API errors; rapid repeated submits; 320px, 200% zoom, dark mode, RTL.
