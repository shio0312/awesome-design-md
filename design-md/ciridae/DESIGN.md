# Ciridae — Design System

> **North Star**: void chamber with ember pulse — a near-black cathedral where the only warm note is a thin line of ember rust, and every surface is defined by hairline borders rather than shadow.
> **Theme**: dark
> **Source**: https://www.ciridae.com
> **Refero Style**: https://styles.refero.design/style/a1b78a21-a304-482b-8ce5-f612d95d44fe
> **Synced**: 2026-09-01

## Overview

Ciridae operates in a void: #0b0b0b canvas, ghost-outlined pill controls, and typography locked in uppercase Pragmatica Cond at weight 400 — no bold, no mixed case, no decoration. The only chromatic note is #cc6437, a warm ember rust used as hairline strokes and small accent punctuation, never as a fill. Cards float on #272a2a with 10px radius and zero shadow; the system refuses elevation, defining surfaces through tonal contrast and 1px hairline borders. Photography arrives heavily blurred and atmospheric — liquid marble, smoke, fire — set behind type at full-bleed scale, so the visuals feel ambient rather than illustrative.

## Color Palette

- **Ember Rust**: `#cc6437` — Accent strokes, icon linework, small text highlights — the only chromatic color in an otherwise monochrome system, appearing as a hairline pulse rather than a fill [brand]
- **Void Black**: `#0b0b0b` — Primary page canvas and section backgrounds; the foundation of the entire system [neutral]
- **Charcoal Surface**: `#272a2a` — Card and panel backgrounds on dark sections — one step lighter than the canvas to create surface separation without shadow [neutral]
- **Bone**: `#edebe7` — Light section backgrounds and off-white surfaces where the system flips from dark to bright [neutral]
- **Bone Darker**: `#dfddd9` — Subtle variant of Bone for layered light surfaces and warm-tinted off-white elements [neutral]
- **Pure White**: `#ffffff` — All body and heading text, ghost button borders, nav elements — the dominant foreground color at 19.7:1 contrast on Void Black [neutral]
- **Abyss**: `#050505` — Elevated bar backgrounds (top news strip) — one shade darker than the main canvas to push the bar forward [neutral]
- **Steel**: `#484848` — Mid-tone border for secondary solid buttons where Pure White would be too stark [neutral]
- **Ash**: `#cecece` — Hairline borders for pill badges and numbered markers — lighter than Steel to read as fine detail against the dark canvas [neutral]

## Typography

- **Pragmatica Cond**
- **Pragmatica**
- **Roboto Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.1 |
| body-sm | 14 | — | 1.43 |
| heading-sm | 20 | — | 1 |
| heading | 24 | — | 1.2 |
| heading-lg | 32 | — | 1.05 |

## Spacing & Layout

- **Max Width**: 1400px
- **Card Padding**: 32px
- **Element Gap**: 16-20px
- **Section Gap**: 80px
- **Border Radius**: {'nav': '1440px', 'cards': '10px', 'badges': '1440px', 'buttons': '1440px', 'news-bar-button': '0px'}

## Layout

Full-bleed page model with content centered within a ~1400px max width. Hero is a full-viewport dark composition with centered constellation logo, flanked by micro-labels at far left and right. Sections alternate: dark hero → light backers strip (Bone) → dark transformation narrative → dark systems card grid → dark footer. The single light section creates one dramatic tonal break. Card grid uses 4 columns where the first card is approximately 2× wider than the remaining three, creating an asymmetric featured layout. Vertical breathing room between sections is generous (80px+). Navigation is minimal: top news bar + a single left-aligned ghost pill ('Start Now') and right-aligned ghost pill ('Menu') in the header bar. No sidebar, no mega-menu.

## Surfaces / Elevation

- **Void Canvas**
- **Abyss Bar**
- **Charcoal Card**
- **Bone Inversion**

## Imagery

Atmospheric, full-bleed photography dominates the hero and card backgrounds. Images are heavily blurred (50px and 40px backdrop-blur values detected) and high-contrast, depicting liquid marble with blue/red swirling patterns, smoke, dark landscape silhouettes, and fire/ember textures. The photography is moody and dark, not high-key — it sits in the same tonal register as the void canvas rather than popping against it. No product photography, no people, no UI screenshots. Imagery is ambient atmosphere, not illustrative content. The card grid pairs each system with a different atmospheric scene, making the photographs function as abstract visual identifiers rather than literal representations of the product.

