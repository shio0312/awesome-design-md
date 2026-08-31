# Miranda — Design System

> **North Star**: Old-world broadsheet on warm cream — newspaper editorial for the digital age.
> **Theme**: light
> **Source**: https://www.niccolomiranda.com
> **Refero Style**: https://styles.refero.design/style/3f6e3076-e77f-487e-b212-3b5946a34e87
> **Synced**: 2026-09-01

## Overview

A vintage broadsheet portfolio rendered on warm parchment stock. Near-black ink dominates text, borders, and large editorial banners; the cream canvas stays quiet and matte, never clinical. Display type is the brand: enormous custom serifs (Canopee, Germgoth) with negative tracking and sub-1.0 line-heights so letters collide and bleed into one another, mimicking woodblock print and 19th-century poster lettering. One warm ember-orange accent appears sparingly — a stamp, a star icon — like a hand-stamped seal. Components stay flat and borderless; depth comes from contrast, not shadow. Layout reads like a zine or newspaper spread: oversized headline banners intercut with tight three-column project grids and full-bleed illustrations.

## Color Palette

- **Parchment**: `#e2dedb` — Page background, image matte areas — the warm stock everything else is printed on [neutral]
- **Bone Cream**: `#cdc6be` — Card surfaces, secondary panels, subtle inset backgrounds slightly darker than parchment [neutral]
- **Ink Black**: `#1d1d1b` — Body text, nav links, borders, large display banner fills, icon strokes — the near-black that carries every contrast-critical role [neutral]
- **Charcoal**: `#69645f` — Muted secondary text, subdued borders, quiet typographic accents [neutral]
- **Pure Black**: `#000000` — Card outline emphasis, deepest fills, highest-contrast border work on cream surfaces [neutral]
- **Ember Orange**: `#c03f13` — Stamp illustrations, star icon accent, occasional seal/sticker color — the single chromatic punctuation in an otherwise monochrome system [accent]

## Typography

- **Editorial New**
- **Canopee**
- **Domaine Display**
- **Germgoth**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.18 |
| body-sm | 16 | — | 1.27 |
| subheading | 22 | — | 1.18 |
| heading-sm | 32 | — | 1.11 |
| heading | 65 | — | 0.91 |
| heading-lg | 122 | — | 0.79 |
| display | 446 | — | 0.73 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 24px
- **Element Gap**: 14px
- **Section Gap**: 43px
- **Border Radius**: {'tags': '2.88px', 'cards': '11.52px', 'images': '0px', 'buttons': '2.88px'}

## Layout

Full-bleed page with max-width ~1440px centered. The top opens with a thin header bar, then a three-column 'featured work' strip (image, type, image). A full-width Ink Black display banner (MIRANDA) crashes through the middle, acting as a typographic section break. Below: alternating two-column and three-column blocks of project cards and portrait illustrations, each separated by generous 43px vertical rhythm. Another full-width banner (WEBSITE) punctuates the lower half. The footer is a simple two-column text block. Navigation is minimal — a single hamburger icon top-right, no persistent nav bar. The grid is consistent: always 3 equal columns at the top tier, breaking into 2 or 1 for illustrative sections. Vertical spacing is comfortable but not airy; the density feels curated, not sparse.

## Surfaces / Elevation

- **Parchment**
- **Bone Cream**
- **Ink Black**
- **Pure Black**

**Shadow tokens:**

## Imagery

Digital illustration dominates over photography. Portrait subjects are stylized semi-realistic digital paintings with dramatic lighting (rim-lit faces, saturated backgrounds, painterly texture). Project thumbnails lean toward moody interior photography (warm wood, cool blue retail spaces). Illustrations are tightly cropped, often filling the full card width, with no border or padding buffer. One Ember Orange graphic accent (stamp sunburst) appears as a decorative seal. The overall treatment feels like a curated magazine spread — every image is art-directed, never stock.

## Design Principles

### Do

