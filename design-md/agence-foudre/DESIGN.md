# Agence Foudre — Design System

> **North Star**: Magazine splash page in lipstick pink.
> **Theme**: light
> **Source**: https://www.agencefoudre.com
> **Refero Style**: https://styles.refero.design/style/c1534c74-f7b8-44de-a913-586d0f78fb08
> **Synced**: 2026-09-01

## Overview

Agence Foudre uses a bold editorial-magazine language: warm cream canvas, oversized condensed display type in vivid magenta, and a surprising deep-forest green that reads as both body text and accent. The interface is deliberately sparse — most of the viewport is empty space, and content arrives in dense typographic punches rather than card grids or product visuals. Color is used as emotional punctuation: hot pink screams, faded pink whispers, deep green grounds, and warm off-white softens every surface. Components are minimal — circular pink buttons, pill-shaped badges, and big chunky type are the only chrome. This is a portfolio/expression site, not a product UI: the brand's personality IS the typography and color, everything else stays out of the way.

## Color Palette

- **Lipstick Magenta**: `#db3c8a` — Display headlines, primary brand color, icon buttons, heading accents — vivid pink carries 100% of brand recognition [brand]
- **Forest Ink**: `#00522d` — Body text, links, iconography, footer — deep saturated green against cream creates editorial gravitas no neutral could [brand]
- **Blush Cream**: `#fce5df` — Soft surface tint, badge backgrounds, gentle wash blocks, hover states — warm off-pink that sits between page and accent [neutral]
- **Warm Chalk**: `#fff8f6` — Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color [neutral]
- **Charcoal Black**: `#000000` — High-contrast text, dark icons, line art, SVG fills — used sparingly for maximum punch [neutral]
- **Lilac Mist**: `#d1cfe4` — Decorative type tint, subtle dividers, soft outline strokes — cool gray-lilac for the quietest visual moments [neutral]
- **Bubblegum**: `#f29ebd` — Secondary accent, lighter pink washes, faded display type, ghost button borders — pink dialed back from brand magenta [accent]
- **Cotton Pink**: `#e878b2` — Mid-tone pink surface for elevated cards, tonal accent between magenta and bubblegum [accent]

## Typography

- **Beni**
- **Clash Grotesk**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| micro | 10 | — | 12 |
| label | 12 | — | 14 |
| caption | 14 | — | 17 |
| body-sm | 16 | — | 19 |
| body | 20 | — | 24 |
| subheading | 46 | — | 32 |
| heading-sm | 80 | — | 56 |
| heading | 94 | — | 66 |
| heading-lg | 130 | — | 91 |
| display | 230 | — | 161 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 30px
- **Element Gap**: 15-20px
- **Section Gap**: 120px
- **Border Radius**: {'tags': '9999px', 'cards': '20px', 'badges': '10px', 'buttons': '10px', 'elevated': '25px', 'iconButtons': '9999px'}

## Layout

Full-bleed single-column layout with extreme vertical whitespace. Each section typically owns an entire viewport height, anchored by massive display type at the bottom-left or top-left. Navigation is stripped to two pink circles in the absolute corners — no nav bar, no mega-menu, no breadcrumbs. Content scrolls as a sequence of typographic statements rather than traditional sections: each scroll position delivers one bold message, then vast white space, then the next. No card grids, no multi-column layouts, no sidebar. The page reads like a typographic manifesto: one idea per screen, each rendered at maximum scale. Responsive behavior collapses display type proportionally but preserves the generous spacing and corner-circle navigation.

## Surfaces / Elevation

- **Warm Chalk**
- **Blush Cream**
- **Cotton Pink**

## Imagery

Almost no traditional imagery. The site is a typographic showcase where oversized Beni display type IS the visual content. Where images appear (portfolio pieces, team, or case studies), they are treated as full-bleed editorial crops with no rounded corners, no shadows, no decorative frames — raw photographs presented in rectangular slabs. Any illustrations or graphic elements use the brand palette: hot pink forms, deep green line work, lilac accents. Icons are minimal line-art glyphs in black or green, never filled or colorful. The visual density is inverted: 95% typography, 5% image.

## Design Principles

### Do

- Use Beni weight 900 with 0.70 line-height for all display type — the tight leading is what makes the headlines feel architectural, not just big
- Default to #fff8f6 as the canvas; let #fce5df appear only as a 5-10% accent surface, never as a full page background
- Pair #db3c8a (loud) with #fce5df (whisper) of the same hue to create dialogue between sections — full color makes a statement, faded color echoes it
- Use #00522d for all body text and links — the deep green is a signature choice that no neutral substitute can replicate
- Let whitespace do the structural work: 60-120px section gaps, and let individual display blocks own full viewport heights
- Set all interactive circles (menu, brand) to 50px diameter with full radius and #db3c8a fill — these are the only two dots on the page
- Cap body text width at 60ch regardless of viewport — readability over impact

