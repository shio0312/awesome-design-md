# Portal — Design System

> **North Star**: twilight serif editorial — a premium indie magazine spread sitting inside a native iOS aesthetic
> **Theme**: light
> **Source**: https://useportal.net
> **Refero Style**: https://styles.refero.design/style/b9aeb945-2f6e-4557-9115-e3ff3a8f8dc8
> **Synced**: 2026-09-01

## Overview

Portal uses a twilight-editorial visual language: a dramatic sunset gradient hero (sky-blue fading through violet to warm coral) gives way to a clean, paper-white editorial canvas below. Display headlines are set in Perfectly Nineties — a confident retro serif that signals craft over typical startup sans. Body and UI copy stay in Inter at restrained sizes, with one vivid iOS-blue accent (#007aff) punctuating an otherwise achromatic system. Surfaces are flat and generously rounded: cards at 22-30px, buttons as full pills at 50px, and the floating nav as a soft white capsule. Elevation is whispered rather than dropped — the system prefers 1px outlines and pale #f7f7f7 glow rings over heavy shadows.

## Color Palette

- **Signal Blue**: `#007aff` — Primary action buttons, active states, brand icon highlights, inline links — the only chromatic accent in an otherwise achromatic system. iOS-native vivid blue that makes functional elements feel switched on [brand]
- **Ink Black**: `#000000` — Headings, primary borders, button text — maximum-contrast structural color [neutral]
- **Graphite**: `#3e3e3e` — Body text, secondary borders — softer than black for sustained reading on white [neutral]
- **Smoke**: `#636363` — Muted helper text, metadata labels, subtle borders [neutral]
- **Paper White**: `#ffffff` — Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color [neutral]
- **Ash Mist**: `#f7f7f7` — Page canvas background, soft glow rings around cards and images, pale elevation halos [neutral]
- **Dusk Gradient**: `#7a7fd4` — Hero background — sky-blue descending through violet to warm coral sunset with landscape silhouettes at the base. Defines the system's only atmospheric moment [accent]

## Typography

- **Perfectly Nineties Regular**
- **Inter**
- **System sans-serif**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| micro | 10 | — | 1.2 |
| caption | 12 | — | 1.2 |
| body-sm | 14 | — | 1.3 |
| body | 16 | — | 1.35 |
| heading-sm | 18 | — | 1.35 |
| heading | 36 | — | 1 |
| display | 48 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 20px
- **Element Gap**: 10px
- **Section Gap**: 80-120px
- **Border Radius**: {'nav': '22px', 'cards': '22-30px', 'badges': '50px', 'images': '30-40px', 'buttons': '50px'}

## Layout

Centered max-width layout at approximately 1200px. The hero is full-bleed with the gradient extending edge-to-edge, and a device mockup overlapping the bottom into a landscape silhouette. Below the hero, content flows on a #f7f7f7 canvas with centered or left-aligned text columns at 640-720px reading width. Section gaps are generous (80-120px) to let the editorial typography breathe. The navigation is a floating pill capsule anchored at the top of the viewport with margin, not a full-width bar. Content sections are single-column and text-dominant — no multi-column grids or card grids in the marketing sections. The product mockup is the only visual element competing with text in the hero composition.

## Surfaces / Elevation

- **Page Canvas**
- **Card Surface**
- **Nav Pill**
- **Hero Atmosphere**

**Shadow tokens:**

## Imagery

The hero is the only atmospheric visual: a full-bleed gradient sunset landscape (blue sky through violet to coral) with silhouetted tree horizons along the bottom edge. All other imagery is product screenshots presented inside white device-frame mockups with soft glow rings. There is no lifestyle photography, no stock imagery, and no illustrations. The product UI itself (shown in the device mockup) uses white cards with clean typography and small inline data elements. The visual strategy is one dramatic atmospheric moment (the hero) followed by pure UI and editorial typography. The blue brand accent (#007aff) appears in the gradient brand icon and as functional highlights in the product UI — never as decorative imagery.

## Design Principles

### Do

- Set all display headings in Perfectly Nineties Regular at 36-48px, line-height 1.0, weight 400 — this serif is the system's signature voice and must not be diluted by using it at smaller sizes
- Use #007aff exclusively for functional accents: primary CTA fills, active states, brand icon highlights, and inline links. Never use it for decorative backgrounds or large surface fills
- Make every button a full pill at 50px border-radius with no exception — 12-14px vertical padding, 20-24px horizontal padding
- Keep body text in Inter at 14-16px, line-height 1.30-1.35, with -0.02em letter-spacing for a refined iOS-native feel
- Round all card and image corners to 22-30px — the generous radii are what give the system its soft, premium character
- Default the page canvas to #f7f7f7 with cards on #ffffff. Use the 5px #f7f7f7 glow ring as your primary elevation technique instead of drop shadows
- Use #000000 for headings and primary borders only; switch to #3e3e3 for body text and #636363 for muted helper text and secondary metadata

### Don't

- Don't introduce a second chromatic accent color — the system is monochromatic plus exactly one blue (#007aff)
- Don't use Perfectly Nineties for body text, captions, buttons, or UI labels — it is display-only at 36px and above
- Don't apply drop shadows heavier than the 5px #f7f7f7 glow ring or 1px #000000 outline — heavy shadows break the flat editorial feel
- Don't use sharp corners (0-4px radius) on any interactive element or card — minimum 7px, prefer 16px+ for cards and 50px for buttons
- Don't set body text below 14px in Inter or above weight 600 — the weight range is the system's restraint mechanism
- Don't place #000000 text directly on a chromatic or gradient background — text must sit on white or #f7f7f7 surfaces only
- Don't use #007aff for large fills, hero backgrounds, or decorative shapes — it is a functional accent, not a surface color

## Components

### Hero Pill Button

50px border-radius, #ffffff background, #000000 text in Inter 600 at 14-16px, padding 14px 24px. No border. The white-on-gradient contrast makes it the clear action target against the blue-to-coral backdrop

### Ghost Pill Button

50px border-radius, transparent background, 1.5px #000000 border, #000000 text in Inter 500 at 14-16px, padding 12px 22px. Outlined only — never filled

### Floating Nav Capsule

22px border-radius, #ffffff background, 1px border with 5px #f7f7f7 soft glow ring. Contains brand mark (gradient circle icon + 'Portal' wordmark in Inter 600 18px) on left, nav links (Product, Blog, Contact in Inter 500 14px #000000) on right. Padding 8px 16px. Floats with 16-24px top margin

### Device Mockup Card

Outer frame at 22-30px border-radius, #ffffff background, 5px #f7f7f7 glow ring as elevation. Inner screen area shows the Portal product UI at 16px border-radius. The mockup overlaps into the landscape silhouette at the hero's bottom

### Editorial Content Block

Centered or left-aligned text column at 640-720px max reading width. H2 in Perfectly Nineties 400 at 36px, #000000, line-height 1.0. Body in Inter 400 at 16px, #3e3e3, line-height 1.35, letter-spacing -0.32px. Paragraphs separated by 16-20px gap. Section gap 80-120px from adjacent blocks

### Brand Mark Icon

Circular icon with blue-to-violet gradient (matches hero gradient mid-tones), containing a white paper-plane or forward-arrow glyph. Paired with 'Portal' wordmark in Inter 600 18px, #000000. Icon-to-text gap 8px

### Project Card

16-22px border-radius, #ffffff background, 1px #f7f7f7 border or soft glow. Padding 20px. Project title in Inter 600 16px, metadata in Inter 400 14px #636363, status badges below

### Status Badge

50px border-radius full pill, Inter 500 12px text, padding 4px 10px. Subtle #f7f7f7 background for neutral states, #007aff-tinted background for active/paid states

### Nav Link Item

Inter 500 14px, #000000, 8px horizontal padding, 4px vertical padding. No underline. Hover: opacity 0.6 or subtle color transition

### Soft Glow Ring

0px 0px 0px 5px #f7f7f7 — a pale outline that creates the sense of light emanating from the element rather than a traditional drop shadow. The system's depth language

### Hero Gradient Background

180deg linear gradient from #4a7ff2 (sky-blue) at top through #7b7ed8 (violet) to #c98ab5 (mauve) and #e8a87c (warm coral) at the bottom, with dark landscape tree/horizon silhouettes along the bottom 15-20% of the viewport

## Similar Design Systems

- {'why': 'Same monochromatic palette with a single vivid accent color, generous rounded corners, and clean Inter-based UI typography', 'business': 'Linear'}
- {'why': 'Editorial display-serif headlines paired with minimal sans-serif body, clean white surfaces, and restrained accent usage', 'business': 'Pitch'}
- {'why': 'Magazine-style editorial layout with dramatic hero visuals and large confident serif type treatment', 'business': 'Framer'}
- {'why': 'Distinctive gradient brand identity with soft, generous rounded shapes and a single functional accent color', 'business': 'Arc Browser'}

## Agent Prompt Guide

## Quick Color Reference
- text (headings): #000000
- text (body): #3e3e3e
- text (muted): #636363
- background (canvas): #f7f7f7
- background (card): #ffffff
- border: #000000 (primary) / #f7f7f7 (soft glow ring)
- accent: #007aff
- primary action: #007aff (filled action)

## Example Component Prompts

1. Create a Primary Action Button: #007aff background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Floating nav capsule**: White #ffffff background, 22px border-radius, 1px subtle border with 5px #f7f7f7 soft glow ring. Left: gradient circle icon (40px, blue-to-violet gradient) + 'Portal' wordmark in Inter 600 18px #000000. Right: 'Product', 'Blog', 'Contact' in Inter 500 14px #000000, separated by 20px gaps. Container padding 8px 16px. Float at top with 20px margin.

3. **Editorial content block**: Centered on #f7f7f7 canvas, max-width 640px. H2 in Perfectly Nineties Regular 400 at 36px, #000000, line-height 1.0. Body paragraph in Inter 400 at 16px, #3e3e3e, line-height 1.35, letter-spacing -0.32px. Paragraph margin-bottom 20px. Section gap 100px above and below.

4. **Device mockup card**: White #ffffff frame at 22px border-radius, 5px #f7f7f7 glow ring. Inner screen area: #ffffff background, project card with 16px border-radius containing a title in Inter 600 16px #000000, metadata in Inter 400 14px #636363, and a status badge (50px radius pill, Inter 500 12px).

5. **Ghost nav link**: Inter 500 14px, #000000, padding 4px 8px, no underline, no border. Hover: opacity 0.6 with 200ms transition. Set inside a white #ffffff nav capsule with 22px border-radius.

## Signature Choices

What makes this system visually distinctive from the sea of generic SaaS landing pages:

- **Retro serif in a tech product**: Perfectly Nineties Regular at display sizes is anti-convention for SaaS. Most startups use geometric sans for everything. The serif creates a magazine/editorial voice that signals craft and taste over speed and engineering.

- **Single iOS-blue accent**: #007aff is Apple's system blue. Using it as the only chromatic accent in an otherwise achromatic system is a deliberate native-aesthetic choice — it makes the product feel at home on macOS/iOS without copying Apple wholesale.

- **Glow rings instead of shadows**: The 5px #f7f7f7 halo around cards and mockups is a depth technique borrowed from visionOS/frosted glass. It whispers elevation rather than declaring it with a drop shadow.

- **50px pill buttons**: Full rounding on all interactive elements. The pill is the system's gesture toward softness — combined with the serif headlines, it creates a product that feels handcrafted rather than engineered.

- **Hero as atmosphere, not pitch**: The gradient landscape hero doesn't show a dashboard screenshot or a feature list — it sets a mood. The product earns attention through beauty, not claims. This is unusual in a productivity SaaS category that typically leads with product screenshots.
