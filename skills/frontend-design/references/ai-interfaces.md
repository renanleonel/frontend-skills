# AI interfaces

Patterns for AI-native UI (agent chat, tool activity, approvals, retrieved context, AI-edited data). Read when building or reviewing anything where a model acts, streams, or proposes changes. Measurements come from inspecting a polished reference set (MIT-licensed, beautifului.dev); treat them as a compact, dense baseline, not law. Motion: see `frontend-motion-design`.

## Cross-cutting AI-UI rules

- **Show the process in three distinct tiers: working, thinking, answer.** Users must tell "the system is busy" from "the model is reasoning" from "this is the result". Busy = loader plus elapsed time. Thinking = collapsed, expandable trace. Answer = full-contrast body text. Never mix the tiers in one block.
- **Collapse reasoning by default, summarize it in one line, keep the detail one click away.** Header reads like "Thought for 4 seconds" (past tense, duration) while done and a present-tense verb while running ("Reading briefs"). Auto-collapse when the answer starts.
- **Make every agent action a compact, inspectable row, not prose.** One line = icon + verb + object + small count/duration. Expand for input/output. Users scan 20 actions in a glance and drill into one.
- **Ask before any irreversible, costly or externally visible action; otherwise just act.** Approval is for sending, deleting, spending, publishing, writing to shared data. Read-only and reversible steps must not interrupt. Always offer Skip and a safe default.
- **Propose, never silently apply.** Edits to the user's data arrive as a reviewable diff with per-item toggles and one explicit "Apply N changes" button that states the count.
- **Every proposal carries its own undo path and its own off-ramp.** Cards have Dismiss (top-right), an alternative, and a primary action. Nothing auto-confirms.
- **Show provenance.** Claims get inline source chips; retrieved context shows source name, type and size. Group all sources behind one "N sources" control.
- **Status is a closed vocabulary with fixed color roles.** running = neutral spinner, completed = green, needs attention = orange, failed/removed = red, selected/primary = blue accent. Color is never the only signal: pair with an icon, count or word.
- **Use one density for the whole assistant surface.** Body 13px, secondary 12-12.5px, meta/chips 11-11.5px, mono for paths, counts, URLs and elapsed time. Text is small because many rows coexist; keep hit areas at least 28px (24px for secondary icon buttons inside dense rows, with padding that extends the target).
- **Keep the user in control during long work.** Persistent Stop, visible current step, progress counts (`12/12`, `68%`), partial results readable while running, failures shown per row with a retry, never a global spinner that hides state.
- **Suggestions are small and follow the answer.** Follow-up prompts and quick actions (Explain, Shorten) appear after content, as 32px rows or pills; they fill the composer, they don't auto-send.
- **Make confidence legible.** Recommendations state confidence as a label plus a small segmented meter (for example 4 bars), and list alternatives with their own status ("Needs review", "No signal").
- **Surface hierarchy through lightness, not boxes.** Cards are one raised surface with a hairline ring; nested chips and inputs use a slightly different inset tone. No heavy borders, no colored backgrounds except status tints.

## Shared tokens (copy as a starting point)

- Font: Inter (sans) + a system monospace. Mono is for code, filenames, elapsed time, counts, URLs.
- Neutrals (light / dark): page 98.5% / 20.9% lightness; surface 100% / 26%; inset 97.9% / 24.3%; hover 97% / 28.9%; ink 24.7% / 96.4%; ink-2 50.6% / 73.1%; ink-3 69.5% / 54.1%; line 94.6% / 30.8%. Neutrals have chroma near 0.005 (a faint cool tint).
- Status colors in OKLCH: accent blue `62.6% .205 255` (dark `68% .173 253`), green `60.3% .155 151`, orange `68.9% .179 50`, red `62.1% .192 23`. Each has a tint for backgrounds: light = ~95.5% lightness, dark = same hue at 14-16% alpha.
- Radii: cards/panels 10px (hero composers and agent windows 14px), inner rows/buttons 8px, small chips 6px, checkboxes 5px, pills fully round. Task capsules 22px on 44px height.
- Card shadow: 1px ring in `--line` plus a faint blur; overlays use a stronger ring plus a larger blur; dark mode raises ring opacity to 11-15% white instead of relying on shadow.
- Standard icon button: 28x28, radius 8px (24x24, radius 6px inside tight rows).
- Segmented control (view toggles): pill container with 2px padding, 21px-high segments, 11.5px/500 text, 8px horizontal padding.
- Primary pill button: 27px high, 12px horizontal padding, 12-13px/500 text, accent fill. Secondary: same size, surface fill with ring.

