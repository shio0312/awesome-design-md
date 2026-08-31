# Geniestudio — Design System

> **North Star**: soft daylight notebook — the kind with generous margins and a single bold pen stroke
> **Theme**: light
> **Source**: https://geniestudio.app
> **Refero Style**: https://styles.refero.design/style/2ffd50d4-93b7-4acf-9bc2-e86e61b63f27
> **Synced**: 2026-09-01

## Overview

Genie uses an airy, daylight-studio language: a pale sky-blue canvas (#ebf5ff) hosts an almost-monochrome interface where near-black buttons provide the only dense visual weight. Display type runs enormous — up to 148px in Aeonik — with a fixed weight 500 that feels engraved rather than shouted, and tracking pulled tight (-0.02em) so headlines read as confident typography, not decorative type. Rounded shapes dominate: 32px cards, 9999px pills, and soft pastel washes (lavender, mint, peach, sky) become the only places color appears beyond a single vivid blue accent and the dark charcoal CTA fill. Whimsical 3D-rendered illustrations — clouds, crayons, smiling objects, floating envelopes — float in the whitespace and carry the brand's personality; the UI itself stays disciplined, almost architectural in its restraint.

## Color Palette

- **Sky Tint**: `#ebf5ff` — Page canvas and soft background washes — the defining ambient color that sets the daylight atmosphere [neutral]
- **Paper White**: `#ffffff` — Pure card surfaces, button text, and icon fills on dark controls [neutral]
- **Bone White**: `#fafdff` — Primary card surface and elevated panel backgrounds — a barely-blue white that feels paper-like [neutral]
- **Mist Gray**: `#f6f7f8` — Subtle secondary surfaces and section dividers [neutral]
- **Ink**: `#0a0d12` — All heading text, primary display type, and deep emphasis copy [neutral]
- **Charcoal**: `#181d27` — Filled button backgrounds and the dense visual anchor against the airy canvas [neutral]
- **Graphite**: `#535862` — Secondary body text and supporting copy [neutral]
- **Fog**: `#93979f` — Muted helper text, FAQ answers, and low-emphasis body [neutral]
- **Slate Shadow**: `#3b3d41` — Dark shadow tone behind buttons and elevated controls [neutral]
- **Iris Blue**: `#0069e0` — Brand accent — chromatic borders, outline strokes, and the single vivid punctuation color in the otherwise pale system; Brand gradient used for decorative borders and accent fills [accent]
- **Sky Blue**: `#0099ff` — Inline highlight text and emphasis spans within body copy [accent]
- **Lavender Wash**: `#f1e6ff` — Pastel card surface for feature tiles and category blocks [accent]
- **Mint Wash**: `#d3f6e3` — Pastel card surface for feature tiles and category blocks [accent]
- **Powder Blue**: `#cce7ff` — Gray wash for highlight backgrounds, decorative bands, and soft emphasis behind content [accent]
- **Solar Gradient**: `#fff2be` — Warm gradient stop for decorative feature highlights [accent]
- **Violet Gradient**: `#e4ccff` — Decorative gradient wash for feature category blocks [accent]
- **Aqua Gradient**: `#c2e9ff` — Decorative gradient wash for feature category blocks [accent]
- **Peach Gradient**: `#ffd1b8` — Decorative gradient wash for feature category blocks [accent]

## Typography

- **Aeonik**
- **Geist**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.4 |
| body-sm | 14 | — | 1.14 |
| body | 16 | — | 1.35 |
| body-lg | 18 | — | 1.33 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.17 |
| heading | 32 | — | 1.25 |
| heading-lg | 48 | — | 1.17 |
| display | 72 | — | 1.11 |
| hero | 148 | — | 1.05 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 40px
- **Element Gap**: 24px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '9999px', 'cards': '32px', 'images': '24px', 'inputs': '16px', 'buttons': '32px', 'cardsSmall': '16px', 'buttonsPill': '9999px'}

## Layout

