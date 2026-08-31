# Relate — Design System

> **North Star**: cool dawn over product canvas
> **Theme**: light
> **Source**: https://www.relate.so
> **Refero Style**: https://styles.refero.design/style/337ade6a-4bae-49ba-b4aa-8994ac805a81
> **Synced**: 2026-09-01

## Overview

Relate renders as a cool-white SaaS surface with near-black headline ink and one vivid royal-blue accent that does all the brand talking. The product UI is shown through soft rounded cards floating on a pale lavender wash, with colored status dots (blue/green/red/orange) punctuating pipeline columns like Kanban tickets. Typography is tight: Inter at 56–80px with strong negative tracking whispers scale, body copy sits compact at 14–16px on generous line-height, and spacing leans dense (8–12px gaps) rather than airy. Everything lives in pill and rounded-rect containers; hard corners are absent.

## Color Palette

- **Snow Canvas**: `#fcfcfc` — Page background, card surfaces, nav surface — the dominant neutral that makes blue accents feel switched on [neutral]
- **Lavender Wash**: `#f0f4fe` — Subtle accent surface behind hero and feature blocks — gives cool-tinted depth without darkening the page [neutral]
- **Midnight Ink**: `#020520` — Hero and section headings — near-black with a violet cast, reads warmer than pure black against white [neutral]
- **Graphite Body**: `#14141e` — Body text, secondary headings, product UI labels — workhorse dark neutral with cool undertone [neutral]
- **Slate Caption**: `#374151` — Muted body text, nav labels, list items — medium-dark gray for subordinate copy [neutral]
- **Ash Helper**: `#6b7280` — Helper text, metadata, timestamps — lighter gray for tertiary information [neutral]
- **Stone Divider**: `#e2e8f0` — Hairline borders, card edges, divider lines — barely-there separation between surfaces [neutral]
- **Fog Surface**: `#f1f5f9` — Input backgrounds, disabled states, subtle grouping surfaces — one shade darker than canvas [neutral]
- **Royal Signal**: `#145aff` — Primary brand accent — headlines, links, hero word highlight, pipeline-active dots, logo mark. Single saturated hue carries the entire brand identity [brand]
- **Cobalt Glow**: `#3b82f6` — Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content [accent]
- **Mint Win**: `#16ca2e` — Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Coral Lost**: `#f26052` — Red text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Amber Pending**: `#ffa64d` — Orange text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Azure Focus**: `#0099ff` — Input focus ring glow — pure blue that distinguishes active form state from ambient blue brand color [accent]

## Typography

- **sans-serif**
- **Inter**
- **Pretendard**
- **Roboto Mono**
- **Font Awesome 6 Pro Light**
- **Font Awesome 6 Pro Solid**
- **Font Awesome 6 Pro Regular**
- **Font Awesome 6 Brands Regular**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.2 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.63 |
| subheading | 20 | — | 1.4 |
| heading-sm | 22 | — | 1.4 |
| heading | 40 | — | 1.05 |
| heading-lg | 56 | — | 1.05 |
| display | 80 | — | 1.05 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 12px
- **Element Gap**: 8-12px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '8px', 'pills': '100px', 'inputs': '12px', 'buttons': '9999px', 'containers': '16-40px', 'pipeline-cards': '16px'}

## Layout

Full-width sections with centered content capped at ~1200px max-width. Hero is a centered single-column layout: YC badge above, oversized headline (56px) with one colored word, body paragraph (18px), single ghost-outline CTA button, all centered over a blue gradient band. Product UI screenshots appear as large floating elements below the fold. Mid-page sections alternate: centered heading + description above, then full-width product UI mockup. Feature blocks use large rounded containers (40px radius) with generous internal padding. Customer logo strip is a 4×2 centered grid. Footer is a dark navy section. Navigation is a horizontal top bar with logo left, center links, dual CTAs right.

## Surfaces / Elevation

- **Canvas**
- **Wash**
- **Card**
- **Frosted**

**Shadow tokens:**

## Imagery

Minimal literal photography — the page relies on product UI screenshots rendered as floating mockups rather than lifestyle or product photography. The hero features a large Kanban-style CRM screenshot showing pipeline columns with deal cards. Below sections show prospect-list and contact-detail UI screenshots, all rendered as white cards on light backgrounds. Customer logos appear as monochrome black marks in a grid. The Y Combinator badge uses a small flat-color icon. No illustrations, no 3D renders, no decorative graphics — visual interest comes entirely from the product interface itself, which acts as the brand's visual proof.

