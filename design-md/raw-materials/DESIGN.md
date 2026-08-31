# Raw Materials — Design System

> **North Star**: brutalist editorial on warm cream
> **Theme**: light
> **Source**: https://therawmaterials.com
> **Refero Style**: https://styles.refero.design/style/274e85fb-a34d-4e41-9369-be03065b971b
> **Synced**: 2026-09-01

## Overview

Raw Materials operates as a typographic maximalist system: a warm cream canvas carrying display type that regularly exceeds 200px, with every major surface element given its own vivid color identity. The system abandons a single brand color in favor of seven section-marker hues (orange, violet, ink, cobalt, crimson, yellow, green) that label navigation and content blocks alike, creating a zine-like rhythm where the color tells you which chapter you're in. Surfaces are flat and rounded at 16px — no shadows, no gradients, no elevation. Typography does all the hierarchy work, jumping from 12px captions to 259px display headlines with a cast of four custom typefaces, all sharing the "ss02" stylistic alternate.

## Color Palette

- **Ember Orange**: `#ff3d00` — Orange supporting accent for decorative details and low-frequency emphasis [accent]
- **Pulse Violet**: `#5900cc` — Violet supporting accent for decorative details and low-frequency emphasis. [accent]
- **Cobalt Blue**: `#2835f8` — Violet supporting accent for decorative details and low-frequency emphasis. [accent]
- **Crimson**: `#ff003d` — Red supporting accent for decorative details and low-frequency emphasis [accent]
- **Caution Yellow**: `#ffff00` — Yellow supporting accent for decorative details and low-frequency emphasis. [accent]
- **Voltage Green**: `#05ff00` — Green supporting accent for decorative details and low-frequency emphasis [accent]
- **Electric Blue**: `#1b73e6` — Headings and body text on cream, mid-saturation blue used in content [accent]
- **Sky Cyan**: `#00c2ff` — Headings and accent text, cool counterpoint to warm cream [accent]
- **Forest**: `#008163` — Card fills, moderate green for body-level content blocks [accent]
- **Lime Pulse**: `#3eea5a` — Headings and body, brighter green counterpart to Voltage; Green supporting accent for decorative details and low-frequency emphasis [accent]
- **Tangerine**: `#ff5c00` — Card fills, warm orange variant for content blocks [accent]
- **Signal Red**: `#ee2526` — Red supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color [accent]
- **Ink**: `#0e0e0e` — Dark supporting neutral for text, icons, and strong contrast. [neutral]
- **Bone Cream**: `#f4e9e1` — Primary page canvas, nav text on color blocks, card surface [neutral]
- **Paper White**: `#ffffff` — Active nav card, elevated card surface, input fields [neutral]
- **Charcoal**: `#242320` — Dark surface fill, image overlays, secondary text on light [neutral]
- **Sage**: `#cee4cd` — Tinted section background, warm green wash [neutral]
- **Blush**: `#e4d0cd` — Tinted section background, warm pink wash [neutral]
- **Sand**: `#e7e4d0` — Tinted section background, warm yellow wash, card fill [neutral]
- **Sky Tint**: `#cddae4` — Tinted section background, cool blue wash, image-related surfaces [neutral]
- **Celadon**: `#ddded3` — Tinted section background, muted green wash [neutral]
- **Olive Slate**: `#444639` — Dark olive section background, secondary text [neutral]
- **Forest Slate**: `#374936` — Dark green section background, heading text on light [neutral]
- **Cocoa Slate**: `#4a3937` — Dark warm section background, heading text on light [neutral]
- **Plum Slate**: `#493648` — Dark purple section background, heading text on light [neutral]

## Typography

- **StabilGrotesk**
- **Optimistic Text**
- **KlarheitKurrent**
- **HTQ-Waldenburg-FettSchmal**
- **RightGrotesk**
- **Moderat**
- **Courier New**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.38 |
| body-sm | 14 | — | 1.38 |
| body | 16 | — | 1.38 |
| subheading | 20 | — | 1.2 |
| heading-sm | 24 | — | 1.2 |
| heading | 32 | — | 1.17 |
| heading-lg | 46 | — | 1.14 |
| display | 100 | — | 1.03 |
| display-lg | 200 | — | 1 |
| display-xl | 259 | — | 1 |

## Spacing & Layout

- **Card Padding**: 16-24px
- **Element Gap**: 8-16px
- **Section Gap**: 48-80px
- **Border Radius**: {'cards': '16px', 'pills': '99px', 'badges': '24px', 'images': '16px', 'buttons': '16px', 'nav-blocks': '16px', 'display-shapes': '187px'}

## Layout

