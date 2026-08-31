# ON.energy — Design System

> **North Star**: High-voltage caution yellow on midnight steel
> **Theme**: mixed
> **Source**: https://www.on.energy
> **Refero Style**: https://styles.refero.design/style/31e00a99-6946-4f07-829a-b0904a39a20d
> **Synced**: 2026-09-01

## Overview

ON.energy operates in a high-contrast industrial language: a single vivid yellow (#fff313) that functions as both full-bleed atmospheric section and functional accent against deep black surfaces, with no gradients or decorative effects in between. The type system uses Univers Next Pro at whisper-light weight 300 for all display and headline work — an anti-convention choice that creates authority through restraint rather than volume, paired with aggressively tight tracking (-0.04em at 36px+). Layout alternates between dramatic full-bleed color blocks (dark product photography, pure yellow statement sections, white content areas) rather than gentle cards-on-canvas, creating a rhythmic, almost industrial-signage quality. Radii stay small and utilitarian (6-9px), shadows are absent, and the component vocabulary is deliberately narrow: pill nav items, one yellow CTA, image cards, and a strong typographic hierarchy.

## Color Palette

- **Caution Yellow**: `#fff313` — Yellow supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Midnight Steel**: `#000000` — Page canvas, dark hero surfaces, nav background, text on yellow sections [neutral]
- **Industrial White**: `#eeeeee` — Light section backgrounds, text on dark surfaces, news card surfaces [neutral]
- **Carbon**: `#333333` — Elevated dark surfaces, navigation pill buttons, card backgrounds on dark sections [neutral]
- **Gunmetal**: `#4b4b4b` — Hairline borders, dividers, subtle structural lines on dark surfaces [neutral]
- **Aluminum**: `#afafaf` — Muted body text on dark backgrounds, secondary copy, footer text [neutral]

## Typography

- **Univers Next Pro**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| micro | 10 | — | 1.2 |
| caption | 12 | — | 1.2 |
| body-sm | 14 | — | 1.2 |
| heading | 24 | — | 1.17 |
| heading-lg | 36 | — | 1.13 |
| display | 64 | — | 1 |

## Spacing & Layout

- **Card Padding**: 24px
- **Element Gap**: 16px
- **Section Gap**: 120px
- **Border Radius**: {'nav': '6px', 'cards': '9px', 'images': '16px', 'buttons': '6px', 'sections': '24px'}

## Layout

Full-bleed page model with no global max-width constraint. The page is structured as a sequence of three distinct full-viewport section types: (1) dark hero with overlaid white headline and small product discovery card anchored bottom-right, (2) pure yellow statement section with large ghosted text, (3) white content sections with generous internal padding. Navigation floats as a translucent bar over the hero, then sits solid over subsequent sections. Content within light sections uses a centered column with ~400-500px text width and 2-column image grids for editorial blocks. The 120px section gap creates deliberate breathing room between the full-bleed color acts, making each section feel like a discrete visual statement rather than a continuous scroll.

## Surfaces / Elevation

- **Pure Black**
- **Carbon**
- **Industrial White**
- **Caution Yellow**

## Imagery

Industrial product photography dominates: close-up shots of metal panels, rack hardware, and power equipment with dark, moody lighting. The hardware itself is the hero — no lifestyle context, no people operating equipment, no staged environments. The metallic surfaces catch light against black backgrounds, creating a high-contrast, almost forensic feel. Team photography uses the brand yellow as a backdrop. Infrastructure shots show real deployments in outdoor settings. Images are treated as full-bleed atmospheric elements, not thumbnails — they fill sections edge to edge with 16px corner radius as the only softening.

## Design Principles

### Do

- Use weight 300 for all headlines and display text — it is the system's signature restraint and must not be substituted with medium/semibold weights
- Use #fff313 only for CTA buttons, full-bleed section backgrounds, and small accent borders — never for body text, icons, or decorative fills
- Apply -0.04em letter-spacing at 36px and above, -0.02em at 16-24px — the tight tracking reinforces the industrial precision feel
- Let sections alternate full-bleed: dark image → pure yellow → light white — this three-mode rhythm is the page's structural backbone
- Keep border-radius at 6px for interactive elements (nav, buttons) and 9px for cards — stay utilitarian, never approach full-pill rounding
- Use #000000 text on yellow sections and #eeeeee text on dark sections — never invert, the high contrast is non-negotiable
- Maintain 120px vertical gaps between major sections to let the full-bleed color blocks breathe as distinct visual acts

### Don't

- Never add box-shadows — the system is deliberately flat, relying on color contrast and full-bleed section breaks for hierarchy
- Never introduce gradients — the yellow sections ARE the color moments; gradients would dilute their impact
- Never use weight 500, 600, or 700 — the binary 300/400 pairing is a design constraint, not an oversight
- Never place yellow body text on yellow backgrounds, or black text on black — the contrast pairs are fixed
- Never use large border-radius values (above 16px) on functional elements — the industrial feel depends on tight radii
- Never add intermediate gray text colors on yellow sections — stick to #000000 or a single muted yellow tone
- Never constrain full-bleed sections to a max-width container — the yellow and dark sections must span edge to edge

## Components

### Yellow CTA Button

Filled #fff313 background, #000000 text, 6px border-radius, 7px vertical and 16px horizontal padding. Univers Next Pro 400 at 14px. No shadow, no gradient. The high-contrast yellow-on-black creates the system's one point of interactive urgency.

### Dark Navigation Pill

#333333 background, #eeeeee text, 6px border-radius, 5px vertical and 14px horizontal padding. Univers Next Pro 400 at 14px. Appears as a horizontal row of dark pills on yellow or image sections, creating contrast without weight.

### Logo Mark

Small yellow (#fff313) square with black 'ON' text inside, set against the dark nav bar. Sharp corners, no padding, functions as a compact signal mark.

### Hero Headline

Univers Next Pro 300 at 64px, line-height 1.00, letter-spacing -0.04em (-2.56px). White (#eeeeee) on dark image backgrounds. Left-aligned, large negative space below. The whisper-weight at this size is the system's signature typographic move.

### Product Highlight Card

Dark surface (#333333 or near-black) with #4b4b4b border or yellow accent, 9px border-radius, 24px padding. Contains a small product image thumbnail on the right, yellow label text on the left. Univers 300 for the label, 400 for supporting text.

### Full-Bleed Yellow Statement Section

#fff313 fills the entire viewport height. Large statement text in Univers 300 at 36-64px, rendered in a slightly desaturated yellow tone that creates a subtle ghosting effect against the saturated background. No card containers, no dividers — the text floats on the yellow field.

### News Image Card

#eeeeee background or transparent, 16px border-radius on the image. Image fills the card width. Title in Univers 300 at 24px, #000000. Arranged in a 2-column grid with 16px column gap.

### Section Heading

Univers Next Pro 300 at 36px, line-height 1.13, letter-spacing -0.04em (-1.44px). #000000. Left-aligned with generous left margin. Sits at the top of light content sections with 120px gap above.

### Body Text Block

Univers Next Pro 400 at 16px, line-height 1.20. #000000 on light sections, #afafaf on dark sections. Constrained to approximately 400-500px max width for comfortable reading.

### Nav Bar Container

Transparent or semi-transparent over hero images, solid #000000 or #333333 over yellow/light sections. Contains logo mark left, nav pills center, CTA button right. Full-width with 24px horizontal padding.

## Similar Design Systems

- {'why': 'Same industrial-grade photography of hardware against dark backgrounds, minimal component vocabulary, and singular accent color discipline', 'business': 'Rivian'}
- {'why': 'Iconic caution-yellow + black-steel color system for industrial machinery, full-bleed product imagery as hero', 'business': 'Caterpillar'}
- {'why': 'Dark-canvas product showcase with whisper-light weight typography and deliberate monochrome restraint punctuated by single accent moments', 'business': 'Polestar'}
- {'why': 'Energy infrastructure brand using full-bleed industrial photography and minimal UI chrome to let hardware speak', 'business': 'Form Energy'}
- {'why': 'Dark-mode tech brand with tight typographic tracking, pill-shaped navigation, and utilitarian radii for a hardware-adjacent feel', 'business': 'Arc'}

## Agent Prompt Guide

Quick Color Reference:
- text: #000000 (on light/yellow) / #eeeeee (on dark)
- background: #000000 (dark sections) / #eeeeee (light sections) / #fff313 (accent sections)
- border: #4b4b4b (hairlines), #fff313 (accent highlights)
- accent: #fff313
- primary action: no distinct CTA color

Example Component Prompts:

1. HERO SECTION: Full-bleed dark industrial photograph as background. Headline at 64px Univers Next Pro weight 300, #eeeeee, letter-spacing -0.04em (-2.56px), line-height 1.00, left-aligned at 40px from left edge. Body text at 14px weight 400, #afafaf. Small product highlight card anchored to bottom-right: #333333 background, 9px radius, 24px padding, yellow (#fff313) label text at 12px weight 400, thumbnail image on the right.

2. YELLOW STATEMENT SECTION: Full-bleed #fff313 background spanning 100vw and 100vh. Large statement text at 36px Univers Next Pro weight 300, line-height 1.13, letter-spacing -0.04em (-1.44px), rendered in a desaturated/muted yellow that creates a ghosting effect against the saturated background. Text left-aligned with generous left margin, vertically centered.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

4. NEWS SECTION: White (#eeeeee) background. Section heading at 36px Univers 300, #000000, letter-spacing -0.04em, at top with 120px space above. Body intro paragraph at 16px weight 400, #000000, max-width 500px. Two-column image grid below with 16px column gap: each card has a 16px-radius image filling card width, 24px space below image for title text at 24px Univers 300.
