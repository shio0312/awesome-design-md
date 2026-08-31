# Integrated Biosciences — Design System

> **North Star**: bioluminescent laboratory at midnight
> **Theme**: mixed
> **Source**: https://integratedbiosciences.com
> **Refero Style**: https://styles.refero.design/style/80099f79-72b7-4367-b2e9-6a3d4a3e9e6a
> **Synced**: 2026-09-01

## Overview

Integrated Biosciences operates in a darkroom-laboratory visual language: a near-black canvas with cool green undertones, restrained white typography, and a single bioluminescent lime accent that activates only on small interactive elements like arrow buttons, tag dots, and progress indicators. The entire type system runs on a single weight of Aspekta — hierarchy is sculpted purely through size and aggressive negative letter-spacing, which makes 111px and 158px display lines feel architectural rather than decorative. Roboto Mono is reserved for technical labels, nav items, and metadata, reinforcing the instrumentation-bench character of the brand. Surfaces stay mostly flat — no shadows, no gradients — with thin hairline borders in #c9cbbe or #4d5757 doing all the delineation. Light sections flip to a warm off-white canvas (#f7f7f5) with white cards, but the green accent persists as a constant biological signal.

## Color Palette

- **Bioluminescent Lime**: `#cef79e` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content [accent]
- **Abyssal Ink**: `#222f30` — Primary text, borders, dark canvas sections, nav backgrounds. Near-black with a cool green undertone — it is not pure black, it carries the same green note as the accent. Darkest content surface [neutral]
- **Bone White**: `#f7f7f5` — Light-section page canvas, hero/section backgrounds when in light mode. Warm off-white with the faintest cream cast [neutral]
- **Paper**: `#ffffff` — Card surfaces on light sections, elevated containers, icon fills, body text on dark surfaces. The brightest surface in the system [neutral]
- **Graphite**: `#4d5757` — Secondary body text, muted metadata, subdued borders, ghost button outlines. Mid-tone with a green undertone matching the system [neutral]
- **Lichen**: `#c9cbbe` — Hairline borders, subtle dividers, placeholder metadata text. Warm desaturated green-beige that disappears on white but is visible on #f7f7f5 [neutral]
- **Tissue**: `#e7e8e1` — Alternate card surface — warmer light gray used to differentiate secondary cards or muted content blocks from the white primary surface [neutral]
- **Frost**: `#eeeeee` — Neutral light card surface when a non-warm alternate is needed [neutral]
- **Void**: `#000000` — Footer background, pure black anchors. Used sparingly as a true neutral when the Abyssal Ink is too colored [neutral]

## Typography

- **Aspekta**
- **Roboto Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.23 |
| body | 18 | — | 1.3 |
| body-lg | 22 | — | 1.3 |
| subheading | 24 | — | 1.2 |
| heading-sm | 36 | — | 1.2 |
| heading-lg | 58 | — | 1.1 |
| display | 75 | — | 1.1 |
| display-lg | 89 | — | 1.1 |
| display-xl | 111 | — | 1 |
| hero | 158 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 40px
- **Element Gap**: 8-20px
- **Section Gap**: 80-120px
- **Border Radius**: {'nav': '12px', 'tags': '9999px', 'cards': '16-20px', 'buttons': '8px', 'largeCards': '40px'}

## Layout

Max-width 1200px centered for all content. Dark sections (hero, 'What We Do', platform) are full-bleed in Abyssal Ink with content constrained to the 1200px column and generous left-padding for text. Light sections (Newsroom) are full-bleed in Bone White with the same 1200px content column. Hero is asymmetric: headline occupies the left two-thirds, large amounts of right-side and bottom negative space. Section rhythm alternates: dark band → dark band → light band, with no dividers between same-mode sections. Card layouts are two-column (image-left, text-right) for editorial blocks, and single-column stacked for text-heavy content. Navigation is a single horizontal bar — logo left, nav links right, with a pill-shaped active indicator. No sticky header, no sidebar, no mega-menu — the navigation is intentionally minimal so the content commands attention.

## Surfaces / Elevation

- **Page Canvas — Light**
- **Page Canvas — Dark**
- **Card Surface — Light**
- **Card Surface — Warm Alternate**
- **Accent Fill**
- **Footer Ground**

## Imagery

Scientific microscopy and 3D molecular renders dominate — cell clusters, protein structures, and neural networks rendered in a single dark-green-to-black palette so they integrate with the Abyssal Ink canvas. Photography is not used; all imagery is generated or illustrated. Imagery is always contained within rounded rectangles (radius 12–16px) and paired with white cards. The green Bioluminescent Lime is echoed in the imagery's highlights, creating visual continuity between the interface accent and the scientific subject matter. The Newsroom section's lead image is a tight crop of glowing cell structures on black — full-bleed within the card, with no text overlay, letting the subject speak.

