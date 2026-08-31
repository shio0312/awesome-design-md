# Supabase — Design System

> **North Star**: Midnight code editor with phosphor green caret — a single chromatic pulse on a sea of charcoal.
> **Theme**: dark
> **Source**: https://supabase.com
> **Refero Style**: https://styles.refero.design/style/632249f1-fd78-4c77-9b34-7bae37ff3e9b
> **Synced**: 2026-09-01

## Overview

Supabase is a midnight IDE with phosphor green punctuation: a near-black canvas, monochrome UI surfaces, and a single vivid green that marks emphasis, headings, and primary actions. The interface borrows its rhythm from code editors — hairline borders, pill controls, generous vertical breathing room, and tight geometric typography (Circular) that whispers in regular weight rather than shouting in bold. Color is rationed: the page is 99% grayscale, and every green pixel earns its place by being a CTA, a highlighted keyword, or a logo. Cards float one elevation level above the canvas using subtle border contrast rather than shadow. The overall feel is fast, terminal-native, and quietly confident — designed to disappear so the product and its developer audience can take the spotlight.

## Color Palette

- **Phosphor Green**: `#3ecf8e` — Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Mint Pulse**: `#00c573` — Link text and inline accent — a slightly cooler green variant for textual references that shouldn't compete with primary CTAs [brand]
- **Forest Depth**: `#1f4b37` — Hover and pressed borders on green CTAs — keeps the button identifiable when the fill darkens on interaction [brand]
- **Midnight Emerald**: `#006239` — Deepest green surface — for low-key brand-tinted backgrounds, subtle section washes, and disabled-brand states [brand]
- **Snow**: `#fafafa` — Primary text, icon strokes, button labels — the dominant foreground across the entire interface [neutral]
- **Silver Mist**: `#b4b4b4` — Secondary headings, nav items, body emphasis — readable but never competing with Snow [neutral]
- **Smoke**: `#898989` — Tertiary text, captions, helper text, muted icon fills — the voice of metadata and annotations [neutral]
- **Graphite**: `#4d4d4d` — Icon outlines, low-emphasis borders, divider lines, and stroke color for illustrative line work [neutral]
- **Slate**: `#393939` — Input borders, subtle dividers, hairline separators between nav and content [neutral]
- **Charcoal**: `#2e2e2e` — Card and component borders — the most-used border color, giving surfaces their defined edge without a visible shadow [neutral]
- **Ash**: `#242424` — Elevated surface tier for nested cards, hover states, and popover backgrounds [neutral]
- **Obsidian**: `#121212` — Page canvas — the deep near-black foundation behind every section and card [neutral]

## Typography

- **Circular**
- **Source Code Pro**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.38 |
| heading-sm | 24 | — | 1.33 |
| heading | 36 | — | 1.2 |
| display | 72 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8-16px
- **Section Gap**: 64-96px
- **Border Radius**: {'tags': '9999px', 'cards': '16px', 'inputs': '8px', 'buttons': '9999px'}

## Layout

Full-width dark canvas at 1200px max-width centered. Hero is centered text with a 72px display headline (two lines, second line in Phosphor Green), 16px subtitle, and two side-by-side pill buttons. Below hero, a horizontal logo cloud strip. Feature sections alternate between centered text blocks and 2x2 card grids (4 columns at full width). Cards are uniform 16px radius with equal padding. Vertical rhythm uses 64-96px section gaps with seamless flow — no visible dividers between sections, just generous breathing room. Testimonials appear in a 4-column masonry grid. Footer is a single dark band. The navigation is a fixed 64px top bar with transparent background that may darken on scroll.

## Surfaces / Elevation

- **Obsidian Canvas**
- **Ash Card**
- **Charcoal Border**

## Imagery

Line-art and wireframe illustrations dominate — 3D geometric shapes (cubes, grids, network nodes) rendered in #4d4d4d stroke on #0d0d0d backgrounds with occasional Phosphor Green dot accents. Product screenshots appear in dark frames within cards. No photography, no lifestyle imagery. Icons are thin-stroke outlined (1.5px), monochrome in #fafafa or #b4b4b4, with Phosphor Green reserved for active/brand-icon contexts. The visual language is diagrammatic and technical — the aesthetic of a developer tool schematic, not a marketing site.

## Design Principles

### Do

- Use #3ecf8 (Phosphor Green) exclusively for primary CTAs, emphasized headline keywords, the logo, and active nav indicators — ration the green to one element per visual region
- Set all button radius to 9999px (pill) and all card radius to 16px — the pill/card duality defines the system
- Use Circular weight 400 for headlines and weight 500 for emphasis and button labels — never bold weight; the 500 is the loudest voice available
- Separate surfaces with 1px solid #2e2e2 borders on #121212 backgrounds — never rely on shadow to define elevation
- Keep letter-spacing at -0.007em uniformly across all sizes — the negative tracking is what makes Circular feel custom and tight
- Use #3ecf8 as the focus border color on inputs (1px, no glow ring) — the chromatic border replaces the conventional focus shadow
- Maintain page canvas at #121212 with no alternative — the single dark surface is the system's anchor

### Don't

- Don't introduce any chromatic color beyond the four greens — the monochrome discipline is the brand
- Don't use weight 600 or 700 in Circular — the type system tops out at 500; if you need more emphasis, increase size or use Phosphor Green
- Don't add box-shadows to cards, popovers, or modals — the design is deliberately flat; use #2e2e2 borders instead
- Don't use radius values other than 9999px (buttons/tags), 16px (cards), or 8px (inputs) — the limited radius vocabulary is intentional
- Don't place Phosphor Green on large background areas — it should appear as small functional punctuation, not as a section background
- Don't use light text on light backgrounds or any non-#121212 canvas — Snow (#fafafa) is the only text color
- Don't add gradients — the system is strictly flat, terminal-native, and gradient-free