## 01 Loading state

- **Pair a quiet animated mark with a verb and a live elapsed timer.** Line: grid/dot loader, shimmering verb ("Churning"), elapsed time in mono 12px (`4.0s`). Verb 13px/500; the shimmer sweeps across text, not a spinner beside it.
- **Offer variants only as a brand choice, never per state.** Pick one loader style (dots, orbit, pixel grid) for the whole product; switch with a pill segmented control only in a design playground.
- **Use specific verbs tied to the task** ("Reading", "Searching", "Churning"), not "Loading...".

## 02 Thinking

- **Render the trace as a disclosure.** Header button: chevron + "Thought for N seconds", 13px/500, 28px high, radius 8px, hover tint. Body lists steps as rows.
- **Support four trace types with distinct row anatomies:** Steps (verb + object + optional count chip), Reasoning (prose paragraph), Search (query + result count + source favicons), Coding (file/command rows). Switch types in the same component, don't build four.
- **Step row:** 28px high, 8px gap, radius 6px, leading status icon, label 12.5px/500, trailing meta 11.5px/400 in ink-3 (`6 flavors`).
- **Active step shows the spinner/shimmer; finished steps show a check or nothing.** Do not keep spinning decorations on completed rows.
- Motion for expand and step reveal: see `frontend-motion-design`.

## 03 Streaming text

- **Stream plain text with inline source chips as tokens complete.** Chip: mono 10.5px, radius 5px, 18px high, favicon 12px + domain, hover darkens. Chips sit inline in the sentence flow, after the claim they support.
- **After the answer, show an action row:** icon buttons (24px: copy, regenerate, rate) and one "N sources" pill (22px, stacked favicons 14px + 12px label) that opens a popover (radius 10px, rows 26px, 12px text).
- **Then Follow-ups:** a 12px/500 label and full-width rows (32px, radius 7px, 12.5px text). Click fills the composer.
- **Body 13px, line-height roughly 1.55; keep answer text color at full ink and chips subdued.**
- **Never reflow committed text while streaming**: append at the end, keep the scroll anchored to the bottom only if the user hasn't scrolled up.
- Error state: stop the stream, keep partial text, show an inline red-tint note with Retry. Don't discard what already arrived.

## 04 Approval card

- **Ask structured questions as a stepper, one question at a time.** Card 320px wide, radius 10px, dismiss X top-right (28px). Question 14px/500; options below as single-choice rows (296x24-28px, radius 8px, 16px radio, 13px label).
- **Footer: pager "1 / 3" with prev/next chevrons (18px) on the left, Skip (ghost pill) and Continue (primary pill) on the right.** Continue becomes the final submit on the last question. Skip is always present.
- **Support single-select (radio) and multi-select (checkbox, radius 5px) in the same row anatomy.** Selecting an option may auto-advance for single-select.
- **Offer an "Other / write your own" row when options may not fit.**
- **Keep options to 2-5, labeled by outcome** ("Three (core line)"), not letter codes.
- States: idle, option selected (accent ring or tinted fill), answered (collapses into a one-line summary), dismissed.

## 05 Tool chips

- **Collapse a run into one summary line** like "4 tool calls, 2 messages" (12.5px, chevron, 27px high); expand to the full ordered timeline of thinking, edits, commands, results.
- **Interleave typed entries:** Thinking (label + one-line gist, expandable bullet list), File edit ("Write 204 lines" + file name + diff excerpt with +/- lines), Command (mono command + check lines such as `built in 1.2s`, `34 checks passed`), Media read (filename, dimensions, one-line description).
- **Show changed files as chips at the end:** mono 11.5px, radius 6px, 28px high, name plus green `+N` and red `-N`. Chip click opens that file's diff; overflow becomes "+2 more".
- Success lines use green checkmarks; failures use red with the first error line inline.
- Keep diff excerpts to a few lines inside the chip; link out for the full diff.

