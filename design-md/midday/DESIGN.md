# Midday — Design System

> **North Star**: Editorial broadsheet on parchment — a 72px serif headline over warm stone, spaced sans-serif body text, pill-shaped controls, zero shadows.
> **Theme**: light
> **Source**: https://midday.ai
> **Refero Style**: https://styles.refero.design/style/3f2b79c1-d980-4380-a903-29856975fc37
> **Synced**: 2026-09-01

## Overview

Midday reads like an editorial broadsheet translated to software: a warm parchment canvas, a spaced sans-serif body voice, and a serif display face that announces sections like magazine pull-quotes. The system is monochrome to the point of austerity — surfaces stack in warm off-whites, borders are hairline-thin, and chromatic color appears only as functional punctuation for financial data (a single moss green) and the dark filled CTA. Every interactive element is pill-shaped; nothing is squared off. The design is completely flat — no shadows, no gradients, no decorative depth. Spacing is compact and rhythmic on a 4px grid, keeping dense ledger data legible without breathing room.

## Color Palette

- **Parchment**: `#dbdad7` — Page canvas and hairline borders — the warm off-white that unifies every surface and defines every divider at 1px [neutral]
- **Paper**: `#ffffff` — Card surfaces, input fields, pill button fills — pure white sits one level above the warm canvas [neutral]
- **Sand**: `#e6e4e0` — Secondary surface for table rows, inset panels, and tonal contrast between stacked cards [neutral]
- **Ink**: `#121212` — Primary text, icons, and logo — near-black for maximum contrast against parchment and paper [neutral]
- **Smoke**: `#616161` — Secondary text, muted labels, chart axis lines, non-active icon strokes [neutral]
- **Charcoal**: `#18181b` — Primary action fill — dark filled buttons and active navigation state, white text reverses on top [neutral]
- **Moss**: `#4caf50` — Green text accent for links, tags, and emphasized short phrases [accent]

## Typography

- **Hedvig Letters Sans**
- **Hedvig Letters Serif**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.56 |
| body | 14 | — | 1.43 |
| heading-sm | 20 | — | 1.4 |
| heading | 24 | — | 1.33 |
| heading-lg | 48 | — | 1 |
| display | 72 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'cards': '8px', 'icons': '8px', 'pills': '9999px', 'badges': '9999px', 'inputs': '8px', 'buttons': '9999px'}

## Layout

Max-width 1200px centered, generous 64px vertical gaps between sections. Hero is a centered text stack (announcement pill → serif display → sans subtext → CTA → trust line → tool logos) on the warm parchment canvas. The product screenshot breaks full-bleed with a dark device frame. Mid-page sections use centered text headings above wide grids (integration pills in a single flowing row, pricing cards in a 2-column grid). Navigation is a minimal top bar: logo left, right-aligned text links, outlined sign-in button. Content density is compact within cards and data tables, spacious between marketing sections.

## Surfaces / Elevation

- **Parchment**
- **Sand**
- **Paper**

## Imagery

Photography-free. The visual centerpiece is a single product screenshot presented in a dark laptop frame, showing a full dashboard with bar charts, line graphs, and data tables rendered in the same monochrome palette with moss-green data accents. Secondary imagery is limited to grayscale third-party tool logos (Slack, Stripe, Xero, etc.) used as integration markers. No decorative illustrations, no abstract graphics, no stock photography — the product UI itself is the hero visual.

## Design Principles

### Do

- Set body sans-serif text to 0.05em letter-spacing at 10–14px and 0.025em at 16px+ — the positive tracking is the system's editorial signature
- Use Hedvig Letters Serif at 72px with -0.025em tracking for display headlines; pair it with spaced sans-serif body below
- Set all buttons, badges, and pills to 9999px border-radius — no element in the interface is squared off
- Fill primary CTAs with #18181b and reverse to white text; keep all secondary actions as transparent ghost or outlined pills
- Use 1px #dbdad7 hairline borders for cards, inputs, and table rows — the same color as the canvas, so borders feel engraved not stamped
- Keep the canvas at #dbdad7 — never switch to cool grays, pure white page backgrounds, or off-brand cream tones
- Use #4caf50 only inside data contexts (chart bars, positive table values, status pills) — never as a button fill or decorative accent

### Don't

- Don't add box-shadows to any component — depth comes from surface tone shifts and hairline borders only
- Don't use #4caf50 for CTAs, links, or brand decoration — it's a data color, not an action color
- Don't apply negative letter-spacing to sans-serif body text — the positive tracking is the voice, not a bug to fix
- Don't use square corners on buttons, inputs, badges, or tags — everything interactive is pill-shaped
- Don't introduce blue, purple, or any second chromatic accent — the system is monochrome by design
- Don't use Hedvig Letters Serif for body copy, labels, or navigation — it's reserved for display headings at 24px and above
- Don't use cool gray borders or backgrounds — the warm stone palette (#dbdad7, #e6e4e0) is non-negotiable

## Components

### Top Navigation Bar

Transparent over parchment canvas. Logo (sun mark) at far left, 4–5 text links (Features, Pricing, Story, Download, Resources) right-aligned with dropdown carets, outlined pill button at far right. 16px vertical padding, no border, no background fill.

