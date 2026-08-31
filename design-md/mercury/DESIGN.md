# Mercury — Design System

> **North Star**: Alpine banking at blue hour
> **Theme**: dark
> **Source**: https://mercury.com
> **Refero Style**: https://styles.refero.design/style/3172cd4d-118a-4a16-a259-6b634d32322e
> **Synced**: 2026-09-01

## Overview

Mercury operates in an alpine banking aesthetic: a near-black canvas (#171721) sets a cinematic, observatory-like atmosphere where content surfaces float as subtly lighter graphite cards. The interface is overwhelmingly monochromatic — ivory text on onyx, with a single vivid cobalt (#5266eb) acting as the only chromatic punctuation, reserved exclusively for the primary 'Open account' action. Typography carries the weight of expression: a custom display face at intermediate weight 480 (neither bold nor light) paired with a refined body face at weight 400, creating a voice that is confident but never loud. Components are flat and borderless, relying on the 12px-radius graphite card lift and pill-shaped controls to define structure rather than shadows. The full-bleed photographic hero — misty mountains with a solitary desk — establishes aspiration before the product UI takes over, and every subsequent surface maintains that hushed, premium darkness.

## Color Palette

- **Onyx Canvas**: `#171721` — Dominant page background, hero overlay base, footer and section canvases [neutral]
- **Graphite Card**: `#1e1e2a` — Elevated card and section surfaces — one step lighter than the canvas to create quiet separation [neutral]
- **Obsidian Button**: `#272735` — Secondary button fills, inline form backgrounds, subtle interactive surfaces [neutral]
- **Slate Border**: `#70707d` — Medium-weight dividers and structural borders between content blocks [neutral]
- **Mist Border**: `#e2e3ed` — Light hairline borders, ghost-button outlines, input edges — light-on-dark border [neutral]
- **Ash Text**: `#c3c3cc` — Muted body copy, helper text, secondary labels — reduced hierarchy without losing legibility [neutral]
- **Ivory Text**: `#ededf3` — Primary text, icons, nav items, ghost-button strokes and text — the dominant foreground color across the system [neutral]
- **Cobalt**: `#5266eb` — Violet action color for filled buttons, selected navigation states, and focused conversion moments. [brand]
- **Pure White**: `#ffffff` — Text and icon fills on cobalt primary buttons for maximum contrast [neutral]

## Typography

- **arcadia**
- **arcadiaDisplay**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1 |
| body-sm | 14 | — | 1 |
| body | 16 | — | 1.5 |
| body-lg | 18 | — | 1.35 |
| subheading | 21 | — | 1.35 |
| heading-sm | 28 | — | 1.2 |
| heading | 32 | — | 1.15 |
| heading-lg | 42 | — | 1.15 |
| display | 65 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 12px
- **Section Gap**: 72px
- **Border Radius**: {'nav': '40px', 'tags': '40px', 'cards': '12px', 'inputs': '32px', 'buttons': '32px', 'default': '4px'}

## Layout

Full-bleed dark canvas throughout. Hero is 100vw full-bleed photographic with centered headline + subtext + email-capture form stack (max-width ~640px). Below hero, content flows in 1200px max-width sections with 72px vertical padding, alternating between text-left/image-right 2-column splits and 3-column card grids for product features. Navigation is a transparent top bar overlaid on the hero, transitioning to a frosted-glass (backdrop-blur) solid dark fill on scroll. Footer is dark with disclaimer text. Vertical rhythm is generous — spacious density with large breathing room between sections. No sidebar navigation; all navigation lives in the top bar.

## Surfaces / Elevation

- **Onyx Canvas**
- **Graphite Card**
- **Obsidian Button**

## Imagery

Cinematic full-bleed photography dominates the hero — atmospheric, aspirational landscapes (misty mountains, isolated desks in nature) that position banking as a contemplative, elevated experience. Photography is high-quality, slightly desaturated with cool tones, and treated with a subtle dark overlay to maintain text legibility. Below the hero, imagery shifts to product UI screenshots and abstract atmospheric backgrounds. No illustrations, no icons-as-art — visuals are photographic or purely functional. Icon style throughout the UI is minimal line/glyph style in Ivory, appearing in nav, buttons, and form elements.

## Design Principles

### Do

- Use Cobalt #5266eb exclusively for the single primary action per page — never as a decorative accent, icon fill, or secondary button
- Set all cards to #1e1e2a with 12px radius and 32px padding — rely on the one-step value lift from the canvas, not shadows, for separation
- Apply arcadiaDisplay weight 480 (not 600/700) for all headings — the intermediate weight is Mercury's signature restraint
- Use 32px or 40px pill radius for all interactive controls (buttons, inputs, nav items) — sharp 4px corners are reserved for structural elements only
- Set body text at 16px arcadia weight 400 with 1.5 line-height — this is the density baseline for all content
- Maintain 72px vertical rhythm between major sections — spacious density is part of the premium feel
- Use ivory #ededf3 on ghost/outline buttons for both border and text — never use a chromatic color for secondary actions

### Don't

- Do not use multiple bright accent colors — Cobalt is the only chromatic note; introducing greens, reds, or oranges breaks the monochrome discipline
- Do not add drop shadows to cards or components — separation comes from the graphite-on-onyx value difference alone
- Do not use bold weights (700+) for headings — arcadiaDisplay at 480 is the ceiling
- Do not use sharp corners (0–4px) on buttons, inputs, or nav items — the pill shape is non-negotiable
- Do not use #ffffff for body text — always #ededf3 Ivory; pure white on dark creates harsh, cold contrast
- Do not place Cobalt-filled elements next to each other without at least 32px gap — the vivid color creates visual competition when clustered
- Do not use bright or saturated backgrounds for sections — every surface is either #171721 (canvas) or #1e1e2a (card); no mid-gray or colored bands

## Components

### Primary CTA Button (Cobalt)

Filled with #5266eb Cobalt, white text at 16px arcadia weight 400, 32px border-radius (pill), 0px vertical padding with 20px horizontal padding for inline contexts, 40px vertical padding when standalone. No border, no shadow. The vivid blue against the dark canvas makes this button the gravitational center of any page.

### Ghost Outline Button

Transparent background, 1px solid #ededf3 Ivory border, Ivory text at 16px arcadia weight 400, 40px border-radius (pill). Zero padding top/bottom with 20px horizontal padding. Used for navigation links and secondary CTAs where a filled button would overpower the layout.

### Navigation Pill Link

Transparent background, no border, Ivory text at 16px arcadia weight 400, 40px border-radius, 0px vertical / 20px horizontal padding. Floats over the hero image and transitions to a solid dark fill on scroll via backdrop-blur.

### Graphite Card

Background #1e1e2a, 12px border-radius, 32px padding on all sides, no shadow, no border. The one-step lift from the #171721 canvas creates separation through subtle value contrast rather than elevation. Cards sit flat on the dark plane.

### Email Capture Input (Pill, Left-Half)

Transparent background, 1px solid #ededf3 Ivory border on left side only, Ivory text at 16px arcadia weight 400, border-radius 32px 0px 0px 32px (left-side pill, flat right edge where it meets the button), 20px left padding. Placeholder text in #c3c3cc Ash.

### Full-Bleed Hero Section

100vw × ~100vh, no padding constraints, centered content stack. Headline in arcadiaDisplay at 65px weight 480, subtext in arcadia at 18px weight 480. A full-bleed photographic background (atmospheric landscape) sits behind a subtle dark overlay. Content max-width ~640px centered vertically and horizontally.

### Transparent Top Navigation Bar

Full-width, fixed or sticky, transparent background over the hero image. Brand mark (Mercury logo with concentric-circle icon) on the left, nav links centered (Products, Solutions, Resources, About, Pricing), Log in text link and Cobalt 'Open account' pill button on the right. Uses backdrop-blur(8px or 20px) on scroll to create frosted-glass separation.

### Disclaimer Banner

Dark background (matches canvas or slightly lighter), small text at 12px arcadia weight 480 with 0.01em letter-spacing, centered or left-aligned, subtle Ivory or Ash text color. Minimal visual weight — present but never distracting.

### Section Container

Full-width dark canvas (#171721) with inner content constrained to 1200px max-width, 72px vertical padding. Contains 2- or 3-column grids of Graphite Cards or text+image splits.

## Similar Design Systems

- {'why': 'Same dark-canvas + single-accent-color approach to fintech, with pill-shaped controls and flat card surfaces', 'business': 'Wise'}
- {'why': 'Similar graphite-on-dark card system with minimalist borderless components and a restrained primary accent', 'business': 'Ramp'}
- {'why': 'Dark-mode fintech aesthetic with comparable flat card elevation and confident intermediate-weight typography', 'business': 'Brex'}
- {'why': 'Same whisper-weight typography philosophy and dark monochrome canvas with a single chromatic action color', 'business': 'Linear'}
- {'why': 'Shared approach to generous spacing, intermediate-weight display type, and letting one accent color carry the brand', 'business': 'Stripe'}

## Agent Prompt Guide

**Quick Color Reference**
- Background (canvas): #171721 Onyx
- Card surface: #1e1e2a Graphite
- Primary text: #ededf3 Ivory
- Muted text: #c3c3cc Ash
- Border: #e2e3ed Mist
- primary action: #5266eb (filled action)

**Example Component Prompts**

1. Create a product feature card: background #1e1e2a Graphite, 12px border-radius, 32px padding all sides, no shadow. Heading at 28px arcadiaDisplay weight 480, letter-spacing 0.015em, color #ededf3 Ivory. Body text at 16px arcadia weight 400, line-height 1.5, color #ededf3 Ivory.

2. Create a primary CTA button: background #5266eb Cobalt, white text at 16px arcadia weight 400, 32px border-radius (pill), no border, no shadow, 12px vertical / 24px horizontal padding. Text is 'Open account' or equivalent action label.

3. Create a ghost/outline button: transparent background, 1px solid #ededf3 Ivory border, #ededf3 text at 16px arcadia weight 400, 40px border-radius, 10px vertical / 20px horizontal padding.

4. Create a hero section: full-bleed (100vw), full-viewport height, photographic landscape background with dark overlay. Headline at 65px arcadiaDisplay weight 480, line-height 1.1, color #ffffff, centered. Subtext at 18px arcadia weight 480, color #ededf3 Ivory, centered, max-width 520px.

5. Create an inline email capture form: flex row, no gap. Input — transparent background, 1px solid #ededf3 Ivory border (left + top + bottom only), #ededf3 text at 16px arcadia weight 400, placeholder in #c3c3cc Ash, border-radius 32px 0 0 32px, 14px vertical / 20px horizontal padding. Button — #5266eb Cobalt fill, white text at 16px arcadia weight 400, border-radius 0 32px 32px 0, 14px vertical / 24px horizontal padding, no border.

## Typography Philosophy

Mercury's type system uses two custom faces — arcadia for UI/body and arcadiaDisplay for headlines — both built on an intermediate weight axis (360, 420, 480, 530) that avoids the conventional bold/light binary. Heading weight 480 is the signature: it is heavier than regular but distinctly lighter than semibold, creating a voice that asserts without shouting. Display sizes use tight line-heights (1.1–1.15) with positive letter-spacing (0.01–0.02em), giving large text an architectural, wide-set quality. Body text stays at 16px weight 400 with generous 1.5 line-height. The overall effect is a voice that is measured, premium, and digitally native — never editorial, never corporate.
