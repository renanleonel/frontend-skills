How to review, audit, critique or polish an interface: scope, check order, severity, evidence rules and the report format. Read when asked to review a diff, file, component, page or flow, or to give a final quality pass before shipping.

## Pick the review type

One process, four entry points. Decide which the request is, say so, then run the same pipeline.

| Request | Type | Output |
| --- | --- | --- |
| "Review these changes / my PR / uncommitted work" | **Change review** | Findings with a status per finding |
| "Review / audit this screen, component, flow" | **Surface review** | Findings table, coverage, verdict |
| "Critique this design" (judgment, not code defects) | **Critique** | Heuristic scores, persona red flags, strengths, priorities |
| "Polish this before we ship" | **Polish** | Fixes applied, not a report |

Reviews are read-only by default. Edit source only when asked to fix. Polish and fix requests are the edit case: keep the report as the change scope and re-verify afterward.

## Resolve the scope first

**State the resolved scope in the output.** Never imply surfaces were reviewed that you did not inspect. If the scope is too big to inspect credibly, narrow it to one complete flow (the one the request centers on, otherwise the entry path every user passes), and say what was excluded.

### Diff scope (change review)

The question is "did this change make the interface worse?", so report what the change caused and stay quiet about what it merely touched.

- **No target given: resolve in this order and stop at the first match.** (1) `HEAD` is ahead of `git merge-base origin/<default> HEAD`: that range plus uncommitted changes, with the two counts stated separately. (2) Dirty working tree: uncommitted changes. (3) Neither: there is nothing to review. Check the merge base before the working tree, or one stray edit hides a twelve-commit branch.
- **Nothing to review: ask, don't invent.** Do not fall back to `HEAD~1..HEAD` on your own. State the facts (branch, clean tree, commits ahead, last commit short SHA and subject, any open PR), then offer: the last commit, a target they name, or a whole-repo audit (which is not a change review).
- **Diff against the merge base with three dots** (`base...HEAD`). Two dots reports upstream commits as part of the change. When the user wrote an explicit `a..b` or `a...b`, keep their dots.
- **Include untracked files.** `git diff HEAD` skips new files; pair it with `git ls-files --others --exclude-standard`, or new components vanish from a scope you call complete.
- **PRs:** fetch the head into a remote-tracking ref (`git fetch origin pull/<n>/head:refs/remotes/pr/<n>`), read files with `git show <ref>:path`, and cite line numbers against that ref. Never check out the PR or switch branches in the user's tree. For rendered checks use a throwaway worktree and remove it afterward.
- **Exclude machine-authored paths and list them:** lockfiles, snapshots, build output (`dist/`, `.next/`, `coverage/`), generated sources, vendored code, binaries. Exceptions stay in: a swapped font file (typography) and an image added to a component (alt text, outline). Run the diff with and without the pathspecs and confirm the count dropped by exactly what you named.
- **Stop on unreviewable states:** mid-rebase or mid-merge, unresolvable base, unrelated histories. A shallow clone: deepen and retry before giving up. Never review a range you cannot name.
- **Read the intent.** PR title and body, linked issue and commit messages define what "incomplete" means. Do not report scope creep; that is a process question.
- **Expand to the blast radius.** A changed file is evidence; the surfaces it renders in are the subject. Go one hop (direct importers), two for design tokens, theme values and shared primitives. For a token, search its name, not its file. Review at most five consumers, ordered by route/layout entry points first, then importer count, then proximity, and state how many you skipped.
- **Read the removed (`-`) lines.** Regressions are invisible in the post-change state. Search deleted lines for lost accessibility, focus, language and text signals:
  ```bash
  git diff -U0 "$BASE"...HEAD -- '*.tsx' '*.css' | grep -E '^-[^-]' | grep -E 'aria-|role=|alt=|focus|tabindex|prefers-|text-wrap|tabular|lang=|dir='
  ```
  A removal is a lead, not a finding. Confirm nothing in the change replaces it before reporting. Equivalent replacements are fine: `aria-labelledby` for `aria-label`, a native element for an explicit `role`, a `box-shadow` focus ring for `outline` that still passes, a token that measures the same pair, a logical property for a physical one, a string moved into the i18n catalog.
