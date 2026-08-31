# Visitors — Design System

> **North Star**: white engineering blueprint
> **Theme**: light
> **Source**: https://visitors.now
> **Refero Style**: https://styles.refero.design/style/e7876363-181a-44a9-9e5c-2255cf98aea5
> **Synced**: 2026-09-01

## Overview

Visitors is a bright white-canvas analytics product with a restrained grayscale spine and a single lavender accent (#918df6) that does the heavy lifting as a CTA color. Typography is confident and geometric — OpenRunde at heavy display weights with tight negative tracking, creating headlines that feel engineered rather than editorial. The interface lives flat: hairline borders, subtle surface tinting, minimal elevation, and pill-shaped controls that read as light and fast. Color appears as functional punctuation — green for positive deltas, amber for neutral data, pink and blue for feature categories — never as decoration on chrome.

## Color Palette

- **Carbon**: `#181925` — Primary text, headings, nav links — near-black with the faintest cool tint gives type a deliberate, engineered weight without pure-black harshness [neutral]
- **Paper White**: `#ffffff` — Page canvas, card surfaces, button fills — the base layer everything sits on [neutral]
- **Linen**: `#fafafa` — Subtle background sections, table rows, secondary surfaces — separates content bands from pure white without introducing a visible gray [neutral]
- **Mist**: `#f5f5f5` — Primary page canvas and white card surfaces. Do not promote it to the primary CTA color [neutral]
- **Fog**: `#e8e8e8` — Table gridlines, hairline borders, divider lines — the structural 1px that defines table cells and card edges [neutral]
- **Ash**: `#999999` — Muted body text, placeholder text, inactive nav items — secondary information that recedes [neutral]
- **Graphite**: `#666666` — Secondary text, button text on light fills, captions — readable but clearly subordinate to Carbon [neutral]
- **Lavender**: `#918df6` — Violet action color for filled buttons, selected navigation states, and focused conversion moments. [brand]
- **Iris**: `#9580ff` — Register button and gradient endpoint — a slightly deeper lavender for secondary action emphasis [brand]
- **Mint**: `#33c758` — Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Mint Wash**: `#def6e4` — Soft section background, alternate surface, and quiet card fill. Use as a supporting accent, not as a status color [accent]
- **Amber**: `#ffa600` — Yellow text accent for links, tags, and emphasized short phrases [accent]
- **Sky**: `#2c78fc` — Violet text accent for links, tags, and emphasized short phrases. [accent]
- **Magenta**: `#d6409f` — Visitor profiles category, icon accents — vivid pink that earns its place by mapping to one specific feature domain [accent]
- **Ember**: `#ff3e00` — Chart fill accents, decorative illustration — warm orange that breaks the cool palette inside data visualizations [accent]

## Typography

- **OpenRunde**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.33 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.33 |
| heading-sm | 24 | — | 1.17 |
| heading | 36 | — | 1.22 |
| heading-lg | 48 | — | 1 |
| display | 60 | — | 1.13 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 16px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '9999px', 'cards': '16px', 'images': '8px', 'inputs': '8px', 'tables': '24px', 'buttons': '9999px'}

## Layout

Full-width sections stacked vertically with max-width ~1200px content centered. Hero is a centered text stack (announcement chip → 60px headline → subtext → dual CTA → partner logos) on white, followed immediately by a full-bleed atmospheric gradient band (blue-to-lavender) containing a floating dashboard mockup in a white card with rounded corners. Feature sections alternate between centered 3-column icon grids and alternating 2-column text+product layouts. All sections use generous 64px+ vertical breathing room. Navigation is a single centered pill-bar floating at the top with no sticky behavior visible. Footer is minimal, multi-column link grid.

## Surfaces / Elevation

- **Canvas**
- **Linen Band**
- **Mist Fill**
- **Mint Wash**

**Shadow tokens:**

## Imagery

