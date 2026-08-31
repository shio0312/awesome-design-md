# ClickUp™ — Design System

> **North Star**: Hardworking dashboard on white marble. The page is a product brochure for a productivity tool, so the visual language borrows from the product itself: dense lists, status pills, avatar clusters, and bold typographic claims that read like a product spec sheet at exhibition scale.
> **Theme**: light
> **Source**: https://www.clickup.com
> **Refero Style**: https://styles.refero.design/style/efcb73cb-b84a-4ae7-9a2b-e1116f79f130
> **Synced**: 2026-09-01

## Overview

ClickUp speaks in a sharp, high-contrast productivity dialect: a white canvas where oversized bold headlines (52-80px, weight 650-800, tracking pulled to -0.04em) collide with compact 14px button labels and a black filled CTA. The signature move is the 9999px pill — chips, tags, nav items, and badges all share one relentless full-radius curve, giving the interface a soft, rounded personality against otherwise hard typographic weight. Color is used surgically: a single vivid purple (#6647f0) stamps brand identity, blue (#0091ff) handles interactive links, and the rest of the system is pure grayscale. Rotating conic-gradient borders animate around hero elements, the only moment the page lets its hair down. The product UI screenshot on the right of the hero anchors the brand: real, dense, working software — not abstract gradients or stock illustration.

## Color Palette

- **Signal White**: `#ffffff` — Page background, card surfaces, button fills — the default canvas against which every other color is placed [neutral]
- **Ink Black**: `#202020` — Primary action fills, headline text, filled CTA buttons — near-black at 12.9:1 on white for confident authority without pure #000 harshness [neutral]
- **Onyx**: `#090c1d` — Headlines at maximum scale (48-80px display) — the deepest near-black with a barely perceptible cool tint [neutral]
- **Carbon**: `#2a2a2a` — Card borders, button text on light fills, section dividers — the workhorse dark neutral for structural elements [neutral]
- **Slate**: `#646464` — Body text secondary, link text, nav labels, icon fills — carries the 153-occurrence body copy load [neutral]
- **Ash**: `#838383` — Tertiary text, muted nav, meta labels, disabled states — recedes into the background hierarchy [neutral]
- **Fog**: `#b3b3b3` — Card borders at low contrast, subtle dividers, placeholder accents — the lightest border that still reads on white [neutral]
- **Cloud**: `#d4d4d4` — Hairline borders, dashed dividers, input outlines — appears 49× as borderColor [neutral]
- **Bone**: `#e8e8e8` — Default border color (88× in buttons), the most-used border tone in the system [neutral]
- **Mist**: `#f8f9fa` — Light neutral action fill for buttons on dark surfaces. [neutral]
- **Plaster**: `#e9ebf0` — Body section background band — appears 500×, the large neutral that breaks white sections [neutral]
- **Mercury**: `#eeeeee` — Badge text, card accents, neutral chip backgrounds — soft contrast for non-interactive surfaces [neutral]
- **Brand Violet**: `#6647f0` — Violet state accent for badges, validation surfaces, and short status labels. [brand]
- **Signal Blue**: `#0091ff` — Blue accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color [accent]
- **Mint**: `#6ee7b7` — Green text accent for links, tags, and emphasized short phrases [accent]
- **Emerald**: `#00c07a` — Green outline accent for tags, dividers, and focused UI edges [accent]
- **Teal Tag**: `#16c0a4` — Teal state accent for badges, validation surfaces, and short status labels. [semantic]
- **Rainbow Conic**: `#7d5be7` — Animated conic-gradient border rotating around hero CTAs and Brain² element — the brand's most expressive moment [brand]
- **Primary Gradient**: `#40ddff` — Cyan-to-magenta linear gradient for premium brand moments, 83deg angle — the system gradient for hero text and premium badges [brand]
- **Dark Fade**: `#111111` — Section-level dark gradient from charcoal to true black — used on dark feature panels [neutral]

## Typography

- **Plus Jakarta Sans**
- **Inter**
- **Sometype Mono**
- **SF Pro**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.5 |
| heading-sm | 34 | — | 1.2 |
| heading | 48 | — | 1.25 |
| heading-lg | 60 | — | 1.1 |
| display | 80 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 28px
- **Element Gap**: 12px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '100px', 'cards': '12px', 'badges': '9999px', 'images': '16px', 'inputs': '9px', 'buttons': '9999px', 'largeCards': '20px'}

## Layout

Max-width 1200px centered, no sidebar. Hero is a 2-column split: left column holds the headline (80px display), checkmark benefit list, dark filled CTA, and a row of feature tag pills; right column holds the product UI screenshot at full column width. Below the hero, sections alternate: a centered-headline illustration section (the tangled gray 'context loss' graphic), then a G2 awards section (text left / badge grid right), then a stats band with large numbers. Navigation is a single top bar with logo, 6 nav items (some with dropdown indicators), a 'Get a Demo' ghost link, a 'Login' ghost button, and a 'Sign Up' filled dark pill. Section gaps are large (~80px) while internal element gaps are compact (8-12px), creating a rhythmic density contrast: tight inside sections, spacious between them. The page reads top-to-bottom as: announcement bar → nav → hero split → social proof logos → illustration section → awards grid → stats → footer.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Section Band**
- **Dark Panel**
- **Ink Surface**

