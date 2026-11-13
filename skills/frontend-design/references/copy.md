# Copy

Product writing: labels, buttons, errors, empty/loading/success text, links, tone, numbers and consistency. Read before writing or reviewing any user-facing string. Markup for errors and announcements: see `accessibility.md`. Casing and punctuation rendering: `typography.md`. Layout room for translated strings: `edge-cases.md`.

## Method

**Read the surrounding copy before writing.** Note the product's terms, casing, localization setup and any style guide. A deliberate brand voice is not a defect; flag it only when it causes inconsistency, ambiguity, translation risk or a tone the stakes can't carry.

**Review the whole interaction path, not isolated strings.** Look for: ambiguous verbs/nouns, internal jargon, vague outcomes, missing consequence or recovery, mixed terminology, redundant headings/intros/helper text, and text that breaks at real widths or in translation.

**Per state, decide in this order:** the one fact the user needs now, the next available action, context that changes the decision, then tone. Say each idea once; if the heading explains the state, the intro adds new information or goes.

**Ask before changing factual claims, legal meaning or domain-specific terms.** Refinement keeps existing copy; don't invent claims.

**Final copy is as short as it can be without losing meaning or the recovery path.**

## Voice and tone

**One voice, tone scaled to stakes.** A local edit never invents a new voice.

| Context | Tone |
| --- | --- |
| Success, onboarding, empty states | Warm, may be light |
| Routine actions, settings | Neutral, minimal |
| Errors, destructive confirmations | Calm, plain, no playfulness |
| Data loss, payment, security, access loss | Serious, explicit; warmth ok, jokes never |

**Use one copy register per page.** Don't mix technical mono ("47 tasks · 0.6 ctx-switches/day"), editorial prose and marketing punch unless the brand calls for it.

**Plain words a tired reader gets on the first pass.** Delete words that do no work. No idioms, colloquialisms or humor that won't translate.

**Address the reader as "you" in instructions, not "the user".** In errors avoid "we" (reads as deflection): "Unable to load content", not "We're having trouble loading this". Keep an established first-person voice only in low-stakes copy.

**Prefer "Favorites" over "Your Favorites".** Possessives add noise. Hold one perspective across a flow.

**Skip needless gender** ("Subscribers can post recipes"). Match the input device: "tap" on touch, "click" with a pointer, "select" when both apply.

## Buttons and actions

**Start button labels with a verb and object when the outcome isn't obvious:** "Save draft", "Delete project", "Invite member". Never "OK!", "Let's go!", "Submit", or bare Yes/No on a consequential action.

**Describe the outcome, not the gesture.** "Export report", not "Click to export".

**Make the confirm button restate the consequence** so the dialog is answerable without reading the body: title "Delete this project?" with `Delete project` and `Cancel`.

**Name the object and the consequence on destructive actions** ("Delete 12 files permanently"). Prefer undo over a confirmation when recovery is safe.

**One label per intent across a page.** "Get in touch" + "Contact us" + "Let's talk" is three labels for one intent: pick one for nav, hero and footer. Same for sign-up and portfolio CTAs.

**Keep primary CTAs to 1-3 words and on one line at desktop.** If it wraps, shorten the label rather than constraining width.

**Use one vocabulary across a multi-step flow:** "Get started" to enter, "Continue" or "Next" (pick one) to advance, "Done" to finish. Alternating synonyms makes users suspect different behavior.

## Links

**Link text must make sense out of context** (screen readers list links): "Read the billing docs". Never "click here".

**Disambiguate repeated links.** Two "Learn more" on a page become "Learn more about exports" and "Learn more about billing".

**Link straight to a setting instead of describing the path.** A "Notification settings" link, not "Go to Settings > Notifications > Email".

## Capitalization and consistency

**Pick one casing per element type and apply it everywhere. Default to sentence case.** Calmer, no per-word rules, localizes cleanly. "Save Changes" next to "Discard changes" reads as sloppy.

**One term per concept across the product.** "Archive" in the menu is "Archive" in the toast, not "Move to storage". Keep a short glossary when inconsistency spans the product.

**Treat required/optional the same way everywhere** in forms.

## Toggles and settings

**Label a toggle for its ON state:** "Send read receipts". Negative labels ("Don't send read receipts") create a double negative when off.

## Forms

**Keep a visible label on every field; placeholders only show example format** (`name@example.com`, `DD/MM/YYYY`). A placeholder disappears on input and often fails contrast. Label above input, helper text optional, error below (layout: `interaction.md`).

**State format and eligibility rules before submission, not after the mistake.** Explain why data is requested only when it isn't obvious.

**Phrase hints positively:** "Use only letters", not "Don't use numbers or symbols".

## Errors

**Write errors as instructions, placed next to the field that failed.** Answer: what failed, why (only if known and useful), how to recover or what alternative remains.