## 06 Task rows

- **Represent each agent task as a row: status glyph, title, trailing meta, status pill, chevron.** Capsule style: 44px high, fully rounded (22px), 440px wide in the reference; list style: flat rows with dividers. Offer both only if users need density control.
- **Status glyph:** 22px circle. Done = filled green with check; running = ring spinner containing the step number; failed = red; pending = hollow.
- **Meta on the right in ink-2 (12.5px):** counts like "12 suppliers", "7 SKUs", "2 messages". Status pill 22px high, 11.5px/500, tint background + matching text ("Completed" green, "Failed" red).
- **Expanded row lists sub-steps** (28px glyphs, 12px label, mono 11.5px progress `12/12`, `68%`), with a warning count badge (orange, 10.5px/600) for flagged items.
- **Failed rows list what was not done as drafts** ("draft") with a retry affordance; never hide failures inside a collapsed section.
- Order: running first or in plan order; completed stay in place (don't reorder under the user's cursor).

## 07 Chat panel

- **Tabs on top for parallel threads** (26px high, radius 6px, 13px) with a 24px icon button for new thread. Panel radius 14px, ~380px wide.
- **User message:** right-aligned bubble, radius 12px, padding 6px 12px, 13px text, subtle fill.
- **Assistant message: no bubble.** Starts with a collapsed reasoning/tool header (icon + name 12px/500 + duration "for 4s" 12px ink-3), then a 13px body paragraph, then optional chips (Comparison, Trend Detection) as the tool outputs.
- **Composer pinned at the bottom:** radius 8px, padding 10px, 76px tall at rest (textarea + send 28px). Send is disabled when empty.
- States: idle, user-sent (assistant header shows running state), streaming, done (reasoning collapses), error (inline retry).

## 08 Prompt bar (composer)

- **One rounded composer, growing with content:** radius 14px, ~42px minimum height, 6px padding, 6px gaps. Left: attach "+" (28px). Middle: textarea 13px. Right: model picker (72x28, radius 8px, 12px/500), dictation, send.
- **`@` opens a source menu; `/` opens a command menu.** Menu is a raised card (radius 10px, 4px padding) with 36px rows (radius 6px): icon, name 12.5px/500, one-line description 12px ink-3. Groups: Add files, Connected sources, Web search, Apps. A footer hint row (11px) explains how to type-to-filter.
- **Selected sources and commands become inline tokens** in the text (`/compare` style chip), removable with Backspace.
- **Model picker is a menu, not a modal;** show the model name and a short descriptor.
- **Dictation changes the whole bar:** show a live waveform in place of the textarea and swap send for confirm/cancel.
- **Shape is a brand choice** (rounded 14px or pill); keep one.
- Keyboard: Enter send, Shift+Enter newline, arrows + Enter in menus, Esc closes menus first, then clears.

## 09 Recommendation card

- **Phrase it as a question with the proposed action inline.** Title 14px/500 ("Want me to place this restock order?"), 13px body with entity chips inside the sentence (avatar 16px + name 12px/500, pill 22px).
- **List alternatives as selectable rows** (364x31, radius 8px, 12.5px text, status label 11px at right: "Needs review", "No signal").
- **Confidence meter:** 4 small vertical bars (4x10px, rounded) filled to level, next to a label "High confidence" 12.5px/500. Color the filled bars by level, not by decoration.
- **Footer: "Alternatives" (secondary pill, 27px) and "Accept" (primary pill).** Dismiss X top-right. Card 380px wide, radius 10px.
- Accept performs the action; a result row replaces the card (done) with undo if possible.

## 10 Context cards

