# Customer.io — Design System

> **North Star**: dark spruce forest meeting cream paper
> **Theme**: mixed
> **Source**: https://customer.io
> **Refero Style**: https://styles.refero.design/style/abbaa70a-5fe2-44a9-9c5f-272e68c450c3
> **Synced**: 2026-09-01

## Overview

Customer.io uses a deep forest palette anchored in near-black spruce greens, creating a page that feels like dark pine on warm paper. Typography is custom Saans at near-uniform weight 475 — an unusual medium-light voice that avoids the typical SaaS shout of bold headings, instead making 96px display text feel architectural and quietly authoritative. Color appears sparingly as functional punctuation: a vivid verdant green glow marks interactive elements, while warm cream surfaces and soft blue washes tint alternate sections. The system is built on thin 1px borders, minimal elevation, pill-shaped primary buttons, and 2px corner radii everywhere else — a flat, almost editorial product surface.

## Color Palette

- **Spruce Abyss**: `#00191c` — Deepest background — footer canvas, dramatic section breaks [neutral]
- **Spruce 900**: `#032125` — Primary dark surface — headers, hero, main navigation background; dominant text color on light surfaces [neutral]
- **Spruce 700**: `#0b363b` — Primary CTA fill on dark backgrounds, elevated card surfaces, border accent [brand]
- **Spruce 500**: `#437278` — Muted teal accent — illustration fills, secondary icon color [accent]
- **Spruce 200**: `#a1c2c6` — Decorative stroke, muted link text, icon outlines on dark surfaces [neutral]
- **Spruce Mist**: `#354d51` — Body text on light surfaces, secondary heading color [neutral]
- **Charcoal 100**: `#ebebeb` — Hairline borders, dividers, subtle separators across the interface [neutral]
- **Charcoal Mist**: `#fafafa` — Alternate section background, subtle card backgrounds [neutral]
- **Cream Warm**: `#fffcf6` — Primary light surface — content sections, card backgrounds [neutral]
- **Pure White**: `#ffffff` — Elevated card surface, button text on dark fills, content blocks [neutral]
- **Verdant 300**: `#abffae` — Interactive glow — CTA button fill, focus ring halo, active state border; vivid green signals action without aggression [brand]
- **Verdant Whisper**: `#eafde8` — Primary page canvas and white card surfaces. Use as a supporting accent, not as a status color [accent]
- **Wave 700**: `#123a88` — Violet text accent for links, tags, and emphasized short phrases. [accent]
- **Wave 500**: `#0a6de6` — Heading accent color for keyword highlights in display text [accent]
- **Wave Frost**: `#e2f4ff` — Hairline borders, dividers, input outlines, and card edges on light surfaces. Use as a supporting accent, not as a status color [accent]
- **Zest 700**: `#863d1c` — Orange text accent for links, tags, and emphasized short phrases. [accent]
- **Zest Blush**: `#fdf0e9` — Hairline borders, dividers, input outlines, and card edges on light surfaces. Use as a supporting accent, not as a status color [neutral]
- **Mustard 700**: `#83611c` — Yellow text accent for links, tags, and emphasized short phrases. [accent]

## Typography

- **Saans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.38 |
| body | 16 | — | 1.38 |
| subheading | 20 | — | 1.13 |
| heading-sm | 24 | — | 1.13 |
| heading | 30 | — | 1.13 |
| heading-lg | 40 | — | 1.13 |
| display | 96 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 24px
- **Section Gap**: 96px
- **Border Radius**: {'tags': '2px', 'cards': '2px', 'images': '6px', 'inputs': '2px', 'buttons': '9999px', 'default': '2px'}

## Layout

