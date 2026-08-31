# Revolut — Design System

> **North Star**: Monochrome editorial banking on cloud photography — white ink, pill buttons, one blue ribbon of color in an otherwise grayscale world.
> **Theme**: light
> **Source**: https://revolut.com
> **Refero Style**: https://styles.refero.design/style/a3161c3c-26d4-425b-aaa3-4fc3f06b77ee
> **Synced**: 2026-09-01

## Overview

Revolut runs an editorial-monochrome banking language: the product UI is nearly entirely achromatic — white surfaces, #1f1f1f ink, hairline #c9c9cd dividers — and the entire color budget is outsourced to full-bleed sky photography that washes across hero sections. Aeonik Pro at weight 500 carries every display moment with aggressively tightened tracking (-0.024em at 88px), while Inter at 16px handles all UI density. Controls are exclusively pill-shaped (9999px) in four restrained variants, and the only chromatic element in the entire system is a single blue gradient reserved for the promotional bar. Surfaces prefer to float without shadows — edges do the work that elevation usually would.

## Color Palette

- **Ink**: `#1f1f1f` — Primary text, footer background, filled dark buttons. The near-black that carries all body and display copy [neutral]
- **Pure Black**: `#000000` — Button text on light surfaces, pure-black background blocks. Used where maximum contrast is required [neutral]
- **Bone**: `#ffffff` — Page canvas, card surfaces, button text on dark fills, button borders on light fills. The dominant surface color across all sections [neutral]
- **Ash Grey**: `#c9c9cd` — Hairline borders, disabled dividers, and the dominant link color at 80 occurrences. The neutral that defines edge separation without shadow [neutral]
- **Mist**: `#f7f7f7` — List and grouped-background fills — the recessed surface beneath cards, tables, and secondary containers [neutral]
- **Slate**: `#717173` — Neutral form states, badge text, and quiet UI feedback where color should stay understated. [neutral]
- **Graphite**: `#4c4c4c` — Tertiary body text, inline badge copy, and minor muted surfaces between true ink and slate [neutral]
- **Cobalt Wash**: `#1227fd` — Promotional bar gradient start. The single chromatic accent in the entire system — only ever appears as part of the blue gradient on top-of-page offer strips [brand]

## Typography

- **Aeonik Pro**
- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 18 |
| body-sm | 14 | — | 22 |
| body | 16 | — | 19.2 |
| subheading | 18 | — | 24 |
| heading-sm | 24 | — | 28 |
| heading | 32 | — | 38 |
| heading-lg | 40 | — | 48 |
| display | 52 | — | 52 |
| display-xl | 88 | — | 88 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '9999px', 'cards': '22.5px', 'lists': '20px', 'buttons': '9999px', 'smallControls': '12px'}

## Surfaces / Elevation

- **Canvas**
- **Recessed**
- **Edge**
- **Card**
- **Inverted**

## Imagery

Photography is the primary color source. Hero sections use full-bleed, high-key sky-and-cloud photography — pale blues, whites, and warm skin tones — that acts as the canvas for white display headlines. People are shot close-up, looking off-camera, in soft natural light, with a candid editorial feel rather than staged commercial poses. No decorative graphics, no 3D renders, no illustrations. Icons throughout the product are monochrome line icons at 1.5-2px stroke weight, neutral-colored, never filled with brand color. Award logos in the trust section are full-color third-party brand marks on white. Product UI is shown via iPhone-frame overlays with 22.5px top radius, never as flat screenshots.

## Design Principles

### Do

- Use 9999px radius for every button, tag, and input — pill geometry is the signature.
- Keep display headlines at Aeonik Pro weight 500, never heavier — authority comes from size, not weight.
- Reserve #1227fd→#6fa0ff gradient exclusively for the top promotional bar; never use it on buttons, cards, or section backgrounds.
- Use #c9c9cd hairlines (1-2px) instead of shadows to separate cards and lists from the page canvas.
- Let full-bleed photography carry all color and atmosphere — keep UI surfaces #ffffff, #f7f7f7, or #1f1f1f.
- Apply tightening tracking at every display size: -0.024em at 88px through -0.010em at 24px, opening only at 12px uppercase (+0.015em).
- Place pricing and conversion sections on #1f1f1f backgrounds with white cards — the dark/light flip is the pricing module's signature.

### Don't

- Don't introduce new chromatic colors — the palette is 7 neutrals and one blue gradient, and that's the whole system.
- Don't apply shadows to cards or buttons — separation is achieved with #c9c9cd borders and surface color shifts, not elevation.
- Don't use a heading weight above 500 on Aeonik Pro — going to 600/700 breaks the editorial calm.
- Don't place the promo gradient on hero sections, buttons, or product cards — it loses its meaning if it appears more than once per page.
- Don't use square or slightly-rounded corners on primary actions — pills (9999px) are the only acceptable control shape.
- Don't mix Inter and Aeonik Pro at the same size — Aeonik Pro owns 18px and above, Inter owns 16px and below.
- Don't use color to indicate state on neutral surfaces — use opacity shifts and border weight instead (e.g. #1f1f1f at 80% vs 100%).

