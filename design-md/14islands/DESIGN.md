# 14islands — Design System

> **North Star**: Monochrome editorial gallery — A pristine gallery wall where oversized black typography and full-bleed photography exist without decoration, color, or UI noise.
> **Theme**: light
> **Source**: https://14islands.com
> **Refero Style**: https://styles.refero.design/style/139c4bee-396d-494c-baf0-fe211bf4928d
> **Synced**: 2026-09-01

## Overview

14islands operates as a gallery space for digital work: pure white canvas, near-black text, and a single mid-gray for quiet secondary information. The visual hierarchy is built entirely through scale — display type swells to 180px while body text stays at a disciplined 16px, creating a 10× relationship that feels editorial rather than digital. Components are barely there: hairline borders, 4px corners, no shadows, no chromatic color anywhere in the interface. Photography and full-bleed dark media blocks carry the visual weight that color would in a more conventional system. The single design device that breaks the monochrome discipline is the lighter-gray ampersand or category label — a whisper of contrast that structures typographic relationships without adding hue.

## Color Palette

- **Ink**: `#070707` — Primary text, display headlines, full-bleed dark media blocks, nav wordmark — the single near-black that anchors every interface [neutral]
- **Paper**: `#ffffff` — Default canvas, card surfaces, text on dark sections [neutral]
- **Fog**: `#f2f2f2` — Subtle surface differentiation for alternating sections or inset panels — barely visible, used to create quiet separation without borders [neutral]
- **Stone**: `#a2a2a9` — Secondary text, category labels, decorative ampersand, muted button text — the entire chromatic-like hierarchy comes from this one gray [neutral]
- **Graphite**: `#797979` — Muted body text, helper copy, tertiary metadata — deeper than Stone for occasional emphasis on small text [neutral]

## Typography

- **BentonSans**
- **AftenScreen**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.2 |
| body | 16 | — | 1.4 |
| subheading | 27 | — | 1.3 |
| heading | 75 | — | 1 |
| heading-lg | 100 | — | 0.8 |
| display | 180 | — | 0.8 |

## Spacing & Layout

- **Max Width**: 1400px
- **Card Padding**: 20-25px
- **Element Gap**: 5-10px
- **Section Gap**: 100-160px
- **Border Radius**: {'tags': '4px', 'cards': '4px', 'inputs': '4px', 'buttons': '4px'}

## Layout

Full-bleed page canvas with no persistent side margins on the outermost sections. Top navigation spans edge-to-edge. The display headline bleeds across the full viewport width. Section rhythm is: short typographic intro → full-bleed media block → grid of case studies → typographic transition. The case study grid is a strict 2-column layout (10-25px gaps) that always reads as pairs, never as a 3+ column matrix. Vertical breathing room is extreme (100-160px between major sections) — the layout is generous and editorial, never information-dense.

## Surfaces / Elevation

- **Paper**
- **Fog**
- **Ink**

## Imagery

Photography is the only visual medium beyond type. Case study images are high-production editorial photography — fashion, lifestyle, product, and luxury — often full-bleed with no treatment overlay. Portrait-oriented crops for people, product crops for objects. Full-bleed video blocks in Ink act as movement punctuation. The aesthetic is gallery-curated, not stock — every image looks commissioned. No illustrations, no abstract graphics, no decorative shapes. The interface itself is the negative space; imagery is the content.

## Design Principles

### Do

