# Default — Design System

> **North Star**: Mission control behind frosted glass — weight 400 headlines float over matte-black panels lit by thin blue ring-light accents.
> **Theme**: dark
> **Source**: https://www.default.com
> **Refero Style**: https://styles.refero.design/style/eeeb6ac9-fc07-4965-935a-e1989ed831f1
> **Synced**: 2026-09-01

## Overview

Default operates in a dark control-room language: near-black canvas, hairline borders, and pill-shaped controls that feel calm rather than loud. Typography stays light — weight 400 at 52–64px — so headlines whisper against the matte background instead of shouting. Color is rationed: blue is the only true brand accent (links, active states, highlights, rings), green/red are reserved for success/destructive signals, and neutral fills (off-white #f2f2f2) do the work of primary CTAs. Surfaces stack in subtle elevation jumps (canvas → card → elevated panel) achieved mostly through 0.5px hairlines and inset 1px white-alpha highlights rather than drop shadows. Components are tight, compact, and information-dense — this is infrastructure software, not marketing spectacle.

## Color Palette

- **Void**: `#0b0c0e` — Deepest page canvas, terminal background, behind everything [neutral]
- **Graphite**: `#131416` — Primary card surface, panels, elevated containers, table rows [neutral]
- **Charcoal**: `#1f1f21` — Secondary surface, borders, dividers, rail backgrounds [neutral]
- **Smoke**: `#3c3d3e` — Button borders, subtle separators [neutral]
- **Steel**: `#71717a` — Muted body text, captions, helper text, dimmed labels [neutral]
- **Fog**: `#858687` — Secondary text, icon strokes, inactive nav items [neutral]
- **Ash**: `#9d9e9f` — Tertiary text, placeholder text, disabled states [neutral]
- **Chalk**: `#cececf` — Body text secondary, table cell text [neutral]
- **Snow**: `#ffffff` — Primary headings, body text, icon fills, active states — the dominant ink at 413 occurrences [neutral]
- **Bone**: `#f2f2f2` — Primary action button fill — off-white pill against dark creates the highest-contrast CTA without introducing a chromatic brand color [neutral]
- **Ink**: `#333333` — Secondary body text, navigation labels, and subdued headings. Do not promote it to the primary CTA color [neutral]
- **Signal Blue**: `#3b82f6` — Brand accent — active nav indicators, link highlights, icon fills, active card borders. The one true chromatic color; used 21 times as fills, borders, and background tints [brand]
- **Arc Blue**: `#60a5fa` — Light blue text accent, informational highlights, node icons in workflow diagrams [brand]
- **Ring Blue**: `#93c5fd` — Focus rings, active card outline borders, selection state outlines at low alpha [brand]
- **Mint**: `#4ade80` — Green outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color [accent]
- **Fern**: `#22c55e` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]
- **Coral**: `#f87171` — Red text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Ember**: `#ea580c` — Decorative icon accent — orange chromatic chip in product mockups [accent]
- **Iris**: `#314ef0` — Brand chip background tint in embedded mockups and product screenshots [accent]

## Typography

- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| body-lg | 14 | — | 1.43 |
| body-xl | 16 | — | 1.5 |
| subheading | 18 | — | 1 |
| heading | 32 | — | 1.25 |
| heading-lg | 42 | — | 1.2 |
| display | 52 | — | 1 |
| display-lg | 64 | — | 0.94 |

## Spacing & Layout

- **Max Width**: 1080px
- **Card Padding**: 28px
- **Element Gap**: 8px
- **Section Gap**: 96px
- **Border Radius**: {'lg': '16px', 'md': '12px', 'sm': '8.77px', 'xl': '20px', 'xs': '5.26px', '2xl': '24px', 'cards': '12px', 'pills': '10px', 'buttons': '10px'}

## Layout

Max-width 1080px (67.5rem) centered, with sections that feel full-bleed but content stays contained. Hero is a two-column split: large headline left (60% width), supporting copy + CTA right (40% width), with a multi-panel product mockup below spanning full width. Below the hero: logo strip (single row, centered), then a feature section with a dark canvas and floating icon tiles that bleed beyond the content column. The infrastructure section uses a tabbed two-column layout: left column (30%) lists tab labels with icons and short descriptions, right column (70%) shows an active product mockup. Cards and panels are 12px radius with 28px 32px padding. Section gaps are generous (96px+) to let the dark sections breathe. Navigation is a single sticky top bar at 72px — no sidebar, no mega-menu visible, just a 'Platform' dropdown trigger.

