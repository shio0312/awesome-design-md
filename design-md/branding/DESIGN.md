# Branding — Design System

> **North Star**: Black gallery wall, blood-red punctuation — Oversized white display type floats on a void-like dark canvas, interrupted by a single vivid red accent and dramatic ornamental display faces that feel like gallery signage rather than web UI.
> **Theme**: dark
> **Source**: https://www.svz.io
> **Refero Style**: https://styles.refero.design/style/4d4772a3-e1da-415f-a6d7-658dcefdcecd
> **Synced**: 2026-09-01

## Overview

SVZ operates in the visual register of a high-fashion editorial: pitch-black canvas, oversized display typography that dominates the viewport, and a single arterial red that appears like a wound in the monochrome. The interface is deliberately sparse — most surfaces carry no chrome at all, letting type, photographic collage, and oversized background shapes do the work. Text is primarily white on near-black, with an off-white (#f3efef) reserved for inverted bodies and footers. Hierarchy is achieved through scale (160px display stepping down to 10px labels) and weight contrast (300 whisper-thin body against 700 blocky caps), never through color or chrome. Every interactive element is ghost or hairline-bordered — the system refuses to shout with buttons, preferring arrows and discover-call links that feel like editorial pull-quotes.

## Color Palette

- **Void Canvas**: `#080808` — Primary page background; the base upon which all display type and floating shapes sit [neutral]
- **Absolute Black**: `#000000` — Deepest surface, decorative fills, icon strokes — the floor beneath the void [neutral]
- **Charcoal Plate**: `#171617` — Footer and inverted section backgrounds, slightly elevated off the base void [neutral]
- **Smoke Plate**: `#262525` — Secondary surface for content blocks and image treatments layered over the void [neutral]
- **Graphite Lift**: `#393939` — Subtle elevation surface and card background; the only visible shadow color [neutral]
- **Bone White**: `#fcfcfc` — Primary text, hairline borders, icon outlines — the dominant non-black color in the system [neutral]
- **Linen**: `#f3efef` — Inverted body sections, off-white text on dark cards, soft warm-white content surfaces [neutral]
- **Ash**: `#d4d2d2` — Muted secondary text, nav labels, subtle borders — the whispered voice between bone and graphite [neutral]
- **Pebble**: `#b5b2b2` — Disabled borders, tertiary helper text, low-priority metadata [neutral]
- **Iron**: `#525252` — Link underlines, nav dividers, hairline separators on dark surfaces [neutral]
- **Arterial Red**: `#fe1e34` — Sole brand accent — card borders, cursor, hero dot, gradient terminator; the only saturated color and it is used like a heartbeat, not a coat of paint [brand]
- **Crimson Pure**: `#ff0000` — Heading underline accent and decorative fill — a purer red for typographic emphasis only [brand]

## Typography

- **Kmr Waldenburg**
- **Editorialnew**
- **Dirtyline 36 Daysoftype 2022**
- **system-ui**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.2 |
| body | 14 | — | 1.5 |
| subheading | 24 | — | 1.1 |
| heading-sm | 32 | — | 1.05 |
| heading | 42 | — | 1.05 |
| heading-lg | 64 | — | 1 |
| display | 80 | — | 0.9 |
| display-xl | 160 | — | 0.9 |

## Spacing & Layout

- **Card Padding**: 12-24px
- **Element Gap**: 24px
- **Section Gap**: 48-64px
- **Border Radius**: {'nav': '3px', 'cards': '8px', 'buttons': '8px', 'largeCards': '14.4px'}

## Layout

Full-bleed dark canvas with no max-width container — content uses generous internal padding (48–64px section gaps) to feel composed against the void. The hero is a full-viewport moment dominated by 160px display type centered or left-aligned, with the dark background visible around all four edges. Sections alternate between void (#080808) and a single inverted linen (#f3efef) body panel, with 48–80px vertical breathing room. Navigation is a transparent top bar; no sticky header, no sidebar. Content arrangement is editorial: asymmetric, with display headlines set as two- or three-line stacks and small italic connectives. Card grids (when used) are 2–3 columns with 24px gaps, 8px radius, and 1px hairline borders.

## Surfaces / Elevation

- **Void**
- **Absolute**
- **Charcoal**
- **Smoke**
- **Graphite**
- **Linen**

**Shadow tokens:**

## Imagery

Imagery is editorial-collage: large-scale photographic textures (leopard-print heart, animal patterns) and oversized geometric shapes bleeding off-canvas in Smoke (#171617–#262525) tones. Full-bleed, no rounded corners, no contained frames — images occupy the canvas like wallpaper, not thumbnails. Photography is high-contrast, dark/moody, often surreal or fashion-editorial, used to punctuate display type rather than explain product. Iconography is minimal: 1px hairline arrows (↗) and stroked SVGs in bone-white on the void. No illustration, no 3D, no abstract gradients on content.

## Design Principles

### Do

- Let type carry hierarchy — use 80–160px display sizes for hero moments and 10–12px tracked uppercase for metadata; do not introduce color, chrome, or icons to compensate.
- Use #fe1e34 only as a 1px border on one or two featured elements per page, plus the accent dot — the red must remain rare to function as punctuation.
- Mix Kmr Waldenburg caps at 700 with Editorialnew italic weight 300 on the same baseline for editorial contrast — this two-family dialogue is the signature.
- Maintain 0.90–1.10 line-height on all display sizes; the system uses tight leading to let oversized type feel architectural rather than airy.
- Track 10–12px nav and label text OUT to +0.071em–+0.308em and display text IN to -0.050em–-0.080em — letter-spacing is a load-bearing typographic tool, not decoration.
- Anchor interactive elements with a diagonal arrow icon (↗) rather than color, weight, or background change — hover states should shift position or weight, not hue.
- Use #f3efef as the only surface that escapes the void; light sections feel like turning a page in a magazine.

### Don't

- Do not introduce filled buttons, drop shadows, or gradients on UI elements — the system rejects conventional depth and uses a single white inset highlight at most.
- Do not use #fe1e34 as a text color, background fill, or icon color beyond borders and the single accent dot; spreading the red flattens its meaning.
- Do not use Kmr Waldenburg body weights (300/400) for display headings under 64px — the system reserves 700 weight for sizes 42px and above to preserve impact.
- Do not apply border-radius above 14.4px; the system uses crisp 3px (nav/links) and 8px (cards/buttons) only — rounding is a whisper, not a curve.
- Do not place body text below 14px or above 32px without shifting to a display role; 10–12px is reserved for tracked uppercase labels with no sentence structure.
- Do not combine more than two typeface families in a single composition (Kmr Waldenburg + Editorialnew, or + Dirtyline 36); adding a third breaks the editorial discipline.
- Do not use #000000 as a text color on dark surfaces — the void (#080808) and bone-white (#fcfcfc) pairing is the system's reading contract; pure black text only appears on #f3efef.

## Components

### Ghost CTA Link

Uppercase 12px Kmr Waldenburg weight 400 with 0.071em letter-spacing, bone-white (#fcfcfc) text on void canvas, paired with a 45° arrow icon. No fill, no background, no border. 32px vertical padding, 8px horizontal. Replaces the conventional button entirely — the system treats calls-to-action as editorial pull-quotes, not UI controls.

### Discovery Call Outlined Button

Top-right header element: uppercase 12px tracked text inside an 8px-radius rectangle with a 1px hairline border at #d4d2d2 on the void, containing a diagonal arrow. Internal padding 12px 24px. This is the only element that visually resembles a 'button' in the conventional sense — even it is a ghost.

### Hero Display Headline

160px Kmr Waldenburg weight 700, all caps, line-height 0.90, letter-spacing -12.8px. White (#fcfcfc) on void (#080808). Small Editorialnew italic weight 300 words ('crafting', 'for the') sit inline at 42px between the caps as connective tissue. The two type families are locked at the same baseline grid.

### Section Transition Headline

80px Kmr Waldenburg weight 700 with -6px tracking, paired with a single oversized ornamental letter from Dirtyline 36 Daysoftype 2022 in 80–160px. The contrast between blocky geometric caps and a hand-drawn calligraphic glyph is the signature moment.

### Bordered Brand Card

Background: void or smoke (#080808–#262525). Border: 1px solid #fe1e34. Border-radius: 8px. Internal padding: 24px. The red border is the only chromatic border in the system; it functions as a 'featured' marker, not decoration.

### Standard Card

Background #080808 or #f3efef, 1px hairline border at #d4d2d2 (on dark) or #525252 (on light), 8px radius, 12–24px internal padding. Inset highlight: rgba(255,255,255,0.2) 0px 2px 5px 0px inset on dark variants to suggest a glass edge.

### Hairline Link

12–14px Kmr Waldenburg weight 400, uppercase, 0.071em tracking. Underline in #525252 (on dark) or #b5b2b2 (on light). 3px border-radius is reserved for link/nav containers only. No color change on hover — the system relies on weight or position shift instead.

### Top Navigation

Full-width, transparent over void canvas. Logo 'SVZ' top-left in 32px Editorialnew or Kmr Waldenburg caps. Four column groups (AGENCY, WORK, CULTURE, INSIGHTS) centered as tracked uppercase labels with stacked sub-items in 12px. Discovery Call outlined button pinned top-right. No background fill — the nav floats on the void.

### Footer Panel

Charcoal (#171617) background, full-bleed, bone-white text. Mirrors the nav's column structure. 48px vertical padding minimum.

### Accent Dot

Solid 16–24px #fe1e34 circle, no border, no shadow. Appears as a cursor-like marker near CTA areas and as visual rhythm against the void. Functions like a drop of blood in the monochrome system.

### Decorative Background Shape

Oversized geometric forms (crosses, arrows, letters) rendered in #171617 to #262525 with 8–20% perceived opacity, bleeding off-canvas. Establishes editorial composition without competing with foreground type. No interaction.

### Editorial Body Panel

Linen (#f3efef) background, 080808 text, 14px Kmr Waldenburg weight 400, line-height 1.50, 24px section padding. The only high-density reading surface in the system. 1px #d4d2d2 border or seamless transition from a dark section.

## Similar Design Systems

- {'why': 'Same agency-portfolio instinct for oversized display type on dark canvases, with display faces treated as editorial objects rather than UI text', 'business': 'Locomotive Mtl'}
- {'why': 'Dark-mode creative agency site with a single saturated accent color used as punctuation and a refusal of conventional button chrome', 'business': 'Resn'}
- {'why': 'Editorial-magazine layout rhythm, hairline-bordered cards on near-black surfaces, and serif-italic connectives woven into display caps', 'business': 'Huge'}
- {'why': 'Full-bleed dark canvas, bleeding decorative shapes behind display type, and a single vivid accent (their neon) used as rare punctuation', 'business': 'Active Theory'}
- {'why': 'Agency sites that treat typography as art direction — mixing geometric sans display with editorial serif italics and letting the type do the layout work', 'business': 'Ueno'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #fcfcfc
- background: #080808
- border: #d4d2d2 (on dark) / #525252 (on light)
- accent: #fe1e34
- primary action: #fe1e34 (filled action)

**3-5 Example Component Prompts**

1. Create a Primary Action Button: #fe1e34 background, #fcfcfc text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Build a featured project card: background #080808, 1px solid #fe1e34 border, 8px border-radius, 24px padding. Headline 'PROJECT NAME' in 24px Kmr Waldenburg weight 700, color #fcfcfc, letter-spacing -0.91px. Body description in 14px Kmr Waldenburg weight 400, color #d4d2d2, line-height 1.50. The red border is the only chromatic chrome — do not add shadows, fills, or icons.

3. Build the top navigation: transparent background over void canvas. Left: logo 'SVZ' in 32px Kmr Waldenburg weight 700 caps, color #fcfcfc. Center: four column headers (AGENCY, WORK, CULTURE, INSIGHTS) in 10px Kmr Waldenburg weight 400 uppercase, tracked +0.8px, color #d4d2d2, each with 2–3 sub-items in 12px same color directly below at 8px row gap. Right: a Discovery Call outlined button — 8px border-radius rectangle with 1px #d4d2d2 border, 12px 24px padding, 'DISCOVERY CALL ↗' in 12px Kmr Waldenburg weight 400 uppercase, color #fcfcfc, tracked +0.85px.

4. Build an inverted body section: background #f3efef, 64px vertical padding. Body text in 14px Kmr Waldenburg weight 400, color #080808, line-height 1.50. Section heading 'EDITORIAL' in 32px Kmr Waldenburg weight 700, color #080808, letter-spacing -1.6px, uppercase. Use this surface sparingly — it is the only escape from the void and should feel like turning a page.

5. Build a 'WE ARE' transition moment: void background, 80px Kmr Waldenburg weight 700 caps spelling 'WE' and 'RE' with extreme letter-spacing -6px, color #fcfcfc, line-height 0.90. Between them, a single ornamental 160px character from Dirtyline 36 Daysoftype 2022 (a stylized 'a' or calligraphic letterform) as a sculptural object — the geometric caps and the hand-drawn glyph must sit on the same baseline with the cap-height of the glyph matching the cap-height of the surrounding letters.
