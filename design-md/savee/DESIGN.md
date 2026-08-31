# Savee — Design System

> **North Star**: Black canvas for visual curators
> **Theme**: dark
> **Source**: https://savee.it
> **Refero Style**: https://styles.refero.design/style/c6d8490d-e3f2-45c8-aebf-fe5f11daf116
> **Synced**: 2026-09-01

## Overview

Savee operates in near-total darkness: an almost pure black canvas (#050505) where the only chromatic element is a single electric indigo (#1500ff) that punctuates the interface like a neon gallery light. Typography does all the heavy lifting — a single custom sans-serif used at every level, from 96px display headlines with 0.96 line-height and -0.04em tracking down to 13px captions, creating a confident editorial rhythm that feels more like a museum wall than a SaaS dashboard. Surfaces are barely distinguishable: the page canvas, elevated cards (#151515), and deeper overlays (#1e1e1e) form a near-invisible hierarchy that lets imagery and type carry the experience. The lone violet accent on the primary CTA is the only visual noise the system permits — everything else is white type on black, pill-shaped controls, and generous 64px section breathing room.

## Color Palette

- **Electric Indigo**: `#1500ff` — Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Obsidian**: `#050505` — Page canvas, deepest background — the void that all content sits on [neutral]
- **Charcoal**: `#151515` — Elevated surface, product preview frames, secondary panels [neutral]
- **Graphite**: `#1e1e1e` — Deeper overlay surface, hover states on dark cards, input fields [neutral]
- **Paper**: `#fdfdfd` — Primary text, inverted surface, button text, high-contrast foreground [neutral]
- **Silver**: `#e5e5e5` — Hairline borders, dividers, subtle structural edges [neutral]
- **Pearl**: `#d4d4d4` — Secondary text, subdued headings, placeholder body copy [neutral]
- **Slate**: `#2f2f2f` — Footer borders, low-contrast dividers between dark zones [neutral]
- **Ash**: `#a3a3a3` — Muted helper text, inactive icons, de-emphasized metadata [neutral]
- **Stone**: `#737373` — Tertiary text, timestamps, supplementary labels [neutral]

## Typography

- **Savee Font**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.5 |
| body | 16 | — | 1.5 |
| body-lg | 18 | — | 1.38 |
| subheading | 21 | — | 1.33 |
| heading-sm | 24 | — | 1.29 |
| heading | 30 | — | 1.25 |
| heading-lg | 36 | — | 1.13 |
| display | 60 | — | 1 |
| display-lg | 96 | — | 0.96 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 12px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '9999px', 'cards': '14px', 'pills': '9999px', 'inputs': '9999px', 'buttons': '9999px'}

## Layout

The page is centered single-column with a max content width around 1200px. The hero opens with a centered display headline, subtext, and single CTA — no split layout, no side imagery. Below the hero, a large product preview frame (Charcoal rectangle) occupies the full content width. A partner logo strip follows as a single horizontal row. Then large left-aligned editorial body text at 36px. Navigation is a floating text-only bar with no background fill. Sections are separated by 64-80px of pure Obsidian canvas — no dividers, no color bands. The rhythm is: massive centered type → large dark product frame → quiet logo strip → oversized prose → void.

## Surfaces / Elevation

- **Canvas**
- **Elevated Panel**
- **Deep Overlay**

## Imagery