## Imagery

The page is UI-screenshot-dominant, not photo-dominant. The hero features a real product UI screenshot of the ClickUp app (sidebar nav, inbox, task list with status pills and avatar clusters) rendered at large scale. Secondary visuals include: G2 award badge grid (grayscale with red G2 logos), logo strip for 'trusted by' (Amazon, NVIDIA, Wayfair, Verizon, Spotify, Stanford — all rendered flat in grayscale), and abstract decorative elements made of gray swirling line-art (the 'context loss' illustration uses tangled gray ribbons with floating app icons). Photography is essentially absent. The visual language is: show the product, show the awards, show the logos — no stock lifestyle photography, no hero videos. Icons are colorful and flat in the product UI (red, blue, green, purple app icons) but rendered in single-tone grayscale in decorative contexts.

## Design Principles

### Do

- Use Plus Jakarta Sans at weight 650-800 for any display text 34px or larger — the heavy weight with tight tracking is the brand's typographic signature
- Default all buttons, tags, and badges to border-radius 9999px — the fully-pill curve is the system's most consistent geometric choice
- Use #202020 (not pure #000) for filled CTA buttons and headline text — the slight softness reads more premium than absolute black
- Apply -0.04em letter-spacing to all display text 48px+ — the aggressive negative tracking is what makes the headlines feel confident rather than shy
- Use #6647f0 purple exclusively for brand identity moments (badges, Brain² tags, brand icon) — never as a primary action fill
- Maintain a 4px spacing base unit; snap all padding and margin values to multiples of 4
- Use 1px solid #e8e8e8 as the default border — 88 occurrences in buttons make it the structural baseline
- Add the rotating conic-gradient border to one hero element per page — restraint keeps the rainbow effect from becoming visual noise

### Don't

- Don't use #000000 for large text fills or backgrounds — use #202020 (Ink Black) or #090c1d (Onyx) instead for softer contrast
- Don't mix multiple border-radius values on the same component level — if buttons are 9999px, every button stays 9999px
- Don't use Plus Jakarta Sans below 14px — it gets too geometric for small text; switch to Inter for body-sm and caption roles
- Don't apply the brand purple #6647f0 to primary CTA buttons — it appears only on badges and brand marks
- Don't stack more than two surface elevation levels in a single section — the system relies on flat hierarchy, not deep shadow stacking
- Don't use letter-spacing wider than 0 for any body text — positive tracking appears only on uppercase mono labels
- Don't use Inter as a display font — it lacks the geometric authority of Plus Jakarta Sans at large sizes
- Don't add decorative gradients to cards or section backgrounds — gradients belong only in the conic border animation and hero text

## Components

### Filled Dark CTA Button

Background #202020, text #ffffff at 14px Plus Jakarta Sans weight 700, border-radius 9999px (fully pill-shaped), padding 12px 24px, no border. Single solid color, no shadow. Used for 'Get started. It's FREE!', 'Sign Up' in header.

### Ghost Outline Button

Background transparent, 1px border in #e8e8e8 or #0091ff (blue for interactive, gray for neutral), text #202020 at 14px weight 700, border-radius 9999px, padding 10px 20px. The blue-border variant signals a chromatic outlined action.

### Nav Pill Button

Background rgba(0,0,0,0.04) hover, text #2a2a2a at 14-16px, border-radius 9999px, padding 4px 12px (very compact). No visible border. Sits inline with other nav items.

### Feature Tag Pill

Background transparent or #f8f9fa, text #202020 or #0091ff at 14px weight 700, border-radius 9999px, padding 8px 16px, no border or 1px #e8e8e8. The blue-text variant indicates the currently active or highlighted tag.

### Product Screenshot Card

No background fill, border-radius 12px, no shadow, the screenshot sits on the white canvas with breathing room. Padding 0 (screenshot is the content). 16-32px corner radius on screenshot itself.

### Stat Callout Card

