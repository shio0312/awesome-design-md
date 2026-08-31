# Structured — Design System

> **North Star**: Renaissance gallery on putty paper
> **Theme**: mixed
> **Source**: https://structured.money
> **Refero Style**: https://styles.refero.design/style/6c0b77d3-71f9-469d-98aa-4ce1d6d76ac8
> **Synced**: 2026-09-01

## Overview

Structured treats finance as a gallery exhibition: a warm putty-beige canvas, stark black accents, and classical oil-painting imagery that reframes Bitcoin yield as high art. Typography is the protagonist — a custom serif at display sizes up to 374px carries the brand voice with dramatic negative tracking, while a neutral grotesk handles utility. Sections alternate between light editorial spreads and pitch-black rooms, with no gradients, no shadows, and almost no color. Every surface is flat, every border is hairline, and the only accent is the warm cream/black contrast that runs through everything. The aesthetic borrows from museum wall labels and Renaissance folios: restrained, authoritative, slightly precious.

## Color Palette

- **Putty**: `#c4c3b6` — Dominant page canvas — the warm gray-beige that fills hero and most light sections. The single most-used color in the system; sets the gallery-wall tone [neutral]
- **Ink**: `#000000` — Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color [neutral]
- **Bone**: `#e7e5e4` — Elevated card surfaces and secondary canvas in light sections. Sits one step above Putty for subtle layering without breaking the monochrome warmth [neutral]
- **Chalk**: `#ebebeb` — Footers and lightest surface tier. The coolest neutral — used sparingly at section bases to signal a different page zone [neutral]
- **Vellum**: `#dfdcd5` — Hairline borders on body and icon elements. A mid-tone warm gray that reads as a printed page edge, not a UI divider [neutral]
- **Graphite**: `#595855` — Muted secondary text fills and subtle image backgrounds. The darkest warm gray — used where pure black would be too severe [neutral]
- **Ash**: `#808080` — Image placeholder backgrounds and mid-neutral surfaces. The only truly cool gray in the system, reserved for image containers [neutral]
- **Paper**: `#ffffff` — Text on dark sections, white icon strokes, and the rare pure-white element. Used only as reverse type or accent fill, never as a large surface [neutral]

## Typography

- **Davinci**
- **Helvetica Now**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| body-sm | 15 | — | 1.5 |
| subheading | 22 | — | 1.33 |
| heading-sm | 26 | — | 1.33 |
| heading | 43 | — | 1.1 |
| heading-lg | 52 | — | 1 |
| display | 374 | — | 0.84 |

## Spacing & Layout

- **Card Padding**: 24px
- **Element Gap**: 6px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '9px', 'links': '2px', 'buttons': '28.8px'}

## Layout

Full-bleed sections with no max-width content container — the page breathes edge-to-edge. Hero is a light putty canvas with a tiny centered type cluster (sub-headline, stats, button) floating above a monumental 374px serif wordmark that anchors the lower half. Middle section: full-bleed classical painting with a single dark product card floating dead-center. Feature section: full-width black canvas with centered serif heading, then a 3-column grid of circular image vignettes with hexagonal nav dots below. Navigation is minimal — logo mark top-left, single text link top-right, no visible menu bar. Section rhythm alternates light/dark/light with generous vertical breathing room between blocks.

## Surfaces / Elevation

- **Putty Canvas**
- **Bone Card**
- **Chalk Footer**
- **Ink Room**

## Imagery

Classical oil paintings — Renaissance and Baroque landscapes with mountains, architecture, clouds, and still-life studies (rabbit, amphora, butterfly). Treatment is full-bleed canvas-like reproductions and circular crops with no rounded corners or framing on the full images. The paintings carry the entire decorative load: no abstract graphics, no product screenshots, no photography. Dense visual presence on the middle section, near-absent on the hero and dark feature section. The imagery is editorial and atmospheric — it sets mood rather than explaining product.

## Design Principles

### Do