Full-bleed layout with no max-width constraint. A fixed left sidebar (~160px) holds the seven numbered section nav cards stacked vertically, each card a different vivid color. The main content area fills the remaining viewport with the warm cream canvas. The hero is a single oversized display headline (200-259px) that bleeds past its container — the type IS the hero, not a background image. A bottom progress bar (Ember Orange) spans the full viewport width. Sections alternate between cream canvas and one of five warm tinted backgrounds (Sage, Blush, Sand, Sky, Celadon) or one of four dark slates, creating a zine-like chapter rhythm. The page model is asymmetric: the sidebar is a permanent anchor while content flows full-width to the right edge.

## Surfaces / Elevation

- **Bone Cream Canvas**
- **Paper White**
- **Tinted Washes**
- **Saturated Color Blocks**
- **Dark Slates**

## Imagery

Primarily typographic and color-block-based — the system treats massive display type itself as the dominant visual. When photography appears (in Work, Talent, Careers sections), it is contained in 16px-radius frames on the cream canvas, never full-bleed, and never given a shadow. No illustrations, no 3D, no decorative graphics — the seven section colors and the display type ARE the visual identity. Iconography is minimal to absent; when present, it is a single-color flat glyph at 16-24px. Image-to-text ratio is low: text dominates, images serve as proof points within color blocks.

## Design Principles

### Do

- Use StabilGrotesk for every interactive element and any type below 80px — it's the only font that touches UI controls
- Set all type to feature-settings: 'ss02' — this stylistic alternate is applied to every font on the site and is part of the visual identity
- Lock display headlines to line-height 1.00-1.03 so the type touches itself vertically
- Use 16px radius for all cards, buttons, images, and nav blocks — never mix in 8px or 4px corners
- Assign each page section one of the seven nav colors and carry that color into its content blocks, badges, and accent type
- Let display headlines bleed past their container — do not constrain them to a max-width
- Alternate between cream canvas and one of the five warm tinted backgrounds (Sage, Blush, Sand, Sky, Celadon) to create section rhythm

### Don't

- Don't add drop-shadows, inner-shadows, or any blur effects — the system is entirely flat
- Don't use a single 'primary' brand color for CTAs — buttons inherit their section's accent color
- Don't set body text below 16px or above 20px — the body range is tight by design
- Don't apply letter-spacing wider than +0.01em to body or subheading text — only the +0.084em Moderat all-caps labels and +0.112em Optimistic uppercase use wide tracking
- Don't introduce a new color outside the seven nav hues and the five tinted washes — the palette is deliberately finite
- Don't use rounded corners smaller than 16px on any container — 4px or 8px corners will read as a different system
- Don't place display headlines centered on the canvas — they are always left-aligned and bleed right

## Components

### Numbered Section Nav Card