- **Show what the model retrieved, as cards:** header "All chunks" 13px/600 with a count badge (radius 6px, 20px high), then one card per chunk (radius 10px).
- **Chunk anatomy:** title 13px/500, size meta "290 characters" 12px ink-3, excerpt 12.5px clamped to 3 lines (padding 8px 12px), footer source chip (24px high, pill) with a 14px type badge (PDF, CSV; 7px bold on a colored 4px-radius square) + filename 12px/500.
- **Let users remove or deprioritize a chunk** (icon button, 24-28px). Click opens the source at the chunk.
- Empty state: "No sources used" with a short explanation, not a blank panel.

## 11 Diff table (AI edits to tabular data)

- **Render proposed changes in place inside the table.** Removed rows: red tint background, red text, strikethrough on changed cells. Added rows: green tint, green text. Unchanged rows stay neutral. Cell padding 10px 12px, cell text 13px/500, header 12px/500 ink-3, rows 40-45px.
- **Each changed row has a checkbox (18px, radius 5px) at its end; clicking the row toggles it.** Hint in the header: "Click changed rows to toggle" (11px).
- **Footer summarizes and commits:** "2 removals · 1 addition" (11.5px) left, "Apply 3 changes" primary pill right; the number updates as rows are toggled and the button disables at 0.
- Table header: title 12.5px/500 left, hint right, card radius 10px, 380px wide.
- Keep tag/category chips (pill, 11.5px/500, 6px dot) so the changed row still reads as a record.

## 12 Records table (CRM-style)

- **Sticky header, 36px tall, 12.5px/500 ink-3, sort control per column (28px icon button).** Rows 35px, text 13px/500, 12.5-13px cells, hover tint, 0.12s color transition.
- **Row number and alpha-index column on the left;** group by first letter with the letter shown in a 20px rounded-6px tile.
- **Tags as pills (23px high, radius 8px, 13px, 7px padding), cap at 2-3 then "+N" overflow pill.**
- **Relationship strength as a colored label with a small dot (green strong, neutral weak, gray none)**; dates relative ("4 days ago") in ink, empty values as an em dash.
- **Links column renders domains in ink-2 with a favicon; empty = "—".**
- **Header actions:** "New property" and a "Table options" menu (28px icon buttons). Checkbox column for multi-select that triggers the Selection bar.
- Virtualize past a few hundred rows; keep row height fixed.

## 13 Filter table

- **Status filter tabs above the table, with counts:** pills 26px high, 12px/500, 10px padding, a count in a 15px chip (radius 4px, 10.5px) and a 6px status dot. "All" first.
- **Table card radius 10px, header 35px (12.5px/500), rows ~39px, 13px text.** Columns: name (500 weight), date (400), status pill (23px, radius 8px, tint + text), owner.
- **Selecting a tab filters instantly, keeps column widths, and keeps the header.** Empty filter result shows an inline empty row with a "Clear filter" action.

## 14 Sidebar nav

- **Workspace switcher at top (32px row, 14px/500), collapse toggle beside it, primary "New chat" button (36px, radius 8px).** Collapsed state shrinks to a 32-36px icon rail with tooltips.
- **Nav rows 32px, radius 8px, 13-14px, hover tint, active tint+ink.** Section label "Chats" 12.5px/500 ink-3; recents are one-line truncated titles.
- **Usage meter** (`3/10`, 12px/500) near the top for plan limits; "Upgrade" as a full-width 32px button at the bottom.
- **Search chats = icon button that morphs into an inline input with a close X** (see Search).
- Sidebar ~208px wide in the reference; keep titles truncated with ellipsis and full title in a tooltip.

## 15 Search

- **A search button opens a compact command list, not a page.** Panel 288px wide, radius 10px, rows 32px, radius 6px, 13px text, the first row pre-focused.
- **Seed with suggested queries (recent or contextual) when empty;** filter as the user types, highlight the matching substring, show "No results" with a way to ask the assistant instead.
- Keyboard: arrows move, Enter opens, Esc closes and restores focus to the trigger.

## 16 Flowchart (agent workflows)

