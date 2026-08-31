# Vercel — Design System

> **North Star**: Typeset terminal on white paper
> **Theme**: light
> **Source**: https://vercel.com
> **Refero Style**: https://styles.refero.design/style/f24daf3a-d43f-4dec-85a9-8ac1d5148a03
> **Synced**: 2026-09-01

## Overview

Vercel's design system is an exercise in disciplined monochrome: a near-white canvas (#fafafa), black typography, hairline borders, and the complete absence of decorative color. The visual language reads like a developer terminal rendered in print — Geist Sans whispers at hero scale with weight 400-450 and -0.06em tracking, while Geist Mono stamps labels, metadata, and code samples in 11-13px caps. Buttons are sharp 6px-radius pills or rectangles in pure black-on-white or white-on-black. The system trusts contrast and typography hierarchy over color, using the triangle mark (▲) and a two-line wordmark as the only brand ornament. Surfaces stack as #fafafa → #ebebeb → #171717, creating depth through tonal value shifts rather than shadow or color. Every element is built on a 4px grid with compact density, producing an interface that feels like an engineer's notebook — precise, functional, and unafraid of empty space.

## Color Palette

- **Paper White**: `#fafafa` — Page canvas, card surfaces, light button fills — the default background that everything else sits on [neutral]
- **Pure White**: `#ffffff` — Elevated card surfaces, inset highlights, input fields [neutral]
- **Hairline**: `#ebebeb` — 1px borders on buttons, links, and cards — visible at high zoom, invisible at speed [neutral]
- **Ash**: `#c9c9c9` — Disabled text, muted labels, brand name watermarks in customer logos [neutral]
- **Smoke**: `#a8a8a8` — Tertiary text, placeholder copy, subtle icon fills [neutral]
- **Graphite**: `#8f8f8f` — Footer micro-copy, secondary metadata [neutral]
- **Slate**: `#7d7d7d` — Customer brand names in logo strips, muted heading variants [neutral]
- **Stone**: `#666666` — Muted captions, helper text, and de-emphasized UI labels. [neutral]
- **Charcoal**: `#4d4d4d` — Body paragraph text, card descriptions, button secondary labels — where reading weight lives [neutral]
- **Obsidian**: `#171717` — Primary headings, nav borders, dark button fills, list markers — near-black that avoids pure #000 harshness [neutral]
- **Carbon**: `#000000` — SVG icon fills, logo marks, the triangle brand glyph — pure black reserved for graphic elements only [neutral]
- **Terminal Green**: `#297a3a` — Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Spectrum Gradient**: `#ff1744` — Decorative gradient sweep for marketing hero accents — the only place color is permitted to exist [accent]
- **Solar Edge**: `#ffdc30` — Decorative two-stop gradient for feature callouts — yellow-to-blue sweep [accent]

## Typography

- **Geist Sans**
- **Geist Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| eyebrow | 11 | — | 1.5 |
| caption | 13 | — | 1.54 |
| body | 16 | — | 1.5 |
| heading | 30 | — | 1.1 |
| heading-lg | 56 | — | 1 |
| display | 64 | — | 1 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 16px
- **Element Gap**: 12px
- **Section Gap**: 96-128px
- **Border Radius**: {'nav': '2px', 'cards': '6px', 'pills': '9999px', 'buttons': '6px'}

## Layout

Max-width 1280px centered container with generous horizontal padding (24-48px). The hero uses an asymmetric three-zone composition: oversized headline left, brand glyph center, eyebrow stack right. Below the hero, content flows in alternating bands: a full-width customer logo strip, then a two-column 'build agents' section with heading left and product mockup right, then a three-up feature card grid. Sections are separated by 96-128px vertical gaps with no dividers or background shifts. The nav is a single 64px sticky bar with backdrop blur. Card grids consistently use a 2-column or 3-column layout with 16-24px gaps. The overall density is compact — text is comfortable to read, whitespace is generous, but the type scale and component sizing keep the page from feeling airy.

## Surfaces / Elevation

- **Page Canvas**
- **Card Surface**
- **Inverted Surface**

**Shadow tokens:**

## Imagery