## Design Principles

### Do

- Use #145aff as the sole saturated accent for headings, links, logos, and the one word-of-color in hero copy — never introduce a second brand hue
- Set body text at 14–16px Inter 400 with #14141 or #374151 on #fcfcfc canvas; minimum 17.8:1 contrast ratio
- Apply pill radius (9999px or 100px) to all buttons, tags, and nav items — hard 90° corners should not appear in interactive elements
- Use the multi-layer soft shadow stack (three rgba layers at increasing blur) on feature section cards for floating elevation
- Render colored status dots at 4–6px diameter with #3b82f6/#16ca2e/#f26052/#ffa64d for pipeline and deal states
- Set hero and display headings at 56–80px Inter 600 with letter-spacing -0.027 to -0.037em for tight compressed scale
- Use 8px border-radius for inner cards (deal rows, prospect items) and 16–40px for outer feature containers — maintain a two-tier rounding system

### Don't

- Don't use #0000ee or browser-default link blue — it is an artifact, not a brand choice; use #145aff or #3b82f6
- Don't fill CTA buttons with heavy solid color blocks — the pattern here is ghost-outlined or frosted pills, not filled rectangles
- Don't introduce gradients with more than two stops; all detected gradients are simple linear or radial two-color blends
- Don't use sharp 0px corners on any visible element; the minimum radius in the system is 4px
- Don't set body text below 14px or above #6b7280 lightness — legibility collapses below this threshold
- Don't stack multiple saturated accent colors in one component — only one blue, green, red, or orange dot per surface
- Don't use Inter weights above 600 or below 400 — the system operates in a tight 400/500/600 range

## Components

### Ghost Outline Button

Background #fcfcfc, text #145aff (or #020520), border 1px #145aff, border-radius 50px (pill), padding 14px 32px. Semi-transparent variant uses rgba(255,255,255,0.8) background on dark surfaces.

### Filled Dark Button

Background appears as dark text-link style; actual filled CTAs in the hero use white surface with #145aff text and pill radius. The dominant CTA pattern is a ghost-outline or frosted button, never a heavy filled block.

### Pipeline Column Card

Background #ffffff, border-radius 16px, subtle shadow rgba(0,0,0,0.1) 0px 0px 4px -2px, padding 12px. Column header has a 4px colored dot (blue/green/red/orange) followed by count and total deal value in #145aff.

### Deal Card

Background #ffffff, border-radius 8px, padding 12px 16px, shadow rgba(0,0,0,0.1) 0px 0px 4px -2px. Contains: company avatar + name, deal value, last-activity note, assignee avatar, time-ago badge.

### Prospect List Card

Background #ffffff, border-radius 16px, padding 12px. Row contains company logo, name, contact person, timestamp, and a right-side detail panel with email-thread and properties.

### Logo Mark Badge

Rounded square 32–40px container with #145aff background, white lowercase 'r' glyph inside. Sits beside wordmark 'relate' in Inter 600.

### Nav Link

Inter 15px weight 500, color #14141, no underline, 16px horizontal gap between items. Active/hover state: color shift to #145aff.

### Hero Gradient Banner

Linear gradient from rgba(20,90,255,0.1) to rgba(182,203,253,0.4) creating a soft blue glow under the 'Get started free' CTA. Extends full-width with large border-radius (40–48px) on the bottom edge.

### Feature Section Card

Background #fcfcfc, border-radius 40px, padding 52px 72px, multi-layer shadow: rgba(0,0,0,0.08) 0px 0.36px 1.8px -1.4px, rgba(0,0,0,0.07) 0px 1.37px 6.87px -2.8px, rgba(0,0,0,0.016) 0px 6px 30px -4.25px. Gives a floating elevated feel.

### Glassmorphic Container

Background rgba(252,252,252,0.2), border-radius 28–48px, padding 12–20px, backdrop-filter blur(15px). Reveals underlying gradient — used in dark or tinted sections.

### Status Dot

4–6px filled circle, color-coded: #3b82f6 (Potential/blue), #ffa64d (Pending/orange), #16ca2 (Closed Won/green), #f26052 (Lost/red). Sits inline with column title text.

### Customer Logo Strip

8 monochrome brand logos arranged in 2 rows of 4 on white canvas. Logos rendered in #14141 at ~60% opacity, no color, evenly spaced with 40–60px gaps.

### Input Field

Background rgba(255,255,255,0.08) on dark or #ffffff on light, border 1px #ffffff or #e2e8f0, border-radius 12px, padding 15px. Focus state: box-shadow with #0099ff glow ring.

