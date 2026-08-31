# Air — Design System

> **North Star**: midnight sky through glass sculpture
> **Theme**: dark
> **Source**: https://air.inc
> **Refero Style**: https://styles.refero.design/style/d3289fe7-a85e-42d8-96b7-eb7faa62a104
> **Synced**: 2026-09-01

## Overview

Air uses a dark, atmospheric canvas with full-bleed cloud photography and sculptural glass-like 3D forms as its primary visual mode. The type system is the brand: a single sans-serif at moderate weights carries everything from nav to body, while compressed and cursive display cuts break in for emphasis — one italic word ("AI") in cursive sets a confident, slightly playful tone against the otherwise restrained UI. Components are lightweight — minimal elevation, thin borders, small radii, and near-transparent surfaces — letting the imagery carry emotion while the interface stays functional and fast.

## Color Palette

- **Whiteout**: `#ffffff` — Primary text on dark surfaces, nav button borders, hairline strokes, card surfaces over photographic backgrounds [neutral]
- **Haze**: `#f5f5f5` — Card surfaces, input fields, subtle button fills on dark backgrounds — the off-white layer that sits above the dark canvas [neutral]
- **Ink**: `#1b1b1b` — Body and heading text on light surfaces, button borders on light cards [neutral]
- **Black Void**: `#000000` — Navigation borders, link underlines, deepest contrast layer on white surfaces [neutral]
- **Twilight Blue**: `#426188` — Heading text on dark backgrounds — the only chromatic text color, a desaturated steel blue that reads as cool and atmospheric rather than vivid [accent]
- **Signal Blue**: `#2b7fff` — Blue text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [accent]

## Typography

- **Control**
- **Control Compressed**
- **Control Cursive**
- **Control TNT**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.4 |
| heading | 32 | — | 1.1 |
| heading-lg | 56 | — | 1 |
| display | 259 | — | 0.85 |

## Spacing & Layout

- **Max Width**: 1150px
- **Card Padding**: 20px
- **Element Gap**: 8px
- **Section Gap**: 48px
- **Border Radius**: {'cards': '12px', 'pills': '9999px', 'images': '11px', 'inputs': '4px', 'buttons': '8px'}

## Layout

Full-bleed dark sections with photographic backgrounds alternate with centered content blocks. The page max-width is 1150px for text and card grids, but hero and atmospheric sections break to full viewport. Navigation is a minimal top bar (72px height) with left-aligned links and right-aligned actions. Feature sections follow a consistent pattern: centered headline + subtitle, then content arranged in 2-column or 3-column grids with 24px gutters. Display headlines (Control Compressed at 259px) bleed to viewport edges. Logo grids use a single horizontal row with generous spacing. Footer sits on the dark canvas with light text.

## Surfaces / Elevation

- **Dark Canvas**
- **Haze Card**
- **Whiteout**

## Imagery

Full-bleed photographic sections are the primary visual language — moody sky/cloud photography with sculptural translucent glass forms rendered in 3D. The imagery is atmospheric and slightly surreal, occupying the entire viewport with no container constraint. Product UI is shown via contained screenshots in light cards (Haze) that sit as islands on the dark photographic background. Logo bars are monochrome white on the dark canvas. The visual density is image-heavy at section-level but text-dominant in feature breakdowns.

## Design Principles

### Do

- Use Control at weight 500 for all body, nav, button, and link text — consistency of weight creates visual calm
- Set all buttons and interactive elements to 8px border-radius
- Apply 4px radius to form inputs only
- Use #f5f5f5 (Haze) for card surfaces and inputs on dark backgrounds
- Use #ffffff (Whiteout) for borders and text on dark surfaces
- Use #1b1b1b (Ink) for text and borders on light surfaces
- Break headlines with one italic word in Control Cursive against upright Control TNT or Control

### Don't

- Don't use solid filled colored buttons — buttons are ghost (transparent + border) or haze (light fill) only
- Don't apply shadows or elevation to cards — surfaces are flat with borders or background contrast only
- Don't use more than one saturated accent color per page — Signal Blue is for links only, not for buttons or backgrounds
- Don't set body text below 16px or above 500 weight — the type system is deliberately restrained
- Don't use rounded pill shapes for anything except toggle/filter controls
- Don't introduce new radii — stick to 4px (inputs), 8px (buttons), 11–14px (cards/images)
- Don't use gradients — the design relies on photography and flat color contrast for depth

