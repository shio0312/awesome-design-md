# AgentQL — Design System

> **North Star**: Aurora glow over a midnight terminal
> **Theme**: dark
> **Source**: https://www.agentql.com
> **Refero Style**: https://styles.refero.design/style/d5307f56-76de-4d13-9741-f969c42e9aa5
> **Synced**: 2026-09-01

## Overview

AgentQL operates in a deep-space command-center register: near-black canvas, tightly letter-spaced Figtree display headlines, and a single pair of violet aurora glows (purple + pink radial gradients) that bleed from the hero into the background. The interface is overwhelmingly achromatic — white type, cool-gray secondary text, hairline borders in dark navy — with color reserved for two specific jobs: product surface highlights (a few cards lift into a slightly violet-tinted dark) and accent CTAs (a single blue→violet gradient pill). Components sit on flat dark surfaces with generous padding, rounded to 12px, and rely on heavy dark drop shadows rather than glow for depth. The overall feel is closer to a dark IDE theme than a marketing site — Inter carries the UI, IBM Plex Mono owns code blocks, and Figtree whispers the headlines at weight 500 with tight tracking.

## Color Palette

- **Void**: `#0b0c0e` — Deepest surface layer, page base under hero — the floor of the dark stack [neutral]
- **Abyss**: `#0e111b` — Primary page canvas and most card backgrounds; cool blue-black anchors the whole system [neutral]
- **Deep Sea**: `#0d172b` — Elevated card surface — sits one step above the canvas, used for feature and pricing cards [neutral]
- **Cobalt Panel**: `#12244f` — Highlighted card surface for feature spotlights; a violet-tinted lift that breaks the monochrome rhythm without becoming decorative [brand]
- **Frosted Lilac**: `#85a6e9` — Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color [brand]
- **Signal Blue**: `#2862d7` — Vivid blue link and accent text — the sharp chromatic punctuation against all the dark navy [brand]
- **Pulse Violet**: `#305fbd` — Mid-saturation violet-blue used in code-syntax blocks and gradient stops [brand]
- **Aurora Purple**: `#625fff` — Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color [accent]
- **Plasma Pink**: `#ff7dda` — Secondary hero glow bleeding from bottom-right — warm counterpoint to the aurora purple [accent]
- **Quartz**: `#ffffff` — Primary text and primary CTA fill — high-contrast white against the dark canvas [neutral]
- **Ash**: `#abaebb` — Secondary text and subtle hairline borders — the most-used neutral after white [neutral]
- **Mist**: `#c7c9d1` — Tertiary text, muted descriptions, helper copy [neutral]
- **Slate**: `#3c3f44` — Muted borders and disabled state outlines [neutral]
- **Obsidian Edge**: `#172540` — Primary border color on cards and buttons — defines component outlines against the dark canvas [neutral]
- **Inkline**: `#151e32` — Subtle card borders, slightly lighter than Obsidian Edge for inner nesting [neutral]
- **Sapphire Hairline**: `#24375a` — Lighter violet-tinted border for dividers and section separators [neutral]

## Typography

- **Inter**
- **IBM Plex Mono**
- **Figtree**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.38 |
| heading-sm | 28 | — | 1.25 |
| heading | 36 | — | 1.13 |
| heading-lg | 48 | — | 1.13 |
| display | 64 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 80px
- **Border Radius**: {'nav': '8px', 'tags': '9999px', 'cards': '12px', 'small': '2px', 'inputs': '8px', 'buttons': '9999px'}

## Layout

Centered max-width 1200px container, full-bleed dark canvas. The hero is a two-column split: left holds a two-line Figtree 64px headline with subtext and paired CTAs, right holds a multi-layered code-editor mockup that extends to the page edge. Below the hero, sections alternate between two patterns: (1) centered text blocks with a 36–48px heading and supporting copy, and (2) 2-column or 3-column card grids with 12–16px gaps. The integrations section is a full-width card with a 4×N logo grid flush right. The pricing section is a 3-column card grid with the middle column elevated via a violet-tinted fill. Section gaps are generous — 80px between major blocks — and the dark canvas flows seamlessly with no visible section dividers. Navigation is a single sticky transparent bar at the top with a left logo, centered nav links, and right-side social + CTA cluster.

## Surfaces / Elevation

