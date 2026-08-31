# Caldera — Design System

> **North Star**: forge fire on warm limestone. The canvas is raw warm plaster, and every orange element reads as glowing embers pressed into the surface.
> **Theme**: light
> **Source**: https://caldera.xyz
> **Refero Style**: https://styles.refero.design/style/fe8cdcf9-c850-4d52-be07-5ad269bf9ebf
> **Synced**: 2026-09-01

## Overview

Caldera runs on a warm limestone canvas flooded with molten orange. The interface is flat and unshadowed, letting ultrabold compressed type at near-architectural scale (up to 189px) carry all structural weight. A single vivid orange (#fc5000) acts as the only aggressive chromatic accent against monochrome warm grays, with a violet plasma reserved for the hero halftone and a sulfur yellow for tags. The visual language is volcanic: condensed heavy letterforms, halftone dot patterns, 40px radii on cards and buttons, and 800px pill controls — heat contained within a soft, paper-like surface.

## Color Palette

- **Ember**: `#fc5000` — Primary action buttons, featured stat cards, key visual highlights — the only aggressive chromatic accent; its vivid saturation against warm grays creates urgency without needing supporting decorative weight [brand]
- **Plasma Violet**: `#524ae9` — Hero halftone gradient base, single secondary card surface — appears almost exclusively in the hero dot pattern and one standout card; never used for controls [brand]
- **Sulfur**: `#f5f28e` — Tag and category badge backgrounds, small highlight washes — the soft yellow that labels blog post categories and program announcements [accent]
- **Limestone**: `#f7f6f2` — Card surfaces, content block backgrounds, secondary button fills — the lighter warm off-white that lifts elements off the page canvas [neutral]
- **Pumice**: `#e2e2df` — Page canvas, dominant background — the warm medium-gray that grounds every section; slightly darker than card surfaces to create subtle figure/ground separation without shadows [neutral]
- **Obsidian**: `#070607` — Primary text, headings, link text, button borders — near-black with a barely-warm cast matching the canvas warmth [neutral]
- **Chalk**: `#ffffff` — Dark-section text, input text on dark backgrounds, high-contrast overlays — pure white used only where maximum contrast against dark surfaces is required [neutral]

## Typography

- **PP Neue Corp Compact**
- **DM Sans**
- **System sans-serif**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.2 |
| body-sm | 14 | — | 1.2 |
| body | 16 | — | 1.55 |
| subheading | 26 | — | 1.2 |
| heading-sm | 30 | — | 1.5 |
| heading | 32 | — | 1 |
| heading-lg | 48 | — | 1 |
| heading-2xl | 80 | — | 1.1 |
| heading-3xl | 96 | — | 0.95 |
| display | 189 | — | 0.94 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 40px
- **Element Gap**: 16px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '40px', 'pills': '800px', 'small': '16px', 'inputs': '100px', 'medium': '20px', 'buttons': '40px'}

## Surfaces / Elevation

- **Pumice Canvas**
- **Limestone Surface**
- **Ember Feature**
- **Plasma Hero**

## Imagery

Imagery is minimal and deliberate. The hero uses an abstract halftone dot pattern (orange dots on a violet-to-orange gradient) rather than photography — it functions as brand artwork, not decoration. Product and announcement cards use either solid Ember blocks or the Plasma Violet halftone as image-area fills, keeping a consistent graphic system. Partner/integration logos are rendered as monochrome marks on light backgrounds. No photography, no 3D renders, no lifestyle imagery anywhere. Icons are small, monochrome, and minimal — Discord, X, and Telegram sit in the nav as simple glyphs. The visual language is graphic and editorial, not photographic: think poster design, not stock imagery.

## Design Principles

### Do

