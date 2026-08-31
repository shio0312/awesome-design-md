# Shares — Design System

> **North Star**: Ivory terminal with violet pulse — a clinical white workspace where one color marks every deliberate action.
> **Theme**: light
> **Source**: https://shares.io
> **Refero Style**: https://styles.refero.design/style/cd293b92-71a3-4cc2-a56b-0fa60425b42a
> **Synced**: 2026-09-01

## Overview

A monochromatic fintech interface on near-white surfaces, where one vivid violet does all the talking. The visual language is sparse and confident: no decorative gradients, no chromatic ornamentation, no shadow theatrics. Everything sits on flat porcelain with dark charcoal text, and the only color that earns attention is Signal Violet (#594ff4), reserved strictly for action — filled buttons, active links, brand marks. Components lean on geometry rather than depth: pill-shaped controls (99px radius), generously rounded cards (36px), and soft 1px gray dividers instead of elevation. Typography is geometric and tightly tracked, with large headlines at compressed line-heights (1.05–1.15) that feel architectural rather than editorial. Product mockups float in layered, slightly overlapping arrangements — phone + dashboard + code panel — anchored by a single brand color.

## Color Palette

- **Signal Violet**: `#594ff4` — Primary action fill, active links, brand iconography — the only chromatic color in the system, creating high-contrast urgency against the monochrome canvas [brand]
- **Inkstone**: `#1f1f1f` — Primary headings, body text emphasis, dark surface fills — the dominant dark neutral [neutral]
- **Graphite**: `#333333` — Secondary text, dense borders, icon strokes — the most-used neutral [neutral]
- **Slate**: `#5d5d5d` — Muted body text, navigation subtext, secondary borders [neutral]
- **Smoke**: `#888888` — Tertiary text, helper copy, light borders [neutral]
- **Ash**: `#b0b0b0` — Muted link text, hairline dividers, inactive borders [neutral]
- **Mist**: `#e7e7e7` — Image and photo borders, very light separators [neutral]
- **Cloud**: `#f6f6f6` — Card surfaces, FAQ panels, subtle background tints — the soft elevation layer [neutral]
- **Porcelain**: `#ffffff` — Page canvas, button text on violet fill, primary card background — the dominant base surface [neutral]
- **Obsidian**: `#000000` — Footer fill, maximum-contrast text — used sparingly for the darkest dark [neutral]

## Typography

- **Aeonik**
- **Rubik**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.5 |
| heading-sm | 20 | — | 1.33 |
| heading | 26 | — | 1.2 |
| heading-lg | 36 | — | 1.15 |
| display | 56 | — | 1.1 |
| display-lg | 72 | — | 1.05 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 24px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '99px', 'cards': '36px', 'images': '10px', 'inputs': '16px', 'buttons': '99px', 'accordion': '16px'}

## Layout

Max-width 1200px centered container, full-bleed sections within that constraint. Hero: centered headline (72px) + subtext (17–18px) stacked vertically, then layered product mockup cluster below. Feature highlights: 3-column equal grid with icon + heading + body, centered within container. Product detail sections: 2-column text-left / visual-right, alternating direction down the page. FAQ: centered single-column with max-width ~720px. Footer: full-bleed dark band spanning edge-to-edge. Navigation: sticky top bar, white, 64–80px height, logo-left / nav-center / CTA-right. Section rhythm: generous vertical breathing (64–96px between sections) with seamless flow, no alternating dark bands.

## Surfaces / Elevation

- **Porcelain**
- **Cloud**
- **Signal Violet**
- **Inkstone**

**Shadow tokens:**

## Imagery

