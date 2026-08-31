# General Intelligence Company — Design System

> **North Star**: Literary journal beside a bonfire
> **Theme**: light
> **Source**: https://www.generalintelligencecompany.com
> **Refero Style**: https://styles.refero.design/style/34baa524-5d5b-4165-bbab-d01f05e6d6b9
> **Synced**: 2026-09-01

## Overview

General Intelligence Company uses an editorial, almost literary visual language: a warm off-white canvas interrupted by hand-painted atmospheric illustrations (moonlit skylines, wildflower meadows) that do the emotional work, while the actual UI lives on clean white between these scenes. Typography carries the brand — a custom display serif (ppmondwest) speaks in a low, measured voice at 48–54px with tight -0.04em tracking, while a custom sans (af) handles everything utilitarian at 13–18px. Color is nearly absent: a warm parchment white, a soft green-gray border, and one vivid blue (#41a1cf) used only as an outlined action border. Components whisper — 4px and 8px radii, hairline 1px borders, subtle backdrop-blur on the navigation, no decorative shadows.

## Color Palette

- **Parchment**: `#fefffc` — Page canvas — warm off-white slightly creamier than pure white, gives the whole site its book-page atmosphere [neutral]
- **Paper**: `#ffffff` — Card surfaces, section backgrounds, footer — the slightly cooler clean white used for elevated content areas [neutral]
- **Linen**: `#f9faf7` — Input fields, subtle surface wash, nav fill — barely-perceptible off-white that reads as neutral [neutral]
- **Ink Black**: `#171717` — Primary foreground token, strong body text where maximum contrast is needed [neutral]
- **Graphite**: `#2c2c2c` — Headlines and key body text — softer than pure black, pairs with the warm canvas [neutral]
- **Charcoal**: `#444141` — Secondary text, button text — the workhorse text tone for body copy and UI labels [neutral]
- **Ash**: `#646464` — Muted helper text, descriptive copy, subdued UI [neutral]
- **Fog**: `#b4b8b4` — Tertiary borders, disabled states, lightest neutral in the scale [neutral]
- **Mist**: `#dee2de` — Hairline borders on cards, buttons, and section dividers — green-tinted to harmonize with illustrations [neutral]
- **Twilight**: `#282834` — Near-black with a cool blue undertone — used for nav borders, icon strokes, and outlined actions; reads darker than its lightness suggests [neutral]
- **Dusk**: `#1f1f29` — Filled button background — a near-black with cool violet undertone, the only non-white filled surface in the system [neutral]
- **Signal Blue**: `#41a1cf` — Blue accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color [brand]
- **Cerulean**: `#0081c0` — Vivid blue used for a singular saturated card surface — the lone moment of pure color intensity, used sparingly as atmospheric punctuation [brand]

## Typography

- **ppmondwest**
- **af**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.3 |
| body-sm | 15 | — | 1 |
| subheading | 18 | — | 1.3 |
| heading-sm | 27 | — | 1.5 |
| heading | 40 | — | 1.1 |
| heading-lg | 48 | — | 1.1 |
| display | 54 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8-12px
- **Section Gap**: 32-64px
- **Border Radius**: {'nav': '50px (pill)', 'cards': '12px or 16px', 'buttons': '4px or 8px', 'large-surfaces': '24px'}

## Layout

Full-bleed illustrated hero sections alternate with clean white content sections in a vertical rhythm. The hero is a 100vh painted illustration with a floating frosted-glass navigation pill at top-center and a glassmorphic overlay card at bottom-left containing the headline and CTA. Content sections are max-width 1200px centered, with generous vertical breathing room (64-96px). Headlines are left-aligned and large, often spanning 6-8 columns. Two-column layouts pair text with diagrams or illustrations. The diagram sections use a 6+6 split: explanatory text and figure caption on the left, line-art diagram in a soft-bordered card on the right. Navigation is a single floating pill — no sidebar, no mega-menu. Footer is a white band with a large editorial statement. The overall density is spacious: one idea per screen, never crowded.

## Surfaces / Elevation

- **Parchment Canvas**
- **Paper Card**
- **Linen Wash**
- **Vivid Blue**

**Shadow tokens:**

## Imagery

Hand-painted digital illustrations carry the emotional narrative: a moonlit New York skyline with cherry blossom branches framing the composition, a dark wildflower meadow with golden poppies and purple flowers, a pixelated yellow-and-pink flower rendered in a low-resolution game-art style. The illustrations are painterly, not flat-vector — they have visible brush texture, atmospheric depth, and cinematic color grading (cool blues for night, warm greens for fields). All illustrations sit full-bleed or at 24px radius against the white canvas. No photography, no product screenshots, no abstract 3D. The pixelated flower is the one element that breaks the painted language — a deliberate contrast. Icons are minimal: a small sun-over-landscape glyph in the nav, simple line arrows in buttons.

## Design Principles

### Do

- Use ppmondwest for any heading 27px and above; never use the sans for display text
- Set all ppmondwest headings to weight 400, never 600 or 700 — the serif does the work
- Use 1px solid #dee2de for all card and section borders; this green-tinted hairline is the visual signature
- Apply 8px border-radius to buttons and 12-16px to cards — avoid mixing 4px and 24px in the same surface
- Use #41a1cf as a border-only accent on CTAs; the system has no filled chromatic buttons
- Let the canvas be #fefffc (warm off-white), not pure #ffffff, to maintain the book-page atmosphere
- Pair display headings with line-height 1.1; pair body text with line-height 1.5 — the contrast is intentional

### Don't

- Do not use #000000 for text — use #171717 (Ink Black) or #2c2c2c (Graphite) for softer warmth
- Do not apply box-shadow to buttons; the system uses borders and backdrop-blur instead of elevation
- Do not introduce new accent colors — the palette is deliberately 95% neutral with one blue
- Do not use weight 600+ on ppmondwest; the serif's personality is in its thin strokes
- Do not use rgba or transparency on body text — all text colors should be solid hex values
- Do not use radius values above 24px except for the navigation pill; this is not a soft-rounded design
- Do not fill buttons with #41a1cf or #0081c0; Signal Blue and Cerulean are border/surface colors only

## Components

### Frosted Navigation Pill

Floating pill at top center of the page, background rgba(255,255,255,0.06) with backdrop-blur(9-20px), 50px border-radius (fully rounded), 1px border in #282834 or white. Contains a small sun/landscape icon, three text links (About, Writing, Careers) in af 15px weight 500, and a bordered 'Get Cofounder' CTA button. The blur and transparency let the illustrated hero show through softly.

### Primary Outlined CTA Button

8px border-radius, transparent background, 1px border in #41a1cf (Signal Blue), text in #41a1cf, af 15px weight 500, padding 5px 12px. The chromatic border is the entire visual identity of the button — no fill, no shadow. Arrow icon (→) inside a circle at the right edge.

### Secondary Outlined Button

8px border-radius, transparent background, 1px border in #282834 (Twilight), text in #282834, af 15px weight 500, padding 5px 12px. The neutral cousin of the primary CTA — used when a second action appears alongside.

### Filled Dark Button

8px border-radius, background #1f1f29 (Dusk), text white, border 1px in #282834, af 15px weight 500, padding 8px 16px. Used very sparingly — the only filled button in the system, appears in footer or high-emphasis contexts.

### Ghost Text Link

No background, no border, text in #444141 or #282834, af 16px weight 400, often with an arrow icon. The default for 'Get to know us' style links. Underlined version used inline within headings for cross-references.

### Frosted Hero Overlay Card

Overlays the illustrated hero. 24px border-radius, semi-transparent background, backdrop-blur, generous padding (80px on the vivid blue variant), white or dark text depending on background. The frosted glass treatment ties the UI to the painted illustration.

### White Content Card

12px border-radius, background #ffffff (Paper), 1px border in #dee2de (Mist), shadow rgba(0,0,0,0.08) 0px 1px 1px / 0px 4px 5px. Padding varies — 0px for media cards, 16px for text cards. The soft green-tinted border is the signature edge treatment.

### Atmospheric Illustration Card

Large format (often 1100000+ px area), 24px border-radius, vivid background color (#0081c0 Cerulean or painted landscape), generous internal padding 80-128px. These are the moments where color is allowed to exist — illustration-as-component.

### Diagram Card

16px border-radius, semi-transparent white background, subtle shadow rgba(0,0,0,0.05) 0px 1px 8px, padding 12px. Houses line-art diagrams (isolated agent squares, coordinator nodes) — the visual explanations are always inside this soft frame.

### Input Field

0px border-radius (flat edges), background #f9faf7 (Linen), text #444141 (Charcoal), border-bottom-only in #444141. No visible top/side borders — the input is defined by its fill color and a single bottom line, giving a paper-form feel.

### Cookie Consent Banner

White background, rounded corners, small font af 13px, inline text + Decline/Accept text buttons separated by a vertical divider. The minimal, text-first treatment is characteristic — no icons, no color, no urgency.

### Footer

White background, large editorial statement in ppmondwest serif, small navigation links in af, generous vertical padding. The footer extends the literary feel — reading like the colophon of a book.

## Similar Design Systems

- {'why': 'Same editorial use of large custom serif headings on a warm off-white canvas, with illustrations doing narrative work between clean white content sections', 'business': 'Stripe'}
- {'why': 'Similar restraint in color usage — near-monochrome palette with a single chromatic accent, hairline borders, 8px button radius, and generous spacing', 'business': 'Linear'}
- {'why': 'Shared literary, almost book-like visual register: warm canvas, serif display type, and painted or hand-crafted imagery replacing stock photography', 'business': 'Anthropic'}
- {'why': 'Comparable soft-green border tones (#dee2de family) and the same approach of using atmospheric illustrations as structural section dividers', 'business': 'Notion'}
- {'why': 'Similar product-as-editorial-object sensibility with custom serif display type, off-white canvas, and full-bleed illustrated sections punctuating clean white content blocks', 'business': 'Pitch'}

## Agent Prompt Guide

## Quick Color Reference
- text: #2c2c2c (headlines), #444141 (body), #646464 (muted)
- background: #fefffc (canvas), #ffffff (cards), #f9faf7 (inputs)
- border: #dee2de (cards), #282834 (nav/actions), #41a1cf (primary CTA)
- accent: #0081c0 (vivid blue — atmospheric surface only)
- foreground: #171717
- primary action: #41a1cf (outlined action border)

## 3-5 Example Component Prompts

1. **Outlined primary CTA button**: 8px border-radius, transparent background, 1px solid border in #41a1cf (Signal Blue), text #41a1cf, af family weight 500 at 15px, padding 5px 12px, with a small arrow icon in a circle on the right.

2. **Editorial headline section**: White (#ffffff) background, 64px vertical padding. Headline in ppmondwest weight 400 at 48px, line-height 1.1, letter-spacing -0.02em, color #2c2c2c. Subtext below in af weight 400 at 16px, line-height 1.5, color #646464.

3. Create an Outlined Primary Action: Transparent background, #41a1cf border and text, 9999px radius, compact pill padding. Use it for the main CTA instead of a filled button.

4. **Content card with hairline border**: 12px border-radius, background #ffffff, 1px solid border in #dee2de (Mist), shadow rgba(0,0,0,0.08) 0px 1px 1px / 0px 4px 5px. Padding 16px. Body text in af 16px weight 400, #444141.

5. **Full-bleed illustrated hero section**: 100vh height, illustration fills entire section (no border-radius or 24px). Floating glassmorphic overlay card at bottom-left: 24px border-radius, semi-transparent white background, backdrop-blur, 32px padding, serif headline in ppmondwest 48px weight 400, white text.