White background (#ffffff), no border, no shadow, padding 28px. Number in Plus Jakarta Sans 60-80px weight 700, tracking -0.04em, color #090c1d. Caption below in Inter 16-18px, color #646464.

### Dark Feature Card

Background #000000 to #191919 with subtle linear-gradient fade, border-radius 12-16px, no visible border, padding 40-80px vertical. White text (#ffffff) for headings at 48-60px weight 650, gray text (#b3b3b3) for body.

### Trust Badge Strip

No background, horizontal flex layout, logos rendered in #838383 to #202020 grayscale. No borders, no cards. Heading label 'TRUSTED BY THE BEST' in Sometype Mono 10px weight 400, tracking 0.08em, uppercase, color #838383.

### Rounded Avatar Cluster

Circular avatars (border-radius 9999px), 24-32px diameter, overlapping by ~8px, 1-2px white stroke border to separate overlapping faces. Mix of brand-tinted and neutral fills.

### G2 Award Badge

White card with 1px #d4d4d4 border, border-radius 8px, padding 16px, G2 red logo top-left, tier text centered, orange/blue gradient chevron at bottom. 3-column grid arrangement.

### Conic Gradient Border Element

1.5-2px conic-gradient border rotating at 0.45s linear infinite, starting from 90deg, cycling through #7d5be7 → #bc3fda → #fa24ce → #fb49a5 → #fc6d7b → #fd8461 → #fd9a46 → #f687c6 → #a3a0e0 → #4fb9fa → #0091ff. Inner fill white. Border-radius 9999px for pill, 12-20px for cards.

### Checkmark List Item

Blue checkmark icon (#0091ff) at 18px, bold lead text (#202020, 14-16px weight 600-700) followed by regular-weight descriptor text in #646464. 8-12px row gap between items.

### Status Pill (In UI Screenshot)

Pill-shaped with border-radius 9999px, small text 10-12px weight 600, colored backgrounds: green #6ee7b7 bg with dark text for 'DONE', blue #0091ff bg with white text for 'IN PROGRESS', pink/magenta for overdue. Padding 3px 9px.

## Similar Design Systems

- {'why': "Same tight typographic discipline with display headlines at 48-80px, negative letter-spacing, monochrome canvas with a single brand accent (purple vs Linear's violet), and 9999px pill buttons for primary actions", 'business': 'Linear'}
- {'why': 'Shared compact density, 4px spacing base, and a flat UI philosophy that relies on hairlines and whitespace instead of heavy shadows; both use a near-black for primary CTAs and reserve color for badges and tags', 'business': 'Notion'}
- {'why': 'Similar treatment of black/white/grayscale as the primary palette, with vivid color appearing only in decorative gradient borders; both use a custom geometric sans for display and rely on real product screenshots in hero sections', 'business': 'Vercel'}
- {'why': 'Comparable use of a conic-gradient rainbow border as the signature brand element, 9999px pills throughout the component system, and product-screenshot-driven hero layouts with bold oversized headlines', 'business': 'Webflow'}

## Agent Prompt Guide

**Quick Color Reference**
- Text: #202020 (primary), #646464 (secondary), #838383 (tertiary)
- Background: #ffffff (canvas), #f8f9fa (card), #e9ebf0 (section band)
- Border: #e8e8e8 (default), #d4d4d4 (hairline), #0091ff (interactive accent)
- Brand: #6647f0 (purple — badges, brand identity only)
- primary action: #202020 (filled action)

**3 Example Component Prompts**

1. Create a Primary Action Button: #202020 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.


3. **Dark Feature Card**: Create a dark surface card with background gradient from #111111 to #000000, border-radius 16px, padding 80px 40px. White headline (#ffffff) at 48px Plus Jakarta Sans weight 650, tracking -0.035em. Body text in #b3b3b3 at 16px Inter. A 2px rotating conic-gradient border (cycling through #7d5be7 → #0091ff → #fa24ce) wraps a white inner button with blue text.

## Gradient System

Two gradient families serve distinct purposes:

**1. Conic Gradients — Animation**: Used exclusively for the rotating border effect on hero CTAs and the Brain² element. The signature 11-stop conic (violet → magenta → pink → orange → cyan → blue) rotates at 0.45s linear infinite, creating a rainbow chase. This is the brand's most expressive visual moment and should appear at most once per page section.

**2. Linear Gradients — Static Brand**: The 83deg cyan-to-magenta primary gradient (#40ddff → #7612fa → #fa18e3) is used for premium text treatments and the 'Brain²' wordmark. The 97deg dark-to-gray gradient (#202020 → #8f8f8f) is used on premium badges and feature highlights.

**3. Dark Fades**: linear-gradient(#111111 24%, #000000) creates the 'abyss' effect on dark feature panels — a subtle 3-stop fade from charcoal to true black that adds depth without a flat black surface.

## Motion Philosophy

Motion is expressive but constrained. The dominant duration is 0.45s (1000 occurrences) with a cubic-bezier(0.33, 1, 0.68, 1) ease — a slow-out curve that feels like content settling into place. Secondary durations are 0.25s and 0.3s for state changes. The hero conic gradient rotates at 0.45s linear, creating constant motion that draws the eye to the single brand-significant CTA. Hover transitions use 0.15s for instant feedback. Named animations (Brain2MemoryVisual, ContextCardVisual, HomeHero4o) all involve border-pulse or rainbow-rotation effects tied to the conic gradient system. The principle: one dramatic continuous animation per viewport, everything else settles with soft ease-out.
