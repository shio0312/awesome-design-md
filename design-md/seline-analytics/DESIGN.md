# Seline Analytics — Design System

> **North Star**: Quiet analyst's desk on warm paper
> **Theme**: light
> **Source**: https://seline.so
> **Refero Style**: https://styles.refero.design/style/7967c6d9-e50c-42b5-b4d1-74003ba41781
> **Synced**: 2026-09-01

## Overview

Seline sits on a warm-stone canvas (#fafaf9) with a single vivid cyan as its only chromatic accent — every other color is a neutral pulled from the Tailwind stone scale. Headlines use a custom geometric sans (roobert) at weight 400 with tight negative tracking, giving display copy an unhurried, almost whispered authority that contrasts with the usual SaaS shout. UI surfaces are flat white cards floating over the warm background via a single soft 16px-blur shadow; borders are 1px stone hairlines used generously as the primary structural device instead of heavy dividers or panels. The layout breathes: max-width content centered on generous vertical rhythm, with pill-shaped interactive controls, a mascot sticker illustration for personality, and data dashboard screenshots as proof-of-product. The overall feel is editorial analytics — calm, monochrome, confident — where the blue CTA is the loudest thing on the page by deliberate restraint of everything else.

## Color Palette

- **Stone Canvas**: `#fafaf9` — Page background — warm off-white that reads as paper, not screen-white [neutral]
- **Pure White**: `#ffffff` — Card surfaces, elevated panels, input fills — flat and shadowless by default [neutral]
- **Stone Border**: `#e8e6e5` — Hairline borders on cards, nav, inputs — the primary structural device, not dividers [neutral]
- **Stone Muted**: `#d6d3d1` — Secondary borders, subtle background tints, decorative separators [neutral]
- **Ash Gray**: `#a8a29e` — Muted helper text, icon strokes, disabled states — readable but recessive [neutral]
- **Warm Gray**: `#78716c` — Body text, nav links, secondary copy — warm-tinted neutral that softens body type [neutral]
- **Ink Black**: `#0c0a09` — Primary headings, emphasized body, strong icons — near-black with a warm cast [neutral]
- **Soot**: `#1c1917` — Dark surface backgrounds for inverted sections, dark dashboard tabs [neutral]
- **Sky Wash**: `#c1e1f7` — Soft highlight wash behind highlighted text spans, decorative blue tint [accent]
- **Cyan Signal**: `#3ba6f1` — Primary CTA fill, active links, brand icon strokes — the only chromatic voice on the page, used sparingly to make actions feel switched on [brand]
- **Cyan Edge**: `#3398e1` — Blue accent for outlined action borders, linked labels, and lightweight interactive emphasis. Do not promote it to the primary CTA color [brand]

## Typography

- **Roobert**
- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 2.3 |
| body-lg | 16 | — | 1.69 |
| subheading | 20 | — | 1.2 |
| heading-sm | 32 | — | 1.25 |
| display | 52 | — | 1.12 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 96px
- **Border Radius**: {'tags': '9999px', 'cards': '10px', 'icons': '4px', 'inputs': '6px', 'buttons': '9999px', 'feature-card': '16px'}

## Layout

Page is max-width centered at ~1200px with generous vertical breathing room. Hero is a two-row text block left-aligned with a single highlighted phrase ('simple & actionable') in cyan, followed by a dual-CTA row (cyan pill + ghost pill), then a row of grayscale partner logos, then a star-rating trust line, then a full-width floating dashboard preview that overlaps slightly into the next section. Below the fold: alternating single-column testimonial rows in a 2-column grid, then full-width feature sections with left-aligned text and centered product visuals. Navigation is a minimal top bar — logo left, centered nav links, sign-in + cyan CTA right — with a floating avatar cluster mid-nav as social proof. Section gaps are wide (96px) to create editorial pacing rather than dense information stacking.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Floating Preview**
- **Inverted Section**

**Shadow tokens:**

## Imagery

Visual language is dominated by product UI screenshots — the dashboard preview is treated as photography, rendered with a grayscale(1) contrast(0.94) filter that mutes the data colors to monochrome. The only human figure is a line-art mascot sticker (hooded character) drawn in outline-only SVG style, placed once per section as a playful counterweight to the analytical content, with a soft drop-shadow for sticker-like depth. Logo and brand glyphs are small black spark/flame marks. Photography is absent — no lifestyle, no team shots, no environment imagery. The object (the dashboard) IS the hero. All decorative icons are 1px-stroke outline style in either #0c0a09 or #3ba6f1, never filled.

## Design Principles

### Do

- Use Roobert at weight 400 for all display and heading sizes — never bump to 600/700 for emphasis, rely on size and the cyan highlight span instead
- Use #fafaf9 as the page background and #ffffff only for card surfaces — never invert this (white on canvas, not the other way around)
- Apply exactly one cyan highlight span (#3398e1 text + #c1e1f7 pill background) per headline to mark the value proposition keyword
- Use 1px #e8e6e5 borders as the primary structural separator inside cards — reserve shadows for product-preview cards only
- Keep buttons pill-shaped (9999px radius) with 8px 16px padding — the cyan filled CTA must be the only chromatic filled element on any screen
- Set body copy at 14px Inter weight 400 with 1.64 line-height — this is the dominant UI rhythm, do not break it
- Let the mascot sticker appear once per section as a personality beat — do not repeat or animate it

### Don't

- Do not introduce new accent colors — the entire palette is stone neutrals plus one cyan; adding green, purple, or red breaks the editorial restraint
- Do not use heavy drop shadows on content cards — the 16px-blur floating preview shadow is reserved for exactly one element per page
- Do not set headlines in Inter — Roobert at the 32px/52px sizes is the brand voice; mixing fonts breaks hierarchy
- Do not use #ffffff as the page background — always #fafaf9; pure white belongs only on elevated card surfaces
- Do not fill buttons with dark/neutral colors for primary actions — the cyan #3ba6f1 is the only correct filled-button color
- Do not add gradients, glassmorphism, or decorative color washes — the design is deliberately flat and paper-textured
- Do not stack multiple cyan highlight spans in one headline — one per headline maximum, the restraint is the point

## Components

### Primary CTA Button (filled cyan)

Pill shape (9999px radius), fill #3ba6f1, 1px border #3398e1, white text (#ffffff) weight 500, padding 8px 16px. The only chromatic filled element on the page — use once per viewport maximum.

### Secondary Ghost Button

Pill shape (9999px radius), transparent fill, 1px border #e8e6e5, text #0c0a09 weight 400, padding 8px 16px. Quiet companion to the cyan CTA.

### Navigation Link

No fill, no border, 14px Inter weight 400, color #78716c, padding 0 12px, height 32px. Hovers to #0c0a09. Dropdown caret inline at end.

### Signed-in Avatar Link

24px circles with 2px ring offset, -8px overlap spacing. Sits inline between nav items as proof-of-community. Avatars are real photos, no border.

### Flat Content Card

White (#ffffff) fill, 10px radius, 1px border #e8e6e5 (not shadow-dependent), 24px padding. Subtle shadow rgba(0,0,0,0.05) 0px 4px 16px 0px adds lift without weight. The border IS the structure.

### Floating Dashboard Preview

16px radius, white fill, shadow rgba(17,12,46,0.12) 0px 12px 45px 0px — the one card allowed to feel elevated/3D. 8px padding internally so the dashboard UI sits within a frame. Grayscale(1) contrast(0.94) filter applied for muted product photography feel.

### Highlighted Text Span

Text in #3398e1 with a soft #c1e1f7 background highlight (pill-shaped background behind the word). Weight 400. The only inline color treatment — every headline gets one.

### Text Input

White fill, 6px radius, 1px border #d6d3d1, placeholder #78716c, padding 4px 12px. Focus ring: 2px #3ba6f1. Minimal, inline with label.

### Mascot Sticker Illustration

Grayscale illustration with drop-shadow filter (rgba(0,0,0,0.25) 0px 2px 4px). SVG outline-only treatment. Used once per section as a playful counterweight to the monochrome data UI.

### Logo Wordmark

Small black flame/spark glyph + 'Seline' wordmark in Inter weight 500, 14px, #0c0a09. Compact, sits left of nav.

### Star Rating Display

Five small star glyphs in #0c0a09 (or warm gray), inline with platform name in 14px Inter #78716c. No card chrome — sits inline in copy flow.

### Testimonial Card

No card chrome. Star row (★ in #0c0a09), 16px quote text in #0c0a09 with inline cyan highlights for emphasized phrases, 32px avatar circle + name (14px weight 500) + role (14px #78716c). Vertical gap 16px between elements.

### Tab Pill Group

Horizontal row of 4 pill-shaped tabs at bottom of dashboard preview. Active tab: #1c1917 fill, white text, 9999px radius. Inactive: transparent, #0c0a09 text, 1px #e8e6e5 border. Switches the dashboard view above.

## Similar Design Systems

- {'why': 'Same single-accent-on-warm-canvas approach with privacy-focused analytics positioning; both use one vivid color against an almost-monochrome palette', 'business': 'Plausible Analytics'}
- {'why': 'Same weight-400-at-large-size headline restraint and tight negative letter-spacing on a custom geometric sans', 'business': 'Linear'}
- {'why': 'Same minimal analytics-alternative visual language with warm-neutral canvas and one accent color, editorial vertical rhythm', 'business': 'Fathom Analytics'}
- {'why': 'Same restrained monochrome palette with a single chromatic accent and pill-shaped interactive controls', 'business': 'Vercel'}
- {'why': 'Same warm-stone canvas with cyan accent, mascot sticker personality element, and flat product-screenshot hero', 'business': 'Cal.com'}

## Agent Prompt Guide

Quick Color Reference:
- page background: #fafaf9
- card surface: #ffffff
- primary text: #0c0a09
- secondary text: #78716c
- border / hairline: #e8e6e5
- accent (text highlight + icons): #3ba6f1
- primary action: #3ba6f1 (filled action)
- highlight wash: #c1e1f7

Example Component Prompts:

1. Hero headline: 52px roobert weight 400, #0c0a09, line-height 1.12, letter-spacing -1.092px. Inline the phrase 'simple & actionable' as a span with #3398e1 text on a #c1e1f7 pill background highlight. Subheadline at 16px Inter weight 400, #78716c, line-height 1.69.

2. Create a Primary Action Button: #3ba6f1 background, #0c0a09 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. Feature card: white (#ffffff) fill, 10px radius, 1px border #e8e6e5, 24px padding, shadow rgba(0,0,0,0.05) 0px 4px 16px 0px. Heading 32px roobert weight 400 #0c0a09, body 14px Inter #78716c.

4. Dashboard preview card: white fill, 16px radius, shadow rgba(17,12,46,0.12) 0px 12px 45px 0px, 8px internal padding. Apply CSS filter grayscale(1) contrast(0.94) to mute the dashboard to monochrome.

5. Testimonial block: star row of 5 small ★ glyphs in #0c0a09, quote text 16px Inter #0c0a09 line-height 1.69 with inline cyan highlight span on the emphasized phrase, 32px circular avatar below with name 14px Inter weight 500 #0c0a09 and role 14px Inter #78716c. No card chrome — copy flows directly on canvas.

## Highlight Span Pattern

The signature typographic move is the inline highlight: one phrase per headline receives #3398e1 text color with a #c1e1f7 pill-shaped background behind it (padding ~2px 8px, radius 4px). This is the brand's voice marker — it always lands on the value-prop keyword. Rules: exactly one per headline, never inside body paragraphs, never on nav items. The highlight carries the entire chromatic budget of the headline; everything else stays #0c0a09.
