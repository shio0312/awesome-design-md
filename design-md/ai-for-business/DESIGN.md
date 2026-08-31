# AI for Business — Design System

> **North Star**: Brutalist editorial showroom on warm gray
> **Theme**: light
> **Source**: https://www.dayos.com
> **Refero Style**: https://styles.refero.design/style/ee403055-480e-4bd4-9216-07c9ae2dde2e
> **Synced**: 2026-09-01

## Overview

Dayos runs on a brutalist-editorial logic: near-monochrome canvas (#e5e5e5 page, #ffffff cards, #000000 blocks), oversized uppercase display type squeezed into 0.9 line-height, and zero shadows or gradients. The single chromatic accent is a pale mint green (#d1ffca) used sparingly on tags and links, with yellow (#fff100) as a near-neon highlight on small elements. Components are heavy on border-radius (24-64px on cards, 48px on nav pills) and light on decoration — flat surfaces, thin or zero borders, no elevation effects. Typography does all the emotional work: compressed condensed headlines at 130px tower over 16px body text, creating a dramatic scale ratio. The hero pairs a massive black headline with a 3D physical object render (textured cubes with brand labels), establishing a tactile, material-product feel against the clinical canvas.

## Color Palette

- **Carbon Black**: `#000000` — Primary text, inverted card surfaces, filled blocks — the structural dark that anchors the monochrome system [neutral]
- **Paper White**: `#ffffff` — Card surfaces, inverted text on dark blocks, icon fills — the bright counterpoint to carbon black [neutral]
- **Warm Canvas**: `#e5e5e5` — Page background, hero backdrop, section dividers — the slightly warm gray that distinguishes this from a clinical white canvas [neutral]
- **Mist Gray**: `#f3f3f3` — Secondary surface, nav pill backgrounds, subtle panels — one step lighter than canvas for quiet layering [neutral]
- **Ash**: `#c6c6c6` — Borders, hairlines, disabled states — mid-tone neutral for structural lines [neutral]
- **Smoke**: `#979797` — Body text secondary, meta labels, icon strokes — the muted text level for non-emphasized content [neutral]
- **Slate**: `#444444` — Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color [neutral]
- **Graphite**: `#2f2f2f` — Deep surface for code blocks or heavy accents — near-black alternative [neutral]
- **Mint Chip**: `#d1ffca` — Link backgrounds, tag pills, accent highlights — the signature pale green that punctuates the monochrome system [accent]
- **Voltage Yellow**: `#fff100` — Email highlights, small accent dots, decorative bursts — the high-energy chromatic note on micro-elements [accent]

## Typography

- **SuisseIntlCond**
- **SuisseIntl**
- **SuisseIntlMono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.6 |
| body-sm | 14 | — | 1.3 |
| body | 16 | — | 1.25 |
| subheading | 18 | — | 1.33 |
| subheading-lg | 20 | — | 1.2 |
| heading-sm | 28 | — | 1.3 |
| heading | 40 | — | 1.1 |
| heading-lg | 48 | — | 0.9 |
| display | 80 | — | 0.9 |
| display-xl | 130 | — | 0.9 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 16-24px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '64px', 'cards': '24-32px', 'buttons': '4-8px', 'nav-pill': '48px', 'large-cards': '64px'}

## Layout

