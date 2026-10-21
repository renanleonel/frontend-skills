# Easing equivalents

The library's defaults use GSAP ease names. Use these when the target is plain CSS / WAAPI / Motion.

| GSAP | CSS `cubic-bezier` | Motion (`ease`) |
|---|---|---|
| `power1.out` | `cubic-bezier(.25,.46,.45,.94)` | `[0.25, 0.46, 0.45, 0.94]` |
| `power2.out` | `cubic-bezier(.215,.61,.355,1)` | `[0.215, 0.61, 0.355, 1]` |
| `power3.out` | `cubic-bezier(.165,.84,.44,1)` | `[0.165, 0.84, 0.44, 1]` |
| `power4.out` | `cubic-bezier(.23,1,.32,1)` | `[0.23, 1, 0.32, 1]` |
| `power1.inOut` | `cubic-bezier(.455,.03,.515,.955)` | `[0.455, 0.03, 0.515, 0.955]` |
| `power2.inOut` | `cubic-bezier(.65,0,.35,1)` | `[0.65, 0, 0.35, 1]` |
| `power4.inOut` | `cubic-bezier(.86,0,.07,1)` | `[0.86, 0, 0.07, 1]` |
| `sine.inOut` | `cubic-bezier(.445,.05,.55,.95)` | `"easeInOut"` / `[0.445, 0.05, 0.55, 0.95]` |
| `back.out(1.7)` | `cubic-bezier(.175,.885,.32,1.275)` | `"backOut"` |
| `back.out(2)` | `cubic-bezier(.34,1.56,.64,1)` (approx.) | `[0.34, 1.56, 0.64, 1]` |
| `bounce.out` | no cubic-bezier — use CSS `linear()` or keyframes | not built in → keyframes, or a spring with low damping |
| `elastic.out(1, 0.3)` | no cubic-bezier — use CSS `linear()` or keyframes | spring `{ stiffness: 300, damping: 8 }` (approx.) |
| `elastic.out(1, 0.6)` | — | spring `{ stiffness: 170, damping: 12 }` (the library's spring default) |
| `none` / `linear` | `linear` | `"linear"` |

Notes:
- `bounce` and `elastic` can't be expressed with one cubic-bezier. In modern CSS, use `linear(...)` with sampled points, or a `@keyframes` sequence.
- After Effects: use Graph Editor easing (Easy Ease ≈ in-out); overshoot/elastic via expressions.
- Remotion: `Easing.bezier(...)` with the CSS values above, or `spring({ config: { stiffness, damping } })`.
