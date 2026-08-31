# xAI — Design System

> **North Star**: warm cream laboratory with a black pill
> **Theme**: light
> **Source**: https://x.ai
> **Refero Style**: https://styles.refero.design/style/3b83dfe4-2f53-4a4d-819d-e6045ca5f7dc
> **Synced**: 2026-09-01

## Overview

xAI runs a restrained near-monochrome editorial system on a warm-white canvas. Type leads the visual hierarchy: oversized display headlines at near-100% line-height with tight negative tracking sit above generous breathing room, while GeistMono punctuates the interface with terminal/code fragments. The single defining interaction is a pill-shaped, pure-black filled button — everything else is ghost, outlined, or surface-toned. Cards are flat, borderless, and warm-cream (#f9f8f6); depth comes from a single hairline ring rather than shadow stacks. Color is rationed: a warm off-white page, cream cards, near-black ink, and the occasional vivid accent (Beta pill, traffic-light terminal dots, gradient orbs) that earns attention precisely because the rest of the page refuses it.

## Color Palette

- **Jet Ink**: `#0a0a0a` — Primary text, filled CTA buttons, logo mark — near-black anchors the hierarchy without the harshness of pure black [neutral]
- **Charcoal**: `#151515` — Dark code-block surface behind terminal demos (used where black feels too stark against warm white) [neutral]
- **Fog**: `#858585` — Secondary text, icon strokes, inactive nav items — the most-used gray; carries the bulk of body and link copy [neutral]
- **Pewter**: `#9d9d9d` — Tertiary text, meta labels, decorative fills — softer than Fog for de-emphasized utility copy [neutral]
- **Steel**: `#545454` — Mid-weight body text where Fog reads too washed out (inline stats, spec lines) [neutral]
- **Dove**: `#d5d9e2` — Hairline borders, input rings, button focus outlines — the only border color in the system [neutral]
- **Cream**: `#f9f8f6` — Card surfaces, secondary panels, tag backgrounds — warm off-white distinguishes layered surfaces from the pure-white page [neutral]
- **Paper**: `#ffffff` — Page background, button text on filled CTAs, icon foreground on dark surfaces [neutral]
- **Sand**: `#f2ede5` — Warm wash backgrounds, subtle highlight zones, section tints [neutral]
- **Slate**: `#3b3b3b` — Muted heading variant for secondary headlines and section labels [neutral]
- **Ember**: `#ff5f57` — Terminal traffic-light dot (red) — decorative accent inside code-block mocks only [accent]
- **Sunbeam**: `#ffbd2e` — Terminal traffic-light dot (yellow), and the Beta pill background — the single warm accent that signals novelty [accent]
- **Sprout**: `#28c840` — Terminal traffic-light dot (green) — decorative accent inside code-block mocks only [accent]

## Typography

- **universalSans**
- **universalSansDisplay**
- **GeistMono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 20 |
| body-sm | 14 | — | 20 |
| body | 16 | — | 24 |
| heading-sm | 24 | — | 32 |
| subheading | 30 | — | 36 |
| heading | 48 | — | 48 |
| heading-lg | 60 | — | 60 |
| display | 72 | — | 72 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 40px
- **Element Gap**: 12px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '16px', 'pills': '9999px', 'inputs': '6px', 'buttons': '9999px', 'smallCards': '8px'}

## Layout

Layout is max-width centered (~1200px) on a full-bleed white canvas, with generous vertical rhythm (80px section gaps). The hero is text-first: a centered headline stack on white with two CTAs below, followed by a 2-column product-card row (Chat / Code) at comfortable density. Below the hero, the page alternates into single-column feature blocks (One API. Every modality.) with text-left and code-panel-right splits, then a 4-column news index, then a 2-column pricing/CTA tier. Navigation is a single sticky top bar (64px) with logo + horizontal menu + two right-aligned action buttons. The page never uses a sidebar; content density stays low. Cards are flat and borderless — the cream surface alone carries the grouping. The sticky header adopts a backdrop-blur (12px) and hairline bottom border on scroll.

## Surfaces / Elevation

- **Paper**
- **Cream**
- **Sand**
- **Charcoal**

**Shadow tokens:**

## Imagery

