# Ease Health — Design System

> **North Star**: Botanical greenhouse on cream paper
> **Theme**: light
> **Source**: https://easehealth.com
> **Refero Style**: https://styles.refero.design/style/e9f5e976-53f7-42f5-a882-4e63b3c2f734
> **Synced**: 2026-09-01

## Overview

Ease Health uses a clinical-botanical language: a warm cream canvas layered with soft sage, keylime, and slate-blue panels that feel like a greenhouse rendered on paper. Typography carries the entire personality — weight 300 serif headlines (Faire Octave) paired against a humanist sans (Suisse Intl) create a hushed, editorial authority unusual for healthtech. A single deep forest green (#0f3e17) anchors every action and heading, reading like ink on watercolor. Surfaces are flat and shadowless; depth comes from layered tinted panels and generous padding, not elevation. Components are rounded (~14px) and pill-shaped for tags, keeping the whole system soft and approachable without losing clinical seriousness.

## Color Palette

- **Forest Ink**: `#0f3e17` — Primary action buttons, headings, links, icon strokes — deep botanical green reads as ink, the only saturated dark in the system [brand]
- **Sage Mist**: `#b1dbb8` — Mid-tone card backgrounds and decorative washes, panel-level surfaces [brand]
- **Keylime Wash**: `#e1f4df` — Hero panel background, light card surfaces — the dominant tinted canvas tone [brand]
- **Mint Veil**: `#cfe7d3` — Accent card surfaces, soft section dividers between sage and keylime layers [brand]
- **Slate Hush**: `#b6ced5` — Cool counter-balance panel for product preview and feature blocks — breaks the green monotony with desaturated blue-gray [accent]
- **Cream Paper**: `#fffefc` — Page background, badge backgrounds, button text — warm off-white that softens every green [neutral]
- **Charcoal**: `#222222` — Navigation text and minor UI strokes — restrained secondary ink [neutral]
- **Border Mist**: `#efeeeb` — Hairline dividers and subtle borders throughout the layout [neutral]
- **Forest Shadow**: `#0c2f10` — Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color [neutral]

## Typography

- **Faire Octave**
- **Suisse Intl**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.61 |
| body | 14 | — | 1.5 |
| subheading | 18 | — | 1.3 |
| heading-sm | 23 | — | 1.5 |
| heading | 40 | — | 1.35 |
| heading-lg | 56 | — | 1.2 |
| display | 74 | — | 1.05 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 28-42px
- **Element Gap**: 14-21px
- **Section Gap**: 64-96px
- **Border Radius**: {'nav': '7px', 'cards': '14px', 'badges': '999px', 'buttons': '14px', 'sections': '9999px'}

## Layout

Max-width 1200px centered container with 64–96px vertical section gaps. Hero is a two-column split: left panel tinted Keylime Wash with serif headline + body + CTA; right panel tinted Slate Hush housing three product preview cards (CRM, EHR, RCM) in a row. Below the hero, sections alternate between cream canvas and tinted panels in a botanical rhythm. FAQ uses a two-column text grid (serif question left, sans answer right). The investor logo strip is a single full-width row on cream. Navigation is minimal — left-aligned logo, centered text links, right-aligned CTA pill — no sticky behavior or mega-menu. The overall page rhythm is generous and editorial rather than dense.

## Surfaces / Elevation

- **Cream Paper**
- **Keylime Wash**
- **Mint Veil**
- **Sage Mist**
- **Slate Hush**

## Imagery

Imagery is product-first and UI-native: floating product screenshots (CRM cards, EHR patient views, RCM revenue graphs) rendered as crisp white cards on Slate Hush panels. No lifestyle photography, no stock imagery. Iconography is minimal stroke-based, rendered in Forest Ink. Illustrations, where present, use the same sage/keylime palette to stay on-system. The visual density is text-dominant with product mockups serving as proof, not decoration.

## Design Principles

### Do

- Use Forest Ink (#0f3e17) for every CTA, heading, and primary link — it is the only saturated dark and must remain singular
- Set all display headings in Faire Octave weight 300 with tight tracking (-0.03em at 56–74px) — never bold the serif
- Pair serif questions with sans-serif answers in FAQ and feature blocks to create typographic contrast
- Layer surfaces using cream → keylime → mint → sage → slate in order to create depth without shadows
- Use 14px border-radius on all cards and buttons, 999px on all badges and tags — consistency is non-negotiable
- Apply 0.08em letter-spacing with uppercase and 600 weight for eyebrow labels only — nowhere else
- Keep the Slate Hush panel as the exclusive home for product screenshots — it provides the cool counterbalance to warm green panels

### Don't

- Never add box-shadow to cards — the system communicates elevation through tinted layers only
- Don't use Forest Ink as a background tint — it is too dark for surface washes; reserve for text and action fills only
- Avoid mixing multiple heading weights — everything is weight 300 in Faire Octave; bold would break the hushed editorial tone
- Don't place colored borders on cards — depth comes from fill contrast, not strokes
- Never use more than one serif at a time — Faire Octave owns display, Suisse Intl owns everything else
- Don't introduce new accent hues — the palette is strictly botanical greens + slate; any other color breaks the greenhouse metaphor
- Avoid tight padding under 21px on cards — generous 28–42px padding is essential to the soft, breathing-room aesthetic
- Don't use the sage or keylime tones for text — they are surface colors only and fail contrast for copy

## Components

### Primary Forest Button

Background #0f3e17, text #fffefc, 14px border-radius, padding 14px 21px, Suisse Intl 14px/400. Arrow icon in white at trailing edge. Hover transitions to #0c2f10.

### Large Forest Button

Same Forest Ink fill and white text, but padding scales to 42px all sides for hero placement. Rounded 14px corners. Used sparingly for maximum-weight calls to action.

### Pill Badge / Tag

Background #fffefc, text Forest Ink #0f3e17, 999px border-radius (full pill), padding 9px 14px, Suisse Intl 14px/400. Inverted cream-on-green relationship makes tags feel like paper labels.

### Sage Feature Card

Background Sage Mist #b1dbb8, 14px border-radius, 42px padding all sides, no shadow. Hosts illustration or product preview content. Flat surface — depth comes from color not elevation.

### Keylime Soft Card

Background Keylime Wash #e1f4df, 14px border-radius, 28px padding, no shadow. Tighter padding than sage variant for compact content blocks.

### Slate Product Panel

Background Slate Hush #b6ced5, 14px border-radius, 42px padding, no shadow. Provides cool visual counterpoint to warm green panels — the only non-green tinted surface.

### Product Preview Card (Inner)

Background Cream Paper #fffefc, 14px border-radius, 28px padding, no border or shadow. Represents a product screen mockup (CRM, EHR, RCM). Sits on the Slate panel like a printed screenshot.

### Navigation Bar

Transparent over cream canvas, text Charcoal #222222, Suisse Intl 14px/400, 7px radius on interactive items. 'Book a Demo' CTA pill on the right uses Forest Ink fill.

### Eyebrow Label

Suisse Intl 11px/600, letter-spacing 0.08em, uppercase, Forest Ink color. Tiny typographic marker that labels each section's theme (e.g. 'QUICK ANSWER').

### FAQ Row

Left column: Faire Octave 40px/300 in Forest Ink for question. Right column: Suisse Intl 14px/400 in Charcoal for answer. 1px Border Mist divider between rows.

### Investor Logo Strip

Single horizontal row, monochrome treatment in Charcoal #222222 on cream canvas, generous vertical padding (42px+). No decorative borders — relies on whitespace for rhythm.

## Similar Design Systems

- {'why': 'Same botanical palette approach with sage greens and soft tinted panels, plus serif-leaning editorial calm and generous breathing room', 'business': 'Headspace'}
- {'why': 'Nature-inspired muted greens against cream, generous whitespace, flat surfaces without shadows, and a serene clinical-adjacent tone', 'business': 'Calm'}
- {'why': "Deep single-color ink (#0f3e17 forest vs Mercury's near-black) against a warm off-white canvas with editorial serif display type at weight 300", 'business': 'Mercury'}
- {'why': 'Behavioral health branding with green-dominant palette, soft panel layering, and humanist sans body type paired with serif accents', 'business': 'Spring Health'}
- {'why': 'Healthcare SaaS using sage and mint greens against cream, with rounded components and a botanical rather than clinical visual mood', 'business': 'Grow Therapy'}

## Agent Prompt Guide

**Quick Color Reference**
- Text/Heading: #0f3e17 (Forest Ink)
- Page background: #fffefc (Cream Paper)
- Hero/light panel: #e1f4df (Keylime Wash)
- Feature panel: #b1dbb8 (Sage Mist)
- Product showcase panel: #b6ced5 (Slate Hush)
- Border: #efeeeb
- primary action: #0f3e17 (filled action)

**Example Component Prompts**
1. Create a Primary Action Button: #0f3e17 background, #fffefc text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Feature card**: Sage Mist #b1dbb8 background, 14px border-radius, 42px padding all sides, no shadow. Eyebrow label in Suisse Intl 11px/600 uppercase with 0.08em tracking, Forest Ink color. Heading in Faire Octave 40px/300, Forest Ink. Body in Suisse Intl 14px/400, Charcoal #222222.

3. **Pill badge**: Background Cream Paper #fffefc, text Forest Ink #0f3e17, 999px border-radius, padding 9px 14px, Suisse Intl 14px/400. Place above section headings as a category tag.

4. **FAQ row**: Two-column grid. Left: Faire Octave 40px/300 question in Forest Ink. Right: Suisse Intl 14px/400 answer in Charcoal #222222. Separator: 1px solid Border Mist #efeeeb below each row.


## Type Pairing Philosophy

The serif/sans split is the system's defining typographic move. Faire Octave (or Cormorant Garamond as substitute) handles ALL headings at weight 300 — never bold. Suisse Intl (or Inter) handles ALL UI and body text. The whisper-weight serif creates editorial calm unusual in healthtech, where most competitors use bold geometric sans headlines. Tracking tightens as size grows: -0.01em at 40px, -0.03em at 56–74px. Body text uses natural tracking. The only uppercase treatment is 11px/600 eyebrows at 0.08em — these are navigational markers, not decorative caps.