Full-bleed sections that alternate between dark Spruce 900 (#032125) and warm cream (#fffcf6) backgrounds. Hero is left-aligned text block occupying ~40% width with product screenshot occupying right ~60%, set against photographic backdrop. Content sections use centered 1200px max-width containers with 96px vertical section gaps. Trust strip uses horizontal marquee of monochrome logos. Footer is full-bleed dark with 4-column grid of links. Navigation is a 64px-tall sticky top bar with logo left, centered nav items, and sign-in + CTA cluster right. Key sections are full-viewport-width colored bands rather than card grids.

## Surfaces / Elevation

- **Spruce Abyss**
- **Spruce Dark**
- **Spruce Mid**
- **Cream Warm**
- **Charcoal Mist**
- **Zest Blush**
- **Verdant Whisper**
- **Wave Frost**
- **Pure White**

**Shadow tokens:**

## Imagery

Warm interior photography with greenery as the backdrop for the hero product preview — a person working at a desk with potted plants, soft natural light, slightly desaturated warm tones. Product screenshots are presented raw without device frames or shadows, blending directly into the photographic background. The brand mark uses a geometric double-chevron arrow symbol in Spruce 900. No illustrations — the visual language is photography + product UI + typography-driven keyword coloring in headings. Logo strip is monochrome black marks on white. The overall density is moderate: generous whitespace in hero, information-dense footer with 4-column link structure.

## Design Principles

### Do

- Use 2px border-radius on all cards, inputs, images, and containers — pill shapes (9999px) are reserved exclusively for buttons
- Use weight 475 for all text including 96px display headlines — never bold above 600 except for 20px subheadings
- Use 1px solid #ebebeb hairline borders for card edges and dividers — never thicker
- Color individual words in display headlines using #863d1c (orange), #123a88 (blue), #41a251 (green), #b52473 (pink) — words stay inline, never separate blocks
- Use #abffae exclusively for primary CTA fills and focus glow rings — never as body text or background tint
- Use 24px for element gaps, 32px for card padding, 96px for section vertical gaps — the 4px base unit scales through these three tiers
- Use #fffcf6 as the default light surface; alternate to #032125 for dark sections; tint with #e2f4ff, #fdf0e9, or #eafde8 for semantic accent bands
- Use 4px colored focus glow rings (0px 0px 0px 4px) for interactive focus states instead of outline or shadow changes

### Don't

- Never use drop shadows for elevation — depth comes from colored 4px glow rings only
- Never use bold weights above 600 for display or heading text — the signature is the calm 475 voice
- Never use corner radius above 2px on non-button elements — sharp-cornered cards define this system
- Never use #0000ee or default browser blue for links — links use #032125 or #a1c2c6
- Never place #abffae on white or light backgrounds without sufficient contrast — it is a glow color, not a fill
- Never use more than 4 columns in content grids — the system favors generous spacing over density
- Never use the heading accent colors (#863d1c, #123a88, etc.) for UI chrome — they exist only for inline keyword coloring in display text

## Components

### Primary Pill Button

Pill shape (9999px radius), Verdant 300 (#abffae) background, Spruce 900 (#032125) text at 16px weight 475, padding 8px 20px, 4px Verdant glow shadow ring on hover/focus

### Secondary Outline Button

Pill shape (9999px radius), transparent background, Spruce 900 (#032125) text at 16px weight 475, 1px Spruce 700 (#0b363b) border, padding 8px 20px

### Ghost Navigation Button

Transparent background, Spruce 900 text at 16px weight 475, no border, padding 0 16px, chevron indicator

### Small Tag Button

2px radius, subtle background tint, Mustard 700 (#83611c) text at 12-14px weight 475, padding 4px 8px

### Content Card

32px padding all sides, Pure White (#ffffff) background, 1px Charcoal 100 (#ebebeb) hairline border, 2px corner radius, no shadow

### Dark Section Card

32px padding, Spruce 700 (#0b363b) background, 1px Spruce 700 border, 2px radius, Spruce 200 (#a1c2c6) body text

### Tinted Feature Surface

Full-bleed tinted background — Wave Frost (#e2f4ff), Zest Blush (#fdf0e9), or Verdant Whisper (#eafde8), 2px radius containers inside, generous 96px vertical padding

### Footer Column

4-column grid on Spruce Abyss (#00191c) background, white heading text at 16px weight 600, Spruce 200 (#a1c2c6) link text at 14px, 24px row gap

### Logo Strip Card

Pure White background, 1px Charcoal 100 border, 2px radius, logo centered, no padding variation; arranged in horizontal marquee

### Heading with Keyword Accent

96px Saans weight 475, Spruce 900 base text with individual words in Zest 700 ('messaging'), Wave 700 ('AI'), Wave 500 ('AI'), Verdant 600 ('data'), Nova 500 ('customers') — words stay inline, color creates semantic meaning

### Trust Indicator Row

Inline list with checkmark icon (Verdant 300), Spruce 900 text at 14px, separated by 16px gaps, no bullet markers

### Interactive Product Preview

Large product UI screenshot with browser chrome, set against a warm interior photography background with green plant, no border or shadow — raw edges blending into scene

### Status Badge

Small green dot (2px radius circle, Verdant 300 fill) beside white text at 12px weight 500

## Similar Design Systems

- {'why': 'Same near-uniform medium weight custom typeface, dark primary surface with cream/warm light alternation, hairline 1px borders, minimal corner radii, generous vertical rhythm', 'business': 'Linear'}
- {'why': 'Dark hero-to-light-section alternation with full-bleed bands, pill-shaped CTAs, subdued typography that lets color accents do the emotional work', 'business': 'Vercel'}
- {'why': 'Warm cream surfaces paired with deep saturated dark sections, thin borders, near-flat elevation, editorial product photography in hero', 'business': 'Attio'}
- {'why': 'Custom geometric sans at restrained weight, dark spruce-toned palette, glow-ring focus states instead of traditional shadows, monochrome logo strip trust section', 'business': 'Resend'}

## Agent Prompt Guide

**Quick Color Reference**
- text (primary): #032125
- text (secondary): #354d51
- text (muted/link): #a1c2c6
- background (light): #fffcf6
- background (dark): #032125
- border (hairline): #ebebeb
- accent (highlight keywords in headings): #863d1c
- primary action: #0b363b (filled action)

**Example Component Prompts**

1. **Hero headline**: Render at 96px Saans weight 475, line-height 1.0, color #032125, letter-spacing 0.0020em. Use the word 'messaging' in #863d1c and 'AI' in #123a88 as inline accent colors within the same line.

2. Create a Primary Action Button: #0b363b background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. **Dark section card**: Background #0b363b, 32px padding all sides, 2px corner radius, 1px #0b363b border, body text #a1c2c6 at 16px weight 475, heading in white at 24px weight 475.

4. **Trust indicator row**: Three inline items at 14px weight 475 in #032125, each preceded by a small #abffae checkmark icon, separated by 24px gap, no dividers.

5. **Tinted feature section**: Full-bleed #e2f4ff background, 96px vertical padding, centered 1200px content container, heading at 40px weight 475 in #032125, 3-column grid of feature items below with 2px-radius white cards inside.
