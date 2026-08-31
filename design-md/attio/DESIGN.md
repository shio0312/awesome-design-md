# Attio — Design System

> **North Star**: Architectural editorial on white marble
> **Theme**: light
> **Source**: https://attio.com
> **Refero Style**: https://styles.refero.design/style/08c8700c-f278-42bc-812e-f60dc6ce996e
> **Synced**: 2026-09-01

## Overview

Attio uses an editorial SaaS language: near-white canvas, near-black type, and one vivid cobalt accent (#266df0) that does the talking while everything else stays quiet. The type stack is a deliberate three-voice system — Inter for UI, InterDisplay for marketing headlines at weight 600 with tight tracking, and TiemposText (serif) for testimonial/pull-quote moments that need warmth and human weight. Components feel light and precise: 7px and 12px radii, hairline borders, blue-tinted shadows at very low opacity, and ghost/outline buttons that defer to the primary filled dark action. Layout breathes — generous vertical rhythm with a 1440px max-width — but density is compact within cards and lists. The signature move is restraint: the same monochrome restraint you'd see in a financial publication, punctuated by exactly one chromatic moment per screen.

## Color Palette

- **Page Canvas**: `#ffffff` — Primary page background, card surfaces, button backgrounds [neutral]
- **Ink Black**: `#1c1d1f` — Primary heading and body text, logo mark [neutral]
- **Graphite**: `#232529` — Dark surface text, dark filled button background [neutral]
- **Obsidian**: `#101113` — Deepest text and dark surface fills [neutral]
- **Carbon**: `#2e3238` — Secondary dark text, nav states, button text on light fills [neutral]
- **Slate 500**: `#505967` — Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color [neutral]
- **Slate 600**: `#6f7988` — Muted body text, secondary descriptions [neutral]
- **Slate 700**: `#8f99a8` — Tertiary headings, captions, low-emphasis text [neutral]
- **Fog 400**: `#9fa1a7` — Placeholder text, disabled states, subtle icons [neutral]
- **Mist 300**: `#b5bdc9` — Muted body text, secondary copy [neutral]
- **Cloud 200**: `#cad0d9` — Hairline borders on cards, input borders, dividers [neutral]
- **Cloud 100**: `#d3d8df` — Card borders, surface boundaries [neutral]
- **Mist 50**: `#e4e7ec` — Primary border color, dividers, subtle backgrounds, button borders [neutral]
- **Haze**: `#eeeff1` — Subtle background fills, section bands, inset borders [neutral]
- **Paper**: `#f4f5f6` — Alternate surface background, subtle elevated panels [neutral]
- **Cobalt Core**: `#266df0` — Primary brand accent — link text, focus rings, active states, highlighted icons, gradient midtone [brand]
- **Cobalt Bright**: `#407ff2` — Secondary accent, hover states, decorative strokes in illustrations [brand]
- **Cobalt Soft**: `#538bf3` — Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. [brand]
- **Periwinkle**: `#bad0fa` — Decorative card borders, subtle blue-tinted surface outlines [accent]
- **Ice Wash**: `#e4edff` — Soft blue-tinted background, highlight washes, button box-shadow tints [accent]
- **Onyx Footer**: `#000000` — Footer background, dark section backgrounds, high-contrast text on light [neutral]

## Typography

- **Inter**
- **InterDisplay**
- **TiemposText**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.42 |
| body-lg | 16 | — | 1.38 |
| subheading | 20 | — | 1.3 |
| heading-sm | 32 | — | 1.19 |
| heading | 40 | — | 1.1 |
| heading-lg | 56 | — | 1.07 |
| display | 64 | — | 1 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 80-120px
- **Border Radius**: {'tabs': '10px', 'cards': '11-14px', 'badges': '7px', 'inputs': '10px', 'buttons': '10px'}

## Layout

Max-width 1440px centered, with a prominent top promo banner (48px) + nav header (68px) → fixed total header of ~116px. Hero pattern: centered headline + subtext + two-button row, with a product screenshot card below — no split-image, no full-bleed hero. Section rhythm: white → white with subtle Paper-tone bands, alternating full-bleed white and off-white. Content arrangement is predominantly centered stacks and symmetrical 2-column grids; asymmetric layouts are rare. Feature sections use 3-column card grids and side-by-side text+product-screenshot rows. Footer is full-bleed black with a 4-column link grid. Overall density is spacious — 80-120px between major sections, compact 8-12px gaps within cards and lists.

## Surfaces / Elevation

- **Page Canvas**
- **Paper**
- **Card Surface**
- **Dark Surface**

**Shadow tokens:**

## Imagery

Product screenshots are the primary visual — real interface captures rendered as cards with subtle blue-tinted shadows, zero internal padding (the screenshot fills the card). One hero section uses a grid of small user avatar tiles arranged in a wave/contour pattern as decorative atmosphere. Customer logos appear in a monochrome strip (all rendered in near-black) — no photography, no lifestyle imagery. Iconography is 16-20px line icons, 1.5px stroke weight, monochrome, consistent across nav and UI. The overall visual density is low — white space dominates, and imagery is either product UI or abstract decorative elements, never stock photography.

## Design Principles

### Do

- Use #266df0 (Cobalt Core) as the single accent for all interactive highlights, active states, and link text — never introduce additional saturated colors
- Set display headlines in InterDisplay weight 600 at 40-64px with tracking -0.015em to -0.02em and line-height 1.0-1.1
- Use 10px border-radius for all buttons and inputs, 7px for tags and badges, 11-14px for cards
- Apply blue-tinted shadows at very low opacity (rgba(28, 40, 64, 0.04) to rgba(28, 40, 64, 0.1)) — never use warm-gray or pure-black shadows
- Use Inter weight 500 as the default UI weight, not 400 — the slightly heavier weight is the system's default voice
- Activate 'ss03' on all Inter and InterDisplay text for the alternate geometric character
- Keep the max-width at 1440px and maintain 80-120px vertical gaps between major sections

### Don't

- Don't use rounded buttons with radius above 12px — the 10px radius is part of the system identity
- Don't introduce secondary accent colors, gradients on buttons, or decorative color — one blue accent is the rule
- Don't use TiemposText for anything other than testimonial pull-quote headings — the serif/sans contrast is earned by rarity
- Don't use Inter weight 400 as a default — weight 500 carries the UI voice
- Don't apply shadows warmer than rgba(28, 40, 64, ...) — the blue-tinted shadow is deliberate, not neutral
- Don't use letter-spacing wider than 0 for body or heading text — the system is consistently tight-tracked
- Don't place the cobalt accent on filled backgrounds in body copy — it belongs to links, icons, and small interactive moments

## Components

### Primary Filled Button

Dark filled button, background #232529 (Graphite) or near-black, text #ffffff (white), 10px border-radius, 12px horizontal padding, height ~40px. Inter weight 500, 15px. No border. Signature element: the only colored-fill button in the system. Examples: 'Start for free'.

### Secondary Outline Button

White background (#ffffff), 1px border #e4e7ec (Mist 50), text #1c1d1f (Ink Black), 10px radius, 12px horizontal padding. Inter weight 500, 15px. Ghost-like restraint — sits beside the dark primary without competing. Examples: 'Talk to sales'.

### Ghost Text Button

Transparent background, no border, text in #1c1d1f or #2e3238, 10px radius, 0px padding. Inter weight 500, 15px. Used in nav and inline contexts where the action is implied, not proclaimed. Examples: nav items, 'Sign in'.

### Dark Inverted Button

Background #1c1d1f (Ink Black), text #ffffff, 1px border #2e3238, 10px radius. Same dimensions as primary but inverted for use on dark bands or footers.

### Tab Bar

Horizontal tab strip with bottom-border active indicator. Text Inter 15px weight 500, inactive in #6f7988 (Slate 600), active in #1c1d1f (Ink Black) with a 2px bottom border in Ink Black. No background fill. Examples: 'Ask Attio / Data model / Workflows / Reporting'.

### Product Screenshot Card

White background (#ffffff), 11-14px border-radius, subtle blue-tinted shadow (rgba(28, 40, 64, 0.04) 0px 12px 30px 0px or rgba(28, 40, 64, 0.08) 0px 6px 20px -2px). Zero or very minimal internal padding — the screenshot IS the card. No border.

### Feature Card

White background, 12px border-radius, 1px border #e4e7ec or subtle shadow stack (rgba(28, 40, 64, 0.1) 0px 2px 3px -2px + rgba(28, 40, 64, 0.04) 0px 4px 6px -2px), 11-24px internal padding. Heading 20-32px InterDisplay 600, body 15-16px Inter 500 in #6f7988.

### Logo Strip

Inline row of monochrome customer logos on white background, all rendered in #1c1d1f or #2e3238. No card wrapping, no dividers. Generous vertical padding (60-80px) above and below. Example: granola, Flow, Listen, Obvious, Modal, USV logos.

### Eyebrow Pill / Tag

Small pill or bordered label above section headings. Transparent or very light background, 1px border #e4e7ec, 7px radius, 6-8px vertical padding, 10-12px horizontal. Inter weight 500, 12px. Used as a quiet signifier. Example: 'Explore GTM frameworks from operators like Elena Verna'.

### New Badge

Small filled badge, background #538bf3 (Cobalt Soft), text #ffffff or dark, 7px radius, ~5px vertical / 8px horizontal padding. Inter weight 500, 11-12px. The only chromatic badge in the system — its rarity makes it meaningful.

### Promo Banner

Thin dark bar at top of page (48px height), background #000000 or #101113, text #ffffff, Inter 14px weight 500, centered content with an arrow link in white. Dismissable. Example: 'Orchestrate revenue agents with the new Workflows →'.

### Chat Input Field

White background, 1px border #e4e7ec, 10-12px radius, subtle shadow, generous internal padding (12-16px). Placeholder text in #9fa1a7 (Fog 400). Send button: small cobalt blue square, #266df0 background, 7px radius.

### Sidebar Navigation

Light background (#ffffff or #f4f5f6), no visible border separating from main content. Items: Inter 14-15px weight 500, text #1c1d1f, hover/active state in #2e3238. Indentation uses 16-24px left padding. Icons: 16px, 1.5px stroke, monochrome.

### Footer

Black background (#000000), text #ffffff and #b5bdc9 (muted), Inter 14-15px weight 500. Column-based layout (4 columns: Platform, Import from, Apps, Resources). Logo + wordmark in white at top-left. Generous vertical padding (80-120px).

## Similar Design Systems

- {'why': "Same monochrome restraint with a single vivid accent (Linear's purple), Inter-based type stack, hairline borders, and near-white canvas with tight 10px button radii", 'business': 'Linear'}
- {'why': "Editorial SaaS language with a custom display sans for headlines, generous white space, and the same 'one accent color doing all the work' philosophy", 'business': 'Stripe'}
- {'why': 'Black-and-white interface with a single bright accent, Inter at weight 500 for UI, and the same compact card padding with subtle shadows', 'business': 'Vercel'}
- {'why': 'Near-white canvas with a serif/sans contrast in headings, compact component density, and the same editorial approach to product marketing pages', 'business': 'Notion'}
- {'why': "Bold display headlines, single cobalt-blue accent, dark footer inversion, and the same 'architectural editorial' treatment of product UI cards", 'business': 'Framer'}

## Agent Prompt Guide

Quick Color Reference:
- text primary: #1c1d1f (Ink Black)
- text muted: #6f7988 (Slate 600)
- background: #ffffff (Page Canvas)
- border: #e4e7ec (Mist 50)
- accent: #266df0 (Cobalt Core)
- primary action: #232529 (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #232529 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a product screenshot card: white background, 14px border-radius, shadow rgba(0,0,0,0.04) 0px 12px 30px 0px, zero internal padding, product UI image fills the card edge-to-edge.

3. Create a section with eyebrow pill + heading + body: Eyebrow pill (7px radius, 1px border #e4e7ec, Inter 12px weight 500, #6f7988 text, 8px 12px padding). Heading at 40px InterDisplay 600, #1c1d1f, tracking -0.4px. Body at 16px Inter weight 500, #6f7988, line-height 1.38.

4. Create a chat input field: white background, 1px border #e4e7ec, 12px radius, shadow rgba(28,40,64,0.06) 0px 2px 6px 0px. Placeholder in #9fa1a7 (Fog 400) Inter 15px weight 500. Send button: 28px square, #266df0 background, 7px radius, white arrow icon.

5. Create a footer: full-bleed #000000 background, 4-column grid with column titles (Inter 15px weight 500, #b5bdc9) and links below (Inter 14px weight 500, #ffffff). Logo + wordmark in white at top-left, 80-120px vertical padding.
