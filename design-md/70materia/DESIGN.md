# 70Materia — Design System

> **North Star**: Architectural sample board on white paper — the UI is the mount, never the artwork.
> **Theme**: light
> **Source**: https://70materia.com
> **Refero Style**: https://styles.refero.design/style/f22a5ad1-2770-48d5-aff4-d1aaf0b789b8
> **Synced**: 2026-09-01

## Overview

70Materia is a neutral frame built to disappear around its content — a curated material library where the UI chrome is deliberately invisible so stone, terrazzo, and pigment samples can dominate. Every typographic element sits at weight 400 in a single sans family (Matter), with a monospace companion (Matter Mono) used for labels, navigation, and small UI controls. Letter-spacing on the mono (0.02em–0.04em) plus tabular numerals gives the interface a spec-sheet, architectural-drawing quality — as if the page itself is a technical sample board. The palette is strictly achromatic: black text, white surfaces, and a warm mid-gray canvas (#bababa) that recedes behind the photography. Buttons are thin, square, and outlined; the only filled surface is a near-black (#1e1e1e) for select actions and the footer. No accent color exists in the system — all chromatic energy is outsourced to the product photography.

## Color Palette

- **Obsidian**: `#000000` — Primary text, hairline borders, navigation outlines — the structural ink [neutral]
- **Bone**: `#ffffff` — Page highlights, card surfaces, text on dark surfaces, button outlines [neutral]
- **Graphite**: `#1e1e1e` — Filled button background, footer surface, dark UI blocks — warm near-black replacing pure black for non-text surfaces [neutral]
- **Ash**: `#bababa` — Dominant page canvas, muted dividers, secondary surface tone [neutral]

## Typography

- **Matter**
- **Matter Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.3 |
| body | 15 | — | 1.2 |
| subheading | 19 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 960px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 100-180px
- **Border Radius**: {'tags': '0px', 'cards': '0px', 'inputs': '0px', 'buttons': '3px'}

## Layout

The page is a vertical sequence of full-bleed editorial moments, each consisting of either a single full-width image or a two-column image+text block. The hero opens with an edge-to-edge photograph and the nav floats on top; no centered headline, no gradient overlay. After the hero, sections appear as centered two-column grids with a max content width of ~960px, where each column contains an image stacked above a mono label, a short body paragraph, and an outlined button. Section spacing is generous (100–180px vertical padding), creating a slow museum-walk rhythm between content blocks. There is no sidebar, no card grid, no pricing table — the layout is always image-then-text, never the reverse. Navigation is a single transparent top bar; the footer is a dark band that closes the page.

## Surfaces / Elevation

- **Canvas**
- **Paper**
- **Lacquer**

## Imagery

Photography is the entire visual identity. Images are tight, material-focused crops of finished surfaces — terrazzo tables, stone slabs, pigment samples, furnished interiors — presented as full-bleed objects with no lifestyle context. The subject is always the material itself, isolated against neutral concrete or white walls, lit with soft natural light. No illustration, no abstract graphics, no icons except tiny mono-style UI labels. Color treatment is true-to-life — the system trusts the materials to be chromatic. The visual density is overwhelmingly image-heavy: one photograph typically occupies 60–100% of the viewport, with text and UI chrome compressed into small 10–12px labels that read as documentation rather than design.

## Design Principles

### Do

- Set every heading and body run in Matter at weight 400 — never introduce a bold weight to create hierarchy; use size and space instead.
- Use Matter Mono 10–12px with letter-spacing 0.02em–0.04em for all labels, nav items, button text, and product codes.
- Let product photography fill the viewport edge-to-edge; never crop, frame, or overlay UI on hero images.
- Build buttons as 1px outlined rectangles with 3px radius and 8px × 24px padding — the default action style.
- Use #bababa as the page canvas and let white (#ffffff) appear only as inset paper or dark text on dark surfaces.
- Keep the corner radius at 3px for buttons and 0px for everything else; the system is fundamentally sharp-edged.
- Apply tabular numerals ("tnum") on all text containing numbers so they align vertically across the page.

### Don't

- Do not introduce any chromatic accent color — orange, blue, green, red. The palette is permanently achromatic; color is the photography's job.
- Do not use drop shadows, gradients, or glow effects — the depth model is light surface → mid-gray canvas → dark footer, nothing more.
- Do not round card corners, image corners, or section containers — only buttons get a 3px radius; everything else is sharp.
- Do not use a bold or semibold weight from Matter; weight 400 is the only weight in the system.
- Do not place colored text, colored icons, or colored borders on functional UI — keep all chrome black, white, or gray.
- Do not center body copy in editorial sections; left-align descriptions and labels in the two-column showcase layout.
- Do not use a filled white input field with a visible border — form fields are defined by a single bottom underline only.

## Components

### Primary Outlined Button

1px solid #000000 border on transparent background, 3px corner radius, 8px vertical × 24px horizontal padding. Label set in Matter Mono 12px, weight 400, letter-spacing 0.02em, uppercase, #000000. No hover fill — the button stays an outline at all times, reading more like a tagged label than a CTA.

### Filled Dark Button

Background #1e1e1, white Matter Mono 12px label, 3px radius, 8px × 24px padding. Reserved for high-intent actions; the rest of the system is outlined.

### Top Navigation Bar

Transparent over the hero image, single row, logo '70Materia' left in Matter 20px, nav items right (MATERIALS, APPLICATIONS, PRODUCTS, PROJECTS, JOURNAL, COMPANY, NEWS, CONTACTS) in Matter Mono 10px uppercase, letter-spacing 0.04em, #000000. No background fill, no shadow — the nav floats on the image.

### Full-Bleed Hero Image

Edge-to-edge photograph, no overlay, no gradient, no text within the image area. The first screen of the site is 100% photography — the UI only appears as nav chrome on top.

### Two-Column Showcase Section

Two equally weighted columns, each containing a full-bleed image, a Matter Mono 10px label (e.g. VISIT OUR SHOWROOM), a Matter 15px description paragraph in #000000, and an outlined button beneath. 24px row gap between elements, columns separated by the page canvas, not a divider.

### Product Caption Tag

Bottom-left of the viewport, Matter Mono 10px, uppercase, letter-spacing 0.04em (e.g. 'AT.OLO'). Functions as a museum-style object label — the same piece of furniture/material gets identified regardless of which section you're viewing.

### Footer

Dark band, background #1e1e1, text #ffffff in Matter Mono 10–12px. Minimal — links, address, and legal. The only place the page drops below the gray canvas into a defined dark block.

### Image Card

Zero radius, no border, no shadow. Images sit directly on the #bababa canvas or on a white (#ffffff) panel. The corner is always sharp — the materials themselves provide the visual interest, not the frame.

### Newsletter Input Row

Underlined text input (1px #000000 bottom border only) with a SUBSCRIBE button to the right. No filled input field, no rounded corners — the underline is the entire affordance.

## Similar Design Systems

- {'why': 'Same material-library editorial approach — achromatic UI, full-bleed stone and surface photography, mono-style small labels, and outlined ghost buttons that defer to the materials', 'business': 'Dzek (dzekdzek.com)'}
- {'why': 'Architectural practice websites that use the same neutral-canvas + large-format photography + tiny mono label pattern, with buttons as thin-outlined rectangles', 'business': 'Studio Zhu Pei'}
- {'why': 'Italian stone brand that pairs a mid-gray or white page canvas with large hero photography and minimal outlined UI chrome', 'business': 'Salvatori'}
- {'why': 'Surface/tile brand using a similar spec-sheet sensibility — mono labels with letter-spacing, matter-of-fact body type at 400, and a palette that stays achromatic so the tile photography carries the color', 'business': 'Mutina (mutina.it)'}

## Agent Prompt Guide

## Quick Color Reference
- background: #bababa (page canvas)
- surface: #ffffff (inset paper, text panels)
- text: #000000 (primary), #ffffff (on dark)
- border: #000000 (1px hairlines)
- primary action: #1e1e1e (filled action)
- dark surface: #1e1e1e (filled button, footer)

## Example Component Prompts

1. **Outlined Action Button** — "Create a DISCOVER THE SHOWROOM button. 1px solid #000000 border, transparent background, 3px corner radius, 8px vertical × 24px horizontal padding. Label in Matter Mono 12px weight 400, letter-spacing 0.02em, uppercase, color #000000. No hover fill, no shadow."

2. **Two-Column Editorial Section** — "Build a centered two-column block at max-width 960px on a #bababa canvas. Left column: full-bleed photograph with no border or radius. Below the image, a Matter Mono 10px uppercase label 'VISIT OUR SHOWROOM' in #000000, then a Matter 15px paragraph in #000000, then an outlined button (see prompt 1). Right column mirrors the same structure with label 'ENTER THE WORLD OF 70MATERIA'."

3. **Full-Bleed Hero with Floating Nav** — "Render a full-viewport photograph edge-to-edge with no overlay. Top nav bar floats over the image: logo '70Materia' in Matter 20px #000000 on the left; nav items (MATERIALS, APPLICATIONS, PRODUCTS, PROJECTS, JOURNAL, COMPANY, NEWS, CONTACTS) in Matter Mono 10px uppercase, letter-spacing 0.04em, #000000, right-aligned. No background on the nav."

4. **Persistent Product Caption** — "Place a fixed label in the bottom-left corner of the viewport: Matter Mono 10px uppercase, letter-spacing 0.04em, #000000, e.g. 'AT.OLO'. No background, no border — the label sits directly on the image as if it were a museum object tag."

5. **Newsletter Underline Input** — "Create an email capture row: a single-line text input with no background and no border except a 1px #000000 bottom border, placeholder 'Your email' in Matter 15px #000000, followed by an outlined SUBSCRIBE button (see prompt 1). The input has 0px radius."
