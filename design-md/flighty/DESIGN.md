# Flighty — Design System

> **North Star**: Control tower at midnight — a luminous control room with glowing screens floating around a single device
> **Theme**: mixed
> **Source**: https://flighty.com
> **Refero Style**: https://styles.refero.design/style/0d0de64c-1891-4984-9e12-8976e042ce11
> **Synced**: 2026-09-01

## Overview

Flighty is a departure-board-meets-control-tower: the upper page reads as a crisp white airport information panel, then the page drops into a deep midnight-violet control room with glowing screens in the dark. The palette is overwhelmingly achromatic, with one vivid blue (#007bff) reserved for actions and one amber-yellow (#f7be00) for the download conversion — a signal-light system against the dark and light surfaces. Typography is confident and heavy: a 56px display headline with tight -0.025em tracking that lands like a gate-change announcement, supported by compact system-ui body text. The signature element is the phone mockup surrounded by floating notification cards — soft, shadowed, slightly tilted cards showing real-time flight data (delays, gate changes, check-in opens) that orbit the device and make the product feel alive rather than static. Surfaces are nearly flat with ultra-low-opacity shadows (0.02–0.04) and hairline borders, so depth comes from layering and the page's light-to-dark transition, not from heavy drop shadows.

## Color Palette

- **Signal Blue**: `#007bff` — Primary action button fill, active link states, focus indicators — the single chromatic action color in an otherwise achromatic system [brand]
- **Amber Alert**: `#f7be00` — Download CTA, high-priority callouts, notification accents — warm yellow against dark surfaces for the conversion moment [accent]
- **Deep Indigo**: `#0d0021` — Dark section backgrounds, announcement bar, hero gradient base — the midnight-violet that makes screens glow [brand]
- **Midnight Ink**: `#05010d` — Dark card surfaces, deepest background layer — near-black with a violet undertone [neutral]
- **Pure White**: `#ffffff` — Light canvas, notification card surfaces, text on dark — the dominant surface color in the upper page [neutral]
- **Pure Black**: `#000000` — Primary text, icon strokes, hairline borders, ghost button fills — the structural ink of the system [neutral]
- **Carbon**: `#333333` — Secondary text, subdued body copy — reads softer than pure black for paragraph-length content [neutral]
- **Slate**: `#595959` — Tertiary text, metadata, timestamps in notification cards [neutral]
- **Steel**: `#737373` — Muted body text, disabled states, inactive nav items [neutral]
- **Fog**: `#808080` — Placeholder text, dimmed labels, low-priority metadata [neutral]
- **Silver**: `#cfcfcf` — Hairline borders, card outlines, subtle dividers, very light surface tint [neutral]
- **Linen**: `#faf8f7` — Warm off-white surface — alternate card background, subtle tonal shift from pure white [neutral]
- **Ash**: `#89898e` — Cool gray for pressed states and slightly cooler text — the only neutral with a slight blue cast [neutral]
- **Alert Red**: `#d92d20` — Red outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color [accent]

## Typography

- **sans-serif**
- **system-ui**
- **EB Garamond**
- **SF Pro Text Regular**
- **SF Pro Text Semibold**
- **Inter**
- **Indie Flower**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.2 |
| heading-sm | 22 | — | 1.38 |
| heading | 32 | — | 1.1 |
| display | 56 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 20px
- **Element Gap**: 10px
- **Section Gap**: 64-80px
- **Border Radius**: {'nav': '999px', 'tags': '999px', 'cards': '16px', 'icons': '999px', 'inputs': '12px', 'buttons': '999px', 'floatingCards': '20px'}

## Layout

The page is a scrolling narrative that alternates between two surface modes: a light departure-board mode (white canvas, centered content) and a dark control-room mode (#0d0021 canvas, centered content). The hero is full-width white with a centered headline stack, centered subtext, centered award badges, and a large phone mockup flanked by scattered notification cards. Sections are separated by seamless background-color transitions rather than visible dividers. Content is consistently center-aligned on a max-width ~1200px column. The dark section features a phone-in-hand at scale, then transitions to a press-logo grid (4 columns × 2 rows) followed by a left-aligned text block. Navigation is a floating pill at the top, not a full-width bar. The rhythm is: white hero → dark product showcase → dark press credibility → dark text closer. There are no sidebar or multi-column layouts — everything is single-column, centered, with the product imagery providing the only lateral content.

## Surfaces / Elevation

- **Light Canvas**
- **Linen Card**
- **Silver Divider**
- **Deep Indigo**
- **Midnight Ink**

**Shadow tokens:**

## Imagery

Product photography dominates: a large realistic phone render held in a human hand, photographed in natural light with visible skin texture and finger positioning — the hand is not staged flat, it has grip and dimensionality. Around the phone, floating UI notification cards (rendered, not photographed) orbit the device at slight angles, showing real flight data: gate changes, check-in openings, delay alerts, landing confirmations. No lifestyle photography of airports, planes, or travelers. The press section uses monochrome logo marks (CNBC, CNN, Fox News, WSJ, Inc., Business Insider, TechCrunch, The Verge) rendered in white/light gray on dark cards — no brand-color treatment. The visual language is product-first: the app and its data ARE the imagery, not supplementary decoration.

## Design Principles

### Do

- Use system-ui at 400-700 weights — never introduce a custom sans-serif for body or UI text
- Set display headlines at 56px system-ui 700 with -1.4px letter-spacing and line-height 1.00 — the tight tracking and full line-height are the announcement-board voice
- Use #007bff only for the single most important action on any given surface — never for decoration, tags, or secondary buttons
- Use #f7be00 exclusively for the download conversion moment — pair it with a download icon and dark surroundings for maximum signal
- Apply 999px radius to all buttons, tags, nav elements, and icon containers — the pill shape is the system default, not an option
- Position notification cards at slight rotations (-3° to +3°) around product mockups with 20px radius and whisper-thin shadows to create the scattered, real-time feel
- Transition between light and dark sections seamlessly — use #0d0021 as the dark canvas and keep the same type scale; only swap the color token

### Don't

- Don't add drop shadows heavier than the 0.02-0.04 opacity system — heavy shadows break the flat, departure-board aesthetic
- Don't use #007bff or #f7be00 for text, borders, or backgrounds other than their specific action roles — these are signal colors, not brand washes
- Don't introduce a second sans-serif typeface — system-ui covers the full range from caption to display
- Don't use sharp corners (0-4px radius) on cards, buttons, or containers — the minimum card radius in this system is 8px, the default is 16-20px
- Don't place colored borders or backgrounds on body text — keep #000 or #333 for text on light, #fff or #cfcfcf on dark
- Don't crowd sections — even with compact density, maintain 64-80px section gaps to let the large headlines breathe
- Don't use the #d92d20 red decoratively — it is a functional alert color for cancellations and critical delays, nothing else

## Components

### Announcement Bar

Full-width bar with #0d0021 (Deep Indigo) background, white text at 13px system-ui 500, centered content with a small icon (lightbulb) and a 'View Live →' link. Padding approximately 8px vertical. Optional close button on the right. This bar announces live features or news and uses the dark-indigo to set the control-room tone before the white page begins.

### Floating Navigation Pill

Single rounded pill (999px radius) floating on the page with subtle shadow stack. Contains the ✈ logo mark, menu items (Pricing, Gift Cards, Passport, Airports, Help Center) in 15px system-ui 500 #000, and a 'Get the app' ghost button on the right. The pill itself has a white or very-light background with 1px border. Padding 8px vertical, 12-16px horizontal inside the pill. The pill form — rather than a full-width bar — is the signature: the nav sits on the page like a control device, not a structural element.

### Ghost App Button (nav)

Inside the nav pill: transparent background, #000 text, 1px border in #000 at 50% opacity, 999px radius, 8px 16px padding. Includes a small phone icon. This is the quiet 'get the app' prompt that lives inside the nav.

### Primary Blue Button

Filled #007bff background, white text, 999px radius, 12px 24px padding, 15px system-ui 600. No border. The only chromatic filled button in the system — used sparingly for the most important action on a given page.

### Amber Download Button

Filled #f7be00 background, #000 text, 999px radius, 12px 24px padding, 15px system-ui 600 with a download icon. Appears at key conversion moments (hero floating, dark section). The yellow-against-dark contrast makes it the most attention-grabbing element on dark backgrounds.

### Dark Ghost Button

Transparent or #05010d background, white text, 1px white-at-low-opacity border, 999px radius, 12px 24px padding, 15px system-ui 500 with a phone icon. Used alongside the Amber Download button in the dark section as the quieter companion action.

### Display Headline

56px system-ui 700, -1.4px letter-spacing, line-height 1.00, color #000 on light surfaces or #fff on dark. Sentence-case or title-case. The tight tracking and full line-height-to-font-size ratio make the headline feel like one block of type rather than wrapped text — like a gate-change announcement.

### Section Subheadline

17px system-ui 400, -0.17px tracking, line-height 1.50, color #333 (Carbon) on light or #cfcfcf on dark. Centered or left-aligned. Generous line-height gives it a reading-optimized feel despite the compact density of surrounding UI.

### Award Badge Pair

Horizontal pair of small pill-shaped badges, each ~40px tall with 999px radius. Left badge: white background, black text 'Apple Design Award · Winner 2023' with a small Apple logo icon. Right badge: blue gradient or solid blue background, white text 'App of the Year · Finalist 2023' with a small App Store icon. Sized as supporting evidence, not as primary content.

### Phone Mockup Frame

Large central element holding a realistic phone render showing the Flighty app interface. The phone sits in a realistic hand photograph with natural skin tones. The frame itself has no border or shadow — the photographic context provides all the depth. Sized at roughly 350-400px wide on desktop.

### Floating Notification Card

The signature component. White (#ffffff) background, 20px border-radius, subtle multi-layer shadow at 0.02-0.04 opacity, 16px padding. Contains: a small icon or avatar (24-32px), a bold 15px headline in #000 ('Mom landed in New York', 'Check in is now open'), and muted 13px metadata in #737373 ('6:32am (22m early) and ↓ 88°', 'You can check-in at delta.com'). Cards are positioned around the phone at slight rotations (-3° to +3°) to feel scattered, not gridded. Some cards use a left border accent in #007bff, #d92d20, or #f7be00 to indicate status.

### Press Logo Card

Each press logo sits in a #05010d or near-black card with 1px white-at-8% border, 12px or 16px border-radius, generous internal padding (40-60px vertical). Logo marks are rendered in white or light gray at ~60% opacity. Arranged in a 4-column grid (4×2) with 10-16px gaps. The cards are flat — no shadows — so they read as tiles on the dark surface, not as floating elements.

### Section Divider Band

Full-width bands that shift the page from white canvas to #0d0021 Deep Indigo. No hard border — the transition is seamless, using the deep-indigo background to envelop the next section. Headlines within these bands switch to white at the same 56px / 32px scale, maintaining typographic continuity across the theme change.

## Similar Design Systems

- {'why': 'Same hero-with-headline-over-product pattern, same light-to-product-showcase rhythm, same heavy display typography with tight tracking', 'business': 'Apple Product Pages'}
- {'why': 'Same app-in-hand photography style with product UI rendered around the device, same restrained color palette with one accent for action', 'business': 'Things 3 (Cultured Code)'}
- {'why': 'Same compact density, same preference for hairline borders over heavy shadows, same system-font typography approach with tight letter-spacing on display sizes', 'business': 'Linear'}
- {'why': 'Same floating UI elements orbiting a central product, same playful scattering of notification-like cards, same dark-mode depth with glowing accent colors', 'business': 'Arc Browser'}
- {'why': 'Same minimal navigation (floating pill rather than full bar), same transition from light marketing surface to dark product surface, same ultra-subtle shadow approach', 'business': 'Vercel'}

## Agent Prompt Guide

**Quick Color Reference**
- text (primary): #000000
- text (secondary): #333333
- background (light): #ffffff
- background (dark): #0d0021
- border: #cfcfcf (light) / rgba(255,255,255,0.08) (dark)
- accent: #f7be00
- primary action: #007bff (filled action)

**Example Component Prompts**
1. Create a hero section: #ffffff background. Headline at 56px system-ui weight 700, #000000, letter-spacing -1.4px, line-height 1.00. Subtext at 17px system-ui weight 400, #333333, letter-spacing -0.17px, line-height 1.50, centered. Amber Download button (#f7be00 fill, #000 text, 999px radius, 12px 24px padding, 15px system-ui weight 600) with a download icon.
2. Create a floating notification card: #ffffff background, 20px border-radius, 16px padding, whisper-thin shadow stack (0.02-0.04 opacity layers). Bold 15px system-ui weight 600 #000000 headline, muted 13px system-ui weight 400 #737373 metadata below, optional 3px left border in #007bff or #d92d20 for status.
3. Create a press logo grid: 4-column grid on #0d0021 background, 10-16px gaps. Each logo sits in a #05010d card with 1px rgba(255,255,255,0.08) border, 16px border-radius, 40-60px vertical padding, logo rendered in white at ~60% opacity.
4. Create a dark section headline: 56px system-ui weight 700 #ffffff on #0d0021 background, letter-spacing -1.4px, line-height 1.00, centered. Subtext at 17px system-ui weight 400 #cfcfcf, line-height 1.50, centered.
5. Create a floating navigation pill: #ffffff background, 999px radius, 8px 16px internal padding, subtle shadow stack. Logo mark on left, menu items (15px system-ui weight 500 #000) in the center, ghost 'Get the app' button (transparent fill, 1px #000-at-50% border, 999px radius, phone icon) on the right.

## Gradient System

Two gradients define the dark-mode atmosphere: a diagonal indigo-to-near-black wash (linear-gradient(171deg, rgb(97,97,112) -45%, rgb(18,18,140) 69%)) for subtle surface modulation, and a radial deep-violet pulse (linear-gradient(180deg, rgb(18,0,54) 0%, rgb(37,1,96) 51%, rgb(18,0,54) 100%)) that creates a glowing centerpoint behind the phone mockup in dark sections. Gradients are atmospheric, not decorative — they should suggest light emanating from a screen, not be visible as gradient patterns.
