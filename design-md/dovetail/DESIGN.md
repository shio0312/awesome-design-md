# Dovetail — Design System

> **North Star**: blueprint control room at midnight.
> **Theme**: dark
> **Source**: https://dovetailapp.com
> **Refero Style**: https://styles.refero.design/style/6f9452a4-3b64-4c6f-a05e-528d7a586f24
> **Synced**: 2026-09-01

## Overview

Dovetail's design language is a dark command center: near-black canvas, subtle grid wireframes, and cool gray type that recedes so charts and data can lead. A single vivid cornflower blue (#6798ff) acts as the system's only chromatic accent — it appears on the announcement bar, feature icons, and active highlights, never as decorative noise. Typography is Inter at every layer with progressively tighter tracking as sizes grow (from -0.012em at 14px to -0.036em at 64px), giving headlines a compressed, engineered quality rather than a marketing gloss. Components are weightless: 8px radii, hairline borders at #1e1e1 or #313131, zero shadows, and flat surfaces that stack through tone rather than elevation. The overall rhythm is compact, technical, and instrument-like — a tool room, not a pitch deck.

## Color Palette

- **Blue Cornflower**: `#6798ff` — Accent for announcement bar, feature icons, active states, and data highlight strokes [accent]
- **Page Ink**: `#0a0a0a` — Primary page background — the dark canvas that everything sits on [neutral]
- **Card Carbon**: `#1e1e1e` — Card surfaces, button backgrounds, and key borders that delineate panels [neutral]
- **Deep Coal**: `#141414` — Alternate surface level for nested cards and section backgrounds [neutral]
- **Onyx**: `#000000` — Pure black used in SVG illustration fills and contrast anchors [neutral]
- **Steel Border**: `#313131` — Hairline borders on image frames and subtle dividers [neutral]
- **Graphite**: `#454545` — Mid-tone borders on outline buttons and input frames [neutral]
- **Fog**: `#7c7c7c` — Disabled or de-emphasized button text [neutral]
- **Ash**: `#a7a7a7` — Secondary body text, borders on muted elements, icon strokes [neutral]
- **Snow**: `#ffffff` — Primary text, primary filled button background, icon fills, nav links [neutral]

## Typography

- **Inter**
- **JetBrains Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.4 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.33 |
| heading | 40 | — | 1.2 |
| heading-lg | 56 | — | 1.14 |
| display | 64 | — | 1.13 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24-32px
- **Element Gap**: 8-16px
- **Section Gap**: 64-96px
- **Border Radius**: {'tags': '4px', 'cards': '8px', 'inputs': '8px', 'buttons': '8px'}

## Layout

Pages are max-width 1200px centered with generous side padding. The hero uses an asymmetric 50/50 split: left column carries headline, subtext, and dual CTAs; right column holds a product preview card. Section rhythm is uniform — dark background continues throughout with no alternating bands, separated only by vertical spacing. Stat highlights and feature grids use 3-column or 4-column card rows at equal widths. Navigation is a single top bar with logo, product/use-cases/resources/enterprise/customers/pricing links center-left, and Log in + Contact sales right-aligned. No sidebar, no mega-menu. Footer is a 4-column link grid plus a single illustration card on the right. The overall density is compact and consistent — every section breathes the same amount.

## Surfaces / Elevation

- **Canvas**
- **Section**
- **Card**
- **Raised Edge**

## Imagery

