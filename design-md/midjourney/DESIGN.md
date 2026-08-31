# Midjourney — Design System

> **North Star**: Deep-ocean bioluminescent terminal. A pressurized darkness where intelligence visibly generates itself in ASCII streams, and controls appear as faintly glowing specimens.
> **Theme**: dark
> **Source**: https://midjourney.com
> **Refero Style**: https://styles.refero.design/style/225059ac-0450-49d3-b2b7-d0e98b7ae938
> **Synced**: 2026-09-01

## Overview

Midjourney's interface feels like peering through a deep-ocean porthole into a bioluminescent void — vast, pressurized darkness with faint light sources. The #06051d near-black with violet undertone is not simply dark but dimensionally deep, distinguished from pure black by that violet warmth that reads as cosmic rather than void. A sprawling ASCII/generative text animation fills the hero against this background, making the interface itself feel like it's generating intelligence in real time. Section headings and nav use JetBrains Mono exclusively — monospace as aesthetic choice, not technical necessity, giving every label the weight of a terminal command. The three pill buttons (Sign Up, Log In, Explore) float as translucent jewels — each tinted a different hue (green, yellow, red-orange) at 20% opacity against their dark backgrounds, with matching text colors, making them feel less like CTAs and more like categorized data packets.

## Color Palette

- **Cosmic Void**: `#06051d` — Primary page background and hero fill — the violet undertone separates it from neutral black, making darkness feel galactic rather than empty [brand]
- **Abyssal Blue**: `#0f1c36` — Secondary surface backgrounds, button background variant — a step lighter than Cosmic Void for subtle depth layering [brand]
- **Steel Navy**: `#1d293d` — Card surfaces, nav background, interactive container backgrounds [neutral]
- **Deep Slate**: `#314062` — Elevated card or hover state backgrounds [neutral]
- **Mist**: `#cad5e2` — Primary body text, general UI text — slightly blue-gray rather than pure white, reducing harshness against the dark void backgrounds [neutral]
- **Fog**: `#e5e7eb` — Borders, dividers, icon strokes throughout the UI [neutral]
- **Ash**: `#2e3038` — Secondary text, subdued labels [neutral]
- **Ghost White**: `#ffffff` — Heading text at maximum contrast [neutral]
- **Ice Blue**: `#ebf8ff` — High-brightness text on dark surfaces, link contrast text [neutral]
- **Portal Blue**: `#63b3ed` — Hyperlinks, inline text links — the single fully saturated accent visible in body content, connecting to Midjourney's Discord/community ecosystem [accent]
- **Bioluminescent Green**: `#004f3b` — Sign Up pill button background (20% opacity tint) — deep green specimen glow against void [accent]
- **Terminal Amber**: `#733e0a` — Explore pill button background (20% opacity tint) — amber specimen variant [accent]
- **Crimson Depth**: `#8b0836` — Log In pill button background (20% opacity tint) — deep red specimen variant [accent]
- **Specimen Green**: `#00bc7d` — Icon strokes and decorative SVG fills — vivid but used sparingly in iconography only [semantic]
- **Warning Amber**: `#f0b100` — Icon and UI accent strokes — section heading icons (Projects ⚙, About ℹ) [semantic]
- **Fault Red**: `#ff2056` — Icon strokes, error-adjacent SVG fills [semantic]

## Typography

- **JetBrains Mono**
- **DM Sans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.63 |
| body | 16 | — | 1.5 |
| heading | 30 | — | 1.25 |

## Spacing & Layout

- **Max Width**: 800px
- **Card Padding**: 32px
- **Element Gap**: 8-16px
- **Section Gap**: 64px
- **Border Radius**: {'cards': '8px', 'images': '8px', 'inputs': '8px', 'buttons': '9999px'}

## Layout

Narrow centered column layout with a max-width of approximately 800px — deliberately constrained for a research lab publishing cadence rather than a marketing site. The hero is full-viewport dark with centered ASCII text animation and overlaid logo, creating an immersive first screen before content begins. Below the hero, content flows as a single column of prose sections separated by 64px vertical gaps. Section headings use a left-aligned icon + label pattern. The Projects section breaks into a 4-column image grid with 8px gaps. Navigation is a full-width sticky bar at the top with left-aligned text links and right-aligned pill button cluster — no hamburger menu, no mega-menu, no sidebar. The layout is deliberately text-document-like: a long scrolling page of research notes with visual inserts, not a feature-driven marketing layout.

