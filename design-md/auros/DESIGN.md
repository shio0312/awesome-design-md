# Auros — Design System

> **North Star**: Abyssal terminal with bioluminescent data orbs
> **Theme**: dark
> **Source**: https://auros.global
> **Refero Style**: https://styles.refero.design/style/21cfe0c1-778d-4613-9f47-a5718eb929b3
> **Synced**: 2026-09-01

## Overview

Auros operates as an abyssal fintech terminal: near-black teal canvas with bioluminescent data orbs and teal-to-pink light gradients that suggest depth, liquidity, and flow. The interface is sparse and cinematic, relying on a single custom display face (Matter) at medium weight with aggressive negative tracking to create scale without shouting. Color is rationed — achromatic whites and silvers carry almost all content, while the chromatic palette is reserved for atmospheric gradients, card surface differentiation, and one signature pill button that morphs from teal-cyan to lavender-pink. Cards float on subtle teal-tinted surface lifts (16px radius, no shadows) rather than using elevation, so the hierarchy reads as depth-of-water rather than shadow-on-paper. Components feel engineered and instrument-like: uppercase tracked labels, thin geometric arrow icons, large numerical stats in pale pink.

## Color Palette

- **Liquid Abyss**: `#012624` — Primary canvas — page background, header, hero, and the dominant dark-teal field. Establishes the deep-water atmosphere [brand]
- **Liquid Deep**: `#011d1c` — Recessed surface level — footer background and deeper card panels. Reads as a half-step darker than the canvas, creating a subtle depth gradient downward [brand]
- **Liquid Kelp**: `#003734` — Raised card surface and primary button fill — the lifted surface that sits one step above the abyss. Used for feature cards, content panels, and the gradient button's origin point [brand]
- **Liquid Mist**: `#edfffe` — Cool-tinted off-white for emphasized body text, section labels, and warm-light typographic moments. Carries a barely-perceptible cyan whisper that ties body text to the teal atmosphere [neutral]
- **Platinum**: `#ffffff` — Pure white for headings, nav items, icon strokes, and high-contrast text. The dominant text color across all heading levels and the primary nav [neutral]
- **Silver Mist**: `#bbc7c6` — Secondary body text, muted descriptions, and link color in resting state. Carries a faint green undertone that harmonizes with the teal canvas [neutral]
- **Ash**: `#f2f2f2` — Tertiary text for pull-quotes and testimonial copy. A neutral cool-gray fallback when Silver Mist's teal undertone is too colored [neutral]
- **Slate Deep**: `#707777` — Subtle surface tint for inactive or low-emphasis backgrounds. Sits between canvas and card for very low-elevation differentiation [neutral]
- **Lavender Phosphor**: `#fde9ff` — Highlight color for large statistics, counter numbers, and emphasis figures. The pink end of the signature gradient — used sparingly as luminous punctuation on dark surfaces [accent]
- **Bioluminescent Gradient**: `#00827c` — Signature button and UI gradient — linear sweep from teal-cyan through pale aqua into lavender-pink. The brand's signature chromatic gesture [accent]
- **Aurora Gradient**: `#cbfffc` — Supporting palette color for small decorative accents when the core palette needs contrast. [accent]

## Typography

- **Matter**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.4 |
| body | 16 | — | 1.4 |
| subheading | 24 | — | 1.3 |
| heading | 36 | — | 1 |
| heading-lg | 61 | — | 1 |
| display | 96 | — | 1 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 36-48px
- **Element Gap**: 20px
- **Section Gap**: 68px
- **Border Radius**: {'cards': '16px', 'small': '6px', 'buttons': '6px'}

## Layout

