# Pa'lais — Design System

> **North Star**: Botanical sketchbook dipped in honey. The cream paper canvas, blue toile-style line illustrations, and warm color blobs recall a hand-bound recipe journal, while the bold condensed display type and generous whitespace give it modern editorial confidence.
> **Theme**: light
> **Source**: https://www.palais.bio
> **Refero Style**: https://styles.refero.design/style/5ef5e1ff-3cb3-4383-9f66-26474409d9ae
> **Synced**: 2026-09-01

## Overview

Pa'lais reads like a hand-illustrated artisan cookbook dropped into a modern food-magazine layout. The canvas is a warm cream paper (#fbf9f6) with pure white cards layered on top, anchored by a single deep-indigo brand voice (#234386) that owns every headline, link, and primary button. That indigo is intentionally the only saturated cool in the system; everything else is warm and edible — honey-gold (#ffc400), burnt orange (#ed7328), warm sand (#d2b68c), mint sage (#a2d3a6) — and those warms appear almost exclusively as organic flowing blob shapes and botanical line-art, never as flat fills. Typography splits into two loud voices: bold condensed display fonts in all-caps navy for headlines, and widely-tracked geometric sans (Axiforma / ITC Avant Garde) for labels and UI chrome with letter-spacing up to 0.27em. A handwritten script carries emotional taglines ('The future of cooking – today'). Components stay lightweight — soft 8px cards, generous 32px-radius pill buttons, hairline borders — letting the illustrations and photography do the storytelling.

## Color Palette

- **Deep Indigo**: `#234386` — Primary brand color — headlines, navigation text, links, filled CTA buttons, and dark section backgrounds. The only cool saturated hue in the system, it gives every action weight and authority [brand]
- **Honey Gold**: `#ffc400` — Decorative accent — used exclusively in organic flowing blob shapes and illustration highlights, never as a fill or button. The warm burst of yellow is the system's signature punctuation against the cream canvas [accent]
- **Burnt Orange**: `#ed7328` — Orange accent for outlined action borders, linked labels, and lightweight interactive emphasis. [accent]
- **Sky Blue**: `#6aa8dc` — Soft illustration blue — used in botanical line-art washes and supporting decorative blobs. Lighter and more atmospheric than the primary indigo, it adds depth to the plant illustrations [accent]
- **Warm Sand**: `#d2b68c` — Subtle warm accent — used sparingly in illustration details and supporting decorative shapes. Bridges the gap between the cream canvas and the more saturated orange and gold accents [accent]
- **Mint Sage**: `#a2d3a6` — Botanical green — appears in organic blob shapes and plant illustration washes. Soft enough to read as a pastel, it reinforces the plant-based brand without competing with the indigo or orange [accent]
- **Ink Black**: `#000000` — Primary text, hairline borders, icon strokes, and neutral UI elements. The sheer frequency of black borders (503+ occurrences) signals the system relies on thin dividing lines rather than card elevation to separate content [neutral]
- **Pure White**: `#ffffff` — Card surfaces, text on dark backgrounds, button text fills, and inset panels. Creates the layered surface effect — white cards resting on the cream canvas [neutral]
- **Cream Paper**: `#fbf9f6` — Page canvas and hero background. This warm off-white is the system's base surface, immediately distinguishing it from a stark white SaaS layout — it reads as paper, not screen [neutral]
- **Soft Shadow**: `#d6d6d6` — Card shadow base tone — used exclusively in box-shadow declarations at low opacity. The shadow is the only elevation mechanism; there are no borders on cards [neutral]

## Typography

- **Times**
- **hwt-artz**
- **Delivery Note DEMO**
- **Sandman_Fill**
- **Axiforma**
- **ITC Avant Garde Std Bk**
- **Caveat (script accent)**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.6 |
| body-sm | 14 | — | 1.67 |
| body | 16 | — | 1.5 |
| subheading | 24 | — | 1 |
| heading-sm | 32 | — | 0.9 |
| heading | 46 | — | 1.18 |
| heading-lg | 56 | — | 1.14 |
| display | 88 | — | 0.82 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '16px', 'blobs': 'organic (SVG paths, no fixed radius)', 'cards': '8px', 'inputs': '8px', 'buttons': '32px'}

