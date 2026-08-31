# TWOMUCH.STUDIO — Design System

> **North Star**: floating museum of curiosities
> **Theme**: light
> **Source**: https://twomuch.studio
> **Refero Style**: https://styles.refero.design/style/12b3e1b6-31b9-4843-9b3b-8f39c9dd1474
> **Synced**: 2026-09-01

## Overview

A studio interface that disappears into its own canvas — a vast field of curated 3D objects, printed artifacts, and cultural ephemera floats on a flat gray plate, with the UI reduced to a single pill-shaped nav bar pinned at the visual center. Color is rationed to one vivid lime accent that acts as a highlighter against a near-total monochrome system; every other surface stays quiet so the objects can speak. Typography is locked to a single custom geometric grotesque at medium weight with aggressive negative tracking, giving even short labels a compressed, poster-like authority. Components are minimal by design — pills, circles, and hairline rules — letting the curated imagery carry the page.

## Color Palette

- **Gallery Plate**: `#e5e7eb` — Primary canvas and hairline dividers — the infinite gray field that hosts floating objects and borders nearly every surface in the system [neutral]
- **Carbon**: `#000000` — Primary text, icon strokes, and the dark pill in the nav bar — the only true black in the system, used for type and high-contrast marks [neutral]
- **Chalk**: `#f4f4f4` — Elevated surface above the canvas — cards, panels, and lighter button fills that need to lift off the gray field [neutral]
- **Paper White**: `#ffffff` — Inset surfaces and inverse text on dark fills — the cleanest white available for maximum contrast pop [neutral]
- **Concrete**: `#dedede` — Tertiary surface and muted button fill — one step darker than Chalk, used where a surface needs weight without drama [neutral]
- **Voltage Lime**: `#e2ff70` — Primary action fill and highlight accent — the only chromatic button/link background in the system, applied to the Menu pill and active link states to switch a control on [brand]
- **Oxide Brown**: `#68340e` — Decorative content accent — appears inside imagery and printed artifacts (labels, type on objects); not a UI color but a recurring editorial note [accent]

## Typography

- **ABCMonumentGrotesk**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 0.9 |
| body-sm | 14 | — | 1 |
| body | 16 | — | 1.05 |
| subheading | 18 | — | 1.33 |
| heading-sm | 20 | — | 1.33 |
| heading | 22 | — | 1.43 |

## Spacing & Layout

- **Card Padding**: 16-24px
- **Element Gap**: 8px
- **Section Gap**: 48-64px
- **Border Radius**: {'tags': '9999px', 'pills': '9999px', 'small': '4px', 'buttons': '9999px'}

## Layout

The page model is full-bleed: no max-width container, no centered column, no traditional header/footer/sidebar. The Gallery Plate canvas extends edge-to-edge and objects are absolutely positioned or loosely scattered across it. The hero is the floating object collage itself — not a headline over an image, but the curated image field with a single small nav bar pinned at the visual center. Section rhythm is sparse: long visual passages interrupted by a tight list of project indices, an occasional inverted Carbon panel, or a dense object cluster. Content is arranged through absolute placement rather than a grid; when a list or grid does appear, it uses full-width rows separated by 1px Gallery Plate hairlines. Navigation is a single floating pill bar at the center of the viewport — not a top bar, not a sticky header, not a sidebar. The density is paradoxical: visually dense with imagery, but the underlying UI is almost empty.

## Surfaces / Elevation

- **Gallery Plate**
- **Paper White**
- **Chalk**
- **Concrete**
- **Voltage Lime**

## Imagery

Imagery is the dominant content type and carries the brand identity entirely. The visual language is a surreal, curated 3D collage: scanned real-world objects (Porsche model, astronaut helmet, vinyl record, art book, Capsicum can, frisbee, printed ephemera) rendered or photographed and placed on the Gallery Plate canvas without shadows, grounding, or context. Objects are large, overlapping, slightly rotated, and extend beyond the viewport — they are not contained in cards. Treatment is high-key, evenly lit, with crisp edges against the gray field. The mix spans 3D renders, product photography, and scanned printed material (type on packaging, barcodes, record labels), creating a tactile, museum-archive feel. Icons in the UI are stroked at a thin-to-medium weight in Carbon, mono, and always circular or pill-shaped. Imagery is image-heavy at the page level, UI is nearly invisible by comparison — a deliberate inversion where the chrome retreats and the objects advance.

