# Dub — Design System

> **North Star**: frosted link dashboard on rice paper
> **Theme**: light
> **Source**: https://dub.co
> **Refero Style**: https://styles.refero.design/style/b0d80806-b724-4ed1-a1d1-074edd3c9bc9
> **Synced**: 2026-09-01

## Overview

Dub's visual system is a quiet, almost editorial SaaS aesthetic — a near-white canvas held together by hairline borders rather than elevation, with dense monochrome typography doing the structural work and one electric blue (#2563eb) doing the talking. Surfaces stay flat and borderless-looking at a glance, but every container carries a 1px #e5e5e5 edge that creates a printed-document feel. The personality comes from a small vocabulary of colored 'feature pill' accents (orange, green, violet) that float above the otherwise neutral palette, and from Satoshi-weight-500 display headlines that read as confident and contemporary without being loud. Components are compact and dense: 8px gaps, 12px card radius, pill-shaped tags at 9999px, and ghost controls instead of heavy filled buttons.

## Color Palette

- **Canvas White**: `#ffffff` — Page background, card surfaces, popover panels — the absolute base of every screen [neutral]
- **Paper Mist**: `#f5f5f5` — Subtle alt-surface for nested cards, secondary panels, and hover fills [neutral]
- **Ash**: `#e5e5e5` — Hairline borders on cards, inputs, and dividers — the structural line that holds the system together [neutral]
- **Smoke**: `#d4d4d4` — Stronger borders for emphasis containers and secondary button outlines [neutral]
- **Pebble**: `#c8c8c8` — Medium-contrast borders, control outlines, and structural separators. Do not promote it to the primary CTA color [neutral]
- **Midnight Ink**: `#0a0a0a` — Primary button text, high-emphasis buttons, nav text — near-black for maximum contrast [neutral]
- **Charcoal**: `#171717` — Body text, button text, default heading color — slightly softer than pure black [neutral]
- **Graphite**: `#262626` — Secondary text, icon strokes, subtle UI elements [neutral]
- **Slate**: `#404040` — Tertiary text, nav hover states, subdued iconography [neutral]
- **Steel**: `#525252` — Muted body text, helper text, less-prominent labels [neutral]
- **Fog**: `#737373` — Placeholder text, disabled states, link text in rest state [neutral]
- **Silver**: `#a3a3a3` — Disabled iconography, decorative strokes, very light dividers [neutral]
- **Electric Blue**: `#2563eb` — Primary brand color — logo, links, key metric highlights, active states, icon accents. Saturated blue against white gives the system its one moment of visual voltage [brand]
- **Deep Sapphire**: `#1e40af` — Primary action button background, high-emphasis CTA fill — the single committed action color, used sparingly so it earns attention [brand]
- **Soft Mint**: `#dcfce7` — Gray outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color [accent]
- **Vivid Green**: `#16a34a` — Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Tangerine**: `#ea580c` — Orange text accent for links, tags, and emphasized short phrases. [accent]
- **Lavender**: `#7c3aed` — Violet text accent for links, tags, and emphasized short phrases. [accent]
- **Conic Spectrum**: `#8b5cf6` — Decorative gradient — used as full-spectrum conic gradient on brand visuals and logo, never on UI elements [accent]
- **Primary Action Fill**: `#000000` — High-contrast neutral action fill for primary buttons on light surfaces. Use as the primary filled action background [neutral]

## Typography

- **Satoshi**
- **Inter**
- **Geist Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.5 |
| body | 14 | — | 1.43 |
| body-lg | 16 | — | 1.5 |
| body-xl | 18 | — | 1.56 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.33 |
| heading | 30 | — | 1.38 |
| heading-lg | 36 | — | 1.11 |
| display | 48 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '9999px', 'cards': '12px', 'inputs': '6px', 'buttons': '8px', 'largeCards': '16px'}

## Layout

The page follows a centered, max-width contained model at approximately 1200px. The hero is a centered text stack with three floating feature pills (Affiliate Programs, Conversion Analytics, Short Links) arranged horizontally above a large product mockup. Sections stack vertically with consistent 64px gaps, alternating between white canvas and the #f5f5f5 paper mist for tonal separation. The lower section uses a z-pattern: editorial text centered in the middle third, with floating UI cards anchored at the left and right margins, creating an asymmetric, magazine-like rhythm. The logo cloud is a simple 5×2 grid centered on the page. Navigation is a minimal top bar — logo left, nav center, two-button cluster (ghost Log in + filled Sign up) right — with no sticky or mega-menu behavior. The dashboard mockup in the hero shows a classic 2-column app shell: fixed sidebar (240px-ish) + content area, establishing the product's information density for visitors before they scroll.

