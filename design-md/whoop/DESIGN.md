# WHOOP — Design System

> **North Star**: Performance laboratory at midnight — clinical white lab benches beneath a black theatrical void, one violet pulse of electricity.
> **Theme**: mixed
> **Source**: https://whoop.com
> **Refero Style**: https://styles.refero.design/style/05053a60-1964-4154-9d58-ebdf6352ed3a
> **Synced**: 2026-09-01

## Overview

WHOOP operates on a high-contrast split-canvas system: full-bleed black theatrical heroes alternate with clinical white content sections, creating a rhythm that mimics the alternation between effort and recovery. Typography is the dominant voice — oversized Proxima Nova display type at 120px with aggressive negative tracking carries the brand, while body copy stays compact and neutral. A single vivid violet (#4a53ff) acts as the lone chromatic accent against an otherwise achromatic palette, appearing only on primary actions and the announcement bar. Components are large, confident, and rounded: 24px-radius cards, fully pill-shaped buttons, and photographic overlays with heavy text treatment replace the typical SaaS card grid. The result feels less like a product page and more like a premium performance lab at night — scientific, dramatic, and focused on data over decoration.

## Color Palette

- **Pulse Violet**: `#4a53ff` — Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Obsidian**: `#000000` — Primary text on light surfaces, dark hero/section backgrounds, filled neutral buttons, icon strokes [neutral]
- **Carbon**: `#191919` — Secondary dark surface (footer band, alternating black sections), heading text on light surfaces [neutral]
- **Paper White**: `#ffffff` — Primary page canvas, card surfaces on dark sections, text on dark backgrounds, filled white pill buttons [neutral]
- **Lab Mist**: `#f3f5f9` — Soft elevated surface for light cards and feature panels — a cool off-white that distinguishes cards from the page without using shadow [neutral]
- **Hairline**: `#e5e7eb` — Borders, dividers, outlined button strokes, input frames — the most-used neutral in the system (2560 occurrences) [neutral]
- **Fog Gray**: `#808080` — Muted body text, secondary descriptions, placeholder copy on light surfaces [neutral]
- **Ash**: `#999999` — Tertiary text, inactive button labels, disabled icon strokes — sits one step below Fog Gray for de-emphasized metadata [neutral]

## Typography

- **Proxima Nova**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.59 |
| body-sm | 16 | — | 1.33 |
| body-lg | 20 | — | 1.29 |
| subheading | 24 | — | 1.13 |
| heading-sm | 32 | — | 1.09 |
| heading | 35 | — | 1 |
| heading-lg | 50 | — | 0.8 |
| display | 120 | — | 0.71 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24-32px
- **Element Gap**: 15-24px
- **Section Gap**: 80-120px
- **Border Radius**: {'cards': '24px', 'pills': '300px', 'images': '24px', 'buttons': '300px', 'mediumRounded': '30px', 'smallElements': '8px'}

## Layout

Page model alternates between full-bleed edge-to-edge sections (no max-width constraint on the outer container) and a 1200px max-width content well for text and card grids. Hero is a full-viewport black theater with a 120px display headline left-aligned in the first 60% of the screen. Below the hero, content sections stack as white bands containing a single max-width column or a 3-up carousel of photographic cards. Closing section returns to full-bleed black. Navigation is a fixed top bar on the dark hero only; content sections rely on the page scrolling naturally without sticky chrome. Card grids use 3 equal columns with 24px gutters. Density is comfortable: 80-120px between sections, 15-24px between elements. No sidebar, no mega-menu.

## Surfaces / Elevation

- **Page Canvas**
- **Lab Mist Card**
- **Dark Section**
- **Carbon Band**

## Imagery

Photography is the dominant visual asset: tight, full-bleed lifestyle crops of athletes and bodies in motion — swimming, running, sleeping on textured bedding. Images are warm-toned and natural-light, never staged studio shots. Treatment is raw: no duotone, no color grading overlays, no masks. They sit inside 24px-radius carousel cards with white text overlaid directly on the photo (no scrim). UI graphics are minimal — small white circular expand buttons, thin pagination dots, and one green radial-glow metric on the longevity card. No illustrations, no 3D renders, no abstract graphics. Icons (where present) are thin-stroke monoline, white on dark, black on light.

## Design Principles

### Do

- Use 300px border-radius for every button — pill shape is non-negotiable, even on small utility buttons
- Set display headlines at 120px with line-height 0.71 and letter-spacing -4.8px; this tight tracking is the brand's visual signature
- Alternate full-bleed black sections with full-bleed white sections at 80-120px gaps; never blend the two with a gray transition
- Use #4a53ff exclusively for primary actions and the announcement bar — no other element should carry chromatic color
- Render cards at 24px radius with no drop shadow; elevation comes from #f3f5f9 fills, not blur
- Apply 0.1em letter-spacing with uppercase to all 14-15px labels in nav, buttons, and metric captions
- Keep body text at 19-20px with -0.57 to -0.6px tracking; anything smaller loses the brand's confident scale

### Don't

- Don't add drop shadows to cards or buttons — WHOOP uses flat color elevation only; the single rgba(199,199,199,0.25) shadow is reserved for floating overlays
- Don't introduce a second accent color — the system is monochromatic + one violet, anything else breaks the lab aesthetic
- Don't use line-height above 1.0 on display sizes (50px+) — the tight 0.71-0.80 ratio is what makes headlines feel carved
- Don't center body paragraphs — text in feature cards and descriptions left-aligns with max-width 520px
- Don't use square or 8px-radius buttons — every action is a pill, including icon buttons and tags
- Don't place colored gradients on UI surfaces; the three detected gradients are decorative background washes only, not component fills
- Don't set body text below 16px — 14px is reserved for uppercase labels with tracking, never running prose

## Components

### Announcement Bar

Full-width, 40-48px tall, Pulse Violet (#4a53ff) background, white Proxima Nova 14px text centered, with an underlined white text link aligned right. Sits flush above the nav bar with no gap.

### Primary Navigation

Full-bleed black background, 80-100px tall. WHOOP wordmark left in white 24px weight 700. Nav links in white 15px weight 500 with 0.1em tracking, spaced ~32px apart. Right-aligned Pulse Violet pill button (#4a53ff, white text, 300px radius, 12px 24px padding).

### Full-Bleed Dark Hero

100% width, 100vh height, pure #000000 background. Display headline at 120px Proxima Nova weight 400, white, line-height 0.71, letter-spacing -4.8px, occupying 2 lines and left-aligned with ~8% page padding. Subtext at 19px weight 400, white or Fog Gray, max-width 520px. White pill CTA centered below (300px radius, 16px 32px padding, black 15px weight 600 uppercase text with 0.1em tracking).

### Pulse Violet Pill Button

#4a53ff background, white text, 300px border-radius, 12px 24px padding, Proxima Nova 15px weight 600 uppercase with 0.1em letter-spacing. Used in nav and promotional contexts. No shadow.

### White Pill Button

White (#ffffff) background, black (#000000) text, 300px border-radius, 16px 32px padding, 15px weight 600 uppercase with 0.1em tracking. Centered in hero sections and dark bands.

### Outlined Pill Button

Transparent background, 1.5px Hairline (#e5e7eb) border, black text, 300px border-radius, 12px 28px padding, 14px weight 500. Used in feature cards for trial and secondary offers.

### Lab Mist Feature Card

Lab Mist (#f3f5f9) background, 24px border-radius, no shadow, 24px padding. Contains a 24px-radius square image left (~200×140px), bold heading and body text middle, outlined pill button right. Total height ~200px, full content-width.

### Carousel Story Card

Tall card (aspect ratio ~3:4 or 4:5), photographic background filling the entire card, 24px border-radius. Overlay heading top-left at 24px weight 600, white. Small white circular expand button (40px, 1px white border) bottom-right. Pagination dots centered below carousel.

### Dark CTA Band

Full-width #000000 background, 400-600px height, large display heading in white (50px weight 400, -2px tracking), centered or left-aligned with generous padding (80-120px vertical).

### Membership Pricing Card

White background, 24px border-radius, 1px Hairline (#e5e7eb) border, 32px padding. Black tier name at 24px weight 700, price at 50px weight 400 with -2px tracking, feature list at 16px with 15px row gap. Pulse Violet pill button at bottom for selected tier.

### Metric Overlay Stat

Small white number (32px weight 400) with thin white label (12px weight 500, 0.1em tracking, uppercase). Used as floating data callouts over carousel images — e.g. '98%' '82%' on a forest scene, '45.8%' inside a green radial glow.

## Similar Design Systems

- {'why': 'Same split-canvas black/white alternation, oversized display headlines with tight tracking, and single-accent restrained palette in the health-wearable space', 'business': 'Oura'}
- {'why': 'Full-bleed photographic hero cards with 24px radius, pill-shaped CTAs, and a dark theatrical opening that transitions to white content sections', 'business': 'Peloton'}
- {'why': 'Performance-data aesthetic with uppercase tracking labels, flat card elevation, and Proxima-Nova-adjacent geometric sans typography', 'business': 'Garmin'}
- {'why': 'Minimalist monochrome palette with a single violet brand accent, tight letter-spacing on large headlines, and pill-shaped primary buttons', 'business': 'Notion'}
- {'why': 'Athletic-performance category peers using photographic carousel cards as the primary content unit with direct text overlay', 'business': 'Whoop Coach / Apple Fitness+'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #000000 (light surfaces) / #ffffff (dark surfaces)
- background: #ffffff (light sections) / #000000 (dark sections)
- card surface: #f3f5f9
- border: #e5e7eb
- muted text: #808080 / #999999
- accent: #4a53ff (brand action, announcement bar)
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. Build a full-bleed dark hero: #000000 background, 100vh. Headline at 120px Proxima Nova weight 400, #ffffff, line-height 0.71, letter-spacing -4.8px, left-aligned with 8% page padding. Subtext at 19px weight 400, #808080, max-width 520px. White pill button centered below: #ffffff background, #000000 text, 300px radius, 16px 32px padding, 15px weight 600 uppercase with 0.1em tracking.

2. Build a Lab Mist feature card: #f3f5f9 background, 24px radius, 24px padding, full content-width. 200×140px image left at 24px radius. Bold heading 24px weight 700, #000000. Body 16px weight 400, #808080. Outlined pill button right: transparent fill, 1.5px #e5e7eb border, 300px radius, 12px 28px padding, 14px weight 500 black text.

3. Build a carousel story card: photographic background filling the entire card, 24px radius, aspect ratio 3:4. White heading 24px weight 600 top-left with 24px padding. Small white circular button 40px diameter, 1px white border, positioned bottom-right at 16px offset.

4. Build a Pulse Violet pill action button: #4a53ff background, #ffffff text, 300px radius, 12px 24px padding, Proxima Nova 15px weight 600 uppercase with 0.1em letter-spacing. No shadow, no border.

5. Build a metric overlay stat: white number at 32px weight 400, white uppercase label at 12px weight 500 with 0.1em letter-spacing, positioned over a photographic background. Example: '45.8' with 'STRESS' below.

## Elevation Philosophy

WHOOP avoids drop shadows almost entirely. The single detected shadow (rgba(199,199,199,0.25) 0px 4px 15px 0px) is used sparingly on floating overlays only. Elevation is communicated through flat color contrast: Lab Mist (#f3f5f9) cards sit on Paper White (#ffffff) canvases; black sections sit on white sections; the Pulse Violet button sits on black. This keeps the system feeling clinical and flat — closer to print editorial than interactive app.
