# Lightdash — Design System

> **North Star**: violet pixel-grid on drafting paper
> **Theme**: light
> **Source**: https://www.lightdash.com
> **Refero Style**: https://styles.refero.design/style/d0f65d12-a8e6-4631-99f7-bb7cdcd5b6c5
> **Synced**: 2026-09-01

## Overview

Lightdash operates as a calm, developer-first command center: a near-white canvas populated by slate-gray typography, subtle hairline borders, and one saturated violet (#5e4cff) that powers every interactive moment. The brand voice is confident and quiet — headlines are set in a custom geometric sans (Britti Sans) at 48–76px with aggressively tight tracking (-0.025em), making them feel architectural rather than decorative. Body copy uses Inter at 14–18px with slightly negative letter-spacing, keeping dense information readable without feeling heavy. Surfaces layer gently from #ffffff canvas to #f6f8fa sections to 12px-rounded cards, and a pixel-art violet mosaic in the hero is the only ornamental gesture — a deliberate nod to the 'code-native' identity. Components are flat and borderless-by-default; elevation is borrowed from layered rgba shadows tinted with the brand's slate (#272835) rather than neutral gray, which keeps every card visually on-brand.

## Color Palette

- **Canvas White**: `#ffffff` — Primary page background, card surfaces, input fills [neutral]
- **Cloud Mist**: `#f6f8fa` — Alternate section background, subtle surface tier below white [neutral]
- **Frost Tint**: `#eceff3` — Tertiary surface, muted background blocks [neutral]
- **Ash Border**: `#cdd2d9` — Hairline dividers, card borders, table separators [neutral]
- **Mist Border**: `#c1c7d0` — Secondary borders, disabled state outlines [neutral]
- **Fog Text**: `#a4abb8` — Helper text, link underlines in body copy, placeholder text [neutral]
- **Steel Text**: `#818898` — Muted metadata, timestamps, caption text [neutral]
- **Slate Body**: `#666d80` — Secondary body text, descriptions, supporting paragraphs [neutral]
- **Graphite Heading**: `#36394a` — Primary headings, strong body text, high-emphasis content [neutral]
- **Midnight Ink**: `#272835` — Dark surface fills, announcement bar, code terminal background, primary button background [neutral]
- **Onyx**: `#1a1b25` — Deepest text, high-contrast dark surfaces [neutral]
- **Volt Violet**: `#5e4cff` — Primary CTA fill, active link, brand accent — vivid violet against slate neutrals is the single chromatic punctuation of the entire system [brand]
- **Lavender Wash**: `#c8ccf3` — Muted accent background, hero pixel-art mid-tones, tag chips [accent]
- **Lilac Whisper**: `#dfdbff` — Tertiary accent surface, selected row tint, soft callout [accent]

## Typography

- **sans-serif**
- **Britti Sans Trial Semibold**
- **Britti Sans Medium**
- **Inter**
- **Inter Variable**
- **IBM Plex Mono**
- **Britti Sans Trial Regular**
- **Micro 5**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.63 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.3 |
| heading-sm | 24 | — | 1.25 |
| heading | 32 | — | 1.2 |
| heading-lg | 48 | — | 1.05 |
| display | 76 | — | 0.95 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 40px
- **Border Radius**: {'nav': '8px', 'cards': '12px', 'badges': '999px', 'inputs': '8px', 'buttons': '8px', 'special': '80px'}

## Layout

Layout is centered max-width 1200px with generous left/right padding. The hero is split-asymmetric: left two-thirds is headline + sub + CTAs, right one-third is the pixel-art mosaic. Below the hero, content alternates between white #ffffff and #f6f8fa bands at 40px section gaps. Feature sections use 2 or 3 column card grids with 12px radii. The product preview is a single full-width card with a browser-chrome frame. Customer logos sit in a centered 2x6 grid. Testimonials are centered at 600px max-width. Navigation is a single sticky 64px white bar with logo left, links center, auth right. Density is comfortable — pages breathe with whitespace rather than packing information tightly.

## Surfaces / Elevation

- **Canvas**
- **Cloud Section**
- **Frost Block**
- **Card Surface**
- **Terminal**

**Shadow tokens:**

## Imagery

Imagery is minimal and functional. The hero uses a custom pixel-art mosaic of violet squares (#5e4cff, #c8ccf3, #dfdbff) as the sole decorative element. Product screenshots appear inside browser-frame cards with macOS chrome, always set on white. Code/terminal screenshots use the dark #1a1b25 surface with IBM Plex Mono and violet syntax tokens. Customer logos are monochrome #36394a in a clean 2x6 grid. Avatars in testimonials render as 80px circular crops. There is no lifestyle photography, no full-bleed images, no abstract gradients — visuals are either product, code, logo, or the violet pixel motif.

## Design Principles

### Do

- Use #5e4cff (Volt Violet) for exactly one primary CTA per viewport — never pair it with another accent color on the same screen.
- Set display headlines in Britti Sans Semibold at 48-76px with -0.025em letter-spacing; this aggressive tracking is the signature of the brand voice.
- Set body copy in Inter at 14-18px with -0.01 to -0.02em tracking, never in pure #000000 — use #36394a (Graphite Heading) for strong text and #666d80 (Slate Body) for descriptions.
- Use 12px radius for all cards and 8px radius for all buttons, inputs, and nav elements — these two values are the system's structural constants.
- Default cards to 1px #cdd2d9 border with no shadow; reserve the multi-layer shadow stack for hero product previews and elevated feature cards only.
- Use the pixel-art violet mosaic (#5e4cff, #c8ccf3, #dfdbff, #ffffff tiles) as the single decorative flourish — it is the brand's only ornament.
- Tint all shadows with #272835 rgba values, never neutral gray — this keeps elevation on-brand.

### Don't

- Don't introduce additional chromatic accent colors — the system runs on slate neutrals plus one violet.
- Don't use #000000 for body text; the brand reads as #36394a (Graphite) which is softer and more distinctive.
- Don't center body copy in feature sections — only hero headlines and testimonials are centered; everything else is left-aligned.
- Don't apply heavy drop shadows to standard cards; 1px borders are the default, shadows are earned by elevation tier.
- Don't set headlines at line-height > 1.10; the 0.95 line-height at 76px is a deliberate compression.
- Don't use the Inter font for display sizes above 32px — Britti Sans owns the display tier, Inter owns body and UI.
- Don't use rounded shapes above 16px radius for standard UI; 80px and 999px are reserved for special elements (tab toggles, full-width brand blocks).

## Components

### Announcement Bar

Full-width #1a1b25 dark bar. 12px Inter Variable white text, centered, with inline link in #c8ccf3. Padding 8px vertical. No radius.

### Primary Navigation

White background, 64px height, 8px radius dropdowns. Logo (lightning bolt glyph) in #5e4cff on the left, nav links in #36394a at 14px Inter Medium, Login as text link, 'Book a demo' as ghost button (1px #cdd2d9 border, 8px radius), 'Start for free' as filled #272835 button with white text and 8px radius.

### Ghost Button

White background, 1px #cdd2d9 border, 8px radius, 10px 16px padding, 14px Inter Medium #36394a text. Hover darkens border to #818898.

### Primary Filled Button

Filled #272835 background, white text, 8px radius, 10px 20px padding, 14px Inter Medium. Or the brand-violet variant: #5e4cff fill, white text, 8px radius, used for one hero CTA per page.

### Violet Accent Button

#5e4cff fill, white text, 8px radius, 12px 24px padding, 14-16px Inter Medium. The single saturated moment in an otherwise monochrome page — use sparingly, at most one per viewport.

### Tab Toggle

Pill container, 999px radius, #f6f8fa inactive background, white active background with subtle shadow on the active tab. Text 14px Inter Medium, #666d80 inactive, #36394a active.

### Hero Section

White #ffffff canvas. Headline 56-76px Britti Sans Semibold #36394a with -0.025em tracking. Body 16-18px Inter Regular #666d80. Violet pixel-art mosaic decoration anchored to the right edge. CTAs stacked horizontally with 8-12px gap.

### Pixel-Art Hero Decoration

Scattered 4px-12px violet square tiles in a loose grid, anchored to the upper-right of the hero. Colors: #5e4cff (saturated), #c8ccf3 (muted), #dfdbff (pale), #ffffff (negative space). The only decorative flourish in the system.

### Product Preview Card

White surface with 12px radius and the multi-layer shadow stack (see elevation). Contains a macOS-style window chrome at top, then product UI inside. Sits on #f6f8fa section background.

### Code Terminal Card

#1a1b25 background, 12px radius, 16px padding, IBM Plex Mono 12px text in #a4abb8 with syntax tokens in #5e4cff and #c8ccf3. Provides visual contrast against the white page.

### Logo Grid Section

White background, 2-row x 6-column grid of customer logos, evenly spaced with 40px row gaps. Logos render monochrome in #36394a or original brand colors at 60% scale.

### Testimonial Block

Centered 18-20px Inter Regular #36394a quote, 600px max-width, preceded by a small violet pixel-art icon (#5e4cff). Avatar row of 5 headshots below in 80px circles.

### Feature Card

White surface, 12px radius, 16px padding, 1px #cdd2d9 border, no shadow by default. Heading 24px Britti Medium #36394a, body 14-16px Inter #666d80. Optional violet icon at top in #5e4cff.

### Input Field

White background, 1px #cdd2d9 border, 8px radius, 10px 12px padding, 14px Inter Regular #36394a text. Placeholder #a4abb8. Focus ring: 2px #5e4cff at 20% opacity.

### Badge / Tag

Pill shape (999px radius), #f6f8fa or #dfdbff background, 12px Inter Medium text, 4px 10px padding, #36394a or #5e4cff text.

## Similar Design Systems

- {'why': "Same single-accent restraint (Linear's purple vs. Lightdash's violet) and the same display-headline + tight-tracking combination on a near-white canvas.", 'business': 'Linear'}
- {'why': 'Monochrome-first system with a single saturated accent, hairline-bordered cards, and developer-facing code/terminal blocks embedded in light pages.', 'business': 'Vercel'}
- {'why': 'Open-source dev tool with a white canvas, slate-gray typography, and a violet accent used sparingly for primary actions only.', 'business': 'Cal.com'}
- {'why': 'Code-first product landing pages that mix a clean white UI surface with dark terminal previews, set in a custom geometric sans at large display sizes.', 'business': 'Cursor'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #36394a (Graphite Heading)
- background: #ffffff (Canvas White)
- border: #cdd2d9 (Ash Border)
- accent: #5e4cff (Volt Violet)
- secondary surface: #f6f8fa (Cloud Mist)
- primary action: #5e4cff (filled action)

**3-5 Example Component Prompts**
1. Create a Primary Action Button: #5e4cff background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. *Feature card*: White surface, 12px radius, 16px padding, 1px #cdd2d9 border, no shadow. Violet #5e4cff icon at top (24px). Heading at 24px Britti Sans Medium #36394a, letter-spacing -0.48px. Body at 16px Inter Regular #666d80, line-height 1.50.

3. *Product preview card*: White surface with browser-chrome top bar (3 traffic-light dots, #f6f8fa). 12px radius, multi-layer shadow stack tinted #272835. Contains a product screenshot inside at full width with 8px inner padding.

4. *Code terminal card*: #1a1b25 background, 12px radius, 16px padding. IBM Plex Mono 12px text — comments in #818898, keywords in #5e4cff, strings in #c8ccf3, plain text in #a4abb8.

5. *Tab toggle*: 999px radius outer pill, #f6f8fa background. Two 14px Inter Medium labels, inactive in #666d80, active in #36394a on white fill with a subtle 1px #cdd2d9 border and 2px shadow. 8px 20px padding on each tab.

## Signature Moves

Three choices define Lightdash's visual identity and should be preserved across every new screen:

1. **One violet per viewport.** The system runs on slate. A single #5e4cff CTA per screen is the maximum chromatic load. This restraint is what makes the violet feel switched-on rather than decorative.

2. **Britti Sans at display tier only.** The custom font appears at 48px and above. Inter handles everything below 32px. Mixing tiers creates a clear hierarchy: brand voice at the top, functional clarity below.

3. **Slate-tinted shadows.** Every shadow in the system uses rgba versions of #272835, not neutral gray. This subtle choice means even elevated surfaces feel cut from the same brand material rather than floating in generic space.
