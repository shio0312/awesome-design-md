# Hungry Tiger — Design System

> **North Star**: Turmeric-bright graffiti on a tandoor wall. A single gold-on-rust palette with display type so large it reads as a spice market sign, not a webpage.
> **Theme**: dark
> **Source**: https://www.eathungrytiger.com
> **Refero Style**: https://styles.refero.design/style/47f15da7-8905-45b3-bcab-06a4277c6168
> **Synced**: 2026-09-01

## Overview

Hungry Tiger is a fire-roasted condiment brand rendered as a maximalist typographic poster: a deep rust-brown canvas, a single searing Tiger Gold accent, and an absurdly oversized custom display face that swallows the viewport. The system behaves like a spice label — confident, warm, slightly aggressive — with pill-shaped controls, dotted horizontal rules, and dense botanical watermarks that suggest Indian heat without literal illustration. Text is the hero; product photography is small and isolated against the dark. Every surface shares the same warm brown family, and contrast is driven by the gold against charred browns, not by adding new hues.

## Color Palette

- **Tiger Gold**: `#faae33` — Primary action, filled buttons, active nav, heading strokes, key icon accents — the only chromatic color permitted to leave the warm-brown monochrome and interrupt the page [brand]
- **Ember Rust**: `#823513` — Dominant page canvas and hero backdrop — the color that defines every viewport [brand]
- **Saffron Glow**: `#9f531b` — Secondary heading accent, decorative borders, mid-tone text — a warm orange that softens Tiger Gold without competing [brand]
- **Dark Spice**: `#402011` — Card surfaces, input fields, badge fills, button ghost backgrounds, body text color — the workhorse dark-brown that lifts content off Ember Rust [neutral]
- **Charred Clove**: `#281006` — Deepest surface — used for innermost cards, modal scrim, and the background behind the deepest contrast pairs [neutral]
- **Cardamom Brown**: `#6b2e12` — Input borders, subtle dividers, muted inline elements — a step between Dark Spice and Ember Rust [neutral]
- **Chili Red**: `#d1255c` — Saturated accent reserved for badge fills and alert-level highlights — appears sparingly to signal heat [accent]

## Typography

- **Salmond**
- **Graphikx**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.2 |
| subheading | 18 | — | 1.2 |
| heading-sm | 29 | — | 1.1 |
| heading | 65 | — | 0.95 |
| heading-lg | 101 | — | 0.9 |
| display | 195 | — | 0.8 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 12-16px
- **Element Gap**: 10px
- **Section Gap**: 80-120px
- **Border Radius**: {'cards': '6px', 'badges': '9999px', 'inputs': '9999px', 'buttons': '9999px'}

## Layout

Full-bleed dark page with no max-width container; content is laid out in asymmetric two-column compositions where a massive display headline occupies one side and a small product image anchors the other. The hero is a full-viewport poster: eyebrow text top-left, then 200px+ display type, then a centered product bottle below. Subsequent sections alternate between left-anchored headline + right-side product bottle and centered product + surrounding type. Dotted gold dividers separate every major band. Navigation is a minimal top bar with ghost pill buttons and a centered brand mark. Floating circular icon buttons (bag, basket) dock in the bottom-right corner. Vertical rhythm is spacious — 80–120px between sections, allowing the poster-scale type to breathe without competing.

## Surfaces / Elevation

- **Tandoor Canvas**
- **Spice Card**
- **Charred Core**

**Shadow tokens:**

## Imagery

Product photography is tightly cropped, studio-lit jars of sauce centered against the Ember Rust canvas — no lifestyle context, no hands, no kitchen. The jar IS the hero. Background atmosphere is delivered through low-opacity botanical watermarks (ferns, leaves, florals) that read as spice-garden texture rather than illustration. No 3D renders, no abstract graphics, no people. Imagery density is intentionally low — the page is 90% type, 10% product.

## Design Principles

### Do

- Use Salmond at 130–213px weight 700 with line-height 0.80–0.90 for all hero and section display headlines — this is the brand's voice and must never be downsized into body territory
- Set all buttons, badges, inputs, and icon containers to 9999px (1296px in tokens) radius — sharp corners break the spice-label personality
- Use only #faae33 as the chromatic accent against the brown monochrome; never introduce additional bright colors except the reserved #d1255c for heat-level badges
- Step surface depth through three browns: #823513 (page) → #402011 (card) → #281006 (deepest) — never use box-shadow to imply elevation
- Apply dotted #faae33 horizontal rules as section dividers between major viewports instead of relying on whitespace alone
- Tighten letter-spacing inversely to size: -0.02em at display sizes, 0.01–0.02em at 11–18px — Salmond's tracking is a load-bearing part of its character
- Crown every viewport with massive type first, then position product photography as a small anchored element below — the page is a poster, not a storefront

### Don't

- Do not introduce a secondary display typeface — Salmond owns the entire type system, and adding a different heading face dilutes the brand voice
- Do not use box-shadow, drop-shadow, or glow effects on any component — the flat tandoor-wall aesthetic is non-negotiable
- Do not place product photography in large rectangular frames, cards, or with rounded edges — the bottle should sit raw on the canvas
- Do not use the 6px radius for anything other than cards — buttons, badges, inputs, and icon containers must all be full pills
- Do not dilute the gold-on-brown palette with white, blue, green, or cool neutrals — the system is intentionally monochromatic-warm
- Do not let body copy exceed 18px or sit at more than 1.4 line-height — the design is poster-first and any comfortable reading block will feel out of place
- Do not use solid color blocks for section backgrounds — every section is Ember Rust; depth comes from type scale and surface color shifts, not from alternating bands

