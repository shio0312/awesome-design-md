# Sauce Labs — Design System

> **North Star**: Neon-lit command center on obsidian glass — a dark engineering console where a single green pulse marks every live signal.
> **Theme**: dark
> **Source**: https://saucelabs.com
> **Refero Style**: https://styles.refero.design/style/d271a6c4-942f-4abf-a3de-66795f15f031
> **Synced**: 2026-09-01

## Overview

Sauce Labs operates as a neon-lit engineering console: deep obsidian canvas (#132322) with white precision typography and a single vivid green (#3ddc91) that activates every interactive surface. The system alternates between dark structural bands and light content cards (#edf7f5), creating rhythm through luminance contrast rather than ornament or elevation. Components are confident and generously rounded — 56px pill buttons, 20px card radii, minimal shadow — reading as high-end developer tooling where the product's intelligence is the visual subject. The green accent is rationed: it appears on primary actions, active tab states, announcement bars, and stat highlights, never as decoration, which gives it real semantic weight.

## Color Palette

- **Obsidian Shell**: `#132322` — Primary page background, dark navigation, dark card surfaces — the structural canvas that absorbs everything else and makes the green accent feel electric by contrast [neutral]
- **Pure White**: `#ffffff` — Primary text on dark surfaces, card content backgrounds, light section canvases — maximum contrast against the obsidian shell [neutral]
- **Mint Frost**: `#edf7f5` — Light content card surfaces, elevated feature panels — the bright counterpoint that breaks up dark sections and hosts detailed content [neutral]
- **Deep Abyss**: `#0e1a19` — Darker surface variant for nested elements, deep card backgrounds, gradient endpoints — pushes further into the void when extra depth is needed [neutral]
- **Charcoal**: `#070f0f` — Darkest surface for overlays, modals, and maximum-contrast panels [neutral]
- **Fog Border**: `#d0d3d3` — Hairline dividers and borders on light surfaces — quiet structural lines that never compete with content [neutral]
- **Stone Border**: `#b2b6b4` — Medium borders on light cards, secondary dividers, subtle frame lines [neutral]
- **Slate Text**: `#828786` — Muted body text, captions on light backgrounds, secondary labels [neutral]
- **Graphite Fill**: `#424f4f` — Icon fills, decorative SVG strokes on light sections [neutral]
- **Pure Black**: `#000000` — SVG icon fills, high-contrast decorative strokes — graphic asset workhorse [neutral]
- **Neon Pulse**: `#3ddc91` — Green action color for filled buttons, selected navigation states, and focused conversion moments. [brand]
- **Mint Whisper**: `#97ddbc` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color [accent]
- **Signal Yellow**: `#ffcd48` — Accent fills within isometric illustrations and product mockups — a warm punctuation that breaks the green monochrome and adds dimensional interest to graphics [accent]

## Typography

- **Aeonik**
- **AeonikFono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| body-sm | 14 | — | 1.45 |
| body | 16 | — | 1.5 |
| body-lg | 18 | — | 1.45 |
| subheading | 24 | — | 1.4 |
| heading-sm | 32 | — | 1.22 |
| heading | 40 | — | 1.2 |
| heading-lg | 48 | — | 1.12 |
| display | 64 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 24px
- **Section Gap**: 80px
- **Border Radius**: {'tabs': '56px', 'cards': '20px', 'buttons': '56px', 'largeCards': '60px', 'smallElements': '10px'}

## Layout

Full-bleed dark canvas with max-width 1200px content containers. The hero is a split composition: left-aligned headline and CTAs (roughly 50% width) with a right-aligned isometric product illustration. Section rhythm alternates between dark structural bands and light content cards (mint frost #edf7f5) that float on the dark background. Logo bar uses evenly-spaced dark tiles in a single row. Feature sections use centered headline stacks with tab-pill navigation below. Stats appear as a horizontal row of large green numbers with small uppercase labels. Navigation is a single dark bar with logo left, centered nav items, and CTA cluster right. The overall feel is a dark dashboard with bright content cards rising from it.

## Surfaces / Elevation

- **Obsidian Canvas**
- **Deep Card**
- **Mint Card**
- **White Panel**

**Shadow tokens:**

## Imagery

The visual language centers on isometric product illustrations — a 3D phone rendering with stacked colored cards representing product modules (AI-Powered Insights, Mobile App Testing, Web Testing, Model App Distribution, Error Reporting, Visual Testing). Illustrations use flat geometric shapes with soft shadows, brand greens (#3ddc91, #97ddbc) and signal yellow (#ffcd48) for card surfaces, and thin connector lines linking modules. Product screenshots appear in dashboard mockup panels with realistic UI chrome. Logo bars for social proof use dark tile containers with white monochrome logos. No photography — the product itself is the hero, rendered as 3D isometric and flat UI mockups.

## Design Principles

### Do

- Use #3ddc91 exclusively for primary actions, active states, and the announcement bar — ration it to preserve its signal weight
- Set all buttons to 56px border-radius for the fully pill-shaped interactive language
- Use 60px radius for large content cards and 20px for smaller nested cards
- Place uppercase eyebrow labels (AeonikFono 9px, 0.45px tracking) above section headlines as structural anchors
- Alternate between dark #132322 bands and light #edf7f5 content cards to create section rhythm through luminance contrast
- Set Aeonik body text to weight 400 with -0.08px tracking at 16px for the clean geometric feel
- Use #0e1a19 for nested dark surfaces to create depth within the obsidian shell without introducing new hues

### Don't

- Don't apply #3ddc48 or any green to decorative non-interactive elements — the accent only works as a live signal because it's rationed
- Don't use square or slightly-rounded buttons — the 56px pill is non-negotiable for system identity
- Don't place light cards directly adjacent to each other without a dark band between them
- Don't use box shadows heavier than rgba(0,0,0,0.04) — depth comes from luminance layers, not drop shadows
- Don't use color gradients — the system is entirely flat with luminance-defined depth
- Don't use body weight above 400 or display weight above 500 — the thin weights are the signature
- Don't introduce new chromatic colors beyond the defined palette — green, yellow, and white are the only voices

## Components

### Primary CTA Button (Pill)

56px border-radius (fully pill-shaped). Background: #3ddc91 (Neon Pulse). Text: #132322, Aeonik 16px weight 400, letter-spacing -0.08px. Padding: 14px 28px. No border. On hover, slightly brightens. This is the single most prominent interactive element in the system.

### Ghost CTA Button (Pill)

56px border-radius. Background: transparent. Border: 1.5px solid #ffffff. Text: #ffffff, Aeonik 16px weight 400. Padding: 14px 28px. Pairs directly beside the primary green pill in the nav and hero.

### Dark Text Button

No background, no border. Text: #ffffff, Aeonik 15px weight 400. Minimal padding. Sits left of the CTA cluster in navigation.

### Announcement Banner

Full-width bar. Background: #3ddc91 (Neon Pulse). Text: #132322, Aeonik 14px weight 400. Small close (×) button on the right. Creates immediate green punctuation at the page entry point.

### Navigation Bar

Full-width dark bar. Background: #132322. Logo left, nav items centered (Aeonik 15px white, with dropdown chevrons), CTA cluster right. No visible border or shadow — sits directly on the dark canvas.

### Stat Block

Horizontal row. Number: #3ddc91, AeonikFono 48px weight 500. Label: #ffffff at ~50% opacity, Aeonik 9px weight 400, letter-spacing 0.45px, uppercase. No container — floats directly on the dark hero background.

### Logo Bar Tile

Dark rounded card (60px radius, background: #0e1a19) containing a white monochrome logo. Arranged in a horizontal row with even spacing. Logos sit at white or light gray for contrast against the dark tile.

### Light Content Card

60px border-radius. Background: #edf7f5 (Mint Frost). Padding: 48px internal. Shadow: rgba(0,0,0,0.04) 1px 0px 9px 2px. Contains headline, description text, tab navigation, and product preview. The bright counterpoint to the dark page.

### Tab Pill Navigation

Horizontal row of pill-shaped tabs. Active tab: 56px radius, #3ddc91 background, #132322 text. Inactive tabs: 56px radius, transparent background, #828786 text. Padding: 12px 24px. Arrow chevrons at both ends for overflow indication.

### Eyebrow Label

AeonikFono 9px weight 400, letter-spacing 0.45px, uppercase. Color: #132322 on light cards, #3ddc91 on dark sections. Examples: 'ENTERPRISE-READY. AI-DRIVEN. ONE UNIFIED VIEW.'

### Hero Headline

AeonikFono 64px weight 500, line-height 1.10, color #ffffff on dark hero. Multi-line, left-aligned. The largest text element on the page — sets the tone for everything below.

### Isometric Product Illustration

3D isometric phone rendering with stacked colored module cards (green #3ddc91, mint #97ddbc, yellow #ffcd48, light gray). Thin connecting lines and small floating elements (Test, Build, Deploy, Operate labels). Sits on the right side of the hero split.

### Product Screenshot Panel

Embedded within Mint Frost content cards. Shows realistic product UI with browser chrome, dashboard widgets, and data visualizations. Background: #ffffff for the screen area, #0e1a19 for the chrome frame.

## Similar Design Systems

- {'why': 'Same dark-canvas + single-accent approach with pill-shaped CTAs and minimal shadow — both treat the dark background as a stage for a single luminous signal color', 'business': 'Vercel'}
- {'why': 'Identical dark navigation, restrained green accent on interactive states, geometric sans typography, and the same sense of a product-first engineering tool', 'business': 'Linear'}
- {'why': 'Dark devtools dashboard aesthetic with monospace-influenced geometric sans, flat surfaces, and accent colors reserved for live data signals', 'business': 'Datadog'}
- {'why': 'Dark hero with vivid single-color accent, generous card radii, uppercase tracked-out eyebrow labels, and alternating dark/light content bands', 'business': 'Resend'}

## Agent Prompt Guide

**Quick Color Reference**
- text on dark: #ffffff
- text on light: #132322
- dark canvas: #132322
- light card: #edf7f5
- border (light): #d0d3d3
- primary action: #3ddc91 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #3ddc91 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Build a stat block row: Four columns on #132322 background. Each shows a number in AeonikFono 48px weight 500, color #3ddc91, with a label below in AeonikFono 9px weight 400, letter-spacing 0.45px, uppercase, color #ffffff at 50% opacity.

3. Build a light content card: 60px border-radius, background #edf7f5, padding 48px. Eyebrow label in AeonikFono 9px weight 400, letter-spacing 0.45px, uppercase, color #132322. Headline in AeonikFono 40px weight 500, color #132322, line-height 1.20. Body text in Aeonik 16px, color #132322.

4. Build a tab pill navigation row: Five pill tabs, each 56px radius, 12px 24px padding. Active tab: #3ddc91 background, #132322 text. Inactive: transparent background, #828786 text. Aeonik 16px weight 400 throughout. Left/right chevron arrows in #828786.

5. Build a logo bar: Row of five tiles, each 60px border-radius, #0e1a19 background, 120px tall. Inside each: white monochrome client logo, centered. Even 24px gap between tiles.

## Dark/Light Rhythm

The page oscillates between dark structural sections and light content cards. Dark sections host: navigation, hero, stats, CTA bands, footer. Light cards (Mint Frost #edf7f5, 60px radius) float on the dark canvas to host: feature deep-dives, platform overviews, product module breakdowns. This luminance alternation replaces the need for section dividers, borders, or heavy shadows. Never place a light card on a light card or a dark card on a dark card — the contrast is the structure.