- Use only the five neutral tokens — Ink, Paper, Fog, Stone, Graphite. Never introduce chromatic color.
- Set display type at 75-180px with line-height 0.80-1.00 and letter-spacing -0.04em; weight stays at 400.
- Keep all border-radius at 4px — for cards, buttons, tags, inputs, and image frames.
- Maintain a 10× scale ratio between body (16px) and display (180px) to preserve editorial hierarchy.
- Use Stone (#a2a2a9) for the ampersand, category labels, and any secondary text — never for body paragraphs.
- Space major sections with 100-160px vertical padding; element gaps stay in the 5-25px compact range.
- Render case study images edge-to-edge with no border, no radius, no shadow — the image is the card.

### Don't

- Do not introduce any color — no blue, red, green, or accent hue of any kind.
- Do not use shadows, glows, or any CSS box-shadow. Depth comes from scale and contrast only.
- Do not use border-radius above 4px — the 4px value is the ceiling, not the floor.
- Do not use display type at body sizes. AftenScreen under 50px should be paired with lower line-height to feel intentional, not just oversized body text.
- Do not use bold or semibold weights for emphasis — weight 400 + size does all the work.
- Do not fill buttons with Ink as a primary action. The system has no filled button; navigation and CTAs are text-only.
- Do not use 3+ column grids for case studies. The layout is always pairs.

## Components

### Top Navigation Bar

Full-bleed white bar, 16px BentonSans. Three-zone layout: wordmark "14islands" left-aligned in Ink, nav links (WORK, SERVICES, CULTURE, JOURNAL, AI) center-aligned and spaced, CONTACT right-aligned. No background fill, no border, no shadow. Links are Ink at 16px; CONTACT carries the same weight and color but sits in the right zone to read as a soft CTA through position, not styling.

### Uppercase Eyebrow Tag

BentonSans 12px, Stone (#a2a2a9), uppercase, letter-spacing slight. Two-line block with a label (e.g. "CREATIVE AGENCY") over a short sentence. Functions as the quiet lead-in to any major section. No background, no border.

### Display Headline Block

AftenScreen 180px, weight 400, line-height 0.80, letter-spacing -0.04em, color Ink. Can span one or two lines; ampersand or connecting words rendered in Stone (#a2a2a9) as a typographic device. No max-width constraint on the type itself — it bleeds to the viewport edges, reading as a poster rather than a paragraph.

### Case Study Card

Two-column grid (gap 25px row / 10px column). Image fills card edge-to-edge with no radius. Below image: project name in AftenScreen ~27px Ink, followed by em-dash and category label in Stone BentonSans 16px. No card background, no border, no shadow — the image IS the card surface.

### Full-Bleed Media Block

Rectangular block, 100% viewport width, 0px radius, Ink (#070707) background. Typically hosts video or oversized photography. Sits between text sections as a visual breather. No overlay, no caption within the block — context lives above and below in surrounding text.

### Section Heading (Lighter)

AftenScreen 100px, weight 400, line-height 0.80, color Stone (#a2a2a9). Appears as a quiet alternative to the full-strength Ink display — used for transition sections ("Lovable Products / from vision to launch") where the content is still introducing itself.

### Nav Link (Ghost)

BentonSans 16px, weight 400, color Ink (top nav) or Stone (footer). No underline by default, no background. On hover: opacity shift or color transition to Stone. The link IS the button — there is no filled alternative.

### Footer

Ink (#070707) background, Paper (#ffffff) text. BentonSans 16px body, 12px caption for fine print. Spacious padding (54-100px vertical). No social icons styled prominently — links live as text only.

## Similar Design Systems

- {'why': 'Same monochrome editorial aesthetic, oversized display type, and case-study-as-poster card grid with no border-radius beyond 4px', 'business': 'Locomotive'}
- {'why': 'Full-bleed video blocks, white canvas, single-font type system where scale alone drives hierarchy', 'business': 'Active Theory'}
- {'why': 'Creative agency portfolio with extreme typographic scale, no chromatic palette, and full-bleed media as section dividers', 'business': 'Resn'}
- {'why': 'Near-identical monochrome discipline, display-serif-on-white-canvas presentation, and gallery-style project grid', 'business': 'DIA Studio'}
- {'why': 'Editorial-agency restraint with large display type, minimal UI chrome, and photography carrying all the color and visual weight', 'business': 'Pentagram'}

## Agent Prompt Guide

## Quick Color Reference
- Background: #ffffff
- Surface (subtle): #f2f2f2
- Primary text / dark block: #070707
- Secondary text / decorative: #a2a2a9
- Muted helper text: #797979
- Border / hairline: #070707 at 0.1 opacity, or #a2a2a9
- primary action: no distinct CTA color

## Example Component Prompts

1. **Build the top navigation bar**: Full-bleed white bar with three zones. Left: wordmark "14islands" in AftenScreen weight 400 at 16px, color Ink (#070707). Center: nav links (WORK, SERVICES, CULTURE, JOURNAL, AI) in BentonSans 16px Ink with 42px gap between items. Right: CONTACT in BentonSans 16px Ink. No background, no border, no shadow. Padding 20px top and bottom.

2. **Build a case study card (2-column grid)**: Edge-to-edge image at 4px radius, no border. Below the image, 20px gap, then project name in AftenScreen 27px weight 400 Ink. On the same line after the name: em-dash then category label in BentonSans 16px Stone (#a2a2a9). The card has no background fill and no shadow.

3. **Build a display headline section**: Full viewport width. AftenScreen 180px weight 400, line-height 0.80, letter-spacing -0.04em, color Ink. Place the ampersand "&" in Stone (#a2a2a9) at the same size. Section padding: 108px top, 160px bottom.

4. **Build a full-bleed media block**: 100% viewport width, 0px radius, Ink (#070707) background, 4:3 or 16:9 aspect ratio. Place it directly after a typographic section, with 100px gap above and below. No overlay, no caption inside the block.

5. **Build a transition heading section**: Stone-colored secondary headline. AftenScreen 100px weight 400, line-height 0.80, color #a2a2a9. Two lines, second line can be a sub-line at 27px BentonSans 16px Graphite. Background Paper, padding 100px vertical.