- **Void**
- **Abyss**
- **Deep Sea**
- **Cobalt Panel**

**Shadow tokens:**

## Imagery

The visual language is code-first: the hero's right side is a layered composition of floating code-editor windows, file tabs, and data lists rendered as if captured from a dark IDE. These are not screenshots but illustrated product mockups with syntax highlighting in purple, blue, and muted pink against #0d172b panels. The hero is split — text-left, code-visual-right — and the code panels overlap with slight rotation and heavy black drop shadows (rgba(0,0,0,0.34) 0px 20px 35px) to create a stacked depth effect. The integration section uses isolated square tiles, each containing a single brand logo on a violet-tinted surface. No photography, no illustration, no 3D — the only 'decoration' is the two large radial gradient glows (purple and pink) bleeding from the hero corners, which double as atmospheric light source and brand identity.

## Design Principles

### Do

- Use 9999px radius for all interactive elements — buttons, badges, tags, and nav pills
- Use Figtree at weight 500 for all display text 32px and above with -0.02em tracking
- Use Inter weight 300–400 for body copy; let low weight do the work against the dark canvas
- Apply the aurora gradient pair (purple #625fff + pink #ff7dda) as large soft radial glows on dark hero sections only
- Layer surface colors in order: #0b0c0 → #0e111b → #0d172b → #12244f to indicate elevation without shadows
- Use #2862d7 or #305fbd for link text and code syntax, never for large fills
- Apply 1px borders in #172540 or #151e32 to define cards — avoid using shadows alone for card definition

### Don't

- Don't use bright fills on CTA buttons — white (#ffffff) is the primary action color, never a saturated blue or purple
- Don't place radial gradient glows inside content cards or feature sections — reserve for hero and section backgrounds only
- Don't use Inter for headlines 32px and above — Figtree owns the display register
- Don't use #12244f as a page background — it's a highlight surface, not a canvas
- Don't add color to secondary text — keep #abaebb and #c7c9d1 strictly achromatic
- Don't use sharp corners (0px radius) on any interactive element — minimum is 2px for code, 8px for inputs, 12px for cards
- Don't apply elevation shadows to ghost or outline buttons — they should sit flat against the canvas

## Components

### Primary CTA Button

Background #ffffff, text #050606, weight 500 Inter at 15–16px, border-radius 9999px, padding 10px 20px. No shadow, no border. 1px hairline border optional in #161618 for definition. Used for 'Get started', 'Get API key', 'Sign up for free trial', and 'Let's chat!'.

### Ghost Button

Background transparent, border 1px #777a88, text #ffffff Inter 500 at 15px, border-radius 9999px, padding 10px 20px. Used for 'Sign up' and 'Explore Playground' paired beside a primary CTA.

### Accent Gradient Button

Background linear-gradient(90deg, #305fbd, #625fff), text #ffffff Inter 500 at 14–15px, border-radius 9999px, padding 10px 20px. Used for 'See all examples' — a once-per-page accent.

### Feature Card

Background #0e111b or #0d172b, border 1px #151e32 or #172540, border-radius 12px, padding 24px. Card lifts with shadow rgba(0,0,0,0.5) 0px 4px 30px 0px when elevated. Contains a small icon, heading, and supporting text.

### Highlighted Card

Background #12244f, border 1px #1e2b48, border-radius 12px, padding 32px. Reserved for the 'Plays well with others' integration block and pricing 'Most Popular' tier. The violet-tinted fill and brighter border create visual priority without a shadow.

### Pricing Tier Card

Background #0d172b, border 1px #172540, border-radius 12px, padding 24px. Professional tier uses background #12244f and a 'Most Popular' pill badge in the top-right. Price rendered in Figtree 48–64px weight 500, feature list uses Inter 14–15px with 4–6px row gaps and checkmark icons.

### Code Snippet Block

Background #0d172b with #151e32 border, border-radius 12px, padding 16px. Header row contains a filename (Inter 13px #abaebb) and copy icon. Code body uses IBM Plex Mono 13px. Syntax colors: keywords in #ff7dda, strings in #28b6ff, comments in #8798c1, plain text in #c7c9d1. Line numbers in #3c3f44.

### Navigation Bar

Background transparent or #0b0c0 at 90% opacity, height 56–64px. Logo on left (Figtree 500), nav links in Inter 14–15px weight 400, social and CTA buttons on right. No visible border, no shadow. Active nav state uses text #ffffff, inactive uses #abaebb.

### Section Label

Inter 12–13px weight 500, uppercase, letter-spacing 0.02em, color #abaebb. Pairs with a 36–48px Figtree heading directly below.

### Integration Tile

Individual tile 80–96px square, background #0d172b with gradient overlay, border-radius 12px. Contains a centered brand logo on a slightly violet-tinted surface. Tiles arranged in a 4×N grid with 8–12px gaps.

### Badge / Tag

Background #12244f or #0d172b, text #85a6e9 or #ffffff, Inter 12px weight 500, border-radius 9999px, padding 4px 12px. Used for '#1 Product of the Day', '#1 Product of the Week', and 'Most Popular'.

### Feature List Item

Icon (checkmark or info) in #8798c1 at 16px, text in Inter 14–15px #c7c9d1, row gap 6–8px between items. Info icon triggers a tooltip or small info text.

### Stat Highlight Row

Icon + label in horizontal row, Inter 14–15px #c7c9d1, icon 16px in #8798c1. Items separated by 16–24px gaps, arranged in a 2-column grid inside signup prompt cards.

## Similar Design Systems

- {'why': 'Same dark canvas with subtle aurora-style radial glows and code-first product mockups as the hero visual', 'business': 'Replicate'}
- {'why': 'Near-identical aurora purple + pink radial gradient pattern on a near-black canvas with white pill CTAs', 'business': 'Together AI'}
- {'why': 'Dark IDE-inspired aesthetic with deep blue-black surfaces, Inter body type, and a single chromatic accent reserved for gradients', 'business': 'Cursor'}
- {'why': 'Same minimalist dark-mode language: heavy use of white text, cool-gray secondary type, and a tightly tracked geometric display font for headlines', 'business': 'Perplexity'}
- {'why': 'Achromatic dark surfaces with selective violet-blue accent glows and white pill buttons as the primary action pattern', 'business': 'Vercel'}

## Agent Prompt Guide

**Quick Color Reference**
- text (primary): #ffffff
- text (secondary): #abaebb
- text (tertiary): #c7c9d1
- background (canvas): #0e111b
- border: #172540
- accent / link: #2862d7
- primary action: #0d172b (filled action)

**3-5 Example Component Prompts**

1. **Hero section with headline + code visual**
   Create a Primary Action Button: #0d172b background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Feature card grid (3-column)**
   Card: background #0d172b, border 1px #172540, border-radius 12px, padding 24px. Icon: 24px in #2862d7 at top-left. Heading: Inter 20px weight 500, color #ffffff. Body text: Inter 16px weight 400, color #c7c9d1, line-height 1.5. Grid gap: 16px between cards, 80px between grid and next section.

3. **Code snippet block**
   Container: background #0d172b, border 1px #151e32, border-radius 12px, padding 16px. Header row: filename in Inter 13px #abaebb, copy icon in #8798c1. Code body: IBM Plex Mono 13px, line-height 1.5. Syntax colors — keywords #ff7dda, strings #28b6ff, comments #8798c1, plain text #c7c9d1. Floating drop shadow: rgba(0,0,0,0.34) 0px 20px 35px 0px, rgba(0,0,0,0.25) 0px 4px 13px 0px.

4. **Pricing tier card**
   Background #0d172b, border 1px #172540, border-radius 12px, padding 24px. Tier name: Inter 20px weight 500 #ffffff. Price: Figtree 48px weight 500 #ffffff with '/monthly' suffix in Inter 16px #abaebb. Feature list: checkmark icon 16px in #8798c1 + Inter 14px #c7c9d1, 8px row gap. CTA at bottom: white pill button (same as hero primary). Middle 'Most Popular' tier: background #12244f, border 1px #1e2b48, with a gradient badge pill at top-right.

5. **Section with eyebrow + heading + supporting copy**
   Eyebrow: Inter 12px weight 500 uppercase, letter-spacing 0.02em, color #abaebb. Heading: Figtree 48px weight 500, color #ffffff, letter-spacing -0.96px, line-height 1.13, centered. Body: Inter 18px weight 400, color #abaebb, centered, max-width 640px. Followed by a 3-column card grid below with 80px gap.