Vivid solid-fill card, 16px radius, full width of sidebar (~150px). Two-line layout: tiny '00'–'07' index number in Bone Cream (#f4e9e1) at 12-13px StabilGrotesk 400, then the section label in Bone Cream at 16-18px StabilGrotesk 400. Padding 12-16px vertical, 16px horizontal. One card per section color: Ember Orange, Pulse Violet, Ink, Cobalt Blue, Crimson, Caution Yellow, Voltage Green.

### Active Section Nav Card

Same 16px-radius dimensions as a Numbered Section Nav Card, but filled Paper White (#ffffff) with Ink (#0e0e0e) text. The color inversion reads as 'you are here' without needing an underline or dot indicator.

### Display Headline

100-259px using KlarheitKurrent 400-500 or RightGrotesk 700. Ink (#0e0e0e) on cream, or Bone Cream on a color block. Line-height locked to 1.00-1.03 — the type touches itself. Letter-spacing -0.02em to -0.04em at display sizes. No max-width constraint; type bleeds to the container edge or wraps to 2-3 lines.

### Page Header

Full-width, sits on the cream canvas with ~24px padding. Left: 'Raw Materials' at 17-18px StabilGrotesk 400 in Ink. Right: 'An Unusual Design Company' in the same size and weight, Ink. No logo mark — the wordmark IS the logo. No border, no background fill — type sits directly on cream.

### Scroll Progress Bar

Full-width Ember Orange (#ff3d00) bar, 4-6px tall, fixed to viewport bottom. Fills left-to-right as the user scrolls. Also includes a tiny '01/01' section counter in Ink at 12px StabilGrotesk on the right edge.

### Color Block Content Card

Full-saturation fill in one of the accent colors or dark slates, 16px radius, 24px padding. Content inside is Bone Cream or Paper White type at 16-18px StabilGrotesk 400. No shadow, no border. Often used as a 2-column or 3-column grid element.

### Tinted Section Background

Full viewport-width band in one of the five warm washes: Sage (#cee4cd), Blush (#e4d0cd), Sand (#e7e4d0), Sky (#cddae4), or Celadon (#ddded3). No border between sections — the color shift itself is the divider. 48-80px vertical padding. Type inside is Ink.

### Pill Tag

99.36px radius (full pill), 6-8px vertical padding, 12-16px horizontal. Filled with a section color or Ink, text in Bone Cream or Paper White at 12-13px StabilGrotesk 400.

### Rounded Badge

24px radius (slightly more than fully rounded at small sizes), 4-8px padding. Filled with a section accent color. Text at 12px StabilGrotesk 400 in Bone Cream or Paper White.

### Image Frame

16px radius, no border, no shadow. Image fills the frame edge-to-edge. Sits on cream canvas or inside a Color Block Content Card.

### Ghost Button

Transparent fill, 1.5-2px Ink border (#0e0e0e), 16px radius, 12px 20px padding. Text at 16px StabilGrotesk 400 in Ink. No fill on hover — instead the border thickens to 3px. This is the system default; filled colored buttons only appear in nav.

### Body Text Block

StabilGrotesk 400, 16-18px, line-height 1.38, Ink (#0e0e0e) on cream, or Bone Cream on dark/colored surfaces. Max reading width ~640px even though the container is wider — text doesn't stretch full-bleed.

### Section Index Header

12-14px StabilGrotesk 400 in Ink or Bone Cream, letter-spacing -0.05em. Sits above a display headline, left-aligned, with 8px gap to the headline.

### Link Inline

StabilGrotesk 400 at body size, Ink with a 1px Ink underline. On hover: text color shifts to the accent color of the current section. No color-only differentiation — always underlined.

## Similar Design Systems

- {'why': 'Same maximalist agency approach where each project gets its own typographic identity, with massive display type and bold color blocks on neutral canvases', 'business': 'Pentagram'}
- {'why': 'Same warm cream/neutral canvas with oversized editorial type and section-by-section color shifts; similar Swiss-poster-meets-zine DNA', 'business': 'DIA Studio'}
- {'why': 'Same flat-design agency aesthetic with vivid accent colors on muted warm backgrounds and strong typographic hierarchy', 'business': 'Locomotive (Montreal)'}
- {'why': 'Same Dutch-design confidence in treating type as the primary visual element, with flat surfaces, saturated color blocks, and no decorative shadows', 'business': 'Studio Dumbar'}
- {'why': 'Same numbered-section navigation pattern and warm-paper canvas with bold display type, though with a slightly more restrained color palette', 'business': 'Order Design'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #0e0e0e (Ink)
- background: #f4e9e1 (Bone Cream)
- border: #0e0e0e at 1-1.5px
- accent: section-dependent (Ember Orange #ff3d00, Pulse Violet #5900cc, Cobalt Blue #2835f8, Crimson #ff003d, Caution Yellow #ffff00, Voltage Green #05ff00)
- card surface: #ffffff (Paper White)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Numbered Section Nav Card**: 150px wide, 16px border-radius, fill #ff3d00. Two lines: '01' at 12px StabilGrotesk 400 in #f4e9e1, then 'Hello' at 18px StabilGrotesk 400 in #f4e9e1. 16px horizontal padding, 12px vertical. No shadow.

2. **Display Headline**: 'We are Raw Materials' at 200px KlarheitKurrent 400, #0e0e0e, line-height 1.00, letter-spacing -4px, feature-settings 'ss02'. No max-width — type bleeds right.

3. **Scroll Progress Bar**: Full viewport width, 4px tall, fixed to bottom. Fill #ff3d00. Grows left-to-right with scroll position.

4. **Tinted Section Background**: Full-width band, 80px vertical padding, background #cee4cd (Sage). Contains a 24px StabilGrotesk 400 subheading in #0e0e0e, then 18px body in #0e0e0e at line-height 1.38, max-width 640px.

5. **Ghost Button**: 16px border-radius, 1.5px border #0e0e0e, transparent fill, 12px 20px padding. Text 'View project' at 16px StabilGrotesk 400 in #0e0e0e. On hover: border thickens to 3px, no fill change.

## Color System Logic

The palette is not decorative — it is functional. The seven section colors (Ember Orange, Pulse Violet, Ink, Cobalt Blue, Crimson, Caution Yellow, Voltage Green) map 1:1 to the numbered navigation, so color tells the user which chapter of the site they are in at all times. The five warm tinted washes (Sage, Blush, Sand, Sky, Celadon) are the same idea at lower saturation: they create alternating section backgrounds without introducing new hues. Dark sections use a parallel set of hue-tinted darks (Olive, Forest, Cocoa, Plum) — never pure black, always carrying a subtle color. Every other color on the site is either a variant of one of these, or a one-off illustration color that should not be added to the system.

## Type System Logic

Four display fonts (Optimistic Text, KlarheitKurrent, HTQ-Waldenburg, RightGrotesk) compete at 95-259px — they are NEVER used below 80px, and StabilGrotesk is NEVER used above 46px. This hard split is the system: StabilGrotesk does UI, the display fonts do poster-scale. All five custom fonts share the 'ss02' stylistic alternate, which means the alternate glyph forms are part of the brand voice, not a hidden detail. The Moderat font is reserved for wide-tracked all-caps labels (+0.084em) and is the only font that uses positive letter-spacing meaningfully — it acts as a label/caption voice at display scale.