## Components

### Pill Primary Button

Background #3ecf8, text #fafafa, border 1px solid #3ecf8 (on hover border shifts to #1f4b37). Padding 8px 16px. Radius 9999px. Circular 500 weight, 14px, line-height 1.43. The green is the only filled chromatic surface in the system — every green button should feel like a deliberate decision.

### Pill Ghost Button

Background transparent, border 1px solid #393939, text #fafafa. Padding 8px 16px. Radius 9999px. Circular 400 weight, 14px. On hover border shifts to #4d4d4d and background fills with rgba(255,255,255,0.04).

### Pill GitHub Stars

Background #242424, border 1px solid #2e2e2, text #fafafa, small GitHub icon in #fafafa. Padding 6px 10px. Radius 9999px. Circular 400, 12px. Compact, unobtrusive — it's a status indicator, not a CTA.

### Feature Card

Background #121212 (same as canvas, defined only by border). Border 1px solid #2e2e2e. Radius 16px. Padding 24px. Each card has a small icon in #3ecf8, a heading in #fafafa (Circular 500, 18px), body text in #b4b4b4 (Circular 400, 14px), and a dark illustration area in the lower half with line-art or wireframe graphics in #4d4d4d on #0d0d0d backgrounds.

### Product Showcase Card

Same surface as Feature Card: background #121212, border 1px solid #2e2e2, radius 16px, padding 24px. The visual area fills the card with a 3D geometric or wireframe illustration in #4d4d4d line work on #0d0d0d. Phosphor green dots or highlights appear as accent within the illustration — not as UI chrome.

### Testimonial Card

Background #121212, border 1px solid #2e2e2, radius 16px, padding 20px. Circular avatar 40px, handle in #fafafa (Circular 500, 14px), quote body in #b4b4b4 (Circular 400, 14px, line-height 1.5). Cards vary in height — masonry-style layout.

### Announcement Pill

Background #242424, border 1px solid #2e2e2, radius 9999px, padding 6px 16px. Circular 400, 12px, text #b4b4b4. Small chevron icon in #b4b4b4 on the right.

### Logo Cloud Item

Logos rendered in #898989 (monochrome) at uniform height ~24px. No backgrounds or borders — just floating marks on the canvas.

### Top Navigation Bar

Full-width, background transparent or #121212 on scroll. Height ~64px. Left: green Supabase logo (mark + wordmark in #fafafa). Center: nav links in #b4b4b4 (Circular 400, 14px). Right: GitHub stars pill, Sign in ghost button, Start your project green pill. 1px bottom border #2e2e2 for separation.

### Input Field

Background #121212, border 1px solid #393939, radius 8px, padding 8px 12px. Text in #fafafa, placeholder in #898989 (Circular 400, 14px). Focus: border shifts to #3ecf8 with no glow ring — the green border IS the focus indicator.

## Similar Design Systems

- {'why': 'Same monochrome dark canvas, single accent color strategy, and pill-button primary actions — Vercel uses white/blue, Supabase uses phosphor green', 'business': 'Vercel'}
- {'why': 'Dark developer-tool aesthetic with tight geometric typography and minimal surface treatment — similar card grid patterns and code-editor visual language', 'business': 'Railway'}
- {'why': 'Dark-mode product UI with rationed color usage, hairline borders instead of shadows, and pill-shaped interactive elements', 'business': 'Linear'}
- {'why': 'Dark database-platform marketing site with centered hero, monochrome palette, and a single vivid accent for emphasis', 'business': 'PlanetScale'}
- {'why': 'Similar dark devtools aesthetic with phosphor-toned accent color and terminal-inspired UI — the green-on-black visual heritage is shared', 'business': 'Neon'}

## Agent Prompt Guide

## Quick Color Reference
- text: #fafafa
- background: #121212
- card surface: #121212 (with #2e2e2e border)
- border: #2e2e2e (cards), #393939 (inputs), #4d4d4d (icons)
- accent: #3ecf8e (Phosphor Green)
- primary action: no distinct CTA color

## Example Component Prompts

1. **Hero Section**: Centered on #121212 canvas. Display headline at 72px Circular weight 400, #fafafa, letter-spacing -0.5px. Second line in #3ecf8e. Subtitle at 16px Circular 400, #b4b4b4, line-height 1.5. Two pill buttons side by side: green primary (#3ecf8e fill, #fafafa text, 9999px radius, 8px 16px padding) and ghost secondary (transparent, 1px #393939 border, #fafafa text, 9999px radius).

2. **Feature Card Grid**: 2x2 grid on #121212. Each card: 16px radius, 1px solid #2e2e2e border, 24px padding. Icon in #3ecf8e at 24px stroke. Heading in #fafafa Circular 500 18px. Body in #b4b4b4 Circular 400 14px line-height 1.5. Lower half of card has dark illustration area (#0d0d0d background) with #4d4d4d line-art.

3. **Top Navigation**: 64px height, full-width, #121212 background. Left: Supabase logo (green mark + #fafafa wordmark). Center: nav links in #b4b4b4 Circular 400 14px. Right: GitHub stars pill (#242424 bg, #2e2e2e border, 9999px radius), Sign in ghost button, green Start your project pill.

4. **Testimonial Card**: 16px radius, 1px solid #2e2e2e border, 20px padding. 40px circular avatar, handle in #fafafa Circular 500 14px, quote in #b4b4b4 Circular 400 14px line-height 1.5. Masonry layout in 4-column grid.

5. **Input Field**: Background #121212, border 1px solid #393939, radius 8px, padding 8px 12px. Text in #fafafa Circular 400 14px, placeholder in #898989. On focus: border changes to #3ecf8e — no glow ring or shadow.
