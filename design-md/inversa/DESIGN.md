# INVERSA — Design System

> **North Star**: topographic field terminal at midnight. A dark command surface where massive editorial type and a single neon-lime marker layer over satellite earth photography, every label set in mono as if reading mission coordinates.
> **Theme**: dark
> **Source**: https://inversa.com
> **Refero Style**: https://styles.refero.design/style/8a6dc9c8-7892-4eab-baaa-3c342d5671f2
> **Synced**: 2026-09-01

## Overview

Inversa operates as a dark conservation-tech command console: a near-black canvas saturated with aerial earth imagery, where massive editorial type and a single electric lime accent function like tactical highlights on a topo map. The visual language is sparse and deliberate — generous negative space, no shadows, near-zero radius — letting one vivid chromatic note (electric lime) cut through the otherwise binary warm-cream-on-near-black system. Typography does the heavy lifting: a humanist sans at near-architectural sizes (58–72px) speaks the narrative voice, while JetBrains Mono handles every data label, tag, and interface annotation as if reading coordinates. Components are utilitarian and unadorned — sharp 3.6px corners, no elevation, no decorative chrome — creating the feel of a field instrument rather than a marketing site.

## Color Palette

- **Obsidian Loam**: `#13140e` — Page canvas, hero background, card surfaces — the near-black base with a faint olive cast that keeps the dark from feeling synthetic [neutral]
- **Bone Vellum**: `#f4f3e8` — Primary text, body copy, headings, icon strokes, border color on dark — warm off-white that reads as paper, not LCD white [neutral]
- **Iron Filings**: `#404040` — Hairline borders, footer dividers, low-emphasis rules [neutral]
- **Drift Ash**: `#84837b` — Muted secondary text, placeholder input state, low-contrast labels on light surfaces [neutral]
- **Lime Surveyor**: `#ebfc72` — Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Marsh Olive**: `#bacd31` — Gradient transition shade for the lime accent — deeper stop used in horizontal lime fades [accent]

## Typography

- **NB International Pro**
- **JetBrains Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.2 |
| body | 18 | — | 1.62 |
| subheading | 29 | — | 1.28 |
| heading | 58 | — | 1.06 |
| display | 72 | — | 0.9 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 14-18px
- **Element Gap**: 18px
- **Section Gap**: 86-104px
- **Border Radius**: {'tags': '3.6px', 'cards': '0px', 'inputs': '3.6px', 'buttons': '3.6px'}

## Layout

Full-bleed dark canvas with content anchored to a max-width 1200px column. The hero is a full-viewport satellite image with bottom-left text overlay — a massive 72px headline, a lime-filled action button directly below, and minimal nav (brand wordmark top-left, menu top-right). Sections are separated by generous 86–104px vertical gaps rather than dividers, creating a sense of topographic sheets laid on a dark surface. Content alternates between full-bleed image bands and contained text blocks. The grid is narrow (2–3 columns max) — this is not a dense dashboard but a reading surface for mission briefings.

## Surfaces / Elevation

- **Obsidian Loam**
- **Iron Filings**

## Imagery

Full-bleed aerial and satellite photography of coastline, estuaries, and terrain — the imagery IS the atmosphere, not decoration. Photos span edge-to-edge with no framing, border, or radius. Color treatment is naturalistic (greens, earth tones, water blues) allowed to carry the only chromatic weight in the system, while overlaid UI remains monochrome. No product screenshots, no illustrations, no abstract graphics — the site is a map and a logbook, not a brochure.

## Design Principles

### Do

- Set hero headlines at 58–72px NB International Pro weight 400 with line-height 0.90 and letter-spacing -0.03em — the tight leading stacks lines into a single mass.
- Use #ebfc72 as the sole chromatic accent for any element that needs to be noticed: buttons, active states, data tags, and icon highlights.
- Apply -0.03em letter-spacing to all NB International Pro text regardless of size — the tracking is part of the brand voice, not a display-only treatment.
- Let imagery bleed to all four edges at 100vw with zero radius, zero border, and zero overlay — the photo is the surface.
- Set all UI labels, button text, and metadata in JetBrains Mono — the mono voice distinguishes interface from editorial copy.
- Use 3.6px border-radius consistently for buttons, tags, and inputs — do not introduce larger radii for 'softness'.
- Space sections at 86–104px and separate them with whitespace, not dividers or background color shifts.

### Don't

- Do not add box-shadows to any element — the system is deliberately flat; depth comes from color contrast, not elevation.
- Do not introduce a second accent color — the lime is alone by design. Any other chromatic addition dilutes the survey-marker effect.
- Do not set body text below 18px in NB International Pro — the font's humanist proportions require generous size to read correctly.
- Do not use #000000 as the canvas — the olive undertone of #13140 is what makes the dark feel organic rather than digital.
- Do not round corners beyond 3.6px on any component — larger radii would contradict the instrument-panel aesthetic.
- Do not use colored backgrounds for cards or content blocks — content sits directly on the dark canvas with no chrome.
- Do not center body text — editorial alignment is left-aligned throughout, matching the mission-log reading flow.