## Layout

The page uses a full-bleed cream canvas with content max-widthed to ~1200px centered. The hero is a split layout: condensed display headline + script tagline on the left, product photography on the right, divided by a flowing organic SVG blob (gold over sage) that replaces a straight vertical line. Below the hero, sections alternate between white and full-bleed orange bands, each separated by organic wavy dividers rather than hard lines. Content sections are typically 2-column (text + image/illustration) or centered single-column stacks. The recipes section is a horizontal card carousel on an orange background. Navigation is a minimal top bar with logo left, nav center, CTA right. Density is spacious — 64px section gaps and generous breathing room around illustrations let the decorative elements (blobs, line-art) feel curated rather than cluttered. The overall rhythm is: quiet cream → bold orange → quiet cream → dark indigo footer.

## Surfaces / Elevation

- **Cream Paper Canvas**
- **Pure White Card**
- **Burnt Orange Section**
- **Deep Indigo Section**

**Shadow tokens:**

## Imagery

Imagery is split between two distinct modes: (1) hand-drawn botanical line illustrations in Deep Indigo or Sky Blue, rendered in a toile/engraving style with no fills, depicting plants, cashews, leaves, knives, and herbs — scattered around sections, overlapping content edges, and bleeding off the page; (2) warm natural-light food photography showing the Pa'lais product tub in context (on linen, wood, ceramic surfaces) and finished dishes (toast with spread, wraps, bowls) garnished with fresh herbs. Product shots are slightly angled, lifestyle food shots are close-up and slightly overhead with shallow depth of field. The illustrations carry the editorial/artisan mood; the photography carries the appetite appeal. Neither uses duotone or color treatment — illustrations are pure line, photography is natural color.

## Design Principles

### Do

