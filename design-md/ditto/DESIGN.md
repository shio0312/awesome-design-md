# Ditto — Design System

> **North Star**: Sunlit wildflower compliance atelier. Warm cream surfaces, vivid yellow primary action, deep navy ink, organic color shapes blooming behind the product.
> **Theme**: light
> **Source**: https://trustditto.com
> **Refero Style**: https://styles.refero.design/style/e9001d5a-504d-47ed-aef0-d0d35fa86418
> **Synced**: 2026-09-01

## Overview

Ditto uses a sunlit, garden-inspired SaaS language: a warm cream canvas, organic decorative blobs in vivid greens, pinks, and yellows, and a confident pairing of a warm serif (Hedvig Letters) for headlines with a clean grotesque (Inter) for everything else. The deep navy-violet #130e30 carries all structural text and borders, while a single bright yellow #ffe228 powers every primary action — the contrast is so high it reads almost like a highlighter. Components stay lightweight: pill-shaped buttons (1440px radius), generously padded cards on a slightly green-tinted surface (#eff2e5), and minimal elevation. The mood is optimistic and approachable, not corporate or clinical — the floral backdrop shapes, serif headlines, and warm neutrals keep it human.

## Color Palette

- **Deep Ink**: `#130e30` — Primary text color, heading ink, card borders, secondary button fills — near-black violet that adds warmth over pure black [brand]
- **Hi-Yellow**: `#ffe228` — Primary action fill (filled CTA buttons), hero pill backgrounds, accent highlights — bright highlighter yellow with near-black text for maximum contrast [brand]
- **Moss Green**: `#59e25d` — Decorative organic shape fill behind hero — warm leaf green used in background blobs, not UI controls [accent]
- **Fuchsia**: `#e261e5` — Decorative organic shape fill behind hero — vivid pink used in background blobs, not UI controls [accent]
- **Slate**: `#5f5c6e` — Body text, helper copy, muted icons, subtle borders — cool desaturated gray for secondary information [neutral]
- **Canvas**: `#f9fbf2` — Page background, button ghost fills, lightest surface — near-white with slight green-warmth [neutral]
- **Soft Meadow**: `#eff2e5` — Card surfaces, nav background, elevated panels, hero backdrop — green-tinted off-white for soft surface separation [neutral]
- **Charcoal**: `#222222` — Secondary dark button text and borders, nav dividers — softer than pure black for dark UI elements [neutral]
- **Onyx**: `#000000` — Logo mark, nav text, input borders, fine stroke details — true black for highest-contrast elements [neutral]

## Typography

- **Hedvig Letters Serif**
- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.2 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.5 |
| heading-sm | 22 | — | 1.25 |
| heading | 32 | — | 1.15 |
| heading-lg | 48 | — | 1.1 |
| display | 64 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24-48px
- **Element Gap**: 12-16px
- **Section Gap**: 48-80px
- **Border Radius**: {'nav': '1440px', 'tags': '1440px', 'cards': '24px', 'icons': '1440px', 'images': '24-48px', 'buttons': '1440px'}

## Layout

Max-width 1200px centered container with generous side padding. Hero is a two-column split: left column holds the headline, subtext, email input with CTA, and Trustpilot badge; right column holds the product mockup card with organic blob backdrop. Below the hero, a customer logo trust strip sits on Soft Meadow. Sections alternate between white canvas and Soft Meadow bands, separated by 48-80px vertical gaps. Feature grids use 3 equal columns. Testimonials are a horizontal carousel with 3 cards visible. Navigation is a simple top bar, not sticky. The layout breathes — no information-dense blocks, every section has whitespace margins.

## Surfaces / Elevation

- **Canvas**
- **Soft Meadow**
- **Hi-Yellow Accent**
- **Deep Ink**

## Imagery

