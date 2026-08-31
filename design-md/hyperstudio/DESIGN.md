# Hyperstudio — Design System

> **North Star**: blueprint scratched into obsidian. Type and hairline borders carve white space from pure black, with the occasional gold compass-mark to show the way.
> **Theme**: dark
> **Source**: https://hyperstudio.org
> **Refero Style**: https://styles.refero.design/style/8eb9c53e-d69c-497a-b640-610856cf3a60
> **Synced**: 2026-09-01

## Overview

Hyperstudio runs on a near-black canvas where everything is carved out by light. The aesthetic is editorial-tech: a deep matte black background (#101010), crisp off-white type (#f3f3f3), hairline 1px borders (#212121), and the occasional warm gold or signal-green dot for punctuation. Typography does the heavy lifting — oversized 400-weight headlines with aggressive negative tracking create a quiet, confident voice, never shouting. Components are reduced to their skeleton: outlined buttons, ghost pills, thin dividers, no shadows, no fills beyond a single white pill for primary actions. The whole system feels like a wireframe rendered in light on obsidian — restrained, precise, and deliberate.

## Color Palette

- **Obsidian**: `#101010` — Page canvas, full-bleed dark background [neutral]
- **Carbon**: `#080808` — Deepest surface level, hero band, and overlay backgrounds [neutral]
- **Chalk**: `#f3f3f3` — Primary text, headings, and body copy on dark surfaces [neutral]
- **Smoke**: `#9c9c9c` — Secondary muted text, captions, helper labels [neutral]
- **Ash**: `#c1c1c1` — Mid-weight borders, subtle dividers, tertiary text [neutral]
- **Graphite**: `#212121` — Primary 1px border color for cards, grids, and section dividers — the structural line work [neutral]
- **Iron**: `#474747` — Secondary border and stroke detail [neutral]
- **Signal White**: `#ffffff` — Filled pill buttons (LET'S CHAT, START NOW), inverted text on light surfaces, icon strokes — the single high-contrast action color [brand]
- **Compass Gold**: `#6f6759` — Outlined icon strokes in service and portfolio sections — warm metallic against the cool dark [accent]
- **Card Slate**: `#3b3d45` — Card and panel border accent on elevated sections [neutral]

## Typography

- **Aeonik**
- **Input**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 2.69 |
| body | 16 | — | 1.25 |
| heading-xs | 18 | — | 1.31 |
| subheading | 21 | — | 0.95 |
| heading-sm | 23 | — | 1.07 |
| heading | 34 | — | 1.03 |
| heading-lg | 44 | — | 1.07 |
| display | 63 | — | 1.05 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32-48px
- **Element Gap**: 20-24px
- **Section Gap**: 120-210px
- **Border Radius**: {'tags': '4px', 'cards': '8px', 'icons': '99px', 'buttons': '9999px (pills)'}

## Layout

Full-bleed Obsidian canvas, content constrained to a 1200px max-width centered column. Hero is a centered headline stack with a dot-map world graphic spanning the full viewport width below. Sections are separated exclusively by 1px Graphite horizontal dividers — no alternating bands, no background shifts. The services section uses a 2×2 grid inside a bordered frame. The 'Why Hyperstudio?' block is a narrow centered column. Navigation is a transparent top bar with no sticky behavior visible. Spacing is generous — 120–210px between sections — creating a slow, editorial vertical rhythm rather than a dense product layout.

## Surfaces / Elevation

- **Obsidian Canvas**
- **Carbon Depth**
- **Hairline Grid**

## Imagery

Near-zero photography. The only imagery is the dot-matrix world map on the hero — white circular dots on black forming continents through density alone. No product shots, no team photos, no client logos as photography. Icons are the only recurring graphic motif: thin 1.5px outlined strokes in Compass Gold or Chalk, geometric and minimal (pen, book, monitor, waveform). The visual system treats whitespace and type as the primary content; imagery is decorative atmosphere, not explanatory.

## Design Principles

### Do

- Use weight 400 for all headings — never bold. Scale and tracking carry hierarchy, not weight.
- Separate every section with a 1px #212121 hairline rule. No background color shifts between sections.
- Use 9999px radius only on filled white pill buttons. Everything else stays at 4px or 8px.
- Set display type at 63px Aeonik weight 400 with letter-spacing -0.69px. This is the voice of the system.
- Use #6f6759 Compass Gold exclusively for icon strokes — never for text or backgrounds.
- Apply a Pulse Green (#98ff38) dot only for live/active status indicators like availability counts.
- Keep all body text in #9c9c9c Smoke. Never use pure #808080 — the slight warm tilt matters.

### Don't

- Never add drop shadows. Elevation comes from hairline borders and color contrast alone.
- Never use bold or semibold weight on display type. Weight 400 at 63px IS the headline.
- Never use a colored fill behind text. The canvas stays Obsidian or Carbon throughout.
- Never use fully rounded corners on cards. 8px maximum — the system is architectural, not soft.
- Never place icons in any color other than Compass Gold or Chalk. No blue, no green, no multicolor.
- Never use photography as hero or section content. Dot-maps, icons, and type are the only visuals.
- Never break the 1200px content column. Full-bleed is reserved for the canvas and the dot-map graphic.

## Components

### White Pill Button (Primary Action)

Solid white (#ffffff) fill, Obsidian (#101010) text, 9999px border-radius, 12px 24px padding, Aeonik 14px weight 400 uppercase. Small icon or arrow glyph right-aligned. No shadow — contrast alone creates elevation.

### Ghost Outline Button (Secondary)

Transparent background, 1px white (#ffffff) border, white text, 8px radius (not fully pill), 10px 20px padding, Aeonik 14px weight 400 uppercase. Used for VIEW WORK and similar secondary flows.

### Status Badge (Pill)

Dark card background (#1a1a1a), 1px Graphite (#212121) border, 4px radius, 8px 14px padding. Small Pulse Green (#98ff38) dot prefix. Text in Aeonik 12px weight 400, Smoke (#9c9c9c) color, uppercase tracking.

### Service Card (2×2 Grid Cell)

Transparent background, 1px Graphite (#212121) border on bottom and sides (no top border to merge with section divider). Compass Gold (#6f6759) outlined icon at top-left, 32px. Heading in Aeonik 14px weight 400 uppercase Chalk (#f3f3f3), body in Aeonik 14px weight 400 Smoke (#9c9c9c). 48px padding all sides.

### Portfolio Card

No background fill, 1px Graphite (#212121) border or divider line, 8px radius. Small outlined client icon centered, client name in Aeonik 16px weight 400 Chalk, category label in Input 13px uppercase Smoke. Tight vertical padding 24px.

### Section Divider Line

1px solid Graphite (#212121) stroke spanning full content width. The single most repeated visual element — it IS the page structure. No gradients, no fades, no decorative breaks.

### Top Navigation Bar

Transparent background floating over Obsidian canvas. Left: 'Hyperstudio' wordmark in Aeonik 18px weight 400 Chalk. Center-left: nav links (SERVICES, PORTFOLIO, PROCESS) in Aeonik 14px weight 400 uppercase Smoke with 24px gaps. Right: outlined 'LET'S CHAT' pill button. 1px Graphite bottom border.

### Headline Display Block

Aeonik 63px weight 400 Chalk (#f3f3f3), line-height 1.05, letter-spacing -0.69px. Centered or left-aligned. No color, no decoration — the size and tracking do all the work. Followed by a compact sub-headline in Aeonik 21px weight 400 Smoke.

### Dot-Map World Graphic

Full-width illustration of a world map composed of small white (#f3f3f3) circular dots on the Obsidian canvas. No stroke, no fill — just dot density defining continents. Serves as atmospheric proof of global reach without literal photography.

### Manifesto Text Block

Max-width 600px centered. Aeonik 23px weight 400 Chalk for the section title, Aeonik 16px weight 400 Smoke for body paragraphs, generous 24px line-height. Ghost outline 'READ MANIFESTO' button below.

### Outlined Icon Set

1.5px stroke, no fill, Compass Gold (#6f6759) or Chalk (#f3f3f3) color, 24–32px size. Geometric and minimal — pen nib, open book, monitor, waveform. The gold tint against black gives them a compass-rose quality.

### Footer / Bottom Bar

1px Graphite top border, transparent background. Small Aeonik 14px Chalk text for email (hello@hyperstudio.org), Input 13px Smoke for secondary links. No background fill, no padding beyond 32px vertical.

## Similar Design Systems

- {'why': 'Same near-black canvas with large-weight-400 type and the world-is-our-canvas dot/illustration energy', 'business': 'Resn'}
- {'why': 'Dark-mode studio site with oversized quiet headlines, minimal UI chrome, and editorial section spacing', 'business': 'Active Theory'}
- {'why': "Obsidian background, Aeonik-adjacent geometric sans, ghost-outline buttons, and the 'wireframe in light' visual philosophy", 'business': 'Locomotive (studio)'}
- {'why': 'Editorial typography discipline — weight 400 at 63px, aggressive negative tracking, sections divided by hairline rules rather than color bands', 'business': 'Pentagram'}
- {'why': 'Dark agency site with single-color icon system, generous section gaps, and type as the dominant visual element', 'business': 'Ueno'}

## Agent Prompt Guide

primary action: no distinct CTA color
## Quick Color Reference
- Canvas: #101010
- Primary text: #f3f3f3
- Muted text: #9c9c9c
- Border: #212121
- Icon stroke: #6f6759
- Primary action (filled pill): #ffffff background with #101010 text

## Example Component Prompts
1. **Hero headline block**: Obsidian (#101010) background. Headline at 63px Aeonik weight 400, color #f3f3f3, letter-spacing -0.69px, line-height 1.05. Below it a filled white pill button (#ffffff fill, #101010 text, 9999px radius, 12px 24px padding, Aeonik 14px uppercase) labeled 'START NOW ↗'.

2. **Service grid cell**: Transparent background, 1px bottom border in #212121. Compass Gold (#6f6759) outlined icon at 32px top-left. Heading in Aeonik 14px weight 400 uppercase #f3f3f3, 16px margin-top. Body in Aeonik 14px #9c9c9c, 8px line-height increase.

3. **Status pill badge**: Background #1a1a1a, 1px #212121 border, 4px radius, 8px 14px padding. Pulse Green (#98ff38) 6px dot prefix. Text in Aeonik 12px uppercase #9c9c9c, letter-spacing 0.5px.

4. **Section divider**: Full-width 1px solid #212121 line, 0 margin top and bottom — the line IS the layout.

5. **Manifesto block**: Centered, max-width 600px. Title at 23px Aeonik weight 400 #f3f3f3. Body at 16px Aeonik weight 400 #9c9c9c, line-height 1.5. Ghost outline button below: transparent fill, 1px #ffffff border, 8px radius, #ffffff text, Aeonik 14px uppercase.