## Components

### Hero Headline

NB International Pro weight 400, 72px, line-height 0.90, letter-spacing -2.16px, color #f4f3e8. Sits bottom-left over full-bleed image with no background treatment. The extreme line-height (0.90) stacks lines tightly into a single block, creating weight without weight-of-stroke.

### Lime Action Button

Background #ebfc72, text #13140, font JetBrains Mono weight 400 at 14px, padding 14px 18px, border-radius 3.6px, uppercase letter spacing. The button is the only high-saturation element on the page — its presence makes it impossible to miss without needing size or shadow emphasis.

### Ghost Text Button

Transparent background, text #f4f3e8, border optional 1px #404040, JetBrains Mono 14px, 3.6px radius. Used for navigation items and secondary links in dark contexts.

### Data Tag

Background #ebfc72 or transparent with #ebfc72 border, text #13140 or #f4f3e8, JetBrains Mono 13px weight 400, padding 5px 7px, 3.6px radius. Functions as the 'survey marker' of the system — small, bright, unmistakable.

### Top Navigation Bar

Transparent over hero, fixed/sticky. Left: brand wordmark 'INVERSA' in NB International Pro 14px #f4f3e8. Right: 'Menu' trigger in JetBrains Mono 13px #f4f3e8 with small indicator dot. No background fill, no border — the nav floats on the image.

### Full-Bleed Image Band

Edge-to-edge photographic imagery (aerial/satellite) with no radius, no border, no overlay. Sits at 100vw. Provides the only color in the system outside the lime accent.

### Text Block (Dark Surface)

No card chrome — content sits directly on #13140e. Headings in NB International Pro 58px #f4f3e8, body in 18px #f4f3e8 lh 1.62. No background fill, no border, no shadow. Spacing between blocks: 18px element gap, 86–104px section gap.

### Footer

Full-width dark #13140 band. Top border 1px #404040. Content in JetBrains Mono 13px #f4f3e8. Sparse — typically 2–3 columns of links and metadata.

### Input Field

Transparent background on dark canvas, bottom border only 1px #404040, text in NB International Pro 14px #f4f3e8, placeholder #84837b. No fill, no radius on the field — the underline IS the field.

## Similar Design Systems

- {'why': 'Same full-bleed satellite earth photography as the visual backbone, dark canvas, and single-color data annotation approach', 'business': 'Planet Labs'}
- {'why': 'Identical top-map-as-hero pattern with minimal text overlay and utilitarian interface chrome', 'business': 'Sentinel Hub'}
- {'why': 'Dark-mode conservation/earth-observation aesthetic with editorial-scale type and restrained accent usage', 'business': 'Radiant Earth'}
- {'why': 'Same editorial use of NB International-style humanist sans at large compressed sizes on dark backgrounds, treated like a publication rather than a product', 'business': 'Stripe Press'}
- {'why': 'Near-identical typographic attitude — dark canvas, mono for UI labels, humanist sans for headlines, zero-radius buttons, and shadowless flat surfaces', 'business': 'Vercel'}

## Agent Prompt Guide

**Quick Color Reference**
- background: #13140e
- text: #f4f3e8
- border: #404040
- accent: #ebfc72
- muted text: #84837b
- primary action: no distinct CTA color

**Example Component Prompts**

1. Build a hero section: full-bleed background (any photo or solid #13140e), max-width 1200px content container, headline NB International Pro 72px weight 400 color #f4f3e8 line-height 0.90 letter-spacing -2.16px left-aligned at bottom-left. Include a lime-filled action button (#ebfc72 bg, #13140e text, JetBrains Mono 14px, 3.6px radius, 14px 18px padding).

2. Create a data tag: #ebfc72 background, #13140e text, JetBrains Mono 13px weight 400, padding 5px 7px, 3.6px radius, uppercase content.

3. Build a content section on dark canvas: #13140e background, no card chrome, heading in NB International Pro 58px #f4f3e8, body in NB International Pro 18px #f4f3e8 line-height 1.62, section gap 86–104px above and below.

4. Create a top navigation bar: transparent background, brand 'INVERSA' left in NB International Pro 14px #f4f3e8, 'Menu' label right in JetBrains Mono 13px #f4f3e8 with a 4px #f4f3e8 dot indicator beside it.

5. Build a footer: full-width #13140e band with 1px #404040 top border, 2–3 column link grid in JetBrains Mono 13px #f4f3e8, 86px top padding.
