# Anthropic — Design System

> **North Star**: scientific field journal on warm parchment — quiet ivory surfaces, editorial serif headlines, and a single clay accent that only appears when you must act
> **Theme**: light
> **Source**: https://anthropic.com
> **Refero Style**: https://styles.refero.design/style/d469cba4-c448-4a43-a033-883f8bfcdc42
> **Synced**: 2026-09-01

## Overview

Anthropic's interface reads like a curated research publication on warm parchment paper. Ivory and oat neutrals replace the typical cool-gray tech palette, giving every surface a paper-like quality that pairs with a custom serif used at unprecedented scale for both body and display text. A single clay-toned accent surfaces only at moments of action; everything else stays quiet and editorial. Components are flat — hairline borders and selective bottom-corner radii replace shadows as the elevation language, sans-serif handles UI chrome, and the serif carries voice.

## Color Palette

- **Slate Dark**: `#141413` — Primary text, headings, footer background, hairline borders — near-black with a hint of warmth, never pure black [neutral]
- **Ivory Medium**: `#f0eee6` — Page canvas and large surface fills — the parchment background that sets the entire warm tone [neutral]
- **Ivory Light**: `#faf9f5` — Card surfaces, elevated panels, skip-link buttons — one step brighter than canvas for subtle layering without shadows [neutral]
- **Cloud Medium**: `#b0aea5` — Muted helper text, inactive nav items, secondary labels — the neutral that recedes without disappearing [neutral]
- **Cloud Dark**: `#87867f` — Outlined button borders, mid-contrast dividers [neutral]
- **Stone**: `#cccbc8` — Hairline borders and dividers between sections — visible but never assertive [neutral]
- **Slate Medium**: `#3d3d3a` — Dark-on-dark borders inside the footer [neutral]
- **Oat Warm**: `#e3dacc` — Secondary warm surface for grouped panels and feature containers — a deeper paper tone for variety [neutral]
- **Manilla**: `#f5e3c7` — Featured hero card background — vintage paper tone that signals editorial importance without color shouting [neutral]
- **Clay**: `#d97757` — Filled CTA buttons (e.g. cookie consent accept) — the single chromatic accent in the system, a terracotta warmth that belongs to the earth-tone family rather than typical UI blue [brand]
- **Clay Deep**: `#c6613f` — Hover/pressed state for Clay CTAs and the canonical accent token — deeper version of the primary accent [brand]

## Typography

- **Anthropic Serif**
- **Anthropic Sans**
- **Anthropic Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.4 |
| body-sm | 16 | — | 1 |
| body | 20 | — | 1.4 |
| subheading | 24 | — | 1.3 |
| heading | 61 | — | 1.1 |
| display | 68 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 24-32px
- **Element Gap**: 8px
- **Section Gap**: 80-120px
- **Border Radius**: {'nav': '0px', 'cards': '24px', 'links': '0px', 'badges': '0px', 'buttons': '8px (bottom-only on filled variants), 12px (outlined)'}

## Surfaces / Elevation

- **Canvas**
- **Card Surface**
- **Warm Feature Surface**
- **Deep Warm Surface**
- **Inversion Surface**

**Shadow tokens:**

## Imagery

Imagery leans heavily into vintage scientific illustration: the hero feature card contains a dense botanical/zoological collage of butterflies and moths rendered in classic naturalist plate style, evoking 19th-century field guides. Illustrations are warm-toned to harmonize with the parchment background rather than pop against it. No photography, no product screenshots, no abstract gradients. Iconography is minimal — small chevrons for dropdowns and sparse line indicators, always in the same warm-neutral family as text. The visual density is low: large blocks of text and whitespace dominate, with imagery appearing only at hero-feature scale.

## Design Principles

### Do

- Use Anthropic Serif at 20px for all body copy and Anthropic Sans at 12-16px for UI chrome — the serif/sans split defines the system's voice.
- Use #f0eee6 as the page canvas and #faf9f5 for cards; reach for #f5e3c7 only when a card needs to feel like a featured editorial spread.
- Use the bottom-only 8px radius on filled buttons (Filled Ivory Button); this signature corner treatment replaces the generic pill.
- Use #d97757 Clay exclusively for the most consequential single CTA on any given page; never apply it to multiple actions or decorative elements.
- Keep underlines persistent on inline links — editorial print convention, not reveal-on-hover.
- Reach for 24px radius on all card-level surfaces to maintain the paper-stacked feel.
- Use the 61px sans weight 700 paired with the 68px serif weight 400 as the dual display system — sans for declarative statements, serif for editorial reflection.

### Don't

- Don't introduce cool grays, blues, or any color outside the warm earth-tone family — the palette is ivory/oat/clay, period.
- Don't use box-shadow for elevation — this system elevates through surface tone (#f0eee6 → #faf9f5 → #f5e3c7) and 1px borders only.
- Don't use the Clay accent for decoration, icons, hover states, or non-CTA elements; reserve #d97757 for filled action buttons only.
- Don't set body text in sans-serif — body must be serif at 20px; sans is UI chrome only.
- Don't apply uniform border-radius to buttons; the bottom-only 8px is a signature, not a default that should be rounded everywhere.
- Don't use bright white (#ffffff) as a surface — the system is ivory-tinted throughout (#faf9f5, #f0eee6, #f5e3c7); pure white would feel clinical and break the paper metaphor.
- Don't add gradients, glows, or color washes to backgrounds; surfaces are flat solid fills only.

