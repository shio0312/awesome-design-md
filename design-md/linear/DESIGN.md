# Linear — Design System

> **North Star**: midnight precision instrument
> **Theme**: dark
> **Source**: https://linear.app
> **Refero Style**: https://styles.refero.design/style/90ce5883-bb24-4466-93f7-801cd617b0d1
> **Synced**: 2026-09-01

## Overview

Linear's design system is a midnight command center built on near-black surfaces (#08090a) with paper-white type and one electric acid-lime accent (#e4f222) that functions as a functional flashlight — small, high-contrast, and used sparingly to signal action. The interface treats darkness as a substrate rather than a theme: text is crisp white at tight tracking (-0.022em), weights sit in a low 400–510 band rather than bold, and borders are hairline-thin (0.5px) to let geometry do the work that shadows usually would. Components feel precision-machined — 6px and 12px radii, compact 8–12px paddings, and almost no decorative ornament — letting the product UI (issue cards, kanban boards, AI agent panels) be the only visual texture in an otherwise quiet system.



## Color Palette

- **Void**: `#08090a` — Page canvas, full-bleed backgrounds — the default everything sits on [neutral]
- **Carbon**: `#0f1011` — Card surfaces, nav bars — one step above canvas for contained content [neutral]
- **Obsidian**: `#161718` — Elevated surfaces, deeper card panels [neutral]
- **Graphite**: `#23252a` — Subtle borders, dividers, ghost button outlines — low-contrast structural edges [neutral]
- **Smoke**: `#383b3f` — Hairline borders at higher contrast than graphite — section separators [neutral]
- **Ash**: `#62666d` — Muted body text, inactive icons, secondary metadata [neutral]
- **Fog**: `#8a8f98` — Tertiary text, placeholder copy, icon fills [neutral]
- **Mist**: `#d0d6e0` — Secondary headings, button text on dark surfaces [neutral]
- **Bone**: `#e5e5e6` — Near-white surface fills, high-contrast button text [neutral]
- **Paper**: `#ffffff` — Primary headings, hero type, max-contrast emphasis text [neutral]
- **Acid Lime**: `#e4f222` — Primary action buttons, active nav indicators — electric accent that breaks the monochrome system [brand]
- **Pulse Green**: `#27a644` — Green outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color [accent]
- **Coral Red**: `#eb5757` — Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]
- **Signal Teal**: `#02b8cc` — Decorative accent, informational icon fills [accent]
- **Iris Violet**: `#6366f1` — Tag/badge fills — soft chromatic punctuation on tags and labels [accent]
- **Lavender**: `#8b5cf6` — Secondary tag fills, category indicators [accent]

## Typography

- **Inter Variable**
- **Berkeley Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.2 |
| body-sm | 15 | — | 1.6 |
| body-lg | 20 | — | 1.33 |
| subheading | 24 | — | 1.33 |
| heading-sm | 32 | — | 1.13 |
| heading | 48 | — | 1 |
| heading-lg | 64 | — | 1 |
| display | 72 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 96px
- **Border Radius**: {'cards': '12px', 'pills': '9999px', 'small': '2px', 'badges': '4px', 'inputs': '6px', 'buttons': '6px'}

## Layout

Layout is max-width contained at ~1200px, centered, with full-bleed dark backgrounds extending to viewport edges. The hero is a left-aligned oversized headline (64–72px) paired with a right-aligned link CTA, followed by a large product screenshot that bleeds beyond the max-width slightly. Section rhythm alternates between text-left/image-right 2-column compositions and full-width product showcase bands, separated by 96px vertical gaps. The customer logo strip is a single horizontal row. The page never uses 3-column card grids or masonry — information density stays low, with most sections using generous whitespace and a single focal point per screen. Navigation is a fixed top bar with left-aligned logo and right-aligned links, no sidebar, no mega-menu.

## Surfaces / Elevation

- **Void**
- **Carbon**
- **Obsidian**
- **Slate**

## Imagery