- Use PP Neue Corp Compact at 48px or larger for any heading that needs to feel structural — below 40px the ultrabold weight overwhelms and loses its industrial character
- Apply 40px border-radius to all cards, content blocks, and non-pill buttons as the default surface radius
- Use 800px border-radius (full pill) for all buttons, tags, nav containers, and small interactive elements
- Set primary CTAs to Ember (#fc5000) with Obsidian (#070607) text, sized at 12px/24px padding — never rectangular, always pill-shaped
- Keep body text at DM Sans 500 (Medium) — never drop to Regular weight, which reads as anemic against the ultrabold display type
- Use the halftone dot pattern (orange dots on violet) as the hero/signature visual treatment — it is the system’s most recognizable motif
- Layer surfaces using color contrast (Pumice canvas → Limestone cards → Ember features) rather than shadows or borders

### Don't

- Do not add drop shadows to any element — the system is intentionally flat; shadows would undermine the paper-like warmth
- Do not use rectangular (low-radius) buttons — the pill/40px-radius treatment is non-negotiable
- Do not introduce additional accent colors beyond Ember, Plasma Violet, and Sulfur — the palette is deliberately constrained to three chromatic tones
- Do not use Regular or Bold weights of DM Sans for body — Medium (500) is the only correct weight
- Do not set headings below 26px or above 189px — the display type only works at architectural scale
- Do not use Plasma Violet for buttons or controls — it is reserved for the hero halftone and a single accent card
- Do not apply negative letter-spacing to PP Neue Corp Compact — the +0.02em positive tracking is intentional at display sizes to prevent stroke collision

## Components

### Primary CTA Button

Filled Ember (#fc5000) with Obsidian (#070607) text. 800px border-radius (full pill). Padding 12px vertical, 24px horizontal. DM Sans 500 weight at 16px. No shadow. The pill shape is the most distinctive control shape in the system — never rectangular.

### Secondary Pill Button

Transparent background, 1.5px Obsidian (#070607) border, Obsidian text. 40px border-radius. Padding 16px all sides. DM Sans 500 at 16px. Border style is solid here, not dotted. Sits beside the primary CTA as the quieter counterpart.

### Outlined Ghost Link

Transparent background, no visible border, Obsidian text. 800px pill radius. Padding 0 vertical, 12px horizontal. DM Sans 500 at 16px. Used for nav items and inline links — relies on color and position rather than container weight.

### Stat Feature Card

Ember (#fc5000) solid background, Chalk (#ffffff) text. 40px border-radius. Padding 40px on all sides. No shadow. The large metric number uses PP Neue Corp Compact at 80px+; the label above uses DM Sans 500 at 14–16px. These cards are the system’s most visually dominant elements after the hero.

### Content Card

Limestone (#f7f6f2) background, no border, no shadow. 40px border-radius. Padding 40px all sides. Contains a category tag, headline (PP Neue Corp Compact 26–32px in Obsidian), and date metadata. The image area at the top can be a halftone or solid Ember block.

### Plasma Hero Card

Plasma Violet (#524ae9) background with white halftone dot pattern overlay. 40px border-radius. Used sparingly — appears once as a signature visual anchor. No shadow.

### Category Tag Badge

Sulfur (#f5f28e) background, Obsidian (#070607) text. Pill shape (800px radius). DM Sans 500 at 12–14px. Padding approximately 3–4px vertical, 8–10px horizontal. Small, bright, and functionally pure — the only yellow element in the system.

### Navigation Bar

Pumice (#e2e2df) page background continues through. Nav items are Obsidian text in DM Sans 500 at 16px, separated by 9px gaps. The entire nav row can sit inside a Limestone (#f7f6f2) pill container with 800px radius — a signature element. Logo lockup (mountain icon + wordmark) sits left, social icons and CTA right.

### Hero Halftone Block

Large rounded rectangle filled with a Plasma Violet (#524ae9) to Ember (#fc5000) gradient overlaid with an orange halftone dot pattern. 40px border-radius. Dimensions are hero-scale (roughly 50% of viewport width). The halftone effect is the system’s most distinctive visual signature — pixel-art-like, high-density dot grid that fades to solid orange at the top right.

### Input Field

Transparent background, 1.5px Chalk (#ffffff) border. 100px border-radius (pill). Padding 24px vertical, 32px left, 64px right. Chalk text. DM Sans 500. Used in dark/contrast sections only.

### Partner Logo Strip

Limestone (#f7f6f2) background card, 40px radius, 40px padding. Logos arranged in a single row with consistent height, separated by vertical 1.5px Obsidian dotted dividers. No individual logo containers — flat inline treatment.

### Dotted Divider

1.5px dotted line in Obsidian (#070607). Used as vertical dividers in nav and partner strips, and occasionally as horizontal section breaks. The dotted (not dashed, not solid) style is a small but consistent signature detail.

## Similar Design Systems

- {'why': 'Similar crypto/web3 site language with warm off-white canvas, massive condensed display type, and a single bold accent color dominating featured surfaces', 'business': 'Berachain'}
- {'why': 'Matching approach of ultrabold compressed headlines at near-architectural scale, flat no-shadow surfaces, and pill-shaped controls with aggressive border-radius', 'business': 'Monad'}
- {'why': 'Shared visual DNA of warm neutral canvas, single vivid accent color for CTAs and stat cards, and condensed industrial display typography', 'business': 'Dymension'}
- {'why': 'Same flat-design philosophy on warm background, pill buttons in one dominant accent color, and oversized compressed headlines as structural anchors', 'business': 'Blast'}
- {'why': 'Comparable crypto ecosystem site pattern with generous 40px surface radii, warm light canvas, and medium-weight body sans against heavy display type', 'business': 'Arbitrum'}

## Agent Prompt Guide

## Quick Color Reference
- Page background: #e2e2df (Pumice)
- Card/content surface: #f7f6f2 (Limestone)
- Primary text/headings: #070607 (Obsidian)
- primary action: #fc5000 (filled action)
- Accent: #524ae9 (Plasma Violet) — hero halftone only
- Tag/badge: #f5f28e (Sulfur)
- Input border (dark sections): #ffffff (Chalk)

## 3-5 Example Component Prompts
1. Create a Primary Action Button: #fc5000 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Stat Row**: Four Ember (#fc5000) cards in a row, each 40px radius, 40px padding. Label in DM Sans 500 at 14px, Chalk (#ffffff) text. Metric value in PP Neue Corp Compact at 80px weight 400, Chalk text, line-height 1.1.

3. **Content Card**: Limestone (#f7f6f2) background, 40px radius, 40px padding. Sulfur (#f5f28e) pill tag at top with DM Sans 500 12px Obsidian text, 800px radius. Headline at 32px PP Neue Corp Compact, Obsidian, letter-spacing 0.64px. Date at 12px system sans-serif, Obsidian.


5. **Dark Input Section**: Obsidian (#070607) background. Chalk (#ffffff) pill input with 100px radius, 24px/32px padding, 1.5px Chalk border. DM Sans 500 16px Chalk text. Submit button: Ember fill, 800px radius, 12px/24px padding.

## Signature Motifs

Three visual signatures define Caldera’s identity and should be reused across new pages: (1) The halftone dot pattern — orange dots on a violet-to-orange gradient, always at hero scale with 40px radius, is the most recognizable motif. (2) The 189px display headline — ultrabold compressed type at near-architectural scale, with tight 0.94 line-height, signals the page is a Caldera page. (3) The triple-radius system — 100px for inputs, 40px for cards and rectangular buttons, 800px for pills — creates a consistent roundness without monotony.