Product UI screenshots are the primary visual asset — shown inside a white card floating above organic colored blob shapes in green, fuchsia, yellow, and violet. The blobs are flat, irregular, and overlapping, creating a garden-meadow feel that softens the compliance/B2B context. Photography appears in section dividers (urban outdoor scenes with trees and architecture, high-saturation). Customer logos are monochrome in a horizontal trust strip. Iconography is minimal and line-style, not colorful. No 3D renders or illustrations of people — the visual identity is abstract, organic, and product-forward.

## Design Principles

### Do

- Use the 1440px pill radius on every button, input, nav link, tag, and icon container — the pill shape is the brand's signature geometry
- Pair the yellow CTA #ffe228 with the dark pill #130e30 for button hierarchy; never use two yellow buttons side by side
- Use Hedvig Letters Serif exclusively for headings ≥22px and Inter for everything below; never use Inter for headings or Hedvig for body copy
- Set body text to #130e30 (not pure black) for warmth; reserve #000000 for the logo mark, input borders, and high-contrast fine details
- Build the surface stack as Canvas #f9fbf2 → Soft Meadow #eff2e5 cards; the slight green tint is intentional and should be preserved
- Use the decorative organic blobs (green #59e25d, fuchsia #e261e5, yellow #ffe228, violet #130e30) only as background atmosphere behind hero/product visuals — never as UI fills or icon colors
- Tighten letter-spacing to -0.01em on all headings and -0.02em on small caps labels for the warm, literary headline feel

### Don't

- Do not use sharp corners (<16px) on buttons, inputs, or nav items — the pill is non-negotiable
- Do not introduce additional accent colors into the UI; green, pink, and fuchsia are decoration-only and must not appear in buttons, badges, or status indicators
- Do not use pure white #ffffff for card surfaces when Soft Meadow #eff2e5 is the designated card layer
- Do not place two primary yellow CTAs in the same viewport; alternate with the dark pill for hierarchy
- Do not use Inter for display headlines or Hedvig Letters Serif for UI labels — the font-role boundary is strict
- Do not add drop shadows to cards or buttons; surface differentiation comes from the green-tinted #eff2e5 layer, not elevation
- Do not use the nav Slate #5f5c6 for primary body text — it is reserved for muted copy and helper text only

## Components

### Primary CTA Button (Filled Yellow)

Background #ffe228, text #130e30 in Inter 500 at 16px. Full pill radius 1440px. Padding 12px 24px. No shadow. Black text on yellow achieves 16.2:1 contrast. The yellow is so bright it functions as a highlighter; one per viewport maximum.

### Secondary Button (Dark Pill)

Background #130e30, text #ffffff in Inter 500 at 16px. Full pill radius 1440px. Padding 12px 22px. Creates a dark/light button pair with the yellow primary for visual hierarchy.

### Email Input Field

White background #ffffff, border 1px solid #000000, text #130e30 in Inter 400 at 16px. Placeholder text in Slate #5f5c6e. Pill radius 1440px — the input and its adjacent button share the same radius creating a continuous capsule. Padding 12px 22px.

### Logo Lockup

Mark + wordmark 'ditto' in #130e30. The mark uses a leaf/petal shape echoing the organic decorative blobs. Always paired with a nav layout, never standalone.

### Nav Bar

Background #eff2e5, horizontal layout with logo left, nav links center (Inter 500 16px in #130e30), CTA pair right. Nav items separated by chevron-down indicators for dropdowns. Globe icon for language. No shadow, sits flush on canvas.

### Hero Card / Product Mockup Container

White product card sits on top of organic colored shapes (green, pink, yellow, violet). The card has subtle border-radius 24px. Behind it, SVG-style organic blobs in #59e25d, #e261e5, #ffe228, and #130e30 create a garden-like atmosphere without illustration.

### Feature Card

Background #eff2e5, padding 24-48px, border-radius 24px. Contains a small logo mark at top, a Hedvig Letters Serif heading at 22-32px in #130e30, and body text in Inter 16px #5f5c6e. No shadow or border — the surface contrast alone defines the card.

### Customer Logo Card

Logo centered on #eff2e5 surface, padding 24px, radius 24px. Below each logo, a small-caps 'CASE STUDY' link in Inter 500 10px with chevron. Logos displayed in monochrome #130e30.

### Testimonial Card

Background #eff2e5, padding 32px, radius 24px. Large quote text in Hedvig Letters Serif 22-32px or Inter 18px in #130e30. Avatar + name (Inter 500 14px #130e30) + title (Inter 400 12px #5f5c6e) at bottom. Horizontal carousel with arrow controls.

### Pagination Dot

Inactive: small line/rectangle in #5f5c6e. Active: Hi-Yellow #ffe228 pill. Centered below the carousel.

### Small Caps Label

Inter 500 at 10-12px, letter-spacing -0.02em, color #5f5c6 or #130e30. All uppercase. Used sparingly as taxonomic labels rather than decoration.

### Hero Headline

Hedvig Letters Serif weight 700 at 48-64px, line-height 1.0-1.1, letter-spacing -0.01em, color #130e30. Fills the left column of a two-column hero with the product mockup on the right.

## Similar Design Systems

- {'why': 'Same warm cream canvas, organic decorative blob shapes behind product UI, serif headline + sans body pairing, and pill-shaped yellow/dark CTA pair', 'business': 'Sweep (sweep.net)'}
- {'why': 'Sustainability/compliance domain with light surfaces, soft organic accents, and a single bright highlight color for CTAs', 'business': 'Watershed (watershed.com)'}
- {'why': 'CSR-adjacent SaaS with cream backgrounds, serif display type, pill buttons, and nature-inspired decorative elements', 'business': 'Klim (klim.co)'}
- {'why': 'Light off-white canvas, Inter for body type, pill-shaped buttons, and minimal card elevation — shares the approachable, not-corporate base layer', 'business': 'Notion'}

## Agent Prompt Guide

**Quick Color Reference**
- text (primary): #130e30
- text (muted): #5f5c6e
- background (page): #f9fbf2
- background (card): #eff2e5
- border: #130e30
- accent (decorative blobs only): #ffe228, #59e25d, #e261e5
- primary action: #ffe228 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #ffe228 background, #222222 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Feature Grid Card**: Background #eff2e5, 24px border-radius, 32px padding. Small partner logo (40px) at top-left. Heading in Hedvig Letters Serif 700 22px #130e30, line-height 1.25. Body in Inter 400 16px #5f5c6e.

3. **Top Navigation Bar**: Background #eff2e5, horizontal flex with logo left, nav links center (Inter 500 16px #130e30 with chevron-down icons), right side has dark pill button #130e30 bg / white text 'Log In' and yellow filled button #ffe228 / #130e30 text 'Get Started', both pill radius 1440px, 12px 22px padding.

4. **Testimonial Carousel Card**: Background #eff2e5, 24px radius, 32px padding. Quote in Inter 400 18px #130e30, line-height 1.5. Author block at bottom: 40px circular avatar + name in Inter 500 14px #130e30 + title in Inter 400 12px #5f5c6e.

5. **Customer Logo Trust Strip**: Full-width Soft Meadow #eff2e5 band, 48px vertical padding. Horizontal row of 8 monochrome client logos in #130e30, each above a small-caps 'CASE STUDY' link in Inter 500 10px #5f5c6e with right chevron.

## Decoration vs Interface Color Boundary

The colors #59e25d (moss green) and #e261e5 (fuchsia) exist exclusively in the organic blob shapes behind the hero product card. They must never appear in buttons, badges, tags, icons, or any functional UI element. The single exception is #ffe228 yellow, which functions as both a decorative blob color AND the primary CTA fill — it is the bridge between decoration and interface. This dual role is deliberate: the yellow appears in the atmosphere before the user interacts, then becomes the action color they click.

## Surface Temperature

The off-white tones are not neutral white — #f9fbf2 has a faint warm-green cast and #eff2e5 is a clearly green-tinted meadow surface. This warm canvas is core to the brand's organic, garden-influenced feel. Do not substitute pure #ffffff or neutral grays. The two surface tones create enough separation for cards without needing borders or shadows.
