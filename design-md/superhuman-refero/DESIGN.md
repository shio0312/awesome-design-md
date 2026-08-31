# Superhuman — Design System

> **North Star**: golden hour editorial dashboard
> **Theme**: light
> **Source**: https://superhuman.com
> **Refero Style**: https://styles.refero.design/style/418b374a-be64-44f0-b17e-1d45308c7e62
> **Synced**: 2026-09-01

## Overview

Superhuman sits at the intersection of editorial photography and software UI — a warm parchment canvas (never pure white) frames deep-maroon brand moments and vivid violet accents. Headlines whisper at weight 460 rather than shout, letting the cinematic full-bleed hero photograph do the emotional heavy lifting while translucent product UI cards float like glass over the image. The palette stays quiet and editorial most of the time: cream surfaces, charcoal text, hairline warm-gray borders, and generous spacing, with color reserved for deliberate brand punctuation — a single maroon CTA, violet links, a light-lilac secondary button. The system deliberately avoids heavy shadows and gradients on UI surfaces; depth comes from layered photography and subtle backdrop blur on the header, not from elevation stacks.

## Color Palette

- **Midnight Wine**: `#421d24` — Primary action buttons, announcement banner, footer — a warm near-black maroon that reads as ink rather than red, anchoring the palette without screaming [brand]
- **Royal Violet**: `#714cb6` — Violet text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Lilac Mist**: `#d4c7ff` — Secondary surface fills, light-tinted badges, ghost button backgrounds — desaturated violet that hints at the brand accent without claiming focus [accent]
- **Deep Lagoon**: `#0c4243` — Dark band section background for feature storytelling — the only dark surface in the system, paired with overlaid geometric art [accent]
- **Warm Parchment**: `#f2f0eb` — Page canvas — the dominant surface; warm cream that replaces white as the base, giving the whole system an editorial warmth [neutral]
- **Soft Mist**: `#e3e3e2` — Hairline borders, card outlines, divider lines — warm light gray that disappears against parchment but defines edges crisply [neutral]
- **Ink Charcoal**: `#292827` — Primary text, headings, icon strokes — warm near-black with just enough brown to feel like ink on paper, never a cold #000 [neutral]
- **Stone Gray**: `#666666` — Secondary body text, helper copy, muted descriptions — the only mid-gray, used sparingly so it never competes with primary text [neutral]
- **Paper White**: `#ffffff` — Elevated card surfaces, floating UI overlays, text on dark backgrounds — reserved for cards that must lift off the parchment canvas [neutral]

## Typography

- **Super Sans VF**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.2 |
| label-bold | 19 | — | 1.5 |
| subheading | 26 | — | 1.3 |
| heading-sm | 28 | — | 1.14 |
| heading-lg | 49 | — | 1.2 |
| display | 64 | — | 0.96 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 64-96px
- **Border Radius**: {'tabs': '8px', 'cards': '16px', 'pills': '999px', 'buttons': '16px', 'small-buttons': '8px', 'floating-cards': '16px'}

## Layout

Hero is full-bleed photograph with overlaid centered headline (48-64px/460) and a single wine-filled CTA, with floating translucent product UI cards composited over the photo on left and right margins. Below the hero: a white-band logo strip (6 cells in a single row, max-width contained), then a suite-tabs section with white card surface on parchment canvas. A dark teal band breaks the rhythm roughly two-thirds down the page — full-bleed, two-column (art left, text right), creating the only tonal contrast in the scroll. A gradient atmospheric band follows. Section spacing runs 64-96px vertically. Content max-width is ~1200px centered, with hero and dark band breaking out to full viewport width. Navigation is a single sticky header with backdrop blur; no sidebar, no mega-menu. The footer is full-bleed maroon with multi-column link layout. Overall rhythm: photographic hero → quiet white/cream content → dark feature band → atmospheric gradient → maroon footer, alternating light and dark bands to create editorial pacing.

## Surfaces / Elevation

- **Parchment Canvas**
- **Paper Card**
- **Lilac Wash**
- **Deep Lagoon Band**
- **Wine Ground**

## Imagery

