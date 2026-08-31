# Steep — Design System

> **North Star**: serif analytics on warm paper
> **Theme**: light
> **Source**: https://steep.app
> **Refero Style**: https://styles.refero.design/style/75fdb89f-ca64-41b3-af36-7a78bd09448e
> **Synced**: 2026-09-01

## Overview

Steep renders analytics as editorial — serif Signifier headlines float over a near-monochrome white canvas while a single warm peach accent (#fbe1d1) punctuates an otherwise achromatic system. The page reads like a product magazine spread: oversized italicized display type, generous breathing room, large soft-edged cards at 24px radius, and pill-shaped controls that sit flat against the surface. Components feel quiet and weightless — shadows are barely-there, borders are hairline, and color is rationed to functional emphasis (a peach callout card, a dark brown label on peach). The product surfaces (region tables, activation charts, AI composers) are presented as floating artifacts around the headline, not nested in a dashboard shell.

## Color Palette

- **Ink Black**: `#17191c` — Primary text, filled button background, nav logo — the only dark surface in the system; every CTA and body headline resolves to this near-black [neutral]
- **Paper White**: `#ffffff` — Page canvas, button text, elevated card surfaces — the dominant background tone carrying ~76 frequency points [neutral]
- **Mist Gray**: `#f2f2f3` — Card surfaces, secondary backgrounds, input fills — the quiet layer beneath paper for nested content [neutral]
- **Fog White**: `#fafafb` — Secondary page background for alternating sections, hover surfaces — one step above paper for subtle band variation [neutral]
- **Slate Gray**: `#777b86` — Link color, muted helper text, footer copy — cool desaturated gray that sits between body text and disabled [neutral]
- **Ash Gray**: `#979799` — Tertiary labels, category tags (Marketing, Finance, Sales) — one step lighter than link color [neutral]
- **Smoke Gray**: `#a3a6af` — Placeholder text (Ask anything…), disabled labels — the lightest functional gray, used when text recedes [neutral]
- **Blush Peach**: `#fbe1d1` — Accent card background, warm highlight wash — the only chromatic surface in the system; creates editorial warmth against monochrome [accent]
- **Sienna Brown**: `#5d2a1a` — Text and stroke on peach surfaces, dark accent for chart line strokes — a warm deep brown that pairs with Blush Peach like ink on kraft paper [accent]

## Typography

- **Signifier**
- **Sohne**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 15 | — | 1.5 |
| body | 17 | — | 1.35 |
| body-lg | 20 | — | 1.35 |
| subheading | 22 | — | 1.5 |
| heading-sm | 26 | — | 1.18 |
| heading | 44 | — | 1.3 |
| heading-lg | 64 | — | 1.3 |
| display | 90 | — | 1.3 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 20px
- **Element Gap**: 8px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '24px', 'images': '12px', 'inputs': '16px', 'buttons': '9999px', 'smallCards': '16px', 'elevatedCards': '20px'}

## Layout

Page model is max-width 1200px centered, with hero sections going near full-bleed but staying within the container. The hero pattern is a centered oversized serif headline with a subhead and pill button pair, surrounded by four floating product artifact cards (region table top-left, registration card right, activation chart bottom-left, AI composer bottom-center) that overlap the white canvas at varied offsets. Sections alternate between Paper White and Card Mist backgrounds to create quiet rhythm without strong contrast. Feature sections use a 2-column text+UI layout with generous 80px vertical gaps. Navigation is a single transparent top bar (no background, no border, no shadow) with logo left, nav links center, and two CTAs (text link + filled pill) right. The overall density is spacious — the page breathes between sections, and content never crowds the edges.

## Surfaces / Elevation

- **Canvas**
- **Card Mist**
- **Section Fog**
- **Accent Blush**
- **Elevated White**

**Shadow tokens:**

## Imagery

