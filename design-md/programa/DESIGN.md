# Programa — Design System

> **North Star**: Swiss design studio at high noon. A white gallery wall lit by a single yellow desk lamp — everything is grayscale until a button, badge, or highlight demands attention, and then that one yellow note carries the whole room.
> **Theme**: light
> **Source**: https://programa.design
> **Refero Style**: https://styles.refero.design/style/41af8353-6a8f-416d-947b-57932f591497
> **Synced**: 2026-09-01

## Overview

Programa operates in a Swiss-design vocabulary: near-pure white canvas, architectural sans-serif type at tightly tracked small-to-medium sizes, hairline borders, and a single saturated yellow-green accent that functions as a highlighter pen across an otherwise austere page. The entire palette is essentially four grays plus one chromatic signal — chromatic real estate is rationed, not distributed, so when yellow appears it reads as a switch flipped on. Components are slim and confident: 10px radii, thin 1px borders, generous white space, and zero shadow noise. The aesthetic is editorial-portfolio meets productivity tool — restrained enough to feel serious, bold enough to feel like a designer's tool.

## Color Palette

- **Ink Black**: `#1a1a1a` — Primary text, all borders, icon strokes, logo, divider lines, button outlines — the structural ink that defines every shape on the page [neutral]
- **Paper White**: `#ffffff` — Page canvas, card surfaces, text on dark fills, input fields [neutral]
- **Fog Gray**: `#f4f4f4` — Soft section background, alternate surface, and quiet card fill [neutral]
- **Ash Gray**: `#a3a3a3` — Muted secondary text, inactive links, placeholder copy, tertiary metadata [neutral]
- **Highlighter Yellow**: `#fbff2b` — Primary action background, focus highlights, tag fills — the single chromatic accent that makes interactive elements feel switched on against the monochrome system [brand]

## Typography

- **Neue Haas Grotesk Text**
- **neue-haas-grotesk-text**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.4 |
| body-sm | 16 | — | 1.4 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.2 |
| heading | 42 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 12px
- **Section Gap**: 96px
- **Border Radius**: {'nav': '10px', 'cards': '16px', 'inputs': '10px', 'buttons': '10px'}

## Layout

Centered max-width layout (~1200px) with generous side margins (111px+). The header is a flat white bar with no border, logo left, centered nav cluster, auth actions right. Content pages lead with a single large 42px left-aligned heading, followed by a full-width Fog Gray info banner, then a vertically stacked numbered content list that uses bold lead-in labels + paragraphs. Section separation is 48-96px vertical padding. No alternating bands, no sidebar, no grid cards on content pages — the rhythm is a single column of breathing white space punctuated by sparse structural elements.

## Surfaces / Elevation

- **Canvas**
- **Fog Card**
- **Accent Fill**

## Imagery

Pure UI with no photography or illustration on this page — the visual language is typographic and structural. Logo is the only graphic mark, rendered as two solid Ink Black geometric shapes (diamond/parallelogram forms). The highlighter-yellow CTA is itself a visual element: a stamped sticker on the white canvas. No icons, no avatars, no product screenshots on the Acceptable Use Policy page. When imagery does appear elsewhere, expect it to be contained within sharp or slightly rounded crops, full-bleed product photography on pure white, and monochromatic or single-accent treatment consistent with the palette.

## Design Principles

### Do

- Use #fbff2b fill with 1px #1a1a1a border exclusively for the single primary action per screen — never use the yellow as a background for large surfaces or decorative blocks.
- Set all text at -0.03em letter-spacing using the Neue Haas Grotesk Text scale (14/16/17/20/24/42px) — do not introduce a second typeface or loosen tracking at display sizes.
- Apply 10px border-radius to buttons, nav elements, and inputs; reserve 16px for larger card surfaces and info banners.
- Build vertical rhythm on the 6px base unit: 8px between list items, 12px for element gaps, 16px for card padding, 48-96px for section separation.
- Use #f4f4f4 as the only mid-surface between white and the yellow accent — never introduce additional gray tints or gradient washes.
- Keep page layout centered with a 1200px max-width and 111px left margin for content blocks; let white space carry the visual weight.
- Communicate hierarchy through weight (400 vs 500), not color or size variation — the system has exactly two weights and a tight type scale.

### Don't

- Don't introduce drop shadows, glow effects, or blur — elevation is flat and border-defined.
- Don't use #fbff2b on more than one element per viewport — its power comes from scarcity.
- Don't add a second accent color; the palette is monochrome + one yellow-green signal.
- Don't use Ash Gray (#a3a3a3) for body copy — it's a 2.5:1 contrast fail on white; reserve it for placeholders and inactive metadata only.
- Don't increase border-radius above 16px — the slightly squared geometry is part of the identity.
- Don't break the 6px spacing grid with arbitrary pixel values; every gap should be a multiple of 6.
- Don't add a subtitle or eyebrow text above page headings — the 42px heading stands alone.

## Components

### Top Navigation Bar

