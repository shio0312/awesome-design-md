# Altitude — Design System

> **North Star**: midnight financial editorial — a darkened trading floor printed on bone-white serif stock, lit only by thin borders and a single blue accent.
> **Theme**: dark
> **Source**: https://www.altitude.so
> **Refero Style**: https://styles.refero.design/style/0e971626-ca51-45ba-acf6-35a53c561b2c
> **Synced**: 2026-09-01

## Overview

Altitude operates in a midnight editorial register: near-black canvas, off-white serif headlines (Libre Baskerville), and razor-thin secondary type (Inter). The serif-on-dark pairing is the signature — most AI finance tools lean on geometric sans-serifs; Altitude borrows from financial print (WSJ, FT) to signal authority and discretion. Mountain ridge linework and painterly landscape photography replace the usual gradient meshes and 3D renders, grounding the AI product in a sense of summit and scale. Surfaces are stratified by barely-perceptible gray steps (#111 → #181 → #1f → #26 → #32), with hairline borders doing the structural work that shadows do elsewhere. Color is almost entirely absent from the interface — when it appears, it reads as functional punctuation rather than decoration. Components are tight, rectangular (4–8px radii), and content-forward.

## Color Palette

- **Carbon Canvas**: `#181818` — Primary page background; the foundational dark surface that all sections sit on [neutral]
- **Obsidian**: `#111111` — Deepest layer — footer, contrast blocks, shadow wells [neutral]
- **Graphite Card**: `#1f1f1f` — Card and input surfaces lifted one step above canvas [neutral]
- **Slate Elevated**: `#262626` — Elevated surfaces — table rows, hover states, secondary panels [neutral]
- **Iron Peak**: `#323232` — Highest surface tier — dropdowns, popovers, selected list items [neutral]
- **Bone**: `#eeeeee` — Primary text and hairline borders — the dominant foreground tone [neutral]
- **Ash**: `#e4e4e4` — Secondary borders and card outlines [neutral]
- **Fog**: `#a4a19b` — Muted helper text, icon strokes, disabled labels [neutral]
- **Smoke**: `#5e5d59` — Subtle dividers, badge backgrounds, low-emphasis text [neutral]
- **Pewter**: `#4b4b4b` — Deep borders, table separators [neutral]
- **Pure White**: `#ffffff` — Icon glyphs, card backgrounds for light-section contrast blocks, max-emphasis text [neutral]
- **Voltage Blue**: `#2b7fff` — Sole chromatic accent — inline link highlights, selection, active state within data-dense terminal views; appears as the only color in an otherwise achromatic system [accent]
- **Mid Navy**: `#1a365d` — Decorative deep-blue tone used in heading borders and subtle heading tints — adds depth without breaking the monochromatic discipline [brand]

## Typography

- **Libre Baskerville**
- **Inter**
- **Fira Code**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.5 |
| body | 14 | — | 1.5 |
| heading-sm | 18 | — | 1.43 |
| heading | 28 | — | 1.38 |
| heading-lg | 36 | — | 1.15 |
| display | 72 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 12px
- **Element Gap**: 8px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '8px', 'icons': '4px', 'badges': '4px', 'inputs': '4px', 'buttons': '4px', 'large_surfaces': '16px'}

## Layout

Max-width 1200px centered, full-bleed dark canvas. Hero is a centered single-column stack (display headline → subhead → ghost CTA) with the mountain ridge line running full-width at the bottom. Product sections alternate between two patterns: (1) a dark product-visual-right layout (40% copy left, 60% terminal-over-landscape right) and (2) a dark copy-right layout with a light off-white workflow card grid on the left. Section gaps are generous — 80px vertical rhythm separates each band. Navigation is a single 64px-tall top bar with the wordmark left, three nav links center, Login right; no sticky behavior, no hamburger. The page flows seamlessly from dark to dark with one light-section interruption (the workflow grid) for contrast.

