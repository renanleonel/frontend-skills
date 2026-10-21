# The 24 effects — full reference

Each effect: Portuguese name · when to use · how people ask (PT / EN) · default · example prompt.

## Entrances

### 01 · fade in (Surgir)
- **When:** subtle entrance for text or images.
- **Phrases:** "aparecer suave", "surgir", "ir aparecendo" / "fade it in", "appear softly".
- **Default:** opacity 0 → 1, 0.4s, `power2.out`.
- **Prompt:** "fade in the title over 0.4s" / "faz o título surgir com fade in em 0,4 s".

### 02 · slide in (Deslizar)
- **When:** a card, caption or image coming from one side.
- **Phrases:** "vir da direita", "entrar de lado", "deslizar" / "slide in from the right", "come in from the side".
- **Default:** 40–80px offset + fade, 0.5s, `power3.out`.
- **Prompt:** "slide the card in from the right in 0.5s".

### 03 · pop in (Aparecer com salto)
- **When:** icon, badge or number that needs attention.
- **Phrases:** "pular na tela", "aparecer estourando", "saltar" / "pop it in", "make it pop".
- **Default:** scale 0 → 1 passing the target, 0.35s, `back.out(1.7)`.
- **Prompt:** "pop in the subscribe button at the end".

### 04 · scale up (Crescer)
- **When:** giving weight to something central.
- **Phrases:** "crescer", "ir aumentando", "ganhar destaque" / "grow it", "scale it up".
- **Default:** scale 0.8 → 1 + fade, 0.6s, `power2.out`.
- **Prompt:** "scale the map up from 80% to 100%".

### 05 · blur in (Do borrado ao nítido)
- **When:** elegant entrance, a sense of focus.
- **Phrases:** "sair do desfoque", "entrar fora de foco", "ganhar nitidez" / "blur in", "come into focus".
- **Default:** blur 12px → 0 + fade, 0.6s, `power2.out`.
- **Prompt:** "bring the sentence in with a blur in".

### 06 · stagger (Cascata)
- **When:** lists, grids, several items.
- **Phrases:** "um depois do outro", "em sequência", "em fila" / "one after the other", "in sequence", "cascade".
- **Default:** 0.06–0.1s between items, each with the chosen entrance. Always in reading order.
- **Prompt:** "stagger the 5 topics in, 0.08s apart".

## Rhythm (the physics of movement)

### 07 · overshoot (Passa do ponto e volta)
- **When:** energetic movement, arrows, buttons.
- **Phrases:** "com tranco", "passa e volta", "com energia" / "with some punch", "overshoot and settle".
- **Default:** `back.out(2)`, 0.5s.
- **Prompt:** "move the block to the mark with overshoot".

### 08 · bounce (Quicar)
- **When:** something falling, light tone.
- **Phrases:** "quicar", "pingar", "cair e pular" / "bounce", "drop and bounce".
- **Default:** `bounce.out`, 0.8–1s.
- **Prompt:** "drop the ball and bounce it until it stops".

### 09 · spring (Mola)
- **When:** UI, something attached that stretches.
- **Phrases:** "como mola", "esticar e voltar", "molinha" / "springy", "stretch and snap back".
- **Default:** Motion/Framer `{ type: "spring", stiffness: 170, damping: 12 }`. GSAP ≈ `elastic.out(1, 0.6)`.
- **Prompt:** "animate with a spring, medium stiffness, low damping".

### 10 · ease in-out (Acelera e freia)
- **When:** any move between two points.
- **Phrases:** "suave", "natural", "sem robótico" / "smooth", "natural", "not robotic".
- **Default:** `power2.inOut` or `cubic-bezier(.65,0,.35,1)`. Almost always better than linear.
- **Prompt:** "move from A to B with ease in-out in 0.8s".

### 11 · elastic (Elástico)
- **When:** exaggerated emphasis, cartoon feel.
- **Phrases:** "tremer até parar", "borracha", "vibrar" / "wobble", "rubbery", "jiggle until it stops".
- **Default:** `elastic.out(1, 0.3)`, 0.8–1.2s.
- **Prompt:** "bring the number in with elastic".

### 12 · pulse (Pulsar)
- **When:** drawing attention to something already on screen.
- **Phrases:** "pulsar", "respirar", "piscar", "chamar atenção" / "pulse", "breathe", "draw attention".
- **Default:** scale 1 → 1.08 → 1, 1.2s per cycle, `sine.inOut`, loop.
- **Prompt:** "pulse the city marker on the map".

## Text & numbers

### 13 · typewriter (Máquina de escrever)
- **When:** text being typed, code, scripts, quotes.
- **Phrases:** "digitando", "letra por letra" / "typing", "letter by letter".
- **Default:** 25–40 chars/s, optional blinking cursor.
- **Prompt:** "type the quote letter by letter like an old document".