## Surfaces / Elevation

- **Cosmic Void**
- **Deep Navy Gradient**
- **Abyssal Blue**
- **Steel Navy**
- **Deep Slate**

## Imagery

All imagery on this site is AI-generated — square-format monochromatic renders in blue-violet tones depicting anatomical and symbolic subjects: an eye with radiating iris lines, a stylized brain, a heart, a human hand, a profile of a head, lips, an arched passage, and a needle. Each image is contained in an 8px-radius tile with no text overlay. The color treatment is consistent: desaturated blue-violet with slight 3D relief texturing, making them feel like scientific specimens under ultraviolet light. No photography, no lifestyle imagery, no illustrations in the traditional sense. The hero visual is a generative ASCII sphere — thousands of characters forming a 3D ellipsoid — which is the primary 'image' of the page. Icon usage is minimal: small colored glyphs (gear, info circle) in amber preceding section headings. The visual content IS the product demonstration, not a metaphor for it.

## Design Principles

### Do

- Use JetBrains Mono as the primary typeface for all UI elements — navigation, headings, buttons, body copy — treating monospace as the visual identity, not a code-context exception.
- Apply the three-color pill button system (green/amber/red tints at ~20% opacity) only for the Sign Up / Explore / Log In triad — do not extend the specimen-color scheme to other button types.
- Set all page backgrounds to #06051d or the gradient variant linear-gradient(0deg, #06051d 30%, #061434) — never use pure #000000, which would flatten the violet cosmic depth.
- Use 9999px border-radius for all pill buttons and 8px for all card/image containers — no intermediate values; the contrast between fully rounded and gently rounded is the shape system.
- Render section headings at 30px JetBrains Mono weight 400 with a small amber #f0b100 icon prefix — never increase to bold weights, the whisper-weight at large sizes is the signature.
- Use #63b3ed Portal Blue exclusively for inline hyperlinks and flat navigation text links — it is the only fully visible chromatic color in body content.
- Maintain 64px vertical gap between page sections to preserve the spacious, pressurized-void atmosphere between content blocks.

### Don't

