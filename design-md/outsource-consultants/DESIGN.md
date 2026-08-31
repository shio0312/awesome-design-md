# Outsource Consultants — Design System

> **North Star**: Architectural broadsheet on bone paper. A monograph aesthetic where one violent indigo section interrupts an otherwise warm, typographically maximalist grid.
> **Theme**: light
> **Source**: https://oci.madebybuzzworthy.com
> **Refero Style**: https://styles.refero.design/style/16be276a-d8ce-484e-8f7a-cbbb09f717f7
> **Synced**: 2026-09-01

## Overview

Outsource Consultants operates on a stark editorial-architectural system: a warm bone-gray canvas, a single vivid indigo that detonates across full-bleed sections, and typography that swings between a grotesque sans at 160px and a mono micro-label at 10px. The aesthetic borrows from Swiss broadsides and architecture plates — large type does the heavy lifting while information is compressed into monospaced metadata. Layouts are asymmetric and generous, with sections alternating between bone and indigo rather than stacking on white. Components are borderless, almost flat, relying on scale and the indigo-on-bone contrast to create hierarchy rather than elevation, shadows, or fills. The system feels less like a SaaS dashboard and more like a printed monograph for a technical practice.

## Color Palette

- **Indigo Strike**: `#1925aa` — Brand mark, full-bleed section backgrounds, large headlines, icon strokes, nav borders — the singular chromatic voice of the system, used as a sudden tonal shift rather than a decorative accent [brand]
- **Bone**: `#e8e6e0` — Page canvas and card surface — a warm off-white that reads as paper rather than screen, providing the neutral ground against which indigo gains force [neutral]
- **Ink**: `#000000` — Body copy, small labels, standard text — used for dense information layers that must stay recessive against the bone canvas [neutral]
- **Paper**: `#ffffff` — Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color [neutral]
- **Deep Indigo**: `#0d1355` — Logo and brand-mark fill — a near-black violet that grounds the wordmark against the brighter Indigo Strike used in UI contexts [brand]

## Typography

- **GT America Mono**
- **PP Neue Montreal**
- **ui-sans-serif**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.5 |
| body | 16 | — | 1.5 |
| body-lg | 18 | — | 1.5 |
| subheading | 24 | — | 1.3 |
| heading-sm | 30 | — | 1.2 |
| heading | 36 | — | 1.1 |
| heading-lg | 46 | — | 1.05 |
| display | 160 | — | 0.94 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 20px
- **Element Gap**: 15px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '0px', 'cards': '0px', 'inputs': '0px', 'buttons': '0px'}

## Layout

Asymmetric editorial layout. The page is not a max-width centered column — it is a series of full-bleed horizontal bands (bone or indigo) with content anchored to the left edge and occasional vertical annotations in the right margin. The hero is a 160px flush-left display headline with a rotated side label, spanning the full viewport. Section transitions use the split-heading device (one word left, one word right, hairline bisector). Service lists are full-width accordions, not card grids. Navigation is a minimal single-line header with no dropdowns visible — menu access is gated by the Menu button. The overall rhythm is slow and poster-like: few elements per viewport, large vertical breathing room (80px section gaps), and tonal shifts doing the work that cards and grids do in conventional SaaS layouts.

## Surfaces / Elevation

- **Bone Canvas**
- **Paper**
- **Indigo Field**

## Imagery

No photography, illustration, or product imagery. The system is pure typography on flat color — the page reads as a printed document. The only graphical element is the small square brand mark in the header and the '/' icon glyph in the menu button, both flat single-color. Visual richness comes entirely from typographic scale and the bone/indigo tonal alternation.

## Design Principles

### Do