## Design Principles

### Do

- Apply Voltage Lime (#e2ff70) as a fill to exactly one action per screen — it is a rationed accent, not a decorative color
- Use the 9999px pill radius for every interactive control, label, and tag — the pill is the only shape language in the UI
- Set all type at weight 500 in ABCMonumentGrotesk with negative tracking near -0.48px, including headings — do not introduce a bold or light weight
- Let objects float directly on Gallery Plate (#e5e7eb) without card backgrounds, shadows, or frames — the canvas IS the container
- Keep the central nav bar the only persistent UI element; let every other surface be content
- Use 1px Gallery Plate hairlines for all borders and dividers — never go thicker
- Pair Voltage Lime fills with Carbon text only; never put the lime against Paper White or Chalk (contrast pair #000 → #e2ff70 = 18.8:1)

### Don't

- Do not introduce a second typeface, a second weight, or positive letter-spacing — the monochrome grotesque is the voice
- Do not add drop shadows, glows, or elevation tiers — the system is flat by design
- Do not use a chromatic fill other than Voltage Lime for any button or link — Concrete and Chalk are the only neutral fills
- Do not frame imagery in rounded cards or bordered containers — let objects touch the canvas directly
- Do not use the Oxide Brown (#68340e) as a UI color — it belongs inside imagery and printed artifacts only
- Do not stack more than two surface levels on a single screen (e.g. Chalk card on Gallery Plate is fine; a third nested card is not)
- Do not center-align body copy or use large type sizes — the system stays compact and left-aligned, max 22px

## Components

### Floating Central Nav Bar

A compact pill-shaped bar (9999px radius) floating at the visual center of any page, sitting directly on the Gallery Plate canvas. Contains a brand wordmark at 14-16px in Carbon, a circular black status pip, and a Menu control. Background uses Chalk (#f4f4f4) with a 1px Gallery Plate border. Functions as the only persistent UI element on the site.

### Menu Pill Button

9999px radius, 6-8px vertical padding, 12-16px horizontal padding. Filled with Voltage Lime (#e2ff70) with Carbon text at 14-16px weight 500. Trailing chevron or dot indicator. This is the system's one chromatic action — reserve it for the single most important action on any screen.

### Status Pip (Circular)

Small filled circle (~10-14px diameter), 9999px radius. Two variants: Carbon (default state) and Voltage Lime (active/highlighted). Used to punctuate nav bars, count badges, and inline status markers. No text, no border.

### Counter Badge

Small two-digit numeral (e.g. "01") in Carbon at 12-14px, set inside or beside a 9999px pill. Used to mark project indices, slide positions, and chapter numbers in editorial layouts.

### Ghost Link

Text-only link in Carbon at 14-16px, no underline at rest. On hover, background fills with Voltage Lime at 4px vertical / 8px horizontal padding with 9999px radius. The lime flash is the system's only hover affordance — keep it snappy and minimal.

### Object Tile (Floating Asset)

An image or 3D render presented without a card chrome — objects sit directly on the Gallery Plate canvas with no background fill, no shadow, no border. Optional 4px radius for any inline label. The absence of a card is the design: imagery IS the surface.

### Editorial Label Tag

9999px radius pill, Chalk (#f4f4f4) background, 4-8px vertical padding, 8-12px horizontal padding. Text in Carbon at 12-14px. Used to tag projects with discipline, year, or client. Sits inline with copy or floats near an object.

### Secondary Button (Neutral Pill)

9999px radius, Chalk (#f4f4f4) fill, 1px Gallery Plate border, Carbon text at 14-16px. For actions that need to exist but shouldn't compete with the Menu Pill. Use Concrete (#dedede) as a hovered/pressed state.

### Hairline Divider

1px line in Gallery Plate (#e5e7eb). The dominant border color in the system (1224+ uses as borderColor). Used between list items, around the nav bar, and as a soft section separator. Never heavier than 1px.

### Inverse Surface Block

Solid Carbon (#000000) background with Paper White text. Used sparingly for a single inverted panel or footer band — a moment of darkness inside the otherwise bright field. Padding 32-48px, 4px radius for any contained elements.

### Project Index Row

Full-width row separated by a 1px Gallery Plate hairline. Project title in Carbon at 16-18px left-aligned, index number ("01") or year right-aligned, optional Editorial Label Tag inline. Vertical padding 16-24px. Hovering fills the row with Chalk.

### Cursor Label / Tooltip

Tiny pill (9999px radius) in Carbon with Paper White text at 12px, shown on hover for interactive 3D objects. Sits offset from the cursor; functions as a nameplate for the object being inspected.

## Similar Design Systems

- {'why': 'Same floating-object-on-light-canvas approach, where 3D artifacts dominate the page and the UI retreats to a single minimal control', 'business': 'Resn'}
- {'why': 'Both treat the portfolio page as a curated 3D field with sparse, pill-shaped navigation floating over it', 'business': 'Active Theory'}
- {'why': 'Shared gallery-plate aesthetic — flat light gray canvas, tight grotesque type, and objects presented without card chrome', 'business': 'Studio Bruch'}
- {'why': 'Same constraint of a single typeface at one weight with negative tracking, and the same rationed use of one vivid accent against a near-monochrome field', 'business': 'Manual (design studio)'}
- {'why': 'Editorial restraint — maximalist content density paired with a near-invisible UI chrome, one chromatic highlight per page', 'business': 'Pentagram (partner sites)'}

## Agent Prompt Guide

Quick Color Reference
- canvas: #e5e7eb (Gallery Plate)
- text: #000000 (Carbon)
- border: #e5e7eb (Gallery Plate, 1px)
- surface: #f4f4f4 (Chalk)
- accent: #e2ff70 (Voltage Lime)
- primary action: #e2ff70 (filled action)

Example Component Prompts
1. Central Nav Bar: 9999px radius pill, #f4f4f4 background, 1px #e5e7eb border, floating at the visual center of the viewport. Brand wordmark "Twomuch.Studio" in #000000 ABCMonumentGrotesk weight 500, 14px, letter-spacing -0.48px. A 12px solid #000000 status pip sits inline. A Menu Pill button (9999px, #e2ff70 fill, #000000 text "Menu" at 14px) anchors the right side.

2. Ghost Link with Lime Hover: inline text "Read case" in #000000 ABCMonumentGrotesk 500 at 16px, no underline, letter-spacing -0.48px. On hover, background fills with #e2ff70, padding 4px 8px, 9999px radius. No color transition on the text — only the fill appears.

3. Project Index Row: full-width row on #e5e7eb canvas, 1px #e5e7eb hairline border-bottom, 20px vertical padding. Project title "Object Study No. 04" left-aligned in #000000 at 18px, year "2024" right-aligned in #000000 at 14px, inline #f4f4f4 pill tag "Editorial" at 12px. Hover fills the row with #f4f4f4.

4. Counter Badge "01": 9999px radius pill, 6px vertical / 10px horizontal padding, #000000 text at 12px ABCMonumentGrotesk 500, letter-spacing -0.48px. No background fill — sits directly on the canvas, used to mark project sequence or slide position.

5. Editorial Label Tag: 9999px radius pill, #f4f4f4 background, 4px 10px padding, #000000 text "Identity" at 12px, letter-spacing -0.48px. Sits inline with project metadata or floats near a 3D object on the canvas.

## Object-as-Content Rule

When a project, case study, or portfolio item is shown, present the artifact (3D render, photograph, scan) directly on the Gallery Plate canvas at large scale, without a card, border, or shadow. The object may overflow the viewport, overlap siblings, and rotate slightly. If a caption is required, use a Counter Badge or Editorial Label Tag placed at the object's edge, never a framed caption box. The 9999px pill IS the only container shape in the system.