- Use Canopee at 200px+ for any section-divider banner — display sizes below 122px lose the system's defining character
- Set line-height below 0.85 on all Canopee display text so letters crowd and nearly collide; this is the signature, not a bug
- Pair every project card with a 2.88px-radius square NEW badge in Ember Orange (#c03f13) — the badge is the only chromatic note in a monochrome page
- Use Editorial New weight 300 exclusively for body, nav, and small headings — heavier weights break the editorial restraint
- Let images bleed to the card edge with 0px radius; sharp corners are part of the broadsheet language
- Keep the page background Parchment (#e2dedb) and card surfaces Bone Cream (#cdc6be) — never introduce a white or cool gray
- Use negative letter-spacing on all Canopee and Domaine Display headings; positive tracking destroys the printed-poster feel

### Don't

- Do not introduce gradients, glassmorphism, or modern blur effects — this is a 1890s broadsheet, not 2024 SaaS
- Do not use border-radius above 12px on any element — sharp geometry defines the print aesthetic
- Do not add more than one chromatic accent — the Ember Orange only works because the rest is monochrome
- Do not center-align body text longer than two lines; flush-left only for paragraphs
- Do not use shadows for general depth; reserve the directional ink-color shadow for project cards only
- Do not substitute system sans-serifs (Inter, Helvetica) for any of the four custom faces — the serif/gothic mix is load-bearing
- Do not use line-height above 1.0 on display headings — open spacing kills the compressed woodblock feel

## Components

### Editorial Header Bar

Full-width Parchment (#e2dedb) bar with location label left ('Amsterdam, NL'), centered brand name in Editorial New 19-20px weight 300, and hamburger icon right. 1px Ink Black border-bottom for hairline separation.

### Project Grid Card

3-column grid card. Thumbnail image with 0px radius fills top. Below: project title in Editorial New 20px weight 300, a 2.88px-radius square NEW badge in Ember Orange (#c03f13) with white text, and a 2-3 line description in Editorial New 16-17px. No card border; separation comes from whitespace alone.

### Display Banner Block

Full-width Ink Black (#1d1d1b) rectangle spanning the page with oversize Canopee text in Parchment (#e2dedb). Text sizes 202-533px, line-height 0.71-0.79 so letters nearly touch. Negative letter-spacing up to -0.089em. This is the system's most recognizable pattern.

### NEW Badge

Small square 2.88px-radius tag, Ember Orange (#c03f13) background, Editorial New 12-14px weight 300 white text. Sits inline with project title.

### Portrait Illustration Card

Full-bleed digital illustration with tight cropping. No border, no radius. Caption sits below in Canopee or Domaine Display at 43-86px, line-height 0.91-0.79, weight 400-500. The illustration does the heavy lifting; type acts as a placard.

### Drop Cap Bio Block

Two-column intro: left column opens with a large Canopee drop cap (the brand's first letter) at 86px+, then Editorial New body text. Right column holds a larger Canopee headline ('CREATIVE DEVELOPER BASED IN AMSTERDAM, NL.') at 65-72px. The drop cap is the only typographic flourish in body text.

### Stamp Seal Illustration

Perforated-edge postage-stamp rectangle at 11.52px radius, off-white interior with Ember Orange sunburst graphic, handwritten signature line, and two metadata rows ('NAME', 'BIRTH') in tiny Editorial New caps. Functions as a signature mark, not a functional UI element.

### Three-Column Section Header

Left card: image. Center card: massive Canopee heading ('ALL WORK!') in 65-86px with short Editorial New subhead. Right card: image. Visual rhythm of image-type-image. Center column centered.

### Text Link with Underline

Editorial New 16-19px weight 300, Ink Black (#1d1d1b) color, 1px underline offset 3px. Hover darkens to Pure Black. No background fill, no button shape — editorial hyperlinks stay as text.

### Project Metadata Row

Single-line row of Editorial New 14-16px caption text in Charcoal (#69645f) below project description, listing role/agency/year. Acts as a byline.

## Similar Design Systems

- {'why': 'Same broadsheet editorial typography with extreme display sizes and tight letter-spacing on a cream/warm background', 'business': 'Locomotive (locomotive.ca)'}
- {'why': 'Newspaper-grid layouts, oversize serif headlines bleeding off cards, monochrome with single chromatic stamp accent', 'business': 'Pentagram portfolio pages'}
- {'why': 'Custom display faces, sharp-cornered image cards, generous whitespace on warm neutral canvas', 'business': 'Rauno Freiberg (raunofreiberg.com)'}
- {'why': 'Playful experimental portfolio that uses oversize custom type as architectural elements rather than body copy', 'business': 'Resn (resn.co.nz)'}
- {'why': 'Editorial portfolio tradition — broadsheet-inspired, serif-driven, monochrome with intentional restraint', 'business': 'Frank Chimero'}

## Agent Prompt Guide

**Quick Color Reference**
- background: #e2dedb (Parchment)
- surface/card: #cdc6be (Bone Cream)
- text: #1d1d1b (Ink Black)
- border: #1d1d1b or #000000
- accent: #c03f13 (Ember Orange)
- primary action: #1d1d1b (filled action)

**Example Component Prompts**

1. *Full-width display banner*: Ink Black (#1d1d1b) rectangle spanning 1440px, height auto. Inside, the word 'MIRANDA' in Canopee 446px, weight 400, color #e2dedb, line-height 0.73, letter-spacing -22.3px. Letters should nearly touch.

2. *Project card*: Bone Cream (#cdc6be) surface, no visible border, 24px internal padding. Top: full-width image at 0px radius. Below: 'AVRO&KO' in Editorial New 20px weight 300 color #1d1d1b, followed by a 2.88px-radius square badge (background #c03f13, text 'NEW' in Editorial New 12px weight 300 color #e2dedb). Description in Editorial New 16px weight 300 color #1d1d1b, line-height 1.27.

3. *Portrait illustration block*: Two-column layout. Left: a vertical digital painting illustration filling the column, 0px radius. Right: 'DIGITAL ART DIRECTOR / INTERACTIVE DESIGNER' in Canopee 86px weight 400, color #1d1d1b, line-height 0.91, letter-spacing -2.08px.

4. *Editorial header bar*: Parchment (#e2dedb) background, 1px Ink Black (#1d1d1b) bottom border. Left: 'Amsterdam, NL' in Editorial New 19px weight 300. Center: 'The Niccolò Portfolio' in Editorial New 19px weight 300. Right: hamburger icon (3 horizontal Ink Black lines).

5. *Stamp seal accent*: 11.52px-radius perforated-edge rectangle, background #e2dedb, with an Ember Orange (#c03f13) sunburst icon, a signature line, and two tiny text rows ('NAME Niccolò Miranda' / 'BIRTH 18/10/1995') in Editorial New 11px.