- Use Davinci serif at 52px+ for all section headings and 94px+ for primary display titles — the serif is the brand voice
- Set the hero wordmark to exactly 374px in Davinci weight 500 with -3.37px letter-spacing so it crops at the viewport edges
- Alternate between Putty (#c4c3b6) light sections and Ink (#000000) dark sections — no gradients between them, just hard cuts
- Use the 28.8px pill radius for all filled action buttons and keep padding to 9px 17px for a compact capsule
- Apply circular crops to all feature imagery — the circle is the system's primary image shape after the full-bleed rectangle
- Set all body and utility text in Helvetica Now at 9–16px; the grotesk never exceeds 43px
- Use hexagonal shapes for pagination and decorative indicators — a secondary geometry that complements the circular vignettes and pill buttons

### Don't

- Don't introduce any saturated color — the palette is warm grays and black; adding a blue, green, or red CTA would break the gallery aesthetic
- Don't use shadows or gradients — the system is entirely flat; depth comes from alternating light/dark sections, not elevation
- Don't set body text in the serif — Davinci is display-only; using it below 34px breaks the editorial hierarchy
- Don't use standard border-radius values (4px, 8px, 12px) on cards — the system uses 9px for cards and 28.8px for buttons; anything in between is off-system
- Don't use stock photography or modern digital illustrations — all imagery should be classical oil paintings or nothing
- Don't add a visible menu bar or navigation chrome — the header is just a logo mark and a single text link
- Don't set body type below 12px or above 26px in Helvetica Now — the grotesk's range is narrow and intentional

## Components

### Pill Action Button

Background #000000, text #ffffff, font Helvetica Now 12px weight 400, padding 9px 17px, border-radius 28.8px (near-full pill), no border, no shadow. Tight horizontal padding creates a compact capsule. Single accent button per viewport.

### Ghost Text Link

Text only, no background, color #000000, font Helvetica Now 12–16px weight 400, underline on hover only. Sits in the top-right header and inline in body copy. No border or background in default state.

### Circular Feature Vignette

Circular crop of a classical painting (no border, no shadow), diameter ~200px. Davinci serif caption (22–24px) above, hexagonal nav indicator below. Spaced in a 3-column grid on dark background.

### Notched Product Card

Dark card (~400px square) with notched/hexagonal corner cuts (not standard border-radius — corner geometry), #000000 background, #ffffff micro-label ('SCROLL' at 9px Helvetica Now) in the lower-left. Floats centered over imagery. 9px radius on the primary edges before the notches.

### Hero Wordmark

Davinci serif at 374px weight 500, color #000000, letter-spacing -3.37px, line-height 0.84. Extends beyond the visible viewport width — intentionally cropped at the edges. This is the signature component; the brand IS this wordmark at this scale.

### Stat Pair

Two values side by side, Helvetica Now 16px weight 500, separated by spacing. Label-value pairs in uppercase tracking, e.g. 'TVL: 85 BTC'. Color #000000 on light sections.

### Hexagonal Nav Indicator

Small hexagonal outline shapes (~12px), stroke #000000 on light sections or #ffffff on dark sections, fill transparent. Used in groups of 3 below circular features. The hexagon is a secondary brand shape — distinct from the pill button and circular image crops.

### Logo Mark

A circled 'S' monogram, ~32px diameter, thin black stroke on transparent or light fill. Minimal, monoline, no decoration. The only graphic mark on the page.

### Section Header

Davinci serif 94px weight 500, color #000000 on light or #ffffff on dark, letter-spacing -0.85px, line-height 0.84, centered alignment. Used for section titles like 'MAX BTC EXPLAINED'. Often paired with small uppercase section labels at 12px in opposite corners.

### Classical Painting Panel

Renaissance/Baroque oil painting reproduction, edge-to-edge with no border or rounded corners, no overlay. The image fills the entire section viewport. Functions as background atmosphere, not as a content asset.

## Similar Design Systems

- {'why': 'Same editorial serif + grotesk pairing with dramatic size contrast and warm neutral canvas', 'business': 'Framework (framework.so)'}
- {'why': 'Same restrained warm-beige palette with serif display type and a gallery-like product presentation', 'business': 'Aesop'}
- {'why': 'Same minimal header (logo + single link), oversized wordmark, and alternating light/dark full-bleed sections', 'business': 'Vercel (older brand identity)'}
- {'why': 'Same use of classical painting as atmospheric full-bleed imagery and serif typography at large display sizes', 'business': 'Renaissance Art Museum sites (e.g. The Met)'}

## Agent Prompt Guide

## Quick Color Reference
- Background (light): #c4c3b6 (Putty)
- Background (dark): #000000 (Ink)
- Card surface: #e7e5e4 (Bone)
- Text primary: #000000 on light / #ffffff on dark
- Text muted: #595855 (Graphite)
- Border: #dfdcd5 (Vellum)
- primary action: no distinct CTA color

## Example Component Prompts

1. **Hero Wordmark Section**: Full-bleed #c4c3b6 background. Top-left: circled 'S' monogram in #000000 stroke. Top-right: 'Structured Points' in Helvetica Now 12px weight 400, #000000. Center cluster: 'REAL YIELD on BITCOIN' in Davinci 52px weight 500, #000000, letter-spacing -0.47px ('on' in italic). Below: 'TVL: 85 BTC    APY: 6%' in Helvetica Now 16px weight 500. Below: filled black pill button, 9px 17px padding, 28.8px radius, 'mint mxBTC' in Helvetica Now 12px weight 400, #ffffff. Then a 374px Davinci weight 500 #000000 wordmark 'Structured' at letter-spacing -3.37px, cropped at viewport edges.

2. **Dark Feature Section**: Full-width #000000 background. Centered heading 'MAX BTC EXPLAINED' in Davinci 94px weight 500, #ffffff, letter-spacing -0.85px. 3-column grid below: each column has a Davinci 22px weight 400 caption in #ffffff, a ~200px circular image crop, and a 12px hexagonal outline indicator in #ffffff stroke. Column gap 28px.

3. **Floating Product Card Over Painting**: Full-bleed classical landscape painting. Centered dark product card, ~400px square, #000000 background with notched/hexagonal corner cuts, 9px primary edge radius. Lower-left corner: 'SCROLL' in Helvetica Now 9px weight 400, #ffffff.

4. **Stat Display Block**: Inline row of two stat pairs on #c4c3b6 background. 'TVL: 85 BTC' and 'APY: 6%' in Helvetica Now 16px weight 500, #000000, separated by 28px gap. No borders, no backgrounds.

5. **Minimal Header**: Full-width #c4c3b6 background row, ~40px tall. Left: 32px circled 'S' monogram, 1.5px #000000 stroke, transparent fill. Right: 'Structured Points' text link in Helvetica Now 12px weight 400, #000000, no underline.

## Typographic Philosophy

The system uses size and tracking to create drama, not color or weight contrast. Display type at 94–374px carries letter-spacing between -0.85 and -3.37px — tighter as size increases, so the wordmark reads as a single carved shape rather than separate letters. Body type stays at 9–16px with normal tracking. The serif (Davinci) does all emotional work; the grotesk (Helvetica Now) does all functional work. Never let them compete: serif is for moments, grotesk is for systems. Line-heights compress at display sizes (0.84 at 94–374px) to make headings feel carved rather than set. The 374px hero wordmark is intentionally cropped at the viewport — it should always feel larger than the screen.
