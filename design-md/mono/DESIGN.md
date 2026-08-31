# mono — Design System

> **North Star**: White-walled gallery grid. A page organized like a museum contact sheet — stark white cells, thin black rules, and type that floats without shadow or ornament.
> **Theme**: light
> **Source**: https://mono.frm.fm/en
> **Refero Style**: https://styles.refero.design/style/859f6be7-9d2d-4da6-a9b7-baa658172696
> **Synced**: 2026-09-01

## Overview

Mono X7 operates as a Brutalist editorial canvas: pure white surface, dark ink type, hard 2px rules dividing the page into modular cells. NH and S-Condensed do all the talking — weight 100/300 at large sizes with negative tracking creates breathy headlines that sit beside S-Condensed uppercase labels tracking wide at +0.1em. No shadows, no gradients, no color accent; the system is deliberately monastic, treating typography and grid as the entire visual language. Every component is rectilinear, zero radius, and bound by visible borders rather than elevation.

## Color Palette

- **Ink**: `#292929` — Primary text, heading color, link color, border strokes, surface blocks — the structural dark that replaces shadow everywhere in the system [neutral]
- **Paper**: `#ffffff` — Page canvas, card surface, input fill, inverse text — the dominant white ground [neutral]
- **Carbon**: `#000000` — SVG illustration fills and input text — appears in decorative line-art and form value color [neutral]

## Typography

- **NH**
- **S-Condensed**
- **EV**
- **S-Works**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.34 |
| body-sm | 14 | — | 0.9 |
| body | 16 | — | 1.34 |
| body-lg | 18 | — | 1.5 |
| subheading | 25 | — | 1.27 |
| heading-sm | 32 | — | 1.25 |
| heading | 40 | — | 1.34 |
| display | 43 | — | 1.34 |

## Spacing & Layout

- **Card Padding**: 20px
- **Element Gap**: 8px
- **Border Radius**: {'tags': '0px', 'cards': '0px', 'images': '0px', 'inputs': '0px', 'buttons': '0px'}

## Surfaces / Elevation

- **Paper**
- **Ink Block**

## Imagery

Product photography dominates: a single hardware device (the Mono X7 display) rendered straight-on against white, treated as an object in a museum rather than a lifestyle product. Black-and-white decorative SVG line-art appears in editorial rotations and rotating circular typographic ornaments. The page is text-and-product dominant, not image-heavy — imagery occupies roughly 30% of total visual real estate and is always contained inside bordered cells with 0px radius, no masks or vignettes.

## Design Principles

### Do