## Surfaces / Elevation

- **Void**
- **Graphite**
- **Charcoal**
- **Soft Fill**

**Shadow tokens:**

## Imagery

No photography. The visual language is pure UI: product mockups, workflow node diagrams, data tables, and tool icon tiles. Embedded product screenshots are the primary visual content — they show a dark CRM-like interface with green status badges, blue workflow nodes, and tabular data. The 'revenue stack' section uses floating icon tiles (Salesforce, HubSpot, etc.) at varying opacity with backdrop blur to create a spatial depth effect — sharp tiles in the foreground, blurred tiles fading into the background. The hero features a large multi-panel product mockup with a chat panel, a workflow canvas with connected nodes, and a form builder. All imagery is rendered in the same dark palette as the UI — there is no light-mode content, no lifestyle photography, no abstract gradients.

## Design Principles

### Do

- Use weight 400 for all headlines 32px and above — the whisper-weight is the signature
- Set primary action buttons to #f2f2f2 fill with #333333 text and 10px radius — never introduce a chromatic brand color for CTAs
- Apply 0.5px solid borders (never 1px) for card edges, dividers, and panel outlines
- Use Inter with 'ss01' and 'ss03' font features enabled — the geometric alternates are part of the identity
- Stack surfaces in three levels: #0b0c0 canvas → #131416 card → rgba(255,255,255,0.05) hover
- Apply tight letter-spacing at body sizes: -0.026em at 13px, -0.023em at 14px, -0.034em at 18px
- Use Signal Blue (#3b82f6) only for active states, links, and icon accents — never for backgrounds or large fills

### Don't

- Do not use weight 600+ for headlines — it breaks the calm, terminal-like register
- Do not use blue or any chromatic color for CTA buttons — the bone (#f2f2f2) pill is the only primary action
- Do not use 1px or thicker borders — 0.5px hairlines are essential to the 'frosted glass' surface treatment
- Do not apply large drop shadows to cards — elevation comes from inset highlights, not cast shadows
- Do not use more than one weight from the 500+ range per text block — the type system is built on the 400–480 range
- Do not introduce gradients on UI elements — the site is deliberately flat with single-color fills only
- Do not use green or red as decorative color — they are semantic signals (success/destructive) only

## Components

### Primary Pill Button (Bone)

Background #f2f2f2, text #333333, border none, border-radius 10px, padding 8px 20px, font-size 14px weight 400. Shadow: 0 1px 4px rgba(0,0,0,0.1) + 0 0 1px rgba(0,0,0,0.1). The off-white fill against the dark canvas is the only bright element on most pages — it reads as a single confident click target.

### Secondary Pill Button (Ghost)

Background rgba(255,255,255,0.05), text #ffffff, border none, border-radius 10px, padding 8px 16px, font-size 14px weight 400. Whisper-quiet on dark — present but not competing with the primary action.

### Text Link Button

Background transparent, text rgba(255,255,255,0.92), border none, no padding, border-radius 0, font-size 14px weight 400. The high opacity (0.92, not 1.0) creates a subtle softness that distinguishes links from body text without a color shift.

### Announcement Bar

Full-bleed strip at top of page, background #0b0c0, text 14px weight 400, centered. Includes 'Read more' link in #ffffff with underline. Dismissible with × icon at 92% opacity.

### Feature Card (Tabbed Content)

Background #121316, border-radius 12px, padding 28px 32px, no visible shadow. Left column lists tab labels with small icon (16px) in signal blue, text #ffffff, 14px weight 400. Active tab has a white underline indicator.

### Product Mockup Card (Floating Panel)

Background rgba(21,22,24,0.8), border-radius 7px, with a complex layered shadow: 0 100px 106px rgba(0,0,0,0.05), 0 42px 44px rgba(0,0,0,0.04), 0 22px 24px rgba(0,0,0,0.03), 0 12px 12px rgba(0,0,0,0.03). Contains tab bar at top, data table or workflow canvas inside, status badges with green/blue text.

### Logo Strip Card

Transparent background, logos rendered in #858687 (mid-gray) with brightness(0) invert(1) filter on dark surfaces. No card container — logos float in a single row with 48–64px gap. Logos are monochrome to avoid chromatic noise.

### Status Badge (Live/Active)

Background transparent or rgba(74,222,128,0.1), text #4ade80, border 1px #4ade80, border-radius 5.26px, padding 2px 6px, font-size 9–10px weight 500. Small green dot prefix. The thin border + green text combo is more architectural than a solid filled badge.

### Workflow Node Card

Background #131416, border 1px rgba(255,255,255,0.08), border-radius 8.77px, padding 12px. Contains small icon (16px) in node-specific color (blue for triggers, green for actions, orange for enrichtment), node title in 12px weight 500, description in 10px weight 400 in #858687. Connected by thin lines with small circular handle dots.

### Nav Header

Height 72px (4.5rem), background transparent over hero, becomes semi-transparent with backdrop blur on scroll. Contains logo (left), nav items centered (Platform dropdown, Agent, Resources) at 14px weight 400, Login text link + Request a Demo pill button (right). Border-bottom 0.5px rgba(255,255,255,0.07) when scrolled.

### Data Table Row

Background #131416, border-bottom 0.5px rgba(255,255,255,0.05), padding 8px 12px. Cell text 10–12px weight 400 in #cececf. Avatar circles 16px with company logo, company name in #ffffff, numeric values right-aligned. Column headers in 9px weight 500 in #858687 with sort indicators.

### Icon Tile (Tool Icon)

Background rgba(255,255,255,0.03), border 0.5px rgba(255,255,255,0.08), border-radius 8.77px, size 48–64px, contains a single monochrome icon at 24px in #858687 or #b6b6b7. Tiles float with varied opacity and blur to create depth — some are sharp, some are 20–30% opacity, some have backdrop blur.

### Footer

Background #171717, padding 48px vertical, border-top 0.5px rgba(255,255,255,0.07). Columns of links in 12px weight 400 #858687, section headers in 9px weight 500 #71717a. No large logo or social icons visible — minimal and institutional.

## Similar Design Systems

- {'why': 'Same dark canvas with near-black backgrounds, hairline borders, Inter typeface with whisper-weight headlines, and pill-shaped CTAs', 'business': 'Linear'}
- {'why': 'Same weight-400 display type, #f2f2f2 bone-white primary buttons on black, and minimal chromatic palette with one signal accent', 'business': 'Vercel'}
- {'why': 'Same developer-tool aesthetic with dark surfaces, green/red semantic status colors, and Inter at light weights for all display sizes', 'business': 'Cursor'}
- {'why': 'Same information-dense dark UI with product mockup screenshots as the primary visual, compact spacing, and hairline-bordered panels', 'business': 'Retool'}
- {'why': 'Same infra-for-engineers positioning reflected in the terminal-like type weight, dark matte surfaces, and rationed blue accent color', 'business': 'Modal'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff (primary), #858687 (secondary), #71717a (muted)
- background: #0b0c0e (page), #131416 (card), #1f1f21 (panel)
- border: rgba(255,255,255,0.07) at 0.5px
- accent: #3b82f6 (Signal Blue)
- primary action: #f2f2f2 (filled action)

**Example Component Prompts**

1. Create a hero section: #0b0c0e background. Headline at 52px Inter weight 400, #ffffff, letter-spacing -1.3px, line-height 1.0. Secondary pill button: #f2f2f2 fill, #333 text, 10px radius, 8px 20px padding, 14px Inter weight 400. Subtext at 18px Inter weight 450, #858687, letter-spacing -0.61px.

2. Create a feature card: #131416 background, 12px radius, 28px 32px padding, 0.5px solid rgba(255,255,255,0.07) border. Title at 32px Inter weight 400, #ffffff. Description at 14px Inter weight 400, #858687. Small icon at 16px in #3b82f6.

3. Create a status badge: transparent background, 1px solid #4ade80 border, 5.26px radius, 2px 6px padding, 9px Inter weight 500, #4ade80 text. Prefix with 4px green dot.

4. Create a workflow node card: #131416 background, 8.77px radius, 12px padding, 0.5px solid rgba(255,255,255,0.08) border. Title at 12px Inter weight 500, #ffffff. Description at 10px Inter weight 400, #858687.

5. Create a nav header: 72px height, transparent background, backdrop blur 6px. Logo left, nav items centered at 14px Inter weight 400, login text link + secondary pill button right. Bottom border 0.5px rgba(255,255,255,0.07).
