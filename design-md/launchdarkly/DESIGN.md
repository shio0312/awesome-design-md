# LaunchDarkly — Design System

> **North Star**: Neon control room — a dark cockpit where violet signals pulse through charcoal panels.
> **Theme**: dark
> **Source**: https://launchdarkly.com
> **Refero Style**: https://styles.refero.design/style/18a75348-513a-49d8-94f5-e2df8c118b6b
> **Synced**: 2026-09-01

## Overview

LaunchDarkly is a midnight control room: deep charcoal canvas, cool violet-blue as the only chromatic voice, and white type that cuts through like console output. The interface is dense and technical without feeling cluttered — it borrows the visual language of developer tools (monospace code, panel grids, pill-shaped inputs) and wraps it in a confident marketing skin. The violet→blue gradient (#405bff → #7084ff) acts as the brand's electronic pulse, appearing in glows, hero text, active states, and decorative washes rather than flat fills. Components are pill-soft (30-60px radii dominate), borders are hairline-white on near-black, and elevation is communicated through glow rather than shadow.

## Color Palette

- **Signal Violet**: `#7084ff` — Hero text accent, link underlines, icon glows, decorative gradient endpoint — the brand's chromatic signature; used as paint, not fill; Hero ambient washes, card glow halos, decorative background floods [brand]
- **Voltage Blue**: `#405bff` — Violet outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color [brand]
- **Midnight Ink**: `#0e0e0e` — Page canvas, deepest background layer [neutral]
- **Carbon**: `#191919` — Surface level 1 — nav pill, card backgrounds, button fills, footer [neutral]
- **Graphite**: `#414042` — Surface level 2 — elevated panels, card borders, secondary surfaces [neutral]
- **Steel**: `#58595b` — Input borders, inactive form fields [neutral]
- **Slate**: `#6d6e71` — Muted helper text, disabled labels [neutral]
- **Fog**: `#a7a9ac` — Secondary text, subtle borders, placeholder copy [neutral]
- **Ash**: `#d1d3d4` — Tertiary text, icon strokes, list dividers [neutral]
- **Paper**: `#ffffff` — Primary text, heading fills, icon strokes, card backgrounds in product-screenshot panels [neutral]
- **Smoke**: `#2c2c2c` — List dividers, row separators in dense tables [neutral]
- **Plasma Cyan**: `#3dd6f5` — Secondary gradient endpoint — used sparingly in radial glows for atmospheric warmth [accent]

## Typography

- **bodyFont**
- **Sohne / custom grotesk**
- **Sohne Mono / JetBrains Mono**
- **monoFont**
- **Arial**
- **Helvetica**
- **headingFont1**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.3 |
| heading | 36 | — | 1.2 |
| heading-lg | 66 | — | 1.09 |
| display | 100 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32-48px
- **Element Gap**: 16-24px
- **Section Gap**: 80-120px
- **Border Radius**: {'tags': '30px', 'cards': '30px', 'inputs': '10px', 'buttons': '30px', 'navPill': '60px'}

## Layout

Full-bleed dark canvas with max-width 1200px content containers centered inside. The hero is a tall vertical block (80-100vh) with centered headline + subtext + form input stacked vertically with generous breathing room. Below the hero, sections alternate between two-column layouts (text-left / product-screenshot-right) and three-column card grids. The floating nav pill sits fixed at top center. Section gaps are large (80-120px) to let the dark canvas breathe between content blocks. Content rhythm: hero → logo strip → tabbed feature section (2-col) → code integration section (2-col) → resource card grid (3-col).

## Surfaces / Elevation

- **Midnight Canvas**
- **Carbon Panel**
- **Graphite Edge**
- **Product White**

**Shadow tokens:**

## Imagery

Imagery is sparse and functional. The primary visual content is embedded product UI screenshots — bright white panels showing the LaunchDarkly pipeline interface floating on the dark page. The hero has no photography or illustration; it relies on type, glow, and a large form input. Customer logos appear as a grayscale strip. The code-snippet section uses syntax-highlighted mono text as a visual element. There is no lifestyle photography, no abstract 3D, no decorative illustration — the brand's visual language is the product itself, the code, and the type.

## Design Principles

### Do

- Use 30px radius for all buttons, tags, and cards — the pill-softness is non-negotiable for this brand
- Use 60px radius for the top navigation pill and any full-width pill containers
- Use Signal Violet (#7084ff) for the second half of hero headlines to split the message into 'what' (white) and 'why it matters' (violet)
- Render embedded product screenshots as pure white panels on the dark canvas — the contrast signals 'this is the real workspace'
- Use the #405bff → #7084ff linear gradient at 179deg for ambient glows behind cards and hero text
- Set body text at 16-18px weight 400, white on Carbon — never below 14px for readability on dark
- Use mono font for SDK names, code, and technical identifiers — the monospace voice is part of the developer-tool identity

### Don't

- Don't use square corners or small radii (4-8px) on user-facing components — they break the pill language
- Don't use drop shadows for elevation — use glow (rgba(64,91,255,0.25) or rgba(112,132,255,0.19)) instead to stay on-brand
- Don't introduce additional accent colors — the entire system is monochromatic-plus-violet; adding green, red, or yellow dilutes the signal
- Don't use white or gray for primary action buttons — Voltage Blue (#405bff) is the only correct fill for a main CTA
- Don't center-align body copy or feature lists — only headlines and hero blocks center; everything else is left-aligned
- Don't use 1.5+ line-height on display headlines — keep it tight (1.0-1.09) so the type stacks as a solid block
- Don't put dark product screenshots on the page — the real product UI is always bright/white, creating the page's key visual tension

## Components

### Floating Nav Pill

Centered floating pill at top of viewport, 60px radius, Carbon (#191919) fill, 1px white-alpha border. Contains: logo with arrow icon, nav links (Platform, Solutions, Resources, Developers, Pricing) with chevron dropdowns, Sign In text link, Sandbox text link, and Voltage Blue (#405bff) 'Get a demo' button. Sits 16-24px from viewport top with horizontal margin. No traditional header bar — the pill IS the header.

### Primary Action Button

Voltage Blue (#405bff) fill, white text, 30px radius, 16px vertical × 24px horizontal padding. Used for 'Get a demo' in nav and 'Get started' in hero form. No border, no shadow — the saturated blue is enough presence.

### Hero Form Input

Large dark input with Carbon (#191919) fill, 10px radius, 1px subtle border. Internal layout: email field (white text, #58595b placeholder) fills left, Voltage Blue 'Get started' button fills right. The whole composite has a soft blue glow halo (rgba(64,91,255,0.25) box-shadow) making it feel like a glowing console. Approximately 600px wide, centered, with generous vertical padding (~16-20px).

### Segmented Tab Control

Three-tab pill control (Release / Observe / Iterate) with 30px radius, Carbon fill, 1px border. Active tab indicated by a small Voltage Blue dot to the left of the label and brighter white text. Inactive tabs use Ash (#d1d3d4) text. Centered above a two-column section.

### Feature Checklist Item

Checkmark icon in Voltage Blue or white, followed by white text at ~16-18px. No background, no card. Vertical stack with 12-16px gap between items.

### Sub-feature Card

Semi-transparent dark card with subtle violet/blue glow at edges, rounded 16-20px radius. Contains: small icon (blue or violet), white label text, right-arrow icon. Sits inside a larger section as a navigational sub-element.

### Product Screenshot Panel

Pure white (#ffffff) card with 12-20px radius and soft shadow, containing the actual LaunchDarkly product interface (pipeline configuration). Contrasts sharply with the dark page — the product UI is always shown as 'light' even on the dark marketing page, signaling that the real tool has its own bright workspace.

### Code Snippet Block

Dark Carbon (#191919) panel with 12-16px radius, containing syntax-highlighted code. Language tabs (JavaScript / Python / iOS / React) at top in Ash text with active language in white. Code uses mono font at 14-16px with Dracula-inspired syntax colors (green strings, cyan keywords, pink literals). Copy button in top-right corner.

### SDK/Resource Card

Dark card (Carbon fill) with 1px white-alpha border, 20-30px radius, 32-40px padding. Contains: small icon top-left, white heading text (~18-20px weight 500), white subtext at 14-15px weight 400. Used in grids of 3 columns to link to Docs, Demo Project, Discord, etc.

### Logo Strip

Horizontal row of grayscale partner/customer logos (SpaceX, Tricentis, GoPro, Volvo, Ally, Priceline) at ~70% opacity, Ash or Fog tone. Logos are rendered in white-alpha on the dark background — no boxes, no borders, just quiet type marks.

### Hero Headline

Two-line display headline at 84-100px, weight 500, line-height 1.0-1.09. First line in white ('Move at AI speed.'), second line in Signal Violet ('Stay in control.'). The violet second line is the signature — the brand literally colorizes its differentiator. Letter-spacing tight (normal or slight negative).

### Ghost / Outlined Action

Transparent fill with 1px Signal Violet (#7084ff) border, Signal Violet text, 30px radius. Used for secondary actions where the primary blue button already exists. The violet outline echoes the hero accent — secondary actions share the brand's signature hue rather than fading to neutral.

## Similar Design Systems

- {'why': 'Same dark-canvas + single-accent-glow approach; both treat the product UI itself as the hero visual, and both use pill-shaped inputs and tight type stacks.', 'business': 'Linear'}
- {'why': 'Shares the monochrome dark palette with one chromatic accent, gradient-driven glow effects, and the practice of rendering product interfaces as bright white cards on a dark page.', 'business': 'Vercel'}
- {'why': 'Both use deep charcoal surfaces with violet/purple brand accents, and both embed real product dashboards (not mockups) as the primary visual proof.', 'business': 'Datadog'}
- {'why': 'Similar typographic confidence — large weight-500 display headlines, tight line-height, and the strategy of using color selectively on a subset of words in a headline for emphasis.', 'business': 'Stripe'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff
- background: #0e0e0e
- card/surface: #191919
- border: rgba(255,255,255,0.1) or #414042
- accent: #7084ff
- primary action: #191919 (filled action)

**Example Component Prompts**
1. **Hero headline block**: Full-width dark section, centered. First line 'Move at AI speed.' at 96px weight 500, #ffffff, line-height 1.0. Second line 'Stay in control.' at 96px weight 500, #7084ff, line-height 1.0. Subtext below at 18px weight 400, #d1d3d4, max-width 560px centered.
2. Create a Primary Action Button: #191919 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
3. **Floating nav pill**: Fixed top center, 60px border-radius, #191919 fill, 1px solid rgba(255,255,255,0.08) border, padding 8px 8px 8px 24px. Logo left, links in #d1d3d4 at 14px, 'Get a demo' button (Voltage Blue, white, 30px radius) right.
4. **Product screenshot card**: White #ffffff panel, 16px radius, 32px padding, contains embedded light-UI screenshot. Sits on dark canvas with a subtle rgba(64,91,255,0.2) glow.
5. **Code snippet block**: Dark #191919 panel, 12px radius, 24px padding. Language tabs at top (#d1d3d4 inactive, #ffffff active). Code in mono font 14px, syntax colors: strings #a6e22e, keywords #66d9ef, literals #f92672.