- **Vertical node stack linked by connectors.** Trigger node first, then conditions, then actions. Node card 300-356px wide, radius 18px, 56px high for simple, 105px for branching.
- **Node anatomy:** 36px icon tile (radius 8px), title 13px/600, subtitle 12px/400 ink-2. Type label pill above ("Trigger", 11.5px/500, radius 6px).
- **Condition node ("If / Else") renders as a sentence with inline editable chips** (`order flavor is Rocky Road and order topping is ...`): chip 24px high radius 6px, operators plain text, "and/or" between.
- **Click selects a node (accent ring) and opens its settings;** connectors are 1px lines in `--line-strong` with an add-step "+" on hover.
- Run state per node: idle, running (spinner replaces icon), success (green check), failed (red, error message under title).

## 17 Insight cards

- **Carousel of short, specific findings with one number each.** Header: "Insights" 13px/600 + count + prev/next (24px). Card radius 10px, padding 12px.
- **Lead with the sentence ("The worst performer in your @Creamery is Rocky Road, down 6%") then a metric block:** big value 17px/600, label 11.5px with a 8px color dot, signed delta (red negative, green positive).
- **Embedded mini-visual** (trend snapshot, 320x199, radius 8px) with a small tab pill ("Snapshot").
- **End with one follow-up question** ("Should I rebalance flavors?") that sends to the assistant.
- Mono for inline numeric deltas (11.5px). Always show signed values with sign + unit.

## 18 Code block

- **Header bar: filename (mono 12.5px) left, Copy button (24px, radius 6px, 12px/500) right.** Copy flips to "Copied" for ~1.5-2s, same width to avoid layout shift.
- **Body:** mono 12.5px, line numbers 11px in ink-3 in a fixed 20px gutter, no wrap by default, horizontal scroll. Bold weight only for definitions (function name 500).
- **Code / Diff toggle (segmented pill, 21px segments)** lets users view the proposed change; diff lines use green/red tint backgrounds with +/- gutter marks.
- Block radius 10px, ring + surface fill; syntax colors from the status palette, desaturated.

## 19 Fine-tune card (inline adjust panel)

- **A compact property panel to refine an AI-generated object:** 240px wide, radius 10px, title 13px/500, section label 12.5px/500, "Adjust" pill.
- **Controls:** segmented layout toggle (row / col / grid; 28px, radius 8px, 2px padding, sliding highlight), number fields (26px, radius 6px, prefix letter W/H/Radius/Opacity in 12px ink-3, unit `%` 11.5px), select (26px, radius 6px).
- **Every field edits live and reflects in the preview; nothing needs a Save button.**
- Field labels are inline prefixes, not stacked labels, to keep height low.

## 20 Selection actions

- **Selecting text reveals a floating pill toolbar** with verbs: Explain, Improve, Shorten, Tone, Grammar. Pill container 36px high, 4px padding, 2px gap; buttons 28px high, 12px text, radius full; icon-only overflow 25-28px.
- **Position above the selection, centered; keep the selection highlight (3px radius) visible.** Dismiss on click outside or Esc.
- **Result replaces the selection as a reviewable change:** an inline strike/insert diff plus Accept/Reject, plus a "Send edit instruction" input for free-form requests.
- Don't show the toolbar for selections under ~3 characters.

## 21 Agent screen

- **Show what the agent is doing as a live window:** 340px card, radius 14px, header "Agent's screen" 13px/500 with a status pill ("Working" / "Loading" / "Idle") and an "Open" button (27px pill) to expand.
- **Modes: Open (watch), Teach (user demonstrates a task), Record (capture a workflow).** Segmented pill selects the mode.
- **Always show a visible "agent is controlling" indicator and a Stop/Take over control.** The user can interrupt at any moment; clicks in the view while the agent runs should offer takeover, not silently conflict.
- Loading state: skeleton window with the status pill pulsing; error state: red pill with a short reason and Retry.

## States checklist (apply to every component above)

- **idle** (nothing running), **working** (spinner/shimmer + step label + elapsed), **streaming** (partial content, stop control), **awaiting approval** (blocking card, focus moved to it, primary action clear), **done** (reasoning collapsed, actions row visible), **error** (red tint, short human reason, Retry, partial results preserved), **cancelled** (neutral note, what was kept).
- Announce status changes to assistive tech with a polite live region; make approval cards focus-trapped only when they block the flow, and keep Esc = Skip/dismiss.