### 14 · count-up (Número contando)
- **When:** statistics, results, counters.
- **Phrases:** "o número subindo", "contar até" / "count up to", "number ticking up".
- **Default:** 1–2s, `power1.out`. Use `font-variant-numeric: tabular-nums` so the number doesn't jitter.
- **Prompt:** "count up from 0 to 1,500 years in 1.5s".

### 15 · word reveal (Palavra por palavra)
- **When:** dynamic captions, punchlines.
- **Phrases:** "palavra por palavra", "legenda aparecendo" / "word by word", "captions appearing".
- **Default:** 0.08–0.15s per word, or synced to speech timing.
- **Prompt:** "reveal the sentence word by word, synced to the voice".

### 16 · ticker (Letreiro rolando)
- **When:** breaking news, headlines, lists of names.
- **Phrases:** "letreiro", "faixa rolando", "rodapé de notícia" / "news ticker", "scrolling banner", "marquee".
- **Default:** constant linear speed; duplicate the content so the loop is seamless.
- **Prompt:** "add a ticker at the bottom with the channel topics".

### 17 · highlight (Grifar)
- **When:** marking the key word in a sentence.
- **Phrases:** "marca-texto", "destacar a palavra", "sublinhar" / "highlight", "marker", "underline the word".
- **Default:** background or underline growing from the left (`scaleX` 0 → 1, `transform-origin: left`), 0.4s, `power2.out`.
- **Prompt:** "highlight the word 'abandoned' from left to right".

### 18 · text swap (Trocar a palavra)
- **When:** cycling options at the end of a sentence.
- **Phrases:** "trocar a palavra", "alternar entre", "ficar mudando" / "rotate words", "cycle between".
- **Default:** old word exits up, new enters from below inside a mask (`overflow: hidden`), 0.3s, every 1–1.5s.
- **Prompt:** "swap the word every 1s between mystery, history and science".

## Shapes & transitions

### 19 · draw-on (Traço se desenhando)
- **When:** maps, routes, line charts, signatures.
- **Phrases:** "desenhar a linha", "traçar o caminho", "a rota se formando" / "draw the line", "trace the path".
- **Default:** `stroke-dasharray` = path length, animate `stroke-dashoffset` length → 0, 1.5–2s, `power1.inOut`.
- **Prompt:** "draw the expedition route on the map in 2s".

### 20 · mask reveal (Revelar por máscara)
- **When:** clean reveal of text or images.
- **Phrases:** "revelar", "aparecer por trás", "sair de dentro" / "reveal", "unmask", "come out from behind".
- **Default:** `clip-path: inset(100% 0 0 0)` → `inset(0)`, 0.6s, `power3.out` (bottom→top; flip the inset side for other directions).
- **Prompt:** "mask reveal the year 1969 from bottom to top".

### 21 · wipe (Cortina)
- **When:** changing scenes or states, before/after.
- **Phrases:** "passar por cima", "cortina", "limpar a tela" / "wipe", "curtain", "swipe across".
- **Default:** a solid block or `clip-path` crossing the frame, 0.5–0.7s, `power4.inOut`.
- **Prompt:** "show the before and after of the city with a wipe".

### 22 · punch zoom (Zoom de impacto)
- **When:** strong moments, numbers, punchlines.
- **Phrases:** "dar um soco no zoom", "zoom de impacto", "tranco" / "punch in", "impact zoom".
- **Default:** 100% → 115% in 0.15s, settle in 0.3s, on the beat or the strong word.
- **Prompt:** "punch zoom on '8 million' when the narrator says it".

### 23 · bar grow (Barra crescendo)
- **When:** bar charts, comparisons.
- **Phrases:** "barra subindo", "gráfico crescendo" / "bars growing", "animate the chart".
- **Default:** `scaleY` 0 → 1 with `transform-origin: bottom`, 0.6s, `power3.out`, staggered.
- **Prompt:** "grow the population bars by decade with a stagger".

### 24 · morph (Uma forma vira outra)
- **When:** transformations, before/after, changing icons.
- **Phrases:** "virar", "se transformar", "mudar de forma" / "morph", "turn into", "transform".
- **Default:** SVG path morph (same number of points), 0.6s, `power2.inOut`.
- **Prompt:** "morph the square into a circle".

## Bonus · Ken Burns
- **When:** still photos in a video — the most common documentary effect.
- **Default:** slow zoom ~5% over 6s, `sine.inOut` (optionally a slight pan).
- **Prompt:** "slow Ken Burns on the photo, about 5% over 6s".
