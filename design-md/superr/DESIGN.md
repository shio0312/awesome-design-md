# Superr — Design System

> **North Star**: Warm schoolyard notebook in soft afternoon light. A cream page, an orange marker uncapped, and a stack of sticker-laminated name labels waiting to be peeled.
> **Theme**: light
> **Source**: https://www.superr.ai
> **Refero Style**: https://styles.refero.design/style/cfd0fec1-f25a-4b9b-9bd0-d5b66960f2f2
> **Synced**: 2026-09-01

## Overview

Superr is a warm schoolyard aesthetic rendered in digital form: a cream-paper canvas, hand-marker orange as the only chromatic accent, and chunky lowercase display type that reads like a child's notebook scrawled at full volume. The product itself is photographed like a real object — leather-bound notebooks, colored pencils, sticker-laminated name labels — and these objects, not abstract UI illustrations, do the visual work. Playful illustrated stickers (lightning bolts, bears, hearts, ghosts) scatter across the layout as little bursts of personality, but they are decorative punctuation, not system icons. Every surface stays matte and soft: thin dark borders instead of fills, minimal shadows, generous breathing room, and rounded corners that stop at 20px before going full-pill. The result is a site that feels like opening a fresh parchi on the first day of school — unhurried, tactile, and slightly mischievous.

## Color Palette

- **Cream Paper**: `#fdfbf9` — Page canvas, card surfaces, button fills — the warm-white ground tone that makes dark borders and orange accents feel like ink and marker on paper [neutral]
- **Charcoal**: `#171717` — Dark borders and separators for elevated surfaces and inverted UI. [neutral]
- **Cocoa Ink**: `#2b1a07` — Headline color, decorative borders — a warmer dark that headlines and accent borders inherit from notebook-leather tones instead of pure black [neutral]
- **True Black**: `#000000` — Reserved for highest-emphasis headline moments and strict edge cases where charcoal feels too soft [neutral]
- **Dew Drop**: `#f7efe9` — Secondary surface tint, the slightly warmer card layer that sits between the cream canvas and colored accents [neutral]
- **Marker Orange**: `#ff6f1e` — Signature accent for handwritten captions, script annotations, the footer brand band, and the highlight underline beneath emphasis words — the uncapped-marker energy of the brand [brand]
- **Burnt Sienna**: `#ce500a` — Darker orange shade used for body-color and border accents when the marker orange needs more weight against cream [brand]
- **Sky Sticker**: `#3b82f6` — Decorative illustration accent — appears in sticker characters, sparkle marks, and notebook cover patterns. Not a UI token; do not use for buttons or links [accent]
- **Bubblegum Sticker**: `#ff66cf` — Decorative illustration accent — used exclusively on sticker characters and pink notebook covers. Do not promote to functional UI [accent]
- **Sprout Sticker**: `#22c55e` — Green outline accent for tags, dividers, and focused UI edges [accent]
- **Shadow Mist**: `#bebcbb` — Shadow base color — the desaturated gray under-toning the card and button drop shadows [neutral]

## Typography

- **gelica**
- **Geist**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 16 | — | 1.5 |
| body-sm | 18 | — | 1.5 |
| body | 20 | — | 1.5 |
| subheading | 24 | — | 1.4 |
| heading-sm | 28 | — | 1.4 |
| heading | 36 | — | 1.2 |
| heading-lg | 46 | — | 1.2 |
| display | 104 | — | 1.08 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 12px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '20px', 'cards': '12px', 'footer': '56px', 'inputs': '8px', 'buttons': '20px'}

## Layout

Asymmetric and editorial. The hero is a two-column split: left half holds the display headline, handwritten caption, and pill CTA stacked loosely; right half is occupied by a single large product photograph of a tilted brown notebook. Below the fold, the layout alternates between product photography blocks and centered typographic moments, with sticker illustrations bridging the two. Navigation is minimal — a 32px icon in the top-left, a pill button in the top-right, and nothing in between. Content is left-aligned throughout; the design resists centering as a crutch. Page max-width is ~1200px but the hero photography often breaks the container to feel more spontaneous.

## Surfaces / Elevation

- **Canvas**
- **Surface Tint**
- **Brand Band**

**Shadow tokens:**

## Imagery