Imagery is minimal and functional: greyscale customer logos in a single trust strip, one or two product-screenshot cards showing real dashboard UI (charts, tables, data bars), and sparse flat illustrations in the footer (a pixel smiley face on a #6798ff tile). No lifestyle photography, no hero video, no decorative 3D. The grid wireframe pattern overlaid on the dark background is the only repeated visual motif — it signals "blueprint" and gives the dark surface structure. Icons are small, single-color (white or #6798ff), 16-20px, stroke-based with a 1.5-2px weight, and sit inline with text rather than floating as decoration.

## Design Principles

### Do

- Use 8px radius for all buttons, cards, and inputs — the only deviation is 4px for small tags and inline chips.
- Set page background to #0a0a0a and reserve #1e1e1 exclusively for card and button surfaces so the surface hierarchy reads through tone alone.
- Use #6798ff only for functional accents: announcement bars, feature icons, active nav states, and data highlight strokes — never as a background fill for content blocks.
- Set display headlines at 56-64px Inter 600 with tracking between -2.0 and -2.3px so they feel engineered, not editorial.
- Reserve JetBrains Mono for eyebrows, BETA tags, and small data labels with positive 0.85-1.0px tracking — never use it for body or headings.
- Keep section gaps between 64-96px and element gaps between 8-16px to maintain the compact, technical density.
- Default to white filled buttons for primary actions and dark outlined (1px #454545) for secondary — never use the blue accent on a button background.

### Don't

- Do not introduce a second chromatic color — the system is monochrome with a single blue accent.
- Do not use shadows or elevation to separate surfaces — rely on tone shifts between #0a0a0a, #141414, and #1e1e1e.
- Do not use gradients on any surface, button, or background.
- Do not use #6798ff as a filled button background — it belongs only on icons, the announcement bar, and small accent strokes.
- Do not use 66px or pill radii on cards or buttons — the 8px corner is the system signature.
- Do not set body text below 14px or use weights lighter than 400 — the type stack is deliberately compact, not delicate.
- Do not use pure #000000 as a page background — it is reserved for SVG illustration fills; pages live on #0a0a0a or #141414.

## Components

### White Filled Button (Primary)

White background (#ffffff), near-black text (#0a0a0a), 8px radius, 16px horizontal / 10px vertical padding. Inter 500 at 14px. Used for "Contact sales" and "Try Dovetail free" in high-priority positions. No border, no shadow.

### Dark Outlined Button (Secondary)

Transparent or #0a0a0a background, 1px border at #454545, white text (#ffffff), 8px radius, 16px / 10px padding. Inter 500 at 14px. The lower-emphasis counterpart to the white filled button.

### Ghost Nav Button

No background, no border, white text at 14px Inter 500. Sits inline with nav items. Padding matches nav height rhythm.

### Stat Card

#1e1e1 background, 1px border at #1e1e1 (or transparent — separation comes from surface tone), 8px radius, 24px padding. A small #6798ff icon sits above a 40px Inter 600 metric value in white, followed by a 14px label in #a7a7a7. No shadow, no hover lift.

### Section Eyebrow Label

JetBrains Mono 400 at 12px, white or #a7a7a7 text, letter-spacing 0.85px. No background, sits directly above headline with 16-24px gap.

### Product Preview Card

#1e1e1 surface with 8px radius, contains a real product UI rendering with charts, tables, and colored data bars. Acts as a flat, borderless visual element — no shadow or frame chrome.

### BETA Tag

Inline text tag, no background, #a7a7a7 text at 12px Inter 400, with "BETA" uppercase in JetBrains Mono 400 at 12px. Sits beside the feature name with 8px gap.

### Logo Strip Item

Greyscale SVG, roughly 80px wide, 8-16px gap between items. Logos sit on transparent background at ~60% opacity to stay subordinate to the page.

### Footer Link Column

Column header in 12px Inter 500 uppercase at #a7a7a7 (letter-spacing ~0.5px). Links below in 14px Inter 400 white, 8-12px vertical gap between links. No bullet markers.

### Social Icon Button

24px square, white stroke or fill, no background, no border, no hover chrome — flat icon-on-dark.

### Announcement Bar

Full-width #6798ff blue background, white text at 14px Inter 500, centered content with a small dismiss icon on the right. 8px vertical padding.

### Rating Badge

5 white stars at 12-14px, followed by "4.5/5 · 62" or similar in 12px Inter 400 #a7a7a7. Inline horizontal layout with 16px gap.

## Similar Design Systems

- {'why': 'Same dark canvas, single vivid blue accent, Inter typeface, 8px radii, and zero-shadow flat surfaces with tone-based hierarchy.', 'business': 'Linear'}
- {'why': 'Dark-first instrument-panel aesthetic with tight Inter tracking on display sizes, monochrome palette, and minimal blue functional accents.', 'business': 'Vercel'}
- {'why': 'Compact dark UI with a single cool accent color, compact density, and a product-preview-led hero layout.', 'business': 'Cursor'}
- {'why': 'Developer-tool dark theme with neutral primary buttons, hairline borders, and product UI inlined directly into marketing sections.', 'business': 'Retool'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff (primary), #a7a7a7 (secondary), #7c7c7c (disabled)
- background: #0a0a0a (page), #1e1e1e (card/button)
- border: #1e1e1e (subtle), #454545 (outlined button), #313131 (image frame)
- accent: #6798ff (icons, announcement bar, active states)
- primary action: #1e1e1e (filled action)

**Example Component Prompts**
1. Create a Primary Action Button: #1e1e1e background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
2. Build a 3-column stat row: each cell is a #1e1e1e card with 8px radius and 24px padding. Inside, a #6798ff icon (16px, stroke) sits above a 40px Inter 600 white metric value, followed by a 14px Inter 400 #a7a7a7 label.
3. Build a top navigation bar: #0a0a0a background, logo on the left, nav links in 14px Inter 500 #ffffff, spaced 24px apart, centered. On the right, a ghost "Log in" text link and a white filled "Contact sales" button (8px radius, 16px/10px padding). Height 64px.
4. Build a section with a JetBrains Mono eyebrow: 12px uppercase label in #a7a7a7 with 0.85px letter-spacing, 24px gap below to a 40px Inter 600 #ffffff headline with -0.84px tracking.
5. Build a footer link column: 12px Inter 500 uppercase #a7a7a7 header with 0.5px tracking, followed by 14px Inter 400 white links stacked at 12px vertical gap. No bullets, no separators.

## Grid Wireframe Motif

A subtle 1px grid pattern at #1e1e1e sits behind the dark canvas across hero and feature sections. The grid is square (roughly 40-60px cells), very low contrast, and never carries content — it exists to give the otherwise flat dark surface a sense of structure and engineering intent. When recreating this system, overlay a 1px #1e1e1e linear-gradient or repeating-linear-gradient grid on the page background; do not attempt to recreate it with borders on individual elements.
