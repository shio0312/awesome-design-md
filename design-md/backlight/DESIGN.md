# Backlight — Design System

> **North Star**: Vermillion stamp on warm vellum — a printed catalog cover where one ink red commands the cream page and everything else stays in quiet grayscale.
> **Theme**: light
> **Source**: https://www.backlight.co
> **Refero Style**: https://styles.refero.design/style/ca9bff3b-d488-46e5-8a32-2d858bb5eed2
> **Synced**: 2026-09-01

## Overview

Backlight uses a warm editorial language built on cream vellum and one vermillion accent. The full-bleed orange-red hero acts as the cover page of a printed catalog, with white type and a single white pill button as the only allowed elements. Below the hero, the canvas shifts to warm cream (#e4ddd5) carrying white cards, dark text, and a thin peach hairline (#f3b8a9) that traces the grid like a printer's rule. Chat-bubble cards are used as a signature device to dramatize team conversations and pain points. The type system is confident but quiet — Instrument Sans with consistent negative tracking creates density without weight, and Fragment Mono punctuates timestamps and metadata. The palette never escalates: no shadows, no gradients, no secondary accents — just warm neutrals, one bold red, and a single full-bleed black band for tonal contrast.

## Color Palette

- **Vermillion**: `#dd3508` — Orange accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color [brand]
- **Peach Hairline**: `#f3b8a9` — Orange outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color [brand]
- **Cream Vellum**: `#e4ddd5` — Page canvas below the hero, input borders, soft surface washes — the warm paper stock everything else sits on [neutral]
- **Bone White**: `#ffffff` — Card surfaces, button fills on the orange hero, nav text on dark/orange, inverted typography — the bright surface layer [neutral]
- **Midnight Ink**: `#151515` — Primary headings, body text, dark section backgrounds, chat bubble fills, button borders on light — the heavy type and the rare full-bleed dark band [neutral]
- **Graphite**: `#4f4f4f` — Card borders, secondary text, muted UI rules — the mid-neutral that softens edges between Bone White and Midnight Ink [neutral]
- **Charcoal**: `#333333` — Link text on light surfaces, image strokes, secondary borders [neutral]
- **Ochre Tan**: `#d7cabb` — Badge backgrounds and borders, secondary surface tint — a warm neutral tag fill that sits between cream and peach [neutral]
- **Press Black**: `#000000` — Icon fills, tight border accents, true-black for print-style contrast moments [neutral]

## Typography

- **Instrument Sans**
- **Fragment Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 17 |
| body-sm | 14 | — | 20 |
| body | 16 | — | 21 |
| subheading | 18 | — | 23 |
| heading-sm | 20 | — | 24 |
| heading | 24 | — | 29 |
| heading-lg | 32 | — | 37 |
| display | 39 | — | 45 |
| display-lg | 48 | — | 48 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16-24px
- **Element Gap**: 16px
- **Section Gap**: 64-96px
- **Border Radius**: {'cards': '8px', 'badges': '60px', 'inputs': '4px', 'buttons': '80px', 'chat-bubbles': '20px'}

## Layout

Backlight is a left-aligned, max-width 1200px layout with full-bleed section bands. The hero is a full-viewport-width Vermillion band with left-aligned headline and email capture. Below the hero, the layout alternates between Cream Vellum canvas and occasional Midnight Ink full-bleed bands. Content blocks use generous 64-96px vertical section gaps. The FAQ section is a single-column list of left-aligned questions with right-aligned Vermillion plus icons. Carousel sections use left/right circular arrow buttons above horizontally-scrolling content. Navigation is a transparent top bar flush with the hero — no sticky behavior, no background fill until the hero ends. The page reads top-to-bottom as a sequence of editorial spreads: orange cover, cream pages with card grids and chat dramatizations, one black inversion page, then a warm footer.

## Surfaces / Elevation

- **Cream Vellum**
- **Bone White**
- **Midnight Ink**
- **Vermillion**

## Imagery

Backlight uses three image modes: (1) small circular avatar portraits inside chat bubble cards, shown at ~32px with a subtle Peach Hairline border, (2) inline product/media thumbnails in the sticky promo banner with a 1px Peach Hairline stroke, and (3) full-bleed media crops on the right edge of content sections, treated with sharp rectangular edges (no rounding) so they read as printed halftones. Photography is warm-toned and editorial — never stock-lifestyle. No illustrations, no 3D renders, no abstract graphics. The visual language is print-catalog: portraits, media stills, and chat artifacts arranged in a grid of cards and bubbles.

## Design Principles

### Do

- Use Vermillion (#dd3508) as a full-bleed hero background — it is the only place this color appears as a surface
- Set border-radius to 80px (full pill) for all primary buttons and to 8px for all cards and rectangular elements
- Apply -0.02em letter-spacing to all Instrument Sans text at 14px and above; use +0.02em at 12px caption
- Use Cream Vellum (#e4ddd5) as the page canvas and Bone White (#ffffff) for all cards and surfaces that sit on it
- Use Fragment Mono at 14px with -0.08em tracking for timestamps, metadata, and small data labels in chat bubbles
- Use chat-bubble cards (dark or light, 20px radius) to dramatize team conversations and social proof moments
- Limit Vermillion accents on light backgrounds to thin 1px borders and small icons (FAQ plus, carousel arrows)

### Don't

- Do not add drop shadows, glow effects, or any box-shadow to cards, buttons, or modals — the system is intentionally flat
- Do not use Vermillion as a filled button background — it is only an outlined-action border and a hero surface
- Do not use Peach Hairline (#f3b8a9) as a text color or interactive fill — it is decorative border only
- Do not introduce a second chromatic accent color — the system is monochromatic warm with one red
- Do not use gradients anywhere in the interface — surfaces are solid colors only
- Do not use Midnight Ink (#151515) as body text on the Vermillion hero — all hero text must be Bone White
- Do not center-align headlines — Backlight's editorial voice is left-aligned with generous left padding

## Components

### Primary Pill Button

Bone White (#ffffff) fill, Midnight Ink (#151515) text, 1px Midnight Ink border, 80px border-radius (full pill), 12px 24px padding, Instrument Sans 14px weight 500. Sits on the Vermillion hero as the only permitted action element.

### Outlined Action Button

Transparent fill, 1px Vermillion (#dd3508) border, Midnight Ink text, 80px border-radius, 12px 24px padding, Instrument Sans 14px weight 500. The chromatic border is the only color this button carries.

### Email Input

Transparent background, 1px Bone White border, Bone White placeholder text, 4px border-radius, Instrument Sans 14px, 12px 16px padding. No focus ring color change — the border remains the same weight.

### Transparent Nav Bar

Sits directly on the Vermillion hero with no background fill. Logo 'BACKLIGHT' left in Bone White, Instrument Sans 12px weight 600, letter-spacing wide (uppercase tracking). Nav items in Bone White, 14px weight 500, with Peach Hairline (#f3b8a9) underline indicating active state. Primary CTA is a Bone White pill button flush right.

### Hero Band

Vermillion (#dd3508) background spanning full viewport width, 64-96px vertical padding, left-aligned content with 1200px max-width. Display headline in Bone White at 48px, body at 18px in Bone White. The hero is the only place Vermillion appears as a surface.

### Dark Contrast Band

Midnight Ink (#151515) background, Bone White text, 64-96px vertical padding. Used sparingly — once per page — to create a printed-poster moment of inversion between the warm cream sections.

### Chat Bubble Card (Dark)

Midnight Ink (#151515) fill, Bone White text, 20px border-radius, 16px padding, small avatar circle on the left. Name + Fragment Mono 14px timestamp above message, message in Instrument Sans 16px weight 400. Functions as a social-proof dramatization device.

### Chat Bubble Card (Light)

Bone White fill, Graphite (#4f4f4f) 1px border, Midnight Ink text, 20px border-radius, 16px padding. Same internal structure as the dark variant but inverts the relationship — sits on Cream Vellum canvas.

### FAQ Accordion Row

Full-width row, Graphite (#4f4f4f) 1px hairline divider, 24px vertical padding, Instrument Sans 18px weight 500 question text in Midnight Ink. Plus icon right-aligned in Vermillion (#dd3508), 20px. No background fill, no card chrome — the divider does the visual work.

### Carousel Arrow Button

Circular button, 40px diameter, Bone White fill, Midnight Ink (#151515) 1px border, Midnight Ink chevron icon centered. Left/right pair sits above content blocks.

### Product Card

Bone White fill, Graphite (#4f4f4f) 1px border, 8px border-radius, 16-24px padding, Instrument Sans 18px weight 500 title in Midnight Ink, body at 14px in Graphite. No shadow, no hover elevation — the border carries the definition.

### Pill Badge

Ochre Tan (#d7cabb) background, Graphite (#4f4f4f) 1px border, 60px border-radius (pill), 4px 12px padding, Instrument Sans 12px weight 500 in Midnight Ink. Used for 'NEW' labels and category tags.

### Sticky Promo Banner

Midnight Ink (#151515) fill, 8px border-radius, Bone White text, Fragment Mono 12px weight 700 for the 'NEW' label in Vermillion, headline at 16px Instrument Sans weight 500, inline thumbnail image on the right with Peach Hairline border.

### Footer

Sits on the Vermillion hero continuation or transitions to Midnight Ink. Bone White text, Instrument Sans 14px, link columns separated by Peach Hairline (#f3b8a9) vertical rules. Logo bottom-left in Bone White uppercase.

## Similar Design Systems

- {'why': 'Same warm editorial palette with cream/beige surfaces and a single bold accent — both are media-workflow tools that favor a printed-catalog feel over a typical SaaS dashboard', 'business': 'Frame.io'}
- {'why': 'Same warm cream canvas with one strong accent color and left-aligned editorial headlines — both use generous spacing and chat/bubble cards as signature visual devices', 'business': 'Pitch'}
- {'why': 'Same warm-toned, editorial-brand aesthetic with flat surfaces, no shadows, and a single chromatic voice — both treat the page as a printed publication', 'business': 'Ceros'}
- {'why': 'Same tight tracking on display headlines, generous section spacing, and confident use of a warm-leaning palette with one strong accent', 'business': 'Stripe'}

## Agent Prompt Guide

**Quick Color Reference**
- text (primary): #151515
- text (muted/border): #4f4f4f
- background (canvas): #e4ddd5
- surface (cards/buttons): #ffffff
- accent border (outlined action, hero surface): #dd3508
- decorative border (printed rules): #f3b8a9
- primary action: #dd3508 (outlined action border)

**Example Component Prompts**
1. **Vermillion Hero Band**: Full-width #dd3508 background, 96px vertical padding. Headline at 48px Instrument Sans weight 500, #ffffff, letter-spacing -0.96px, left-aligned with 1200px max-width container. Body text at 18px weight 400, #ffffff. Top nav: 'BACKLIGHT' logo in 12px Instrument Sans weight 600 uppercase, #ffffff, with 0.24px letter-spacing. Nav links in #ffffff 14px weight 500. Right-aligned white pill button: #ffffff fill, #151515 text, 1px #151515 border, 80px radius, 12px 24px padding.
2. **Cream Canvas Section with Chat Cards**: #e4ddd5 background. Section heading at 32px Instrument Sans weight 500, #151515, letter-spacing -0.64px, left-aligned. Below: a staggered layout of chat bubble cards — alternating between #151515 dark bubbles (20px radius, 16px padding, #ffffff text, Fragment Mono 14px weight 400 at -1.12px letter-spacing for timestamps) and #ffffff light bubbles with 1px #4f4f4f border (same 20px radius and internal structure).
3. **FAQ Accordion List**: #e4ddd5 background. List of questions at 18px Instrument Sans weight 500, #151515, 24px vertical padding, separated by 1px #4f4f4f hairline dividers. Each row has a Vermillion (#dd3508) plus icon right-aligned, 20px size. No background fill on rows — dividers do the work.
4. **Dark Contrast Band**: Full-width #151515 background, 80px vertical padding. Headline at 32px Instrument Sans weight 500, #ffffff. 1200px max-width content container, left-aligned.
5. **Outlined Action Button on Cream Canvas**: Transparent fill, 1px #dd3508 border, 80px border-radius, #151515 text at 14px Instrument Sans weight 500, 12px 24px padding. The chromatic border is the only color the button carries.
