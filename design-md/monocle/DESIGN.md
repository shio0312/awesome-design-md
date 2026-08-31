# Monocle — Design System

> **North Star**: Quality broadsheet on cream paper. A curated newsroom where every column earns its keep and the only color on the page is the one that matters.
> **Theme**: light
> **Source**: https://monocle.com
> **Refero Style**: https://styles.refero.design/style/9165ecb1-f068-4093-8783-1f3c98898b8a
> **Synced**: 2026-09-01

## Overview

Monocle reads like a quality broadsheet translated to the web: a warm cream canvas, generous serif typography in Plantin, and a tightly-edited grid that borrows from print pagination rather than app conventions. The entire interface is monochrome — black text, warm whites, and one unmistakable signal yellow (#ffc500) that functions as the magazine's only accent, reserved for the subscribe action, the radio card, and editorial illustration. Layout leans editorial: section labels run as tracked uppercase sans-serif eyebrows, headlines set in Plantin with negative tracking, and body copy in the same serif at a measured 16–18px. Components feel archival — thin rules, minimal radii, no drop shadows, and a 3-column grid that mixes large feature photography, opinion cards, and a persistent sidebar of audio/promo blocks. Density is high but never cluttered because spacing is compact and structural, not decorative.

## Color Palette

- **Signal Yellow**: `#ffc500` — Yellow supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Folio Black**: `#000000` — Primary text, headlines, nav items, icons, and 1px hairline rules — the ink of the page [neutral]
- **Newsprint Cream**: `#fdfcf3` — Page canvas — the warm off-white that keeps the interface from feeling clinical and signals print provenance [neutral]
- **Broadsheet White**: `#ffffff` — Card surfaces, feature panels, and inverted text on dark or yellow blocks [neutral]
- **Margin White**: `#fdfbe4` — Subtle secondary surface — a slightly warmer yellow-tinted off-white used for featured/elevated blocks like the radio card [neutral]
- **Pull Quote Gray**: `#e7e7e7` — Card backgrounds and muted panel fills where content needs to recede from the page cream [neutral]
- **Rule Gray**: `#d9d9d9` — Borders, dividers between columns and sections, input outlines — the structural skeleton of the layout [neutral]
- **Caption Gray**: `#6e6e6e` — Secondary text, metadata, read-time labels, byline captions, and muted UI labels [neutral]
- **Mute Gray**: `#b3b3b3` — Tertiary text, disabled UI states, and low-emphasis nav accents [neutral]
- **Charcoal**: `#211d1c` — Near-black warm border for buttons and decorative outlines where pure black feels too cold [neutral]
- **Desk Blue**: `#64d5ff` — Decorative illustration accent — appears inside editorial artwork, not in interface controls [accent]

## Typography

- **Plantin**
- **Helvetica Neue**
- **Chanel**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.2 |
| body | 16 | — | 1.38 |
| subheading | 18 | — | 1.3 |
| heading-sm | 20 | — | 1.25 |
| heading | 24 | — | 1.2 |
| heading-lg | 28 | — | 1.2 |
| heading-xl | 32 | — | 1.15 |
| display | 40 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 80px
- **Border Radius**: {'nav': '0px', 'tags': '0px', 'cards': '8px', 'buttons': '0px'}

## Layout

Max-width ~1200px centered container on a warm cream (#fdfcf3) canvas. The page model is broadsheet: a masthead with the MONOCLE wordmark, a primary nav row of categories separated by pipes, then a 3-column editorial grid (large lead article on the left, secondary article stack in the middle, persistent Monocle Radio sidebar on the right). Below the fold, a full-width 4-column hero feature row of large photo tiles, followed by further article grids. Sections are separated by 1px #d9d9d9 rules rather than alternating background colors. The sticky utility bar at the very top contains MAGAZINE / RADIO / SHOP links on the left and SUBSCRIBE + cart on the right. Navigation is minimal and typographic — no drop-downs, no mega-menus, just pipe-separated category links.

## Surfaces / Elevation

- **Newsprint Cream**
- **Broadsheet White**
- **Margin White**
- **Pull Quote Gray**

## Imagery

Photography is editorial and documentarian — tight portrait crops of political figures, architectural exteriors of cities, and product still-lifes. Images are large, full-bleed within their grid cells, and treated without color grading or overlays. Editorial illustrations are flat, geometric, and limited to the brand palette: black line work with #ffc500 yellow fills and occasional #64d5ff blue accents. Illustrations often feature a single character or scene with minimal background. The overall image density is high — this is a publication, not a product page — and imagery carries equal weight to text in the layout.

## Design Principles

### Do

- Use Plantin for all editorial content — headlines, body, eyebrows, bylines. Never substitute a different serif.
- Set headlines at 24–40px in Plantin weight 400 with letter-spacing -0.0200em. The negative tracking is the signature.
- Use uppercase tracked Plantin 13px (0.05–0.075em letter-spacing) for section eyebrows (POLITICS, OPINION, AFFAIRS) — this is how the page signals taxonomy.
- Use #ffc500 exclusively for the Subscribe button, the Monocle Radio card, and editorial illustration fills. No other interface element should carry color.
- Separate cards and columns with 1px #d9d9d9 hairline rules, not spacing alone. The grid is a print grid.
- Keep all borders 0 radius. 8px radius only on photograph containers within the hero feature row.
- Maintain a 3-column editorial grid (lead | secondary | sidebar radio) on desktop, collapsing to single column on mobile.

### Don't

- Don't use drop shadows on any component. Elevation is tonal, not projected.
- Don't introduce additional accent colors. The system is monochrome plus one yellow.
- Don't set body copy in a sans-serif. Plantin carries the voice; Helvetica Neue is for chrome only.
- Don't use border-radius larger than 8px. The 0-radius aesthetic is non-negotiable for editorial cards and buttons.
- Don't use centered text for article headlines — they should always left-align, broadsheet style.
- Don't place the SUBSCRIBE button anywhere except the top utility bar. Yellow outside the header breaks the signal.
- Don't use icons with fills other than #000000 or #ffc500. The icon language is binary.

## Components

### Wordmark Header

Center-aligned MONOCLE wordmark in Plantin 700 at ~40px with -0.0200em letter-spacing. Flanked left by a small editorial flag (a thumbnail cover image with two lines of small caption text beneath) and right by a line-drawing mascot illustration with a short tagline. The header sits on #fdfcf3 with no border — it reads as a masthead, not a navigation bar.

### Primary Section Nav

Horizontal row of categories (AFFAIRS | BUSINESS | CULTURE | DESIGN | FASHION | TRAVEL | CITY GUIDES) in Plantin 13px weight 400, uppercase, letter-spacing 0.0750em. Items separated by a thin vertical pipe character. Color #000000 on #fdfcf3. 0 radius, no underline, no background — pure typographic structure with 1px hairline above and below.

### Utility Bar

Sticky top bar with hamburger + MAGAZINE / RADIO / SHOP links on the left, search icon + LOG IN + SUBSCRIBE button + cart + language toggle on the right. Background #ffffff with a 1px bottom border in #d9d9d9. Links in Helvetica Neue 13px weight 700.

### Subscribe Button

Filled rectangle, #ffc500 background, #000000 text in Helvetica Neue 13px weight 700, uppercase, letter-spacing 0.0100em. 0 border-radius (the only yellow + black combo on the page). 8px vertical padding, 16px horizontal padding. No drop shadow. The sole yellow element in the chrome.

### Lead Article Card

Eyebrow label in Plantin 13px uppercase tracked (e.g. POLITICS), color #000000. Headline in Plantin 24–28px weight 400, negative letter-spacing -0.56px, color #000000, line-height 1.20. Deck/subhead in Plantin 16px weight 400, color #6e6e6e. Book icon + read-time label in Plantin 13px, color #b3b3b3. Full-bleed photograph below text. No border, no background fill — sits directly on #fdfcf3.

### Sidebar Article Card

Square or landscape photo at top. Small uppercase eyebrow in Plantin 13px tracked. Headline in Plantin 20px weight 400. Book icon + read-time at bottom. 0 border, 0 background, 8px gap between elements. Photographs often carry editorial illustration overlays.

### Opinion Card

Centered circular portrait illustration or photo on #e7e7e7 or #fdfbe4 circle. Author name in Plantin 16px weight 700 below the portrait. Headline in Plantin 20px weight 400. Read-time at bottom in #b3b3b3. Vertical divider (1px #d9d9d9) separates it from adjacent cards.

### Monocle Radio Card

Tall card filling the right rail. Header strip #000000 background with 'MONOCLE RADIO' in white Plantin 13px uppercase tracked. Content area on #fdfbe4 warm off-white. Contains a black 'LISTEN LIVE' button with play icon, and a list of scheduled shows. 0 border-radius. This is the only persistent block that uses the warm secondary surface.

### Sponsored Module

White card with 'SPONSORED BY' label in Plantin 13px tracked #6e6e6, followed by sponsor logo. 8px padding, 1px #d9d9d9 border. Visually quieter than editorial cards.

### Hero Feature Banner

4-column grid of large article tiles with full-bleed photography, dark overlay-free. Each tile: photo on top, category eyebrow + headline + read-time below. 0 radius. 16px gap between tiles. Background #fdfcf3.

### Editorial Illustration Block

Flat geometric illustration in the brand palette (#ffc500 yellow, #000000 line work, #64d5ff blue accents). Often features a character or scene. Sits inside article cards with 0 radius and no frame. Illustrations carry the brand's only multicolor moments — the rest of the page is monochrome.

### Audio Indicator Icon

Circular #ffc500 icon with a black speaker/sound glyph, 24px diameter, overlaid on article photos to mark audio content. One of the few places yellow appears outside the subscribe button and radio card.

### Section Divider

1px solid #d9d9d9 line, full container width, no label. Separates the lead grid from the hero feature row and subsequent sections.

## Similar Design Systems

- {'why': 'Same broadsheet editorial grid with serif headlines, pipe-separated section nav, and monochrome palette with a single accent color for CTAs.', 'business': 'The New York Times'}
- {'why': 'Similar editorial restraint — serif body type, tight column grid, section eyebrows as tracked uppercase, and a warm off-white canvas.', 'business': 'The Economist'}
- {'why': 'Shared information density, sans-serif utility chrome paired with serif editorial content, and custom editorial illustration style in a limited brand palette.', 'business': 'Bloomberg Businessweek'}
- {'why': 'Same print-publication aesthetic on the web — cream backgrounds, generous serif type, and minimal use of color reserved for brand identity moments.', 'business': 'Cereal magazine'}
- {'why': 'Editorial media grid with 3-column lead/secondary/sidebar structure and tracked uppercase category labels.', 'business': "It's Nice That"}

## Agent Prompt Guide

**Quick Color Reference**
- text: #000000
- background (canvas): #fdfcf3
- background (card/surface): #ffffff
- background (elevated/featured): #fdfbe4
- border/rule: #d9d9d9
- secondary text: #6e6e6e
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. *Lead Article Card*: On #fdfcf3 canvas. Eyebrow label 'POLITICS' in Plantin 13px weight 700, uppercase, letter-spacing 0.075em, #000000. Headline in Plantin 28px weight 400, #000000, letter-spacing -0.56px, line-height 1.20. Deck in Plantin 16px weight 400, #6e6e6e. Read-time label in Plantin 13px, #b3b3b3, with a small book icon. Full-bleed photo below. 0 border-radius, no shadow.

2. *Subscribe Button*: Filled rectangle, background #ffc500, text 'SUBSCRIBE' in Helvetica Neue 13px weight 700, uppercase, #000000, letter-spacing 0.01em. Padding 8px 16px. 0 border-radius. No shadow. Sits in the top utility bar.

3. *Monocle Radio Sidebar Card*: Width ~280px. Top strip: #000000 background with 'MONOCLE RADIO' in Plantin 13px uppercase tracked #ffffff. Body: #fdfbe4 background. Contains a 'LISTEN LIVE' button (#000000 background, #ffc500 play icon, #ffffff text in Helvetica Neue 13px weight 700) and a list of scheduled shows. 0 border-radius, 1px #d9d9d9 left border.

4. *Editorial Illustration Block*: Flat geometric illustration, 200×200px, 0 border-radius. Black (#000000) line work with #ffc500 yellow fills for key shapes and occasional #64d5ff blue accents. Character or scene composition, no background fill (transparent over the cream canvas).

5. *Sidebar Article Tile*: On #fdfcf3. Square photo at top (no border-radius). Below: uppercase eyebrow in Plantin 13px tracked, headline in Plantin 20px weight 400 #000000 letter-spacing -0.4px, book icon + read-time in Plantin 13px #b3b3b3. 16px gap between elements. Separated from adjacent tiles by 1px #d9d9d9 vertical rule.

## Signature Choices

Four choices make Monocle instantly recognizable and must be preserved by any new design:

1. **One color, one button.** The entire chromatic vocabulary is a single yellow (#ffc500) reserved for the Subscribe action and the Radio card. This scarcity makes it impossible to miss.

2. **Plantin does everything editorial.** The custom serif handles 40px display wordmark down to 13px tracked eyebrows. Negative letter-spacing at display sizes and positive at small caps creates typographic contrast without mixing typefaces.

3. **Cream canvas, not white.** The #fdfcf3 page background is the print provenance signal. Pure #ffffff would make this look like any other SaaS site.

4. **Zero shadows, all hairlines.** Depth comes from surface color shifts and 1px rules. Any shadowed card would feel foreign to the system.