Max-width 1200px centered with generous side margins. The hero is a centered text+illustration stack: headline at 148px above a single 3D render, with one dark CTA button below — no left/right split, no columns. Sections alternate between centered single-column editorial stacks (headline → subhead → content) and full-bleed horizontal bands (marquee strips, category tile rows). Cards appear in 3-column grids for feature sections and in a continuous horizontal marquee for testimonials. The layout breathes — vertical section gaps run 80-120px, and even within sections the element gaps sit at 24-40px. Navigation is minimal: logo left, two text links center, single filled CTA right, all in a single row. The footer is a wide centered CTA block followed by a 4-column link grid.

## Surfaces / Elevation

- **Sky Canvas**
- **Paper Card**
- **Pure White**
- **Mist Section**

**Shadow tokens:**

## Imagery

The site leans heavily on 3D-rendered illustrations: soft, rounded, dimensional objects in pastel colors (lavender, mint, peach, powder blue) with a single vivid iris-blue accent object per scene. Objects float in the canvas as isolated subjects — a cloud and a crayon here, an envelope and a smiley face there — with no background, no shadow plate, no lifestyle staging. The style is playful, toy-like, and slightly squishy, almost like clay renders. The canvas is the negative space; illustrations are the positive. There is no photography, no product screenshots in the traditional sense, and no abstract graphic patterns. The 3D objects carry all the personality.

## Design Principles

### Do

- Use weight 500 (not 600 or 700) for all display and heading type — the system is intentionally mid-weight, never bold
- Apply 32px border-radius to all content cards and 9999px to all interactive pills and tags
- Set the page canvas to #ebf5ff and card surfaces to #fafdff — the pale blue-to-bone-white shift is the primary depth mechanism
- Use the dark fill #181d27 for all filled buttons; reserve #0069e0 for accent borders and inline highlight text only
- Pull heading tracking to -0.02em and body tracking to -0.01em; never set type with default or positive letter-spacing
- Let 3D illustrations float in the canvas without cards, borders, or backgrounds — they are the brand voice, not decoration
- Use the iris gradient (71,157,255 → 0,105,224) only for thin 3px accent borders; never as a button fill or large surface

### Don't

