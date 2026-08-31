# OFF+BRAND. — Design System

> **North Star**: Iridescent sphere on warm parchment
> **Theme**: light
> **Source**: https://www.itsoffbrand.com
> **Refero Style**: https://styles.refero.design/style/6b667ffc-5158-4000-9252-3a107d5161ee
> **Synced**: 2026-09-01

## Overview

OFF+BRAND. operates as a typographic architecture on warm parchment: a near-monochrome canvas (#e5e4e0) where a single custom geometric sans-serif (Ataero Retina OB) carries nearly all the expressive weight. Headlines are monumentally large (up to 103px) with tight line-height (0.80) and whisper-wide tracking, while a singular iridescent gradient sphere — yellow bleeding into pink, then blue, then dissolving into white — anchors the hero as the only chromatic event on an otherwise achromatic page. Interfaces should feel like an editorial spread: thin concentric circle ornaments, a precise 2×5 client logo grid, grid-paper project cards, and label text that tracks wide like museum signage. There are no shadows, no fills, no buttons heavier than a ghost link with a 10px radius — restraint is the entire design language.

## Color Palette

- **Parchment**: `#e5e4e0` — Page canvas, section backgrounds — warm off-white that replaces pure white, making the page feel like printed stock rather than a screen [neutral]
- **Ink**: `#1d1d1d` — Primary text, heading strokes, link borders, all dark UI elements — near-black with zero blue cast, reading as editorial print [neutral]
- **Paper**: `#ffffff` — Elevated card surfaces, logo container backgrounds, project card canvases — pure white to lift content above the warm parchment [neutral]
- **Ash**: `#bfbebe` — Hairline borders, subtle dividers, structural outlines that need to recede against the parchment [neutral]
- **Stone**: `#cdcdc9` — Mid-tone surface between parchment and white — secondary panel background when a layer needs quiet separation [neutral]
- **Iridescent Sphere**: `#facb00` — Signature gradient object in the hero — the only chromatic element, flowing from saturated yellow through hot pink to cool blue before dissolving to white. Functions as a brand beacon, not a UI color [accent]

## Typography

- **Ataero Retina OB Edition**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.4 |
| body-sm | 15 | — | 1.4 |
| body | 18 | — | 1.4 |
| subheading | 34 | — | 1 |
| heading-sm | 46 | — | 1 |
| heading | 70 | — | 0.8 |
| heading-lg | 76 | — | 0.8 |
| display | 103 | — | 0.8 |

## Spacing & Layout

- **Max Width**: 1400px
- **Card Padding**: 30px
- **Element Gap**: 19px
- **Section Gap**: 76-119px
- **Border Radius**: {'cards': '0px', 'links': '10px', 'inputs': '10px', 'buttons': '10px'}

## Layout

Full-viewport hero with centered/left-aligned display text overlapping a large gradient sphere positioned right-of-center. Generous vertical breathing room: 76–119px between sections. Content blocks are left-aligned with asymmetric weight — large text left, supporting copy right. Client logos arranged in a strict 2×5 grid with hairline dividers. Project cards appear as large rectangular tiles with grid-pattern backgrounds. The page rhythm is: full-bleed hero → text-forward intro section → logo grid → featured work grid. No sidebar, no sticky navigation, no footer-heavy structure — navigation is minimal top-bar or absent, and the scroll indicator is the primary affordance. The concentric circle ornaments repeat across sections to create spatial continuity without section dividers.

## Surfaces / Elevation

- **Parchment Canvas**
- **Paper**
- **Stone Panel**

## Imagery

Imagery is restrained and product-focused. The hero features one large iridescent gradient sphere (not photography, not illustration — a pure CSS gradient form). Below the fold, project cards use product renders and screenshots on white backgrounds with grid-paper overlays. Client logos are flat monochrome marks in their own brand colors, contained within white cells. There is no lifestyle photography, no abstract illustration, no stock imagery. The visual language is: one gradient object as hero, then sharp product visuals on white for case studies.

## Design Principles

### Do

- Use #e5e4e0 as the exclusive page canvas — never substitute pure #ffffff or gray at the page level
- Set display headlines at 70–103px in Ataero Retina OB weight 400 with line-height 0.80 to create stacked typographic blocks
- Apply the iridescent sphere gradient (255deg, yellow → pink → blue → white) as a hero anchor, never as a button fill, border, or small accent
- Use 10px border-radius on all interactive elements (links, buttons, inputs) — 0px radius on all card surfaces
- Set section labels at 11px with letter-spacing 0.05em and all-caps — this tracking is a brand signature, not a style choice
- Separate sections with 76–119px vertical margins and use Ash (#bfbebe) 1px hairlines for structural dividers, never colored lines
- Maintain the monochrome discipline: if a screen needs more than the parchment/ink/white/ash palette, reassess the design before adding color

### Don't

- Do not introduce a second typeface family — Ataero Retina OB is the sole voice
- Do not use colored fills on buttons, cards, or backgrounds — all interactive surfaces stay ghost or white
- Do not add drop shadows, box-shadows, or elevation effects — the system is flat by design philosophy
- Do not use the gradient outside the hero sphere context — it is a single signature moment, not a recurring accent
- Do not set body text below 15px or above 18px — the 15/18 pair is the readable range in this system
- Do not center-align body paragraphs — body copy reads left-aligned, always
- Do not round card or image containers — cards are sharp-cornered (0px); only interactive elements get 10px radius

## Components

### Hero Gradient Sphere

Large circular form (roughly 50% of viewport height) positioned slightly right-of-center, filled with the iridescent gradient (yellow → pink → blue → white at 255deg). Sits behind display text, partially overlapping. Functions as brand beacon and atmospheric anchor. No border, no shadow, no interaction state.

### Display Headline

Ataero Retina OB, weight 400, 70–103px, line-height 0.80, letter-spacing ~0.013em. Ink (#1d1d1d) on Parchment (#e5e4e0). All caps. Lines stack tightly to form a single typographic block. Can span full viewport width. No text shadow, no gradient, no decoration.

### Ghost Text Link

Ataero Retina OB, 15px, weight 400, Ink (#1d1d1d) text. No background fill. 10px border-radius on the hit area. Often accompanied by a small arrow glyph (→). Padding 5px vertical, 0 horizontal. Underline or arrow reveals affordance on hover. This is the only clickable element style in the system.

### Section Label

Ataero Retina OB, 11px, weight 400, Ink (#1d1d1d), all caps, letter-spacing 0.05em. Aligned left, sits above section content with generous vertical space. Functions as a quiet navigational cue, not a heading.

### Client Logo Cell

Pure white (#ffffff) rectangular cell, no border, no shadow, no padding inside. Logos sit centered at ~60% width in Ink (#1d1d1d) or their own brand color. Arranged in a 2-row × 5-column grid with thin Ash (#bfbebe) hairline dividers (1px) between cells. The grid itself is the design — cells are austere.

### Featured Work Card

White (#ffffff) surface with a subtle dot-grid or line-grid pattern overlay (light gray, ~#e5e4e0 lines on white). Large project title in Ataero Retina OB 46px weight 400 Ink. No border, no shadow, no radius. Image or render sits below title. Functions as a printable editorial layout tile.

### Concentric Circle Ornament

Thin Ash (#bfbebe) or Ink-at-20%-opacity circular outlines, 1px stroke, positioned as background elements. Often 2–3 concentric rings at different radii, anchored to a focal point (sphere, headline, or viewport center). Never filled, never animated. Adds architectural depth without color.

### Scroll Indicator

Ataero Retina OB, 11px, weight 400, all caps, letter-spacing 0.05em, Ink. Text reads 'SCROLL' with a downward arrow. Fixed position, bottom-right with 30px inset. Minimal, editorial, disappears once user scrolls.

### Founder Intro Block

Left column: Section label ('WE ARE A FOUNDER-LED...') in 15px uppercase, weight 400, Ink, with 'ABOUT US →' ghost link below. Right column: body copy in 18px, line-height 1.40, weight 400, Ink. Column gap 19px. Sits on Parchment canvas with generous 76px vertical padding above and below.

### All Work Filter Button

Pill-shaped ghost button: Ink border 1px, 10px radius, padding 8px 19px. Ataero Retina OB 11px, weight 400, all caps, letter-spacing 0.05em, Ink text. Arrow glyph (→) at right. Hover: fill becomes Ink, text becomes Parchment. This is the only state-change button in the system.

## Similar Design Systems

- {'why': 'Same iridescent gradient hero sphere anchored to large display typography on a warm neutral canvas', 'business': 'Active Theory'}
- {'why': 'Monochrome editorial layout with oversized custom sans-serif display type and near-zero color palette', 'business': 'Resn'}
- {'why': 'Warm off-white canvas with sharp 0px-radius cards, grid-line decorative patterns, and typographic-first hierarchy', 'business': 'Locomotive (locomotive.ca)'}
- {'why': 'Achromatic agency site using one large chromatic object (gradient or illustration) as the sole color moment against warm white', 'business': 'Bureau Cool'}
- {'why': 'Editorial print sensibility applied to web — large display type, hairline dividers, grid-paper project cards, ghost navigation links', 'business': 'Pentagram'}

## Agent Prompt Guide

**Quick Color Reference**
- Text: #1d1d1d
- Background: #e5e4e0 (Parchment)
- Elevated surface: #ffffff
- Border: #bfbebe
- Accent: iridescent gradient sphere only (linear-gradient(255deg, rgb(250, 203, 14), rgb(240, 107, 168) 30%, rgb(120, 186, 230) 65%, rgb(255, 255, 255)))
- primary action: no distinct CTA color

**Example Component Prompts**
1. **Display Headline**: 103px Ataero Retina OB weight 400, line-height 0.80, letter-spacing 1.34px, #1d1d1d on #e5e4e0 canvas. All caps. Stacks into a 3-line typographic block.

2. **Ghost Text Link**: 15px Ataero Retina OB weight 400, #1d1d1d, no fill, 10px border-radius on hit area, trailing → arrow. 5px vertical padding. Underline on hover.

3. **Section Label**: 11px Ataero Retina OB weight 400, #1d1d1d, all caps, letter-spacing 0.55px, left-aligned. 76px space below before body content begins.

4. **Client Logo Cell**: White (#ffffff) rectangle, 0px radius, no border, no shadow. Logo centered at 60% width in #1d1d1d. Arranged in 2 rows × 5 columns with 1px #bfbebe hairlines between cells.

5. **Hero Gradient Sphere**: 600px circle, linear-gradient(255deg, #facb00, #f06ba8 30%, #78bae6 65%, #ffffff), positioned right-of-center, partially behind display headline. No border, no shadow, sits as background layer.

## Gradient System

The iridescent sphere gradient is a singleton, not a system. It appears exactly once on any given page — in the hero — and never repeats as a smaller accent, button gradient, or section background. The 255deg angle is fixed: yellow (rgb 250,203,14) at the top-right, pink (rgb 240,107,168) at 30%, blue (rgb 120,186,230) at 65%, dissolving to white at the end. This is the only color event in an otherwise achromatic system; treating it as a reusable token would dilute its impact.

## Typography Voice

Ataero Retina OB Edition is a custom font — not available on Google Fonts or Adobe Fonts. For prototypes and mockups, the closest open substitute is Inter at tight tracking, but production pages must license the original. The font's character: tall x-height, geometric construction with subtle humanist warmth in the terminals, generous counters. At display sizes (70–103px) it reads as architectural; at body sizes (15–18px) it reads as editorial print. The 0.80 line-height on display sizes is unconventional — most systems use 1.0–1.2 — but here it allows headlines to stack into a single visual mass rather than airy separate lines.
