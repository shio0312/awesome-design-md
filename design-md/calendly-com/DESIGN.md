# Calendly.com — Design System

> **North Star**: Navy ink on cool marble.
> **Theme**: light
> **Source**: https://calendly.com
> **Refero Style**: https://styles.refero.design/style/9946887b-ffa9-4276-af81-ae6352795afb
> **Synced**: 2026-09-01

## Overview

Calendly reads as a quiet, confident scheduling workspace: a near-white canvas with generous breathing room, crisp white product cards floating on cool stone-gray, and all typography rendered in deep navy ink rather than pure black. The defining move is the navy (#0b3558) used everywhere text appears — headings, buttons, icons, links — which softens the entire interface into something warmer and more editorial than a typical SaaS landing page. A single vivid blue (#006bff) carries every primary action, while decorative pink and cyan blobs bleed from behind product mockups to add warmth without clutter. Components stay restrained: thin 1px hairline borders, subtle blue-tinted shadows, generous 24px card radii, and 8px button corners that feel intentional rather than pill-soft.

## Color Palette

- **Ink Navy**: `#0b3558` — Primary text, headings, icons, dark CTA backgrounds, nav links [brand]
- **Signal Blue**: `#006bff` — Primary CTA fill, active nav, link accents, selected states [brand]
- **Slate Gray**: `#476788` — Secondary body copy, helper text, muted labels [neutral]
- **Mist Gray**: `#a6bbd1` — Disabled text, inactive feature labels, light icon strokes [neutral]
- **Cloud**: `#f8f9fb` — Page canvas, footer background, secondary surface [neutral]
- **Paper**: `#ffffff` — Card surfaces, elevated panels, button text on dark fills [neutral]
- **Pebble**: `#f0f3f8` — Badge backgrounds, input fills, subtle dividers, hover washes [neutral]
- **Hairline**: `#d4e0ed` — Card and input borders, dividers, link underline defaults [neutral]
- **Carbon**: `#0a0a0a` — Pure-black text fallback, logo glyph, icon fill [neutral]
- **Coral Magenta**: `#e55cff` — Decorative accent blob behind product cards — adds warmth without UI function [accent]
- **Sky Cyan**: `#0099ff` — Decorative accent blob behind product cards — pairs with magenta for gradient washes [accent]
- **Deep Cobalt**: `#004eba` — Badge text on Pebble fills, info labels [accent]

## Typography

- **Gilroy**
- **Gilroy**
- **Gilroy**
- **Gilroy**
- **Gilroy**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.4 |
| body | 16 | — | 1 |
| button | 18 | — | 1.6 |
| body-lg | 20 | — | 1.4 |
| subheading | 28 | — | 1.4 |
| heading-sm | 38 | — | 1.21 |
| heading | 50 | — | 1.2 |
| heading-lg | 68 | — | 1.2 |
| display | 80 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8-16px
- **Section Gap**: 48-64px
- **Border Radius**: {'cards': '24px', 'small': '4px', 'badges': '9999px', 'inputs': '8px', 'buttons': '8px', 'productCards': '16px'}

## Layout

Max-width 1200px centered, generous outer margins on desktop. Hero is a two-column split: left column holds the 80px headline + body copy + stacked sign-in buttons, right column holds the booking widget card backed by decorative blob shapes. Below the hero sits the trust logo strip as a single full-width band. Subsequent sections alternate between centered header blocks (H2 + subtext + optional CTA) followed by two-column feature blocks (text-left/product-right or product-left/text-right) with decorative accent blobs behind every product visual. Card grids are rare — the layout prefers side-by-side paired sections over multi-column grids. Section gaps are 48–64px. Navigation is a 64px sticky top bar with logo left, centered menu, and CTA cluster right.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Input Fill**
- **Dark Surface**
- **Accent Surface**

**Shadow tokens:**

## Imagery

Product screenshots are the primary visual — clean UI mockups of the booking calendar rendered on pure white cards with generous rounded corners. Decorative treatment: each product card is backed by a soft blob shape in Coral Magenta (#e55cff) or Sky Cyan (#0099ff), slightly offset and blurred, creating an editorial collage effect rather than a flat screenshot. No photography, no lifestyle imagery — all visuals are product UI, abstract accent shapes, or monochrome partner logos in the trust strip. Icons are line-style with 1.5–2px stroke weight, mono-tone in Ink Navy or Signal Blue.

## Design Principles

### Do

- Use Ink Navy #0b3558 for all text — never pure #000000, which breaks the system's warmth
- Use Signal Blue #006bff exclusively for filled primary CTAs; reserve Ink Navy for secondary dark buttons
- Set all card border-radius to 16px for product cards and 24px for feature panels
- Apply the three-layer blue-tinted shadow stack to any elevated surface above the canvas
- Use Gilroy weight 700 at 50–80px for hero and section headlines — undersized headings lose the page's editorial confidence
- Place every product visual in front of a Coral Magenta or Sky Cyan decorative blob offset by 20–40px
- Set buttons at 8px border-radius — not 4px (too sharp) and not pill (too soft) for this system

### Don't

- Don't use #000000 as a text color — always reach for Ink Navy #0b3558 or Slate Gray #476788
- Don't apply shadows with neutral black (rgba(0,0,0,...)) — all elevation must use the blue-tinted shadow base
- Don't use the decorative magenta/cyan blobs as fills for UI elements — they are atmosphere only, not functional color
- Don't create buttons with border-radius above 12px or below 4px — 8px is the system's sharp-but-soft sweet spot
- Don't set heading sizes below 38px for H2 or below 24px for H3 — the type scale skips small headings on purpose
- Don't use the badge color #004eba for CTAs — it reads as informational, not actionable
- Don't add gradients to backgrounds — the system is flat surfaces with shadow-based elevation only
- Don't pair the Signal Blue and Ink Navy CTAs on the same surface without enough spacing — they compete at close range

## Components

### Primary CTA Button

Background #006bff, text #ffffff at 18px weight 600, border-radius 8px, padding 6px 16px (compact) or 10px 16px (comfortable). No border. Used for "Sign up for free", "Get started", "Sign up with Google".

### Dark CTA Button

Background #0b3558, text #ffffff at 18px weight 600, border-radius 8px. Used for "Sign up with Microsoft" and "Get started" in the header.

### Ghost Text Link

Color #0b3558 at 14–18px weight 500–600, no background, no border, no padding. Underline optional on hover. Used for inline body links like "View all integrations", "Learn more".

### Outlined White Button

Color #ffffff, border 1px solid #ffffff, border-radius 4px, no background fill. Used over hero imagery or dark sections.

### Social Sign-In Button

Full-width pill with provider logo left, text right. Two variants: Google (white bg, #0b3558 text, 1px Hairline border) and Microsoft (Ink Navy bg, white text, no border). Padding 12px 16px, border-radius 8px.

### Elevated Product Card

Background #ffffff, border-radius 16px, padding 0px (image fills card). Three-layer blue-tinted shadow: rgba(71,103,136,0.04) 0 4px 5px, rgba(71,103,136,0.03) 0 8px 15px, rgba(71,103,136,0.08) 0 30px 50px. Often sits in front of a Coral Magenta or Sky Cyan decorative blob.

### Feature Accordion Item

Active item: heading #0b3558 at 18–20px weight 600 with #006bff icon; inactive items: heading #a6bbd1 at 16px weight 400. Left-aligned icon, right-aligned chevron. 1px Hairline divider below.

### Pill Badge

Background #e6f0ff (Pebble-tinted), text #004eba at 12px weight 500, border-radius 50px, padding 4px 8px. Examples: "Save 16%", "We're hiring!".

### Trust Logo Strip

Single row of monochrome partner logos (Compass, L'Oréal, Zendesk, Dropbox, Gong, Carnival, Indiana University) in #a6bbd1, evenly spaced, centered. No card, no border — logos float on the canvas.

### Booking Widget Card

Background #ffffff, border-radius 16px, internal padding 0px. Three columns: organizer info (avatar + name), date grid (calendar with selected date highlighted #006bff), time slots (pill buttons with active state in #006bff). Mimics the actual product.

### Section Header Block

H2 heading at 50–68px weight 700 in #0b3558, centered. Subtext at 16px weight 400 in #476788, centered, max-width ~640px. Optional CTA button below.

### Footer

Background #f8f9fb, padding 40px horizontal. Link columns in #0b3558 at 14px weight 500, headings at 12px weight 600 uppercase in #476788.

## Similar Design Systems

- {'why': 'Same Ink Navy text on near-white canvas, blue-tinted shadows, and single vivid blue primary action — both treat restraint as a feature', 'business': 'Linear'}
- {'why': 'Similar white-card-on-cool-gray layout, generous 16–24px radii, and navy/blue text palette that avoids pure black', 'business': 'Notion'}
- {'why': 'Same editorial heading sizes (50–80px bold), product-screenshot-in-front-of-colorful-blob hero treatment, and clean light-mode SaaS language', 'business': 'Loom'}
- {'why': 'Shares the white canvas + navy text + single electric blue accent, with decorative gradient shapes behind product visuals', 'business': 'Webflow'}

## Agent Prompt Guide

**Quick Color Reference**
- Text (primary): #0b3558
- Text (secondary): #476788
- Background (canvas): #f8f9fb
- Surface (card): #ffffff
- Border (hairline): #d4e0ed
- Accent (decorative): #e55cff / #0099ff
- primary action: #006bff (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #006bff background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. *Feature block (text-left)*: Section gap 64px. H2 at 50px Gilroy weight 700, color #0b3558, centered above. Left column: feature list with Ink Navy icons (#006bff for active item, #a6bbd1 for inactive). Right column: 16px-radius white card with booking widget UI, backed by a #0099ff blob.

3. *Pill badge*: Background #e6f0ff, text #004eba at 12px Gilroy weight 500, border-radius 50px, padding 4px 8px.

4. *Footer*: Background #f8f9fb, padding 40px horizontal. Column headings at 12px Gilroy weight 600 uppercase, color #476788. Links at 14px Gilroy weight 500, color #0b3558.

5. *Social sign-in button*: Full-width, 12px 16px padding, 8px radius. Google variant: white bg, #0b3558 text, 1px #d4e0ed border. Microsoft variant: #0b3558 bg, white text, no border.
