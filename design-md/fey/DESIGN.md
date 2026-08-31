# Fey — Design System

> **North Star**: Nocturnal Bloomberg terminal, matte-black with luminous type
> **Theme**: dark
> **Source**: https://www.fey.com
> **Refero Style**: https://styles.refero.design/style/a0630421-7b66-48b4-aa14-6194a3b2c2b9
> **Synced**: 2026-09-01

## Overview

Fey operates in a nocturnal financial terminal aesthetic: deep matte-black canvas, a single typographic voice (calibre) doing all the heavy lifting, and chromatic color deployed as signal rather than decoration. The interface feels like a Bloomberg terminal redesigned by an Apple hardware team — data-dense product surfaces float on near-black, white type glows with AAA contrast, and orange/blue/green appear only where meaning demands attention (accented words, price direction, status pills). Components are built from generous 16px card radii and pill-shaped 99px controls, with soft black halos creating depth instead of hard elevation. The signature move is typographic: tight tracking on large display sizes (-0.08em) compresses confident statements into compact, premium-feeling headlines, while weight 400 does most of the work — there is no shouting, only calm authority. Every surface lives in the #0b0b0b→#191919 range, making any chromatic accent feel intentionally switched on.

## Color Palette

- **Fey White**: `#ffffff` — Primary text, decorative borders, hairlines — the dominant color of the system, used for typography and 554+ border occurrences [neutral]
- **Fey Ink**: `#0b0b0b` — Primary canvas and card surfaces — the near-black that everything floats on [neutral]
- **Fey Charcoal**: `#191919` — Elevated card surface, secondary panels — one step lighter than the canvas for nested depth [neutral]
- **Fey Obsidian**: `#131313` — Tertiary surface, input backgrounds, subtle elevated layers [neutral]
- **Fey Graphite**: `#868f97` — Muted secondary text, subdued borders, disabled labels — the workhorse mid-gray for everything that is not the headline [neutral]
- **Fey Mist**: `#cccccc` — Icon strokes, subtle links, tertiary borders — a step brighter than Graphite for elements that need more presence [neutral]
- **Fey Smoke**: `#525252` — Deep dividers, shadow-tinted borders, very low-emphasis strokes [neutral]
- **Fey Pale**: `#e6e6e6` — Subtle body borders, ghost button outlines, light strokes — the lightest non-white neutral [neutral]
- **Fey Ash**: `#999999` — Low-emphasis borders and secondary text — sits between Graphite and Smoke [neutral]
- **Fey Ember**: `#ffa16c` — Warm accent for highlighted headline words and warm gradient terminus — orange-on-black reads as urgency and premium warmth; Warm hero gradient — Ember fading into deep brown for product showcase atmosphere [accent]
- **Fey Signal**: `#479ffa` — Navigation underline, active link border, cool accent — vivid blue draws the eye to current location and trust indicators [accent]
- **Fey Growth**: `#4ebe96` — Green outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color [accent]
- **Fey Abyss**: `#000000` — Shadow base color, deepest possible background — used in 0.8-opacity halos and gradient termini [neutral]
- **Fey Frost**: `#b6d6ff` — Cool gradient accent — pale blue fading into slate for secondary product showcase [accent]
- **Fey Volt**: `#d6fe51` — Highlight gradient — electric yellow-green fading into deep olive for standout elements [accent]

## Typography

- **Calibre**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.5 |
| body | 14 | — | 1.5 |
| heading-sm | 18 | — | 1.32 |
| heading | 24 | — | 1.25 |
| heading-lg | 26 | — | 1.2 |
| display | 48 | — | 1.1 |
| display-lg | 54 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 18-24px
- **Element Gap**: 10-16px
- **Section Gap**: 64px
- **Border Radius**: {'cards': '16px', 'icons': '6px', 'small': '10px', 'buttons': '99px', 'featured': '275px'}

## Layout

Page model is centered max-width ~1200px on a full-bleed dark canvas. The hero is a full-width product showcase — a large device-framed dashboard mockup floats centered, with a two-line headline ('Make better investments.') left-aligned below. Navigation is a minimal top bar: logo left, 5 nav links center-left, a contextual pill ('Hey has joined Wealthsimple') plus a 'Learn more' button on the right. Sections alternate between full-width dark bands and centered constrained content. The Highlights section uses a left-aligned headline + description with right-aligned carousel arrows, followed by a horizontally scrollable row of 3 product cards. Vertical rhythm is generous: ~64px between sections, with sections feeling like discrete dark rooms. Card grids are always 3-up for feature showcases. Navigation patterns: top bar only — no sticky header, no sidebar. The dock section uses a centered dock component floating over a dramatic product image, with annotation text connected via dotted leader lines to the right.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Elevated**
- **Overlay**