Imagery is product-screenshot-driven, not lifestyle. The hero and feature tiles contain in-context product captures: a chat thread rendered as a UI mockup, a code editor with syntax-highlighted TypeScript, a voice waveform on a cream card, a code-snippet panel on a warm gradient backdrop. All product visuals sit inside flat cream containers with no rounded inner edges masking the media. Decorative warmth comes from large radial gradient orbs (peach/coral) that bleed behind code panels — blurred at 64px, they read as ambient glow rather than imagery. Photography is absent; the system is pure UI + illustration + gradient. Icons are stroke-based, 1.5px weight, Fog (#858585) by default with Jet (#0a0a0a) on hover. No 3D renders, no stock photography, no human figures.

## Design Principles

### Do

- Use #0a0a0a for the primary filled button — never substitute a chromatic CTA color; the system is intentionally monochrome
- Set all headlines (24px+) with letter-spacing -0.025em and line-height 1.0–1.33; lock them to the type grid rather than centring them visually
- Apply radius 9999px to every button, tag, and language tab; the pill is the system's signature shape
- Use #f9f8f6 for any surface that sits above the page; let the warm cream alone separate layers — avoid shadows
- Reach for GeistMono whenever content is technical (code, terminal, tabs, metadata); reserve universalSans for editorial and UI copy
- Keep the Beta pill to feature-release moments only (#f2ede5 background, 12px weight 500); do not introduce other accent pills
- Default to ghost/outlined buttons for any action that is not the page's single primary conversion

### Don't

- Do not use chromatic colors for buttons or links — the only saturated color on a page should be a single Beta pill or a terminal dot
- Do not stack shadows; the system uses a single hairline ring (1px solid #d5d9e2) as the sole depth cue
- Do not set body text below 14px or above 18px on screen; the type scale jumps from 18 → 24 → 30 → 48 to preserve hierarchy through size alone
- Do not add background colors to nav links, news cards, or inline list items — the page should read as quiet whitespace
- Do not use line-heights above 1.63 for running text; display headlines must stay at 1.0–1.33 to maintain the editorial lockup
- Do not introduce new radii; the system is binary — pills (9999px) or cream cards (16px), no intermediate rounding
- Do not use pure black (#000000) — always #0a0a0a; the slight lift keeps the dark surfaces on-brand warm rather than CRT-cold

## Components

### Filled Primary Button

Background #0a0a0a, text #ffffff, radius 9999px, padding 12px 20px, font 14px/20 universalSans weight 500. Used for 'Get API Access', 'Start Building', 'Try for free'. The single high-contrast element on the page; no border, no shadow.

### Ghost Secondary Button

Background transparent, text #0a0a0a, radius 9999px, padding 12px 20px, font 14px/20 universalSans weight 500. Pairs directly beside a filled primary as the soft alternative. No visible border by default; hover adds 1px #d5d9e2 ring.

### Compact Nav Button

Background #ffffff, text #0a0a0a, radius 9999px, padding 6px 12px, border 1px #d5d9e2. Smaller scale than hero buttons; sits in the sticky header alongside the filled primary.

### Beta Tag Pill

Background #f2ede5 (warm wash), text #0a0a0a, radius 9999px, padding 2px 8px, font 12px universalSans weight 500. Used inline before a feature label ('Beta  Grok Voice Agent Builder'). The only colored pill in the system.

### Flat Cream Card

Background #f9f8f6, radius 8–16px (asymmetric — inner mockup radius differs from card radius), padding 0, no shadow, no border. Card holds a media element (code mockup, audio waveform, image) flush to its edges; the surface tone alone separates it from the page.

### Pricing Tier Card

Background #f9f8f6, radius 16px, padding 40px on all sides, no shadow. Spacious interior with generous heading-to-body ratio. Uses universalSans weight 500 for tier name, weight 400 for spec lines.

### Terminal Code Block

Background #151515, radius 12px, padding not standardized, font GeistMono 12–13px. Traffic-light dots (#ff5f57, #ffbd2, #28c840) sit top-left at ~8px. Syntax highlighting uses a muted code palette (#032f62 keys, #91c17a strings, #d73a49 errors) — these are mockup-internal, not system tokens.

### Language Tab Pill

Radius 9999px, padding 6px 12px, font 13px GeistMono. Active state: background #0a0a0a, text #ffffff. Inactive: background transparent, text #858585. Sits beneath code-block mocks.

### Navigation Link

Font 14px/20 universalSans weight 500, text #858585 default → #0a0a0a on hover, no underline, no background. Underline appears only on focus. Dropdown indicators (▾) drawn with stroke #858585.

### News Card

Background transparent (inherits page), no border, no radius, no padding. Image at top with default radius, then date meta in 11px universalSans weight 400 #858585, then title in 16px weight 500 #0a0a0a. The absence of a card surface is intentional — news feels like an index, not a gallery.

### Feature Stat Block

Large number 18px universalSans weight 400 #0a0a0a stacked above 11px label #9d9d9d. No card wrapper; sits inline within a feature column.

### Checklist Row

UniversalSans 14px/20 weight 400 #0a0a0a. Leading check glyph in #0a0a0a stroke. Vertical stack with 8px row-gap; no dividers between rows.

## Similar Design Systems

- {'why': 'Same near-monochrome palette with one high-contrast filled pill CTA, and editorial-grade display headlines at near-100% line-height', 'business': 'Linear'}
- {'why': 'Same black-pill-on-white hero button system and tight negative tracking on display type, with similar hairline-border depth cues', 'business': 'Vercel'}
- {'why': 'Same warm-paper editorial tone with restrained color rationing and Geist-family type pairing for developer surfaces', 'business': 'Anthropic'}
- {'why': 'Same pill-shaped CTA convention, near-flat card surfaces, and use of one vivid gradient orb as the sole chromatic punctuation', 'business': 'Stripe'}

## Agent Prompt Guide

## Quick Color Reference
- Text: #0a0a0a (primary), #858585 (secondary), #9d9d9d (tertiary), #3b3b3b (muted heading)
- Background: #ffffff (page), #f9f8f6 (card), #f2ede5 (warm wash), #151515 (code mockup)
- Border: #d5d9e2 (hairline ring)
- Accent: #ffbd2e (Beta pill, terminal yellow)
- primary action: #0a0a0a (filled action)

## Example Component Prompts

1. Create a Primary Action Button: #0a0a0a background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Cream Product Card**: Background #f9f8f6, radius 16px, padding 0 (media flush to edges). Internal media is a terminal mockup: background #151515, radius 12px, GeistMono 13px with traffic-light dots (#ff5f57, #ffbd2e, #28c840) top-left.

3. **Pricing Tier Card**: Background #f9f8f6, radius 16px, padding 40px. Tier name in 24px universalSansDisplay weight 500, #0a0a0a. Spec lines in 14px universalSans weight 400, #858585. Checkmark rows: 14px weight 400 #0a0a0a with leading #0a0a0a check stroke, 8px row-gap.

4. **Language Tab Strip**: Pills at radius 9999px, padding 6px 12px, GeistMono 13px. Active: bg #0a0a0a, text #ffffff. Inactive: bg transparent, text #858585. Sits directly beneath a code-block mockup.

5. **News Index Card**: No surface, no border, no radius. Image at top (default radius), then 11px universalSans weight 400 #858585 date meta, then 16px weight 500 #0a0a0a title. Lives in a 4-column grid with 24px column-gap.

## Editorial Type System

The defining type choice is the pairing of universalSansDisplay (weight 400, not 500 or 700) at hero sizes with line-height locked to ~1.0. Headlines are not bold — they are massive and quiet. Negative tracking (-0.025em) tightens them without compressing letterforms, and the 1.0 line-height means the block becomes a typographic slab rather than a column of text. This is the anti-bold-headline system: authority through size and restraint, not weight. At smaller sizes the same family at weight 500 carries emphasis; GeistMono interrupts to mark technical territory. The three-font system (universalSans / universalSansDisplay / GeistMono) is intentionally narrow — there is no fourth voice.

## Orb and Gradient Vocabulary

Decorative warmth comes from two specific gradient patterns, used sparingly: (1) a radial coral/peach orb (#ff8868 → transparent, or #ffa888 → transparent) blurred at 64px that bleeds behind code-block panels, giving the developer surface a sunset glow without committing to a brand color; (2) a linear indigo→pink→orange→amber spectrum used as a single accent stripe behind logos or progress bars. These are page-atmosphere gradients, never used for buttons, text, or functional UI. Treat them as a third surface tier — visual depth without chromatic commitment.