## Surfaces / Elevation

- **Obsidian**
- **Carbon Canvas**
- **Graphite Card**
- **Slate Elevated**
- **Iron Peak**

**Shadow tokens:**

## Imagery

Photography is the dominant visual medium — specifically painterly, atmospheric mountain landscapes in muted blue-grays that evoke summit, scale, and distance. These appear as full-bleed or large contained images behind product terminal screenshots, creating a 'looking through a window at the product' effect. A continuous single-line mountain ridge SVG runs across the hero, drawn in 1px #a4a19b — a minimalist line-art counterpoint to the photographic sections. Icons are outline-style, 1.5px stroke, monochrome in #1a365d or #a4a19b, never filled. No 3D renders, no abstract gradient art, no stock-style lifestyle photography. The imagery vocabulary is: landscape photography + thin line-art + product terminal screenshots.

## Design Principles

### Do

- Use Libre Baskerville weight 400 at 36–72px for all section and display headlines; never substitute a sans-serif for these.
- Maintain the surface stack: #111 → #181 → #1f → #26 → #32, ascending by roughly 5–10% luminance steps.
- Use 4px radius for all buttons, inputs, and badges; 8px for cards; 16px only for large image containers.
- Keep body text in Inter 14px weight 400, #eeeeee, with #a4a19b for muted helper text and #5e5d59 for placeholders.
- Use 8px element gaps and 12px card padding as the baseline; scale section rhythm in 24/32/64/80px steps.
- Let the mountain ridge line graphic or landscape photography do the visual storytelling — no gradient meshes, no 3D orbs, no neon glows.
- Communicate status through weight, border, and tracking rather than color; reserve #2b7fff for inline links and the focus ring only.

### Don't

- Don't use bold weights (700) for headlines — Libre Baskerville at weight 400 is the voice; going heavier breaks the editorial register.
- Don't introduce new accent colors — the system is monochromatic with one blue; adding green/red/yellow for semantic states breaks the discipline.
- Don't use heavy drop shadows for cards or buttons; shadows here are 0.05 opacity whispers, not 0.3-opacity lifts.
- Don't round corners above 16px — the rectilinear 4–8px language is a signature; pill shapes (9999px) would look foreign.
- Don't use white (#ffffff) as body text — #eeeeee is softer and the right foreground tone against #181818.
- Don't pair Inter with another sans-serif for headings; the Inter/Baskerville duality is the only pairing the system uses.
- Don't apply gradients to UI surfaces — the one detected gradient is on a landscape image, not on any card or button.

## Components

### Ghost Button

Transparent background, 1px solid #eeeeee border, #eeeeee text at 14px Inter weight 500, 4px radius, 16px horizontal / 8px vertical padding. Hover lifts to #262626 background. The filled-inverse version (white bg, black text) is rare; the ghost is the default voice.

### Navigation Link

No background, no border. Inter 14px weight 400 in #eeeeee. Active state: 1px #aeaeae bottom border acting as a thin underline marker. Sits in a 64px-tall bar with the wordmark left and Login right.

### Workflow Tile

