# Arcade — Design System

> **North Star**: Electric blue ripple on white paper. A clean editorial canvas where a single vivid blue flows like liquid from corner to corner, making every interactive element feel switched on.
> **Theme**: light
> **Source**: https://arcade.software
> **Refero Style**: https://styles.refero.design/style/f65b0b91-bdd1-458d-8775-2f6fa8a9d4b1
> **Synced**: 2026-09-01

## Overview

Arcade's visual system is a white-canvas product surface accented by one saturated electric-blue (#2142e7) and a signature flowing blue gradient that anchors the hero. Typography is Inter across all sizes, with weight concentrated in the 400–700 band and tight negative tracking on display sizes that tightens the type optically as it scales. The interface reads as functional and quiet: gray-on-white content blocks, thin borders, compact 12–16px radii, and cool-tinted shadows built on rgba(17,24,39,...) that keep every elevated surface feeling on-brand. Color is rationed — one blue does the work of accent, CTA, and focus — while everything else is a neutral ramp. Density is comfortable but not airy: 8px and 12px gaps dominate micro-spacing, 32–48px separates sections.

## Color Palette

- **Voltage Blue**: `#2142e7` — Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Deep Voltage**: `#182fa5` — Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Midnight Ink**: `#111827` — Supporting neutral for secondary UI, dividers, and muted labels. Do not promote it to the primary CTA color [neutral]
- **Slate 600**: `#4b5563` — Body text, nav links, icon fills, card secondary copy — the dominant text color across the page [neutral]
- **Slate 700**: `#374151` — Nav link hover, emphasized body text, secondary headings [neutral]
- **Slate 500**: `#70747d` — Muted helper text, placeholder copy, low-emphasis labels [neutral]
- **Graphite**: `#414652` — Subheadings and section titles that sit between body and display weight [neutral]
- **Paper White**: `#ffffff` — Card surfaces, button text, input fields, nav bar background — the primary elevated surface [neutral]
- **Fog 50**: `#f9fafb` — Page canvas, section backgrounds, the base layer everything sits on [neutral]
- **Fog 100**: `#f3f4f6` — Alternate section background, subtle hover fills, tag backgrounds [neutral]
- **Mist 200**: `#e5e7eb` — Hairline borders, input borders, card outlines, divider lines [neutral]
- **Smoke 300**: `#d9dadc` — Stronger borders, checkbox frames, visible structural edges [neutral]

## Typography

- **Inter**
- **Balig Script**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.56 |
| subheading | 18 | — | 1.5 |
| heading-sm | 20 | — | 1.4 |
| heading | 24 | — | 1.33 |
| heading-lg | 30 | — | 1.29 |
| display | 48 | — | 1.14 |
| display-lg | 64 | — | 1.06 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'tabs': '12px', 'cards': '16px', 'pills': '9999px', 'inputs': '16px', 'buttons': '12px', 'hero-frame': '24px'}

## Layout

Page model is max-width 1200px centered, full-bleed at the hero and footer. The hero is a full-viewport-width gradient band (~600px tall) with a centered headline, subtitle, toggle group, and URL input stacked vertically. Below the hero, sections alternate between white and #f9fafb bands, separated by 64px gaps. Content sections use a centered section heading block (max 720px) followed by either a single product mockup frame or a two-column layout (text-left / visual-right or text-left / checklist-right). Tab navigation sits centered between heading and content. The nav is a 64px sticky top bar with a single hairline border — no shadow, no background blur. Density is comfortable: cards breathe inside 32px padding, section gaps are 48–64px, and micro-spacing stays at 8/12/16px increments.

## Surfaces / Elevation

- **Page Canvas**
- **Card Surface**
- **Nested Surface**
- **Ink Surface**

**Shadow tokens:**

## Imagery

Imagery is product-centric: the screenshots show browser-framed product captures rendered inside realistic mockup frames with faux window chrome and tab bars. The hero features a flowing blue gradient field with no photography or illustration — color itself does the atmospheric work. Customer logos in the trust strip are desaturated to #70747d gray, removing brand noise so the page's own blue dominates. Icons are minimal line-style at ~16px stroke, appearing as check marks in feature lists, chevrons in nav, and arrow glyphs in CTAs. There is no lifestyle photography, no abstract 3D, and no decorative illustration — the visual language is pure UI artifact (screenshots, gradients, icons, type).

## Design Principles

### Do