**Shadow tokens:**

## Imagery

The site uses product UI mockups as its primary visual — not lifestyle photography, not abstract illustration, but actual screens of the Fey application rendered as floating cards. The hero shows a full stock-portfolio dashboard with charts, news feeds, and insider transactions. Feature cards show individual product surfaces (stock pages, insider lists, market-cap graphs). A second visual motif is a 3D-rendered rough stone/rock sculpture used as a backdrop for the dock navigation section, lit dramatically against black with warm orange/cool blue side lighting. Icon style is uniformly monoline outlined (1.5–2px stroke), white or Fey Mist on dark, used in nav, dock, and inline annotations. No stock photography of people; when faces appear they are circular avatar crops of public figures (Jensen Huang, Elon Musk, etc.) for insider-transaction cards. Overall density is image-dominant in the hero and feature sections, with whitespace carrying the rest.

## Design Principles

### Do

- Use 99px border-radius for all interactive controls (buttons, nav items, badges) — the pill shape is a load-bearing identity choice
- Set display headlines at 48–54px with -0.08em letter-spacing and Calibre 700 — this compressed tracking is the signature typographic move
- Use Fey Ink (#0b0b0b) as the primary canvas; layer Fey Charcoal (#191919) and Fey Obsidian (#131313) for nested card depth
- Apply chromatic accents (Ember orange, Signal blue, Growth green) only as meaning-carriers: highlighted words, status pills, price direction — never as decorative fills
- Use 16px border-radius for all content cards and product mockup surfaces
- Pair every dark surface with a heavy black shadow halo (rgba(0,0,0,0.8) 0px 0px 44px) to create the floating-in-space depth
- Default body text to Fey Graphite (#868f97) for secondary information; reserve pure white for headlines and primary values

### Don't

- Do not use filled chromatic buttons — Fey has no distinct CTA fill color; all actions are ghost or text-style on dark surfaces
- Do not introduce a secondary typeface — Calibre carries every role from 10px captions to 54px display
- Do not apply letter-spacing of 0 or positive values on display sizes — the negative tracking is essential to the premium compressed feel
- Do not use flat #000000 as the page background — always use Fey Ink (#0b0b0b) which is warmer and pairs better with the white type
- Do not use blue (#479ffa) for informational/semantic meaning — it is a navigation accent, not a status indicator
- Do not add more than one chromatic accent per headline or card — the restraint is what makes the color feel intentional
- Do not use heavy elevation (multi-layer drop shadows) — the system relies on a single deep black halo, not stacked shadows

## Components

### Pill Navigation Button

Fully rounded at 99px radius, transparent background, white text at 12–14px Calibre 500. Active state shows a Fey Signal (#479ffa) 1px bottom border. Inactive items sit in Fey Graphite (#868f97). No fill — the pill shape alone signals interactivity.

### Primary Action Button

99px border-radius, transparent or Fey Ink (#0b0b0b) background with subtle 1px shadow line, white text 12–14px Calibre 500. Glows with a soft white halo (rgba(255,255,255,0.25) 0px 0px 14px). Ghost-style — the button is defined by shape and light, not fill.

### Product Showcase Card

16px border-radius, Fey Charcoal (#191919) background, wrapped in a heavy black shadow halo (rgba(0,0,0,0.8) 0px 0px 44px). The card itself is dark; the shadow creates the illusion of it floating in space. Contains sub-product UI: charts, tickers, news feeds in miniature.

### Insider Transaction Card

16px border-radius, Fey Ink (#0b0b0b) or Fey Charcoal (#191919) surface. Left side: circular avatar. Center: name in white Calibre 600 + company in Fey Graphite. Right: Buy pill (Fey Growth #4ebe96 background, white text) or Sell pill (subtle red/gray). The color of the action pill is the only chromatic punctuation.

### Feature Section Card

275px border-radius on outer featured card for distinctive pill shape. Inner content: Calibre 400 body text in Fey Mist (#cccccc) on Fey Ink (#0b0b0b). Each card in the row gets a caption label below (e.g. 'Beautiful Stock and ETF pages') in Fey Graphite 12px.

### Dock Navigation Bar

Pill-shaped (99px radius) horizontal container with Fey Charcoal (#191919) background and 1px Fey Mist (#cccccc) border. Houses 7–8 monoline icons (home, compass, calendar, bookmark, mail, telescope, gear) plus a separated search button. Icons are white outlined strokes at ~20px. The dock floats over a product showcase image with a dotted leader line connecting to annotation text.

### Status Badge (Buy/Sell)

Small pill (99px radius) with colored background: Fey Growth (#4ebe96) for Buy, desaturated warm tone for Sell. White text 10–11px Calibre 500 uppercase. Minimal padding (4px 8px). The badge is the primary color carrier in a sea of monochrome.

### Ticker Display

Large white Calibre 700 at 48px for price values. Fey Growth green for positive change, desaturated red for negative. Portfolio name in Fey Graphite 11px caption above. Tighter tracking (-0.08em) on the large numbers makes them feel like real financial terminals.

### Section Headline

Calibre 700 at 48–54px, white, letter-spacing -0.08em, line-height 1.0–1.1. Centered or left-aligned. Period at end of short statements is deliberate punctuation. The extreme tightness of tracking is the signature — words feel compressed into a confident block.

### Highlighted Word

A single word in a headline rendered in Fey Ember (#ffa16c) or Fey Signal (#479ffa) instead of white. Creates a visual pulse — the eye is drawn to the colored word while the rest of the headline stays in white. Usage is sparing: one colored word per headline maximum.

### News Recap Card

Fey Charcoal (#191919) surface, 10px border-radius, contains: ticker badge (small Fey Growth-bordered tag), headline in Calibre 500 white 14px, summary in Fey Mist (#cccccc) 12px, timestamp in Fey Graphite 10px right-aligned. Ghost border on active/focused card.

### Carousel Navigation Arrow

Circular ghost button, Fey Ink (#0b0b0b) background, 1px Fey Mist (#cccccc) border, white chevron icon centered. ~40px diameter. Sits to the right of section content to scroll the feature card row.

## Similar Design Systems

- {'why': 'Dark-mode fintech with single-color accent signals (green for gains) and dense product-UI mockups in the hero — same terminal-adjacent aesthetic', 'business': 'Robinhood'}
- {'why': 'High-contrast white-on-black with chromatic price-direction indicators and compressed headline typography — Fey is the consumer-friendly descendant', 'business': 'Bloomberg Terminal'}
- {'why': 'Dark canvas, monoline icons, pill-shaped controls, and restrained chromatic accents used only for status — same philosophy of monochrome with strategic color', 'business': 'Linear'}
- {'why': 'Near-black surfaces, generous border-radius on cards, white type with tight tracking, and heavy black halos for depth on dark product mockups', 'business': 'Vercel'}
- {'why': 'Dark product-showcase aesthetic with floating UI cards, soft glow shadows, and a premium restrained palette punctuated by vivid accents', 'business': 'Arc Browser'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff (primary), #868f97 (secondary), #cccccc (tertiary)
- background: #0b0b0b (canvas), #191919 (card), #131313 (elevated)
- border: #868f97 (default), #cccccc (emphasis), #e6e6e6 (subtle)
- accent: #ffa16c (warm), #479ffa (cool), #4ebe96 (positive)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Pill Nav Button**: 99px border-radius, transparent background, text 12px Calibre 500 #868f97. Active state: 1px bottom border in #479ffa, text becomes #ffffff. No fill, no shadow.

2. **Product Showcase Card**: 16px border-radius, #191919 background, wrapped in shadow rgba(0,0,0,0.8) 0px 0px 44px. Contains a miniature dashboard UI with chart, ticker (48px Calibre 700 white), and Fey Growth green percentage change. Caption below: 12px Calibre 400 #868f97.

3. **Insider Transaction Row**: 16px border-radius card, #0b0b0b surface. Left: 48px circular avatar. Center: name 16px Calibre 600 #ffffff, company 12px Calibre 400 #868f97. Right: Buy pill — 99px radius, #4ebe96 background, white text 10px Calibre 500 uppercase.

4. **Section Headline**: 48px Calibre 700, #ffffff, letter-spacing -0.08em (-3.84px), line-height 1.1. One word optionally colored #ffa16c. Period at end of statement.

5. **Dock Navigation**: 99px border-radius pill, #191919 background, 1px #cccccc border. Contains 7 monoline icons (20px, #ffffff stroke) evenly spaced with 24px gaps. Separated search button at right. Floats over dark product image with dotted leader line to annotation text.