Imagery is sparse and always functional. The primary visual element is the black triangle (▲) — a geometric brand mark that appears at hero scale as a floating silhouette. Customer logos in the social-proof strip use each brand's actual wordmark in grayscale. Product mockups (Notion chat UI, CLI terminal output, passport card) are embedded as light-mode screenshots within bordered cards. There is no photography, no illustration, no 3D — the system is pure typography and geometric shapes on white paper.

## Design Principles

### Do

- Use #171717 for all primary text and filled buttons — never pure #000000 for text or #ffffff for dark surfaces
- Apply 6px radius to all cards, buttons, and bordered containers (--geist-radius) — use 9999px only for pill-shaped nav actions
- Set headlines at weight 400-450 with -0.06em letter-spacing at 56-64px — never bold headlines over 700
- Use Geist Mono 11-12px uppercase with 0.071em tracking for all eyebrows, labels, and metadata stamps
- Build depth with hairline borders via stacked box-shadows (0 0 0 1px rgba(0,0,0,0.08), 0 0 0 2px #fafafa) — never with drop-shadow
- Space sections at 96-128px vertical gaps with no background shifts or dividers between bands
- Prefix CLI commands with ▲ and confirmations with ✓ in #297a3a — the terminal pattern is the product demo

### Don't

- Never introduce a chromatic color outside the Terminal Green (#297a3a) success indicator and the spectrum gradient — 0% colorfulness is the rule
- Never use border-radius larger than 6px on cards or rectangular buttons — the sharpness is the point
- Never set body or heading type in any color other than the #171717 / #4d4d4d / #666666 scale
- Never use drop-shadows for elevation — hairline rings only, or no depth at all
- Never use light or semibold (300 or 600-700) weights for headlines — the system speaks at 400-450 maximum
- Never set line-height above 1.0 for display sizes (56-64px) — the tight leading is what makes the type feel architectural
- Never use Geist Sans for labels, metadata, or code — Geist Mono owns that space exclusively

## Components

### Filled Black Button

Background #171717, text #ffffff, 6px radius, 12px horizontal padding, Geist Sans 14px/400. Used for Deploy Now, Sign Up. The only element that reaches 'Obsidian' black, making it unmistakable as the page's primary call.

### Ghost Outline Button

Background transparent, text #4d4d4d, 1px border #ebebeb (rendered via box-shadow ring), 6px radius, 20px all padding, Geist Sans 14px/400. Used for Talk to Sales, Get a Demo. Reads as 'available' without asserting hierarchy.

### Pill Button

Background #171717 or #ffffff, text contrasting, 9999px radius (full pill), 12px horizontal padding, 0 vertical padding for tight header use.

### Text Link Button

No background, no border, 0px radius, color #171717 or #4d4d4d, 14-16px Geist Sans. Used for nav items and inline references.

### Bordered Card

Background #ffffff, 6px radius, 1px border via stacked box-shadows: inset ring rgba(0,0,0,0.08) + outer ring #fafafa, 16px padding. The double-ring technique creates a border that survives any background — a signature Vercel trick.

### Inverted Card

Background #171717, white text, 6px radius. Used sparingly (e.g., the Passport card) to break the monotony of an all-light layout.

### CLI Output Panel

Light background with Geist Mono 12-13px text in #171717, prefixed with ▲ triangle marker in #171717 for commands, ✓ checkmark in #297a3a for confirmations. The terminal IS the marketing.

### Logo Strip Row

7+ logos in a row with 24-32px gaps. Customer names render in Geist Sans at the customer's actual brand treatment, faded to #7d7d7d for the page's neutral context.

### Eyebrow Label

Geist Mono 11px/400, 0.071em letter-spacing, uppercase, color #171717. Pairs with a 12px gap before the heading it announces. Examples: 'FOR CODING AGENTS', 'TO SHIP APPS AND AGENTS'.

### Top Nav Bar

Height 64px, sticky, background #fafafa with backdrop-blur (20-48px), wordmark left (▲ + Vercel), nav items center-left at 14px Geist Sans #171717, action cluster right (Get a Demo ghost, Log In ghost, Sign Up filled). No bottom border — separation comes from spacing alone.

### Hero Composition

Three-column asymmetric layout: headline (56-64px, -0.06em tracking, weight 450) left, black triangle glyph center, eyebrow stack right. No background image. The triangle floats with no border or fill — pure black silhouette.

### Feature Card Grid

Large cards with the Bordered Card treatment, 16-24px padding, title at 30px heading weight, description at 14-16px body in #4d4d4d. Each card contains a small product mockup (CLI output, passport, framework logo) as visual evidence.

## Similar Design Systems

- {'why': 'Same sharp 6-8px radii, monochromatic light canvas, and tight-tracking geometric sans-serif headlines — Linear and Vercel share a print-engineering aesthetic', 'business': 'Linear'}
- {'why': 'Similar near-black on warm-white palette, monospace CLI panels, and the discipline of using one accent color (or none) across an entire interface', 'business': 'Railway'}
- {'why': 'Hairline borders, generous whitespace, and the trust that typography hierarchy alone can carry a page without decorative color or imagery', 'business': 'Stripe'}
- {'why': 'Developer-marketing approach: terminal output as hero, monospace labels, the same paper-white canvas and pure-black wordmark', 'business': 'Resend'}
- {'why': 'High-contrast achromatic system with a single chromatic note for state, trusting typographic weight and spacing to create hierarchy', 'business': 'Plaid'}

## Agent Prompt Guide

**Quick Color Reference**
- Background: #fafafa
- Text: #171717
- Border: #ebebeb
- Accent: #000000 (triangle mark only)
- primary action: #171717 (filled action)

**Example Component Prompts**

1. Create a hero headline: Geist Sans 56px weight 450, color #171717, letter-spacing -3.36px, line-height 1.0. Below it, a filled black button (background #171717, text #ffffff, 6px radius, 12px 20px padding, Geist Sans 14px weight 400) and a ghost button beside it (background transparent, text #4d4d4d, 1px border #ebebeb, 6px radius, 20px padding).

2. Create a feature card: background #ffffff, 6px radius, border via stacked box-shadows (0 0 0 1px rgba(0,0,0,0.08), 0 0 0 2px #fafafa), 16px padding. Title in Geist Sans 30px weight 400 with -1.5px tracking, color #171717. Description in Geist Sans 14px weight 400, color #4d4d4d.

3. Create an eyebrow label: Geist Mono 11px weight 400, 0.071em letter-spacing, uppercase, color #171717. Pair with 12px margin-bottom before the heading it introduces.

4. Create a CLI output panel: background #ffffff with 1px border #ebebeb, 6px radius, 16px padding. Commands prefixed with ▲ in #171717, confirmations prefixed with ✓ in #297a3a, all text in Geist Mono 12px weight 400, color #171717.

5. Create a top nav bar: height 64px, background #fafafa with backdrop-filter blur(20px), flex row. Left: ▲ glyph in #000000 + 'Vercel' in Geist Sans 14px weight 500. Center-left: nav items in Geist Sans 14px weight 400, color #171717, 24px gaps. Right: ghost button (border #ebebeb, text #4d4d4d, 6px radius) + filled button (background #171717, text #ffffff, 6px radius, pill-shaped at 9999px radius for tight header use).

## Typographic Discipline

The type system has only two families and 8 sizes. Headlines are weight 400-450 (not 700), tracking tight at -0.06em, line-height 1.0 — they sit on a single line, dense and confident. Body is 14-16px weight 400 at 1.43-1.5 line-height. The only color in the type system is the value shift from #171717 to #4d4d4d to #666666 — never a chromatic tint. Labels and metadata are ALWAYS monospace, ALWAYS uppercase, ALWAYS small (8-12px). This binary — Geist Sans for reading, Geist Mono for stamping — is the system's most recognizable rule.

## The Triangle Protocol

The ▲ glyph is the brand's most deployed element. It appears as: the wordmark icon, the CLI command prefix, a decorative hero silhouette, a loading indicator, and an interactive collapse marker. Always rendered in #000000 at 1:1 aspect ratio, never with a border, never with a fill other than black. It is the only element in the system permitted to be pure #000000 — everything else is #171717 or lighter.