- Use #234386 Deep Indigo as the only filled-button background color — it is the single saturated cool anchor in an otherwise warm palette.
- Apply Axiforma or ITC Avant Garde with 0.13–0.27em letter-spacing for all labels, nav items, and UI text in uppercase — the aggressive tracking is the system's typographic signature.
- Render all decorative organic shapes as SVG paths in solid accent fills (#ffc400, #ed7328, #a2d3a6) — never use CSS gradients or multiple colors in one blob.
- Use 32px border-radius for all buttons and 8px for cards — the radius contrast between pill-buttons and soft-cornered cards is intentional and creates the system's tactile feel.
- Layer Pure White (#ffffff) cards on the Cream Paper (#fbf9f6) canvas rather than using gray surfaces — the warm off-white base is what makes the system feel like a cookbook rather than a dashboard.
- Combine bold condensed display type (hwt-artz / Bebas Neue substitute) in Deep Indigo all-caps with a handwritten script (Caveat substitute) for emotional subheadlines — this two-voice headline pattern is the brand's verbal-visual signature.
- Use botanical line illustrations in #234386 or #6aa8dc with 1–1.5px stroke and no fills as decorative connective tissue between sections.

### Don't

- Don't introduce new blue or indigo shades — #234386 is the sole cool saturated color and any additional blue will dilute the warm/cool tension.
- Don't use #ffc400 Honey Gold or #ed7328 Burnt Orange as filled button backgrounds — these accents are reserved for organic shapes and outlined secondary actions.
- Don't apply letter-spacing tighter than 0.03em on display headlines or wider than 0.27em on labels — the tracking extremes are calibrated; flattening them kills the editorial cadence.
- Don't use flat gray (#f5f5f5, #e0e0e0) for surface separation — the system achieves layering through cream → white → orange → indigo, not through neutral grays.
- Don't add drop shadows to buttons or navigation — shadows appear only on recipe cards, and even there they are asymmetric and soft.
- Don't set body text in the display fonts (hwt-artz, Delivery Note, Sandman) — those are reserved for headlines at 32px and above.
- Don't place the script accent font (Caveat substitute) in UI chrome, labels, or buttons — it is an emotional headline voice only, used sparingly.

## Components

### Filled Indigo CTA Button

Deep Indigo (#234386) background, Pure White (#ffffff) text, 32px border-radius (pill-adjacent — wider than tall), padding 24px top/bottom × 48px left/right. Text in Axiforma or system sans, 13px, uppercase, letter-spacing ~0.1em. No border, no shadow. Examples: 'STORE LOCATOR' in the nav, 'CHECK OUT OUR RECIPES' in the recipes section.

### Outlined Orange Secondary Button

Transparent background with 2px Burnt Orange (#ed7328) border, Burnt Orange text, 32px border-radius. Padding 24px × 48px. Always includes a right-arrow icon before or after the label. Used for 'MEET US' and similar exploration CTAs. This is the outlined-action variant — not filled.

### Top Navigation Bar

Horizontal bar, white or transparent background resting on the cream canvas. Logo (Pa'lais wordmark) left, nav items center (GET INSPIRED, OUR PRODUCTS, FOR A BETTER WORLD, CONTACT), filled indigo CTA button right. Nav items in Axiforma or ITC Avant Garde at 12–16px with 0.13–0.2em letter-spacing, all-caps, Deep Indigo color. 40px horizontal margin on nav items.

### Recipe Card

8px border-radius, soft box-shadow rgba(0,0,0,0.16) -14px 10px 49px 0px (asymmetric, drifting down-right). White background. Full-bleed food photography at the top with a semi-transparent overlay containing the recipe title in white all-caps condensed display type and a 30-min time badge. Padding 16px. Cards sit directly on the orange section background.

### Hero Section with Organic Wavy Divider

Full-bleed cream (#fbf9f6) background. Left side: large condensed display headline (56–58px, Deep Indigo) with a script tagline below (32–40px, Caveat-style). Right side: product photography of a Pa'lais tub. A flowing SVG blob shape (honey-gold on top, mint-sage on bottom) acts as a wavy vertical divider between the two halves — not a straight line, but an organic curve that bleeds across the section.

### Organic Blob Shape

Free-form SVG path with no fixed dimensions, using a solid fill from the accent palette (Honey Gold, Burnt Orange, Mint Sage). Appears at section boundaries, behind product images, and as background washes. The blobs are not abstract — they evoke liquid, plant, or splash forms. They carry the warm color energy while the indigo type carries the structural weight.

### Botanical Line Illustration

Detailed blue line-art (Deep Indigo #234386 or Sky Blue #6aa8dc, 1–1.5px stroke) of plants, cashews, leaves, knives, and herbs — rendered in a toile/engraving style. Scattered around sections, overlapping content edges, and bleeding off the page. They never have fills — only outlines — and act as the connective tissue between sections.

### Eyebrow Label / Section Tag

ITC Avant Garde or Axiforma, 12–16px, Deep Indigo or white text, letter-spacing 0.2–0.27em. Always uppercase. The aggressive tracking is the system's signature typographic device — it makes even tiny labels feel editorial and intentional. Often paired with a small icon (clock for time, leaf for plant-based).

### Product Tub Image

Photographed in soft natural light on a textured surface (wood, linen, ceramic). The tub itself is off-white/cream with a Deep Indigo label featuring the Pa'lais wordmark and a small botanical illustration. The product is the visual hero — always shot at an angle that shows both the label and a hint of the contents.

### Food Photography Plate

Close-up, slightly overhead shots of prepared dishes (toast with spread, wraps, bowls) on light ceramic or wooden surfaces. Warm, natural lighting, shallow depth of field. Garnished with fresh herbs, nuts (cashews), and crumbs to reinforce the artisan/handmade feel. The food is the product context.

### Section Divider Curve

A large SVG path (typically 200–400px tall) that creates a flowing wave boundary between two color fields (e.g. cream → orange, white → deep indigo). Filled with a single solid color matching the section below. Unlike a hard line, it creates a hand-painted, watercolor-edge effect — the signature transition device of the layout.

### Scroll Indicator

Simple circular outlined icon in Deep Indigo, ~48px diameter, 1.5px stroke, containing a downward-pointing chevron. Centered below the hero text. Minimal — the system doesn't rely on elaborate scroll animations.

## Similar Design Systems

- {'why': "Same warm editorial energy with bold condensed display headlines, playful script accents, and warm/cool color tension — though Oatly leans more into beige and Oatly's signature off-white rather than this system's cream + indigo contrast.", 'business': 'Oatly'}
- {'why': 'Shares the hand-drawn botanical illustration language (leaves, plants) combined with a single saturated brand color, though Allbirds uses more photography and less organic blob shapes.', 'business': 'Allbirds'}
- {'why': "Same warm cream-canvas-plus-organic-illustrations approach with bold condensed display type and warm accent colors used in fluid shapes — the 'recipe-journal' visual language is nearly identical.", 'business': 'Bumble Bee Foods (or any artisan food brand like Graza)'}
- {'why': 'Shares the system-level decision to use a single cool saturated color (indigo/blue) for all structure while pushing all warmth into organic decorative shapes and illustrations — the color-lanes separation is the same.', 'business': 'Meow Mix (rebrand) or Wild One'}
- {'why': "Same botanical line-art illustrations, same generous whitespace, same single-accent-color discipline, though Seed leans more clinical while Pa'lais leans more artisan/handcrafted.", 'business': 'Seed (seed.com)'}

## Agent Prompt Guide

**Quick Color Reference**
- Text: #000000 (body), #234386 (headings, links, nav)
- Background: #fbf9f6 (page canvas), #ffffff (cards)
- Border: #000000 (hairline, 1px)
- Accent: #ffc400 (honey blobs), #ed7328 (orange blobs, secondary buttons)
- primary action: #234386 (filled action)

**Example Component Prompts**
1. *Hero Headline*: Create a 56px headline in Bebas Neue (substitute for Delivery Note), weight 400, all-caps, color #234386, letter-spacing 1.74px. Below it, a 32px script tagline in Caveat, weight 400, italic, color #234386, normal letter-spacing. Background is cream #fbf9f6.

2. *Primary Filled Button*: Render a pill button — 32px border-radius, background #234386, text #ffffff, font Axiforma 13px uppercase letter-spacing 0.1em, padding 24px top/bottom × 48px left/right. Label: 'STORE LOCATOR'.

3. *Outlined Secondary Button*: Render a pill button — 32px border-radius, 2px border in #ed7328, transparent background, text #ed7328, font Axiforma 14px uppercase letter-spacing 0.15em, padding 24px × 48px. Include a right-arrow icon. Label: 'MEET US'.

4. *Recipe Card*: White #ffffff background, 8px border-radius, box-shadow rgba(0,0,0,0.16) -14px 10px 49px 0px. Full-bleed food photo at top, overlay with title in Bebas Neue 24px white all-caps and a 12px time badge in ITC Avant Garde with 0.2em tracking. Padding 16px.

5. *Section Divider*: Insert a 200px-tall organic SVG wave path, solid fill #ed7328, spanning the full viewport width between a white section and the next section. The wave should curve gently — not a straight line — to create a hand-painted edge.

## Color Behavior Rules

The warm/cool tension is structural: #234386 Deep Indigo is the only cool color and it owns all type, links, and filled actions. Everything else (Honey Gold, Burnt Orange, Warm Sand, Mint Sage, Sky Blue) is warm or pastel and appears almost exclusively in organic blob shapes, illustration washes, and outlined secondary actions. Never cross these lanes — don't put warm colors in body text or buttons, and don't put indigo in decorative blobs. The Cream Paper canvas (#fbf9f6) is what makes this rule work: it is warm enough that the indigo reads as the deliberate cool counterpoint, and saturated enough that the white cards pop without needing gray separators.

## Illustration Integration

Botanical line-art illustrations should never sit in a contained box — they should bleed off page edges, overlap section boundaries, and be partially hidden by other elements. This 'living illustration' approach is what makes the system feel hand-crafted rather than stock-decorated. Place illustrations at varying scales (some small accents, some filling 30–40% of a section) and always in #234386 or #6aa8dc with 1–1.5px stroke weight and no fills. Rotate them slightly (±5–10°) for a hand-placed feel.
