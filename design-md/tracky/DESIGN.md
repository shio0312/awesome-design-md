# Tracky — Design System

> **North Star**: doodled planner on warm paper
> **Theme**: light
> **Source**: https://tracky.so
> **Refero Style**: https://styles.refero.design/style/34788d94-1147-4d38-8df7-6f47ef7efb12
> **Synced**: 2026-09-01

## Overview

Tracky reads like a creative's bullet journal that became a product: a warm light canvas (#f2f2f2) carries a near-black navy (#151b31) workhorse for text, borders, and primary actions, while coral red (#ff5858) and mint green (#86e0c1) appear as small functional punctuation for emphasis and live states. GRIFTER supplies the brand's voice at display scale — chunky, hand-printed, slightly loosened tracking — while Inter handles all UI and body work at compact, tightly-tracked sizes. Components sit on soft 8px and 16px radii with whisper-light shadows, generous section breathing, and hand-drawn illustration accents (doodles, organic blobs, bunny mascot) that make project management feel like doodling in a notebook rather than filing a ticket.

## Color Palette

- **Inkwell Navy**: `#151b31` — Primary buttons, dominant text and borders, dark feature card backgrounds — the workhorse near-black that reads as softer and warmer than pure #000 [brand]
- **Coral Emphasis**: `#ff5858` — Accent text for key words in headlines, emphasis highlights, and selective links — warm red against navy creates playful energy without corporate aggression [accent]
- **Mint Pulse**: `#86e0c1` — Green state accent for badges, validation surfaces, and short status labels. [semantic]
- **Butter Yellow**: `#fedf89` — Top announcement banner, highlight washes — warm pastel yellow for friendly alerts that don't shout [accent]
- **Graphite**: `#333333` — Secondary text, hairline borders, icon strokes — sits between navy and pure black for less-load-bearing elements [neutral]
- **Slate**: `#6d6f75` — Muted helper text, subdued borders, caption-level content — the cool gray for de-emphasized UI [neutral]
- **Ash Canvas**: `#f2f2f2` — Page background — warm light gray that lifts white cards without the coldness of pure white [neutral]
- **Paper White**: `#ffffff` — Card surfaces, button labels, overlapping panels — the surface layer above the Ash Canvas [neutral]
- **Pure Ink**: `#000000` — Maximum-emphasis icons, strongest borders, logo mark — used sparingly where absolute contrast is required [neutral]
- **Warm Stone**: `#e8e7e5` — Card drop-shadow tint — warm desaturated beige replaces cold black shadows for a paper-like depth [neutral]

## Typography

- **GRIFTER**
- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.55 |
| body | 16 | — | 1.55 |
| body-lg | 18 | — | 1.5 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.3 |
| heading | 36 | — | 1.2 |
| heading-lg | 48 | — | 1.16 |
| display | 64 | — | 1.1 |
| display-xl | 108 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 20px
- **Element Gap**: 16px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '16px', 'badges': '8px', 'inputs': '8px', 'buttons': '8px', 'featureCards': '24px'}

## Layout

Single-column max-width contained flow at 1200px. Hero is full-width on Ash Canvas with a centered display headline mixed with inline hand-drawn illustration and a centered Filled Primary Button. Below the hero, content flows in vertical sections of 80px gap, alternating between light sections (Ash Canvas with Paper White cards) and dark sections (Inkwell Navy feature cards with overlapping white product-preview cards rotated -3 to -8 degrees). No multi-column grids in the main flow — the system stays single-column, letting the dark feature cards provide visual variety through inversion rather than through column complexity. Navigation is a minimal sticky-or-static top bar with logo left and a single auth button right, no mega-menu. A full-width Butter Yellow announcement banner sits above the header. Sections feel spacious and breathing, with each dark card acting as a full-bleed moment of inversion before returning to the light canvas.

## Surfaces / Elevation

- **Ash Canvas**
- **Paper White**
- **Butter Yellow**
- **Inkwell Navy**