## Components

### Pill Button (Light)

White background, #1f1f1f text, #1f1f1f 2px border, 9999px radius, 10px 24px padding. 16px Inter weight 600. The 'Explore Savings' and 'Sign up' variant.

### Pill Button (Dark)

#1f1f1f background, white text, 9999px radius, 0px 20px padding with vertical centering. The 'Download the app' CTA — appears as a solid dark pill that photographs cleanly against sky imagery.

### Pill Button (Ghost on Photo)

rgba(255,255,255,0.1) background, white text, white 1px border, 9999px radius, 10px 24px padding. Glassmorphic treatment for buttons sitting on top of hero photography.

### Pill Button (Text Link)

Transparent background, #1f1f1f at 80% opacity text, 12px radius, no padding. Smaller interactive elements inside body copy.

### Promo Gradient Bar

linear-gradient(to right, #1227fd, #6fa0ff), 16px Inter weight 400 white text, centered. The only chromatic surface in the entire design system. 32-40px tall. Contains an underlined white link.

### Navigation Header

Dark #1f1f1f band across the top. White 'Revolut' wordmark left, 16px Inter nav items centered, 'Log in' text + 'Sign up' pill right. Sits above photo heroes without competing with them.

### Location Selector Pill

White background, 9999px radius, country flag emoji + label, 12-16px Inter. Sits inside a white utility strip above the dark nav.

### Phone Preview Card

22.5px top-left/top-right radius, 0px bottom radius. Full-bleed photo behind it, white card overlapping the photo bottom. Internal product UI shows on a clean white surface with a pill label like 'Accounts'.

### Pricing Tier Card

White background, 22.5px radius, 24-40px internal padding. Tier name (Aeonik Pro 24px weight 500), price (Aeonik Pro 32px weight 500), description body. Sits on a #1f1f1f section background to maximize card contrast.

### Trust Badge Block

Transparent background, centered logo or icon, 12-14px Inter caption below in #717173. Arranged in 3-column or 4-column grids separated by 40-80px gaps.

### Section Header (Muted)

24-40px Aeonik Pro weight 500, color #717173 (not #1f1f1f). The choice to use slate for section titles instead of ink is deliberate — it creates a calm editorial rhythm between hero and content.

### List Container

#f7f7f7 background, 20px radius, 16-24px internal padding. The recessed surface that sits one step below card white.

## Similar Design Systems

- {'why': 'Same full-bleed sky/cloud photography with massive light-weight display headlines overlaid, and the same near-black-on-white editorial restraint', 'business': 'Apple'}
- {'why': 'Same monochrome fintech language with a single accent color, pill-shaped buttons, and oversized Aeonik-style display type', 'business': 'Wise (TransferWise)'}
- {'why': 'Same achromatic banking palette and pill-button geometry, though N26 tends to use deeper blacks and heavier contrast', 'business': 'N26'}
- {'why': 'Same editorial monochrome approach with full-bleed photography carrying all the color, though Cash App uses green as a brand accent where Revolut uses blue', 'business': 'Cash App'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #1f1f1f
- background: #ffffff
- border: #c9c9cd
- muted text: #717173
- recessed surface: #f7f7f7
- dark surface: #1f1f1f
- primary action: #1f1f1f (filled action)
- promo accent: linear-gradient(to right, #1227fd, #6fa0ff)

**Example Component Prompts**

1. **Hero headline overlay**: Full-bleed sky photograph as background. Display headline at 88px Aeonik Pro weight 500, white, letter-spacing -2.112px. Subtext at 18px Aeonik Pro weight 400, white, line-height 24px. Dark pill button below: #1f1f1f background, white text, 9999px radius, 10px 24px padding, 16px Inter weight 600.

2. **Pricing tier card**: Three cards on a #1f1f1f section background. Each card: white background, 22.5px radius, 32px padding. Tier name at 24px Aeonik Pro weight 500 #1f1f1f, price at 32px Aeonik Pro weight 500 #1f1f1f, description at 16px Inter weight 400 #4c4c4c.

3. **Promotional bar**: linear-gradient(to right, #1227fd, #6fa0ff) background, 40px tall, centered. Text: 16px Inter weight 400 white. Underlined white link inline.

4. **Trust badge grid cell**: Transparent background, 40-80px gap to neighboring cells. Logo or icon centered, 12-14px Inter caption below in #717173.

5. **Section header**: 24-40px Aeonik Pro weight 500, color #717173 (not #1f1f1f), centered, max-width 800px. This slate color for section titles is the system's calm editorial signature.

## Photography Direction

Full-bleed sky and cloud photography is the only color source in the system. Treatments should follow three rules: (1) high-key, overexposed skies with soft cumulus clouds — never moody or dark, (2) human subjects shot in editorial close-up, looking off-camera, in warm natural daylight, candid rather than posed, (3) crops that leave generous negative space in the upper portion of the frame so white display headlines can sit cleanly on top without competing with the subject. Product UI is never shown as a flat screenshot — it is always inside a white iPhone-frame card with 22.5px top radius, overlapping the bottom edge of the photograph.