- **Check completeness against intent.** The incomplete change is the one a surface review cannot see: a new variant missing hover/focus/disabled/loading, a new string absent from the translation catalog, a new component with no empty/loading/error/narrow state, a control added to one surface but not its siblings.
- **Status every finding:** `Introduced` (the change created it), `Regression` (weakened something that was correct), `Pre-existing` (present in touched code, not caused by it). Status by what the diff touched, not by file; confirm with `git blame` against the base when unsure.
- **Cap pre-existing at 3**, listed apart, outside the verdict. Touching a legacy file must not become a full-file audit.

### File or component scope

Read the file, its styles and tokens, and the components it composes. Then render it if you can (Storybook, dev server) in its states: default, hover, focus, active, disabled, loading, empty, error, long content, narrow width. Cite file and line.

### Page, screen or flow scope

Inspect the rendered result at desktop and mobile widths (320px and a wide viewport at minimum) plus 200% zoom, and the source behind it. Walk the primary task with mouse, keyboard and touch. Include empty, loading and error states where they exist. Mark anything you could not render **Not verified**.

### Recon (all scopes)

Identify the framework, styling system (Tailwind config, CSS variables), component library, tokens, supported viewports and any preview/test command. Write every fix in the project's own idiom. Read project docs that describe the interface (`AGENTS.md`, `CLAUDE.md`, design-system docs, Storybook, ADRs) and name what you found. These decide where a finding is reported (if a shared token or guideline is the cause, report it once against that source), not whether it is reported: a documented convention is no proof the convention is good.

## Check order

**Review foundations first so polish does not hide blockers.** Go through the domains in this order and finish each before consolidating. Each domain's rules live in its own file; apply them, do not restate them here.

1. **Accessibility** (`accessibility.md`; contrast numbers in `color.md`).
2. **Layout and responsive** (`layout.md`): hierarchy, grouping, reading order, spacing, 320px reflow.
3. **Interaction and states** (`interaction.md`): every state, forms, keyboard, hit areas, overlays, feedback.
4. **Copy** (`copy.md`): labels, errors, empty states, consistency.
5. **Typography** (`typography.md`).
6. **Color and theming** (`color.md`): tokens, contrast pairs, dark mode, hard-coded values.
7. **Surfaces and details** (`surfaces.md`, `details.md`): radius, borders/shadows, icons, polish.
8. **Edge cases** (`edge-cases.md`): worst-case data.
9. **AI surfaces** (`ai-interfaces.md`), only if the UI streams, chats or acts as an agent.
10. **Taste and specificity** (`anti-slop.md`): does it feel authored for this product, or interchangeable?

Motion is reviewed through `frontend-motion-design`; performance through `frontend-performance`. Note the concern once and move on.

**Domain not touched or not inspected:** mark `Not reviewed` with the reason (for a change review: "no evidence in the change scope"). `Clear` means inspected with nothing actionable. Never mark a domain `Clear` you did not look at.

**Overlap goes to the owner of the underlying rule.** Report an issue once, with secondary effects in the Why column.

## Severity

Use four levels. Decide by user impact; ask "would a user contact support?" and if so it is at least P1.

| Level | Meaning | Action |
| --- | --- | --- |
| **P0 Blocker** | Prevents task completion, loses data, hides content or controls | Fix now |
| **P1 Major** | Serious difficulty, misleads, or fails WCAG AA; systemic failures repeated across screens | Fix before release |
| **P2 Minor** | Annoyance with a workaround; consistency and comprehension cost | Next pass |
| **P3 Polish** | Isolated, little task impact | If time allows |

**Escalation triggers are P1 minimum on sight** (P0 when the user cannot finish the task), however minor the surface. Do not average them down:
- Interactive control with no accessible name.
- Keyboard-reachable control with no visible focus indicator.
- A control or path reachable by pointer but not keyboard.
- Content or control clipped, overlapped or unreachable at 320px or 200% zoom.
- Text or control whose rendered contrast fails its required ratio.
- State or meaning carried by color alone, or by motion alone with nothing left behind when motion is off.
- Auto-playing motion that ignores `prefers-reduced-motion`.
- Destructive action with no confirmation, undo or distinct treatment.
- Truncated content with no way to reach the full value.
- Content only reachable past a scroll edge or disclosure with no visible cue.
- An error that gives no way to recover.
- A semantic color used against its meaning (danger red on a harmless action).

