# Cosmos — Design System

> **North Star**: Linen gallery wall with floating polaroids
> **Theme**: light
> **Source**: https://cosmos.so
> **Refero Style**: https://styles.refero.design/style/eb804e3a-1b75-446c-8374-114bbabaf0cd
> **Synced**: 2026-09-01

## Overview

Cosmos is a gallery-wrapped canvas for visual discovery: a warm cream background (#f7f5f3) that reads like unprimed linen, black ink typography, and a strict monochrome UI where color only intrudes through user-curated imagery. The product believes in restraint — the chrome is invisible so the images can shout. Type is a single custom serif-influenced face (cosmosOracle) pulled tight with negative tracking, using weight 350 for hero copy to create editorial softness rather than marketing aggression. Surfaces are flat with a single signature radius (16px) repeated across cards, inputs, and video containers. The hero scatters image tiles in a free-form collage that frames centered copy, and the rest of the page settles into a three-column grid of image-led feature cards. There are no gradients, no shadows beyond what the collage cards cast naturally, and no chromatic accents in the interface itself.

## Color Palette

- **Linen Canvas**: `#f7f5f3` — Page background — warm off-white, never pure #ffffff at the root, gives the interface a paper-like, gallery-wall base [neutral]
- **Ink Black**: `#0d0d0d` — Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color; Borders, dividers, outlined button strokes — used at low opacity to create subtle structural lines, always Ink Black rather than a separate gray [neutral]
- **Paper White**: `#ffffff` — Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color [neutral]
- **Stone**: `#6e6a69` — Body text, secondary icons, inactive UI — warm mid-gray for body copy and supporting metadata [neutral]
- **Pebble**: `#9a9796` — Muted helper text, disabled states, tertiary icon strokes — lightest readable gray in the neutral ramp [neutral]

## Typography

- **cosmosOracle**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.29 |
| heading-sm | 24 | — | 1.2 |
| heading | 33 | — | 1.1 |
| heading-lg | 38 | — | 1.08 |
| display | 58 | — | 1.06 |
| display-xl | 74 | — | 0.8 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 16px
- **Element Gap**: 24px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '16px', 'inputs': '16px', 'buttons': '16px', 'imageTiles': '12px', 'videoContainer': '16px'}

## Layout

Page is centered with a ~1280px max-width content well, though the hero uses full-bleed positioning for the scattered image tiles. The hero is a centered text stack: eyebrow ('COSMOS') → 74px headline → two-button row, all vertically and horizontally centered while image tiles float around the periphery at varied rotations. Below the hero, the video container spans the full content width at 16px radius. The feature row is a strict 3-column grid with 24px gap, each cell leading with an image and trailing with a 18px label. Navigation is a single floating pill bar that hovers near the top of the viewport on every page, containing logo, two text links, centered search, theme toggle, and Login/Sign up — it never duplicates into a secondary bar. Vertical rhythm between sections is generous (80px+), giving each band room to breathe like separate gallery rooms.

## Surfaces / Elevation

- **Linen Canvas**
- **Paper White**

## Imagery

Imagery is the product, not decoration. The hero scatters small cropped image tiles (60–140px) at 12px radius around the centered text like polaroids pinned to a gallery wall. The three feature cards lead with edge-to-edge photography and collage — vivid red florals, warm beige bag silhouettes, and moody purple portraiture — each carrying the only chromatic color in the interface. The video container uses a cinematic still (green-tiled interior, soft focus) with a 9-dot loading animation overlaid in white. There are no illustrations, no abstract graphics, no 3D renders. Icons are minimal stroked linework in Ink Black, used sparingly (magnifier, play triangle, sun/moon, social glyphs). Photography style across the collage feels curated and editorial: high contrast, varied subjects, no unified color treatment — the variety is the point.

## Design Principles

### Do

