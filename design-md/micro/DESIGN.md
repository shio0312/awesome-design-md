# Micro — Design System

> **North Star**: sunrise over a digital meadow — a calm horizon gradient holding a quiet, ink-on-paper workspace beneath it.
> **Theme**: light
> **Source**: https://www.micro.so
> **Refero Style**: https://styles.refero.design/style/cc43cfe3-195b-4081-b586-c42db054a466
> **Synced**: 2026-09-01

## Overview

Micro is a sunrise productivity workspace: a chromatic blue-to-teal gradient sky opens the page, then drops into a quiet, neutral canvas of warm off-white with a near-black ink text color. The signature typographic move pairs a chunky editorial display face (perfectlyNineties) for oversized headlines with a neutral workhorse (haffer) for the dense product UI — giving marketing pages a magazine-cover gravity and product screens a calm, readable density. Color is used as functional punctuation: one azure blue (#518bdb) for actions, plus a pastel accent system (mint, peach, lavender, teal-mist) for soft surface washes and a small multicolor icon palette (teal, pink, red, orange, green) that signals connectivity and categories. Components are flat-first, bordered and gently shadowed rather than heavily elevated; radii cluster at 8px and 14px, with 18px for the larger product cards. The overall feel is a software product that has been allowed to breathe — open, friendly, slightly nostalgic in its display type, but precise in its data-rich product surfaces.

## Color Palette

- **Ink Black**: `#221f1c` — Primary text, dark CTA backgrounds, dark icon fills — warm near-black rather than neutral black keeps the palette from feeling clinical [neutral]
- **Paper White**: `#f5f5f5` — Page canvas, card backgrounds, subtle surface fills — the warm off-white that gives the product its paper-like base [neutral]
- **Pure White**: `#ffffff` — Elevated product card surfaces inside the app UI (inbox, context graph nodes) — one level above Paper White [neutral]
- **Stone Gray**: `#797267` — Secondary text, icon strokes, muted body copy — warm gray that stays in the same family as Ink Black [neutral]
- **Pebble**: `#8c8a88` — Tertiary text, disabled states, low-emphasis icons [neutral]
- **Slate Edge**: `#27272a` — Hairline borders on cards and inputs, subtle dividers [neutral]
- **Azure Action**: `#518bdb` — Primary action background, focused links, active states, key icon accents — the one chromatic CTA color, vivid enough to register against the warm neutrals; Hero background gradient (Azure Action → Teal Pulse, left to right in oklab) — the signature opening visual [brand]
- **Teal Pulse**: `#36bab8` — Teal text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Mint Wash**: `#cbfbf1` — Soft pastel surface tint for feature cards and highlight washes [accent]
- **Peach Wash**: `#f8ebd8` — Soft pastel surface tint, warm counterpart to Mint Wash [accent]
- **Lavender Wash**: `#ede9fe` — Soft pastel surface tint for alternate feature blocks [accent]
- **Teal Mist**: `#cff2ef` — Subtle teal-tinted surface, bridges brand teal and neutral canvas [accent]
- **Coral Marker**: `#ed6d68` — Red text accent for links, tags, and emphasized short phrases [accent]
- **Amber Marker**: `#e5a057` — Warm icon accent, category color in the multicolor icon palette [accent]
- **Orchid Marker**: `#bf89cd` — Purple-toned icon accent, category color, decorative node edges in the context graph [accent]
- **Forest Edge**: `#1a3a12` — Dark green border for the live-product mockup's edge treatment, deep botanical accent [accent]
- **Signal Green**: `#3a6b2a` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]
- **Live Lime**: `#7efa55` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]

## Typography

- **perfectlyNineties**
- **haffer**
- **ui-monospace**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| eyebrow | 10 | — | 1.4 |
| caption | 12 | — | 1.4 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.5 |
| heading-sm | 24 | — | 1.4 |
| heading | 30 | — | 1.25 |
| heading-lg | 48 | — | 1.2 |
| display | 72 | — | 1 |
| hero-mark | 96 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'pills': '9999px', 'inputs': '8px', 'buttons': '8px', 'nav-pills': '8px', 'large-cards': '18px', 'small-cards': '14px', 'feature-blocks': '18px'}

## Layout

Page is max-width ~1200px centered, with the hero breaking full-bleed for the gradient sky. The hero itself is a vertical stack: centered eyebrow pill, centered oversized display headline in perfectlyNineties, centered subhead in haffer, centered button pair, then the product mockup floating at the bottom edge, overlapping the transition to the white canvas below. Below the hero, sections follow a consistent rhythm: centered section H1, centered supporting copy, then content arranged in 2-column (text + visual) or 3-4 column card grids. The context graph section is the most distinctive layout — a wide horizontal data visualization that fills the content width, followed by a 4-column feature grid below it. Social proof is a single centered row of monochrome logos. Navigation is a top bar with a left-aligned wordmark, centered nav pills, and right-aligned auth buttons. The product UI itself, shown in screenshots, has a fixed left sidebar (~200px), a top utility bar, and a main content area — a classic 3-zone productivity app shell.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Pastel Wash**
- **Gradient Sky**