Linear's visual language is product-screenshot-first: the hero and section illustrations are real Linear app UI captured at full fidelity — issue cards, kanban boards, AI agent panels, command palettes — placed inside framed card containers with hairline borders. No stock photography, no lifestyle imagery, no abstract illustration. Logos appear as a customer strip in neutral grey (#8a8f98) at uniform size. Icons are minimal line-art SVGs in single-color grey scale. The hero screenshot floats on a subtle linear gradient (dark-to-light) that creates atmospheric depth without literal scenery. Every visual element is a functional artifact of the product itself.

## Design Principles

### Do

- Use Inter Variable with font-feature-settings 'cv01' on, 'ss03' on, 'zero' on — these alternate glyphs define Linear's typographic identity
- Use #e4f222 exclusively for the single primary action per view — never for decoration, never for secondary buttons
- Set body text at 16px Inter weight 400 with line-height 1.5 — larger reading sizes (17px+ at weight 590) are reserved for body emphasis blocks
- Use letter-spacing -0.022em at 48px and above — tight tracking is non-negotiable for display type
- Set card radius to 12px, button radius to 6px, pill radius to 9999px — three radii is the entire radius vocabulary
- Use 0.5px hairline borders (#23252a or #383b3f) instead of shadows for surface separation — Linear's elevation comes from borders and subtle inner shadows
- Keep section gaps at 96px and element gaps at 8px — the 8/12/24/96 spacing ladder is the rhythm

### Don't

- Do not use bold weights (700+) — Linear's type scale caps at weight 590, the system deliberately avoids heavy display weights
- Do not use decorative gradients on buttons, cards, or text — gradients are reserved for the hero atmospheric floor only
- Do not introduce additional chromatic accent colors as actions — the acid-lime button is the only chromatic UI element
- Do not use large radii (16px+) on cards or panels — 12px is the max card radius in this system
- Do not use shadows to separate cards from the canvas — use hairline borders (#23252a) and inner inset shadows instead
- Do not use chromatic text colors for body copy — all body text sits in the #d0d6e0 / #8a8f98 / #62666d grey scale
- Do not use Berkeley Mono for headings or marketing copy — it is reserved for issue IDs, keyboard shortcuts, and technical metadata

## Components

### Primary Action Button (Acid Lime)

Background #e4f222, text #08090a, border-radius 6px, padding 10px 16px, Inter 14px / weight 510, letter-spacing -0.011em. Sits as the sole filled chromatic element — every other button on the site is neutral.

### Nav Text Button

Transparent background, text #d0d6e0, padding 8px 12px, Inter 13px / weight 400. No border, no fill — pure typographic nav with underline on hover.

### Pill Button

Background rgba(255,255,255,0.05), text #d0d6e0, border-radius 9999px, padding 4px 12px, Inter 12–13px / weight 400.

### Ghost / Outline Button

Transparent background, border 1px #23252a, text #d0d6e0, border-radius 6px, padding 8px 12px, Inter 13px / weight 400.

### Sign-up Button (Rounded Pill, Neutral)

Background #ffffff, text #08090a, border-radius 9999px, padding 8px 16px, Inter 13px / weight 510. White pill against the dark nav bar — the second highest-contrast element after the acid-lime CTA.

### Card (Product Screenshot Frame)

Background #0f1011, border-radius 12px, inset shadow rgb(35,37,42) 0 0 0 1px, padding 24px. Hairline inner border defines the card edge — no outer shadow, no glow.

### Card (Subtle)

Background rgba(255,255,255,0.02), border-radius 6px, shadow rgba(0,0,0,0.4) 0 2px 4px, padding 8px. Almost invisible — the card barely separates from the canvas.

### Text Input

Background rgba(255,255,255,0.02), border 1px rgba(255,255,255,0.08), text #d0d6e0, border-radius 6px, padding 12px 14px, Inter 14px / weight 400. Focus ring: border brightens to #d0d6e0.

### Badge / Status Tag

Background rgba(255,255,255,0.05), text #8a8f98, border-radius 4px, padding 0px 6px, Inter 12px / weight 400. Color-coded variants use Pulse Green, Coral Red, Iris Violet, or Lavender fills.

### Logo Mark

Linear wordmark + geometric glyph, Inter 16px / weight 510, color #ffffff. Glyph rendered as inline SVG in white.

### Logo Bar (Customer Strip)

Neutral grey logos (Vercel, Cursor, Oscar, OpenAI, Coinbase, Cash App, Boom, Ramp) at #8a8f98–#d0d6e0, evenly spaced with 48–64px gaps, no card backgrounds.

### Hero Gradient Floor

Linear gradient from rgb(8,9,10) at 10% to rgb(208,214,224) at 100% — a subtle light wash that grounds the floating product UI against the void.

## Similar Design Systems

- {'why': 'Same dark-canvas-first approach with hairline borders, tight Inter typography, and product-screenshot-as-hero layout — both treat the product UI as the visual content rather than illustration', 'business': 'Vercel'}
- {'why': 'Identical midnight dark mode with acid-lime accent CTA, compact Inter type at 400–510 weights, and product-screenshot showcase cards at 12px radius', 'business': 'Cursor'}
- {'why': 'Shared dark precision-instrument aesthetic — compact spacing, 6px button radius, monochromatic chrome with a single functional accent color for active states', 'business': 'Raycast'}
- {'why': 'Same dark-canvas layout language with large 48–64px Inter headings at tight tracking, product-screenshot hero cards, and minimal ornament between sections', 'business': 'Framer'}

## Agent Prompt Guide

**Quick Color Reference:**
- text (primary heading): #ffffff
- text (body): #d0d6e0
- text (muted): #8a8f98
- background (canvas): #08090a
- background (card): #0f1011
- border (hairline): #23252a
- accent (CTA): #e4f222
- primary action: #e4f222 (filled action)

**3-5 Example Component Prompts:**

1. **Hero headline block:** Full-bleed #08090a canvas. Headline at 64px Inter Variable weight 510, color #ffffff, letter-spacing -0.022em, line-height 1.0. Subtext at 16px Inter weight 400, color #8a8f98. No button — secondary link text in #d0d6e0 with arrow glyph.

2. **Product screenshot card:** Background #0f1011, border-radius 12px, inset border 1px #23252a via box-shadow, padding 24px. Contains a simulated app UI at full opacity over the card surface. No outer drop shadow.

3. **Acid-lime primary action button:** Background #e4f222, text #08090a, border-radius 6px, padding 10px 16px, Inter 14px weight 510, letter-spacing -0.011em. Only one per view.

4. **Nav top bar:** Background #08090a (transparent over canvas), padding 16px horizontal, max-width 1200px centered. Logo wordmark #ffffff at 16px weight 510 left-aligned. Nav links #d0d6e0 at 13px weight 400, 8px gaps. Right-aligned white pill sign-up button: bg #ffffff, text #08090a, border-radius 9999px, padding 8px 16px.

5. **Status badge row:** Horizontal flex, 8px gap. Each badge: background rgba(255,255,255,0.05), text #8a8f98, border-radius 4px, padding 0px 6px, Inter 12px weight 400. Color-coded variants: #27a644 for success, #eb5757 for error, #6366f1 for tags.

## Type Scale Detail

Display: 72px / 510 / lh 1.0 / ls -0.022em
Hero: 64px / 510 / lh 1.0 / ls -0.022em
Section heading: 48px / 510 / lh 1.0 / ls -0.022em
Subheading: 32px / 400 / lh 1.13 / ls -0.022em
Heading: 24px / 400 / lh 1.33 / ls -0.012em
Body emphasis: 20px / 590 / lh 1.33 / ls -0.012em
Body large: 17px / 590 / lh 1.6 / ls default
Body: 16px / 400 / lh 1.5 / ls default
Body small: 15px / 400 / lh 1.6 / ls -0.011em
Caption: 13px / 400 / lh 1.2 / ls default
Label: 12px / 400 / lh 1.4 / ls default
Micro: 10px / 510 / lh 1.5 / ls default
