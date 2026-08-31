# Gleap — Design System

> **North Star**: warm cream-paper workspace with graphite accents — a studio where matte-black ink dots float over linen architecture.
> **Theme**: light
> **Source**: https://gleap.io
> **Refero Style**: https://styles.refero.design/style/2eab438d-32cd-40c2-b160-1e4127dac569
> **Synced**: 2026-09-01

## Overview

Gleap operates in a warm-paper product language: a slightly cream canvas carries flat, low-elevation surfaces in sage-tinted stone, with almost no chromatic presence — one vivid green dot punctuates an otherwise fully achromatic system. The whole product reads as architectural: weight 400 headlines, tight -0.01em tracking, and pill-shaped controls feel drawn rather than printed. Color is rationed to functional punctuation (status dots, active nav dots, gradient-free product screenshots) while the primary CTA is a matte black capsule, not a brand-colored button. Surfaces stack from canvas → white card → sage tile → glass overlay without ever using shadows as decoration; depth is communicated through color temperature shifts from cool gray to warm stone.

## Color Palette

- **Linen Canvas**: `#edede8` — Page background, section surfaces — warm off-white that pushes the whole system toward paper rather than screen [neutral]
- **Frosted White**: `#ffffff` — Card surfaces, elevated panels, glass overlays — clean white floats above the linen canvas for primary content [neutral]
- **Warm Stone**: `#dbdbd2` — Secondary card fills, secondary button backgrounds, accent surface — sage-tinted beige gives neutral elements warmth without becoming chromatic [neutral]
- **Pebble**: `#c0c0c0` — Circular accent tiles, muted card backgrounds — cool gray that sits one step back from stone for de-emphasized surfaces [neutral]
- **Graphite Ink**: `#141414` — Primary action button background, dark text on light surfaces — near-black with a hair of warmth, anchors every CTA [neutral]
- **Charcoal Body**: `#292929` — Primary body and heading text — readable but softer than pure black, keeps long-form copy from feeling harsh [neutral]
- **Slate Caption**: `#6f6f6e` — Secondary body, helper text, descriptive copy — carries the most volume of any text color [neutral]
- **Ash Subheading**: `#8f8f8e` — Subtle labels, muted headings, decorative type — sits between caption and hairline [neutral]
- **Iron Nav**: `#353535` — Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color [neutral]
- **Onyx Border**: `#000000` — Hairline borders, strong dividers, selected-state outlines — used at 1-2px to outline cards, buttons, and focus rings [neutral]
- **Quartz**: `#d0d0c8` — Quietest surface tint, reserved for low-contrast dividers and hover-state hints [neutral]
- **Lime Pulse**: `#4cc02b` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]

## Typography

- **Switzer**
- **system-ui**
- **sans-serif**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| small | 12 | — | 1.77 |
| caption | 14 | — | 1.5 |
| body-sm | 16 | — | 1.5 |
| body | 19 | — | 1.4 |
| body-lg | 23 | — | 1.35 |
| subheading | 27 | — | 1.3 |
| heading-sm | 32 | — | 1.3 |
| heading | 45 | — | 1.2 |
| heading-lg | 64 | — | 0.8 |
| display | 80 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 18px
- **Element Gap**: 9px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '12px', 'pills': '200px', 'avatars': '9999px', 'buttons': '200px', 'innerTiles': '6px', 'smallElements': '3.75px'}

## Layout

Max-width 1200px centered container with generous outer padding. Hero is a centered text stack (display headline, sub-headline, description, trust bar, dual CTA) followed by a full-width product screenshot with gradient backdrop. Sections alternate between linen canvas and white card surfaces separated by 80px gaps. Feature blocks use a 2-column text-plus-screenshot layout that alternates sides. Pricing is a 4-column card grid with equal widths. The footer is a multi-column link directory (4 nav blocks) over a slightly darker section tone. Navigation is a single transparent top bar with logo left and pill CTA right.

## Surfaces / Elevation

- **Linen Canvas**
- **Frosted White**
- **Warm Stone**
- **Glass Overlay**
- **Graphite**

**Shadow tokens:**

## Imagery