Minimal product photography — no lifestyle imagery, no people. Visual content is dominated by dashboard screenshots rendered as hero artwork (the analytics UI mockup in the gradient band) and small grayscale partner logos (Temple, inbound, Buildkite, etc.) used as social proof. Decorative gradients in the blue-to-lavender spectrum appear as atmospheric bands behind product imagery. Iconography is flat, single-color, circular containers — no outlined or illustrated icons, just solid filled glyphs in a 40px Lavender circle.

## Design Principles

### Do

- Use Lavender (#918df6) exclusively for the primary action button — never for body text, borders, or decorative elements.
- Set display headlines at 60px/600 with -3px letter-spacing; the tight tracking is what makes the type feel engineered.
- Use 9999px radius on every button, chip, and tag — the pill shape is a signature.
- Apply 1px solid Fog (#e8e8e8) borders on cards and tables; avoid heavy box-shadows for surface definition.
- Pair Mint (#33c758) with Mint Wash (#def6e4) backgrounds for positive metric callouts; never use green text on white without the pastel fill.
- Use OpenRunde weight 500 for all headings and buttons; reserve weight 400 for body and captions.
- Center the hero headline and CTA stack; let the whitespace below the 60px display do the work.

### Don't

- Don't use Iris (#9580ff) for body CTAs — it's reserved for the Register nav button to differentiate from the main Lavender CTA.
- Don't apply elevation shadows larger than the three-layer stack — dramatic drop shadows break the flat aesthetic.
- Don't mix multiple accent colors in one component — each feature category gets exactly one color (Sky for realtime, Amber for performance, Magenta for profiles).
- Don't set heading text in pure black (#000000) — use Carbon (#181925) for the slight cool tint.
- Don't use Ember (#ff3e00) for UI chrome — it's decorative-only, for chart fills and illustration.
- Don't break the pill-radius convention with rectangular buttons or sharp-cornered tags.
- Don't add background colors to feature card containers — they should sit on pure white with only icon + text.

## Components

### Primary Action Button (Filled)

Pill shape (9999px radius), Lavender (#918df6) fill, white text, OpenRunde 14px weight 500, letter-spacing -0.32px, padding 10px 20px, no border. Subtle shadow: rgba(0,0,0,0.08) 0px 1px 1px 1px + rgba(0,0,0,0.06) 0px 0px 0px 0.5px.

### Register Button (Deeper Lavender)

Pill shape, Iris (#9580ff) fill, white text, OpenRunde 14px weight 500, padding 6px 10px. Slightly deeper saturation differentiates from the main CTA.

### Ghost Button

Transparent fill, Graphite (#666666) text, no border, pill shape (9999px radius), OpenRunde 14px weight 500, padding 10px 20px. Relies on whitespace and contrast alone.

### Text Link Button

Transparent fill, Carbon (#181925) text, 12px horizontal padding, no border, no radius. Hairline underline on hover. Weight 500, 14px.

### Announcement Chip

White fill, Sky (#2c78fc) 'NEW' tag text + Carbon (#181925) body text, thin border, pill shape (9999px radius), inline icon. 14px weight 500.

### Navigation Pill

White fill, Carbon text, full pill container (9999px radius) wrapping nav items. Active state shows Lavender underline or fill. Padding 8px internal.

### Tab Bar (Dashboard Tabs)

Horizontal tab row, white fill, Ash (#999999) inactive text, Carbon active text with Lavender underline indicator. 14px weight 500, no background fill change.

### Feature Card

Transparent fill (or very light wash), no border, no shadow, Lavender icon circle (40px) above Carbon bold heading + Graphite body. Center-aligned, 32px vertical padding.

### Pricing Tier Card

White fill, 1px Fog (#e8e8e8) border, 24px radius, 64px vertical / 32px horizontal padding, no shadow. Carbon heading, Graphite feature list.

### Metric Callout Card

White fill, 1px Fog border, 16px radius, tight padding (12px). Mint (#33c758) for positive delta text, Ember (#ff3e00) for negative. Label in Ash, value in Carbon bold.

### Dashboard Panel Card

White fill, 1px Fog border, 16px radius, 20px padding. Carbon heading, small Ash caption. Soft inner shadow for depth: rgba(0,0,0,0.06) 0px 1px 3px + rgba(0,0,0,0.06) 0px 8px 16px.

### Data Table

White fill, 1px Fog (#e8e8e8) gridlines, 24px container radius, no row striping. OpenRunde 12-14px weight 400-500. Header row in Carbon bold, body in Graphite.

### Avatar Circle

40px circle, photographic fill, no border or 1px white ring. Used sparingly in nav and dashboard header.

## Similar Design Systems

- {'why': 'Same white-canvas analytics aesthetic with a single vivid accent color for CTAs, generous spacing, and pill-shaped controls', 'business': 'Plausible Analytics'}
- {'why': 'Same hairline-border-on-white surface treatment, tight geometric type with negative tracking, and minimal elevation philosophy', 'business': 'Linear'}
- {'why': 'Same privacy-first SaaS pattern: monochrome spine with one brand color doing CTA duty, flat cards, and tight typographic scale', 'business': 'Fathom Analytics'}
- {'why': 'Same engineering-blueprint visual language: white canvas, subtle gray borders, single accent gradient for hero bands, geometric sans-serif type', 'business': 'Vercel'}
- {'why': 'Same pill-button convention, pastel accent surfaces for positive states, and flat minimal-elevation card aesthetic', 'business': 'Cal.com'}

## Agent Prompt Guide

## Quick Color Reference
- text (primary): #181925 Carbon
- text (secondary): #666666 Graphite
- text (muted): #999999 Ash
- background: #ffffff Paper White
- border: #e8e8e8 Fog
- accent / primary action: #918df6 (filled action)
- primary action: #918df6 (filled action)

## 3-5 Example Component Prompts

1. Create a Primary Action Button: #918df6 background, #181925 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Dashboard Metric Card**: White (#ffffff) fill, 1px solid #e8e8e8 border, 16px radius, padding 12px. Label 'Revenue' at 12px weight 400, color #999999. Value 'A$750' at 24px weight 500, color #181925. Delta '+20%' at 12px weight 500, color #33c758.

3. **Feature Card (3-column grid)**: White background, no border, no shadow. Lavender (#918df6) icon in 40px circle, fill #918df6, white glyph centered. Heading at 18px weight 500, color #181925, letter-spacing -0.32px. Body at 16px weight 400, color #666666. Center-aligned text, 32px vertical padding.

4. **Announcement Chip**: White (#ffffff) fill, 1px border #e8e8e8, 9999px radius, padding 6px 12px. 'NEW' tag in #2c78fc weight 500 12px, body text in #181925 weight 500 14px, arrow icon in #181925.

5. **Tab Bar**: Horizontal row, white background, no border between tabs. Inactive tab text at 14px weight 500, color #999999. Active tab text at 14px weight 500, color #181925, with 2px solid #918df6 underline indicator.

## Gradient System

Four gradients detected, used as atmospheric bands rather than UI fills:
1. Sky→Lavender: linear-gradient(to right in oklab, #2c78fc 0%, #918df6 100%) — primary hero band behind dashboard mockup
2. Shimmer gray: linear-gradient(90deg, #b3b3b3 25%, #666666 50%, #b3b3b3 75%) — skeleton loading state
3. Pale sky progression: linear-gradient(to right in oklab, #bed5fe 0%, #bed5fe 50%, #00c4ff 100%) — chart fill
4. Pale sky→lavender: linear-gradient(to right in oklab, #bed5fe 0%, #ebf2ff 50%, #918df6 100%) — decorative accent

Use gradients only as full-bleed section backgrounds or chart fills — never on buttons, cards, or text.