## Design Principles

### Do

- Use Aspekta at weight 400 for all display and body text — never bold, never semibold, never italic. Hierarchy is size and tracking only.
- Set Bioluminescent Lime (#cef79e) fills at exactly 40×40px for arrow buttons and 6px diameter for tag dots. Never scale the accent larger than a micro-surface.
- Apply letter-spacing proportionally: -0.03em at 158px, -0.02em at 89–111px, -0.006em at 36–42px, -0.001em at 16–19px. The tracking is what keeps the flat weight readable at extreme sizes.
- Use 1px hairlines in #c9cbbe (on light) or #4d5757 (on dark) for all dividers and card borders. Never use thicker borders, never use shadows for depth.
- Reserve Roboto Mono for nav items, section counters (01/02), publication tags, dates, and button text. Never use it for headlines or body copy longer than a label.
- Maintain 80–120px vertical section gaps. The system breathes — compression destroys the lab-instrument calm.
- Pair every action with its opposite surface: dark button (#222f30 fill) on light canvas, light button (#ffffff fill) on dark canvas. Never use Bioluminescent Lime as a primary button background.

### Don't

- Do not introduce a second weight of Aspekta or any other sans-serif for headings. The single-weight system is the brand's identity — adding bold breaks it.
- Do not use #cef79 as a background for body text, large surfaces, gradients, or hero overlays. The accent is rationed at micro-scale for a reason.
- Do not apply box-shadows, drop-shadows, or any elevation effect. Depth comes from color contrast and borders only.
- Do not use pure #000000 for content sections — reserve it for the footer. Content dark surfaces are #222f30 with its green undertone.
- Do not use the warm neutrals (#e7e8e1, #c9cbbe) on dark sections. They disappear against Abyssal Ink and break the surface hierarchy.
- Do not place images outside of rounded containers (minimum radius 12px) or without the dark scientific treatment. Lifestyle photography breaks the lab-instrument language.
- Do not use multiple accent colors. The system's power is in monochrome discipline plus one signal. Adding a second chromatic role dilutes the brand's visual tension.

## Components

### Hero Display Headline

Set in Aspekta 400 at 111–158px, line-height 1.0, letter-spacing -0.03em. White (#ffffff) on Abyssal Ink (#222f30). Left-aligned, no max-width constraint — the line breaks are generous. Period-terminated. This is the single largest typographic element in the system and sets the brand's architectural tone.

### Section Sub-Headline

Aspekta 400 at 36–42px, line-height 1.2, letter-spacing -0.006em. Rendered in muted Graphite (#4d5757) on dark backgrounds, or Abyssal Ink on light. Reads as a quiet, reflective counterpoint to the hero — the voice of the researcher explaining, not announcing.

### Pill Navigation Button

Outlined pill shape, border 1px in #c9cbbe on dark surfaces or #4d5757 on light, radius 12px. Roboto Mono 13–14px at 400, letter-spacing -0.02em. Text in matching border color. When active, fills with Bioluminescent Lime (#cef79e) and text flips to Abyssal Ink.

### Filled Action Button (Work With Us)

Filled rectangle, background #222f30 (dark) or #ffffff (light), text in opposite surface color. No border. Radius 8px. Roboto Mono 13–14px uppercase tracking -0.02em. Compact horizontal padding ~12-16px, vertical 8px. Restrained size — this system does not shout with button scale.

### Arrow CTA Button

40×40px square, radius 8px, filled Bioluminescent Lime (#cef79e) with Abyssal Ink arrow icon. Used at the end of card titles, section footers, and inline links. This is the only place the green accent fills a shape — it functions as a green traffic light pointing forward.

### Outlined Ghost Button (Discover Our Platform)

Transparent background, border 1px in #4d5757, text in #ffffff or #222f30. Radius 8px. Roboto Mono 14px. Pairs with the Arrow CTA button when two actions sit side by side.

### Section Counter (01/02)

Small pill containing a section number, border 1px in #4d5757, radius 9999px. Roboto Mono 13px. Sits above or beside the section headline as a navigational anchor — the table-of-contents voice of the page.

### News Article Card

White (#ffffff) surface on Bone White (#f7f7f5) canvas, radius 20–40px, no shadow. 40px internal padding. Two-column layout: left half is a dark full-bleed scientific image (radius 12-16px on the image itself), right half is title + meta + excerpt + 'READ ARTICLE' link. Generous breathing room — this card occupies a full viewport-width band.

### Publication Tag

Small green-dot prefix + Roboto Mono uppercase label. Dot is 6px Bioluminescent Lime circle. Label in Roboto Mono 13px in #4d5757 or #c9cbbe. Functions as the system's only color-coded classification marker.

### Hero Section Background

Full-bleed Abyssal Ink (#222f30). No gradient, no texture. Headline left-aligned in upper third, supporting text left-aligned in lower third. Massive vertical breathing room — minimum 400px of negative space between headline and copy.

### Light Section Background

Full-bleed Bone White (#f7f7f5) with white cards. Used for editorial/newsroom sections, creating a flip from the dark content sections. The transition itself is the visual signal — no divider line is needed.

### Hairline Divider

1px line in #c9cbbe (on light) or #4d5757 (on dark). Full width or column-width. The system uses only horizontal dividers — never vertical, never double, never dashed.

### Footer

Pure black (#000000) background — a deeper note than the Abyssal Ink used in content sections. White text, Roboto Mono for links, Aspekta for any larger text. Signals the absolute end of the site.

## Similar Design Systems

- {'why': 'Dark green-black canvas with single vivid accent, oversized single-weight display type, biotech/scientific instrumentation aesthetic', 'business': 'Arc Institute'}
- {'why': 'Near-black backgrounds, bioluminescent accent color, flat minimal surfaces, single-weight large display typography in a bio/AI context', 'business': 'Chai Discovery'}
- {'why': 'Dark-mode biotech interface, extreme type-size contrast between tiny mono labels and massive sans-serif display lines, hairline borders, single accent color', 'business': 'EvolutionaryScale'}
- {'why': 'Oversized single-weight display headlines, generous negative space, muted secondary text color, minimal surface decoration', 'business': 'Notion AI landing pages'}
- {'why': 'Dark canvas with hairline borders, single accent color used sparingly on interactive elements, mono labels for technical metadata', 'business': 'Linear'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #222f30 (dark) / #ffffff (on dark)
- background: #f7f7f5 (light) / #222f30 (dark)
- border: #c9cbbe (light) / #4d5757 (dark)
- accent: #cef79e
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Hero Headline**: Full-bleed #222f30 background. Headline at 158px Aspekta weight 400, color #ffffff, line-height 1.0, letter-spacing -4.74px. Period-terminated, left-aligned, 80px from nav.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

3. **News Article Card**: White (#ffffff) card on #f7f7f5 canvas, radius 20px, 40px padding. Two-column: left = dark scientific image with 16px radius, right = publication tag (6px #cef79e dot + Roboto Mono 13px 'PUBLICATIONS'), date in Roboto Mono 13px #c9cbbe, headline at 36px Aspekta 400 #222f30 letter-spacing -0.22px, excerpt at 18px #4d5757, 'READ ARTICLE' link in Roboto Mono 13px.

4. **Section with Counter**: Dark #222f30 band. Pill counter '01 / 02' with 1px #4d5757 border, 9999px radius, Roboto Mono 13px #4d5757. Headline at 42px Aspekta 400 #4d5757, letter-spacing -0.5px, line-height 1.2, max-width 600px, left-aligned 50% from left edge.

5. **Ghost Navigation Button**: Transparent fill, 1px border in #c9cbbe, radius 12px, padding 8px 16px, Roboto Mono 13px #c9cbbe, letter-spacing -0.26px. When active, fill flips to #cef79e and text to #222f30.

## Type System Philosophy

The entire system runs on a single weight (400) of Aspekta. This is not a limitation — it is the brand's defining choice. Weight variation is deliberately absent; hierarchy is sculpted by three tools: size (16px to 158px), line-height compression (1.3 at body, 1.0 at display), and letter-spacing tightening (-0.001em at body, -0.03em at hero). The result reads as a scientific monograph — flat, precise, and unornamented. Roboto Mono enters only for technical metadata: nav labels, section counters, publication tags, dates, and button text. The mono's geometric rigidity against Aspekta's humanist curves creates the system's only typographic contrast.

## Accent Discipline

The Bioluminescent Lime (#cef79e) is rationed. It appears on: 40×40 arrow buttons, 6px tag dots, active nav pills, and progress indicators. It never fills a large surface, never sits behind body text, never appears in gradients. The discipline is the point — when green appears, the eye locks onto it because the rest of the interface is monochrome. Treat it as a signal lamp: on = active, forward, or biological.