No photography, no illustration, no decorative graphics. The visual language is entirely product-mockup-driven: floating phone screens, dashboard panels, and code editor windows arranged in layered, slightly overlapping compositions. Mockups have 10–16px border-radius and one soft shadow pattern. Inside the product, a vivid green line chart (#1AAB8B approximate) provides the only secondary color accent. The product IS the hero — there are no lifestyle images, no team photos, no abstract backgrounds. Icons are minimal line-art, 1.5–2px stroke, monocolor (Signal Violet or Inkstone).

## Design Principles

### Do

- Use #594ff4 Signal Violet exclusively for primary actions, active states, and brand iconography — never for decorative or background purposes
- Set all interactive buttons to 99px border-radius for the signature pill geometry
- Set all content cards to 36px border-radius with 32px internal padding for the soft, generous feel
- Use Aeonik 500 for body and UI, Aeonik 700 for headings — never mix in other weights or families
- Apply 0.075em letter-spacing to all uppercase eyebrows and display headlines for the tracked-out premium cadence
- Use #f6f6f6 Cloud as the card surface to create elevation through tint, not shadow
- Reserve the single soft shadow pattern for floating product mockups only — never for buttons, cards, or inputs
- Keep section gaps at 64px and element gaps at 24px to maintain the comfortable, architectural rhythm

### Don't

- Do not introduce additional chromatic colors — the system is 98% monochrome and any new hue breaks the discipline
- Do not use sharp corners (0–4px) on cards or images — all containers should be 16px+ radius
- Do not apply heavy drop shadows to UI elements — depth comes from surface tint, not blur
- Do not use gradient fills anywhere — the system is flat by design
- Do not use serif, slab, or display fonts — Aeonik (or Inter/DM Sans substitute) is the only typeface
- Do not set body text above 16px or headings below 26px — the type scale jumps are deliberate
- Do not use emoji or multicolor icon sets — icons are monoline, monocolor, 1.5–2px stroke
- Do not add animations, parallax, or scroll-triggered effects — the system is static and clinical

## Components

### Pill Primary Button

Filled Signal Violet (#594ff4) background, white text, 99px border-radius (full pill), Aeonik 500 at 16px. Padding 12px 28px or 16px 28px depending on size. No shadow. The pill geometry and single-color confidence make every CTA visually unmistakable against the monochrome canvas.

### Ghost Navigation Button

Transparent or white background with Signal Violet border, Signal Violet text, 99px radius, Aeonik 500 at 16px, padding 10px 24px. Lighter visual weight than the primary pill, signaling secondary action hierarchy.

### Feature Highlight Card

Transparent or white background, no border. Icon at top (Signal Violet stroke), heading in Aeonik 700 at 20px Inkstone (#1f1f1f), body in Aeonik 500 at 16px Slate (#5d5d5d). Vertical rhythm of 16–24px between elements. The card does not carry its own surface — the white page IS the card.

### Product Showcase Card

White or Cloud (#f6f6f6) background, 36px border-radius, 32px internal padding. Left column: heading (Aeonik 700 36px Inkstone), body (Aeonik 500 16px Slate), CTA pill button. Right column: layered product mockup floating slightly above the card surface with the single soft shadow pattern.

### FAQ Accordion Item

Cloud (#f6f6f6) background, 16px border-radius, padding 20px 24px. Question text in Aeonik 500 at 16px Inkstone, with a small chevron icon on the right. Closed by default; expanded reveals body text below in lighter Slate. No animation emphasis — the toggle is instant and quiet.

### Navigation Bar

White background, full-width, 64–80px height. Left: logo mark (Signal Violet geometric 'S' + wordmark). Center: nav links (Aeonik 500 16px Inkstone, with dropdown chevrons). Right: Ghost or Primary pill CTA. Hairline bottom border in Ash (#b0b0b0) or none — the nav floats on white with no shadow.

### Layered Product Mockup Cluster

Three overlapping product screenshots arranged with intentional layering: phone mockup front-left, dashboard panel center-right, code/JSON panel back-right. Each panel has 10–16px border-radius and the single shadow pattern (rgba(0,0,0,0.12) 0 0 60px -13px) for soft depth. Accent green line charts inside the dashboard are the only secondary color (from product content, not design tokens).

### Stats Display Block

Large figure in Aeonik 700 at 26–36px Inkstone, with a small percentage delta in muted green below (product data). Label in Aeonik 500 at 14–16px Smoke (#888888) above. Horizontal row layout with 24–32px gaps between stat groups.

### Section Eyebrow Label

Aeonik 500 at 14–16px, letter-spacing 0.075em, uppercase, centered or left-aligned. Color: Inkstone or Smoke. Paired with a large heading below. This eyebrow-to-headline rhythm is the section signature.

### Dark Footer

Obsidian (#000000) or Inkstone (#1f1f1f) background, white and Slate text. Links in Aeonik 500 at 16px. Generous padding (48–64px vertical). Logo, nav columns, and legal text in a multi-column grid. The only dark surface in an otherwise light page — it reads as a definitive close.

### Stat Badge / Tag

99px border-radius, padding 4px 12px, Aeonik 500 at 14px. Two variants: Signal Violet background with white text (active/selected), or Cloud (#f6f6f6) background with Inkstone text (neutral tag).

## Similar Design Systems

- {'why': 'Same monochrome-on-white fintech aesthetic with a single accent color, pill-shaped CTAs, and generous whitespace — both treat the product mockup as the hero visual', 'business': 'Mercury'}
- {'why': 'Shared commitment to a single chromatic accent against a clean white canvas, tight typographic discipline, and pill-shaped primary actions', 'business': 'Stripe'}
- {'why': 'Identical 99px pill-button radius, monochrome interface with one vivid accent, and the same flat-surface-over-shadow elevation philosophy', 'business': 'Linear'}
- {'why': 'Same sparse white-canvas fintech language, dark charcoal typography, and violet-adjacent accent used only for actions — the product UI does the visual heavy lifting', 'business': 'Ramp'}
- {'why': 'Fellow investing platform with a clinical white-interface approach, large rounded product cards, and restrained use of color for functional emphasis only', 'business': 'Wealthfront'}

## Agent Prompt Guide

**Quick Color Reference**
- text (primary): #1f1f1f Inkstone
- text (secondary): #5d5d5d Slate
- text (muted): #888888 Smoke
- background (page): #ffffff Porcelain
- background (card): #f6f6f6 Cloud
- border (hairline): #b0b0b0 Ash
- accent / primary action: #594ff4 (filled action)

**3-5 Example Component Prompts**

1. **Hero Section**: White (#ffffff) page background. Centered headline: Aeonik 700, 72px, #1f1f1f, line-height 1.05, letter-spacing 0.075em. Subtext below: Aeonik 500, 17px, #5d5d5d, line-height 1.50. Below text, a layered product mockup cluster: phone screen (10px radius) overlapping a dashboard panel (16px radius) overlapping a code editor panel (16px radius), all with shadow rgba(0,0,0,0.12) 0 0 60px -13px.

2. **Pill Primary Button**: #594ff4 Signal Violet background, white text, Aeonik 500 at 16px, 99px border-radius, padding 12px 28px, no shadow. Text: 'Get started'.

3. **Feature Highlight Card**: Transparent background (sits on white page). Signal Violet icon at top (monoline, 2px stroke, 32px size). Heading: Aeonik 700, 20px, #1f1f1f. Body: Aeonik 500, 16px, #5d5d5d, line-height 1.50. Vertical gap of 16px between icon, heading, and body.

4. **FAQ Accordion Item**: #f6f6f6 Cloud background, 16px border-radius, padding 20px 24px. Question text: Aeonik 500, 16px, #1f1f1f. Chevron icon on the right (#1f1f1f). No border, no shadow.

5. **Dark Footer**: #000000 or #1f1f1f full-bleed background, 64px vertical padding. Three-column grid of links in Aeonik 500, 16px, white or #b0b0b0 text. Logo mark (Signal Violet geometric shape + white wordmark) at top-left.