## Components

### Text Link Button

Transparent background, #141413 text color, no border, 0px radius, padding 22px 12px. Underline appears on hover. No background fill at any state — this is text that happens to be clickable, not a container.

### Filled Ivory Button

Background #faf9f5, text #141413, bottom-only border-radius 8px (top corners sharp), padding 12px 31px. The bottom-only radius is a signature choice — the button reads like a tab or card pulled from a stack, not a generic pill. No border, no shadow.

### Outlined Dark Button

Transparent background, #ffffff text, 1px border in #87867f, 12px radius, padding 8px 16px. Compact size, ghost treatment that lets the dark background show through.

### Clay Filled Button

Background #d97757, white text, 8px radius, padding matching Filled Ivory Button proportions. Reserved for moments where acceptance must be visually distinct from the rest of the editorial interface. Deepens to #c6613f on hover.

### Featured Hero Card

Background #f5e3c7 (manilla), 24px border-radius, no shadow, no border. Generous internal padding (~48-64px) to accommodate large serif display text and editorial illustration. The warm paper tone separates it from ivory cards without using color.

### Release Card

Background #faf9f5, 24px radius, 1px border in #cccbc8 or no border, padding ~24px. Title in Anthropic Sans 24px weight 600 or Anthropic Serif 20px, body in serif 20px. Three-column grid layout.

### Top Navigation Bar

Transparent or #f0eee6 background, logo left in Anthropic Sans 12px weight 700 all-caps letter-spaced, nav links right-aligned at 12px sans with #b0aea5 hover-to-#141413 transition. Dropdown indicators as chevrons. The 'Try Claude' button on the right uses Filled Ivory Button styling. No background blur, no shadow.

### Footer

Full-bleed #141413 background, #faf9f5 text, multi-column link grid with 8px link gaps. Section headings in sans 12px weight 600, link items in sans 12px at #b0aea5. The dark footer is the only inversion in the system — a final grounded anchor after all the parchment above.

### Hero Heading Block

Two-column layout: left holds Anthropic Sans 61px weight 700 heading with inline underlined links mid-phrase; right holds supporting serif paragraph at 20px. Generous whitespace around the block. Headings use #141413, supporting text #141413 at reduced visual weight.

### Inline Underlined Link

No background, text inherits parent color (#141413), 1px underline always visible (not just on hover) in #141413. The persistent underline is editorial — it matches print convention where links are typeset with underlines, not the UI convention of reveal-on-hover.

### Badge / Inline Label

Transparent background, #141413 text, 0px radius, no padding above/below the text baseline. Effectively just bold or weighted text in flow — not a container. Used sparingly.

### Cookie Consent Bar

Dark band (#141413 background) or dark overlay containing body text and three action buttons: Filled Ivory Button (Accept), Outlined Dark Button (Customize, Reject). The contrast inversion makes consent legible against the parchment above.

### Skip Link

Background #faf9f5, text #141413, small padding, visible only on focus. Positioned absolutely at the top edge.

## Similar Design Systems

- {'why': 'Same warm parchment neutrals and nature-inspired accent palette, editorial type treatment, and rejection of cold tech-blue UI conventions', 'business': 'Arc Browser'}
- {'why': 'Editorial documentation aesthetic with serif body text paired with sans UI, warm grays instead of cool blues, and section-based max-width reading layout', 'business': 'Stripe'}
- {'why': 'Type-driven minimal interface where typography carries hierarchy more than color or shadow, generous whitespace, restrained palette', 'business': 'Notion'}
- {'why': 'Monochrome restraint and the discipline of using a single accent color only at decisive action moments', 'business': 'Linear'}
- {'why': 'Contemporary AI-product visual language with custom sans + serif type pairing and minimal decorative chrome', 'business': 'Cursor'}

## Agent Prompt Guide

## Quick Color Reference
- text: #141413 (Slate Dark)
- background: #f0eee6 (Ivory Medium)
- card surface: #faf9f5 (Ivory Light)
- border: #cccbc8 (Stone)
- muted text: #b0aea5 (Cloud Medium)
- primary action: #d97757 (filled action)

## Example Component Prompts

1. **Hero section**: Canvas #f0eee6. Left column: headline at 61px Anthropic Sans weight 700, #141413, letter-spacing -0.12px. Inline links within the headline underlined persistently in #141413. Right column: supporting paragraph at 20px Anthropic Serif weight 400, #141413. Two-column layout, max-width 1280px centered, generous vertical padding (~120px top).

2. Create a Primary Action Button: #d97757 background, #141413 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. **Three-column release grid**: Three cards on #f0eee6 canvas, each card #faf9f5 with 24px radius and 24px padding. Card title at 24px Anthropic Sans weight 600, #141413. Card body at 20px Anthropic Serif weight 400, #141413. Inline link at bottom: 'Model details →' in #141413 with persistent underline.


5. **Dark footer**: Full-bleed #141413 background, #faf9f5 text, max-width 1280px content centered. Column headings at 12px Anthropic Sans weight 600, #faf9f5. Link items at 12px sans weight 400, #b0aea5 with 8px vertical gaps.