### Y Combinator Badge

Small inline element: orange square #f26052 icon + 'Backed by Y Combinator' text in #14141 Inter 14px. Centered above headline.

## Similar Design Systems

- {'why': "Same ultra-clean white-canvas approach with near-black headings and a single saturated accent color (Notion's red, Relate's blue); both use tight Inter-style type with negative tracking on display sizes and pill-radius buttons", 'business': 'Notion'}
- {'why': "Identical compact-density philosophy, dark-near-black headline ink (#020520 vs Linear's similar), product-UI-as-hero pattern showing the app interface, and tight typographic rhythm with compressed letter-spacing on large sizes", 'business': 'Linear'}
- {'why': 'Same CRM-product-as-hero approach with floating pipeline/contact screenshots on pale tinted backgrounds, cool-blue accent palette, and rounded soft-card components with minimal shadow', 'business': 'Attio'}
- {'why': 'Identical near-black heading color (#020520), single vivid accent for highlights, white-canvas-with-soft-blue-wash section pattern, and pill-radius ghost-outline button system', 'business': 'Vercel'}
- {'why': 'Same restrained color discipline (one brand blue, achromatic everything else), generous 40–48px border-radius on feature containers, and tight Inter display type with aggressive negative tracking', 'business': 'Stripe'}

## Agent Prompt Guide

Quick Color Reference:
- text: #020520 (headings), #14141e (body), #374151 (secondary), #6b7280 (muted)
- background: #fcfcfc (canvas), #f0f4fe (wash), #ffffff (cards)
- border: #e2e8f0 (hairline), #145aff (active/outline)
- accent: #145aff (Royal Signal — brand)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a hero headline section: #fcfcfc canvas. Main headline 'Modern [Sales] CRM for B2B companies' at 56px Inter weight 600, #020520, letter-spacing -1.51px, line-height 1.05. The word 'Sales' colored #145aff. Subtext at 18px Inter weight 400, #0f1f3d, max-width 480px centered. Single ghost-outline pill button below: background #fcfcfc, text #145aff, border 1px #145aff, border-radius 50px, padding 14px 32px. Hero sits above a soft blue gradient band (rgba(182,203,253,0.4) to transparent) with 40px bottom border-radius.

2. Create a pipeline Kanban board: #ffffff cards on #fcfcfc background. Four columns with headers showing a 5px colored dot (#3b82f6 blue, #ffa64d orange, #16ca2e green, #f26052 red) + column name + count + total deal value in #145aff. Deal cards: #ffffff background, 8px border-radius, 12px 16px padding, shadow rgba(0,0,0,0.1) 0px 0px 4px -2px. Card content: company avatar + name at 14px Inter 600 #14141e, deal value at 14px Inter 500 #14141e, activity note at 12px Inter 400 #6b7280, assignee + timestamp row at 12px.

3. Create a customer logo strip: #fcfcfc background, centered. Heading at 14px Inter 400 #14141e reading 'Powering the next generation B2B startups'. Two rows of 4 monochrome logos at ~40px height, color #14141e at 70% opacity, evenly spaced with 48px gaps between logos, max-width 900px centered.

4. Create a nav bar: #fcfcfc background with 1px bottom border #e2e8f0. Logo (32px #145aff rounded square + 'relate' wordmark at 18px Inter 600 #14141e) on left. Center nav links: 'Product', 'Pricing', 'Customers', 'Blog', 'Resources' at 15px Inter 500 #14141e with 16px gaps. Right side: 'Log in' text link + ghost-outline 'Book a demo' pill button (#145aff border, 50px radius) + ghost 'Get started free' pill button. All at 14px Inter 500.

5. Create a feature section card: #fcfcfc background, 40px border-radius, padding 52px 72px, multi-layer shadow stack. Section heading 'Prospect.' at 40px Inter 600 #020520, letter-spacing -1.48px. Subtext at 18px Inter 400 #374151, max-width 560px. Below: product UI mockup showing a prospect list with three columns — company list, email thread, contact details — all on #ffffff cards with 16px radius and the soft single-layer shadow.

## Animation Philosophy

Motion is restrained and functional: timing-function is ease across all transitions with no spring or bounce curves detected. Interactive feedback is limited to color shifts (gray → blue), opacity changes on hover, and subtle shadow elevation increases on cards. No scroll-triggered animations, no parallax, no entrance choreography. The product UI screenshot shows a static, immediately-readable layout — the page communicates confidence through stillness.