- Let PP Neue Montreal do the work — push display sizes to 46–160px and use line-height 0.94–1.10 at those scales; do not add weight to compensate for small size.
- Use GT America Mono exclusively for labels, captions, nav items, and accordion descriptions; keep it at 10–14px with tracking -0.05em (tight) at 10px and +0.02em (open) at 14px.
- Alternate between the bone canvas and the Indigo Strike full-bleed to create section rhythm — do not stack multiple bone sections without an indigo interruption.
- Treat borders as hairlines: 1px Ink at low opacity for dividers between accordion rows and section bisectors; never use borders for cards or containers.
- Use vertical rotated text in the right margin (18px PP Neue Montreal) as a section annotation device.
- Anchor every section with a flush-left display headline in the body color (Ink on bone, Bone on indigo); keep headlines full-width and uncontained.
- Keep all corners sharp — 0px radius on every element including buttons, cards, and tags.

### Don't

- Do not introduce shadows, glows, blurs, or any form of drop elevation — the system is deliberately flat.
- Do not use indigo as a button background fill — the Menu button is white with an indigo icon square; indigo is a surface, not an action color.
- Do not add a second accent color — the system is bone + ink + a single indigo; any new chromatic role will dilute the editorial tension.
- Do not use PP Neue Montreal below 12px — the grotesque loses character at small sizes; switch to GT America Mono for anything sub-14px.
- Do not center headlines or wrap them — display type stays flush-left and bleeds toward the page edge.
- Do not use cards with backgrounds, padding, or radius — content sits directly on the bone canvas divided only by hairlines.
- Do not use a system font fallback for hero type — if PP Neue Montreal is unavailable, substitute with a grotesque (Inter or Söhne), not a humanist sans.

## Components

### Brand Header Bar

Left-aligned logo wordmark ('Outsource Consultants Inc.') set in GT America Mono 10px in Deep Indigo, preceded by a small square brand mark in Deep Indigo. Right-aligned secondary nav links in GT America Mono 10px tracking +0.02em. The header sits directly on the bone canvas with no background fill and no shadow — its presence is defined by content density rather than a container.

### Menu Toggle Button