Cinematic photography is the primary visual asset — a full-bleed portrait shot against an open sky anchors the hero, with a second atmospheric band lower in the page. Treatment is warm, golden-hour, slightly desaturated, shot at profile angle to feel editorial rather than corporate. The dark feature band layers translucent geometric rectangles and handwritten script overlays over a photo of a person in thought — a collage of surfaces, not a single image. Product UI is presented as floating glass cards composited directly over photography rather than as isolated screenshots. No stock illustration, no 3D renders, no abstract decorative shapes outside of the gradient atmospheric band. Icons throughout are minimal monochrome line icons at ~16-20px, single-weight stroke matching the 460 text weight.

## Design Principles

### Do

- Use weight 460 for all headlines at 28px and above — it is the system's signature voice, not a default
- Set body text to #292827 on #f2f0eb canvas, never on pure #ffffff for full-page backgrounds
- Use #421d24 as the single primary action fill; do not introduce a second chromatic button color
- Reserve #714cb6 exclusively for inline links — never use violet as a button fill, badge, or icon stroke
- Float product UI cards at 16px radius over photographic backgrounds with no drop shadow; let the photo provide depth
- Apply backdrop-filter blur(12px) to the header when content scrolls underneath; reveal a 1px #e3e3e2 border on scroll
- Keep letter-spacing tight on display sizes (-0.028em at 64px, -0.027em at 49px) and zero on body text 16px and below

### Don't

