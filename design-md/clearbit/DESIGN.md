# Clearbit — Design System

> **North Star**: data observatory on cloud paper — a room-bright, near-acromatic canvas where midnight ink and a single blue current do all the work.
> **Theme**: light
> **Source**: https://clearbit.com
> **Refero Style**: https://styles.refero.design/style/6221ba67-26e7-4657-91b7-efd77cbb1f12
> **Synced**: 2026-09-01

## Overview

Clearbit reads as a blueprint rendered on white linen: an almost purely achromatic canvas where a single midnight-navy ink carries every word, and one electric blue fires only on actions. The interface floats — product cards, data records, score badges — suspended on a barely-there lavender wash that whispers data-warehouse more than SaaS-template. Typography is InterVar at its most restrained: generous weight range but headlines carry the same navy as body, so hierarchy comes from size and tracking, not color. The product IS the hero: screenshots of company profiles, enrichment tables, and scoring chips do the talking that stock photography would in a less confident design. Components are flat, thin-bordered, and soft-cornered; the only shadow in the system is a deep-blue focus ring, not a drop shadow — elevation is expressed through layering on subtle background tints, not through depth.

## Color Palette

- **Midnight Ink**: `#091135` — Primary text, headings, nav, body, link color — the dominant ink of the entire interface, set against white and pale-lavender surfaces [brand]
- **Electric Blue**: `#0f77ff` — Blue outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color [brand]
- **Cobalt Surface**: `#127ee3` — Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color [brand]
- **Slate**: `#36394a` — Secondary muted text where Midnight Ink would be too heavy — metadata, timestamps, helper copy [neutral]
- **Frost Border**: `#e1e9f0` — Hairline borders on cards, inputs, dividers, and table edges — the structural line color of the entire system [neutral]
- **Mist**: `#b1bbcd` — Soft shadow tone and secondary neutral — used in focus glows and deeper dividers [neutral]
- **Graphite**: `#000000` — Icon fills, deep dividers, and absolute-dark accents — used sparingly where Midnight Ink still feels too soft [neutral]
- **Paper**: `#ffffff` — Page canvas, card surfaces on tinted sections, text on dark buttons [neutral]
- **Lavender Wash**: `#f5f3ff` — Section background tint that signals content zones — the softest product-surface elevation above the white canvas [neutral]

## Typography

- **InterVar**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.5 |
| heading-sm | 32 | — | 1.25 |
| heading | 56 | — | 1.25 |
| display | 64 | — | 1.25 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8-20px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '9999px', 'cards': '12px', 'inputs': '8px', 'buttons': '8px'}

## Layout

Max-width ~1200px centered container, full-bleed sections that alternate between pure white and Lavender Wash. The hero is a centered text stack (display headline → body subhead → centered logo row) with no image. Below the fold, the rhythm shifts to alternating two-column sections: text-left / floating-product-card-right, then text-right / floating-product-card-left, creating a Z-pattern. Each product card is tilted slightly or offset to feel suspended, not gridded. The nav is a minimal top bar (logo left, single filled blue CTA right, no menu items visible). Section gaps are generous (64px), intra-section element gaps tight (8–20px). No sidebar, no mega-menu, no footer visible in the data — the page is deliberately front-loaded.

## Surfaces / Elevation

- **Paper**
- **Lavender Wash**
- **Card**
- **Cobalt Surface**

**Shadow tokens:**

## Imagery

Imagery is product-screenshot-as-hero — the page shows the actual product UI (enrichment tables with Type/Industry/Parent columns, Slack data records with 4 attribute rows, PayPay company cards with red brand marks) floating on soft Lavender Wash backgrounds. No stock photography, no abstract 3D renders, no lifestyle imagery. The visual language is documentary: the product proves itself by being visible. Brand logos inside mockups retain their original colors (Slack's 4-color mark, PayPay's red), which is the one place the system permits chromatic freedom — but only inside the product's own frame. Iconography is minimal and geometric: Electric Blue checkmarks, simple outline arrows, a 'C' notch logomark.

## Design Principles

### Do