## Components

### Ghost Outline Button

Salmond weight 500, 13px, 0.01em tracking, text color #faae33, 1px border in #faae33, fully rounded radius (1296px — effectively pill), padding 8px 17px, transparent fill so the Ember Rust canvas reads through. Used for every nav link and secondary action.

### Filled Primary Button

Salmond weight 500, 13px, #281006 text on #faae33 fill, 1px #faae33 border, 1296px radius, padding 10px 20px. The only filled button in the system — its darkness against the gold makes it the loudest interactive element on any page.

### Ghost Borderless Button

Salmond 13px weight 500, #faae33 text, no border, no background. Appears in paragraph-adjacent micro-CTA positions.

### Pill Badge

Salmond 11–12px weight 500 uppercase, 0.02em tracking, pill radius 1080px, padding 4–8px vertical, 12–16px horizontal. Fill is #faae33 with #281006 text for primary tags, or #402011 with #faae33 text for secondary tags.

### Alert Badge

Pill-shaped, 1080px radius, fill #d1255c, 11px Salmond weight 500, padding 4px 12px. Reserved for the rare spicy/heat callouts.

### Pill Input Field

Fully rounded (1224px radius) input, 1px #6b2e12 border on transparent fill, Salmond 13px weight 500 placeholder, 12–16px vertical padding, 16–20px horizontal padding. No visible focus ring — interaction states use border-color shift to #faae33.

### Surface Card

6px radius, fill #402011, padding 12–16px, no shadow — depth comes from the 2-step color shift against the Ember Rust canvas, not from elevation.

### Product Bottle Showcase

Raw product photography on a transparent canvas, no card frame, no background plate. The jar sits directly on the Ember Rust hero with a subtle warm highlight rim suggesting backlight.

### Botanical Watermark Layer

Faded fern/leaf/flower illustrations rendered as background watermarks behind content sections. Low-contrast, near-invisible at resting state — they only become readable when the eye settles, reinforcing the 'tandoor wall' texture without competing with type.

### Dotted Divider

1px dotted line in #faae33 spanning full width, used between major viewport sections. Replaces whitespace-only separation and gives the page a label-printed rhythm.

### Iconography Set

Thin-stroke 1.5px line icons rendered in #faae33, 16–20px, circular button containers with 1296px radius. Icons are always gold, never filled, never multi-color.

## Similar Design Systems

- {'why': 'Same single warm-color-dominant dark canvas with a vivid accent and oversized display type; both treat the product label as the design language', 'business': 'Graza'}
- {'why': 'Similar maximalist Asian-food brand typography with tightly-tracked display faces and warm rust palettes', 'business': 'Omsom'}
- {'why': 'Bold dark-mode product brand with one saturated accent color and poster-scale headlines dominating every viewport', 'business': 'Fly by Jing'}
- {'why': 'Same single-accent-on-dark-rust visual system with spice-market typographic confidence and flat surfaces', 'business': 'Diaspora Co.'}

## Agent Prompt Guide

## Quick Color Reference
- Page canvas: #823513 (Ember Rust)
- Card surface: #402011 (Dark Spice)
- Deepest surface: #281006 (Charred Clove)
- Primary text / heading strokes: #faae33 (Tiger Gold)
- Body text: #402011 (Dark Spice) — or #faae33 on dark fields
- Hairline borders / input borders: #6b2e12 (Cardamom Brown)
- Heat-level accent: #d1255c (Chili Red) — badges only
- primary action: #faae33 (filled action)

## 3–5 Example Component Prompts
1. **Hero Display Headline**: Render 'BOLD FLAVOR' at 195px Salmond weight 700, line-height 0.80, letter-spacing -0.02em, color #faae33, on a full-bleed #823513 canvas. Place a 13px Salmond weight 500 eyebrow 'FIRE ROASTED INDIAN SAUCE' above it in #faae33 with 0.01em tracking.

2. **Ghost Nav Button**: Pill-shaped button, 1296px radius, transparent fill, 1px #faae33 border, padding 8px 17px, text 'SAUCE' in 13px Salmond weight 500, color #faae33, letter-spacing 0.01em.

3. **Filled Primary CTA**: Pill button, 1296px radius, fill #faae33, 1px #faae33 border, padding 10px 20px, text 'BUY NOW' in 13px Salmond weight 500, color #281006.

4. **Pill Input Field**: Fully rounded input (1224px radius), transparent fill, 1px #6b2e12 border, padding 12px 20px, placeholder 'email address' in 13px Salmond weight 500 #faae33 at 60% opacity. On focus, border shifts to #faae33.

5. **Product Card Section**: Full-bleed #823513 band, left column 'A NEW ANGLE OF FLAVOR' at 101px Salmond weight 700, line-height 0.90, color #faae33. Right column: raw product bottle PNG, no card frame, no background plate, anchored bottom-right. Caption 'DISCOVER HOW OUR CREAMY TOMATO BLEND AND AUTHENTIC SPICES ELEVATE EVERY MEAL' in 13px Salmond weight 500 #faae33 below the headline.