White background, no border-bottom. Left: geometric two-diamond logo (Ink Black) + 'Programa' wordmark at 16-20px weight 400. Center: nav links (Product, Customers, Pricing, Learn) at 16px weight 400, Ink Black, 24px horizontal spacing. Right: 'Log in' as a text link in Ink Black, then a Primary CTA Button. Height feels ~64px with generous horizontal padding.

### Primary CTA Button

Highlighter Yellow (#fbff2b) fill, 1px Ink Black (#1a1a1a) border, 10px border-radius, 8px vertical / 12px horizontal padding. Label in Neue Haas Grotesk Text 16px weight 400, Ink Black. 12px gap between sibling buttons. The 1px black outline around a yellow fill gives the button a hand-stamped, sticker-like quality — it's the only place a border reinforces rather than contains.

### Ghost Text Button

No fill, no border. Label in Neue Haas Grotesk Text 16px weight 400, Ink Black. Sits to the left of the Primary CTA. Vertically aligned to the same baseline as the CTA.

### Page Heading

Neue Haas Grotesk Text 42px weight 500, Ink Black, line-height 1.10, letter-spacing -1.26px. Left-aligned with 111px left margin. No subtitle, no eyebrow — the heading stands alone.

### Info Banner

Fog Gray (#f4f4f4) fill, no border, 16px border-radius. Padding ~12px vertical / 16px horizontal. Content is a label-value pair: bold label ('Last Updated:') in Ink Black weight 500, followed by value in Ink Black weight 400, both at 16px.

### Numbered Section Block

Decimal number (1., 2., …) flush left at 16px Ink Black weight 400. Indented label (e.g. 'Purpose and Scope') in 16px weight 500 Ink Black. Body paragraphs in 16-17px weight 400 Ink Black at line-height 1.4. Vertical gap between sections: 8px. The bold label + paragraph pattern is a signature — it's the page's only typographic hierarchy device.

### Logo Lockup

Two stacked diamond/parallelogram shapes in Ink Black, approximately 24x24px, followed by 'Programa' wordmark in Neue Haas Grotesk Text 20px weight 400, Ink Black, letter-spacing -0.6px. 8px gap between icon and wordmark.

### Form Input

1px Ink Black border, 10px border-radius, 6px vertical / 12px horizontal padding. Placeholder text in Ash Gray (#a3a3a3) at 16px. White fill. On focus: border remains Ink Black (no color shift) — the focus state is communicated through weight or ring, not hue.

### Nav Link

Neue Haas Grotesk Text 16px weight 400, Ink Black, no underline, no color shift on hover visible in data. 24px horizontal spacing between links. 4px column gap from the wordmark.

### Footer Link

Neue Haas Grotesk Text 14-16px weight 400, Ink Black, muted compared to nav. Typically arranged in columns with 8-12px vertical gap between links.

## Similar Design Systems

- {'why': "Same near-monochrome palette with a single saturated accent (Linear's purple), tight typographic system, and minimal-border component geometry", 'business': 'Linear'}
- {'why': 'Same Swiss-design restraint with hairline borders, generous white space, and a single chromatic accent used sparingly for primary actions', 'business': 'Figma Config'}
- {'why': 'Similar flat-no-shadow component language, 10px-ish radii, and a neutral-first palette where one accent color carries the brand', 'business': 'Notion'}
- {'why': 'Same editorial minimalism with monochrome canvas, tight tracking on a neo-grotesque typeface, and accent color rationed to CTAs only', 'business': 'Vercel'}
- {'why': 'Same white-canvas-plus-muted-neutral aesthetic with type-driven hierarchy and zero decorative chrome', 'business': 'Are.na'}

## Agent Prompt Guide

Quick Color Reference:
- text: #1a1a1a
- background: #ffffff
- surface: #f4f4f4
- border: #1a1a1a
- muted text: #a3a3a3
- primary action: #fbff2b (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #fbff2b background, #1a1a1a text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a page heading block: 42px Neue Haas Grotesk Text weight 500 #1a1a1a, line-height 1.10, letter-spacing -1.26px, left-aligned with 111px left margin. Below it, an info banner: #f4f4f4 fill, 16px radius, 12px 16px padding, containing 'Last Updated:' in 16px weight 500 #1a1a1a followed by 'January 1, 2026' in 16px weight 400 #1a1a1a.

3. Create a numbered content section: decimal number '1.' in 16px weight 400 #1a1a1a flush left, then a bold lead-in label in 16px weight 500 #1a1a1a, then a body paragraph in 17px weight 400 #1a1a1a at line-height 1.40. 8px vertical gap to the next section.

4. Create a form input: 1px #1a1a1a border, 10px radius, #ffffff fill, 6px 12px padding. Placeholder 'Enter your email' in 16px #a3a3a3. Label above in 14px weight 500 #1a1a1a with 8px bottom margin.

5. Create a secondary card surface: #f4f4f4 fill, 16px border-radius, 24px padding, no border, no shadow. Heading inside in 20px weight 500 #1a1a1a, body in 16px weight 400 #1a1a1a, 12px gap between heading and body.