**Shadow tokens:**

## Imagery

Illustration-first visual language with zero photography. Hand-drawn SVG characters (a bunny mascot), organic blob shapes in Mint Pulse and a soft blue scattered as decorative atmosphere, and inline doodled annotations with curved arrows and handwritten labels ('start → stop → continue', 'click me'). Illustrations are outlined and lightly filled in brand colors, positioned to overlap text and cards rather than sit in dedicated image containers. The bunny character and organic shapes are decorative atmosphere, not explanatory content — they signal creativity and approachability. No product screenshots in the traditional sense; instead, live product elements (timer widget) appear inline within headlines as contextual demos. Overall density is text-dominant with illustration as accent punctuation, never as hero imagery.

## Design Principles

### Do

- Use GRIFTER 64px+ weight 700 for hero and section openers — its hand-printed character is the brand voice, not decoration
- Apply Coral Emphasis (#ff5858) to exactly one word or phrase per headline for energy — never entire headings
- Pair Inkwell Navy (#151b31) fills with Paper White (#ffffff) text on primary buttons at 8px radius — this is the canonical CTA
- Use Ash Canvas (#f2f2f2) as the universal page background — it lifts white cards with a warm paper feel
- Apply the warm stone shadow rgba(138,133,125,0.2) 0 1px 4px on feature cards instead of cold black shadows
- Use Inter at -0.01em tracking for all UI text — let GRIFTER carry the personality at display scale
- Overlap a tilted Paper White card onto a dark Inkwell Navy feature card to create visual product demo moments

### Don't

- Don't use GRIFTER for body text, buttons, navigation, or form labels — it loses readability below 24px and dilutes the brand voice
- Don't apply Coral Emphasis (#ff5858) to more than one element per visual zone — it loses emphasis when overused
- Don't use pure #000000 as a background or large fill — Inkwell Navy (#151b31) is the system black, pure black is reserved for icon strokes
- Don't stack multiple bold shadows on elevated components — the system relies on 1-4px blurs with under 25% opacity
- Don't use radius below 8px on interactive elements — the softness is part of the friendly personality
- Don't use cold gray drop-shadows (rgba(0,0,0,*)) on cards — the warm stone shadow is the signature depth treatment
- Don't introduce new accent colors — the system speaks through navy, coral, mint, and butter yellow; adding more breaks the notebook palette

## Components

### Filled Primary Button

Inkwell Navy (#151b31) background, Paper White (#ffffff) text, Inter 16px weight 500-600, 8px radius, 13px vertical / 20px horizontal padding, subtle 0 1px 3px shadow. Tight tracking and compact sizing keep it functional rather than celebratory.

### Outlined Ghost Button

White or transparent background, 1px border in #e8e7e5 or Slate (#6d6f75), Inter 16px weight 500 in Inkwell Navy. 8px radius, 8px vertical / 16px horizontal padding. No shadow.

### Inverse Button

White background or white text on Inkwell Navy card, 8px radius, 13px-16px vertical padding. Same compact Inter treatment as primary button, inverted for dark surfaces.

### Top Announcement Banner

Butter Yellow (#fedf89) background spanning full viewport width, Inter 14-16px centered, Inkwell Navy text with a 'Let's Talk' link in Coral Emphasis. Close (×) button at right edge.

### Navigation Header

Minimal: logo mark (Inkwell Navy circle with white play-shape) + 'Tracky' wordmark in Inter 600 on left, Outlined Ghost Button on right. Transparent or Ash Canvas background, no shadow.

### Hero Display Headline

GRIFTER 64px-108px weight 700 in Inkwell Navy, with one phrase swapped to Coral Emphasis for energy. Centered or left-aligned, 1.0-1.1 line-height, 1.92px tracking. Often mixed with inline hand-drawn SVG illustration between phrases.

### Dark Feature Card

Inkwell Navy (#151b31) background, 16-24px radius, generous 40-48px internal padding. GRIFTER or Inter display heading in white, body text in Paper White at 70% opacity, Inverse Button for action. Warm stone shadow: 0 1px 4px rgba(138,133,125,0.2).

### Overlap White Card

Paper White (#ffffff) surface, 16px radius, slight rotation (-3 to -8 degrees), positioned to overlap the right edge of the dark card. No visible border, relies on contrast against dark surface.

### Timer Widget

White pill-shaped card, Inkwell Navy text showing '0:00:00', circular Mint Pulse (#86e0c1) play button icon, small icon button to the right. Sits inline within hero text to demonstrate product contextually.

### Annotation Label

GRIFTER or similar hand-printed font at 24-36px, typically in a blue or Inkwell Navy stroke, with a curved hand-drawn arrow. Positioned above or beside interactive elements to suggest 'try this'. Underlines are hand-drawn squiggles in Coral Emphasis.

### Text Link

Inter 16-18px weight 500-600, Coral Emphasis (#ff5858) for emphasis links or Inkwell Navy for utility links. No underline by default; underline appears on hover in the same color or in Graphite.

### Badge / Tag

8px radius, 8-10px vertical / 12-16px horizontal padding, Inter 12px weight 500. Backgrounds: Mint Pulse for success, Butter Yellow for highlight, Ash Canvas for neutral. Text in Inkwell Navy.

## Similar Design Systems

- {'why': 'Same hand-crafted personality with display type, muted canvas, and single-color accent punctuation in headlines', 'business': 'Notion'}
- {'why': 'Same project management space with playful illustration accents and a warm light canvas, though Trello leans more on saturated brand blue', 'business': 'Trello'}
- {'why': 'Same bold display typography paired with Inter UI, generous spacing, and personality-forward micro-illustrations', 'business': 'Pitch'}
- {'why': 'Same product management space with a single dominant dark color as workhorse, compact UI, and inverted dark feature cards', 'business': 'Height'}
- {'why': 'Same tight Inter tracking, compact 8px-radius components, and a near-black navy as the primary workhorse color', 'business': 'Linear'}

## Agent Prompt Guide

**Quick Color Reference**
- text (primary): #151b31 (Inkwell Navy)
- text (muted): #6d6f75 (Slate)
- background: #f2f2f2 (Ash Canvas)
- surface (card): #ffffff (Paper White)
- border: #333333 (Graphite) / #6d6f75 (Slate)
- accent: #ff5858 (Coral Emphasis)
- primary action: #151b31 (filled action)

**Example Component Prompts**

1. *Create a hero section:* Ash Canvas (#f2f2f2) full-width background. Centered headline at 64px GRIFTER weight 700, #151b31, letter-spacing 1.92px. The phrase 'actually love' set in #ff5858. Subtext at 18px Inter weight 400, #6d6f75. Primary button: #151b31 background, #ffffff text, Inter 16px weight 500, 8px radius, 13px vertical / 20px horizontal padding.

2. *Create a dark feature card:* #151b31 background, 16px radius, 48px padding. GRIFTER 36px weight 700 heading in #ffffff. Body at 16px Inter weight 400, #ffffff at 80% opacity. White Inverse Button: #ffffff background, #151b31 text, 8px radius, 16px / 24px padding. Overlap a Paper White card rotated -5 degrees, 16px radius, no border, positioned to bleed off the right edge.

3. *Create a top announcement banner:* Full-width #fedf89 background, 40px vertical padding. Centered Inter 14px weight 500 in #151b31, with 'Let's Talk' as a #ff5858 link. × close button at right in #151b31.

4. *Create a timer widget demo element:* #ffffff background pill, 8px radius, 12px vertical / 16px horizontal padding. '0:00:00' in Inter 16px weight 600, #151b31. Circular play button: 32px diameter, #86e0c1 background, #151b31 triangle icon.

5. *Create a feature badge:* #86e0c1 background, 8px radius, 8px vertical / 12px horizontal padding. Inter 12px weight 500, #151b31 text.