Imagery is product-first, not lifestyle: floating UI fragments (region tables with 5-row data, line charts showing activation over Aug–Nov, radial progress rings, AI input composers) are positioned as cropped screenshots around editorial headlines. No photography, no illustration, no abstract graphics. All product visuals sit on white floating-artifact cards with hairline borders and soft 10% shadows. Avatar circles carry a small directional cursor pointer — a visual motif that signals live interaction. The hero composition is a text-and-UI collage, not a centered headline with a stock photo.

## Design Principles

### Do

- Use Signifier weight 400 at 44/64/90px for all display and heading copy; never substitute a sans-serif at these sizes
- Use the peach #fbe1d1 card surface at most once per page and only for editorial emphasis — treat it as a rare accent, not a background
- Set border-radius to 9999px on all buttons and 24px on all content cards; these are the two structural radii of the system
- Pair every filled pill button (#17191c) with a ghost pill button (#17191c border, transparent fill) as a secondary action on the same row
- Use Sohne half-step weights (430, 450, 480) for body hierarchy before reaching weight 500 — the scale is finer than standard 400/500/700
- Set letter-spacing to -0.025em on 90px display, -0.015em on 64/44px headings, and -0.009em on 26/18px Sohne — tighter tracking at larger sizes is the typographic signature
- Keep the 4px base unit: use 4/8/12/16/20/24px for component padding, and 80px for section gaps

### Don't

- Don't use chromatic colors beyond the peach/brown pair — the system is intentionally 97% achromatic; introducing blue, green, or purple will break the editorial restraint
- Don't use bold (600+) or semibold (500) weights in Signifier — the serif stays at 400 across all sizes, that restraint is the signature
- Don't apply drop shadows to content cards (Neutral Card or Accent Peach Card) — only floating product artifacts earn elevation
- Don't use border-radius below 16px on cards or below 9999px on buttons — sharp corners and moderate radii are not part of this system
- Don't underline inline text links at rest — the arrow suffix (→) carries the link affordance; underlines appear only on hover
- Don't place the peach #fbe1d1 card on a non-white section background — it needs Paper White or Card Mist beneath it to read as warm-on-neutral
- Don't use the #5d2a1a Sienna Brown outside peach surfaces — it's the ink for Blush Peach cards and chart strokes, never body text on white

## Components

### Pill Button — Filled

Background #17191c, text #ffffff, border 1px solid #ffffff (invisible against fill), border-radius 9999px (fully rounded), padding 0 20px, height auto with text. Sohne 16px weight 400. No shadow. The pill shape and dark fill against white is the signature action element — it reads as a solid black lozenge.

### Pill Button — Ghost

Background transparent, text #17191c, border 1px solid #17191c, border-radius 9999px, padding 0 20px. Sohne 16px weight 400. Shares the pill geometry with the filled variant so they read as a matched pair on the same baseline.

### Text Link with Arrow

No background, no border, no border-radius, text #17191c, Sohne 16px weight 400, padding 20px 0. The arrow glyph (→) is part of the label, not a separate icon. This is the lowest-emphasis interactive element — underlines only on hover.

### Nav Link

No background or border, text #17191c, Sohne 16px weight 400, padding 2px 0. Sits in a transparent top bar with the logo left and CTAs right. The nav is whisper-quiet — no background, no shadow, no separator.

### Neutral Card

Background #f2f2f3, border-radius 24px, no shadow, no border, padding varies (0 internally with content children providing their own padding). This is the default workhorse card — flat, soft, and quiet.

### Accent Peach Card

Background #fbe1d1, text and strokes #5d2a1a, border-radius 24px, no shadow, no border. The warm-on-warm palette creates a kraft-paper effect — these cards should be rare (one per page maximum) to preserve their impact.

### Floating Product Artifact

Background #ffffff, border-radius 20px, subtle box-shadow: 0 0 0 1px rgba(4,23,43,0.05), 0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1), padding 16px 20px 12px 12px. These are the product UI fragments that float around hero text — they are the only elements with visible shadow, and only at 10% opacity.

### Input / Composer

Background #ffffff, border 1px solid #ececec or hairline, border-radius 16px, padding 16px, placeholder text #a3a6af in Sohne 16px. Contains left-side @ and ⓘ icons and a right-side dark circular send button (40px diameter, #17191c fill, white arrow icon).

### Stat Card with Chart

White floating artifact surface with a bold metric in Sohne 20px weight 500 #17191c, a delta line (↑ 5.5x vs last week) in Sohne 14px #777b86, and a minimal line or radial chart in #5d2a1a stroke. No axes, no gridlines — the chart is a gestural line, not a data dashboard.

### Avatar Bubble

Circular, 40px diameter, border-radius 9999px, background tinted (light green for JB, light blue for AF), 2-letter monogram in Sohne weight 500, small directional arrow (cursor pointer) extending from the bubble edge.

### Tag / Category Label

No background, no border, text in Sohne 14px weight 400 #979799. Intentionally ghost-like — these are typographic tags, not badges. They group without visual weight.

## Similar Design Systems

- {'why': "Same monochrome dark-text-on-white approach with oversized serif-free type and pill-shaped CTAs; Linear's restraint matches Steep's editorial minimalism", 'business': 'Linear'}
- {'why': 'Presentation tool that pairs serif display headlines with a warm accent palette and floating UI cards; shares the editorial-product hybrid visual language', 'business': 'Pitch'}
- {'why': 'Browser with a soft warm-toned monochrome interface, generous border-radius on cards, and the same whisper-quiet typography approach', 'business': 'Arc'}
- {'why': 'Large serif headlines floating over white with minimal chrome and pill controls; shares the magazine-spread page architecture', 'business': 'Framer'}

## Agent Prompt Guide

## Quick Color Reference
- text: #17191c
- background: #ffffff
- border: #ececec
- muted text: #777b86
- accent: #fbe1d1
- primary action: #17191c (filled action)

## Example Component Prompts
1. **Hero headline + accent card collage**: White canvas (#ffffff). Display headline at 90px Signifier weight 400, #17191c, letter-spacing -2.25px, with one italicized phrase mid-sentence. Subhead at 17px Sohne weight 400, #777b86. Below: a filled pill button (background #17191c, text #ffffff, border-radius 9999px, padding 0 20px, Sohne 16px) and a ghost pill button (background transparent, border 1px solid #17191c, text #17191c, border-radius 9999px) side by side. Surround the text with three white floating product artifact cards: a data table card, a line chart card, and a stat card — each with background #ffffff, border-radius 20px, box-shadow 0 0 0 1px rgba(4,23,43,0.05) + 0 20px 25px -5px rgba(0,0,0,0.1), positioned with negative margins to overlap the text margins.

2. **Accent editorial card**: Background #fbe1d1, text #5d2a1a, border-radius 24px, no shadow, padding 40px. Title at 26px Sohne weight 450, #5d2a1a, letter-spacing -0.23px. Body quote at 18px Sohne weight 430, #5d2a1a. Attribution at 14px Sohne weight 400, #5d2a1a. Place this card once on a #ffffff section, never on a colored or dark background.

3. **Neutral feature card**: Background #f2f2f3, border-radius 24px, no shadow, padding 32px 20px. Category label at 14px Sohne weight 400, #979799 (no background, no badge style). Title at 20px Sohne weight 500, #17191c. Body at 16px Sohne weight 400, #17191c, line-height 1.5. Text link below: Sohne 16px weight 400, #17191c, no border-radius, padding 20px 0, with → arrow suffix.

4. **AI composer input**: White background #ffffff, border 1px solid #ececec, border-radius 16px, padding 16px, width 480px. Placeholder text Ask anything… at 16px Sohne weight 400, #a3a6af. Left side: two ghost icon buttons (40px circle, no fill). Right side: 40px circular send button with background #17191c, white arrow icon centered.

5. **Section with alternating background**: Section background #fafafb (Fog White), padding 80px vertical. Section title at 64px Signifier weight 400, #17191c, letter-spacing -0.96px. Subhead at 18px Sohne weight 430, #777b86. Below: 3-column grid of neutral feature cards (#f2f2f3 background, 24px radius, 20px padding, no shadow) with 24px column gap.
