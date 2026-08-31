# Harness.io — Design System

> **North Star**: midnight mission control with phosphor-green accents
> **Theme**: dark
> **Source**: https://gitness.com
> **Refero Style**: https://styles.refero.design/style/6f3652cf-583f-411d-a117-3a03f6342917
> **Synced**: 2026-09-01

## Overview

Harness's Gitness surface reads as a nocturnal command deck: near-black canvas (#070707) with stacked card surfaces in marginally lighter shades, oversized display headlines in a condensed Calsans face with positive tracking, and a teal/mint accent (#70dcd3) that surfaces on highlight cards like a phosphor monitor glow. The page stays quiet and high-contrast — white text at AAA contrast on deep neutrals, hairline borders in light gray (not dark) to define edges against the dark canvas, and pill-shaped controls (800px radius) that feel like physical hardware buttons. Color is rationed: one bright blue (#0092e4) for active link borders and one mint (#70dcd3) for accent cards, nothing else. Spacing breathes — generous card padding, comfortable section gaps, and large display sizes that let the type carry the hierarchy rather than color or weight.

## Color Palette

- **Void Canvas**: `#070707` — Page background, deepest surface — near-black, the floor everything else sits on [neutral]
- **Carbon Plate**: `#0d0e12` — Primary card surface, one step above the canvas — the dominant elevated panel [neutral]
- **Obsidian**: `#141418` — Secondary card surface, code blocks, nested panels [neutral]
- **Iron Edge**: `#2e3038` — Mid-tier surface, dividers, hover overlays on dark surfaces [neutral]
- **Steel Border**: `#22222a` — Heavy structural borders, button outlines on dark, nav separators [neutral]
- **Pure White**: `#ffffff` — Primary text, filled pill button fill, icon strokes — the only high-luminance neutral [neutral]
- **Cloud Mist**: `#f0f0f0` — Secondary text, soft fills, muted surface highlights [neutral]
- **Fog**: `#d9dae5` — Card hairline borders — counterintuitively light on the dark canvas, defining card edges by luminosity contrast [neutral]
- **Ash**: `#c8cad0` — Body text secondary, muted descriptions, helper text [neutral]
- **Graphite**: `#aeaeb7` — Tertiary body text, subdued labels, disabled-ish state [neutral]
- **Slate Mute**: `#a2a4a9` — Nav borders, inactive nav text, structural dividers in chrome [neutral]
- **Cinder**: `#60606c` — Deep muted text, low-priority links, icon rest state [neutral]
- **Phosphor Mint**: `#70dcd3` — Accent card fill, highlight surfaces — the signature brand glow, reserved for featured cards and stat panels [accent]
- **Signal Blue**: `#0092e4` — Link borders, active link text, focus accents — the interface's action stroke [brand]
- **Ice Blue**: `#a6e5f2` — Decorative soft borders, light accent strokes on cards [accent]
- **Current Blue**: `#00ade4` — Active nav state, selected menu items, current-page indicator [brand]
- **Deep Signal**: `#0677d4` — Input focus border, form active state, info semantic stroke [semantic]
- **Verdant Edge**: `#75ae4c` — Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Use as a supporting accent, not as a status color [accent]
- **Steel Iris**: `#929dbd` — Card decorative borders with cool blue-gray tint, secondary card outlines [accent]

## Typography

- **Geist**
- **Calsans**
- **Helvetica**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.22 |
| body-sm | 14 | — | 1.44 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.5 |
| heading-sm | 32 | — | 1.1 |
| heading | 56 | — | 1.1 |
| heading-lg | 72 | — | 1 |
| display | 88 | — | 0.96 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 16px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '20px', 'badges': '800px', 'inputs': '5px', 'buttons': '800px', 'nestedCards': '16px'}

## Layout

Max-width 1200px centered content. Hero is split 50/50: headline and subtext left-aligned, 3D visual bleeding to right edge. Subsequent sections are full-bleed dark bands with centered content. Feature sections alternate between 2-column text+visual layouts and centered headline + card grid. Card grids are typically 2-3 columns with 20-24px gaps. Section gaps are generous (64-80px). Navigation is a single sticky top bar, no sidebar. The page rhythm is: dark hero → dark feature section → dark accent section → dark footer — it never breaks from the dark theme.