## Surfaces / Elevation

- **Canvas**
- **Paper**
- **Card**
- **Tinted Accent**

**Shadow tokens:**

## Imagery

Imagery is product-first, not lifestyle. The hero centers a large dashboard screenshot — a real product mockup with sidebar nav, data table, and floating UI elements — presented as a flat panel on the white canvas. Customer logos appear in a desaturated grayscale grid (beehiv, superpower, Chatbase, etc.) for social proof, stripped of color so the page's single blue accent stays dominant. Floating partner cards (small profile + revenue/payout tiles) drift around editorial text blocks in the lower section, giving a sense of depth without using shadows on the text itself. The dotted grid background pattern is a signature: a fine array of small dots at very low opacity creates texture and a sense of a design system / blueprint surface, reinforcing the 'modern link attribution platform' positioning. Iconography is small, outlined-to-filled, and uses the accent palette (orange tangerine, violet lavender, green mint) for feature tags. No photography, no illustrations, no 3D — the product UI IS the visual language.

## Design Principles

### Do

- Use #e5e5e5 for all container borders — 1px solid is the default structural line, not shadows
- Reserve #1e40af (Deep Sapphire) for exactly one primary action per surface — never use it decoratively
- Use Satoshi weight 500 at 36–48px for display headlines; switch to Inter for everything 30px and below
- Use 9999px radius for all tags, badges, and pill-shaped indicators; 8px for buttons; 12px for cards; 16px for large feature cards
- Use 16px as the canonical body text size with lineHeight 1.5; drop to 14px for dense data and 11–12px for micro-labels
- Apply the soft tint palette (#dcfce7 mint, #dbeaff blue, light yellow) to small badge backgrounds and feature highlights — not to large surfaces
- Keep imagery as product UI mockups and desaturated logos; avoid stock photography and decorative illustrations

### Don't

- Don't use heavy drop shadows for card elevation — the system relies on 1px borders, not depth, to define containers
- Don't use pure black (#000000) for body text — use #171717 or #0a0a0a for slightly softer contrast
- Don't apply the Electric Blue (#2563eb) to large background fills — it's a highlight color, not a surface color
- Don't use multiple chromatic colors on a single component — each pill or feature tag gets exactly one accent
- Don't use Satoshi at body sizes — Satoshi is display-only (36px+); Inter handles everything below 30px
- Don't use radii outside the defined vocabulary (9999px, 16px, 12px, 8px, 6px) — ad-hoc rounding breaks the system's rhythm
- Don't use color for decorative gradients on UI elements — the conic spectrum gradient is reserved for the logo and brand visuals only

## Components

### Ghost Nav Button

Transparent background, #171717 text, 9999px radius, no border, 16px horizontal padding. Used for top-level nav items like Product, Solutions, Resources, Enterprise. No visible border until hover.

### Outlined Nav Button

White background (#ffffff), #171717 text, 1px #e5e5e5 border, 8px radius, 16px horizontal padding. Compact and quiet — the 'I'm here but I don't need to be seen' variant.

### Filled Dark CTA

Near-black background (#0a0a0a or #171717), white text, 8px radius, 16px horizontal padding. The committed action — used once per surface for the primary conversion goal.

### Outlined Action Button

White background, #171717 text, 1px #e5e5e5 border, 8px radius, 12px vertical / 16px horizontal padding. The workhorse button — used for most non-primary actions throughout the UI.

### Pill Feature Tag

Transparent or white background, small colored icon (orange/violet/green emoji-style glyph), #171717 label text, 9999px radius, 12px vertical / 16px horizontal padding. These floating pills (Affiliate Programs, Conversion Analytics, Short Links) are the system's signature decorative element.

### Pill Badge

Transparent or white background, #0a0a0a text, 9999px radius, minimal padding. Used for small notification dots, version labels, and category markers.

### Dashboard Card

White background (#ffffff), 1px #e5e5e5 border, 12px radius, 8px internal padding. The most frequent component (57 variants) — flat, border-defined, no shadow. Rely on borders and spacing for visual structure, not elevation.

### Elevated Feature Card

White background, 16px radius, 16px padding, subtle box-shadow: rgba(0,0,0,0.1) 0px 0px 0px 4px ring effect. Used sparingly to lift hero product mockups and featured content above surrounding flat cards.

### Muted Alt Card

Light gray background (#fafafa), 16px radius, 16px padding, no border. Provides tonal contrast when nesting content inside a white card or on the white canvas.

### Dashboard Table Row

Transparent or white background, 1px #e5e5e5 bottom border, 16px row height, 14–16px text. Minimal vertical density — rows breathe with generous padding for scannability.

### Status Badge (Pending/Completed)

Tinted background (soft mint #dcfce7 for completed, light yellow/orange wash for pending), small colored dot icon, dark text, pill radius (9999px), 6px vertical / 10px horizontal padding. Compact inline state communication.

### Sidebar Nav Item

Transparent or light blue (#dbeaff) active background, 8px radius, #171717 text, 12px vertical / 8px horizontal padding. Active state uses a soft chromatic fill rather than a bold left-border indicator.

### Input Field

White background, #111827 text, 1px #000000 border (distinctive — inputs use near-black border instead of #e5e5e5 for emphasis), 6px radius, 8px vertical / 12px horizontal padding. The black border is a signature: inputs feel important, not optional.

### Logo Cloud Item

Transparent background, grayscale (#262626 to #737373) wordmark, no border, centered in grid cell. Logos desaturated to harmonize with monochrome palette — color appears only in active or interactive states.

### Product Mockup Container

White background, 16px top-left/top-right radius (asymmetric — bottom is flush), subtle 4px outer ring shadow for depth. Container is a window into the product, not a framed picture — it sits on the canvas like a floating panel.

## Similar Design Systems

- {'why': 'Same light-canvas + monochrome + single-accent approach, with similar compact density and 1px-border container treatment over heavy shadows', 'business': 'Linear'}
- {'why': 'Geometric sans-serif headlines at weight 500 (not bold), hairline borders, white-on-white card surfaces with 12px radius, and a restrained color palette that lets the product UI do the visual work', 'business': 'Vercel'}
- {'why': 'Open-source SaaS with the same pill-button + flat card aesthetic, similar use of small colored feature tags floating above monochrome layouts, and Inter as the primary workhorse font', 'business': 'Cal.com'}
- {'why': 'Editorial-meets-dashboard layout with centered text stacks, floating UI cards, dotted grid background texture, and a near-monochrome palette with a single accent color for emphasis', 'business': 'Plausible Analytics'}
- {'why': 'Compact information density, border-defined containers instead of shadows, pill-shaped status indicators, and a confident use of one saturated accent (blue) against near-black text', 'business': 'Raycast'}

## Agent Prompt Guide

## Quick Color Reference
- Text primary: #171717
- Text muted: #737373
- Background: #ffffff
- Surface alt: #f5f5f5
- Border: #e5e5e5
- Accent: #2563eb
- primary action: #000000 (filled action)

## Example Component Prompts
1. **Hero Feature Pill**: Transparent background, 9999px radius, 8px vertical / 16px horizontal padding. Small colored emoji-style icon (orange tangerine #ea580c for 'Short Links', violet #7c3aed for 'Conversion Analytics', green #16a34a for 'Affiliate Programs') + 14px Inter weight 500 #171717 label. No border.

2. **Dashboard Card**: White (#ffffff) background, 1px #e5e5e5 border, 12px radius, 16px padding. Content inside uses 14–16px Inter weight 400 #171717. No shadow — borders define the container.

3. Create a Primary Action Button: #000000 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

4. **Outlined Action Button**: White (#ffffff) background, #171717 text, 1px #e5e5e5 border, 8px radius, 6px vertical / 12px horizontal padding. 14px Inter weight 500. Use for secondary actions like 'Learn more' or 'View invoices'.

5. **Display Headline**: Satoshi weight 500, 48px, lineHeight 1.0, color #171717. No letter-spacing adjustment. Use only for the largest hero and section titles — switch to Inter for anything 30px or below.

## Border-First Elevation Philosophy

Dub deliberately uses 1px borders over shadows as the primary container-defining mechanism. The base border color is #e5e5e5 at 1px solid — used 1942 times across the system, making it the most deployed visual element. Shadows are reserved for three specific cases: (1) a barely-there 1px lift on primary buttons (rgba(0,0,0,0.05) 0px 1px 2px), (2) a 4px outer ring on elevated feature cards and product mockups to create a 'floating panel' effect, and (3) the layered 10px/4px shadow stack on hero showcase elements. The philosophy: borders create a printed-document clarity that's better for information-dense SaaS UIs, while shadows are saved for moments that need to truly pop off the page. This is the opposite of Material Design's shadow-heavy approach.

## Pill Architecture

The 9999px radius is deployed 367 times — the second most common radius token. It's used for: feature category tags, status badges, notification dots, partner avatars, and pill-shaped nav elements. Combined with the 8px and 12px radii for buttons and cards, the system has a clear three-tier radius vocabulary: pills (9999px) for tags and badges, medium (8–12px) for buttons and cards, large (16px) for feature surfaces. This tight radius discipline is a key part of what makes the design feel intentional and cohesive.
