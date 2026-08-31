# OFFFICE : — Design System

> **North Star**: noir gallery swallowed by monolithic type
> **Theme**: dark
> **Source**: https://offficestud.io
> **Refero Style**: https://styles.refero.design/style/190d4a0b-0353-4fc8-be09-affa6e977146
> **Synced**: 2026-09-01

## Overview

OFFFICE operates as a black-walled gallery where typography is architecture: a single custom sans-serif (ak) scales from 12px micro-labels to 216px display blocks that bleed off the viewport edges, with line-heights collapsing to 0.80 to stack text into wall-like slabs. The entire palette is near-black canvas against near-white ink — no accent color, no semantic hues, no gradients. A second custom serif (gs) appears only inside the project archive, bringing a subtle editorial counterpoint to the otherwise austere sans system. Product is presented as a single sculptural 3D object centered in the void, overlapping text in the scroll sequence to create depth without any shadow or elevation system. Everything is flat, full-bleed, and typographically loud.

## Color Palette

- **Onyx**: `#0e0e00` — Full-bleed page background, navigation surface, product staging void — the entire canvas is one continuous dark field [neutral]
- **Paper White**: `#fefefe` — Display headlines, body text, navigation labels, archive list entries, locale switcher — the sole ink color across all UI layers [neutral]
- **Faint White**: `#2a2a2a` — Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color [neutral]

## Typography

- **ak**
- **gs**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.4 |
| body | 18 | — | 1.33 |
| subheading | 20 | — | 1.1 |
| heading | 58 | — | 1 |
| heading-lg | 72 | — | 0.9 |
| display | 216 | — | 0.8 |

## Spacing & Layout

- **Card Padding**: 0px
- **Element Gap**: 8px
- **Section Gap**: 96-128px
- **Border Radius**: {'tags': '0px', 'cards': '0px', 'buttons': '0px'}

## Layout

Full-bleed layout with no max-width constraint. Every element can touch the viewport edges. The hero pattern is: minimal top nav → massive type that overflows horizontally → centered 3D product overlapping the type → small editorial caption to the right of the product. Content scrolls into an archive list section where project titles in serif (gs 72px) stack vertically at 32px intervals, with 3D product renders floating over the list on scroll to create implicit layering. Navigation is a single thin top bar (no sticky behavior indicated, no hamburger). The grid is effectively a single column with generous vertical rhythm — 96–128px between major sections. There is no sidebar, no footer structure, no multi-column layout. The entire site reads as a vertical sequence of typographic and sculptural moments.

## Surfaces / Elevation

- **Onyx Canvas**

## Imagery

No photography, no illustration, no icons. The sole visual content is 3D product renders of furniture (chairs, armchairs) presented as dark sculptural forms on the Onyx void. Renders are high-fidelity with realistic material surfaces (fabric texture, wood grain on legs) but no environmental context — no room, no floor, no lighting setup. They are objects-in-space, not products-in-context. The imagery philosophy is museum-object-on-black-pedestal, where the pedestal is the page itself.

## Design Principles

### Do