## Design Principles

### Do

- Use 1440px border-radius for all buttons, badges, nav items, and pill-shaped interactive elements
- Use 10px border-radius exclusively for card and content containers — pill = interactive, rounded-rect = content
- Set all text in uppercase using Pragmatica Cond at weight 400 — never use bold, never use mixed case
- Apply -0.02em letter-spacing to all type sizes above 14px; -0.01em is acceptable for 15px body passages
- Define surfaces through background tonal shifts (#0b0b0b → #272a2a → #edebe7) and 1px hairline borders, never through box-shadow
- Reserve #cc6437 Ember Rust for hairline accent strokes and small text highlights only — never use it as a fill
- Use Roboto Mono 11px exclusively for system data (news ticker, metadata, technical labels) to create a clear typographic register

### Don't

- Do not introduce bold or semi-bold weights — the entire system operates at weight 400 only
- Do not add drop shadows, glow effects, or any box-shadow values — the system is intentionally flat
- Do not use color fills on buttons — all interactive controls are ghost/outlined with 1px borders
- Do not use mixed-case text or sentence case in any UI label, heading, or body string
- Do not introduce additional accent colors — Ember Rust is the only chromatic note permitted
- Do not use non-pill radii (e.g. 4px, 8px) on buttons, badges, or nav items — the 1440px pill is the system's signature shape
- Do not use gradients — the system is built on flat color fields and blurred photography, not color transitions

## Components

### Ghost Pill Button

Transparent background, 1px Pure White border, 1440px border-radius (full pill), 10px vertical / 18-20px horizontal padding, Pragmatica Cond 14px uppercase Pure White text, letter-spacing -0.02em. Used for 'Start Now', 'Menu', and all primary navigation triggers. The 1440px radius (effectively a stadium shape) is extreme — it pushes these controls into a signature capsule form that appears nowhere else in common UI kits.

### News Bar Solid Button

Abyss (#050505) background, 1px Pure White border, 0px border-radius (sharp corners, contrast with pill buttons), 10px vertical / 20px horizontal padding, Pragmatica Cond 14px uppercase text. The sharp-cornered, dark-filled variant is reserved exclusively for the top news strip — the different shape signals a different functional zone (system status, not brand navigation).

### Pill Badge

Transparent background, 1px Ash (#cecece) border, 1440px border-radius, 5px vertical / 11px horizontal padding, Pragmatica Cond 14px uppercase Pure White text. Used for numbered card markers ('01', '02', etc.) and small inline labels. The lighter Ash border (vs Pure White on buttons) reads as subordinate detail.

### System Card

Charcoal Surface (#272a2a) background, 10px border-radius, no box-shadow, 32px vertical / 0px horizontal padding (content aligns to card edges). Full-bleed atmospheric photography sits behind or within each card. The 10px radius is the only non-pill radius in the system, creating a deliberate geometric contrast: pill = interactive, rounded rectangle = content container.

### Top News Bar

Abyss (#050505) background, spans full viewport width, contains centered Roboto Mono 11px uppercase text with bullet separators ('NEWS • JUN 15, 2026 • CRUCIBLE EARLY ACCESS IS NOW OPEN'). The monospace typeface and dotted separators create a terminal/log aesthetic that contrasts with the brand's condensed type.

### Constellation Logo Mark

Geometric mark composed of a central diamond with four extending point-shapes arranged in a cross/star pattern, rendered as thin Pure White strokes. Below it, the wordmark 'CIRIDAE' in Pragmatica Cond 32px uppercase Pure White, letter-spacing -0.02em. The mark's four-pointed geometry echoes the system's orthogonal precision.

### Hero Section

Void Black (#0b0b0b) canvas with full-bleed heavily-blurred atmospheric photography (warm skin tones, bokeh) at 50px backdrop-blur. Centered constellation logo and wordmark. Flanking micro-labels in Pragmatica Cond 14px uppercase Pure White at far left ('AUTOMATE THE MUNDANE') and far right ('ACCELERATE THE REMARKABLE'). The flanking labels span the full width while the logo sits dead center — a triadic composition that fills the viewport without crowding.

### Backers Logo Strip

Bone (#edebe7) background — the only light section, creating a stark visual break. Centered 'OUR WORK IS BACKED BY' label in Pragmatica Cond 14px uppercase, followed by a horizontal row of partner logos (General Catalyst, Accel, Andreessen Horowitz) rendered in Pure White or dark tone. The light-to-dark inversion is the system's most dramatic tonal shift, used once to punctuate the page.

### Section Heading Block

Eyebrow label in Pragmatica Cond 14px uppercase (e.g. 'AI TRANSFORMATION', 'SYSTEMS, NOT TOOLS'), followed by a large headline in Pragmatica Cond 32px uppercase Pure White, letter-spacing -0.64px, centered on Void Black. Generous vertical breathing room above and below (40-60px). The eyebrow-to-headline pairing is the standard section-opening pattern.

### Footer

Void Black (#0b0b0b) background, Pragmatica Cond 14px uppercase Pure White text. Minimal links and legal text arranged in simple rows. No visual embellishment — the footer respects the void.

## Similar Design Systems

- {'why': 'Same near-black canvas with white text, all-caps narrow type, and refusal of color except for a single warm accent — both systems treat the void as the brand', 'business': 'Nothing (nothing.tech)'}
- {'why': 'Dark monochromatic UI with hairline borders, pill-shaped controls, and zero reliance on shadow for elevation — though Linear uses more color in its feature sets', 'business': 'Linear'}
- {'why': 'Full-bleed dark sections with centered typographic compositions, generous vertical breathing room, and minimal navigation chrome', 'business': 'Vercel'}
- {'why': 'Extremely restrained typographic system using condensed uppercase type at small sizes, with color appearing only as a single accent punctuation', 'business': 'Framework'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff
- background: #0b0b0b
- card surface: #272a2a
- border: #cecece (badges) / #ffffff (buttons)
- accent: #cc6437
- primary action: no distinct CTA color

**Example Component Prompts**

1. Create a ghost pill button: transparent background, 1px #ffffff border, 1440px border-radius, 10px 20px padding, Pragmatica Cond 14px uppercase #ffffff text, letter-spacing -0.02em.

2. Create a system card: #272a2a background, 10px border-radius, no box-shadow, 32px vertical padding, Pragmatica Cond 14px uppercase #ffffff body text, with a full-bleed atmospheric photo behind the content.

3. Create a hero section: #0b0b0b canvas, full-bleed blurred warm-toned photography at 50px backdrop-blur, centered constellation diamond mark (4-point star, thin #ffffff strokes), 'CIRIDAE' wordmark below in Pragmatica Cond 32px uppercase #ffffff, flanking labels in Pragmatica Cond 14px uppercase at far left and far right.

4. Create a top news bar: #050505 background, full-width strip, centered Roboto Mono 11px uppercase #ffffff text with '•' bullet separators, containing a news announcement string.

5. Create a numbered pill badge: transparent background, 1px #cecece border, 1440px border-radius, 5px 11px padding, Pragmatica Cond 14px uppercase #ffffff text (e.g. '01', '02', '03').

## Typographic Register System

Ciridae uses a three-register typographic system to signal information hierarchy without weight variation:

- **Brand voice** — Pragmatica Cond 14-32px, uppercase, 400 weight. All UI labels, headings, navigation, and short brand statements live here. This is what the system sounds like.

- **Body voice** — Pragmatica 15-24px, mixed case allowed but rare, 400 weight. Reserved for longer-form prose passages (card descriptions, explanatory text). The shift to mixed case and a slightly wider letterform signals 'read this as a sentence, not a label.'

- **System voice** — Roboto Mono 11px, uppercase, 400 weight. The news ticker and any technical metadata. Monospace + dot separators create a terminal/log register that says 'this is machine data, not brand communication.'

Never cross registers. A navigation label in Roboto Mono would feel broken. A news announcement in Pragmatica Cond would feel like a headline.
