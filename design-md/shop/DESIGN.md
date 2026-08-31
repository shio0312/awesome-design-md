# Shop — Design System

> **North Star**: Floating shopping constellation on white marble
> **Theme**: light
> **Source**: https://shop.app
> **Refero Style**: https://styles.refero.design/style/4fa67bd1-f01d-454a-b522-4a0359ff9815
> **Synced**: 2026-09-01

## Overview

Shop runs on a white-canvas discovery model where products float as large, heavily-rounded image cards instead of grid-locked thumbnails. The entire interface is pillow-soft: 20–28px radii everywhere, pill-shaped controls, a compact 16px GT Standard body with tight negative tracking that pulls text into crisp shapes. A single vivid violet (#5433eb) is the system's only saturated accent — it appears in the wordmark, the circular search submit, and as a tinted shadow on that same button. The rest of the palette is warm-neutral: white surfaces, a faint cool-gray canvas, hairline borders, and near-black text. Density stays compact with 12px gaps, but the hero and category bands breathe through generous 64–80px vertical rhythm, making commerce feel browsable rather than catalog-like.

## Color Palette

- **Canvas Mist**: `#f2f4f5` — Page background and secondary surface wash behind elevated cards [neutral]
- **Pure White**: `#ffffff` — Primary surface for cards, input fields, floating brand spotlights, and pill buttons [neutral]
- **Ink Black**: `#000000` — Primary text, headings, icons, nav symbols, and dark mode product cards [neutral]
- **Faint Border**: `#ebebeb` — Hairline dividers on cards, input outlines, and pill button borders [neutral]
- **Muted Gray**: `#787574` — Secondary text, navigation labels, icon strokes in idle state [neutral]
- **Cool Stone**: `#cccccc` — Placeholder fills, disabled states, and inactive icon backgrounds [neutral]
- **Warm Fog**: `#acb0aa` — Subtle surface tints for secondary product cards and section backgrounds [neutral]
- **Shop Violet**: `#5433eb` — Search submit button, wordmark dot, brand logo — the single accent that makes action and identity pop against the white canvas [brand]
- **Violet Wash**: `#c0b5f3` — Translucent halo behind the violet submit button, extending its glow without changing hue [brand]
- **Slate Ink**: `#332f2d` — Dark product card surfaces and deep-tone overlay text [neutral]
- **Ash Veil**: `#665a54` — Warm desaturated gray used in product imagery backdrops, not an active UI token [neutral]

## Typography

- **GT Standard**
- **Shopify Sans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.33 |
| body-sm | 12 | — | 1.33 |
| body | 14 | — | 1.33 |
| body-lg | 16 | — | 1.33 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 0px
- **Element Gap**: 12px
- **Section Gap**: 64px
- **Border Radius**: {'cards': '28px', 'chips': '9999px', 'pills': '20px', 'inputs': '9999px', 'search': '9999px', 'buttons': '9999px'}

## Layout

Max-width 1200px centered on a faint #f2f4f5 canvas, with a persistent 64px-wide left sidebar rail of icon-only navigation. The hero is a full-width band where product cards float above a centered violet 'shop' wordmark, with the pill search bar directly below. Category pills sit in a single centered row beneath the search. Content sections (Women, Men, Beauty, Home, Baby & Toddler) follow as labeled bands, each containing a 4-column card grid of product image tiles or a 2-column hero-and-grid composition. Vertical rhythm is generous: 64–80px between major sections. The footer is a dark band at the page bottom with columnar link groups. Right-side carousel arrows on horizontal product rails indicate scrollable content without pagination dots.

## Surfaces / Elevation

- **Canvas**
- **Surface**
- **Elevated Card**
- **Accent Product Image**

**Shadow tokens:**

## Imagery

Photography is the dominant visual: full-bleed product photography on white, 1:1 crops, and lifestyle imagery with warm earth-tone palettes (tans, terracotta, sage, ivory). Product images carry their own color — the UI stays achromatic so product hues become the visual variety. Brand logos appear as overlay type on dark or light hero images rather than separate badges. The hero composition arranges product cards as a floating, slightly overlapping constellation above the wordmark. Icons are minimal and mono (ink-black outlined strokes), except for category pill icons which use a single brand color each. No illustrations, no 3D, no gradients on product imagery.

## Design Principles

### Do

- Use 28px radius for all product cards and 9999px for all pills, inputs, and category chips — the generous rounding is the brand signature
- Set the violet (#5433eb) exclusively on the search submit button and the wordmark dot — it is the only saturated color in the system and must stay singular
- Type body text at 16px GTStandard-MRegular with -0.5px tracking, never smaller for primary content — 12px is the floor for secondary labels
- Pair every elevated card with the dual-layer soft shadow (0 4px 6px -1px + 0 2px 4px -2px at 10% black) — never use a single hard shadow
- Separate layers with shadow alone on white surfaces; skip borders on cards and rely on the canvas-to-card color shift
- Maintain 64–80px vertical breathing room between major content sections to preserve the airy, browseable feel
- Tint the search button's shadow with the brand violet (rgba(69,36,219,0.34)) so the accent color is reinforced in the elevation itself

### Don't

- Do not add a second saturated accent color — the system is monochrome with one violet, introducing a second will flatten its impact
- Do not use sharp corners on cards, buttons, or inputs — 0px radius is reserved for image edges only
- Do not use bold (700+) weights — the GTStandard family carries hierarchy through grade and tracking, not weight contrast
- Do not add visible borders to elevated cards — the shadow and white surface against the faint canvas do the separation work
- Do not use colored backgrounds for UI containers — the product photography provides all color in the experience
- Do not break the 9999px pill convention for any control that sits inline with text (search, category chips, cookie buttons)
- Do not set body text below 12px — 9px is reserved exclusively for review counts and brand metadata in tight cards
- Do not add gradients, illustrations, or decorative shapes — the visual language is product photography on white with soft shadows

## Components

### Hero Floating Product Card

White surface, 28px radius, 2-layer soft shadow (0 4px 6px -1px rgba(0,0,0,0.1) + 0 2px 4px -2px rgba(0,0,0,0.1)). Contains a 1:1 product image with its own 20px radius, brand name in 14px semibold ink-black beneath, and a 5-star rating row in 9px caption. Zero internal padding on the card; the image bleeds to the rounded edge.

### Brand Spotlight Card

White surface, 28px radius, same dual-layer soft shadow. A 1:1 product image fills the upper area with 20px inner radius. Below: brand name in 14px semibold, star rating and review count in 9px caption. No visible border; the shadow alone separates it from the canvas.

### Search Input with Violet Submit

Pill-shaped container at 9999px radius, white fill, 1px ink-black border at 0.1 opacity, 4px vertical / 20px left horizontal padding. Right side reserves 48px for a circular violet (#5433eb) submit button with a white arrow glyph. The violet button carries a tinted shadow: 0 4px 24px rgba(69,36,219,0.34). Placeholder text in 16px regular at muted gray.

### Category Pill

Pill at 9999px radius, white fill, 1px faint (#ebebeb) border, subtle elevation shadow (0 2px 8px rgba(0,0,0,0.06)). Left side: 16px circular category icon in its native brand color. Right: 16px GTStandard-MRegular label in ink-black. Horizontal padding 6px, vertical 6px.

### Product Image Tile

Tall or wide image fills the entire card with zero internal padding. The card itself has 0px radius in the grid context (image defines the shape). A semi-transparent white label box sits at the bottom-left with the product type in 14px semibold, 12px internal padding, and 12px radius on the label chip.

### Category Section Header

Left-aligned 20px GTStandard-MSemibold at -1.0px tracking in ink-black, followed by a 16px ink-black chevron. No background, no border. Sits above a 2-column or 4-column product grid with 24px bottom margin before the grid.

### Sidebar Nav Rail

Narrow vertical column (~64px wide), white background, no border. Each nav item is a 24px ink-black icon centered in a 48px square tappable area. Active state fills the icon container with #f2f4f5 at 20px radius. Profile avatar at the bottom is a 32px circle with a 1px #ebebeb ring.

### App Download Banner

Full-width dark band (#000000) at 48px height, 1px radius, white centered text. Contains a 24px rounded app icon, a 14px Shopify Sans link label reading 'Download Shop app', subtext 'Available on iOS & Android' at 10px, and a white right-pointing arrow. Sits flush against the top edge with zero internal margins beyond 12px horizontal.

### Cookie Consent Button

Pill at 9999px radius, white fill, 1px #ebebeb border. Black 12px semibold label centered. Padding 6px vertical, 16px horizontal. Shadow: 0 2px 8px rgba(0,0,0,0.06) for subtle lift on the white canvas.

### Category Carousel Arrow

Circular 32px white button with 0 4px 24px rgba(0,0,0,0.12) shadow. Contains a 16px ink-black right-chevron. Sits at the right edge of any horizontal product rail, vertically centered.

### Product Type Hero Image

Large rounded image (28px radius) filling roughly 60% of a category row. Brand name rendered in large white display type directly on the image at the top-left, followed by a star rating and review count in 14px white. No card chrome — the image IS the card.

### Mini Product Thumbnail Strip

Row of 3–4 small product images at ~48px square with 12px radius each, separated by 2px gaps. Sits at the bottom of a brand card as a quick-browse affordance. No labels, no borders — just the cropped product images.

### Cookie Modal Link

14px GTStandard-MRegular ink-black, underlined. No background, no border. Sits inline within body copy at standard line height.

## Similar Design Systems

- {'why': 'Same white-canvas product discovery model with image-first cards and minimal chrome around merchandise', 'business': 'Instagram Shopping'}
- {'why': 'Floating rounded product tiles, soft shadows, and a browseable constellation layout over a centered search affordance', 'business': 'Pinterest'}
- {'why': 'Large-format product imagery in heavily-rounded cards, compact 16px body type, and a single restrained accent color', 'business': 'SSENSE'}
- {'why': 'Generous 20–28px radii across all interactive surfaces and pill-shaped controls on a white canvas', 'business': 'Apple Shop'}
- {'why': 'Product-first discovery with elevated floating image cards, tight negative tracking on body type, and warm-neutral palette', 'business': 'Faire'}

## Agent Prompt Guide

Quick Color Reference:
- Background: #f2f4f5 (canvas), #ffffff (surface)
- Text: #000000 (primary), #787574 (secondary)
- Border: #ebebeb (hairline)
- Accent: #5433eb (Shop violet — wordmark + search submit)
- Shadow tint: rgba(69,36,219,0.34) for the violet button only
- primary action: #5433eb (filled action)

Example Component Prompts:

1. Create the hero search bar: 9999px radius pill, #ffffff fill, 1px border in rgba(5,41,77,0.1). Placeholder 'What are you shopping for today?' in 16px GTStandard-MRegular at #787574. Right-aligned circular submit button in #5433eb with a white right-arrow glyph, 48px diameter, shadow 0 4px 24px rgba(69,36,219,0.34). The input padding is 4px vertical, 20px left, reserving 48px right for the submit.

2. Create a floating brand spotlight card: 28px radius, #ffffff fill, dual shadow (rgba(0,0,0,0.1) 0 4px 6px -1px + rgba(0,0,0,0.1) 0 2px 4px -2px). Top half: 1:1 product image at 20px inner radius filling to the card edges. Below: brand name in 14px GTStandard-MSemibold at #000000 with -0.2px tracking, followed by a 9px star-rating row at -0.5px tracking. No card padding, no border.

3. Create a category pill chip: 9999px radius, #ffffff fill, 1px #ebebeb border, shadow rgba(0,0,0,0.06) 0 2px 8px. Left: 16px circular category icon in its native color. Right: 16px GTStandard-MRegular label in #000000 with -0.5px tracking. Padding 6px vertical, 6px left, 16px right.

4. Create a category section header: 20px GTStandard-MSemibold at -1.0px tracking in #000000, followed by a 16px #000000 right-chevron, left-aligned. 24px bottom margin before the 4-column product grid beneath.

5. Create the left sidebar nav: 64px-wide vertical rail, #ffffff fill, no border. Each item is a 24px #000000 icon centered in a 48px tap target. Active state fills a 20px-radius background of #f2f4f5 behind the icon. Profile avatar at bottom: 32px circle with 1px #ebebeb ring.

## Typography Hierarchy Rules

The GT Standard family carries its entire hierarchy through three grades (Regular, Medium, Semibold) and negative tracking — never through weight contrast alone. Display and heading sizes use aggressive tracking tightening (-1.0px at 20px, -0.5px at 16px), while micro-labels relax to -0.2px. This creates a visual compression effect: big text pulls tight, small text breathes. Always pair size with the correct family grade: 16px body is Regular, 14px subheadings are Semibold, 12px meta is Medium. Never mix grades within a single text run — a label and its value must use the same family grade for visual coherence.

## Product Card Composition

Product cards are image-first: the image defines the card's visual identity, and type is a supporting label beneath or overlaid on the image. White product cards stack the image on top with type below in a 12–16px gap. Dark product cards reverse this — brand name in large display type overlays the image at the top-left in white. The card radius (28px) is always larger than the inner image radius (20px) by ~8px, creating a subtle white frame effect even on white-background product images. Never crop a product image to the card's exact rounded shape — the inner 20px radius provides a visible white border that separates the product from the card edge.