Full-bleed dark canvas with max-width 1440px content. Hero is a centered text stack (eyebrow → headline → subtext → CTA) occupying the full viewport height, with the particle sphere as a background element. Sections are full-width bands separated by generous 68px+ vertical gaps, alternating between canvas and slightly recessed surfaces. The Explore section uses an asymmetric two-column layout: left column is stacked feature cards, right column holds the geometric molecular illustration. Content is centered in narrow columns (max ~600px) for readability rather than stretching edge-to-edge. The footer is a recessed well (#011d1c) with 120px vertical padding, creating a deep-pool effect. Navigation is a thin transparent bar with items spaced at 16–24px gaps. The overall rhythm is cinematic and spacious — each section breathes, and the deep-water color scheme makes every gap feel like falling deeper.

## Surfaces / Elevation

- **Liquid Abyss**
- **Liquid Deep**
- **Liquid Kelp**
- **Slate Deep**

## Imagery

Imagery is minimal and atmospheric. The hero features a 3D particle sphere — thousands of small teal-cyan and white dots forming a rotating orb that picks up the canvas color and the lavender-pink accent at its edges, creating a bioluminescent data-entity effect. Section decorations include flat geometric molecular diagrams (white circles and thin connector lines on the dark canvas) used as right-column balancing elements. No photography, no lifestyle imagery, no people — the visual language is pure data-graphics and abstract forms. The particle sphere is the defining brand mark visual; it should appear at least once on any major page to anchor the deep-water metaphor.

## Design Principles

### Do

- Use only the teal-green surface stack (#011d1c → #012624 → #003734) for background differentiation — never introduce gray, black, or blue surfaces
- Reserve the aurora gradient exclusively for primary CTAs and signature accent moments — never as a background fill or decoration
- Set all headings at Matter weight 500 — no bold, no light, no other weights at display sizes
- Apply uppercase tracking (0.08–0.15em) to all section labels, kickers, and eyebrow text at 10–20px
- Use lavender-phosphor pink (#fde9ff) only for large statistics and emphasis figures — never for body text or UI controls
- Keep card radii at 16px and small element radii at 6px — these two values are the complete shape vocabulary
- Use line-height 1.0 for all display text above 36px and line-height 1.4 for all body text — the contrast defines the typographic rhythm

### Don't

- Do not use drop shadows or box-shadows for elevation — differentiation comes from surface color shifts in the teal stack, not shadow
- Do not introduce bold (600+) or light (300-) weights at display sizes — the medium-only strategy is core to the mechanical confidence
- Do not use white (#ffffff) for body text — reserve pure white for headings and nav, use silver (#bbc7c6) or mist (#edfffe) for body
- Do not apply the aurora gradient to text, borders, or backgrounds larger than a single button — it loses luminosity at scale
- Do not use rounded corners above 16px — the system is sharp-rounded, not pill-shaped (buttons are 6px, cards are 16px)
- Do not place light text on light-pink (#fde9ff) — the pink is a background for dark text, not a text color on dark surfaces
- Do not use any color outside the Liquid teal scale, silver neutrals, and lavender-phosphor accent — the palette is rationed and deliberate

## Components

### Gradient Pill Button

Filled button with the aurora gradient background (cyan → white → pink). 6px border-radius, 32px vertical padding, 22px horizontal padding. Text in dark color (#222222) at 14px Arial, uppercase. Used for the most important action on each section. The gradient direction is horizontal, creating a sunrise effect.

### Ghost Navigation Link

Transparent background, no border, uppercase text at 12px Matter weight 400 with 0.12em letter-spacing. White color in active state, silver (#bbc7c6) for inactive. No padding — sits inline with tight 16px column-gap between items.

### Surface Card

Card with #003734 (Liquid Kelp) background, 16px border-radius, 36px padding all sides. No shadow, no border. Headings at 36px Matter 500 white, body at 16px Matter 400 silver. Used for feature blocks and content panels on the Explore section.

### Recessed Card

Card with #011d1c (Liquid Deep) background, 16px border-radius, 120px vertical padding. Creates a sunken well effect — the deepest UI surface, used for footer-adjacent content blocks and call-to-action panels with maximum breathing room.

### Feature Row Card

Transparent background card with 16px radius and 48px vertical / 36px horizontal padding. Contains a heading, body description, and a small square arrow icon button (32×32, 6px radius, dark teal fill with white arrow). Used for the three service divisions (Proprietary Trading, Liquidity Solutions, Careers) in the Explore section.

### Arrow Icon Button

32×32 square button, 6px border-radius, semi-transparent dark teal fill (rgba(3, 81, 75, 0.5)). Contains a white diagonal arrow (↗) icon. Always positioned to the right of a card title as a 'go to' trigger.

### Uppercase Section Label

12px or 20px Matter weight 500, uppercase, letter-spacing 0.08–0.12em, silver (#bbc7c6) or mist (#edfffe) color. Appears above section headings as a categorical label (e.g. 'AUROS', 'EXPLORE'). Wide tracking is signature — it reads as technical instrumentation labeling.

### Hero Headline

61–96px Matter weight 500, line-height 1.0, letter-spacing -0.04em, white. Fluid sizing via clamp(2.5rem, ..., 3.8rem) for H1 and clamp(2.1rem, ..., 3rem) for H2. Tight tracking compensates for the geometric letterforms at scale.

### Oversized Kinetic Text

86–295px Matter weight 500 at line-height 1.0, letter-spacing -0.046em. Used for massive section markers (the 'We D' text visible in the particle sphere section). The extreme size creates a kinetic, almost physical presence — text as environmental element.

### Statistic Counter

Large number in lavender-phosphor pink (#fde9ff) with label below in mist (#edfffe) or silver at 13px uppercase tracked. The pink-on-teal combination is the signature emphasis treatment — statistics glow against the dark canvas.

### Navigation Bar

Full-width header, transparent background, ~80px height. Logo (Auros wordmark + mark) left, nav links centered, CTA button right. 6px radius on the CTA. Items separated by 16–24px gaps.

### Geometric Molecule Illustration

Flat geometric pattern of circles and connector shapes in silver/white, positioned as right-column decoration in the Explore section. No fill complexity — just white circles and thin connector lines forming an abstract molecular/network diagram.

### Particle Sphere Visual

3D particle sphere rendered in teal-cyan and white dots, rotating in the hero or section transition. The particles pick up the canvas teal and the accent pink, creating a bioluminescent data orb effect. Functions as a brand-defining visual element.

## Similar Design Systems

- {'why': 'Same dark teal-black crypto-native palette with white text, generous spacing, and minimal decoration — both feel like trading-terminal instrument panels rather than marketing sites', 'business': 'Wintermute'}
- {'why': 'Dark mode institutional crypto aesthetic with uppercase tracked labels, medium-weight display type, and a single restrained accent color — both prioritize data-readability over visual spectacle', 'business': 'Jump Crypto'}
- {'why': 'Deep dark canvas with luminous accent moments, spacious section rhythm, and a focus on scale through type rather than imagery — similar cinematic financial-institution atmosphere', 'business': 'Galaxy Digital'}
- {'why': 'Dark teal-dominant palette with gradient accent buttons, geometric decorative elements, and medium-weight geometric type — shares the bioluminescent fintech-terminal sensibility', 'business': 'Flowdesk'}

## Agent Prompt Guide

**Quick Color Reference**
- Text (primary): #ffffff
- Text (body/secondary): #bbc7c6
- Text (emphasis/mist): #edfffe
- Background (canvas): #012624
- Border: #707777 or rgba(255,255,255,0.1)
- Accent (stats/highlights): #fde9ff
- primary action: #003734 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #003734 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Create a feature card:** Background #003734, 16px radius, 36px padding. Heading at 36px Matter 500 #ffffff, line-height 1.0. Body at 16px Matter 400 #bbc7c6. Arrow icon button (32×32, 6px radius, rgba(3,81,75,0.5) fill) positioned top-right with white ↗ icon.

3. **Create a statistics block:** Three columns. Large number (e.g. '$18.21B') at 86px Matter 500 #fde9ff, line-height 1.0, letter-spacing -3.96px. Label below at 13px Matter 400, uppercase, 0.055em letter-spacing, #edfffe.