- Do not use weight 700 or higher for headlines — the system speaks at weight 460, not 700
- Do not place white surfaces directly on white; the canvas is parchment (#f2f0eb), cards are white (#ffffff) only when they need to lift
- Do not add drop shadows to cards — depth comes from layering, not elevation stacks
- Do not introduce a blue, green, or red accent color; the accent palette is maroon + violet + lilac only
- Do not center body copy longer than two lines — left-align headlines and descriptions for editorial rhythm
- Do not use pure #000000 for text — Ink Charcoal (#292827) keeps the system warm
- Do not apply the dark teal (#0c4243) to anything other than full-bleed feature bands; it is not a card or component background

## Components

### Primary Action Button

Background #421d24 (Midnight Wine), text #ffffff at 16px/weight 460, border none. Radius 16px. Padding 12px horizontal, height ~48px. Often paired with a small arrow icon at 8px gap to the right of the label. The maroon fill is the ONLY chromatic button fill in the system — everything else is ghost, outlined, or lilac.

### Ghost Text Button

Background transparent, text #292827 (Ink Charcoal), no border, no radius. Underline may appear on hover. Padding 0. Used for nav items, inline learn-more links, and low-emphasis actions that should not compete with primary buttons.

### Outlined Light Button

Background #d4c7ff (Lilac Mist), text #292827, border 1px #292827. Radius 8px. Padding 6px 16px. Lighter weight alternative to the wine filled button; the lilac fill signals secondary rather than tertiary because it still carries brand hue.

### Pill Announcement Banner

Background #421d24, text #ffffff, radius 999px on left and right but clipped to page edges. Padding 12px 16px. Contains a small icon left, inline copy, and a bordered learn-more link. Sits flush at the very top of the viewport above the header.

### Floating Product Card

Background #ffffff at ~85% opacity, radius 16px, padding 16px, border 1px solid rgba(255,255,255,0.2). No drop shadow — depth comes from being composited over the photo. Hosts a small avatar/icon row, body text, and a subtle action affordance. These cards are the system's signature compositional move.

### Trust Logo Card

Background #ffffff, border 1px #e3e3e2, radius 0 (square cell in a grid row, no individual rounding). Padding 24px vertical. Logo centered, rendered in #292827 monochrome. Arranged in a single horizontal row of 6 cells.

### Suite Tab Strip

Four equal-width tabs in a horizontal row, background #ffffff, radius 8px on outer container, no individual tab radius. Padding 16px per tab. Active tab gets #d4c7ff (Lilac Mist) fill with a small chromatic icon; inactive tabs are white with #292827 monochrome icons.

### Suite Product Card

Background #ffffff, radius 16px, padding 16px. Contains a colored icon top-left, product name, body text, and a violet ("Learn more") link at #714cb6. No shadow — sits on parchment so the card edge is defined by the border contrast alone.

### Navigation Header

Background transparent with backdrop-filter blur(12px) and a 1px #e3e3e2 bottom border that fades in on scroll. Logo left, nav links center (weight 460, 16px), auth controls right ("Contact sales", "Log in" as ghost, "Sign up" as lavender outlined). Height ~64px.

### Dark Feature Band

Background #0c4243 (Deep Lagoon). Full-bleed. Left half hosts layered translucent geometric rectangles with handwritten script overlays. Right half hosts white headline (64px/460), white body text at #ffffff, and a white-outlined "Read our announcement" button. The only dark surface in the system, used sparingly for tonal contrast.

### Gradient Banner

Background uses a layered composition of radial gradients: violet glow at 68%/50%, blue glow at 93%/50%, pink glow at 50%/98%, cyan glow at 50%/75%, all at 50-60% opacity. Headline #292827 at 48px/460 left-aligned. White "Get Superhuman" button right-aligned. The gradients are decorative atmosphere, not interactive surfaces.

### Footer

Background #421d24 (Midnight Wine), text #ffffff for headings and #ffffff at ~70% opacity for body. Radius none. Padding 64px top/bottom. Multi-column link layout (Products, Resources, Company, Legal). No social icons row visible in data but footer nav depth suggests 25 interactive elements across columns.

### Link with Underline

Color #714cb6 (Royal Violet), no underline by default, underline appears on hover with 0.2s ease transition. Font weight 460, same size as surrounding body (16px). The violet is the only chromatic text in the system and is reserved exclusively for links.

### Section Heading

Font Super Sans VF weight 460, size 48px, line-height 0.96, letter-spacing 0, color #292827. Anti-convention: weight 460 at 48px reads as confident rather than thin because the warm parchment canvas provides enough contrast for the light cut to remain legible. No text-transform, no italic, no decorative flourishes.

## Similar Design Systems

- {'why': 'Same editorial-meets-product aesthetic with restrained typography, generous spacing, and a single neutral canvas that lets content breathe', 'business': 'Notion'}
- {'why': 'Shared playful-but-premium tone with violet accent on warm neutral, full-bleed cinematic imagery, and floating translucent UI cards over photography', 'business': 'Arc Browser'}
- {'why': 'Same weight-460-at-large-sizes headline approach and preference for hairline borders over heavy shadows, though Linear is dark-first and Superhuman is light-first', 'business': 'Linear'}
- {'why': 'Similar editorial gradient atmospheric bands and the pattern of compositing floating UI mockups over gradient backgrounds rather than flat color', 'business': 'Stripe'}
- {'why': 'Shared warm cream canvas + maroon brand moment pairing, with color reserved for deliberate punctuation rather than applied across the UI', 'business': 'Causal'}

## Agent Prompt Guide

**Quick Color Reference**
- canvas: #f2f0eb
- text: #292827
- secondary text: #666666
- border: #e3e3e2
- card surface: #ffffff
- accent/link: #714cb6
- primary action: #d4c7ff (filled action)
- lilac accent surface: #d4c7ff
- dark band: #0c4243

**Example Component Prompts**

1. Create a Primary Action Button: #d4c7ff background, #292827 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. *Suite product card*: White surface (#ffffff) on parchment canvas (#f2f0eb), radius 16px, padding 16px. Colored icon top-left (16px). Product name at 19px weight 700 #292827. Body text at 16px weight 460 #292827, two lines max. "Learn more" link at 16px weight 460 #714cb6, underline appears on hover at 0.2s ease. No drop shadow.

3. *Primary nav header*: Sticky top bar, height 64px, background transparent with backdrop-filter blur(12px). Logo at left in #292827. Center nav links at 16px weight 460 #292827 with 32px horizontal gap. Right side: "Contact sales" as ghost text button, "Log in" as ghost, "Sign up" as lilac outlined button (background #d4c7ff, text #292827, border 1px #292827, radius 8px, padding 6px 16px). 1px #e3e3e2 bottom border fades in on scroll.

4. *Dark feature band*: Full-bleed background #0c4243. Two-column layout: left half contains layered translucent geometric rectangles (lavender, blue, pink at 50% opacity) with handwritten script overlay. Right half: 64px Super Sans VF weight 460 #ffffff headline, body text at 16px weight 460 #ffffff at 80% opacity, and a white-outlined ghost button below (border 1px #ffffff, text #ffffff, radius 8px, padding 8px 20px).

5. *Footer*: Full-bleed background #421d24, padding 64px top and bottom, max-width 1200px content centered. Four-column link layout with white column headings at 14px weight 700, link items at 14px weight 460 #ffffff at 70% opacity with 12px vertical spacing. No dividers between columns.