- Do not use bold weights (600+) for display headlines — Aeonik 500 is the ceiling
- Do not use 90° sharp corners on cards or buttons — minimum 16px, default 32px, pill 9999px
- Do not place saturated blue (#0069e0) as a button fill — it is an outline/accent color, not a CTA color
- Do not add box-shadows to content cards — depth comes from the canvas/surface color shift, not elevation
- Do not use body-weight black (#000000) for text — use #0a0d12, which has a hint of blue that ties to the canvas
- Do not mix more than two pastel washes in a single section — the pastel palette is for tile variety, not visual noise
- Do not set display type below 48px or use display sizes for body content — the scale has a hard floor for editorial moments

## Components

### Primary CTA Button

Background #181d27, white text (#ffffff), border-radius 32px (or 9999px for full pill), padding 12px 32px, font Geist 16px weight 500, letter-spacing -0.01em. Tight dark shadow ring (0 1px 2px rgba(10,13,18,0.8), 0 0 0 1px #0a0d12) gives it a pressed, pressed-into-page quality. Used for 'Sign up' and the single hero action.

### Secondary CTA Button

Background #181d27, white text, border-radius 16px, padding 8px 16px, Geist 14px weight 500. Compact variant of the primary.

### Ghost Nav Link

No background, Geist 16px weight 500, color inherits from #0a0d12 or #535862, no underline, no hover background fill. Sits on the canvas as plain typography.

### Feature Card (32px radius)

Background #fafdff (bone white), border-radius 32px, padding 40px on all sides, no visible border, no shadow. The card relies on the color shift from canvas (#ebf5ff) to surface (#fafdff) and the 32px radius to define itself.

### Pastel Category Tile

Solid pastel background (#f1e6ff lavender, #d3f6e3 mint, #cce7ff powder blue, #fff2be solar), border-radius 32px, generous padding, no border. Each tile is a flat wash of color — no gradients on the tile itself, though some use gradient fills (#c2e9ff, #e4ccff, #ffd1b8).

### Testimonial Card

Background #fafdff, border-radius 32px, padding 40px, contains a pull-quote at Geist 18px #535862, a divider, then avatar + name (Geist 16px weight 500 #0a0d12) + role (Geist 14px #93979f) and a brand logo on the right. Cards bleed off the edges of the viewport in a continuous horizontal marquee.

### FAQ Accordion Row

Background #fafdff, border-radius 32px, padding 40px. Question in Geist 18-20px weight 500 #0a0d12, answer in Geist 16px #93979f. Animated open/close using grid-template-rows transition at 0.65s ease.

### Pill Tag / Chip

Border-radius 9999px, Geist 12-14px weight 500, padding 4px 12px. Appears in pastel-tinted backgrounds for category labels.

### Marquee Logo Strip

Continuous horizontal marquee animation (no visible container). Logos are monochrome or brand-colored, float in the sky canvas with no card wrapper. Uses linear(0 0%, 0.55 7.5%, ...) timing function for the scroll.

### Hero Gradient Banner

Thin border using the iris gradient (linear-gradient(71,157,255 11.43%, 0,105,224 78.2%)) with 3px solid weight and border-radius 90px. The only place a gradient border appears — it frames the hero illustration like a polaroid edge.

### 3D Illustration Asset

Rounded, dimensional, pastel-colored 3D renders. They float in the canvas as isolated objects with no background container. Colors come from the pastel palette (#cce7ff, #f1e6ff, #d3f6e3, #ffd1b8) plus a vivid iris blue accent. Sized large and given room to breathe — they are the brand personality, not decoration.

### Section Header

Aeonik 48-72px weight 500 in #0a0d12, centered, with a Geist 18px subhead in #535862 below. The 148px hero variant is reserved for the first screen. Letter-spacing tightens with size (-0.96px at 48px, -1.44px at 72px, -2.96px at 148px).

## Similar Design Systems

- {'why': 'Same near-monochrome canvas with a single accent color, oversized display type at weight 500, and pill-shaped dark CTA buttons', 'business': 'Linear'}
- {'why': 'Same playful 3D illustration language floating on a pale tinted canvas, generous spacing, and 32px card radii', 'business': 'Framer'}
- {'why': 'Same near-black button fill (#181d27 ≈ their dark surfaces) and typographic-first layout where type does the work and decoration stays minimal', 'business': 'Vercel'}
- {'why': 'Same dark filled pill buttons, pale neutral canvas, and confident mid-weight display typography', 'business': 'Pitch'}

## Agent Prompt Guide

Quick Color Reference:
- text: #0a0d12 (headings), #535862 (body), #93979f (muted)
- background: #ebf5ff (canvas), #fafdff (card), #ffffff (elevated)
- border: transparent default; #0069e0 for accent outlines
- accent: #0069e0 (iris blue — borders, highlights)
- primary action: #181d27 (filled action)

Example Component Prompts:
1. Create a hero section: #ebf5ff canvas, centered Aeonik 148px weight 500 headline in #0a0d12 with -0.02em tracking, a single 3D-rendered illustration floating below on transparent background, and one filled CTA button (#181d27, #ffffff text, 32px radius, 12px 32px padding, Geist 16px weight 500).
2. Build a feature card: #fafdff background, 32px border-radius, 40px padding all sides, Aeonik 48px weight 500 title in #0a0d12 with -0.96px tracking, Geist 18px body in #535862. No border, no shadow.
3. Create a pastel category tile: solid #f1e6ff (or #d3f6e3 / #cce7ff / #fff2be) background, 32px radius, 40px padding, Aeonik 32px weight 500 label in #0a0d12 centered, with a small 3D illustration inset.
4. Build a testimonial card: #fafdff background, 32px radius, 40px padding, Geist 18px quote in #535862, Geist 16px name in #0a0d12, Geist 14px role in #93979f, brand logo at the right.
5. Create a dark filled button: #181d27 background, #ffffff text, 32px radius, 12px 32px padding, Geist 16px weight 500, tight shadow ring (0 1px 2px rgba(10,13,18,0.8), 0 0 0 1px #0a0d12).

## Motion Philosophy

Animation is expressive but not aggressive. Marquee scrolls run continuously for logo strips and testimonial walls. FAQ accordions use grid-template-rows transition at 0.65s ease for a soft expand. Scroll-triggered reveals use cubic-bezier(0.16, 1, 0.3, 1) — a fast start and gentle settle. The custom linear() timing function in the marquee creates a non-uniform scroll speed that feels organic, not mechanical. Durations cluster around 0.3-0.65s; nothing is snappy, nothing is slow.
