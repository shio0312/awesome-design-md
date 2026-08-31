# Ko-fi — Design System

> **North Star**: Warm café chalkboard on cream paper.
> **Theme**: light
> **Source**: https://ko-fi.com
> **Refero Style**: https://styles.refero.design/style/35ae81e1-273c-43d7-9bcd-ea186d062c13
> **Synced**: 2026-09-01

## Overview

Ko-fi reads like a warm indie café menu printed on recycled card stock. A cream page canvas replaces the cold white typical of creator tools, and a custom chunky display font stamps hero headlines with a hand-set zine energy while DM Sans keeps everything readable. Every interactive element is aggressively rounded — pill buttons, pillow-soft cards, capsule inputs — giving the whole system a tactile, sticker-book quality. Black 2-3px borders wrap photo and card surfaces instead of shadows, reinforcing the cut-out-and-paste craft aesthetic. A single soft periwinkle blue punctuates the otherwise warm neutral palette as the one and only accent, reserved for primary actions so they always feel like the most important thing on screen.

## Color Palette

- **Oat Cream**: `#e9dfd2` — Secondary surface — feature card backgrounds, warm button fills, tag backgrounds [neutral]
- **Morning Fog**: `#e5e7eb` — Page canvas, subtle borders, hairline dividers — the base everything sits on [neutral]
- **Ink Black**: `#202020` — Primary text, dark filled buttons, dark icon fills [neutral]
- **Sticker Black**: `#000000` — Heavy borders on cards, images, and the logo wordmark — the signature outline that makes elements feel cut from paper [neutral]
- **Paper White**: `#ffffff` — Card surfaces above the cream canvas, text on dark buttons, input field fills [neutral]
- **Kofi Blue**: `#aac9f7` — Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color [brand]
- **Cobalt Pop**: `#72a4f2` — Primary action hover/pressed state, saturated Kofi Blue variant [brand]

## Typography

- **bogue-black**
- **DM Sans**
- **Font Awesome 6 Pro**
- **Font Awesome 6 Brands**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.33 |
| heading | 30 | — | 1.2 |
| display | 60 | — | 1 |
| display-lg | 72 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 28px
- **Element Gap**: 20px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '9999px', 'cards': '40px', 'inputs': '9999px', 'buttons': '9999px', 'feature-cards': '24px', 'small-elements': '16px'}

## Layout

Max-width ~1200px centered container on a full-bleed cream canvas. Hero is centered: large bogue-black display headline, DM Sans subtitle, single blue pill CTA, then illustration below. Sections alternate between centered text blocks and 3-column card grids. Category sections use wrapped rows of pill-shaped tags. Creator showcases are 3-up grids of sticker-bordered photo cards. Navigation is a minimal floating top bar with logo left, links center-right, dark pill CTA right. Section gaps of 40-80px create generous breathing room between rhythm blocks.

## Surfaces / Elevation

- **Canvas**
- **Oat Surface**
- **Paper Card**
- **Blue Wash**

## Imagery

Photography is creator-focused portraiture — direct, warm, eye-contact-with-camera shots at close crop, shown full-bleed inside 40px-radius sticker frames with a 2-3px black border. Illustrations are hand-drawn line art of rounded mascot characters (ghost, heart, bean) with selective flat color fills in Kofi Blue and warm cream. The coffee-cup-with-heart logo is a recurring illustration motif. No 3D renders, no stock photography, no abstract gradients — everything reads as either a friendly human portrait or a hand-drawn mascot.

## Design Principles

### Do

