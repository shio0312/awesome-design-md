# Metalab — Design System

> **North Star**: black editorial spread — a serif headline breathing in void, annotated by a whisper-quiet grotesque
> **Theme**: dark
> **Source**: https://metalab.com
> **Refero Style**: https://styles.refero.design/style/da087e69-8832-418a-aa1b-42e1acabb39e
> **Synced**: 2026-09-01

## Overview

Metalab operates in a black-canvas editorial mode: a design agency that lets typography and negative space do the entire performance. Two custom typefaces share the stage — an ultra-light display serif (PP Eiko) at commanding sizes, and a quiet grotesque (Basis Grotesque Pro) for all functional copy — creating a dialogue between a whispering serif headline and a precise sans-serif annotation layer. The interface is achromatic by conviction: no accent color exists, no decorative gradient, no brand chromatic mark. Information is structured purely through scale contrast, micro-typography, and metadata labels (dates, times, coordinates) that float beside content like editorial marginalia. Components are sparse and oversized — a single dark elevated card, a pill toggle, and very little else. The system reads less like a product UI and more like the masthead of a design publication.

## Color Palette

- **Void**: `#000000` — Page canvas, primary surface, heading text on light zones — the dominant black that absorbs all surrounding elements [neutral]
- **Bone**: `#ffffff` — Inverse text on dark surfaces, hairline borders on dark zones, contrast punctuation against the black canvas [neutral]
- **Charcoal**: `#252525` — Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color [neutral]

## Typography

- **Basis Grotesque Pro**
- **PP Eiko**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.4 |
| body | 16 | — | 1.2 |
| display | 88 | — | 0.8 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 24px
- **Element Gap**: 24px
- **Section Gap**: 96px
- **Border Radius**: {'cards': '50px', 'pills': '1000px', 'buttons': '50px'}

## Layout

The page is full-bleed with no container constraint — text and elements flow edge-to-edge across a wide viewport (1440px+ target). The hero pattern is a three-column asymmetric split: display headline flush-left, a dark elevated panel centered, and a secondary headline word ('Make') flush-right with metadata annotations floating in the margins. Section rhythm uses generous vertical gaps (96px+) with no visible dividers — separation is spatial, not structural. Navigation is a minimal text row at the top, not a bar with background fill. The overall density is low: large amounts of black space, few elements per screen, and each element given room to breathe. The grid is loose — columns are implied by alignment, not by visible lines.

## Surfaces / Elevation

- **Void**
- **Charcoal**
- **Bone**

## Imagery

Imagery is minimal and treated with the same restraint as the type system. A single dark, softly gradient panel appears in the hero — its surface is nearly featureless, suggesting a product or device rendering rather than a photograph. No lifestyle photography, no illustration, no decorative graphics. The visual weight of the page comes entirely from typography and negative space. If images appear on inner pages, they would be high-contrast, tightly cropped, and sit on the same #000000 canvas without frames or borders.

## Design Principles

### Do

- Use PP Eiko at 88px weight 240 exclusively for the largest display moments — never at body sizes where the hairline weight becomes illegible
- Set all display headlines to line-height 0.80 and letter-spacing -0.02em to achieve the sculptural, near-touching letterforms
- Use Basis Grotesque Pro weight 350 at 12px for all metadata annotations (dates, locations, timestamps) — this is the system's editorial signature
- Build depth through a single #252525 surface layer over the #000000 canvas — do not introduce additional grays or shadows
- Apply border-radius 50px to all buttons and elevated panels for the soft, tablet-like silhouette that defines the system
- Anchor all dark pages on the #000000 canvas with #ffffff typography — never invert to a white page background within a dark-theme design
- Use line-height 1.76-2.00 for body copy to match the editorial spaciousness of the display type

### Don't