### Don't

- Never use #000000 for body text — #00522d is the editorial voice; black is reserved for icons and graphic elements only
- Don't set Beni at body sizes (under 30px) — it was designed for display only; use Clash Grotesk for everything functional
- Avoid card-heavy layouts — this system breathes through type and space, not through information density
- Never apply #db3c8a to large body areas — pink is an exclamation, not a wallpaper
- Don't add shadows, gradients, or glass effects — the system is deliberately flat; depth comes from color contrast and typographic scale
- Avoid mixing more than two type families — Beni for display, Clash Grotesk for everything else; no serif, no monospace, no decorative fonts
- Don't use symmetric centered layouts — everything left-aligns or uses deliberate asymmetric placement; the type should feel editorial, not ceremonial

## Components

### Circular Menu Trigger

50px diameter pink circle (#db3c8a), full radius. Contains a three-line hamburger glyph in dark or white. Fixed position top-left. No border, no shadow. The pink circle is the only UI element that breaks the cream canvas

### Circular Brand Mark

50px diameter circle matching menu trigger. Contains the agency mark (lightning bolt variant). Fixed top-right. Same pink fill (#db3c8a), same weight as menu — visual symmetry establishes these as the only two interactive dots on screen

### Display Headline Block

Beni weight 900, sizes 94-230px, line-height 0.70. Color cycles between #db3c8a (full intensity), #f29ebd (mid pink), and #fce5df (faded wash) to create visual rhythm across sections. Left-aligned, bottom-anchored in viewport. No margins — the type itself is the layout

### Faded Echo Headline

Same Beni 900 treatment as main headline but in #fce5df or #f29ebd — appears as a ghost version of a statement the full-color version just made. Creates dialogue between sections. Same massive scale (80-130px)

### Section Label

Clash Grotesk 400-500, 12-14px, uppercase or sentence case. Color: #00522d or faded #db3c8a. Positioned directly above the display headline it describes. Tight tracking, no decoration — just a whispered label

### Pill Badge / Tag

Clash Grotesk 500, 12-14px, #00522d text on #fce5df background. Radius 9999px (fully rounded). Padding 7px 15px. No border. Appears sparingly to tag content without competing with display type

### Body Paragraph

Clash Grotesk 400, 16-20px, line-height 1.20, color #00522d. Max width ~60ch. Generous vertical spacing (30-60px between blocks). The deep green on warm cream is the primary reading experience

### Text Link

Clash Grotesk 500, inherits body size, color #00522d with possible #db3c8a accent. No underline by default; underline appears on hover in #db3c8a. Minimal, confident — the link should feel like a directional gesture, not a button

### Icon Button Ghost

No background, no border. Icon only in #000000 or #00522d, 20-24px. Hover state: icon shifts to #db3c8a. Used for secondary actions where the pink circle buttons are too loud

## Similar Design Systems

- {'why': 'Same editorial-magazine approach where oversized display typography replaces product imagery and layout is radically minimal', 'business': 'Pentagram'}
- {'why': 'Shared commitment to bold custom display type and generous whitespace as the primary structural system', 'business': 'Locomotive (studio)'}
- {'why': 'Experimental agency aesthetic with unconventional navigation (circular triggers) and typographic-first page rhythm', 'business': 'Resn'}
- {'why': 'Creative agency portfolio language using display type as hero content with restrained UI chrome', 'business': 'Buck (studio)'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #00522d
- background: #fff8f6
- border / divider: #fce5df
- accent: #db3c8a
- secondary accent: #f29ebd
- primary action: no distinct CTA color

**Example Component Prompts**
1. Create a hero display block: #fff8f6 background, left-aligned Beni weight 900 at 130px with 0.70 line-height, color #db3c8a. Add a 14px Clash Grotesk 500 label above in #00522d reading the section category.
2. Create a ghost navigation link: no background, no border, Clash Grotesk 500 at 16px in #00522d, hover underline in #db3c8a. Inline within body text, max-width 60ch.
3. Create a circular brand button: 50px diameter, border-radius 9999px, background #db3c8a, containing a black lightning-bolt glyph centered. Fixed top-right position.
4. Create a faded echo headline: Beni weight 900 at 80px, line-height 0.70, color #fce5df. Positioned in a new section to echo a previous #db3c8a statement with reduced intensity.
5. Create a pill category tag: Clash Grotesk 500 at 12px, color #00522d, background #fce5df, border-radius 9999px, padding 7px 15px. No border, no shadow.