- Use ak weight 400 for all body and display text; reserve ak weight 700 only for the 'GET IN TOUCH' nav CTA and emphasis that must break through at small sizes
- Let display headlines overflow viewport edges — 216px ak at 0.80 line-height is meant to be cropped by the frame
- Use Onyx (#0e0e0e) as a single continuous background across all pages; never introduce a lighter surface or card fill
- Use gs serif 72px exclusively for archive project titles — this is the only place the serif appears
- Space archive list entries at exactly 32px vertical gap to create rhythmic stacking
- Position 3D product renders centered in the viewport with no shadow, platform, or environmental context
- Set all small metadata (nav, labels, captions) in ak 12px with 1.50+ line-height for gallery-wall-label tone

### Don't

- Do not introduce any accent color, brand color, or chromatic hue — the system is 100% achromatic by design
- Do not add borders, dividers, or background fills to separate sections — use space and type scale instead
- Do not use border-radius on any element — all corners are sharp (0px)
- Do not use shadows, glows, or blur effects for elevation — the design is flat by philosophy
- Do not use the serif (gs) for body copy, navigation, or anything outside the archive project titles
- Do not add gradients, textures, or background patterns to the Onyx canvas
- Do not constrain display headlines with max-width or text-overflow:hidden styling — overflow is the point

## Components

### Top Navigation Bar

Full-bleed, no background fill, sits directly on Onyx canvas. Left: 'offfice studio' in ak 12px weight 400, Paper White. Right: 'GET IN TOUCH' in ak 12px weight 700, Paper White. No border, no shadow, no hamburger menu. Padding: 16px from viewport edges.

### Display Headline Block

ak weight 400 at 216px, line-height 0.80, Paper White. Text deliberately overflows viewport edges — 'OFFICE FOR' bleeds off the right, 'FUTURE' bleeds off the left. No max-width constraint. The tight leading stacks glyphs into a slab that reads as a graphic shape, not a sentence. This is the signature element.

### Product Sculpture (3D Hero Object)

A single dark-toned 3D render of furniture, positioned in the viewport center. Renders in the same tonal range as the Onyx background (near-black) with subtle specular highlights from form, not from a light effect. No background, no platform, no shadow — it floats in the void. In scroll sequences, it overlaps archive list text to create a z-axis depth effect.

### Description Caption

ak 12px weight 400, line-height 1.56, Paper White, all-caps tracking. Text reads: 'FUTURE LIVING DESIGN RESEARCH STUDIO. INSTALLATIONS, COMMERCIAL AND PRIVATE SPACES.' No paragraph break, no emphasis — flat, informational, gallery-wall-label tone.

### Locale Switcher

ak 12px weight 400, Paper White, positioned at the far right below the nav. Format: 'IT / ES / CH' separated by spaces and forward slashes. No active-state styling difference — all three are the same weight and color, implying availability not state.

### Archive Project Entry

Four-column horizontal layout: project title in gs 72px serif weight 400 (Paper White) on the left, year in ak 12px weight 400, category labels ('PROJECT DETAILS', 'Armchair', 'Interior') in ak 12px weight 400 spaced across the row. Entries are separated by 32px vertical gap. The serif title and sans metadata create a deliberate type-mixing effect within a single row.

### Archive List (Full)

Six to eight Archive Project Entries stacked vertically with 32px gaps. No section header, no dividers, no cards. The list occupies the full viewport width. Product 3D renders float over the list on scroll, creating parallax overlap without explicit z-index manipulation beyond natural stacking.

### Section Label (Inline)

ak 12px weight 400, Paper White, used for 'US / WW' region codes, 'Archive' contextual labels, and other micro-annotations. No background, no badge shape, no padding — text only, relying on position and size for hierarchy.

## Similar Design Systems

- {'why': 'Same furniture-design editorial language — monumental type, product-as-sculpture, near-black presentation, zero decorative chrome', 'business': 'Vitra'}
- {'why': 'Same full-bleed black canvas with massive sans-serif type that bleeds past viewport edges and a single product image floating in negative space', 'business': 'Camille Mormal'}
- {'why': 'Same dark-mode luxury product showcase where the object is the only non-text element and typography provides all structural hierarchy', 'business': 'Flos'}
- {'why': 'Same achromatic palette, oversized sans-serif display, and flat-borderless component language — design studio presenting work through typographic intensity', 'business': 'Studio Brasch'}

## Agent Prompt Guide

## Quick Color Reference
- background: #0e0e0e
- text: #fefefe
- border: none (use 0px borders, rely on space for separation)
- accent: none
- primary action: no distinct CTA color

## Example Component Prompts

1. **Display Headline Block**: Full-bleed, no max-width. Text in ak (or Neue Haas Grotesk substitute) weight 400, 216px, line-height 0.80, color #fefefe, on #0e0e00 background. Let text overflow viewport edges horizontally — do not constrain width. This is the signature hero element.

2. **Top Navigation Bar**: Full-bleed, no background fill. Left: 'offfice studio' in ak 12px weight 400, #fefefe. Right: 'GET IN TOUCH' in ak 12px weight 700, #fefefe. 16px padding from viewport edges. No border, no shadow.

3. **Archive Project Entry Row**: Full-width single row. Project title in gs serif (or GT Sectra substitute) 72px weight 400, #fefefe. Year in ak 12px weight 400, #fefefe, positioned to the right of title. Category labels ('Armchair', 'Interior', 'PROJECT DETAILS') in ak 12px weight 400, #fefefe, spaced across the row. 32px vertical gap between entries.

4. **Product Hero Object**: A single centered 3D furniture render (chair/armchair) on #0e0e00 background. No floor plane, no platform, no shadow, no environment. Object fills roughly 40-50% of viewport height. Tonal range matches the dark background — near-black with subtle material highlights. Renders may overlap text elements on scroll to create depth.

5. **Description Caption Block**: ak 12px weight 400, line-height 1.56, #fefefe, all-caps. Positioned to the right of or below the product hero. No emphasis, no bold words, no color differentiation. Reads as a gallery wall label — informational and flat.

## Two-Font System

The entire system runs on two custom faces: ak (geometric sans, 400/700, used at every size from 12px to 216px) and gs (high-contrast serif, 400 only, used exclusively for archive project titles at 72px). No third font enters the system. No system fonts. No icon font. The sans does all structural and informational work; the serif is a single-purpose editorial accent that signals 'this is a project title, not navigation.'

## Type Scale Extremes

The scale jumps from 20px (subheading) to 58px (heading) to 216px (display) — there is no 30px, 40px, or 80px middle ground. This binary of 'normal' and 'monumental' forces every design decision into either functional copy or architectural statement. There is no 'medium' option. This is deliberate: the system communicates in whispers and shouts, never in conversation.
