# Ventriloc — Design System

> **North Star**: Editorial data observatory on warm paper — a single orange ember punctuating monochrome precision.
> **Theme**: light
> **Source**: https://ventriloc.ca/en
> **Refero Style**: https://styles.refero.design/style/f99aca3e-5289-4595-a7cc-77a72052f4b8
> **Synced**: 2026-09-01

## Overview

Ventriloc speaks in a quiet, editorial voice: warm paper-white canvas, monospaced-precision data cards, and a single orange ember that punctuates the monochrome like a highlighter on a printed report. The system pairs a custom neo-grotesque (PolySans) at weight 400 for headings — unusual restraint that trades authority-through-volume for authority-through-precision — against Inter for body and UI chrome. Surfaces are warm grays and ivory rather than cool tech-blue, cards wear asymmetric corner radii (sharp top-right, soft elsewhere), and interactive elements split into two clear dialects: sharp-cornered text-style buttons and pill-shaped navigation containers. Color is rationed: pages should read 95% achromatic with orange appearing only as functional punctuation for highlights, link underlines, and decorative data accents.

## Color Palette

- **Graphite**: `#202020` — Primary text, headings, nav links, icon strokes — the typographic anchor of every surface [neutral]
- **Canvas White**: `#ffffff` — Page background, card elevation, icon fills — the brightest surface in the system [neutral]
- **Ash**: `#efefef` — Primary card and section background, nav pill container — the dominant warm-gray surface [neutral]
- **Fog**: `#f5f5f5` — Subtle background tone for nested surfaces and secondary containers [neutral]
- **Ivory**: `#ebe6dd` — Warm accent background wash for featured blocks — the paper-stock feel [neutral]
- **Steel**: `#4d4d4d` — Secondary body text, long-form paragraph copy [neutral]
- **Slate**: `#828282` — Muted helper text, tertiary nav items, inactive controls [neutral]
- **Mist**: `#e8e8e8` — Hairline dividers, nav background fills [neutral]
- **Ember Orange**: `#ff682c` — Orange text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Brass**: `#816729` — Secondary accent for chart strokes, decorative SVG lines, and tag text — a muted warm counterpoint to Ember [accent]

## Typography

- **PolySans**
- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.43 |
| subheading | 18 | — | 1.25 |
| heading | 32 | — | 1.19 |
| heading-lg | 40 | — | 1.2 |
| display | 66 | — | 0.91 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 40px
- **Element Gap**: 20px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '20px', 'cards': '8px', 'buttons': '0px', 'nav-pills': '200px', 'asymmetric-card': '6px 0px 0px'}

## Layout