- Do not use any sans-serif or serif font as a heading font — DM Sans is for body prose only; JetBrains Mono must dominate the typographic hierarchy.
- Do not create solid-fill opaque buttons — the translucent 20% opacity tinted backgrounds on pills are the system; solid fills break the bioluminescent specimen aesthetic.
- Do not introduce light backgrounds (#ffffff, light grays) into page sections — the design has no light mode; all surfaces must remain within the #06051d to #314062 dark range.
- Do not use more than three accent tint colors for buttons — the red/green/amber specimen triad is a closed system; adding new button colors dilutes the precision.
- Do not bold section headings or use font-weight above 500 anywhere in the UI — weight 400 at display sizes is the deliberate anti-convention choice that defines the visual voice.
- Do not add decorative imagery or photography — the only permitted visuals are AI-generated monochromatic renders and the ASCII/generative text hero.
- Do not apply colored backgrounds to body text sections — prose content must sit directly on #06051d Cosmic Void with #cad5e2 Mist text, no content cards with contrasting backgrounds.

## Components

### Pill Button Group

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400&display=swap');

  :root {
    --color-cosmic-void: #06051d;
    --color-abyssal-blue: #0f1c36;
    --color-steel-navy: #1d293d;
    --color-bioluminescent-green: #004f3b;
    --color-terminal-amber: #733e0a;
    --color-crimson-depth: #8b0836;
    --color-specimen-green: #00bc7d;
    --color-warning-amber: #f0b100;
    --color-fault-red: #ff2056;
    --color-mist: #cad5e2;
    --color-fog: #e5e7eb;
    --color-portal-blue: #63b3ed;
    --font-jetbrains-mono: 'JetBrains Mono', 'Fira Code', 'Source Code Pro', monospace;
    --shadow-sm: rgba(0,0,0,0.1) 0px 4px 6px -1px, rgba(0,0,0,0.1) 0px 2px 4px -2px;
  }

  .pill-group-wrapper {
    background: var(--color-cosmic-void);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 48px 32px;
    font-family: var(--font-jetbrains-mono);
    width: 100%;
    box-sizing: border-box;
  }

  .pill-btn {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 8px 20px;
    border-radius: 9999px;
    font-family: var(--font-jetbrains-mono);
    font-size: 14px;
    font-weight: 400;
    line-height: 1.63;
    cursor: pointer;
    border: 1px solid rgba(255, 255, 255, 0.10);
    box-shadow: var(--shadow-sm);
    text-decoration: none;
    white-space: nowrap;
    letter-spacing: normal;
  }

  .pill-btn--signup {
    background: rgba(0, 79, 59, 0.55);
    color: #00bc7d;
  }

  .pill-btn--login {
    background: rgba(139, 8, 54, 0.55);
    color: #fff1f2;
  }

  .pill-btn--explore {
    background: rgba(115, 62, 10, 0.55);
    color: #fefce8;
  }

  .pill-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
</style>

<div class="pill-group-wrapper">
  <a class="pill-btn pill-btn--signup" href="#">
    <span class="pill-icon">
      <svg width="14" height="14" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="8" cy="5" r="3" stroke="#00bc7d" stroke-width="1.5"/>
        <path d="M2 13c0-2.761 2.686-5 6-5s6 2.239 6 5" stroke="#00bc7d" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </span>
    Sign Up
  </a>

  <a class="pill-btn pill-btn--login" href="#">
    <span class="pill-icon">
      <svg width="14" height="14" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 8H3m0 0l2.5-2.5M3 8l2.5 2.5" stroke="#fff1f2" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M7 4V3a1 1 0 011-1h4a1 1 0 011 1v10a1 1 0 01-1 1H8a1 1 0 01-1-1v-1" stroke="#fff1f2" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </span>
    Log In
  </a>

  <a class="pill-btn pill-btn--explore" href="#">
    <span class="pill-icon">
      <svg width="14" height="14" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="5" height="5" rx="1" stroke="#fefce8" stroke-width="1.5"/>
        <rect x="9" y="2" width="5" height="5" rx="1" stroke="#fefce8" stroke-width="1.5"/>
        <rect x="2" y="9" width="5" height="5" rx="1" stroke="#fefce8" stroke-width="1.5"/>
        <rect x="9" y="9" width="5" height="5" rx="1" stroke="#fefce8" stroke-width="1.5"/>
      </svg>
    </span>
    Explore
  </a>
</div>
```

### Section Heading with Body — About

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400&display=swap');

  :root {
    --color-cosmic-void: #06051d;
    --color-mist: #cad5e2;
    --color-ghost-white: #ffffff;
    --color-portal-blue: #63b3ed;
    --color-warning-amber: #f0b100;
    --color-specimen-green: #00bc7d;
    --font-jetbrains-mono: 'JetBrains Mono', 'Fira Code', 'Source Code Pro', monospace;
  }

  .about-section {
    background: var(--color-cosmic-void);
    padding: 48px 40px;
    font-family: var(--font-jetbrains-mono);
    max-width: 600px;
    box-sizing: border-box;
    width: 100%;
  }

  .section-heading {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 0 0 24px 0;
  }

  .section-heading__icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .section-heading__title {
    font-family: var(--font-jetbrains-mono);
    font-size: 30px;
    font-weight: 400;
    line-height: 1.25;
    color: var(--color-ghost-white);
    margin: 0;
    letter-spacing: normal;
  }

  .about-body {
    font-family: var(--font-jetbrains-mono);
    font-size: 16px;
    font-weight: 400;
    line-height: 1.5;
    color: var(--color-mist);
    margin: 0 0 20px 0;
  }

  .about-body:last-child {
    margin-bottom: 0;
  }

  .about-link {
    color: var(--color-portal-blue);
    text-decoration: underline;
    text-underline-offset: 2px;
  }
</style>

<div class="about-section">
  <div class="section-heading">
    <span class="section-heading__icon">
      <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="9" cy="9" r="7.5" stroke="#f0b100" stroke-width="1.5"/>
        <line x1="9" y1="8" x2="9" y2="13" stroke="#f0b100" stroke-width="1.5" stroke-linecap="round"/>
        <circle cx="9" cy="5.5" r="0.85" fill="#f0b100"/>
      </svg>
    </span>
    <h2 class="section-heading__title">About</h2>
  </div>

  <p class="about-body">
    We're a <a class="about-link" href="#">community-funded research</a> lab of 60 people known for building the most beautiful AI models in the world.
  </p>

  <p class="about-body">
    We believe that we are all midjourney; that we have a rich past behind us and an unimaginable future ahead — and the question we want to most help answer is: what do we want to become?
  </p>
</div>
```

### Projects Section with Image Grid

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400&display=swap');

  :root {
    --color-cosmic-void: #06051d;
    --color-abyssal-blue: #0f1c36;
    --color-steel-navy: #1d293d;
    --color-mist: #cad5e2;
    --color-ghost-white: #ffffff;
    --color-fog: #e5e7eb;
    --color-warning-amber: #f0b100;
    --font-jetbrains-mono: 'JetBrains Mono', 'Fira Code', 'Source Code Pro', monospace;
  }

  .projects-section {
    background: var(--color-cosmic-void);
    padding: 48px 40px;
    font-family: var(--font-jetbrains-mono);
    max-width: 600px;
    box-sizing: border-box;
    width: 100%;
  }

  .projects-heading {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 0 0 24px 0;
  }

  .projects-heading__title {
    font-family: var(--font-jetbrains-mono);
    font-size: 30px;
    font-weight: 400;
    line-height: 1.25;
    color: var(--color-ghost-white);
    margin: 0;
    letter-spacing: normal;
  }

  .projects-body {
    font-family: var(--font-jetbrains-mono);
    font-size: 16px;
    font-weight: 400;
    line-height: 1.5;
    color: var(--color-mist);
    margin: 0 0 16px 0;
  }

  .projects-body:last-of-type {
    margin-bottom: 32px;
  }

  .projects-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
  }

  .project-tile {
    aspect-ratio: 1 / 1;
    border-radius: 8px;
    background: var(--color-abyssal-blue);
    border: 1px solid rgba(229, 231, 235, 0.12);
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .project-tile__inner {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
  }

  /* Eye tile */
  .tile-eye {
    background: radial-gradient(ellipse at 40% 50%, #1a3a7a 0%, #0b1e4a 60%, #060d2a 100%);
  }

  /* Needle tile */
  .tile-needle {
    background: radial-gradient(ellipse at 60% 40%, #162d6e 0%, #0a1a40 70%, #050e26 100%);
  }

  /* Arch tile */
  .tile-arch {
    background: radial-gradient(ellipse at 50% 60%, #1c3580 0%, #0d1e52 60%, #060f30 100%);
  }

  /* Head tile */
  .tile-head {
    background: radial-gradient(ellipse at 55% 35%, #1a3272 0%, #0c1b48 65%, #060d2c 100%);
  }

  /* Heart tile */
  .tile-heart {
    background: radial-gradient(ellipse at 45% 55%, #152e78 0%, #0a1940 70%, #050c24 100%);
  }

  /* Brain tile */
  .tile-brain {
    background: radial-gradient(ellipse at 50% 45%, #1e3888 0%, #0e2058 60%, #071232 100%);
  }

  /* Hand tile */
  .tile-hand {
    background: radial-gradient(ellipse at 50% 50%, #182f70 0%, #0b1b44 65%, #060e28 100%);
  }

  /* Lips tile */
  .tile-lips {
    background: radial-gradient(ellipse at 50% 55%, #1a3278 0%, #0c1c4a 65%, #060e2c 100%);
  }

  .tile-svg {
    width: 65%;
    height: 65%;
    opacity: 0.75;
  }
</style>

<div class="projects-section">
  <div class="projects-heading">
    <span>
      <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M9 2L10.5 6.5H15.5L11.5 9.5L13 14L9 11L5 14L6.5 9.5L2.5 6.5H7.5L9 2Z" stroke="#f0b100" stroke-width="1.4" stroke-linejoin="round"/>
        <circle cx="9" cy="9" r="2" stroke="#f0b100" stroke-width="1.2"/>
      </svg>
    </span>
    <h2 class="projects-heading__title">Projects</h2>
  </div>

  <p class="projects-body">
    Over the coming months, we're unveiling a wide range of ambitious projects under the themes of imagination, coordination, reflection, beauty, and human flourishing.
  </p>

  <p class="projects-body">
    We hope our work will help tell stories of a humane future that we all want to be a part of, and convince you that we aren't at the end of time, or the beginning, but that we are all midjourney in a vast and great adventure.
  </p>

  <div class="projects-grid">
    <!-- Row 1 -->
    <div class="project-tile tile-eye">
      <div class="project-tile__inner">
        <svg class="tile-svg" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          <ellipse cx="30" cy="30" rx="22" ry="13" stroke="#7ba8e0" stroke-width="1.2" opacity="0.7"/>
          <circle cx="30" cy="30" r="8" stroke="#9bbde8" stroke-width="1.2"/>
          <circle cx="30" cy="30" r="4" fill="#1a3a7a" stroke="#7ba8e0" stroke-width="1"/>
          <line x1="30" y1="2" x2="30" y2="12" stroke="#5a8acc" stroke-width="0.8" opacity="0.5"/>
          <line x1="30" y1="48" x2="30" y2="58" stroke="#5a8acc" stroke-width="0.8" opacity="0.5"/>
          <line x1="2" y1="30" x2="12" y2="30" stroke="#5a8acc" stroke-width="0.8" opacity="0.5"/>
          <line x1="48" y1="30" x2="58" y2="30" stroke="#5a8acc" stroke-width="0.8" opacity="0.5"/>
          <line x1="10" y1="10" x2="17" y2="17" stroke="#5a8acc" stroke-width="0.8" opacity="0.4"/>
          <line x1="50" y1="10" x2="43" y2="17" stroke="#5a8acc" stroke-width="0.8" opacity="0.4"/>
          <line x1="10" y1="50" x2="17" y2="43" stroke="#5a8acc" stroke-width="0.8" opacity="0.4"/>
          <line x1="50" y1="50" x2="43" y2="43" stroke="#5a8acc" stroke-width="0.8" opacity="0.4"/>
        </svg>
      </div>
    </div>

    <div class="project-tile tile-needle">
      <div class="project-tile__inner">
        <svg class="tile-svg" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8 40 Q20 28 35 30 Q45 31 55 22" stroke="#8ab4e8" stroke-width="1.5" stroke-linecap="round" opacity="0.8"/>
          <path d="M8 44 Q22 34 36 36 Q46 37 55 26" stroke="#6a94c8" stroke-width="1" stroke-linecap="round" opacity="0.5"/>
          <ellipse cx="52" cy="22" rx="4" ry="2" stroke="#9bbde8" stroke-width="1" transform="rotate(-35 52 22)" opacity="0.8"/>
          <circle cx="55" cy="21" r="1" fill="#8ab4e8" opacity="0.9"/>
        </svg>
      </div>
    </div>

    <div class="project-tile tile-arch">
      <div class="project-tile__inner">
        <svg class="tile-svg" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M10 50 L10 28 Q10 16 19 16 Q28 16 28 28 L28 50" stroke="#8ab4e8" stroke-width="1.3" opacity="0.8"/>
          <path d="M32 50 L32 28 Q32 16 41 16 Q50 16 50 28 L50 50" stroke="#8ab4e8" stroke-width="1.3" opacity="0.8"/>
          <circle cx="19" cy="13" r="3" stroke="#7aa4d8" stroke-width="1" opacity="0.7"/>
          <circle cx="30" cy="11" r="3" stroke="#7aa4d8" stroke-width="1" opacity="0.7"/>
          <circle cx="41" cy="13" r="3" stroke="#7aa4d8" stroke-width="1" opacity="0.7"/>
          <line x1="10" y1="50" x2="50" y2="50" stroke="#6a94c8" stroke-width="1" opacity="0.5"/>
        </svg>
      </div>
    </div>

    <div class="project-tile tile-head">
      <div class="project-tile__inner">
        <svg class="tile-svg" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M34 8 Q42 8 45 18 Q48 28 44 36 Q40 44 34 46 L30 48 L30 52" stroke="#8ab4e8" stroke-width="1.3" stroke-linecap="round" opacity="0.8"/>
          <path d="M34 8 Q26 8 26 18 Q26 26 30 32" stroke="#6a94c8" stroke-width="1" stroke-linecap="round" opacity="0.5"/>
          <circle cx="39" cy="24" r="2" stroke="#9bbde8" stroke-width="0.8" opacity="0.7"/>
          <path d="M36 30 Q39 32 42 30" stroke="#7aa4d8" stroke-width="0.8" stroke-linecap="round" opacity="0.6"/>
          <line x1="30" y1="52" x2="30" y2="56" stroke="#6a94c8" stroke-width="1.5" stroke-linecap="round" opacity="0.5"/>
        </svg>
      </div>
    </div>

    <!-- Row 2 -->
    <div class="project-tile tile-heart">
      <div class="project-tile__inner">
        <svg class="tile-svg" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M30 48 Q10 36 10 22 Q10 12 20 12 Q25 12 30 18 Q35 12 40 12 Q50 12 50 22 Q50 36 30 48Z" stroke="#8ab4e8" stroke-width="1.3" opacity="0.8"/>
          <path d="M30 44 Q14 33 14 22 Q14 15 20 15 Q25 15 30 21 Q35 15 40 15 Q46 15 46 22 Q46 33 30 44Z" stroke="#6a94c8" stroke-width="0.8" opacity="0.4"/>
          <path d="M30 40 Q18 30 18 22 Q18 18 22 18 Q27 18 30 24" stroke="#5a84b8" stroke-width="0.7" opacity="0.3"/>
        </svg>
      </div>
    </div>

    <div class="project-tile tile-brain">
      <div class="project-tile__inner">
        <svg class="tile-svg" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M30 48 L30 12" stroke="#5a84b8" stroke-width="0.8" opacity="0.3" stroke-dasharray="2 2"/>
          <path d="M30 20 Q20 16 16 22 Q12 28 16 34 Q20 40 26 40 L30 40" stroke="#8ab4e8" stroke-width="1.3" stroke-linecap="round" opacity="0.8"/>
          <path d="M30 20 Q40 16 44 22 Q48 28 44 34 Q40 40 34 40 L30 40" stroke="#8ab4e8" stroke-width="1.3" stroke-linecap="round" opacity="0.8"/>
          <path d="M20 26 Q24 24 28 28" stroke="#6a94c8" stroke-width="0.8" stroke-linecap="round" opacity="0.6"/>
          <path d="M40 26 Q36 24 32 28" stroke="#6a94c8" stroke-width="0.8" stroke-linecap="round" opacity="0.6"/>
          <path d="M18 32 Q22 34 26 32" stroke="#6a94c8" stroke-width="0.8" stroke-linecap="round" opacity="0.5"/>
          <path d="M42 32 Q38 34 34 32" stroke="#6a94c8" stroke-width="0.8" stroke-linecap="round" opacity="0.5"/>
          <line x1="30" y1="40" x2="30" y2="48" stroke="#7aa4d8" stroke-width="1.2" stroke-linecap="round" opacity="0.6"/>
        </svg>
      </div>
    </div>

    <div class="project-tile tile-hand">
      <div class="project-tile__inner">
        <svg class="tile-svg" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M10 38 Q10 30 18 28 L38 26 Q44 25 46 30 Q48 35 42 36 L24 38 Q30 38 30 44 Q30 50 22 50 Q14 50 10 44 Z" stroke="#8ab4e8" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" opacity="0.8"/>
          <path d="M24 38 L24 30" stroke="#6a94c8" stroke-width="0.8" stroke-linecap="round" opacity="0.5"/>
          <path d="M30 37 L30 28" stroke="#6a94c8" stroke-width="0.8" stroke-linecap="round" opacity="0.5"/>
          <path d="M36 36 L37 27" stroke="#6a94c8" stroke-width="0.8" stroke-linecap="round" opacity="0.5"/>
        </svg>
      </div>
    </div>

    <div class="project-tile tile-lips">
      <div class="project-tile__inner">
        <svg class="tile-svg" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M10 30 Q15 22 22 24 Q26 26 30 24 Q34 22 38 24 Q45 22 50 30 Q45 38 38 36 Q34 34 30 36 Q26 34 22 36 Q15 38 10 30Z" stroke="#8ab4e8" stroke-width="1.3" opacity="0.8"/>
          <path d="M10 30 Q20 34 30 30 Q40 26 50 30" stroke="#6a94c8" stroke-width="0.8" opacity="0.5"/>
          <path d="M18 27 Q24 25 30 26 Q36 25 42 27" stroke="#5a84b8" stroke-width="0.7" opacity="0.4"/>
        </svg>
      </div>
    </div>
  </div>
</div>
```

### Sign Up Pill Button

9999px border-radius pill. Background: oklch green tint at 20% opacity (#004f3b equivalent). Text: #00bc7d bright green (oklch 0.979 0.021 166.113). Border: white at 10% opacity. Padding: 8px 20px. Font: JetBrains Mono 14px. Shadow: rgba(0,0,0,0.1) 0px 4px 6px -1px, rgba(0,0,0,0.1) 0px 2px 4px -2px. The translucent jewel-tint approach makes it read as a specimen label rather than a traditional CTA button.

### Log In Pill Button

9999px border-radius. Background: dark red tint (~#8b0836 at 20% opacity). Text: near-white #fff1f2. Border: white 10% opacity. Padding: 8px 20px. JetBrains Mono 14px. Double soft shadow.

### Explore Pill Button

9999px border-radius pill. Background: amber/orange tint at 20% opacity (#733e0a base). Text: #fefce8 warm cream (oklch 0.987 0.026 102.212). Border: white at 10% opacity. Padding: 8px 20px. Font: JetBrains Mono 14px. Third specimen-color variant completing the red/green/amber triad in navigation.

### Documentation Tab

Flat tab style: background transparent (rgba 0,0,0,0), no border-radius (0px), no padding (0px all sides). Text: #63b3ed Portal Blue at 16px JetBrains Mono. Acts as a plain text link styled to match the terminal aesthetic — no affordance chrome, relies entirely on color for identification.

### Section Heading with Icon

JetBrains Mono 30px weight 400, #ffffff text. Preceded by a small colored icon (⚙ in amber #f0b100 for Projects, ℹ in amber for About) at 16px. Icon and label sit on the same horizontal baseline with ~8px gap. No text-transform, no letter-spacing override. The monospace weight-400 at 30px is deliberately un-bold — headings do not shout.

### Project Image Card

Square-aspect image tiles arranged in a 4-column grid with 8px gap. 8px border-radius on each image. Images are monochromatic blue-violet renders of anatomical/symbolic subjects (eye, brain, heart, hand) — no text overlay, no hover badge. Border: #e5e7eb Fog at low opacity as a subtle stroke. Cards function as pure image containers without any UI chrome.

### Sticky Navigation Bar

Full-width bar with #1d293d Steel Navy background. Left side: Documentation (flat text link, #63b3ed) and Explore (amber pill) tabs. Right side: Sign Up (green pill) and Log In (red pill). All items use JetBrains Mono 14px. Vertical padding: 8px. Horizontal padding: ~48px on outer edges. Pill buttons float with translucent tinted backgrounds creating a specimen-tray organization.

### Hero ASCII Animation Background

Fills the entire first viewport with dense ASCII/generative text rendered in #cad5e2 Mist at very low opacity against the #06051d Cosmic Void background. The text forms a spherical/elliptical visual mass centered in the frame. Logo 'Midjourney' overlaid at center in a stylized typeface at approximately 36-40px. Three navigation pill buttons overlay the bottom of the hero. No image or photograph — the generative text IS the hero visual.

### Inline Body Link

Inline text at 16px JetBrains Mono weight 400. Color: #63b3ed Portal Blue — the only chromatic accent color used in body text. No underline by default (transparent borderTopColor in the raw data). Sits at zero padding/margin within the text flow. 'community-funded research' example demonstrates usage.

### Background Gradient Surface

CSS gradient: linear-gradient(0deg, #06051d 30%, #061434). Transitions from pure Cosmic Void at the bottom to a slightly lighter deep navy at the top, creating a sense of depth in a dark environment. Applied as the base layer beneath all content — not visible as a discrete element but sets the atmospheric depth of the entire page.

## Similar Design Systems

- {'why': 'Dark-navy page background with monospace type and minimal navigation — similar restraint in using bold weights and color', 'business': 'OpenAI'}
- {'why': 'Research-lab aesthetic with long-form prose sections on dark backgrounds and minimal decorative chrome', 'business': 'Anthropic'}
- {'why': 'Full-dark theme with translucent button styles and monospace typography as primary UI voice', 'business': 'Perplexity AI'}
- {'why': 'AI-generated imagery used as the primary visual language, dark backgrounds, square image grid layouts', 'business': 'Stability AI'}
- {'why': 'Monospace-first design system treating the entire interface as a terminal environment, not just code blocks', 'business': 'Replicate'}

## Agent Prompt Guide

**Quick Color Reference**
- Page background: #06051d (with gradient to #061434)
- Primary text: #cad5e2
- Headings: #ffffff
- Inline links: #63b3ed
- Borders/dividers: #e5e7eb
- Nav surface: #1d293d
- Sign Up button bg: #004f3b at 20% opacity, text: #00bc7d
- Log In button bg: #8b0836 at 20% opacity, text: #fff1f2
- Explore button bg: #733e0a at 20% opacity, text: #fefce8

**Example Component Prompts**

1. **Hero section**: Full-viewport background using linear-gradient(0deg, #06051d 30%, #061434). Center a dense ASCII text animation in #cad5e2 at ~5% opacity forming a sphere shape. Overlay the text 'Midjourney' at 36px JetBrains Mono weight 400 #ffffff centered. Place three pill buttons (Sign Up green, Log In red, Explore amber) horizontally centered at bottom of hero with 16px gaps.

2. **Navigation bar**: Full-width #1d293d background, 8px vertical padding, 48px horizontal padding. Left: 'Documentation' (JetBrains Mono 14px #63b3ed, no padding, 0px radius) and 'Explore' pill (amber tint). Right: 'Sign Up' (green pill) and 'Log In' (red pill). Pills use 9999px radius, 8px 20px padding, white border at 10% opacity.

3. **Section heading**: Left-aligned amber icon (16px #f0b100) + text label 'Projects' at 30px JetBrains Mono weight 400 #ffffff with 8px gap between icon and text. No bold, no uppercase, no letter-spacing modification.

4. **Project image grid**: 4-column grid, 8px column and row gap. Each cell: square-aspect image with 8px border-radius, monochromatic blue-violet AI-generated content, #e5e7eb border at 15% opacity. No hover text, no captions below images.

5. **Body prose block**: Max-width 640px within the 800px page column. JetBrains Mono 16px weight 400, #cad5e2, lineHeight 1.5. Inline links in #63b3ed with no underline. Paragraph gap: 16px. Sits directly on #06051d background with no card container.

## Specimen Button Color System

The three navigation pill buttons operate as a closed specimen-tray system where each button has its own hue tint at ~20% opacity, text color matched to that hue at high brightness, and a shared white 10% border. The triad is: Green (Sign Up) — bg #004f3b@20%, text #00bc7d; Red (Log In) — bg #8b0836@20%, text #fff1f2; Amber (Explore/Documentation) — bg #733e0a@20%, text #fefce8. This is not a priority hierarchy (primary/secondary/tertiary) — it is a categorical taxonomy where each action belongs to a different domain. Do not add a fourth color. Do not make one of the three visually dominant over the others.