A square Paper (#ffffff) button containing the word 'MENU' in GT America Mono 10px tracking +0.02em in Ink, with a flush-right 1:1 Indigo Strike square containing a white '/' glyph. Zero radius, no border, no shadow. The pairing of neutral button + chromatic icon is the only place where indigo acts as a small functional mark — it reads as a light switch rather than a CTA.

### Hero Display Headline

PP Neue Montreal 160px weight 400, line-height 0.94, color Bone (#e8e6e0) when on the indigo full-bleed, or Ink when on bone canvas. The extreme line-height is intentional — letters at 160px nearly touch vertically, creating a dense block of type. Sits flush-left, bleeding to the page edge, with no accompanying image or illustration.

### Vertical Side Label

Short caption (2–4 words) rotated 90° counter-clockwise, set in PP Neue Montreal 18px weight 400 in Bone, positioned in the right margin. Acts as a printed-margin annotation — a signature editorial device borrowed from broadsheet layout.

### Full-Bleed Indigo Section

Edge-to-edge Indigo Strike (#1925aa) background with a large multi-line headline in PP Neue Montreal 46px weight 400 in Bone, and supporting body copy in 18px Bone. The section is a complete inversion of the bone canvas — same typography, reversed tonal relationship. Used sparingly, once per page, to break monotony.

### Service Accordion Item — Collapsed

Full-width row, PP Neue Montreal 24px weight 500 in Indigo Strike, flush-left, with a '+' glyph in PP Neue Montreal 24px in Indigo Strike flush-right. Separated from the next row by a 1px hairline border in Ink at 10–15% opacity. Zero padding-top/bottom asymmetry — the row is the unit of rhythm.

### Service Accordion Item — Expanded

Same row treatment as collapsed state but with a '×' glyph replacing '+', and a description block below in GT America Mono 10px tracking -0.05em in Indigo Strike, followed by a '[ LEARN MORE → ]' link in the same mono micro-label style. The expanded description sits indented to align with the title baseline, not flush-left, creating a subtle hanging indent.

### Section Heading Pair

Two words placed at opposite horizontal extremes of the section — e.g. 'Our' flush-left and 'Services' flush-right — both in PP Neue Montreal 160px weight 400 in Indigo Strike. A 1px vertical hairline in Ink at low opacity bisects the section between them. This split-heading pattern is a signature device for introducing multi-part content.

### Centered Body Caption

Short paragraph (2–4 lines) in GT America Mono 10px tracking +0.02em, all-caps, centered, in Indigo Strike. Used as a transitional element between sections — reads as a caption beneath an architectural plate.

## Similar Design Systems

- {'why': 'Same editorial-broadsheet approach: full-bleed single-color sections, grotesque sans at extreme display sizes, minimal nav, and typography doing all the compositional work', 'business': 'Pentagram'}
- {'why': 'Single-accent chromatic interruption against a neutral canvas, rotated side labels as annotation devices, and poster-scale type used in place of imagery', 'business': 'Studio Dumbar'}
- {'why': 'Architectural/technical aesthetic with mono micro-labels, hairline dividers, and a bone-paper feel — type as the primary visual element', 'business': 'Werkplaats Typografie archive'}
- {'why': 'Split two-word headings bisected by hairlines, generous asymmetric whitespace, and a single indigo/blue that detonates against warm off-white', 'business': 'Hofmann & Brand (or similar Swiss editorial agencies)'}

## Agent Prompt Guide

Quick Color Reference:
- text: #000000 (Ink) on bone, #e8e6e0 (Bone) on indigo
- background: #e8e6e0 (Bone canvas)
- border: 1px Ink at ~10% opacity for hairlines
- accent: #1925aa (Indigo Strike) — used for headlines, icons, and full-bleed section backgrounds, not for button fills
- primary action: no distinct CTA color

Example Component Prompts:

1. Service Accordion Row (collapsed): Full-width row on Bone canvas (#e8e6e0). Title in PP Neue Montreal 24px weight 500, color #1925aa, flush-left. '+' glyph in PP Neue Montreal 24px weight 400, color #1925aa, flush-right. 1px hairline border-bottom in #000000 at 10% opacity. Zero padding-radius. No background fill.

2. Hero Display Headline: PP Neue Montreal 160px weight 400, line-height 0.94, color #000000 (on bone) or #e8e6e0 (on indigo), flush-left, bleeding to the left page edge. Paired with a rotated 18px PP Neue Montreal caption in #e8e6e0 positioned in the right margin.

3. Menu Toggle Button: Square button, 40×40px, background #ffffff, containing 'MENU' in GT America Mono 10px tracking +0.02em in #000000, with a flush-right 40×40px #1925aa square containing a white '/' glyph. Zero radius, no border.

4. Full-Bleed Indigo Section: Background #1925aa spanning full viewport width. Headline in PP Neue Montreal 46px weight 400 line-height 1.05, color #e8e6e0, flush-left. Body copy in PP Neue Montreal 18px weight 400, color #e8e6e0.

5. Section Heading Pair: Two words (e.g. 'Our' and 'Services') in PP Neue Montreal 160px weight 400 color #1925aa, placed at opposite horizontal edges of the section (one flush-left, one flush-right). A 1px vertical hairline in #000000 at 10% opacity bisects the section between them.

## Typographic Philosophy

The system uses a single grotesque sans (PP Neue Montreal) from 12px to 160px, creating an extreme type ratio of ~13:1 between body and display. This is unusual — most sites cap display at 3–4× body size. The result is that headlines behave like posters rather than headings: they dominate the viewport and force the page to scroll vertically through them. Pairing this with a monospaced micro-face (GT America Mono) at 10–14px creates a two-register system: monumental statements and technical annotations. There is no middle-weight voice. Body text at 16–18px is the quietest register, which is counterintuitive but intentional — the system privileges the dramatic and the granular over the conversational.