- Do not introduce any chromatic color — no blues, reds, greens, or brand accents. The system is achromatic by conviction
- Do not use PP Eiko at sizes below 40px — the weight 240 becomes too thin to render reliably at small sizes
- Do not add drop shadows to any element — depth in this system comes from surface value contrast (#000000 → #252525), not elevation effects
- Do not use weight 600+ for any text — the entire system operates in the 240-400 range; heavier weights break the whisper-quiet tone
- Do not add gradients, glows, or any color effects — the flat achromatic palette is the brand identity
- Do not use system serif defaults (Times, Georgia) as substitutes for PP Eiko without matching the ultra-light weight — a regular-weight serif will read as conservative, not editorial
- Do not fill buttons with #ffffff on the dark canvas — it would create the only bright shape on the page and dominate the hierarchy. Use #252525 or transparent

## Components

### Dark Elevated Panel

A tall rounded rectangle filled with #252525 on the #000000 canvas. Border-radius 50px gives it a soft, tablet-like silhouette. No border, no shadow — depth comes purely from the value difference between #000000 and #252525. Dimensions feel cinematic: roughly 380px wide, 500px+ tall, centered or asymmetric in the layout.

### Pill Toggle

Small pill with border-radius 50px or 1000px, padding 3px top/bottom and 16px left/right. Bone (#ffffff) text on transparent or charcoal background. 12px Basis Grotesque Pro at weight 350. Examples: '0 → 1' counter, 'EST 2006' tag.

### Metadata Annotation

12px Basis Grotesque Pro weight 350 in #ffffff, positioned with generous offset from the content it annotates. Always uppercase or title-case. Examples: 'EST 2006', 'BC, CA', '12:32 EDT'. Acts as a typographic signature of the brand — the system of small floating labels is what makes the page feel curated.

### Display Headline

88px PP Eiko weight 240, line-height 0.80, letter-spacing -0.02em. White (#ffffff) on the black canvas. Typically one or two words per line at this scale, creating a staccato rhythm. No maximum width constraint — the text breathes across the full viewport column.

### Ghost Button

Transparent or #252525 fill with #ffffff text. Border-radius 50px. Padding 16px horizontal, small vertical inset. 16px Basis Grotesque Pro weight 400. No border, no shadow. The button blends into the dark canvas until hovered.

### Nav Link

16px Basis Grotesque Pro weight 400, #ffffff, no underline. Items separated by generous horizontal spacing. The nav itself is a quiet row, not a bar — it doesn't compete with the editorial typography.

### Body Copy

16px Basis Grotesque Pro weight 400, line-height 1.76-2.00 (generous, editorial). #ffffff on the black canvas. The high line-height values are deliberate — they create airy columns of text that match the spaciousness of the layout.

### List Item

16px Basis Grotesque Pro in #ffffff, separated by 8px row gaps. Minimal bullet treatment or no bullets at all — the spacing alone creates list rhythm.

## Similar Design Systems

- {'why': 'Same editorial-agency approach: black canvas, oversized type, minimal UI chrome, metadata-style annotations', 'business': 'Ueno'}
- {'why': 'Dark-mode agency portfolio with serif/sans-serif type pairing and generous negative space', 'business': 'Locomotive'}
- {'why': 'Experimental agency aesthetic with achromatic palette and typography-as-hero philosophy', 'business': 'Resn'}
- {'why': 'Dark-canvas design studio site with restrained color and type-driven layout', 'business': 'Ramotion'}
- {'why': 'Editorial agency presentation style: black background, large light-weight serif, micro-typography for metadata', 'business': 'Manual'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff
- background: #000000
- border: #ffffff
- accent: no accent color (achromatic system)
- primary action: no distinct CTA color
- surface elevation: #252525

**Example Component Prompts**

1. Create a hero section: #000000 background, full-bleed. Left-aligned 88px PP Eiko weight 240 headline in #ffffff, line-height 0.80, letter-spacing -0.02em reading 'We Make Interfaces'. Center column: a #252525 rounded panel, border-radius 50px, roughly 380px wide by 500px tall. Right margin: floating 12px Basis Grotesque Pro weight 350 annotations in #ffffff ('EST 2006', '12:32 EDT').

2. Create a navigation bar: minimal text row on #000000 background. 16px Basis Grotesque Pro weight 400 in #ffffff, items left-aligned with 24px gaps, no background fill, no border.

3. Create a ghost button: transparent background on #000000 canvas, #ffffff text at 16px Basis Grotesque Pro weight 400, border-radius 50px, padding 16px horizontal / 8px vertical. No border, no shadow.

4. Create a metadata label: 12px Basis Grotesque Pro weight 350 in #ffffff, positioned as a small floating annotation in the margin of a content layout. No background, no border — just typographic presence.

5. Create a dark elevated card: #252525 fill on #000000 canvas, border-radius 50px, padding 24px. No shadow, no border. Body text inside in #ffffff at 16px Basis Grotesque Pro weight 400, line-height 1.76.