Full-bleed warm gray (#e5e5e5) canvas with max-width ~1200px centered content. Hero is a split: massive 130px condensed headline on the left occupying ~50% width, 3D product render on the right. Nav is a floating pill centered in the 8rem top bar. Sections alternate between light canvas, white card surfaces, and full-width black inverted blocks. Content is primarily single-column or 2-column splits. Use case library is a card grid (2-3 columns). Footer is a compact dark band. Vertical rhythm uses 80px section gaps with 24px element spacing. No sidebar navigation. No sticky elements beyond the header.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Inverted**
- **Mist**

## Imagery

Photorealistic 3D renders of physical objects — textured concrete cubes with wood-grain elements, protruding colored geometric shapes (green, yellow, pink), and branded labels (SAP, Oracle, Workday logos printed on surfaces). The renders sit on the warm gray canvas like product photography in a gallery. No lifestyle photography, no stock imagery, no abstract gradients. The material/tactile treatment (concrete texture, wood grain) creates a physical-product feel that contrasts with the flat typographic UI. Icons are minimal — mostly monoline strokes in black or white. No decorative illustrations or iconography beyond functional UI markers.

## Design Principles

### Do

- Use SuisseIntlCond 700 at 48-130px with 0.9 line-height for all display headings — always uppercase, always tightly tracked
- Apply the warm canvas (#e5e5e5) as the page background, never pure white — the gray is the canvas tone that makes white cards feel lifted
- Use radius between 24-64px on cards; 48px on nav pills; 4-8px on buttons — the radius scale is large and deliberate
- Reserve #d1ffca (mint) for tags and link backgrounds; reserve #fff100 (yellow) for email highlights and micro-accents only
- Keep all cards flat — no shadows, no gradients. Depth comes from surface color contrast between canvas, white, and black
- Set nav height to 8rem with a floating pill-shaped container at 48px radius centered in the bar
- Use 16px/500 SuisseIntl for body text and button labels; 14px/500 for meta and list items

### Don't

- Never add box-shadows to cards or buttons — the system is explicitly flat
- Avoid pure white (#ffffff) as the page background — always use #e5e5e5 canvas beneath content
- Do not use chromatic colors for large surface fills — mint and yellow are accent-only, used on small elements
- Never set display heading line-height above 0.95 — the tight leading is what creates the compressed editorial block
- Do not use mixed-case for headings — all display and secondary headings are uppercase
- Avoid using SuisseIntlCond below 48px — the condensed face is designed for oversized display, not body text
- Never use subtle gray borders on cards — prefer surface color contrast over 1px borders for separation

## Components

### Filled Dark Button

Black (#000000) background, white (#ffffff) text, 8px radius, 16px 24px padding. SuisseIntl 16px/500. The high-contrast inverted treatment makes it the strongest interactive element on any page.

### Ghost Border Button

Transparent background, 1.5px solid border in #444444, #444444 text, 4px radius, 16px horizontal padding. SuisseIntl 16px/500. Restrained outlined variant for less critical actions.

### Text Link Button

No background, no border, #000000 text, 0-4px radius, underline on hover. SuisseIntl 16px/500. Used for 'More details' and similar low-weight navigation.

### Nav Pill

#ffffff background, 48px border-radius, wraps nav links in a floating capsule. Creates a physical 'pill' shape that separates nav from the canvas.

### Standard Card

#ffffff background, 24-32px border-radius, no shadow, no border. Padding 24px. The flat white surface against the warm gray canvas creates natural separation without elevation.

### Inverted Card

#000000 background, 32px border-radius, white text. No shadow. Used for high-impact sections that need to break the light canvas pattern.

### Top-Arc Card

64px 64px 0px 0px border-radius (top corners rounded, bottom corners flat). Creates a 'dome' shape that suggests the card emerges from below. Used in #000000 and #ffffff variants.

### Mint Tag

#d1ffca background, #000000 text, 64px radius (fully pill-shaped), small padding. The pale green pill is the signature accent element — used sparingly for taxonomy.

### Voltage Highlight

#fff100 background or text on select elements. Applied to email links and small accent marks. The high-saturation yellow against monochrome creates visual sparks.

### 3D Product Render

Textured concrete cubes with wood-grain and colored geometric protrusions, branded with SAP/Oracle/Workday logos. Photorealistic 3D renders on clean canvas. The physical/tactile material treatment contrasts with the flat UI.

### Uppercase Display Heading

SuisseIntlCond 700 at 80-130px, line-height 0.9, letter-spacing -0.03em, uppercase. The extreme size + tight leading + condensed width creates massive visual blocks of text that dominate the page.

### Secondary Heading

SuisseIntl 450 at 40px, uppercase, line-height 1.1, letter-spacing -0.02em. Lighter weight than display but still uppercase, bridging the brutalist display voice with readable content.

### Mono Label

SuisseIntlMono 400 at 12px, letter-spacing -0.03em. Used for 'Slide 1/2/3' indicators, metadata, and system labels. The monospace creates a technical/editorial counterpoint to the neo-grotesque body.

## Similar Design Systems

- {'why': 'Same approach of oversized condensed display type, monochrome canvas with single accent color, flat surfaces with zero shadows', 'business': 'Linear'}
- {'why': 'Similar full-bleed hero with massive headline, monochromatic palette, and large-radius card surfaces', 'business': 'Vercel'}
- {'why': 'Same editorial-brutalist typographic voice with uppercase condensed headings and minimal color palette', 'business': 'Cursor'}
- {'why': 'Shared warm-gray canvas approach, oversized display type, and accent color used sparingly on small functional elements', 'business': 'Arc Browser'}

## Agent Prompt Guide

Quick Color Reference:
- text: #000000
- background (canvas): #e5e5e5
- card surface: #ffffff
- border/hairline: #c6c6c6
- accent: #d1ffca (mint)
- primary action: no distinct CTA color

3 Example Component Prompts:

1. Create a hero headline: 130px SuisseIntlCond weight 700, uppercase, line-height 0.9, letter-spacing -3.9px, #000000 text on #e5e5e5 canvas background. The headline should read as 3-4 lines of compressed uppercase text occupying the left 50% of the viewport.

2. Create a content card: #ffffff background, 32px border-radius, no shadow, 24px padding, containing a 40px SuisseIntl weight 450 uppercase heading in #000000 and 16px body text in #444444. Place on #e5e5e5 canvas.

3. Create a mint tag pill: #d1ffca background, #000000 text, 64px border-radius, 8px 16px padding, 12px SuisseIntlMono weight 400 text. Use as a category label above card titles.

4. Create a top navigation bar: 8rem height, transparent #e5e5e5 background, containing a centered white pill at 48px border-radius with horizontal nav links in 16px SuisseIntl weight 500 #444444 text, 24px gap between links. Include a filled black 'Schedule a Demo' button (8px radius, #ffffff text) aligned right.

5. Create an inverted dark section: full-width #000000 background, 80px vertical padding, containing white text — a 80px SuisseIntlCond 700 uppercase headline followed by 16px #979797 body text. No shadows or gradients.