Photography-forward: real product shots of leather-bound notebooks in brown, blue-cloud, and rose-pink cover patterns, each photographed with a colored pencil tucked alongside. Stickers are illustrated (flat, 2px dark outlines, vivid fills) and treated as physical objects placed on the page — slightly rotated, never grid-aligned. Hand-drawn SVG arrows and script captions in Marker Orange connect the photography to the copy. No abstract graphics, no 3D renders, no stock photography — the product IS the imagery.

## Design Principles

### Do

- Set headlines in gelica 600 at 104px, lowercase, color Cocoa Ink (#2b1a07), line-height 1.08
- Use Marker Orange (#ff6f1e) only for handwritten captions, inline emphasis highlights, and the footer brand band
- Use Charcoal (#171717) for all text, borders, button strokes, and structural edges — it is the only 'ink' color
- Round all buttons and tags to 20px pill radius, all cards to 12px, and reserve 56px for the footer's asymmetric top edge
- Keep the canvas at Cream Paper (#fdfbf9) with Dew Drop (#f7efe9) as a subtle secondary surface tint, never pure white
- Lean on photographed product objects (notebooks, pencils, labels) as the primary visual content — they are the hero
- Scatter sticker illustrations at random rotations between 5-15° to maintain the placed-by-hand feeling

### Don't

- Do not use Sky Sticker blue, Bubblegum pink, or Sprout green for any functional UI element — they are decoration only
- Do not use filled CTA buttons — the action language is always a dark border on cream, never a solid color fill
- Do not capitalize headlines or apply letter-spacing — the lowercase + normal tracking is a signature
- Do not use drop shadows heavier than rgba(0,0,0,0.06) on cards or rgba(0,0,0,0.25) on buttons — the elevation is whisper-light
- Do not center-align headlines after the first line; left-align the full stack for the hand-notebook rhythm
- Do not introduce gradients, glassmorphism, or neon accents — the palette is matte and warm
- Do not use Geist for headlines — it is a supporting grotesque, gelica owns all display sizes

## Components

### Pill Action Button

Cream fill (#fdfbf9), 1.5px Charcoal border (#171717), 20px pill radius, 28px horizontal padding / 10-11px vertical padding, gelica 16px weight 500 Charcoal text. Subtle 1-2px drop shadow rgba(0,0,0,0.25) for paper-lift. No fill state — the button's identity is the dark border, not the background.

### Display Headline

gelica 104px / line-height 1.08, weight 600, lowercase, color Cocoa Ink (#2b1a07). Tight two-line stack with no letter-spacing. The headline reads as a single visual object — never break above 3 lines, never center-align after the first line.

### Handwritten Caption

gelica 20-24px weight 400 in Marker Orange (#ff6f1e), slightly rotated or aligned to a hand-drawn arrow. Pairs with a thin SVG curved arrow pointing at the object being labeled.

### Marker Highlight

Text rendered in Marker Orange (#ff6f1e) with a rough hand-drawn underline in the same color, 2-3px stroke weight, slight wobble. Sits inline within a Cocoa Ink body sentence.

### Product Notebook

Full-bleed object image, 12-16px corner radius on the notebook edges in the photo, tilted 5-8° off-axis. Carries a white sticker label (Name / Class / Roll no.) on the cover with gelica 16-20px handwritten text.

### Name Label Sticker

White card with 1px Charcoal border, 8px corner radius, three fields: Name (gelica 20px handwritten), Class (gelica 16px), Roll no. (gelica 16px). Mimics a real school label — small, functional, charming.

### Sticker Illustration

Flat, illustrated characters (lightning bolt, bear, heart with eyes, ghost, cat, sparkle) in Sky Sticker blue / Bubblegum pink / Sprout green with 2px dark outlines. Rotated 5-15° at random, treated as physical stickers placed on the page — never aligned to a grid.

### Hand-drawn Arrow

Thin 1.5px Charcoal stroke curved arrow, hand-drawn wobble, no arrowhead fill. Originates from a Handwritten Caption and terminates at the labeled object with a slight curl.

### Pre-order Info Block

gelica 16px weight 400, color Cocoa Ink (#2b1a07), 8px gap below button. States availability/timing — no decoration, no icon, just a quiet line of text.

### Footer Brand Band

Marker Orange (#ff6f1e) background, 56px asymmetric corner radius on the top edge, gelica text in Charcoal or cream. Functions as the brand closer — a single orange stripe that says 'we're done, and we had fun.'

### Top-left Brand Mark

Small illustrated hand/pointing icon (~32px) in Charcoal, 16px margin from top-left edge. No wordmark beside it — the icon IS the brand mark. Links to home.

### Top-right Action

Same Pill Action Button pattern, positioned top-right with 16px margin. Visible on every screen as the single conversion anchor.

## Similar Design Systems

- {'why': 'Same warm-cream canvas, handcrafted editorial feel, and confident lowercase display type with dark borders on light surfaces', 'business': 'Are.na'}
- {'why': 'Pill-shaped outlined buttons on cream backgrounds, playful illustrated accents scattered through a product-forward layout', 'business': 'Gumroad'}
- {'why': 'Matte paper-like surfaces, thin dark borders defining all structural elements, and sticker/illustration personality on an otherwise restrained UI', 'business': 'Notion'}
- {'why': 'Kawaii-adjacent sticker vocabulary paired with serious editorial typography and warm off-white canvas', 'business': 'Croissant'}
- {'why': 'Hand-marker orange as the only chromatic accent against cream paper, with hand-drawn arrows and annotations labeling product photography', 'business': 'Craigslist redesigns (e.g. by Patta)'}

## Agent Prompt Guide

**Quick Color Reference**
- canvas: #fdfbf9 (Cream Paper)
- text: #171717 (Charcoal) / #2b1a07 (Cocoa Ink for headlines)
- border: #171717 (Charcoal)
- accent: #ff6f1e (Marker Orange)
- surface tint: #f7efe9 (Dew Drop)
- primary action: no distinct CTA color

**Example Component Prompts**
1. Build the hero: Cream Paper (#fdfbf9) canvas, full page. Left half: gelica 104px weight 600 lowercase 'meet superrbook' in Cocoa Ink (#2b1a07), line-height 1.08. Below it, a Handwritten Caption in gelica 20px Marker Orange (#ff6f1e) reading 'Dear grownups,'. Below that, body text in gelica 20px weight 400 Cocoa Ink with the word 'actually!' rendered in Marker Orange and underlined with a 2px hand-drawn stroke. Below the body, a Pill Action Button: 20px radius, 1.5px Charcoal (#171717) border, cream fill, gelica 16px weight 500 text 'I call dibs!'. Under the button, a Pre-order Info Block in gelica 16px Cocoa Ink: 'Pre-order starting April 2026.' Right half: a photograph of a brown leather notebook tilted 5-8°, with a Sky Sticker (#3b82f6) lightning bolt and a Bubblegum (#ff66cf) bear character floating above it at random rotations.

2. Build a product showcase row: Cream Paper canvas. Two notebook photographs side by side — left notebook is blue with white cloud pattern, right notebook is rose-pink. Above the blue notebook, a Handwritten Caption in Marker Orange 'a big blue parchi' with a thin Charcoal curved arrow pointing down to the notebook. Above the pink notebook, a Handwritten Caption 'cute pinks' with a matching arrow. Between them, centered: a small Marker Orange script caption 'Like making' above gelica 36px weight 500 Cocoa Ink text 'Our SuperrBook. Our Way.'

3. Build a pill button: Cream Paper fill (#fdfbf9), 1.5px solid Charcoal (#171717) border, 20px border-radius, 28px horizontal padding and 10px vertical padding. gelica 16px weight 500 Charcoal text, centered. Drop shadow: rgba(0,0,0,0.25) 0px 1px 2px 0px. No hover fill change — keep the cream background on all states.

4. Build a footer band: full-width Marker Orange (#ff6f1e) background with 56px top-left and top-right border-radius (asymmetric cap). gelica 16-20px Charcoal or cream text centered or left-aligned. Functions as the brand closer.

5. Build a sticker illustration cluster: flat 2D characters (lightning bolt in Sky Sticker #3b82f6, heart with eyes in Marker Orange, ghost in Charcoal) each with 2px dark outlines, placed at random rotations between 5-15°, overlapping slightly. No drop shadows on stickers — they sit flat on the page like real peel-and-stick.