- Use Midnight Ink (#091135) for all primary text and headings — never let body color drift to true black for long passages
- Reserve Electric Blue (#0f77ff / #127ee3) exclusively for primary actions, focus rings, and check icons — one signal per screen
- Express section separation through Lavender Wash (#f5f3ff) backgrounds and Frost Border (#e1e9f0) hairlines, never through drop shadows
- Set headings in InterVar weight 500–600 at 32/56/64px with 0.016–0.018em tracking — the widened tracking is the signature, don't tighten it
- Use 12px radius for all cards and 8px for buttons, inputs, and nav elements — the 4px gap between these two radii is deliberate
- Show the product in hero zones: float real UI mockups (data tables, score chips, enrichment rows) on Lavender Wash instead of abstract illustrations
- Keep section vertical rhythm at 64px between major zones, 20–24px between headline and subhead, 8px between metadata lines

### Don't

- Don't add drop shadows to resting cards or panels — the system uses surface tinting and hairline borders for depth, not shadow stacks
- Don't introduce a second accent color — the entire chromatic budget is one blue, applied sparingly
- Don't use negative letter-spacing on display type — the system intentionally opens tracking as size increases
- Don't set body text below 14px or use weight 700 for anything longer than a single word — weight 400–500 carries the voice
- Don't use pure black (#000000) for long-form text — Midnight Ink (#091135) is the ink, black is reserved for icon fills
- Don't break the radius scale — cards at 12px, buttons/inputs at 8px, tags at 9999px; no intermediate values like 10px or 16px
- Don't use heavy gradients or decorative backgrounds — the system is flat; the only gradient language is the subtle Lavender Wash zone transitions

## Components

### Top Navigation Bar

Full-width white bar, 8px vertical padding, logo left in Midnight Ink with a pale-blue logomark, CTA right. No visible border-bottom — floats on white canvas.

### Primary Action Button (Filled)

Cobalt Surface (#127ee3) background, white text, 8px radius, InterVar 500 at 16px, 12px vertical / 20px horizontal padding, white text color. On focus: Electric Blue 1px ring with deep-blue shadow stack.

### Outlined Ghost Button

Transparent fill, Frost Border (#e1e9f0) 1px stroke, 8px radius, Midnight Ink text, same padding as filled button. Restrained — the eye should land on the filled blue first.

### Hero Headline Block

Display weight (64px) or Heading (56px) InterVar, Midnight Ink, letter-spacing 0.018em, centered alignment. Subhead in body 18px Slate. No background, floats on white.

### Product Showcase Card

White card, 12px radius, Frost Border 1px, 24px padding, no shadow. Contains tabular data, attribute rows, or brand logos. The card IS the visual — minimal chrome around it.

### Data Record Row

16px InterVar, Slate (#36394a) label left-aligned, Midnight Ink value right-aligned, 12px vertical row gap, Electric Blue checkmark icons in the leading column. No dividers between rows.

### Section Tag / Eyebrow

InterVar 14px weight 500, Midnight Ink, letter-spacing 0.004em. Often sits as plain text rather than a pill, directly above the section heading.

### Pill Badge (Lavender)

Lavender Wash (#f5f3ff) background, Midnight Ink text at 14px weight 500, 9999px radius, 8px vertical / 16px horizontal padding. Soft, non-urgent.

### Score Indicator Badge

White circle ~40px diameter, Frost Border 1px, Electric Blue numeric text at 18px weight 600, slight shadow. Sits as a corner anchor on the parent card.

### Brand Logo Lockup Card

White surface, brand logo left, attribute table right, no border around the brand mark itself. The Slack card uses a 4-color Slack mark; the PayPay card uses a red square mark — brand color is allowed only inside these mockups.

### Data Table / Record Card (PayPay style)

White card, 12px radius, 24px padding, two-column attribute grid with Slate labels and Midnight Ink values, red brand mark anchored top-left, soft red CTA button bottom-left.

### Lavender Section Background

Lavender Wash (#f5f3ff) fills the section, product cards float white on top. Soft top/bottom transition into white — no hard borders between sections.

### Logo Mark (Clearbit)

Pale-blue rounded square containing a white 'C' notch, paired with Midnight Ink wordmark 'Clearbit' at 18px weight 600 and a smaller 'by HubSpot' subtitle in Slate.

## Similar Design Systems

- {'why': 'Same near-achromatic light canvas with deep-navy text, generous Inter-style typography, and product UI screenshots as hero visuals — the blueprint-on-white feel', 'business': 'Stripe'}
- {'why': 'Equally flat, shadowless interface with a single vivid accent and hairline borders — though Linear is dark-mode, the surface logic and restraint match', 'business': 'Linear'}
- {'why': 'Fellow data-infrastructure B2B with a white canvas, single blue accent, and product-screenshot-as-marketing — the data-terminal vocabulary is shared', 'business': 'Segment'}
- {'why': 'Light airy product page with centered hero, generous 64px section gaps, and product UI floating on subtle tinted backgrounds', 'business': 'Vercel'}
- {'why': 'Data-platform B2B with a similarly restrained achromatic palette, single accent color, and documentary product imagery rather than abstract graphics', 'business': 'Plaid'}

## Agent Prompt Guide

Quick Color Reference:
- text (primary): #091135 Midnight Ink
- text (secondary): #36394a Slate
- background (canvas): #ffffff Paper
- background (section): #f5f3ff Lavender Wash
- border: #e1e9f0 Frost Border
- accent: #0f77ff Electric Blue
- primary action: no distinct CTA color

Example Component Prompts:
1. Build a hero section: #ffffff background, centered 56px InterVar weight 600 #091135 headline with 0.018em letter-spacing, 18px InterVar weight 400 #36394a subhead at 1.5 line-height, 20px gap between headline and subhead.
2. Create a product showcase card: 12px radius, 24px padding, white surface on a #f5f3ff section background, 1px #e1e9f0 border, no shadow. Inside: a two-column data table with 14px #36394a labels left and 14px #091135 values right, 12px row gap, Electric Blue #0f77ff checkmark icons in the leading column.
3. Add a pill section tag: #f5f3ff background, 9999px radius, 8px 16px padding, 14px InterVar weight 500 #091135 text. Sits directly above the section heading with 8px gap.
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
5. Compose a two-column feature section: text left (32px InterVar weight 600 #091135 heading, 16px #36394a body, 24px gap between), floating white product card right with 12px radius, 1px #e1e9f0 border, slightly offset from the baseline to feel suspended on the #f5f3ff section wash.