In a change review, a confirmed `Regression` against a trigger is P1 even where the same symptom would be P2 pre-existing.

**Rank within a level by reach and leverage.** A token or shared-component fix beats the same symptom in one leaf. Triggers come first; if the cap hides some, say how many.

## Evidence and discipline

**The bar for a finding is evidence, not taste.** Every finding cites `path/file:line` (or screen + component when there is no source) and shows the current implementation. A density, radius or voice you merely disagree with is not a finding; a trigger is a finding whatever the style guide says. Do not report a code-level issue from appearance alone, or a visual issue from source alone, when runtime behavior decides it.

**Run the cheap checks available** (lint, typecheck, tests, a11y linters, the dev server) and report the exact command and result. A check you cannot run is **Not verified**, never a finding. A clean automated scan does not replace looking at the rendered result.

**Verify false positives.** Tool output is defect evidence, not proof. Open the context before reporting.

**Prefer the cheapest fix; propose the earliest rung that works:**
1. Delete (a separator space can carry, a redundant ARIA attribute, an unused ramp).
2. Use the platform (native element, native control, browser focus ring).
3. Reuse what the project has (existing token, spacing step).
4. Correct the value (exact radius, gap, contrast pair).
5. Add (new token, wrapper, media query).
Proposing step 5 where step 1 worked is itself a finding.

**One root cause is one row.** List every affected location in the row. Never pad to reach the cap; a short report or "No actionable interface findings." is a valid result. Cap: 15 findings per review.

**Fix the cause at the narrowest correct level:** missing token (add it), one-off implementation (replace with the shared component), conceptual mismatch with neighboring flows (fix the flow), local defect (fix in place). Ask when a binding system principle cannot be inferred.

## Critique mode (design judgment)

Use when the request is about whether the design works, not whether code is defective. Run two passes and keep them independent if you can (spawn two sub-agents when the user has asked for delegation; otherwise do the judgment pass first, then run tools, and say so).

1. **Design pass:** specificity (could an unrelated product use this unchanged?), hierarchy, IA, emotional fit, discoverability, composition, states, copy.
2. **Evidence pass:** automated checks, browser inspection, console errors, rendered widths.

**Score the 10 usability heuristics 0-4** (honest: 4 is genuinely excellent; most real UIs land 20-32 of 40): system status, match with real world, user control and freedom, consistency and standards, error prevention, recognition over recall, flexibility and efficiency, minimalist design, error recovery, help. Mark a heuristic `n/a` with a reason when it cannot apply (efficiency and help on a landing page) and divide by the applicable maximum. Bands by percentage: 90%+ excellent, 70%+ good, 50%+ acceptable, 30%+ poor, below that critical.

**Cognitive load check, count failures:** single focus, chunking (about 4 items per group), grouping, clear hierarchy, one decision at a time, minimal choices (about 4 visible options per decision point; 8+ means overload), no cross-screen memory demands, progressive disclosure. 0-1 failures low, 2-3 moderate, 4+ critical. Working-memory limit is roughly 4 items; one primary action, one or two secondary, the rest grouped.

**Walk the primary task as 2-3 personas that fit the surface and report what breaks, specifically:**
- **Power user:** shortcuts, bulk actions, skippable onboarding, Esc closes overlays.
- **First-timer:** first action clear in about 5 seconds, labeled icons, no jargon, visible help, confirmation after actions.
- **Accessibility-dependent user:** keyboard-only flow, focus visible, names and alt text, status announced, no color-only meaning, 200% zoom.
- **Stress tester:** empty, 1,000 items, long text, emoji, refresh mid-flow, back button, double submit (`edge-cases.md`).
- **Distracted mobile user:** thumb reach, 44px targets, state survives interruption, minimal typing.
Landing pages: first-timer, stress tester, mobile. Dashboards: power user, accessibility. Checkout: mobile, stress tester, first-timer. Forms/wizards: first-timer, accessibility, mobile.

