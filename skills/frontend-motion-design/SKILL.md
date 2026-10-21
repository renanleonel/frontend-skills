---
name: frontend-motion-design
description: >
  Renan's motion design library — turns vague animation asks ("make it pop", "one after
  the other", "faz o número quicar", "entra um depois do outro", "dá um tranco no zoom")
  into one of 24 named motion effects with the exact term, duration and easing. Use when
  asked to animate, add motion, a transition or an effect in HTML/CSS, GSAP, Motion
  (Framer Motion), Remotion, HyperFrames or After Effects — especially when the request is
  vague ("make a nice animation", "make it more dynamic") or the target is a video
  (faceless/documentary, explainer, promo). Also for picking an easing, converting GSAP
  eases to CSS, or choosing an accent color/theme for an animation.
---

# Frontend Motion Design

People rarely say the technical name of an effect. This skill bridges that: identify the effect from how the person talks, use the right term, and apply defaults that work on the first try.

Source: extracted from [apenasdouglas/ai-motion-library](https://github.com/apenasdouglas/ai-motion-library) (MIT, © 2026 Douglas Januário), Documentary version.

## Workflow

1. Match the request against the phrases in [references/effects.md](references/effects.md) (PT and EN).
2. If it matches, apply the effect with its **default** params. Only change duration, direction or intensity if the request says so.
3. **If the request is vague** ("make it nice", "dá uma animada", "more dynamic"), don't invent. Propose 2–3 effects from the library by name, say where each would go, and wait for a pick.
4. For a whole scene (video hook, big number, map, chapter change…), start from [references/recipes.md](references/recipes.md).
5. When delivering, name the effect(s) used in English (and Portuguese if the user wrote in PT), so the user learns the vocabulary.

## The 24 effects (index)

Defaults use GSAP ease names. CSS/Motion equivalents are in [references/easing.md](references/easing.md).

| # | Effect | Default |
|---|---|---|
| **Entrances** |||
| 01 | fade in | opacity 0→1, 0.4s, `power2.out` |
| 02 | slide in | 40–80px offset + fade, 0.5s, `power3.out` |
| 03 | pop in | scale 0→1 with overshoot, 0.35s, `back.out(1.7)` |
| 04 | scale up | scale 0.8→1 + fade, 0.6s, `power2.out` |
| 05 | blur in | blur 12px→0 + fade, 0.6s, `power2.out` |
| 06 | stagger | 0.06–0.1s between items, each with the chosen entrance |
| **Rhythm** |||
| 07 | overshoot | `back.out(2)`, 0.5s |
| 08 | bounce | `bounce.out`, 0.8–1s |
| 09 | spring | Motion: `{ type: "spring", stiffness: 170, damping: 12 }`; GSAP ≈ `elastic.out(1, 0.6)` |
| 10 | ease in-out | `power2.inOut` / `cubic-bezier(.65,0,.35,1)` |
| 11 | elastic | `elastic.out(1, 0.3)`, 0.8–1.2s |
| 12 | pulse | scale 1→1.08→1, 1.2s/cycle, `sine.inOut`, loop |
| **Text & numbers** |||
| 13 | typewriter | 25–40 chars/s, optional blinking cursor |
| 14 | count-up | 1–2s, `power1.out`, `tabular-nums` |
| 15 | word reveal | 0.08–0.15s per word, or synced to speech |
| 16 | ticker | constant linear speed, duplicated content for seamless loop |
| 17 | highlight | bg/underline `scaleX` 0→1 from left, 0.4s, `power2.out` |
| 18 | text swap | out up / in from below with mask, 0.3s, every 1–1.5s |
| **Shapes & transitions** |||
| 19 | draw-on | `stroke-dasharray`/`stroke-dashoffset`, 1.5–2s, `power1.inOut` |
| 20 | mask reveal | `clip-path: inset(100% 0 0 0)` → `inset(0)`, 0.6s, `power3.out` |
| 21 | wipe | block or `clip-path` crossing, 0.5–0.7s, `power4.inOut` |
| 22 | punch zoom | 100%→115% in 0.15s, settle in 0.3s, on the beat/strong word |
| 23 | bar grow | `scaleY` 0→1, origin bottom, 0.6s, `power3.out`, staggered |
| 24 | morph | SVG path morph (same point count), 0.6s, `power2.inOut` |
| *bonus* | Ken Burns | slow zoom ~5% over 6s, `sine.inOut` — most common effect on still photos |

## Rules that prevent ugly animation

- **Max 2 effects per element.** Entrance + emphasis (e.g. slide in + highlight) is enough.
- **Motion without easing looks robotic.** Linear only for tickers and continuous rotation.
- **Exit faster than entrance:** exit ≈ 70% of the entrance duration.
- **Stagger in reading order:** top→bottom, left→right.
- **In video, sync to speech:** the effect lands on the word it illustrates, not before.

## Color & theme

- **Default:** accent red `#E5352A`, dark theme (bg `#0E1110`, white text).
- **Light theme:** cream bg `#F5F0E6`, warm near-black text `#1A1512`.
- **User picks** by name ("use blue"), hex ("use `#2F6FED`") or args (`color #2F6FED theme light`). Remember the choice for every animation in the conversation.
- **Named colors:** red `#E5352A`, blue `#2F6FED`, green `#1F9D60`, yellow `#E2A925`, orange `#EE6A24`, purple `#7C4DFF`.
- **Contrast:** accent is fine on large text and shapes. On small text, if contrast < 4.5:1 against the bg, darken the accent (light theme) or lighten it (dark theme) until it passes. Text on an accent block: use the bg color or a near-black, whichever passes.
- Put the accent in a single variable (e.g. `--accent`) so it can be swapped later.

## Tool names

The English terms are what GSAP, Motion/Framer, Remotion, HyperFrames, CSS and After Effects understand. Params use GSAP ease names; in plain CSS use the `cubic-bezier` equivalents from [references/easing.md](references/easing.md). Respect `prefers-reduced-motion` in UI work (swap movement for a short fade).