| Bad | Good |
| --- | --- |
| That password is too short | Choose a password with at least 8 characters |
| Invalid name | Use only letters for your name |
| Oops! Something went wrong. | Unable to save. Check your connection and try again. |
| Error 500 | Unable to load invoices. Try again, or contact support if it keeps happening. |

**No blame, no "oops", no exclamation marks, no raw codes or stack text as the primary message.** Don't promise a cause or fix the system can't know.

**Preserve the user's input on error.** Tell them it's kept if that's not obvious.

**If the same error keeps firing, redesign the interaction** (constrain input, add a picker, auto-format) instead of rewording. The best error is the one that cannot happen.

**Never leave an error generic** ("Error occurred", "Something went wrong") when the failure is knowable.

## Empty states

**An empty state says what this place is, how to fill it, and offers one clear action.**

```tsx
// Bad: a shrug
<p>No results.</p>

// Good: orientation + next step
<p className="font-medium">No projects yet</p>
<p className="text-sm text-muted-foreground">Projects keep your tasks and files together.</p>
<Button className="mt-4">Create a project</Button>
```

**Distinguish the cause:** first use, no search results, filters hiding everything, no permission, failed load. Each gets its own message.

**Search/filter empties name the query and offer an exit:** "No results for 'quarterly'. Clear filters".

**Never put persistent information in an empty state;** it vanishes once content exists.

## Loading and success

**Name the real operation:** "Loading your projects…", "Importing 240 contacts…". Give an honest time expectation when the wait is meaningful. Show determinate progress when available; never fake it.

**Success confirms the completed outcome in brief.** Mention a next consequence only if it changes what the user should do. Routine success: "Saved", "Link copied".

## Helper text and alt text

**Helper text answers an implicit question; it never restates the label.** Put uncommon detail behind progressive disclosure.

**Alt text conveys the image's information; use empty `alt=""` for decoration.** Icon-only controls get an accessible name that matches the visible label and outcome.

**Don't let punctuation, color or an icon carry the message alone.**

## Numbers, dates, pluralization

**Never build sentences from fragments around a variable** (`"You have " + n + " new messages"`). Word order differs per language. Use one full templated string with real pluralization (`Intl.PluralRules` or an i18n library). `${n} item${n !== 1 ? 's' : ''}` fails for many languages.

**Keep variables structured so translators can reorder them;** allow text expansion (~30-40% budget) rather than abbreviating early.

**Format with `Intl`, never by hand:** `Intl.NumberFormat` (separators, currency, compact), `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`. Show "just now" instead of "0 seconds ago"; switch relative to absolute dates after about a week. Tabular figures for live numbers: `typography.md`.

**Don't invent precision.** Numbers like `92%`, `4.1×`, `48k` need a real source or an explicit mock label. Placeholder content in a shipped UI reads as fake.

## Marketing and landing copy tells

**Self-audit every visible string before shipping** (headlines, buttons, captions, alt text, errors). Rewrite any that is grammatically broken, has an unclear referent, forces a metaphor, or sounds like an LLM being thoughtful. When unsure, use a plain functional sentence; cute AI copy is worse than boring.

**Keep headlines to about 8 words, section sub-copy to about 25, hero sub-copy to about 20.** If the value proposition won't fit, it's unclear; don't loosen the limit.

**Avoid these tells:**
- Poetic section labels ("Field notes", "Currently on the bench"). Use plain ones: "Testimonials", "Latest writing".
- Generic step labels ("Step 1 / Phase 01"). Use the verb: "Install", "Configure", "Ship".
- Meta-sentences under headings ("This list will stay short on purpose").
- "Scroll to explore" cues, version/BETA stamps as hero eyebrows (unless the brief is a launch), `01 / 4` counters on tiles.
- Eyebrows above every section: at most one in three sections, otherwise drop them.
- Placeholder people and brands ("John Doe", "Acme", "Nexus", "SmartFlow"). Use plausible, locale-appropriate names.
- "It's not X, it's Y" / "Not just X. Y." contrast-framing. Say what the thing is.
- Em dashes as a stylistic crutch (choose: comma, colon, period, parentheses). Proper ranges with en dash: `typography.md`.
- Industry captions under logos in a logo wall; logos stand alone.

## Review output

**Severity:** HIGH misleads or hides recovery from an error. MEDIUM breaks voice, terminology or casing consistency. LOW is isolated polish.

**Report one row per root cause, grouped by principle violated, worst first** (source is enough; no browser check needed):

| Severity | Location (`path:line`) | Before | After | Why |
| --- | --- | --- | --- | --- |

End with Block if any HIGH remains, otherwise Approve. Never approve code you didn't inspect.

**Verify before handoff:** comprehension without product knowledge; every error has a stated fix; terminology matches; readable at target widths and 200% zoom; long names, translation expansion, plurals and dynamic values hold up; state changes have accessible announcements.