- Use #2142e7 (Voltage Blue) for exactly one element per viewport: a primary CTA, an active tab, or a focused input — never two blue fills competing at the same visual weight.
- Apply the hero gradient only to the top-of-page brand field; repeat it at smaller scale only for feature hero panels.
- Set display sizes (36–64px) at weight 700 with tracking between -0.020em and -0.025em to optically tighten the type.
- Use 12px radius for buttons and tabs, 16px radius for inputs and cards, 9999px for tags and announcement pills — do not mix these scales on the same component type.
- Build elevation with the six-layer rgba(17,24,39,0.04) shadow stack and a 1px border ring rather than a single hard drop shadow.
- Keep body text at #4b5563 on white — reserve #111827 for headings and dark surfaces to maintain the quiet-to-loud hierarchy.
- Anchor any dark surface (#111827) with a 92–102deg linear gradient toward rgba(30,43,72,0.9) to avoid flat black.

### Don't

- Do not introduce a second saturated color — the system is monochrome plus one blue; adding green, red, or orange breaks the ration.
- Do not use a 1px or 2px hard drop shadow on cards — the design's elevation language is the diffused multi-layer stack.
- Do not round buttons above 12px or below 8px — the 12px radius is the system's signature softness, not a pill and not a sharp square.
- Do not use weight 500 for headings or weight 400 for display — the type weight ladder must move in steps of two (400, 600, 700).
- Do not apply the hero gradient to navigation, cards, or body sections — it belongs only in full-bleed brand moments.
- Do not place white text on white at any opacity below 0.9 — the system's contrast pairs are all AAA and should stay that way.
- Do not use #e5e7eb as a fill for interactive elements — it is a border token only, not a surface.

## Components

### Primary CTA Button

Background #2142e7 (Voltage Blue), white text at 16px weight 600, 12px radius, horizontal padding 20px, vertical padding 10px. Six-layer soft shadow stack tinted with rgba(17,24,39,0.04) plus a 1px #182fa5 (Deep Voltage) inset ring that deepens the edge. The stacked low-opacity shadows create a diffused halo rather than a hard drop, making the button feel lit from within.

### Ghost Button

White background, #111827 text at 16px weight 600, 12px radius, 20px/10px padding. Same six-layer shadow stack as the primary but with a 1px rgba(17,24,39,0.16) border ring instead of a chromatic inset. Creates parity with the primary button's elevation without competing for attention.

### Pill Tab

Active state: white background, #111827 text weight 600, 12px radius, 16px/10px padding, soft shadow ring. Inactive: transparent background, #4b5563 text weight 500, no shadow. The active tab visually lifts off the tab strip through shadow rather than color fill, keeping the group's overall tone neutral.

### URL Input with Submit Arrow

White background, 16px radius, full-width with max ~480px. Placeholder text in #70747d at 16px weight 400. 1px #e5e7eb border with no visible focus ring (the circular blue submit button inside acts as the focal point). Trailing circular #2142e7 submit button, 40px diameter, white arrow icon centered.

### Toggle Button Group

Two adjacent pill buttons inside a #f3f4f6 track with 8px radius. Active button: white background, #111827 text, subtle shadow. Inactive: transparent, #4b5563 text. Each pill 14px weight 500 with a small leading icon. The track itself is rounded and unbordered — the group reads as one segmented control.

### Feature Checkmark List

Two-column grid of items, 8px row gap, 12px column gap. Each item: small circular #e5e7eb checkmark badge (20px) with a blue check inside, followed by 16px weight 400 #4b5563 text. The check badge acts as a quiet brand-color moment within an otherwise gray list.

### Metric Badge

White card, 12px radius, 16px/12px padding, text 14px weight 500 #4b2563 with a small up-arrow icon. Elevated with the floating-card shadow stack. Sits offset to the right of a feature block, breaking the grid to draw the eye.

### Trust Logo Strip

Single horizontal row, white canvas, logos rendered in #70747d muted gray at uniform height (~24px). No borders, no background, generous 48px vertical padding. The desaturation of brand logos is deliberate — it removes visual noise and lets the page's own brand color dominate.

### Top Navigation Bar

White background, 64px height, 1200px max-width centered, subtle 1px #e5e7eb bottom border. Logo left at 24px height, nav links center-left in 16px weight 500 #4b5563 with dropdown chevrons, right cluster has a ghost 'Talk to sales' button and a filled blue 'Sign up for free' CTA. The nav is quiet — it carries no gradient or shadow, only a hairline.

### Announcement Banner

Pill shape (9999px radius), white background, 1px #e5e7eb border, 16px/8px padding. Mixed-weight text: event name 14px weight 600 #111827, CTA link 14px weight 500 #2142e7 separated by a thin vertical divider. Floats above the hero with no shadow, anchored to the page top with 16px margin.

### Hero Gradient Banner

Flowing blue gradient from near-white upper-left through saturated mid-tones to deep #2142e7 lower-right, filling the full viewport width and ~600px height. Contains a radial highlight zone in the center that keeps the headline legible while edges pool into brand color. The gradient is the system's signature — it is the only place in the page where large-scale color lives.

### Product Mockup Frame

White surface, 16px radius, subtle floating-card shadow. Top bar mimics a browser chrome with a #f9f4f6 background, 3 small circular window dots, and tab labels at 12px weight 500 #4b5563. Content area is the screenshot. The frame sells the product as a captured artifact, not a live embed.

### Section Heading Block

Display-size heading 36–48px weight 700 #111827 with -0.020em tracking, centered, max-width 720px. Subtitle below at 18px weight 400 #4b5563, line-height 1.56, also centered. 32px gap between heading and subtitle, 48–64px gap below the block before content begins.

### Section Content Card

White background, 1px #e5e7eb border, 16px radius, 32px padding. No drop shadow beyond the hairline ring — elevation comes from the border and the contrast against the #f9fafb page background. Content inside uses the standard type scale, with the section title at 24px weight 700 and body at 16px weight 400 #4b5563.

## Similar Design Systems

- {'why': "Same monochrome-plus-one-saturated-accent discipline and Inter-typeface system, though Linear's accent is purple and uses sharper radii", 'business': 'Linear'}
- {'why': 'Inter-only typography, hairline borders, 12px button radius, and a single brand color carrying all interactive weight', 'business': 'Vercel'}
- {'why': 'Comfortable white-canvas product surface with a single vivid accent, soft floating shadows, and tight tracking on display sizes', 'business': 'Attio'}
- {'why': 'Friendly SaaS with rounded inputs, gradient hero treatments, and a rationed color palette where one hue does all the interactive work', 'business': 'Loom'}
- {'why': 'Clean editorial layout rhythm with centered section headings, alternating neutral bands, and Inter at restrained weights', 'business': 'Pitch'}

## Gradient System

Two gradient families. (1) The hero brand gradient: a flowing blue field from near-white center to #2142e7 edges, used only at full-bleed scale. (2) The dark surface gradient: linear 92–102deg from #111827 to rgba(30,43,72,0.9), used for dark CTA buttons, dark cards, and inverted sections. A third accent gradient (linear 90deg, #111827 → #2142e7 → #03b5ed → #111827) appears as a thin animated border on premium CTAs — the cyan #03b5ed stop is the only place this second blue appears, so it reads as a special-event highlight, not a system token.

## Agent Prompt Guide

## Quick Color Reference
- text (primary heading): #111827
- text (body): #4b5563
- background (canvas): #f9fafb
- background (card): #ffffff
- border: #e5e7eb
- accent: #2142e7
- primary action: no distinct CTA color

## Example Component Prompts
1. **Hero section**: Full-bleed flowing blue gradient (white center → #2142e7 edges), 600px height. Headline 48px Inter weight 700 #111827, tracking -0.96px, centered. Subtitle 18px Inter weight 400 #4b5563. Ghost toggle group with Demo/Video pills. URL input: white, 16px radius, placeholder #70747d, trailing circular #2142e7 submit button 40px diameter.

2. **Feature column card**: White surface, 1px #e5e7eb border, 16px radius, 32px padding. Section title 24px Inter weight 700 #111827. Body 16px Inter weight 400 #4b5563. Two-column checkmark grid: 20px circular #e5e7eb badge with blue check, 16px #4b5563 text, 8px row gap, 12px column gap.

3. **Tab switcher group**: 8px-radius #f3f4f6 track, 16px/10px pill padding. Active pill: white background, #111827 text weight 600, soft shadow ring. Inactive pill: transparent, #4b5563 text weight 500. 16px Inter throughout.

4. **Product mockup frame**: 16px radius white card, floating-card shadow stack (rgba(17,24,39,0.2) 0px 8px 8px + inner highlight). Top bar #f9f4f6 with 3 circular window dots (8px, gray). Tab labels 12px Inter weight 500 #4b5563. Content area: product screenshot or video frame.

5. **Navigation bar**: White background, 64px height, 1200px max-width centered, 1px #e5e7eb bottom border. Logo 24px left. Nav links 16px Inter weight 500 #4b5563 with dropdown chevrons. Right cluster: ghost 'Talk to sales' (white, 1px border, 12px radius) beside filled blue 'Sign up for free' (#2142e7, white text, 12px radius, six-layer shadow with #182fa5 inset ring).