Off-white card (#e7e5e4 to #ffffff range) on the dark canvas, 8px radius, 24px padding. Centered icon (24px, 1.5px stroke) in #1a365d, label beneath in Inter 13px weight 500, #181818 text. Arranged in a 5-column grid with 12px gaps.

### Terminal Window

Dark app chrome (#1f1f1f) with traffic-light dots (red/yellow/green) top-left, sidebar listing platform items in Inter 13px, and a main content area with Fira Code monospaced text. Rounded 8px on the container; the internal panes are square-cornered. Drops the heavy modal-level shadow when presented as a marketing screenshot.

### Serif Section Header

Libre Baskerville 48px weight 400, #eeeeee, line-height 1.15, letter-spacing -0.025em. No kicker label, no eyebrow — the serif does all the work. Subhead below in Inter 16px weight 400, #a4a19b.

### Hero Composition

Full-viewport #181818 canvas. Centered stack: display headline (Libre Baskerville 72px, #eeeeee, ls -0.025em), single-line subhead (Inter 18px, #a4a19b), ghost CTA below. A continuous mountain ridge line in 1px #a4a19b runs full-width near the bottom — the only decorative graphic on the page.

### Input Field

Background #1f1f1f, 1px #323232 border, 4px radius, 12px padding, Inter 14px weight 400, #eeeeee text. Placeholder in #5e5d59. Focus ring: 2px #2b7fff outer glow.

### Badge / Status Pill

Background #5e5d59 or #323232, text Inter 11px weight 500 in #eeeeee, 4px radius, 6px 10px padding. Uppercase tracking +0.05em. No colored fill — status is always communicated through border weight or text, never hue.

### Data Table Row

Background alternates between transparent and #262626; 1px #262626 bottom border; Inter 13px weight 400 in #eeeeee; 16px vertical padding. Header row uses Inter 11px weight 500 uppercase, tracking +0.05em, in #a4a19b.

### Product Feature Split

Max-width 1200px centered. Left column: 40% width, serif heading + body copy + text-link CTA ('Try Me →'). Right column: 60% width, product visual (terminal window over mountain landscape) with 8px container radius. Section gap 80px above and below.

### Footer

Background #111111, 64px vertical padding. Wordmark, nav links, and legal in Inter 13px weight 400, #a4a19b. 1px #1f1f1f top border separates from main content.

### Image Card / Hero Visual

16px radius, 1px #262626 border, #1f1f1f fallback background behind image. Mountain landscape photography (painterly, blue-gray, atmospheric) is the primary visual — no abstract gradients, no 3D renders.

## Similar Design Systems

- {'why': 'Same near-black canvas with generous serif/sans pairing, monochromatic discipline, and ghost-button CTAs — though Ramp is lighter and more playful.', 'business': 'Ramp'}
- {'why': 'Dark-mode fintech surface with thin borders, hairline structural elements, and restrained color use; similar density and information-forward layout.', 'business': 'Plaid'}
- {'why': "Dark dense UI with the same five-step gray surface stack, 4–8px corner radius vocabulary, and the same 'chromatic accent only where functionally necessary' rule.", 'business': 'Linear'}
- {'why': 'Shares the editorial-financial DNA — serif display, monospaced data, dark canvas, hairline grid lines, and zero tolerance for decorative color.', 'business': 'Bloomberg Terminal'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #eeeeee
- background: #181818
- border: #262626
- accent: #2b7fff
- muted text: #a4a19b
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Serif section header + body**: Left-aligned Libre Baskerville 48px weight 400, #eeeeee, letter-spacing -1.2px. Subhead in Inter 16px weight 400, #a4a19b. Body copy in Inter 14px weight 400, #eeeeee, 1.5 line-height. 'Try Me →' text link in Inter 14px weight 500, #2b7fff.

3. **Workflow tile card**: Off-white #e7e5e4 background, 8px radius, 24px padding, 1px #e4e4e4 border. Centered 24px outline icon in #1a365d. Label beneath in Inter 13px weight 500, #181818. Arranged in a 5-column grid with 12px gaps on the #181818 canvas.

4. **Terminal window**: #1f1f1f background, 8px radius, 1px #262626 border. Top bar with three 10px traffic-light dots (red #ff5f57, yellow #febc20, green #28c840). Sidebar at 200px width with Inter 13px #eeeeee list items on #181818 background. Main pane with Fira Code 14px, #eeeeee text on #1f1f1f.

5. **Data table row**: Full-width row, 16px vertical padding, 1px #262626 bottom border. Inter 13px weight 400, #eeeeee. Alternating row background: transparent and #262626. Header row above: Inter 11px weight 500 uppercase, +0.5px tracking, #a4a19b.