Product screenshots dominate over photography — the hero features a full app interface rendered against a soft gradient backdrop of lavender, teal, and peach (decorative, not part of the design system palette). Secondary imagery is tight UI crops with no lifestyle context. No stock photography, no illustrations, no 3D renders. Icons are monoline outlined at consistent stroke weight, sitting flat on circular pebble (#c0c0c0) tiles. The visual narrative is entirely product-led: the interface IS the hero.

## Design Principles

### Do

- Use 200px border-radius on every button and pill — the capsule shape is non-negotiable for brand recognition
- Set primary CTAs to #141414 fill with white text; use the stone (#dbdbd2) capsule as the default for any non-purchase action
- Keep headlines at weight 400 Switzer with -0.01em tracking at 64px and below, -0.02em at 80px display — never bold a headline above body weight
- Use the linen canvas (#edede8) as the base; place white (#ffffff) cards on top for contrast, and step down to stone (#dbdbd2) for de-emphasized content
- Apply backdrop-filter blur(12px) to any panel that floats over imagery or gradient backgrounds
- Use #4cc02b Lime Pulse only as a status dot or checkmark — never as a button fill, page accent, or decorative color
- Pair the 6px base unit for inline gaps with 18px card padding and 80px section gaps to maintain the comfortable density

### Don't

- Don't introduce a brand-colored CTA — the system is intentionally chromatic-free; colored buttons would break the architectural language
- Don't use bold (600+) on headlines — weight 400 at display sizes is the signature; heavier weights belong in buttons and badges only
- Don't stack more than three surface tones in one screen (canvas → white → stone); the palette is rationed to preserve warmth
- Don't use drop shadows as decoration — if depth is needed, shift surface tone from white to stone to graphite instead
- Don't apply sharp corners to feature cards or panels — 12px is the floor for content surfaces; only consent dialogs may use 3.75px
- Don't add gradients to UI elements — the gradient zone is reserved for the hero product screenshot backdrop only
- Don't use letter-spacing wider than -0.01em on body copy; positive tracking breaks the tight architectural feel

## Components

### Pill Button — Dark (Primary)

Matte black capsule. Background #141414, text #ffffff, border-radius 200px, padding 0 18px, height matches line-height at 16px text (≈44px). Weight 400 in Switzer at 16px. Letter-spacing inherits body tracking.

### Pill Button — Stone (Secondary)

Warm sage capsule. Background #dbdbd2, text #292929, optional 1-2px #292929 border, border-radius 200px, padding 0 24px, height ≈44px. Same Switzer 16px/400 as primary. This is the workhorse — pricing cards, demo buttons, and feature CTAs use this instead of the dark fill.

### Pill Button — Ghost (Tertiary)

Transparent fill, 1px #353535 border, text #353535, border-radius 200px, padding 9px 12px. Smaller padding profile marks it as a lightweight control, not a section-level CTA.

### Square White Button

The system outlier. Background #ffffff, text #000000, border-radius 3.75px (sharp — breaks the pill language intentionally for cookie/consent contexts), padding 15px square. Use only when the pill vocabulary is wrong for the context.

### Feature Card — Warm Stone

Background #dbdbd2, border-radius 12px, padding 18px, no shadow. Used for secondary feature blocks that should recede behind the main white content card.

### Feature Card — White

Background #ffffff, border-radius 12px, padding 18px, optional 1px solid #0000001f border. The default elevated surface. No shadow by default; depth comes from the warmer canvas behind it.

### Glass Overlay Panel

Background rgba(255, 255, 255, 0.7), border-radius 6px, padding 18px, backdrop-filter blur(12px). Used for the floating support widget and any UI that needs to float over imagery while staying legible.

### Circular Accent Tile

Background #c0c0c0, border-radius 50%, no padding (icon centered inside). Functions as a quiet visual marker — never the primary CTA, always a supporting element.

### Navigation Bar

Transparent background over linen canvas. Logo + product nav + auth links + dark pill CTA right-aligned. Height ≈60px. Nav text in #353535 at 14-16px Switzer 400.

### Pricing Card

Background #dbdbd2 with 12px radius and 18px padding. Tier name and price at 32px/27px Switzer 400. Checklist uses Lime Pulse (#4cc02b) checkmarks at 14-16px. Featured tier gains a subtle gradient highlight strip across the top edge.

### Trust Bar

Horizontal row of grayscale customer logos with one-line caption at left. Logos desaturated to monochrome at 60-80% opacity. 9-12px vertical gap between logo and caption.

### Status Dot

8px circle filled with #4cc02b (Lime Pulse). The single chromatic element in the system — appears next to live chat, active features, and system status. Use sparingly.

## Similar Design Systems

- {'why': 'Same weight-400-at-display-sizes typography discipline and matte black pill-button vocabulary; both reject colored CTAs in favor of monochrome depth', 'business': 'Linear'}
- {'why': 'Similar warm off-white canvas with tight tracking and pill-shaped controls; both treat color as rationed punctuation rather than decoration', 'business': 'Vercel'}
- {'why': 'Shared architectural flatness — warm neutral surfaces, minimal shadows, product-screenshot-as-hero imagery, and weight 400 headlines that whisper', 'business': 'Resend'}
- {'why': 'Same dual-pill CTA pairing (dark primary + light secondary) and warm-paper product aesthetic with desaturated supporting imagery', 'business': 'Frame.io'}
- {'why': 'Identical approach to typography tracking (-0.01em at large sizes) and the same rationed chromatic palette with one accent green for status', 'business': 'Stripe (documentation)'}

## Agent Prompt Guide

**Quick Color Reference**
- Text primary: #292929
- Text secondary: #6f6f6e
- Background (canvas): #edede8
- Surface (card): #ffffff
- Border (hairline): #0000001f
- Accent (status only): #4cc02b
- primary action: #141414 (filled action)

**Example Component Prompts**

1. *Create a hero section*: Linen canvas (#edede8) background, centered max-width 1200px. Display headline at 80px Switzer weight 500, color #292929, letter-spacing -1.6px. Sub-headline at 45px weight 400, color #292929. Body description at 19px weight 400, color #6f6f6e, line-height 1.4. Two CTAs centered: dark pill (#141414 fill, white text, 200px radius, 0 18px padding, 16px Switzer 400) followed by stone pill (#dbdbd2 fill, #292929 text, 200px radius, 0 24px padding).

2. Create a Primary Action Button: #141414 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. *Create a feature card*: White surface (#ffffff), 12px radius, 18px padding, no shadow. Optional 1px #0000001f border. Heading at 27px Switzer 400 in #292929. Body text at 16px Switzer 400 in #6f6f6e, line-height 1.5. Optional circular accent tile (background #c0c0c0, 50% radius, 40px diameter) at top of card containing an outlined icon in #353535.

4. *Create a floating chat widget*: Glass panel (rgba(255,255,255,0.7) with backdrop-filter blur(12px)), 6px radius, 18px padding, shadow rgba(0,0,0,0.3) 0 32px 68px 0. Header text at 16px Switzer 400 in #292929. Status indicator: 8px Lime Pulse (#4cc02b) circle to the left of any 'online' label. Position fixed bottom-right.

5. *Create a navigation bar*: Transparent background over linen canvas, height 60px, max-width 1200px centered. Logo at left in #292929 at 16px Switzer 500. Center nav links at 14px Switzer 400 in #353535 with 24px horizontal gap. Right cluster: Login link in #353535 + dark pill CTA (#141414 fill, white text, 200px radius, 0 18px padding).

## Gradient Zone

The only gradient usage in the system is the hero product screenshot backdrop — a soft sweep of lavender, peach, and teal that sits behind the app screenshot. This is decorative screenshot context, not a UI surface. No gradients are applied to buttons, cards, or text. Treat gradients as off-limits for component design; reserve them for full-bleed image backgrounds only.

## Color Rationing

Gleap's chromatic budget is exactly one color: #4cc02b Lime Pulse. This discipline is the brand. Adding a secondary brand color, accent palette, or status spectrum would dilute the architectural feel. Even success/warning/error states default to monochrome (icon + label) rather than chromatic swatches. If a state requires visual emphasis, use surface tone (white → stone → graphite) before reaching for hue.
