# August Health EHR — Design System

> **North Star**: Warm cream pharmacy with violet ink — a humanist clinical surface that softens healthcare's typical sterility.
> **Theme**: light
> **Source**: https://www.augusthealth.com
> **Refero Style**: https://styles.refero.design/style/81bd6ad6-b02b-4fb3-a600-91ecf8324171
> **Synced**: 2026-09-01

## Overview

August Health uses a warm-clinical visual language: a soft cream canvas (#f8f3eb) replaces the cold white typical of healthcare SaaS, and shadows are tinted with warm brown rgba(75,68,57,0.1) rather than cool gray. The pairing of an editorial serif (Reckless Neue) with a geometric sans (Saans) gives the product an approachable, humanist feel appropriate for senior care, while a vivid indigo (#4865ff) anchors all primary actions. Color appears in concentrated bursts — circular portrait frames, tinted feature cards, and pill buttons — against an otherwise restrained neutral palette, creating rhythm and warmth without overwhelming the interface.

## Color Palette

- **Primary Indigo**: `#4865ff` — Primary action buttons, active nav state, icon accents — the single saturated focal color that makes CTAs unmistakably interactive [brand]
- **Deep Ink**: `#080331` — Headlines, body text, primary borders — near-black violet that pairs warmth with the serif typeface [brand]
- **Midnight Violet**: `#1b1463` — Navigation borders, secondary surfaces, gradient terminus — darker sibling to Primary Indigo for layered depth [brand]
- **Forest**: `#328a3b` — Green action color for filled buttons, selected navigation states, and focused conversion moments [accent]
- **Ember**: `#ff6d39` — Tinted card surfaces, portrait frame backgrounds — warm orange that signals energy and human warmth [accent]
- **Blossom**: `#f098d7` — Tinted feature card backgrounds, hero photo frame — mid-pink for category-coded surfaces [accent]
- **Petal**: `#ffaefe` — Light pink surface washes and button backgrounds — lightest tint in the pink family for soft fills [accent]
- **Meadow**: `#114e0b` — Dark green button background variant — deep saturated green for contrasting pill buttons [accent]
- **Lavender Mist**: `#a2baff` — Outlined/ghost button borders, subtle violet washes — soft tint version of Primary Indigo [brand]
- **Cream**: `#f8f3eb` — Page canvas, section backgrounds, link surfaces — the warm off-white base layer that defines the entire mood [neutral]
- **Stone**: `#333333` — Link and icon text — slightly lighter than pure black for secondary text [neutral]
- **Pure White**: `#ffffff` — Card surfaces, button text, inverted elements — the clean surface that sits on top of cream [neutral]
- **True Black**: `#000000` — Primary text, maximum-contrast borders, heading strokes [neutral]
- **Info Blue**: `#dce4fb` — Badge backgrounds for informational tags — near-gray blue for low-emphasis status indicators [semantic]

## Typography

- **Reckless Neue**
- **Saans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.6 |
| body-sm | 14 | — | 1.4 |
| body | 16 | — | 1.6 |
| subheading | 20 | — | 1.3 |
| heading-sm | 24 | — | 1.3 |
| heading | 32 | — | 1.1 |
| heading-lg | 48 | — | 1.1 |
| display | 64 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 16px
- **Section Gap**: 64px
- **Border Radius**: {'nav': '100px', 'cards': '16px', 'links': '24px', 'badges': '1600px', 'images': '1600px', 'buttons': '1600px', 'special': '100px'}

## Layout

Max-width ~1200px centered content with full-bleed cream canvas. Hero is a centered headline stack (no sidebar image) flanked by scattered circular portrait frames that bleed to the page edges. Navigation is a floating pill-shaped bar (radius 1600px) with subtle shadow, positioned at the top. Sections alternate between white cards and cream backgrounds. Feature content uses 2-column card grids on cream. Case study sections use centered headlines above full-width video blocks. The overall rhythm is: generous vertical spacing (64px+), centered text compositions, and circular decorative elements that break the rectangular grid.

## Surfaces / Elevation

- **Cream Canvas**
- **White Surface**
- **Tinted Card**
- **Accent Surface**
- **Vibrant Accent**

**Shadow tokens:**

## Imagery

Photography is central and humanizing: circular portrait crops of caregivers and seniors in vibrant colored frames (pink, green, orange) function as the hero's visual signature. Images are full-face, high-key, candid or semi-staged portraits — not lifestyle environmental shots. The circular masking with bold color halos is a recurring decorative motif. Product UI is shown as floating device mockup screenshots with generous radius. No illustrations or abstract graphics — all visual energy comes from real photography and product screenshots.

## Design Principles

### Do

- Use 1600px border-radius for all interactive elements: buttons, badges, nav bar, and image frames to maintain the pill-shaped consistency
- Set the page canvas to Cream (#f8f3eb), not pure white — the warm tone is the brand's emotional foundation
- Apply warm-tinted shadows (rgba(75,68,57,0.1)) to all elevated elements instead of cool gray shadows
- Pair Reckless Neue (serif, weight 400 only) for all headings with Saans (sans, weights 400-500) for all body and UI text
- Use Primary Indigo (#4865ff) exclusively for the primary action — do not dilute with secondary action colors when a strong CTA is needed
- Layer surfaces as: cream canvas → white card → tinted card → vibrant accent to create depth without heavy shadows
- Maintain 64px minimum vertical spacing between sections and 32px internal padding for all card containers
- Center-align hero and section headlines for editorial compositions; use left-align only for product UI and dense content areas

### Don't

- Do not use bold (600+) weights with Reckless Neue — the serif's power is in its regular weight restraint
- Do not apply cool gray shadows (rgba(0,0,0,...)) — warm brown shadows are part of the visual identity
- Do not use pure white (#ffffff) as the page background — cream is the base, white is for surfaces on top
- Do not use the accent colors (Forest, Ember, Blossom) for primary CTAs — reserve Primary Indigo for that role
- Do not add more than two weights to any text element — the system is intentionally restrained (400/500 for sans, 400 for serif)
- Do not use sharp corners (0px radius) on cards or buttons — the minimum card radius is 16px, buttons are always pills
- Do not break the cream/white/tinted surface hierarchy by placing a colored accent directly on cream without a white card container
- Do not use green for success states or red for error states unless explicitly required — the accent colors are decorative, not semantic

## Components

### Primary CTA Button

Indigo (#4865ff) background, white text, 1600px border-radius (full pill), 8-12px vertical padding with 16-24px horizontal padding, Saans weight 500 at 14-16px. Casts the warm-tinted double shadow (rgba(75,68,57,0.1) at 12px/24px and 48px/48px offsets).

### Ghost/Text Button

Transparent background, Deep Ink (#080331) text, no border, Saans weight 500. Sometimes paired with an arrow icon. Used for navigation dropdowns and less prominent actions.

### Pill Navigation Bar

White (#ffffff) background with 1600px border-radius, floats above the cream canvas with warm-tinted shadow. Contains logo (left), nav links (center, Saans 14px weight 500), and CTA button (right). Internal spacing: 16-24px horizontal padding, 12-14px vertical.

### Tinted Feature Card

16px border-radius, 32px padding, colored background fill (Forest #328a3b, Blossom #f098d7, or other accent tints). Contains a small icon, serif subheading (Reckless Neue 24px), body description (Saans 16px), and a circular arrow button (white, 100px radius) in the top-right corner.

### White Product Card

White (#ffffff) background, 16px border-radius, 32px internal padding. Contains product UI screenshots or detailed feature breakdowns. Sits on cream canvas to create contrast layers.

### Circular Portrait Frame

Circular image masks (essentially 50% border-radius or large radius values) containing portrait photography, set inside larger solid-color circles (pink, green, orange, white). These create the hero's signature scattered decorative composition and break the rectangular grid.

### Info Badge/Pill

1600px border-radius, 10px vertical padding, small text (Saans 12px). Used for section labels like 'THE PLATFORM', 'CASE STUDIES', and 'August Intelligence' indicators with a small icon prefix.

### Video Player Block

Large rectangular media container with 16px radius, cream or white surface, centered play button overlay (circular, indigo background, white triangle). Accompanied by centered serif headline above.

### Logo Strip

Horizontal row of partner/client logos on cream background, displayed in grayscale or muted tones, evenly spaced. No card containers — logos float directly on the cream canvas.

### Section Header

Centered composition: small pill badge label at top, large serif headline (Reckless Neue 48-64px) below, optional subtext (Saans 16-20px) beneath. Generous vertical spacing (40-64px) between elements.

### Dropdown Nav Item

Nav link with caret indicator. When active, shows a dropdown panel with white background, 16px radius, and warm-tinted shadow containing link lists.

### Gradient Hero Accent

Linear gradient (121deg) from pink rgb(204,122,181) through indigo rgb(72,101,255) to deep violet rgb(27,20,99). Used sparingly as a background treatment for special sections or feature highlights.

### Outlined/Secondary Button

Lavender Mist (#a2baff) border, transparent or white background, Deep Ink (#080331) text, 1600px radius. Used when Primary Indigo CTA is already present and a secondary action is needed.

## Similar Design Systems

- {'why': 'Warm cream canvas replacing cold white, editorial serif headlines, pill-shaped buttons, and concentrated accent color usage', 'business': 'Calm'}
- {'why': 'Warm off-white backgrounds, rounded pill buttons, and approachable typography that softens a typically clinical category', 'business': 'Headspace'}
- {'why': 'Healthcare AI with serif/sans typography pairing, warm background tones, and indigo/violet as the primary brand color', 'business': 'Abridge'}
- {'why': 'Healthcare product using soft cream backgrounds, pill-shaped CTAs, and editorial serif display type against clean sans body text', 'business': 'Sword Health'}
- {'why': 'Warm cream surfaces, concentrated accent colors on otherwise neutral palette, and the editorial serif + geometric sans typography approach', 'business': 'Walnut'}

## Agent Prompt Guide

**Quick Color Reference**
- Background: #f8f3eb (cream)
- Surface: #ffffff (white)
- Text: #080331 (Deep Ink)
- Border: #000000 (True Black, for high-contrast hairlines)
- Accent: #4865ff (Primary Indigo)
- primary action: #4865ff (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #4865ff background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Feature Card Grid (2-column)**: White (#ffffff) card, 16px border-radius, 32px padding. Icon (24px, #080331 stroke) in top-left. Heading: Reckless Neue 24px weight 400, #080331. Description: Saans 16px weight 400, #080331. Circular arrow button (100px radius, white background, #080331 arrow) in top-right corner.


4. **Tinted Category Card**: Background #f098d7 (Blossom), 16px radius, 32px padding. Icon prefix + heading: Reckless Neue 24px, #080331. Body: Saans 16px weight 400, #080331. Embedded product screenshot at bottom: white (#ffffff) container, 16px radius.

5. **Section Header**: Centered. Small pill badge (1600px radius, 10px vertical padding, Saans 12px, #080331 text, cream or white background) above. Headline: Reckless Neue 48px weight 400, #080331, line-height 1.1. 40px gap to optional subtext: Saans 20px weight 400, #080331.

## Visual Design Principles

1. **Warmth over sterility**: Every system decision (cream canvas, warm shadows, serif headlines) softens the clinical expectation of healthcare software. This is deliberate emotional design for a senior care audience.

2. **Concentrated color**: The palette is mostly neutral cream and white. Color appears in specific, high-impact moments: circular portrait frames, tinted feature cards, and the single indigo CTA. This makes each color instance feel intentional and celebratory rather than decorative noise.

3. **Pill everything**: 1600px radius is the default for all interactive surfaces and many decorative elements. This creates a soft, approachable, non-corporate geometry that distinguishes the system from angular enterprise software.

4. **Editorial typography**: The serif/sans pairing (Reckless Neue + Saans) borrows from magazine design, not software UI conventions. Headlines are meant to be read and appreciated, not scanned. Weight 400 only for serif — no bold variants exist.

5. **Layered surface hierarchy**: Four distinct surface levels (cream → white → tinted → vibrant) create depth through color temperature, not shadow weight. Cards cast minimal shadows because the color difference already establishes elevation.

## Typography Pairing Rationale

Reckless Neue (serif) and Saans (sans) form a deliberate editorial-meets-functional pairing. The serif carries emotional weight and trustworthiness — critical for a platform handling elder care data. Saans provides the precision and legibility needed for dense UI (tables, forms, data). Both are used at regular weight (400) as the primary, with Saans alone using 500 for interactive emphasis. This restraint means the visual hierarchy is created by size and color, not by weight contrast — a hallmark of confident editorial design.