- Use 9999px pill radius for every button, tag, input, and nav CTA — sharp corners break the tactile language
- Use bogue-black (or Bowlby One substitute) only for display headings 48px and above — DM Sans for everything else
- Wrap all card and image surfaces in a 2-3px solid #000000 border instead of adding drop shadows — the sticker outline is the elevation system
- Reserve Kofi Blue (#aac9f7) exclusively for the single primary action per view; let it win attention by being the only color on screen
- Maintain the cream canvas (#e5e7eb) as the universal page background — never introduce pure white or pure gray as the base
- Keep all icon glyphs at 20px in the same family weight — consistent icon size preserves the sticker-book rhythm
- Pair every category tag with a leading Font Awesome solid icon to reinforce the playful, labeled-sticker feel

### Don't

- Don't use drop shadows on cards, buttons, or images — the black border replaces elevation and shadows would muddy the craft aesthetic
- Don't introduce additional chromatic accents beyond Kofi Blue and its hover state — the warm-neutral-plus-one-blue palette is the identity
- Don't use DM Sans at 40px+ for headings — it loses the chunky display quality; switch to bogue-black or its substitute
- Don't place interactive elements on pure white #ffffff as the page background — the cream canvas is what makes the system feel warm
- Don't use square or slightly-rounded (4-8px) corners on buttons, tags, or inputs — pill is the only acceptable radius for interactive elements
- Don't apply the Sticker Black border to text or background blocks — reserve it for photo and card surfaces where the outline reads as a die-cut shape
- Don't use the bogue-black display font for body, nav, button, or input text — its weight and personality overwhelm functional UI

## Components

### Pill Primary Button (Kofi Blue)

Filled Kofi Blue (#aac9f7) with #202020 text, 9999px pill radius, 20px vertical and 20-28px horizontal padding, DM Sans 16px weight 600. Sits on cream canvas where it reads as the single most important action. Hover/pressed shifts to Cobalt Pop (#72a4f2).

### Pill Dark Button

Filled Ink Black (#202020) with #ffffff text, 9999px pill radius, 20px padding all sides, DM Sans 14-16px weight 600. Used for 'Sign up free' in the nav — the always-visible account action.

### Pill Outline Button (Learn More)

Ink Black (#202020) text on white card surface, 9999px pill radius, 20px padding, no border. Label appears as a standalone pill. Used for 'Learn how Ko-fi works' on feature blocks.

### Sticker Card (Creator Profile)

White (#ffffff) fill, 40px radius, 2-3px solid #000000 border. No shadow — the black border IS the elevation. Contains a full-bleed photo (also 40px radius) above creator info. The sticker effect is the signature visual moment of the whole system.

### Oat Feature Card

Oat Cream (#e9dfd2) fill, 24px radius, generous 40-80px padding, contains a bogue-black display heading, DM Sans body copy, and a pill outline button. Sits inside a white card frame on the cream canvas.

### Category Tag Pill

White fill, 9999px pill radius, 20px horizontal padding, DM Sans 16px weight 400 in Ink Black. Active state gets a 2px Ink Black border. Each tag leads with a 20px Font Awesome solid icon in its natural brand color.

### Top Navigation Bar

Transparent over the cream canvas, 9999px pill for the dark 'Sign up free' button, nav links in DM Sans 16px weight 400. Logo is a chunky bogue-black 'Ko-fi' wordmark with a coffee-cup icon. No background bar — nav floats on the canvas. Padding 16-20px vertical.

### Pill Input Field

White (#ffffff) fill, 9999px pill radius, 28px horizontal padding, 2px Ink Black border, DM Sans 16px placeholder. Border thickens or shifts to Kofi Blue on focus. No sharp corners anywhere.

### Logo Wordmark Lockup

bogue-black 'Ko-fi' text in Ink Black, paired with a rounded coffee-cup icon with a heart on the cup. The coffee cup fill is a warm orange-red (the brand's secondary signal). Surrounded by a 2px black sticker border when used as a standalone badge.

### Section Headline Block

Centered bogue-black heading at 60px line-height 1.0, followed by DM Sans 20px subheading in Ink Black. Generous 40-64px bottom margin before content. Creates the 'chapter title' rhythm that structures the page.

### Creator Photo Tile

Photo fills a 40px-radius tile with a 2-3px #000000 border, white frame around the photo. No caption inside the tile — info lives in adjacent text. Photos are not cropped to square; they keep natural aspect within the rounded frame.

### Feature Illustration Block

Hand-drawn line illustrations with selective Kofi Blue accent fills, no background container, sits directly on the cream canvas. Characters are outlined in black, flat colored, playful proportions. The illustration IS the emotional hook of the hero.

## Similar Design Systems

- {'why': 'Same warm-cream canvas with a single playful color accent, and creator-portrait cards with rounded edges and friendly typography', 'business': 'Gumroad'}
- {'why': 'Direct competitor with the same creator-tip focus, shared hand-drawn mascot illustration style, and rounded-everything button and card system', 'business': 'Buy Me a Coffee'}
- {'why': 'Similar zine-quality custom display headlines, cream-and-black palette, and sticker-bordered editorial card layouts', 'business': 'Substack'}
- {'why': 'Same pill-shaped buttons and capsule input fields, though Notion is colder and more utilitarian — the structural DNA of soft-rounded controls overlaps', 'business': 'Notion'}
- {'why': 'Stripped-back warm aesthetic with one accent color, chunky display type, and an unapologetically craft, non-corporate personality', 'business': 'Craigslist (reimagined)'}

## Agent Prompt Guide

Quick Color Reference:
- canvas/background: #e5e7eb (Morning Fog)
- text/primary: #202020 (Ink Black)
- text/on-dark: #ffffff (Paper White)
- border/sticker: #000000 (Sticker Black)
- card/surface: #ffffff (Paper White)
- accent/feature: #e9dfd2 (Oat Cream)
- primary action: #72a4f2 (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #72a4f2 background, #202020 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a 3-column creator card grid: each card white (#ffffff) with 2px solid #000000 border, 40px radius, no shadow. Photo at top fills a 40px-radius area. Creator name in DM Sans 20px weight 600 #202020, handle in DM Sans 16px weight 400 #202020 below. 28px padding inside card.

3. Create a category tag row: 6-8 pill tags in a wrapped flex layout. Each tag white fill, 9999px radius, 20px horizontal padding, DM Sans 16px weight 400 in #202020. Leading 20px Font Awesome solid icon. Active tag gets a 2px #202020 border.

4. Create a feature block: outer card white (#ffffff) with 24px radius, 40-80px padding. Inner feature panel with #e9dfd2 fill, 24px radius. bogue-black heading at 60px, DM Sans body at 16px. Outline pill button: #202020 text on white, 9999px radius, 20px padding.

5. Create a pill input field: #ffffff fill, 9999px radius, 28px horizontal padding, 2px solid #000000 border, DM Sans 16px placeholder in muted gray. On focus, border shifts to #aac9f7.

## Elevation Philosophy

Ko-fi deliberately avoids drop shadows. The system uses a 2-3px solid #000000 border as its sole elevation mechanism on cards, images, and the logo lockup. This creates a flat sticker-book aesthetic where elements feel cut from paper and placed on a warm canvas, rather than floating above it. The black border must always be paired with a generous radius (24px or 40px) so it reads as a die-cut outline rather than a hard frame. No box-shadows, no glow effects, no layered ambient lighting — the cream canvas itself provides all the depth the design needs.
