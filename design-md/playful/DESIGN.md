# Playful — Design System

> **North Star**: sunlit paper notebook with a hot-pink highlighter. A friendly, editorial product surface printed on warm cream stock, where one vivid magenta accent punctuates an otherwise monochrome warm-gray world.
> **Theme**: light
> **Source**: https://playful.software
> **Refero Style**: https://styles.refero.design/style/f93ac72e-73b2-4b2c-80eb-351ddfa56f4d
> **Synced**: 2026-09-01

## Overview

Playful reads like a warm, hand-crafted workshop printed on cream paper. The entire surface sits on a sandy oat canvas (#f6f2ee) rather than clinical white, giving every screen a paper-like, approachable warmth. A single hot-pink (#ff2e95) does all the chromatic work — CTAs, links, logo mark — against a near-black ink (#111/#000), so screens stay visually quiet until a moment of action is needed. The display type is unapologetically heavy and italic at 70–79px, leaning into editorial poster energy rather than SaaS neutrality. Components are large and soft: 44px cards on pill-shaped buttons, deep diffused shadows, generous breathing room. The overall rhythm is one bold typographic statement per section, surrounded by quiet warm whitespace.

## Color Palette

- **Hot Magenta**: `#ff2e95` — Primary CTA fill, logo mark, link color, accent strokes — the only chromatic voice in the system, used sparingly to signal action [brand]
- **Ink Black**: `#000000` — Primary heading text, button text, heavy borders, navigation bar background [neutral]
- **Oat Canvas**: `#f6f2ee` — Page background, large surface fills — the warm cream that replaces cold white throughout [neutral]
- **Soft Ink**: `#111111` — Body text and headings on light surfaces, card surface background for dark elements [neutral]
- **Slate**: `#0f172a` — Secondary text, subtle body copy — a cool near-black used for non-headline text [neutral]
- **Charcoal**: `#414040` — Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the primary CTA color [neutral]
- **Stone**: `#848383` — Icon strokes, muted helper text, subtle UI dividers [neutral]
- **Paper White**: `#ffffff` — Card surfaces, elevated panels, contrast surface against oat canvas [neutral]
- **Warm Mist**: `#e8e5e0` — Hairline borders, dividers, subtle container outlines — warm-toned to match canvas [neutral]
- **Sand**: `#e2dcd6` — Secondary borders, decorative outlines on warm surfaces [neutral]
- **Driftwood**: `#c3c1bf` — Card shadow base tone, muted surface fills [neutral]
- **Midnight**: `#202126` — Deep heading text variant, near-black with subtle cool cast for high-weight headlines [neutral]

## Typography

- **Inter**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.4 |
| body | 16 | — | 1.5 |
| body-lg | 18 | — | 1.5 |
| subheading | 26 | — | 1.23 |
| heading-sm | 30 | — | 1.2 |
| display | 79 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 10-16px
- **Section Gap**: 113px
- **Border Radius**: {'tags': '999px', 'cards': '44px', 'images': '16px', 'inputs': '99px', 'buttons': '99px (pill)'}

## Layout

Centered, max-width 1200px container with generous 113px section gaps between major vertical bands. The page rhythm alternates between quiet warm-cream sections (hero, FAQ) and a single vivid pink gradient wash section in the middle. Hero is a centered stack: display headline → subtext → email+CTA pill composite → tilted row of app tiles. Below the gradient band, the FAQ section uses a two-column layout (label left, accordion stack right) before returning to a centered final CTA. A full-width black category navigation bar cuts across the page at the transition between hero and gradient sections, providing the only dark band. The overall density is spacious — single elements breathe rather than packing into grids.

## Surfaces / Elevation

- **Oat Canvas**
- **Paper White**
- **Soft Ink**
- **Hot Magenta**

**Shadow tokens:**

## Imagery

Visual language is illustration-led, not photographic. The site shows stylized 3D app icons and playful character mascots (broccoli with face, pink blob, blue ghost, white creature) rendered in soft 3D with rounded, candy-like surfaces and saturated color. Illustrations sit inside rounded square app tiles (44px radius) that are slightly tilted and overlapping in a fan arrangement, evoking a hand of cards rather than a rigid grid. No photography appears anywhere — the warmth comes from the cream canvas and the 3D illustration style, not from lifestyle imagery. Icons in the UI itself are minimal line icons in muted gray, not colorful.

## Design Principles

### Do

- Use Hot Magenta (#ff2e95) only for the primary CTA, the logo, and link accents — never as a large surface fill, icon background, or decorative wash longer than a section
- Set display headlines in Inter 700/900 italic at 70–79px, line-height 1.00, letter-spacing -0.002em — the italic at scale is the brand's typographic signature
- Build cards and tiles with 44px border-radius and the dual-layer shadow stack (0 32px 80px rgba(0,0,0,0.22) + 0 2px 8px rgba(0,0,0,0.08))
- Use Oat Canvas (#f6f2ee) as the base page background — do not switch to pure white for full-page surfaces
- Pair every email input with the Pill CTA inside a single white pill container (99px radius) to read as one composite unit
- Center hero compositions — headline, subtext, and CTA stack vertically with generous 113px section gaps between major bands
- Keep icons stroke-based in Stone (#848383) at 1.5–2px weight, never filled with color

### Don't

- Do not use upright (non-italic) weight 700+ for display headlines — the italic slope is what makes Playful feel editorial rather than corporate
- Do not introduce additional accent colors — blue, green, orange, purple are all out of system; Hot Magenta is the only chromatic voice
- Do not use pure black (#000000) on pure white (#ffffff) for body text without checking — use #111 or #0f172a for less harshness on the warm canvas
- Do not apply sharp 0–4px radii to cards or buttons — the 16/44/99px scale is part of the friendly softness
- Do not stack more than two type weights on a single screen — typically 400 body + 700/900 italic display, with 500/600 for subheads
- Do not place white cards directly on white — always sit Paper White on Oat Canvas so cards read as elevated
- Do not use drop shadows on text, buttons, or icons — shadows are reserved for card-level elevation only

## Components

### Pill CTA Button (Primary)

Hot Magenta (#ff2e95) fill, white text, Inter 600 at 16px, 99px border-radius, 14px 24px padding. Heavy and confident — the only chromatic element competing with the display type.

### Email Input Field

Oat Canvas (#f6f2ee) fill, 1px Charcoal (#414040) border, 99px border-radius, white card container wraps input + button as a unified pill. Placeholder Inter 400 16px in muted gray. Paired visually with the Pill CTA to form a single inline composite.

### Editorial Display Headline

Inter 700 or 900 italic, 70–79px, line-height 1.00, letter-spacing -0.002em, color Ink Black (#000) or Soft Ink (#111). Set in one or two lines, centered. This is the signature element — heavy italic at scale creates a poster-like moment rather than a SaaS tagline.

### App Tile Card

44px border-radius, Paper White (#ffffff) surface, deep diffused shadow (0 32px 80px rgba(0,0,0,0.22)). Contains a full-bleed illustration or icon. Sized roughly 140–180px square, displayed in a slightly tilted overlapping row to suggest a hand of cards.

### FAQ Accordion Card

Paper White (#ffffff) surface, 44px border-radius, warm border or none, soft shadow stack (0 32px 80px / 0 2px 8px rgba(0,0,0,0.22/0.08)). Question text Inter 600 italic 16–18px, chevron icon in Stone (#848383). Stacked vertically with 12–16px gap between cards.

### Category Navigation Bar

Ink Black (#000) background, white text Inter 500 14–16px, horizontal scroll, items separated by 24–32px spacing. No visible border or background change on the bar itself — it reads as a dark band cutting across the page.

### Logo Wordmark

Hot Magenta (#ff2e95) stylized 'playful' wordmark in Inter 700 italic, paired with a small geometric icon (rounded square mark). Functions as both brand and link, so the magenta is doing double duty as identity and navigation.

### App Icon

Rounded square (16–20px radius) dark container with Hot Magenta (#ff2e95) pictogram inside. Appears as a standalone mark above the final headline, echoing the logo's icon component.

### Gradient Highlight Section

Large soft radial or linear gradient from Hot Magenta (#ff2e95) through lavender-pink to Oat Canvas (#f6f2ee). No defined edges — bleeds into surrounding sections. Hosts a single italic headline at 30px with mixed weight ('Describe it. It's yours in minutes.').

### Hero Subtext

Inter 400 16–18px, Slate (#0f172a), centered, max-width ~560px. Quiet by design — lets the headline own the visual weight.

### Two-Column FAQ Section Layout

Left column: small 'Got questions?' label in Inter 500 + bold heading 'Things people want to know'. Right column: stacked FAQ accordion cards. 1200px max-width container, 64–80px section gap above and below.

## Similar Design Systems

- {'why': "Same editorial confidence in display typography (large heavy weight, tight letter-spacing) and a single vivid accent against a monochrome system — though Linear's palette is dark, Playful's italic display shares the same poster-like typographic attitude", 'business': 'Linear'}
- {'why': "Warm off-white canvas (#f6f2ee echoes Notion's slight cream tint) with generous spacing and a minimalist component vocabulary — the friendliness of the surface treatment is the shared trait", 'business': 'Notion'}
- {'why': "Same large italic display headlines, cream/warm canvas, and pill-shaped primary CTA, with a single chromatic accent for action — Pitch's editorial product design language is the closest aesthetic cousin", 'business': 'Pitch'}
- {'why': "Bold typographic statements over warm neutral surfaces, with one bold accent color (Framer's blue, Playful's magenta) — both treat the hero as an editorial moment rather than a feature checklist", 'business': 'Framer'}
- {'why': 'Generous whitespace, soft elevated cards, and the discipline of one accent color doing all chromatic work — though Vercel is dark-mode, the spatial generosity and single-accent philosophy is structurally similar', 'business': 'Vercel'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #111111
- background: #f6f2ee
- border: #e8e5e0
- accent: #ff2e95
- primary action: #ff2e95 (filled action)

**Example Component Prompts**
1. Create a Primary Action Button: #ff2e95 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create an FAQ card: #ffffff surface, 44px border-radius, shadow 0 32px 80px rgba(0,0,0,0.22) + 0 2px 8px rgba(0,0,0,0.08). Question text Inter 600 italic 18px #111111, chevron icon in #848383.

3. Create an app tile: 160px square, 44px border-radius, #ffffff surface, same shadow stack as FAQ card. Contains a centered 3D-style illustration in saturated color.

4. Create a gradient highlight section: full-width background blending from #ff2e95 through lavender to #f6f2ee (radial or large soft linear). Headline at 30px Inter italic 600, #111111, centered — mix regular and italic weight words for emphasis.

5. Create a category nav bar: #000000 background, full width, Inter 500 14px white text, items spaced 28px apart horizontally, 12px 0 vertical padding.

## Shadow Language

The system uses exactly one shadow stack, applied to cards and tiles only. It is a two-layer diffused shadow: a large soft 80px-blur shadow at 22% opacity providing the deep 'lift' off the warm canvas, plus a tight 8px-blur shadow at 8% opacity providing the contact-edge definition. Buttons, text, icons, and inputs receive no shadows. This restraint — shadow as elevation marker, not decoration — keeps the interface feeling like printed paper lifted off a desk rather than a glassmorphic product.