## Components

### Ghost Navigation Button

Transparent background, 1px white border, white text, 8px radius, 10px 16px padding. Used for "Start for free" and "Book a demo" in the nav bar.

### Solid Light Button

#f5f5f5 background, #1b1b1b text, 1px #1b1b1b border, 8px radius, 8px 16px padding. Used on the photo upload card area.

### Pill Toggle Button

Fully rounded (16777220px ≈ pill), semi-transparent dark background (oklab 10% black), black text. Used for feature toggles and category filters.

### Underline Link

Transparent background, 2px bottom underline, text in Signal Blue (#2b7fff) or Ink (#1b1b1b), 8px horizontal padding. Underline is the primary affordance — no color fill.

### Haze Card

#f5f5f5 background, 12px radius, 20px padding, no shadow, no border. Sits as a light island on the dark photographic canvas.

### Image Card with Radius

Transparent background, 11px or 14px radius, no padding, no shadow. Holds product imagery and screenshot grids.

### Text Input

#f5f5f5 background, #1b1b1b text, 1px border at rgba(0,0,0,0.1), 4px radius, 10px padding all sides. Minimal chrome — relies on background contrast rather than border weight.

### Logo Bar Row

Single-row or two-row grid of monochrome logos on the dark canvas, 32px column gap, 48px row gap. Logos rendered in white or semi-transparent white.

### Full-Bleed Photographic Section

Full-viewport-height sections with photographic background (clouds, glass sculpture), centered headline overlay in Whiteout or Twilight Blue, no border, no container constraint. Carries the brand's emotional weight.

### Compressed Display Headline

Control Compressed 900 weight at 259px, line-height 0.85, uppercase, Whiteout text. Bleeds to viewport edges. Used sparingly for maximum-impact statements.

### Dual-Style Headline

Combines Control Cursive italic (56px) for emphasized words with Control TNT upright for the rest. Creates typographic tension — the italic word carries personality while the upright stays grounded.

### Feature Section Header

Control 500 at 20px for subheading, Control Cursive or TNT at 32–56px for the main title. Center-aligned on dark background, generous 48px gap above and below.

## Similar Design Systems

- {'why': 'Same dark-canvas aesthetic with minimal chrome, transparent ghost buttons, and type-driven hierarchy — both let typography carry the brand rather than color or illustration', 'business': 'Linear'}
- {'why': 'Full-bleed dark sections with centered headlines, monochrome interface, and restrained accent color usage — both rely on photographic or gradient atmospheric backgrounds', 'business': 'Vercel'}
- {'why': 'Bold display typography (compressed/condensed faces) over dark backgrounds with sparse UI chrome — both use poster-scale type as the hero moment', 'business': 'Framer'}
- {'why': 'Dark-first product interface with ghost buttons, thin borders, flat card surfaces, and no shadows — components are distinguished by background contrast rather than elevation', 'business': 'Pitch'}

## Agent Prompt Guide

Quick Color Reference:
- text on dark: #ffffff (Whiteout)
- text on light: #1b1b1b (Ink)
- background canvas: #000000 (Black Void)
- card surface: #f5f5f5 (Haze)
- input surface: #f5f5f5 (Haze)
- link text: #2b7fff (Signal Blue)
- heading accent on dark: #426188 (Twilight Blue)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a ghost nav button: transparent background, 1px solid #ffffff border, #ffffff text, 8px radius, 10px vertical and 16px horizontal padding, Control font weight 500 at 14px.

2. Create a Haze card: #f5f5f5 background, 12px radius, 20px padding all sides, no shadow, no border. Place centered on a #000000 dark canvas.

3. Create a text input: #f5f5f5 background, 1px solid rgba(0,0,0,0.1) border, 4px radius, 10px padding all sides, #1b1b1b text, Control font weight 500 at 16px.

4. Create a compressed display headline: Control Compressed at 259px, weight 900, line-height 0.85, uppercase, #ffffff color, bleeding to viewport edges.

5. Create a dual-style headline: first line in Control TNT weight 500 at 56px, line-height 1.0, #ffffff. Second line with one word in Control Cursive weight 400 italic at 56px, remaining words upright. Both centered on dark canvas.
