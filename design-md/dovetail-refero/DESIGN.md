# Dovetail — Design System

> **North Star**: Blueprint grid under a black moon — faint graph lines, white type, one violet spark.
> **Theme**: dark
> **Source**: https://dovetail.com
> **Refero Style**: https://styles.refero.design/style/108e2695-6970-47d5-b5b0-eea8fc34e048
> **Synced**: 2026-09-01

## Overview

Dovetail operates in a midnight command-center language: a near-black canvas structured by a faint blueprint grid, with white type and a single soft indigo accent. Surfaces stack from pure black to charcoal, each step subtle enough to feel like elevation through luminance rather than shadow. The system is compact and data-dense — Inter carries every reading load, JetBrains Mono stamps categorical labels, and 8px radii keep containers crisp rather than soft. Color is rationed: most of the interface stays achromatic, with #6798ff appearing only as functional punctuation on icons, stat markers, and chart elements.

## Color Palette

- **Soft Indigo**: `#6798ff` — Brand accent — iconography, stat markers, chart series, link states; the single chromatic note in an otherwise achromatic system [brand]
- **Pure Black**: `#000000` — Deepest surface — modal backdrops, full-bleed image fills, inline SVG fills [neutral]
- **Carbon**: `#0a0a0a` — Page canvas — the primary background; near-black with no warmth [neutral]
- **Graphite**: `#141414` — Card surface — one step above the canvas to delineate content blocks [neutral]
- **Iron**: `#1e1e1e` — Elevated surface and border — secondary cards, table rows, subtle dividers [neutral]
- **Slate Edge**: `#313131` — Hairline borders on imagery and nested elements — visible but recessive [neutral]
- **Smoke**: `#454545` — Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color [neutral]
- **Mist**: `#7c7c7c` — Disabled or low-emphasis button text [neutral]
- **Ash**: `#a7a7a7` — Secondary text — captions, metadata, helper text, muted labels [neutral]
- **Bone**: `#ffffff` — Primary text, icons, filled CTA background, card surface inverts; the dominant light element in the dark system [neutral]

## Typography

- **Inter**
- **JetBrains Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.4 |
| body-sm | 14 | — | 1.57 |
| body | 16 | — | 1.5 |
| heading-sm | 20 | — | 1.33 |
| heading | 24 | — | 1.29 |
| heading-lg | 40 | — | 1.2 |
| display-sm | 56 | — | 1.14 |
| display | 64 | — | 1.13 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '4px', 'cards': '8px', 'inputs': '8px', 'buttons': '8px', 'navPills': '9999px'}

## Layout

Full-bleed dark sections separated by 80px vertical gaps, all content constrained to a 1200px max-width centered container. The hero uses a two-column split: headline + subtext + dual CTAs on the left, a product dashboard preview on the right, both on the gridded dark canvas. Sections alternate between text-left/visual-right patterns and centered stat blocks (3-column grid for KPI rows with large numeric values). Navigation is a top bar with pill-shaped nav links and a high-contrast filled CTA on the far right. The footer is a multi-column link grid organized by category labels in JetBrains Mono, set against the same dark canvas without a visual separator from the page body.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Elevated**
- **Border**
- **Inverted**

## Imagery

The visual language is dominated by a faint blue-gray grid pattern that fills the dark canvas like architectural graph paper — it recedes into the background and provides spatial orientation without competing with content. Product preview mockups (dashboard panels, bar charts, data tables) are the primary illustrative element, rendered in the same dark palette so they feel native to the page. Icons are small, monochromatic, and outlined at ~1.5px stroke weight, occasionally accented with the #6798ff indigo for stat markers and chart legends. Customer logos in the trust strip are presented as flat monochrome marks on the dark background. There is no lifestyle photography; the product IS the hero.

## Design Principles

### Do