### Announcement Pill

White (#ffffff) fill, #dbdad7 1px border, 9999px radius. Padding 6px 12px. Text: 12px Hedvig Letters Sans weight 500, #121212, letter-spacing 0.6px. Optional trailing arrow icon in #121212.

### Primary CTA Button

#18181b fill, white text, 9999px radius. Padding 6px 16px. Text: 14px Hedvig Letters Sans weight 500, #ffffff, letter-spacing 0.7px. No border, no shadow.

### Ghost/Outline Button

Transparent fill, #dbdad7 1px border, 9999px radius. Padding 6px 12px. Text: 14px Hedvig Letters Sans weight 500, #121212, letter-spacing 0.7px.

### Product Screenshot Frame

Full-bleed section with #121212 or dark gradient background. Centered laptop/screen frame containing the live product UI (dashboard with sidebar nav, data cards, bar charts, tables). The dark frame is the only visual depth in the entire system.

### Integration Pill

White (#ffffff) fill, #dbdad7 1px border, 9999px radius. Padding 6px 10px. Contains a small grayscale tool logo (16px) + 12px sans-serif label. Arranged in a wrapping row with 8px gaps.

### Pricing Toggle

Pill-shaped container with #e6e4e0 fill, 9999px radius. Two segments: inactive segment is transparent text, active segment has white (#ffffff) fill with 9999px radius. Text: 12px sans-serif weight 500.

### Pricing Card

White (#ffffff) fill, #dbdad7 1px border, 8px radius. Padding 24px. Tier name: 18px sans-serif weight 500, #121212. Price: 48px sans-serif weight 500, #121212, with /month suffix at 14px. Description and features in 14px body text, #616161. The 'Most popular' card adds a badge.

### Most Popular Badge

White fill, #dbdad7 1px border, 9999px radius. Positioned at top-right of card, overlapping the border. Text: 12px sans-serif weight 500, #121212.

### Dashboard Data Card

White (#ffffff) fill, #dbdad7 1px border, 8px radius. Padding 20px. Contains a category label (12px sans-serif, #616161), a primary value (24px sans-serif weight 500, #121212), and an optional mini-chart (bar or line, #dbdad7 strokes with #4caf50 or #121212 fills).

### Sidebar Navigation

Transparent or #ffffff fill, no border. Icons: 20px outlined style, #616161 default / #121212 active, 8px radius. Vertical stack with 8px gaps. Active item may show a subtle #e6e4e0 pill background.

### Data Table Row

Transparent fill, #dbdad7 1px bottom border. Padding 12px 16px. Text: 14px sans-serif weight 400, #121212. Alternating rows use #e6e4e0 fill. Positive values shown in #4caf50.

## Similar Design Systems

- {'why': 'Same flat monochrome system with pill-shaped controls, hairline borders, and a single dark filled CTA — both treat shadow as a design failure', 'business': 'Linear'}
- {'why': 'Same editorial typography approach for a financial product — warm canvas, serif/sans contrast, spaced sans-serif body, austere color palette', 'business': 'Mercury'}
- {'why': 'Same serif display + spaced sans-serif body pairing and pill-shaped UI elements that treat the browser/app as an editorial object', 'business': 'Arc Browser'}
- {'why': 'Same editorial typography discipline on marketing pages — large serif headlines above clean sans-serif body, generous whitespace, restrained color', 'business': 'Stripe'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #121212
- background: #dbdad7
- card surface: #ffffff
- border: #dbdad7 (1px hairline)
- secondary text: #616161
- primary action: #18181b (filled action)

**Example Component Prompts**
1. *Hero section*: Parchment (#dbdad7) canvas. Display headline: 72px Hedvig Letters Serif weight 400, #121212, letter-spacing -1.8px. Subtext: 16px Hedvig Letters Sans weight 400, #616161, letter-spacing 0.4px. Primary CTA: #18181b fill, white text, 9999px radius, 6px 16px padding, 14px sans weight 500, letter-spacing 0.7px. Trust line: 12px sans weight 400, #616161, letter-spacing 0.6px.

2. *Pricing card*: White (#ffffff) background, #dbdad7 1px border, 8px radius, 24px padding. Tier name: 18px Hedvig Letters Sans weight 500, #121212, letter-spacing 0.45px. Price: 48px sans weight 500, #121212, letter-spacing 1.2px. Description: 14px sans weight 400, #616161, letter-spacing 0.7px. Features list: 14px sans weight 400, #121212, 8px row gap.

3. *Integration pill*: White (#ffffff) fill, #dbdad7 1px border, 9999px radius, 6px 10px padding. Contains a 16px grayscale tool logo + 12px Hedvig Letters Sans weight 500 label, #121212, letter-spacing 0.6px. Arranged in a wrapping row with 8px gaps.

4. *Announcement badge*: White (#ffffff) fill, #dbdad7 1px border, 9999px radius, 6px 12px padding. Text: 12px Hedvig Letters Sans weight 500, #121212, letter-spacing 0.6px. Trailing arrow icon: 12px, #121212.

5. Create a Primary Action Button: #18181b background, #616161 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
