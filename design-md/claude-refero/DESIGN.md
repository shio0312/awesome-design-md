# Claude — Design System

> **North Star**: Warm parchment printed artifact — ink on bone paper, clay as the only chromatic breath.
> **Theme**: light
> **Source**: https://claude.ai
> **Refero Style**: https://styles.refero.design/style/47cb86b6-cb2d-41c8-94ba-8607cd7c41cd
> **Synced**: 2026-09-01

## Overview

Claude presents a warm-paper editorial interface: off-white parchment canvas (#f8f8f6) replaces the usual cold-white SaaS backdrop, paired with a near-black warm charcoal (#121212) for typography that reads as ink on paper rather than pixels on glass. The system is deliberately monochrome — the only chromatic accent is clay orange (#d97757), used sparingly as a signature mark rather than a call-to-action flood. Typography is the hero: Anthropic Serif sets the emotional headlines (the rare serif in tech), Anthropic Sans carries everything else at restrained weights (400-580), creating a hierarchy through size and weight contrast rather than color. Surfaces are flat with generous corner radii (16-24px on cards, 8px on controls), minimal shadow, and hairline borders — the aesthetic of a printed document rather than a digital product.

## Color Palette

- **Bone Parchment**: `#f8f8f6` — Page canvas, large background areas, nav bar, secondary cards [neutral]
- **Paper White**: `#ffffff` — Elevated card surfaces, primary content surfaces above the canvas [neutral]
- **Soft Stone**: `#efeeeb` — Nested card surfaces, subtle background variation, alternate section bands [neutral]
- **Carbon Ink**: `#121212` — Primary text, headings, icon fills — warm near-black rather than pure black [neutral]
- **Graphite**: `#373734` — Secondary headings, button text, nav text — softer than carbon [neutral]
- **Ashen**: `#7b7974` — Muted helper text, captions, fine print, disclaimer copy [neutral]
- **Pebble**: `#9c9a92` — Tertiary text, copyright, very low-priority labels [neutral]
- **Mist**: `#b7b7b5` — Hairline nav dividers, subtle border lines [neutral]
- **Chalk**: `#e7e6e1` — Decorative illustration fills, soft background tints [neutral]
- **Obsidian**: `#000000` — Footer background — only true black on the page [neutral]
- **Clay**: `#d97757` — Orange decorative accent for icons, marks, and small graphic details. Do not promote it to the primary CTA color [accent]

## Typography

- **Anthropic Serif**
- **Anthropic Sans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.5 |
| body | 14 | — | 1.5 |
| heading-sm | 24 | — | 1.33 |
| heading | 30 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 8-12px
- **Section Gap**: 64-80px
- **Border Radius**: {'nav': '8px', 'cards': '16px', 'inputs': '8px', 'buttons': '8px', 'elevatedCards': '24px'}

## Layout

Claude uses a max-width contained layout centered around 1200px on the Bone Parchment canvas. The hero pattern is a centered editorial headline in Anthropic Serif over generous whitespace, often paired with a full-bleed product image below the fold. Sections flow as alternating light bands — Bone Parchment canvas with white cards floating on it, occasional Soft Stone (#efeeeb) bands for visual rhythm. Content arrangement alternates between centered stacks (headlines, FAQs, CTAs) and asymmetric 2-column layouts (text-left/image-right feature blocks). Pricing uses a 3-column card grid (Free, Pro, Max) with elevated featured tier. Navigation is a minimal top bar: logo left, link cluster right, no heavy borders or fills. Vertical spacing is generous — 64-80px between sections, 32px within cards — creating a printed-page cadence rather than a dense product UI.

## Surfaces / Elevation

- **Page Canvas**
- **Card Surface**
- **Nested Surface**
- **Dark Band**

**Shadow tokens:**

## Imagery

Imagery is sparse and editorial in tone. Product photography and illustrations appear full-bleed within hero or feature sections, treated with generous corner radii (16-24px) and no decorative borders. The Clay orange accent (#d97757) appears in select illustration details — hands, objects, ornamental marks — reinforcing the warm paper aesthetic. Icons are mono Carbon Ink, outlined or filled at consistent weight, never multicolor. The overall density is low: most sections are text-dominant with imagery appearing as punctuation rather than spectacle. No gradients, no glow effects, no 3D renders.

## Design Principles

### Do

- Use Bone Parchment (#f8f8f6) as the default page canvas — never pure white for large backgrounds.
- Set display headlines in Anthropic Serif weight 400 at 30px with line-height 1.2; let the serif do the work, not weight.
- Keep the palette monochrome — the only chromatic color is Clay (#d97757), reserved for decorative marks and editorial accents, never button fills.
- Use 24px radius for elevated cards and 16px for nested/secondary cards; 8px for all buttons, inputs, and nav controls.
- Maintain generous section spacing: 64-80px between major sections, 32px card padding, 8-12px between elements within a component.
- Pair Carbon Ink (#121212) text with Paper White (#ffffff) cards on Bone Parchment (#f8f8f6) for the layered paper effect.
- Reference warm grays (Graphite, Ashen, Pebble) for text hierarchy — never introduce a second chromatic for emphasis.

### Don't

- Don't introduce button fills in Clay orange or any chromatic color — actions stay dark on light or light on dark.
- Don't use pure black (#000000) for body text — Carbon Ink (#121212) is warmer and reads as ink, not void.
- Don't set headlines at weight 700+ — the system speaks at weight 580 max for sans and 400 for serif.
- Don't apply heavy shadows to cards — shadow appears only as a soft 4px 20-24px wash at low opacity, or not at all.
- Don't use cool blues or greens for accent or brand — the system is deliberately warm monochrome.
- Don't set large display headlines in Anthropic Sans — the serif is the signature, the sans is the utility.
- Don't add decorative gradients — the design rejects them in favor of flat, printed-paper surfaces.

## Components

### Filled Dark Button

Dark carbon fill (#121212 or near-black), warm white text (#f8f8f6 or #fff), 8px radius, 8px vertical / 20px horizontal padding, 15px Anthropic Sans weight 500. The warmth of the text color on dark fill (f8f8f6, not pure white) keeps the button from feeling like a generic dark UI element.

### Pill Navigation Button

Transparent background, Graphite (#373734) text, no border, 8px radius, 15px sans weight 500. Sits on the Bone Parchment canvas (#f8f8f6) with generous horizontal padding. The nav bar is minimal — logo left, links centered or right, no heavy borders or fills.

### Pricing Tier Card

White (#ffffff) surface on Bone Parchment canvas, 24px radius, 32px padding all sides. Heading uses Anthropic Serif 24-30px. Price in Carbon Ink (#121212), description in Ashen (#7b7974). No shadow by default — a soft 4px 24px shadow at oklab warmth appears on hover or featured tiers. Hairline 1px border at #e7e6e1 optional.

### Feature Benefit Card

Soft Stone (#efeeeb) or Paper White (#ffffff) surface, 16px radius, generous internal padding (24-32px). Checkmark icons in Carbon Ink, body text at 14px in Graphite. Flat — no shadow. Creates a layered paper effect against the canvas.

### Editorial Section Header

Anthropic Serif 30px weight 400, line-height 1.2, Carbon Ink (#121212). Followed immediately by a short Ashen (#7b7974) body sentence at 16px. Generous 64-80px margin-top from the previous section.

### Footer Band

Obsidian (#000000) background — the only true black on the page, creating a deliberate tonal break. Text in muted gray (#9c9a92), links in Pebble or lighter. Multi-column grid with product/resource/company groupings. Compact 14px sans throughout.

### Inline Link

Color shifts between default (Graphite #373734) and hover (Carbon Ink #121212) with underline. No chromatic color — the system treats links as typography, not as colored emphasis. Transitions on color/background-color at 0.2s ease.

### Input Field

Transparent or Paper White fill, 1px border at Pebble (#b7b7b5) or Mist, 8px radius, 14px sans. Focus ring uses the cds-focus-shadow pattern: inset page-color ring + outer accent ring + blue glow. No dramatic state color shift.

### FAQ Accordion Item

Borderless or hairline divider between items, question text in Graphite (#373734) at 14-16px sans, body expands below in Carbon Ink (#121212). Anthropic Sans carries the entire interaction — no serif in the FAQ body. Generous 24px vertical padding per item.

### Clay Accent Mark

Small Clay orange (#d97757) marks — dots, ornaments, illustration accents — that serve as the single chromatic breath in an otherwise monochrome system. Never used for button fills or large backgrounds.

### Status Badge

8px radius, 11-12px sans weight 500, low-contrast background tint with Carbon Ink or Graphite text. Rarely chromatic — stays in the warm-gray family to match the editorial tone.

## Similar Design Systems

- {'why': 'Same warm off-white canvas (#fbf9f6 territory), generous whitespace, flat card surfaces with soft radii, and restraint in using color — Stripe also keeps its palette nearly monochrome in marketing surfaces.', 'business': 'Stripe'}
- {'why': 'Dark and light mode mastery with minimal chromatic accents, generous card radii (16-24px), and tight typographic hierarchy — though Linear skews darker while Claude skews warm-paper.', 'business': 'Linear'}
- {'why': 'Editorial restraint: monochrome palette, generous spacing, serif-optional typography that prioritizes readability over visual spectacle.', 'business': 'Notion'}
- {'why': 'Warm-paper aesthetic with clay-adjacent accent palette, editorial typographic confidence, and a refusal to use typical SaaS blue as a brand color.', 'business': 'Arc Browser'}

## Agent Prompt Guide

**Quick Color Reference**
- Text (primary): #121212
- Text (secondary): #373734
- Text (muted): #7b7974
- Background (canvas): #f8f8f6
- Background (card): #ffffff
- Border (hairline): #b7b7b5 or #e7e6e1
- Accent (decorative only): #d97757
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Pricing tier card*: White surface (#ffffff) on Bone Parchment canvas (#f8f8f6). 24px radius, 32px padding. Plan name in Anthropic Serif 24px weight 400 (#121212). Price in Anthropic Sans 24px weight 580 (#121212). Description in 14px sans (#7b7974). Filled dark button at bottom: #121212 background, #f8f8f6 text, 8px radius, 8px/20px padding, 15px sans weight 500.

2. *Editorial hero section*: Bone Parchment (#f8f8f6) background, no border. Headline in Anthropic Serif 30px weight 400 (#121212), line-height 1.2. Subtext in Anthropic Sans 16px weight 400 (#373734). 64-80px vertical padding above and below. Optional Clay (#d97757) accent dot or mark beside the headline.

3. *FAQ accordion item*: Transparent background, no card. Question in Anthropic Sans 16px weight 500 (#373734). Body answer in 14px weight 400 (#121212). Hairline 1px bottom border at #e7e6e1. 24px vertical padding. No chevron icon color — use Carbon Ink (#121212).

4. *Footer band*: Obsidian (#000000) full-width background. Three or four columns of links. Link text in Pebble (#9c9a92), 14px sans. Copyright in 12px sans (#9c9a92). 64px vertical padding. No icons in footer link rows.

5. *Dark navigation button*: Transparent fill, Graphite (#373734) text, 8px radius, 15px Anthropic Sans weight 500, 20px horizontal padding. Hover transitions to Carbon Ink (#121212) at 0.2s ease. No border, no background fill.

## Editorial Typography System

The defining signature of this design system is the deliberate pairing of Anthropic Serif (headlines only, weight 400) with Anthropic Sans (everything else, weight 400-580). The serif appears at exactly two sizes: 24px and 30px, used exclusively for section titles, plan names, and editorial hero copy. The sans carries 11px through 24px across all UI roles — body, nav, buttons, labels, captions. Weight 580 is the heaviest weight in use; the system never reaches 600+. This creates a visual language where the serif whispers authority through typographic contrast alone, and the sans does all the functional heavy lifting. When rebuilding pages, resist the urge to bold up — let size and weight differential create hierarchy.

## Warm Monochrome Philosophy

Claude's palette is deliberately restricted to warm neutrals plus one chromatic accent. The near-black text colors (#121212, #373734) carry a subtle warmth that distinguishes them from clinical SaaS blacks. The canvas (#f8f8f6) and card surfaces (#ffffff, #efeeeb) form a paper-like progression: parchment → paper → vellum. The single accent — Clay (#d97757) — appears only in decorative contexts: small marks, illustration details, editorial flourishes. It is never used to fill buttons, highlight links, or draw attention to data. This restraint is the brand. Adding additional chromatic colors (blues for links, greens for success, reds for error) would break the system's editorial integrity.