## Surfaces / Elevation

- **Void Canvas**
- **Carbon Plate**
- **Obsidian**
- **Iron Edge**

**Shadow tokens:**

## Imagery

Hero and feature sections use 3D-rendered product visuals: curved tracks, flowing light ribbons, abstract geometric objects lit with neon edge-light. These renders sit on dark gradient grounds (linear-gradient from rgb(22,48,82) to rgb(13,14,18)) and blend seamlessly into the #070707 canvas. No photography, no flat illustration — the visual language is CGI/dimensional. Icons in the UI are minimal and appear as simple line glyphs in #ffffff or muted grays. The only flat content imagery is the activity feed with circular avatars and status dots.

## Design Principles

### Do

- Use Calsans for all headlines at 56px or larger with its native positive tracking (0.056em)
- Define card edges with a 1px #d9dae5 light border, not shadows or background contrast alone
- Use the filled white pill (800px radius, #ffffff fill, #070707 text) for the single primary action on any screen
- Apply the Phosphor Mint (#70dcd3) accent to no more than one card or panel per viewport
- Use 20px radius for cards and 800px (pill) for all interactive controls
- Keep body text at 16px Geist weight 400 with -0.017em tracking; use weight 500 only for emphasized labels
- Anchor all dark surfaces to the Void Canvas (#070707) as the base; stack upward through #0d0e12 → #141418

### Don't

- Don't use drop shadows on cards or panels — the system defines elevation through light borders and surface luminance steps
- Don't fill buttons with color — the only filled button is white, everything else is ghost/outlined
- Don't use multiple accent colors in one section — Phosphor Mint and Signal Blue should not co-occur on the same surface
- Don't set body text below 14px or above 18px — the reading range is narrow and confident
- Don't apply negative letter-spacing to Calsans — its positive tracking is structural to the typeface's identity
- Don't use dark borders on cards; the system uses light (#d9dae5) borders to define edges on dark surfaces
- Don't break the dark theme with light sections — the entire page lives in the dark spectrum

## Components

### Hero Headline (Calsans Display)

Calsans weight 300 at 88px/0.96 line-height, color #ffffff, letter-spacing 0.056em (~4.9px). The positive tracking on massive type is signature — headlines feel like instrument panel readouts, not editorial. Two-tone color treatment on hero: 'The End-To-End' in pure white, with a secondary line optionally in Phosphor Mint (#70dcd3) for the opening phrase.

### Filled Pill Button (Primary)

Background #ffffff, text #070707, border-radius 800px (full pill), padding 12px 24px, font Geist 500 at 16px. Dark text on white fill — the inversion of the dark interface makes the button physically pop. Subtle inset highlight: rgb(255,255,255) inset shadows on the top/sides create a light edge against the white fill, giving the pill a slightly embossed quality.

### Ghost Pill Button (Secondary)

Transparent background, border 1px solid #ffffff, text #ffffff, border-radius 800px, padding 12px 24px, Geist 400 at 16px. The border is bright white at full opacity — the button's identity comes from the outline, not the fill.

### Dark Surface Card

Background #0d0e12, border 1px solid #d9dae5 (light border on dark surface), border-radius 20px, padding 24px. The counterintuitive light border defines the card edge against the dark canvas — this is the system-defining move. No shadow; the border is the elevation.

### Phosphor Accent Card

Background #70dcd3 (the mint), no border or subtle #d9dae5 border, border-radius 20px, padding 24px. Used sparingly — one per viewport maximum. The teal fill makes the card look lit from within, like a phosphor screen.

### Code/Syntax Surface

Background #141418 (Obsidian), border-radius 16px, padding 16-20px, Geist Mono (or Geist fallback) at 13-14px, text #aeaeb7 with syntax highlighting. Sits nested inside Carbon Plate cards.

### Navigation Bar

Background #070707 (transparent over canvas), height ~64px, logo left, links centered in Geist 14px, #ffffff text with #a2a4a9 for inactive items, border-bottom 1px solid #a2a4a9 (again, light borders on dark). Right side: contact link + filled pill CTA. Sticky, no background blur needed against solid dark canvas.

### Activity Row (PR/Commit List)

Horizontal row: avatar circle (32px) + commit message in Geist 14px weight 500 (#ffffff) + metadata in Geist 12px (#aeaeb7) + status dot (8px circle) in Phosphor Mint (#70dcd3) for pass, Verdant Edge (#75ae4c) for success, or a warm tone for warning. Padding 10px 0, separated by 1px #2e3038 dividers.

### Input Field

Background #0d0e12, border 1px solid #2e3038 (rest) or #0677d4 (focus), border-radius 5px, padding 12px, text Geist 14px #ffffff, placeholder #60606c. Focus adds a 1px Deep Signal border — no glow ring, just a sharp color change.

### Status Badge

Border-radius 800px (pill), padding 2px 8px, Geist 11-12px with 0.042-0.094em tracking. Variants: success = border 1px #75ae4c with text #75ae4c, info = border 1px #0677d4 with text #0677d4. Outlined style, never filled.

### Section Header (Eyebrow + Title)

Eyebrow label in Geist 12px uppercase with 0.094em tracking, color #a6e5f2 or #929dbd, above a Calsans heading at 56px/1.1 weight 300. The uppercase eyebrow with wide tracking is the section's quiet signal.

### 3D Product Visual Block

Full-bleed rendered product imagery with neon-lit 3D objects on a dark gradient ground. The image is not a flat screenshot — it has dimensional lighting, glowing edges, and a horizon line. Blends into the #070707 canvas with no hard mask.

### Footer Link Column

Column heading in Geist 14px weight 500 #ffffff, links in Geist 13-14px weight 400 #aeaeb7 with no underline. 8-16px vertical gap between items. Four-column grid with generous column gaps (32-40px).

## Similar Design Systems

- {'why': 'Same near-black canvas, high-contrast white text, pill-shaped controls, and minimal use of color as functional punctuation rather than decoration', 'business': 'Linear'}
- {'why': 'Dark-mode devtools aesthetic with geometric sans display type, generous spacing, and a single accent color used sparingly', 'business': 'Vercel'}
- {'why': 'Deep dark surfaces with a distinct teal/green accent for featured elements, and light hairline borders defining card edges on dark backgrounds', 'business': 'Supabase'}
- {'why': 'Near-black canvas with stacked neutral surface levels, pill controls, and a restrained palette where color appears only as small functional accents', 'business': 'Railway'}
- {'why': 'Dark devtools surface with oversized display type, white pill CTAs on dark backgrounds, and quiet use of a single accent color', 'business': 'Resend'}

## Agent Prompt Guide

**Quick Color Reference**
- canvas: #070707
- card surface: #0d0e12
- primary text: #ffffff
- secondary text: #aeaeb7 / #c8cad0
- border: #d9dae5 (light on dark)
- accent: #70dcd3 (mint)
- link/active: #0092e4 (blue)
- primary action: #ffffff (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #ffffff background, #070707 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Feature Card Grid**: 3-column grid on #070707 background, 20px gaps. Each card: background #0d0e12, border 1px solid #d9dae5, border-radius 20px, padding 24px. Icon in #70dcd3 at 24px. Title in Calsans 32px weight 300, color #ffffff, letter-spacing 0.056em. Body in Geist 16px weight 400, color #aeaeb7.

3. **Activity Feed Row**: Background #0d0e12 card with 1px #d9dae5 border, 20px radius. Each row: 32px circular avatar + Geist 14px weight 500 text in #ffffff + Geist 12px metadata in #aeaeb7 + 8px status dot in #70dcd3. Rows separated by 1px #2e3038 dividers. Row padding 10px 0.


5. **Footer Link Grid**: 4-column grid on #070707 background. Column headers in Geist 14px weight 500, #ffffff. Links in Geist 14px weight 400, #aeaeb7, no underline. 12px row gap, 40px column gap. Bottom bar: copyright in Geist 13px #60606c, social icons (32px) in #a2a4a9.