Be direct and concrete ("the submit button", not "some elements"); say what is wrong and why it matters; cut "consider exploring". Include 2-3 genuine strengths. End with a few questions tied to actual findings (priority area, intended tone, scope) when 3+ priority issues exist.

## Audit extras (technical health)

For "audit this" requests, optionally score 0-4 per dimension and total out of 20 (18-20 excellent, 14-17 good, 10-13 acceptable, 6-9 poor, below 6 critical): accessibility, responsive (fixed widths, 44px targets, horizontal scroll, text scaling), theming (hard-coded colors, broken dark mode, inconsistent tokens), implementation integrity (system drift, decorative or misleading content, repeated shortcuts, a structure interchangeable with any product), and performance (delegate details to `frontend-performance`). Name systemic patterns ("hard-coded colors in 15+ components: add a token") and what already works so it is kept.

## Polish mode (final pass, fixes applied)

Polish refines; it never conceals a redesign. If the concept itself is wrong, say so and recommend a redesign or `anti-slop.md` bolder pass instead of replacing it quietly.

1. **Establish the system:** read tokens, shared components, neighboring flows. Classify each drift (missing token, one-off, conceptual mismatch, local defect) before fixing.
2. **Use the feature** at representative sizes; confirm the path is functionally complete and note the real content lengths, roles and inputs.
3. **Triage and fix in this order:** broken or blocked tasks, data loss, misleading state, inaccessible paths; missing loading/empty/error/success/disabled/permission states; flow, hierarchy and responsive drift; visual inconsistencies; code and asset cleanup. Do not perfect one corner while the rest sits below the bar.
4. **Sweep the whole path:** matching terminology and save behavior across neighbors; alignment to the grid including optical alignment; same-role typography consistent; icon family, stroke and size coherent; focus, tab order and labels intact; no layout shift from images.
5. **Clean up:** remove debug output, dead code, unused imports and obsolete styles; replace one-offs with shared components; promote a value to a token only when truly reusable.
6. **Verify in one batched round, fix, confirm once.** Mobile, intermediate and wide; loading/empty/error/long/missing content; zoom, contrast, focus, semantic names; console errors; agreement with neighboring features and the user's scope. Stop after that; open-ended self-QA wastes effort and the diff cleanup is the finish. Ship only when the path is complete and consistent.

## Report format

Keep it compact. Open with scope, then findings, then verification and verdict.

**1. Scope and coverage.** Target and resolved scope, stack, convention docs found, exclusions, expansions (and how many consumers skipped). For change reviews add base ref, head ref, commit and file counts.

| Domain | Evidence inspected | Result |
| --- | --- | --- |
| Accessibility | files, states, checks | N findings / Clear / Not reviewed (why) |

List every domain from the check order.

**2. Findings.** One table, ordered by severity then reach. Before and After belong in cells of one row, never as separate lines.

| Sev | Domain | Status* | Location | Before | After | Why |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | Accessibility | Regression | `src/Dialog.tsx:42` | `aria-label` removed from `<button><X/></button>` | restore `aria-label="Close"`; hide the icon from the a11y tree | icon-only control lost its name |

\*Status column only for change reviews. Location is `path:line` against the head ref. Why names the violated principle and the user impact. Consolidate repeats into one row listing every location. With no findings write "No actionable interface findings."

**3. Pre-existing (change reviews only).** Max 3, highest severity first, labeled as not this change's responsibility.

**4. Verification.** Commands and interactions run with observed results; separately list **Not verified** items.

**5. Verdict.** `Block` if any P0 or P1 remains; otherwise `Approve`, with P2/P3 left as work to do. Never approve a domain you did not inspect, and never approve an empty scope. A pre-existing-only report is an `Approve`.

**Rules for the report:** one ranked table, not six domain reports; show which domains and states were actually inspected; name the strongest 2-3 things that work when a critique or audit asks for it; end with the next step (which reference file or fix to start from).