Max-width 1200px centered container with generous 80px section gaps. The hero is a two-column split: left side holds the headline, subtext, and dual-button CTA stack; right side shows a cluster of three overlapping data dashboard cards (finance chart, revenue stat, profitability ring) floating on the white canvas. Below the hero, a full-width partner logo strip on white. Subsequent sections alternate between Ash (#efefef) and white bands. Navigation is a floating pill container centered in the header, with the brand wordmark left-aligned and a dark Contact-us button right-aligned. The overall rhythm is spacious and editorial — wide margins, tall sections, and the data cards as the only visual punctuation beyond typography.

## Surfaces / Elevation

- **Page Canvas**
- **Ash Surface**
- **Fog Surface**
- **Ivory Surface**

**Shadow tokens:**

## Imagery

Visuals are almost entirely data-driven: chart widgets (line graphs, circular progress indicators, stat cards) rendered in a flat, minimal style with thin strokes in Ember Orange and Brass against white card surfaces. No lifestyle photography, no stock imagery, no hero illustrations. The only photographic content is partner/client logos presented in monochrome Graphite. The visual language is closer to a printed annual report than a typical SaaS site — the charts ARE the imagery. Icons are thin-stroke, monoline, and Graphite-colored, appearing sparingly in nav and card headers.

## Design Principles

### Do

- Use PolySans exclusively at weight 400 for all headings — never bold the display type; the whisper-weight is the signature
- Apply the asymmetric border-radius 6px 0px 0px to featured content cards; reserve 20px radius for data widgets and 0px for buttons
- Keep pages 95% achromatic; let Ember Orange (#ff682c) appear only as link underlines, chart highlights, and small icon accents
- Use 20px for element gaps and 80px between sections — the generous whitespace is what makes the editorial voice work
- Pair Inter for all body and UI text; PolySans for headings, nav items, and button labels only
- Separate sections by alternating white canvas and Ash (#efefef) surface bands rather than dividers or shadows
- Use letter-spacing -0.02em on every PolySans text element — it's baked into the font's identity

### Don't

- Do not bold PolySans headings — weight 400 at large size is the whole point; bolding destroys the editorial restraint
- Do not use Ember Orange as a filled button background — it is an accent for highlights and links, not a CTA fill
- Do not add box-shadows to cards or buttons — depth comes from surface color contrast, not elevation
- Do not use symmetric border-radius on all elements; the asymmetric 6px 0px 0px and the 0px button radius are deliberate contrast
- Do not introduce blue, green, or other chromatic colors — the two-warm-accent system (Ember + Brass) is the limit
- Do not set line-height above 1.25 on display headings; the 0.91 leading on 66px creates the tight, poster-like headline
- Do not crowd the layout — if you need to add decoration, increase whitespace instead

## Components

### Primary CTA Button

Dark filled (Graphite #202020 background, white text), sharp 0px corners, PolySans 16px weight 400, padding 10px 20px, letter-spacing -0.02em. No shadow, no border-radius — the square edge is deliberate contrast to the rounded cards

### Ghost Outlined Button

Transparent background, 1px Graphite border, Graphite text, 0px radius, padding 10px 20px, PolySans 16px weight 400. Sits beside the primary CTA as a quieter alternative

### Navigation Pill Container

Ash (#efefef) background, 200px border-radius (fully pill-shaped), 8px vertical padding, 18px horizontal padding, wraps dropdown-trigger links. PolySans 16px for items inside

### Language Toggle Link

Plain text link in Slate (#828282), PolySans 16px, no background or border. Sits inline with nav items

### Asymmetric Radius Card

Ash (#efefef) background, border-radius 6px 0px 0px (soft top-left, sharp everywhere else), generous internal padding (70px top, 60px left). This asymmetric radius is the signature card shape — no shadow, surface color does the lifting

### Data Dashboard Card

White (#ffffff) surface, 20px border-radius, thin border or no border, contains revenue/profitability charts with Ember Orange and Brass accent strokes. No shadow — floats on the Ash page background

### Hero Headline Block

PolySans 66px weight 400, line-height 0.91, letter-spacing -1.32px, Graphite color. Followed by 18px Inter body text in Steel (#4d4d4d). No background — sits directly on white canvas

### Partner Logo Strip

Row of monochrome (Graphite) partner logos on white canvas, separated by generous horizontal spacing (~20px gap), with a "Trusted by 80+ partners" caption in PolySans 13px Brass color above

### Text-Style Nav Link

Graphite (#202020) text, PolySans 16px weight 400, with a small chevron icon. No underline by default, no background — active state may show a subtle color shift

### Link with Orange Underline

Text in base color with a 1px Ember Orange (#ff682c) underline offset 2-3px below baseline. Used sparingly for the one or two most important links per page

### Section Divider

No visible line — sections are separated purely by 80px vertical whitespace and alternating surface colors (white → ash → white)

### Cookie Preferences Link

Small text in Slate (#828282), PolySans 13px, no decoration. Bottom-of-page placement

## Similar Design Systems

- {'why': 'Same editorial restraint with monochrome palette and generous whitespace; both use a single warm accent color for highlights rather than a dominant brand fill', 'business': 'Stripe'}
- {'why': 'Shared taste for sharp 0px-radius buttons against soft rounded surfaces, and a near-monochrome interface that lets typography do the heavy lifting', 'business': 'Linear'}
- {'why': 'Similar data-product aesthetic with dashboard-card imagery and warm-gray surfaces; both treat charts as editorial content rather than decoration', 'business': 'Plaid'}
- {'why': 'Matching sparse, poster-like typographic headlines at extreme sizes with tight tracking, and a commitment to letting negative space carry the design', 'business': 'Figma Config'}

## Agent Prompt Guide

Quick Color Reference:
- text: #202020 (Graphite)
- background: #ffffff (Canvas White)
- surface/card: #efefef (Ash)
- border/divider: #e8e8e8 (Mist)
- accent: #ff682c (Ember Orange)
- secondary text: #4d4d4d (Steel)
- primary action: no distinct CTA color

Example Component Prompts:

1. Hero Section: White canvas background. Headline "Your Headline Here" at 66px PolySans weight 400, #202020, line-height 0.91, letter-spacing -1.32px. Subtext at 18px Inter weight 400, #4d4d4d, line-height 1.25. Two buttons side by side: filled Graphite button "Contact us" (#202020 bg, white text, 0px radius, 10px 20px padding, PolySans 16px) and ghost outlined button "About us" (transparent bg, 1px #202020 border, #202020 text, 0px radius).

2. Asymmetric Card: Ash (#efefef) background, border-radius 6px 0px 0px, padding 70px top and 60px left. Contains an 18px Inter body paragraph in #4d4d4d. No shadow, no border.

3. Data Dashboard Card: White (#ffffff) background, 20px border-radius, 40px padding. Contains a chart with Ember Orange (#ff682c) data line and Brass (#816729) secondary line. Card title in PolySans 18px weight 400, #202020.

4. Navigation Bar: Floating pill container with Ash (#efefef) background and 200px border-radius, wrapping nav items. Items are PolySans 16px weight 400, #202020, separated by 20px gaps. Language toggle "FR" in Slate (#828282) sits to the right.

5. Partner Logo Strip: White background. Caption "Trusted by 80+ partners" in PolySans 13px weight 400, #816729. Row of 7 partner logos in #202020, 20px gap between each, no borders or containers.

## Typography Philosophy

PolySans is the voice; Inter is the grammar. Every heading, nav item, and button label uses PolySans at weight 400 — never 500 or 600. This is counterintuitive (most sites bold their headlines) but it's what makes Ventriloc feel editorial rather than corporate. The tight letter-spacing (-0.02em) compensates for the light weight at display sizes. Inter handles all body copy, captions, and metadata at 500 weight for UI labels and 400 for paragraphs. The 16px PolySans with line-height 1.0 is used for buttons — the tight leading makes labels feel precise and architectural.

## Asymmetric Radius System

The most distinctive structural choice in this system is the asymmetric border-radius 6px 0px 0px on featured cards. This single design decision signals: this is not a standard card grid, this is editorial layout. The soft top-left corner draws the eye downward and rightward, creating visual flow. Pair it with 0px radius on buttons and 200px on nav pills, and you get a three-radius system that creates rhythm: sharp (buttons) → asymmetric (cards) → fully round (navigation). Do not apply symmetric radius to feature cards — the asymmetry is the signature.