- Use #0a0a0a as the universal page background — never pure white or lighter charcoal for the main canvas.
- Stack surfaces at #000000 → #0a0a0a → #141414 → #1e1e1 → #313131 to communicate elevation through luminance, not shadow.
- Apply #6798ff only to functional accents (stat icons, chart series, link hovers) — never as a large fill or background wash.
- Set headings in Inter 400–500 with negative letter-spacing scaling from –0.036em at 64px to –0.012em at 20px.
- Stamp section eyebrows in JetBrains Mono 12px, uppercase, with +0.071em tracking and #a7a7a7 color.
- Use 8px as the default radius for buttons, cards, and inputs; reserve 4px for inline tags and micro-elements.
- Pair every primary CTA (white fill) with a ghost secondary (transparent + #454545 border) in the same action group.

### Don't

- Do not introduce a second chromatic accent — the system runs on one indigo; adding green, red, or warm tones dilutes the signal.
- Do not use drop shadows for elevation; depth comes from surface stepping, not box-shadow.
- Do not center-align body copy — left-align paragraphs and descriptions; reserve center-align for headlines and stat blocks.
- Do not use display sizes below 40px in Inter; if something needs to be smaller than body, switch to JetBrains Mono for the label feel.
- Do not round buttons beyond 8px; the 8px radius is the system signature — full pills are reserved for navigation links.
- Do not place colored fills (other than #6798ff on small marks) over the dark canvas; the page should read as black-and-white with one violet spark.
- Do not use #ffffff as a surface or card background except inside the inverted CTA button; white is reserved for text and primary actions.

## Components

### Primary Button (Filled)

White background (#ffffff), black text (#0a0a0a), 8px radius, 8px 16px padding, Inter 14px/500. Used for "Contact sales" and "Request a demo". The inverted treatment against the dark canvas creates maximum contrast — it is the only high-luminance element on most pages.

### Secondary Button (Ghost)

Transparent background, 1px #454545 border, white text, 8px radius, 8px 16px padding, Inter 14px/500. Used for "Try Dovetail free". Reads as the same action class as the primary but defers visual weight.

### Navigation Pill

Rounded pill shape (9999px radius), transparent background, white text, 8px 14px padding, Inter 14px/500. Product, Use cases, Resources, Enterprise, Customers, Pricing all use this shape. Sits flush on the dark canvas without a border.

### Nav CTA Group

"Log in" as plain text link beside a filled white "Contact sales" button. The pair establishes a clear hierarchy: passive text for existing users, high-contrast action for new ones.

### Dashboard Preview Card

Charcoal surface (#141414) with #1e1e1 borders, 8px radius, 24px padding. Contains a header bar (icon + title + tab toggle), a date-range selector, a bar chart with multi-color series, and a sortable data table below. The card demonstrates the product's actual interface — it is rendered, not illustrated.

### Stat Block

Large numeric value in Inter 40px/500 white, preceded by a small #6798ff icon (up-arrow, clock, speedometer), followed by a bold white label (16px/500) and a descriptive caption in #a7a7a7 (14px/400). Three blocks sit in a row with even spacing, centered within the content width.

### Section Eyebrow Label

JetBrains Mono 12px/400, uppercase, +0.85px letter-spacing, #a7a7a7 color. Sits 24–32px above the section heading. Examples: "HOW IT WORKS", "PLATFORM", "USE CASES". The mono + caps + wide tracking combination reads as metadata rather than copy.

### Trust Logo Strip

Horizontal row of 6 monochrome customer logos in #a7a7a7, set at small scale (24–32px height) with even spacing. A short white label sits above: "Connecting the world's leading companies to their customers:". Flanked by star-rating summaries on the right.

### Footer Link Column

Each column starts with a JetBrains Mono 12px uppercase label in white, followed by 6–8 Inter 14px/400 links in #ffffff stacked with 12px row gap. Five columns total: Platform, Use Cases, Resources, Contact, Explore Outlier. The "Explore Outlier" column includes a long-form link block and a CTA arrow.

### BETA Tag

Small inline label next to feature names (e.g. "AI Dashboards BETA"). Likely JetBrains Mono 12px in #a7a7a7 or a subtle bordered pill. Signals provisional status without alarming the reader.

### Promo Banner

Full-width bar above the nav with a #6798ff or similar accent fill, white text, centered content. Contains a visual badge, short promotional copy, and a CTA. Sits above the main nav and establishes a secondary action channel.

### Chart Bar (Data Series)

Vertical bars at varied heights with rounded tops, rendered in multiple accent hues (indigo, magenta, orange, green) against the charcoal card surface. Bars are ~6–8px wide with 2–4px gaps. The multi-color treatment is unique to data viz — the rest of the site stays monochromatic.

## Similar Design Systems

- {'why': 'Same dark-mode command-center aesthetic with near-black canvas, single accent color, tight Inter typography, and subtle surface stepping instead of shadows', 'business': 'Linear'}
- {'why': 'Identical monochrome dark palette, 8px radii, and the treatment of color as rare functional punctuation on a gridded black canvas', 'business': 'Vercel'}
- {'why': 'Dark UI with a single soft blue/indigo accent, JetBrains Mono for categorical labels, and product-screenshot hero mockups inlined as live-looking UI', 'business': 'Cursor'}
- {'why': 'Same blueprint-grid background pattern on dark sections, compact 8px-radius components, and rationed use of a single chromatic accent', 'business': 'Resend'}
- {'why': 'Developer-tool visual language: charcoal surface stack, data-dense layouts, JetBrains Mono labels for categories, and a single indigo accent for interactive highlights', 'business': 'Retool'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff
- background: #0a0a0a
- card surface: #141414
- border: #1e1e1e or #313131
- accent: #6798ff
- primary action: #1e1e1e (filled action)

**3 Example Component Prompts**

1. **Hero Section**: #0a0a0a background. Headline at 64px Inter weight 500, #ffffff, letter-spacing -2.3px, max 2 lines. Subtext at 16px Inter weight 400, #a7a7a7, max-width 480px. Two buttons side by side: white-filled "Contact sales" (8px radius, 8px 16px padding, #0a0a0a text) and ghost "Try Dovetail free" (transparent, 1px #454545 border, 8px radius, #ffffff text). To the right, a #141414 dashboard preview card with 8px radius, 24px padding, containing a bar chart and data table mockup.

2. **Stat Row**: Three-column grid, centered. Each block: a #6798ff icon (24px), then 40px Inter weight 500 white number, then 16px Inter weight 500 white label, then 14px Inter weight 400 #a7a7a7 description. 32px gap between columns.

3. **Section with Eyebrow**: Centered. JetBrains Mono 12px uppercase #a7a7a7 eyebrow with +0.85px tracking, 32px gap, then 40px Inter weight 500 #ffffff heading, then optional 16px Inter weight 400 #a7a7a7 body below at max-width 640px.

**Grid Background Pattern**: On the #0a0a0a canvas, overlay a 1px grid using #1e1e1e lines at ~48px spacing. The grid is decorative — it recedes at ~5% opacity feel and provides spatial structure without competing with content.

## Grid Background System

The faint blue-gray grid that fills the dark sections is a signature element — it evokes architectural blueprints and data coordinates, reinforcing the product's analytical positioning. The grid uses 1px lines in #1e1e1e at ~48px cell spacing, rendered as a fixed background layer. It spans full-bleed across hero and section backgrounds but is omitted in the footer and content-heavy zones. To recreate: apply a CSS background-image with linear-gradient lines in both axes at the specified spacing, set on the section container behind all content.