- Use 2px solid #292929 borders as the primary separator and container system instead of shadows or background fills
- Set all border-radius to 0px — no rounded corners anywhere
- Use NH weight 100–300 at 32–43px for headlines with -0.02em letter-spacing
- Set S-Condensed labels at 12–14px uppercase with +0.1em to +0.2em letter-spacing for all nav, tags, and metadata
- Let the grid go edge-to-edge (no max-width container) — sections butt directly against each other via shared borders
- Use 8px as the base spacing unit, stepping in multiples (8, 12, 20, 43, 45)
- Pair white (#ffffff) surfaces with #292929 ink for all text and borders — never introduce accent color

### Don't

- Don't add box-shadow, drop-shadow, or any elevation — the system is intentionally flat
- Don't round any corner — cards, buttons, inputs, images all stay 0px
- Don't use bold weights (600+) — the system's voice comes from weight 100/300/400/500
- Don't introduce a brand accent color — the palette is strictly black/white/ink
- Don't use gradients — fills are always flat solids
- Don't use lowercase body text in S-Condensed — that face is always uppercase
- Don't center-align body paragraphs — copy flows left-aligned in editorial register

## Components

### Bordered Cell

White (#ffffff) background, 2px solid #292929 border on all sides, 0px radius, variable internal padding (commonly 43px top/bottom and 45px left/right for heading cells, 20px for content cells). This is the dominant container — every section, card, and panel uses this pattern instead of shadows or fill colors.

### Outline Button

Transparent background, 1–2px #292929 border, 0px radius, padding 0px 20px vertically centered (text-baseline alignment), text in #292929 at 12–14px S-Condensed weight 500 uppercase with +0.1em tracking. Buttons sit on grid lines and inherit the rectilinear grid rather than floating above it.

### Text Link

No border, no background, #292929 text at 12px S-Condensed weight 300 uppercase, +0.2em tracking, 20px horizontal padding. Examples: EN/JP language toggle, ABOUT tag, Pre-order label.

### Inverse Text Button

#292929 or #000000 background, #ffffff text, 0px radius, no border, 12px S-Condensed uppercase. Used for active/selected nav states and inverse actions on dark cells (e.g., the 'MONO X7' label on the product image cell).

### Underline Input

White (#ffffff) background, 1px #000000 bottom border only (no full border), 0px radius, padding 8px 0, #000000 text. The hairline-bottom-only treatment replaces boxed inputs — text sits directly on the page grid.

### Display Headline

NH weight 300 at 43px, lineHeight 1.34, letter-spacing -0.02em (-0.86px), #292929. Large size with whisper-weight and tight tracking is the system's signature — anti-bolding, editorial register.

### Uppercase Label

S-Condensed weight 400–500 at 12px, lineHeight 1.34, uppercase, letter-spacing +0.1em (+0.12px), #292929 on white or #ffffff on #292929 inverse. Functions like museum plaque text — identifies what each cell contains.

### Editorial Caption

S-Condensed or NH at 12–16px, #292929, often rotated or wrapped in a circle as decorative SVG text. The 'Digital canvas that elevates a space with the ease of...' treatment is a signature pattern.

### Vertical Sidebar Label

S-Condensed weight 300 at 12px, rotated 90° on the right edge of the page, #292929, uppercase, tracking +0.2em. Marks vertical navigation categories (Illustration, Creative Coding, Web Experiments, etc.).

### Product Hero Image

Renders without frame/border inside its grid cell, 0px radius, sits on pure white background, no shadow or mask — the product is shown raw within the bordered cell, not lifted off it.

### Footer Bar

Single horizontal row across page width, 2px top border #292929, 12px S-Condensed uppercase content with +0.2em tracking, 20px vertical padding, white background. Examples: '© FRM Inc. 2026  SHOP  CONTACT  PRESS  CORPORATE'.

### Dark Inverse Cell

#292929 fill, #ffffff text and borders, 0px radius, 2px #292929 outer border (visually seamless to adjacent cells). Used sparingly for inverse panels and product overlay labels.

## Similar Design Systems

- {'why': 'Same editorial-grid approach with hard-bordered modular cells, uppercase condensed labels for metadata, and flat surfaces without shadows', 'business': 'Bloomberg Businessweek'}
- {'why': 'Same whisper-weight serif/sans typography at large sizes with tight tracking, pure white backgrounds, and zero-radius frames around imagery', 'business': 'Kinfolk Magazine'}
- {'why': 'Same brutalist flat aesthetic with technical product photography, uppercase tracked labels, and 2px black rules as the dominant visual element', 'business': 'Teenage Engineering'}
- {'why': 'Same gallery-as-grid layout with rotated vertical sidebar text, editorial weight-100 type, and raw product/object imagery without masks', 'business': 'Hito Steyerl / Rhizome art sites'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #292929
- background: #ffffff
- border: #292929
- inverse surface: #292929
- decorative fill: #000000
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. Create a hero headline cell: white (#ffffff) background, 2px solid #292929 border, 0px radius, 43px top/bottom padding. Text inside: 'made for art lovers' in NH weight 300, 43px, #292929, letter-spacing -0.02em, line-height 1.34. No shadow, no rounded corners.

2. Create an outlined navigation button: transparent background, 1px solid #292929 border, 0px radius, padding 0px 20px. Text: 'PRE-ORDER' in S-Condensed weight 500, 12px, uppercase, #292929, letter-spacing +0.1em. The button sits flush on the grid, not floating above it.

3. Create a bordered product showcase cell: white (#ffffff) background, 2px solid #292929 border, 0px radius, full-width inside a grid. Product image renders inside with 0px radius, no border, no shadow — shown raw on the white ground.

4. Create a vertical sidebar label: S-Condensed weight 300, 12px, uppercase, #292929, letter-spacing +0.2em, rotated 90° on the right edge of the page, 20px from the edge. Content: 'Illustration, Creative Coding, Web Experiments'.

5. Create a footer bar: 2px solid #292929 top border, white background, 12px S-Condensed uppercase content with +0.2em tracking, separated by wide horizontal padding. Content: '© FRM Inc. 2026   SHOP   CONTACT   PRESS   CORPORATE'.

## Border System

The 2px solid #292929 border is the system's most-used visual element (51 occurrences in raw data, far exceeding any other pattern). It replaces every function that shadows, fills, or radii would normally serve — containers, dividers, button outlines, and card frames all share the same stroke. 1px borders appear only for subtle inline elements like the bottom edge of inputs. Maintain 2px as the standard; never mix border widths on adjacent cells.

## Animation Philosophy

Motion is minimal and functional: 0.6s ease for height/width transitions (likely product image scaling), 0.3s for state changes. No bounce, no spring, no decorative entrance animations — the system animates only when geometry changes. cubic-bezier(0.455, 0.03, 0.515, 0.955) appears for the rare eased transitions (classic ease-in-out feel).