Imagery is product-first and user-curated. The hero shows a large product preview frame in Charcoal (#151515) suggesting a dark-mode app interface. Partner logos are rendered in flat grayscale — no color, no depth, no backgrounds. The overall visual density is text-dominant: the 96px headline and 36px body copy occupy far more visual space than any imagery. When user content appears (bookmarks, mood boards), it is presented as raw crops on the Obsidian canvas without decorative frames or treatments.

## Design Principles

### Do

- Use #1500ff Electric Indigo exclusively for the single primary CTA on any given screen — never for secondary actions, links, icons, or decorative elements
- Set display headlines at 96px with line-height 0.96 and letter-spacing -0.04em so the type compresses into a confident sculptural block rather than stretching
- Apply 9999px border-radius to every button, tag, and pill — the pill shape is the system's only control geometry
- Use 14px radius for card and product preview surfaces, and nothing else — keep the shape vocabulary to exactly two radii
- Let the Obsidian canvas (#050505) be the separator between sections — add 64-80px of empty space rather than lines, color shifts, or gradient transitions
- Set body prose at 36px when it needs to carry editorial weight; drop to 18px for functional descriptions. Never use 14-16px for primary page copy
- Keep all text in the neutral palette (#fdfdfd, #d4d4d4, #a3a3a3) — the only chromatic color is the CTA indigo

### Don't

- Never use #1500ff for anything other than the primary CTA fill — not for links, not for icons, not for hover states, not for badges
- Never add drop shadows or elevation glows to cards — the system uses surface color shifts (#050505 → #151515 → #1e1e1e) for hierarchy, not shadows
- Never set body text below 16px for primary content — captions and metadata can go to 13-14px, but main copy stays large
- Never introduce additional accent colors, even in illustrations or partner logos — the partner strip stays grayscale to preserve the indigo's dominance
- Never use border-radius values between 0px and 9999px for buttons — the system is binary: fully rounded pills or 14px card corners, nothing in between
- Never apply gradients to backgrounds, buttons, or text — the system is flat monochrome with one solid color exception
- Never use line-height above 1.50 for any text size — the tight line-heights (0.96-1.38) are the system's editorial signature

## Components

### Primary Pill Button

Electric Indigo (#1500ff) background, Paper (#fdfdfd) text at 14-16px weight 500, fully rounded 9999px radius, 12px 24px padding. This is the only place the brand color lives — every other interactive element defers to it. Appears once per viewport maximum to preserve its impact.

### Ghost Pill Button

Transparent background, 1px Paper (#fdfdfd) border at ~30% opacity or full opacity, Paper text at 14px weight 500, 9999px radius, 10px 20px padding. Used for 'Sign up' and 'Join over 1M users' — the outlined variant lets the primary indigo button own the hierarchy.

### Navigation Bar

Transparent background floating on the Obsidian canvas. Logo at left in Paper white, text-only nav links (Features, Marketplace, What's new, Reviews) centered in Pearl (#d4d4d4) at 14px, auth actions (Log in, Sign up) at right. No background fill, no shadow, no border — the nav exists purely as type on the void.

### Display Headline

96px Savee Font weight 500, Paper (#fdfdfd), line-height 0.96, letter-spacing -0.04em. The extreme tightness and massive scale make it read as a single sculptural block. Centered horizontally with generous top/bottom breathing room (64-80px). The hero is centered single-column — no split layout, no side imagery.

### Editorial Body Block

36px Savee Font weight 400, Paper (#fdfdfd), line-height 1.13, letter-spacing -0.01em. This is body copy at headline scale — 36px is massive for prose, creating a magazine-like reading experience. Left-aligned, max-width ~800px, sits below the hero with 48-64px separation.

### Partner Logo Strip

Single horizontal row of grayscale brand logos (Apple, Google, Nike, Adobe, Pentagram, Airbnb, MWS) in Ash (#a3a3a3) or Pearl (#d4d4d4), evenly distributed across the full content width. Preceded by a small caption in Stone (#737373) at 13px. No logos colored, no hover effects — the strip is quiet authority.

### Product Preview Frame

Charcoal (#151515) background surface filling most of the viewport width, 14px border-radius, no border, no shadow. The subtle lift from canvas (#050505) to surface (#151515) is the only elevation cue — no drop shadows are used anywhere in the system.

### Text Link

Inherits body color (Paper or Pearl) with underline on hover only. No chromatic links — even interactive text stays in the neutral palette, reserving Electric Indigo exclusively for the primary CTA.

### Subhead Caption

16-18px Savee Font weight 400, Pearl (#d4d4d4), centered, line-height 1.50. Sits 16-24px below the display headline. The muted color creates a clear visual step-down from the headline without using a different size or weight.

### Full-Width Section Spacer

64-80px of pure Obsidian canvas with no visual element. Sections breathe into the void — no dividers, no background color shifts, no gradient transitions. The darkness itself is the separator.

### Footer Divider

1px horizontal line in Slate (#2f2f2f) or Silver (#e5e5e5) at ~10% opacity, spanning the content width. The only structural border in the entire system — used to separate the footer from the page body.

## Similar Design Systems

- {'why': 'Same near-black canvas, oversized editorial typography, single-color or minimal palette, text-dominant hero with no decorative imagery', 'business': 'Are.na'}
- {'why': 'Same dark-mode product UI with one vivid accent color (Linear uses #5e6ad2 indigo, Savee uses #1500ff), pill-shaped controls, tight line-heights, and surface color stepping instead of shadows', 'business': 'Linear'}
- {'why': 'Same confident use of large-scale display type (90px+) with tight tracking on dark backgrounds, minimal color, and generous vertical breathing room between sections', 'business': 'Pitch'}
- {'why': 'Same dark gallery aesthetic for creative tools, pill-shaped CTAs, and the strategy of reserving color exclusively for the single most important action', 'business': 'VSCO'}
- {'why': 'Same near-black background, pure white type, single blue accent for primary action, pill controls, and the philosophy that restraint in color creates confidence in the product', 'business': 'Things 3 (Cultured Code)'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #fdfdfd
- background: #050505
- border: #e5e5e5
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
- primary action: no distinct CTA color

**Example Component Prompts**


2. Create an editorial body section: #050505 background. Left-aligned prose at 36px Savee Font weight 400, #fdfdfd, line-height 1.13, letter-spacing -0.36px. Max-width 800px. No drop shadows, no card backgrounds — text sits directly on the void.

3. Create a product preview frame: #151515 background, 14px border-radius, full content width (max 1200px), no border, no shadow. Suggests a dark app interface screenshot.


5. Create a partner logo strip: single horizontal row of 8 grayscale logos in #a3a3a3, evenly spaced across full content width. Preceded by a caption at 13px #737373 reading 'Used by leading design studios and teams'. No colored logos, no hover effects.

## Radius Philosophy

The system uses exactly two radius values: 9999px for all interactive elements (buttons, tags, pills, inputs) creating a soft pill shape, and 14px for all passive surfaces (cards, product frames, preview containers). No 4px, no 8px, no 16px. The pill controls and the softly rounded cards together define the system's tactile language — buttons feel like physical pills you press, surfaces feel like slightly rounded frames. This binary radius vocabulary is as important as the color palette to the system's identity.