**Shadow tokens:**

## Imagery

Imagery is sparse and product-led: no lifestyle photography, no stock imagery. The hero is a full-bleed gradient sky over a green field, with a single floating product mockup that overlaps the horizon line — the product is the hero. Subsequent sections rely on large product UI screenshots (inbox, context graph) presented as floating cards with subtle shadows. The context graph is the most distinctive visual: a constellation of white data nodes connected by hairline lines, each node ringed in a different marker color, creating a network-as-illustration effect. Icons are multicolor line-and-fill marks in the brand palette. A small audio player widget (album art + transport) sits in the bottom-right corner as a persistent, almost decorative UI element. No 3D, no illustration system — the visual richness comes from data visualization and product UI itself.

## Design Principles

### Do

- Use the blue→teal gradient only on the hero; it is the single saturated viewport in the system and defines the brand opening
- Set hero and section display headlines in perfectlyNineties at 30-72px with 0.02em positive tracking — the open tracking is the signature
- Set body and product UI in haffer, not in the display face — the contrast between editorial and neutral is the typographic identity
- Use 8px radius for buttons, inputs, and nav; 14px for product rows; 18px for feature blocks and graph nodes — do not mix freely
- Keep product surfaces #ffffff with a 1px border and the subtle two-layer shadow — never heavy elevation
- Reach for the pastel washes (#cbfbf1, #f8ebd8, #ede9fe, #cff2ef) for marketing feature blocks; let the canvas stay #f5f5f5
- Color icons categorically with Teal Pulse, Coral Marker, Amber Marker, Orchid Marker, and Azure Action — never monochrome the icon set

### Don't

- Do not apply the gradient sky to anything other than the top of the page — repeating it kills the opening impact
- Do not use perfectlyNineties for body text, buttons, nav, or product UI — it is a display face only and will crush at small sizes
- Do not skip the 1px border on product cards — the system relies on hairline edges, not shadows, to define surfaces
- Do not use 4px radius on feature cards or marketing blocks — 4px is reserved for small chrome and icons, the card hierarchy starts at 8px
- Do not introduce new chromatic accents beyond the named marker palette — the multicolor icon system is closed
- Do not center body copy in the product UI — left-align data; the only centered text is the hero headline and section H1s
- Do not use pure black #000000 for text — use #221f1c Ink Black; the warm undertone is part of the paper-on-ink feel

## Components

### Dark Filled Button

Background #221f1c (Ink Black), text #ffffff, radius 8px, padding 10px 16px, haffer 500 at 14px, 1.4 line-height. Optional inset 0 -2px 0 0 rgba(0,0,0,0.2) for pressed state. Inverts to white-on-dark when used on the gradient hero.

### White Filled Button

Background #ffffff, text #221f1c, radius 8px, padding 10px 16px, haffer 500 at 14px. No border, no shadow — relies on the gradient backdrop for contrast.

### Ghost Text Button

Transparent background, text #221f1c (or #ffffff on dark), radius 8px, padding 8px 12px, haffer 500 at 14px. No visible border; relies on hover state to reveal affordance.

### Pill Nav Tab

Transparent background, text #221f1c haffer 500 14px, trailing 6px chevron icon in #797267, padding 6px 12px, radius 8px. Active state: #f5f5f5 fill. Lighter and more compact than buttons — nav reads as a row of whispers, not shouts.

### Product Card (App UI)

Background #ffffff, border 1px solid rgba(0,0,0,0.065), radius 14px, padding 12px 16px, haffer 400 at 14px for primary text and #797267 for secondary timestamps. Left-side avatar/initial in a 32px circle, optional unread dot in #518bdb.

### Context Graph Node

Background #ffffff, radius 18px, padding 16px, haffer 500-700 at 12-14px, a 2-3px accent border in one of the marker colors (Teal Pulse, Coral Marker, Orchid Marker, Azure Action). Connected by thin 1px lines in #797267 at 0.4 opacity. The accent border color is the categorical signal — same data shape, different domain.

### Soft Pastel Feature Block

Background one of the pastel washes (#cbfbf1, #f8ebd8, #ede9fe, #cff2ef), radius 18px, padding 32px, no border, no shadow. Headline in haffer 600 at 20-24px in #221f1c, supporting body in haffer 400 at 14px in #797267. The pastel fill IS the visual interest — no icons or illustrations needed inside.

### Search / Prompt Input

Background #ffffff, border 1px solid #27272a at low opacity, radius 8px, padding 10px 14px, haffer 400 at 14px, placeholder in #8c8a88. Focus state: 2px ring in #518bdb. Left-side icon (search or sparkle) in #797267, optional right-side mic icon.

### Sidebar Nav Item

Transparent background, 20px row height, 12px horizontal padding, radius 8px, 14px haffer 400 in #221f1c. Active state: #f5f5f5 fill, haffer 500 weight. Leading 16px icon in #797267 (active: #221f1c). Generous vertical breathing room — sidebar is quiet chrome, not a feature wall.

### Badge / Tag

Background transparent or #f5f5f5, text #221f1c, radius 9999px, padding 4px 10px, haffer 500 at 12px. For colored status: background in marker color at 0.15 opacity, text in the same marker color at full opacity. No border.

### Logo Strip

Single horizontal row, 5-6 monochrome logos in #221f1c, evenly spaced with 48-64px gap. Each logo is a simple geometric mark + wordmark at 18-20px haffer 600. No background card — logos float on the canvas.

### Floating Audio Player

Background #ffffff, radius 14px, shadow 0px 10px 15px -3px rgba(0,0,0,0.1), padding 8px 12px, 280-320px wide. 40px album art on left, track title in haffer 600 12px #221f1c, artist in haffer 400 10px #797267, transport controls on the right in #797267 with one accent (play) in #221f1c.

### Hero Product Mockup Container

No visible card chrome — the screenshot is presented edge-to-edge with a subtle 0px 10px 15px shadow, 18px corner radius, and a 1px #1a3a12 (Forest Edge) border that gives it a framed-on-the-meadow feel. The border color is the signature: it ties the product UI to the green ground beneath it.

### Section Eyebrow Pill

Background #ffffff at 0.9 opacity, radius 9999px, padding 4px 12px, haffer 500 at 12px in #221f1c, optional leading icon at 12px. Floats above the headline with 16px gap.

## Similar Design Systems

- {'why': 'Same warm off-white canvas with near-black ink text, product-led hero with a single bold headline, and a similar reliance on subtle 1px borders rather than heavy shadows', 'business': 'Notion'}
- {'why': 'Compact product UI density, dark filled primary buttons on light backgrounds, and a multicolor accent system used categorically across icons and tags', 'business': 'Linear'}
- {'why': 'Bold gradient hero paired with a quieter product surface below, and a willingness to use a distinctive display typeface (not just another geometric sans) for brand personality', 'business': 'Arc Browser'}
- {'why': 'Pastel-tinted feature blocks floating on a neutral canvas, with the product UI itself doing the visual heavy lifting rather than illustration or photography', 'business': 'Figma'}

## Agent Prompt Guide

Quick Color Reference:
- text: #221f1c (Ink Black)
- background: #f5f5f5 (Paper White)
- card surface: #ffffff
- border: #27272a (Slate Edge) at low opacity
- accent: #518bdb (Azure Action)
- primary action: #518bdb (filled action)

Example Component Prompts:

1. Create a hero section: full-bleed blue-to-teal gradient background (linear-gradient(to right, #518bdb, #36bab8)). Centered eyebrow pill (#ffffff at 0.9 opacity, 9999px radius, 12px haffer 500 #221f1c). Headline in perfectlyNineties 700 at 72px, #ffffff, letter-spacing 1.44px, line-height 1.0, reading 'One place for work that works for you'. Subhead in haffer 400 at 18px, #ffffff at 0.9 opacity, line-height 1.5. Button pair: dark filled 'Sign up' (#221f1c bg, #ffffff text, 8px radius, 10px 16px padding) and white filled 'Talk to sales' (#ffffff bg, #221f1c text, same shape). 32px gap between buttons.

2. Create a Primary Action Button: #518bdb background, #f5f5f5 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. Create a soft pastel feature block: background #cbfbf1 (or rotate through #f8ebd8, #ede9fe, #cff2ef), 18px radius, 32px padding, no border, no shadow. Headline in haffer 600 20px #221f1c, body in haffer 400 14px #797267. Icon optional, 24px, in #221f1c.

4. Create a context graph node: white background, 18px radius, 16px padding, 2px solid border in one marker color (Teal Pulse #36bab8, Coral Marker #ed6d68, or Azure Action #518bdb). Title in haffer 600 12px #221f1c, 2-3 metadata rows in haffer 400 11px #797267. Connect to other nodes with 1px lines in #797267 at 0.4 opacity.

5. Create a search input: white background, 1px border in rgba(0,0,0,0.1), 8px radius, 10px 14px padding, haffer 400 14px, placeholder in #8c8a88. Leading 16px search icon in #797267. Focus state: 2px ring in #518bdb.