- Use only Linen Canvas (#f7f7f5f3) as the root background — never pure white at the page level; white is reserved for cards and inputs.
- Apply 16px border-radius to every container, button, and input — this is the single signature radius of the system.
- Set hero and display copy at weight 350 with letter-spacing between -0.04em and -0.05em; do not bold headlines above 400.
- Pair every primary filled button with an outlined secondary at identical padding and radius so they read as a set.
- Let user imagery carry all chromatic content; the UI palette stays at black/white/cream/gray.
- Use 24px gaps between grid cards and 16px padding inside cards as the default content rhythm.
- Position the nav as a single floating pill with 9999px radius at the top of every page.

### Don't

- Do not introduce accent colors (red, blue, green) into interface chrome — color belongs only in user content.
- Do not use weights above 500 in cosmosOracle; the face is not designed for bold display and will feel chunky.
- Do not apply shadows to cards or buttons; the system is deliberately flat and relies on radius and surface contrast.
- Do not set body text larger than 18px or below 14px; cosmosOracle was sized for a tight 14–18px body range.
- Do not mix border-radius values within a single page (avoid 8px or 24px radii) — 16px is the rule, 12px only for image tiles.
- Do not use pure #000000; always #0d0d0d so the black warms against the cream canvas.
- Do not place colored backgrounds behind text; all text sits on Linen Canvas, Paper White, or directly on imagery.

## Components

### Primary Filled Button

Ink Black (#0d0d0d) fill, Paper White (#ffffff) text, cosmosOracle weight 500, 16px font-size, 16px border-radius, 16px vertical / 24px horizontal padding. Tight, pill-like but squared at the radius. No shadow, no border.

### Secondary Outlined Button

Paper White (#ffffff) fill, 1px Ink Black border at ~15% opacity, Ink Black text, 16px radius, 16px/24px padding. Identical sizing to the primary button so they pair as a two-button row.

### Pill Navigation Bar

A single horizontal pill containing the logo (8-dot cluster glyph), Explore / Careers links, centered search input, and Login / Sign up. Background is Paper White with subtle border, 9999px radius, hovers just below the top edge of the viewport with no shadow.

### Search Input

Borderless text input with a leading magnifier icon, placeholder 'Search Cosmos...' in Stone (#6e6a69). Transparent fill so it sits flush inside the nav pill. 16px text, weight 400.

### Floating Image Tile

User-content image cropped to ~12px border-radius, floating at slight rotations or in a loose grid around the hero text. No caption, no border, no shadow — the image is the component. Sized 60–140px, positioned absolutely around the centered headline.

### Feature Image Card

Large image-first card with a 16px radius. The image fills the card edge-to-edge; below it sits a cosmosOracle weight 400 label at 18px (e.g. 'By color'). No visible border, no shadow, no background color — the image defines the card. Three cards sit in a 3-column grid with 24px gap.

### Video Container

A 16px-radius container spanning the page max-width, holding a video poster with a 9-dot loading animation overlaid in white at center. Split text overlay: 'Watch' left-aligned and 'the film' right-aligned at 38px weight 350, with a play triangle between. Small caption 'featuring Odessa Azion' centered near the bottom.

### AI Content Detection Overlay

Paper White surface with 12px radius, ~280px wide, positioned top-right inside a feature card. Title 'AI content' in Ink Black 16px weight 500, body 'Content detected as likely generated by AI' in Stone 14px. Below: three text buttons — 'Show' (Ink Black, 16px radius, white fill), 'Blur' (neutral), 'Hide' (neutral).

### Text Link with Play Icon

Inline at 18px weight 400, Ink Black, preceded by a small triangle play icon. No underline by default; subtle color shift on hover. Used for tertiary navigation cues that should not compete with the button row.

### Theme Toggle

A small icon-only button (sun/moon glyph) at the right edge of the nav pill, before the Login/Sign up cluster. 32×32px hit area, no visible border, 9999px radius on hover background.

### Eyebrow Label

cosmosOracle weight 500, 15–16px, tracked at 0em, rendered as 'COSMOS' above the hero headline. Sets the editorial tone: small, all-caps, almost a stamp rather than a label.

### Dot Cluster Logo

Eight small black dots arranged in a 3×3 grid with the center dot removed, reading as a tiny flower or asterisk. Always Ink Black on Linen Canvas, always at ~18px in the nav, larger at marketing contexts.

## Similar Design Systems

- {'why': 'Same warm cream canvas, monochrome UI that stays out of the way of user-curated imagery, and an editorial single-typeface approach to a visual bookmarking product', 'business': 'Are.na'}
- {'why': 'Image-led grid systems and the philosophy that color belongs to user content, not the interface chrome', 'business': 'Pinterest'}
- {'why': 'Gallery-wall aesthetic with floating image tiles, minimal text UI, and a single warm neutral background that frames rather than competes with photography', 'business': 'VSCO'}
- {'why': 'Portfolio-first visual discovery tools that use restrained typography and generous whitespace to let creator imagery dominate', 'business': 'Cargo (cargo.site)'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #0d0d0d (Ink Black)
- background: #f7f5f3 (Linen Canvas)
- surface/card: #ffffff (Paper White)
- muted text: #6e6a69 (Stone)
- border: #0d0d0d at 10–15% opacity
- primary action: no distinct CTA color

**3-5 Example Component Prompts**
1. *Hero headline*: Center a 74px cosmosOracle weight 350 headline in #0d0d0d with letter-spacing -3.7px and line-height 0.80. Above it place a 15px weight 500 'COSMOS' eyebrow in Ink Black, tracked at 0. Below place a two-button row: a filled Ink Black button with white 16px text at weight 500, 16px radius, 16px/24px padding, beside a white outlined button with 1px Ink Black border at 12% opacity, identical radius and padding. All on a #f7f5f3 canvas.

2. *Feature image card*: A 3-column grid card with 16px radius, edge-to-edge image filling the card (no padding around the image), and a 18px cosmosOracle weight 400 label in Ink Black below the image at 16px top spacing. No border, no shadow. Gap between cards: 24px.

3. *Floating image tile (hero collage)*: A 100px square user-content image with 12px border-radius, positioned absolutely with a slight 2–4° rotation, no border, no shadow, sitting on the Linen Canvas around the hero text. No caption.

4. *Video container*: A full-width (within 1280px max) 16:9 container with 16px radius, holding a photographic poster image. Overlay a 3×3 grid of 8 white dots (center removed) at 60% opacity in the center. Place 'Watch' left-aligned and 'the film' right-aligned at 38px weight 350 in white, with a small white play triangle between them. Small 14px caption 'featuring …' centered near the bottom in white at 70% opacity.

5. *AI content overlay*: A 280px wide Paper White (#ffffff) card with 12px radius, positioned top-right of a feature image. Title 'AI content' in 16px weight 500 Ink Black, body text 'Content detected as likely generated by AI' in 14px Stone. Three text buttons below: 'Show' as a small filled Ink Black button (16px radius, white text, 8px/16px padding), 'Blur' and 'Hide' as neutral text buttons in Stone.

## Typography Signature

The defining typographic choice is using a whisper-weight (350) serif at display sizes. Most modern product sites reach for 600–800 on hero copy; Cosmos goes the other way, letting the serif's high stroke contrast and tight tracking carry authority without volume. The negative letter-spacing scales aggressively with size (-0.05em at 74px, 0 at 14px), which is what makes the large headlines feel architectural rather than decorative. When recreating pages, never substitute a bold sans for the display — the soft serif is the entire brand voice.

## Image-First Component Rule

Cosmos is a visual product, so the component system intentionally limits UI chrome and lets images do the work. The rule: if a component is not navigation, input, or a button, it is probably an image card with a small text label. Resist building dashboards, tables, or data-dense UI; this system is for galleries, feeds, and discovery surfaces where the image is the unit of value.
