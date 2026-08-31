# Family — Design System

> **North Star**: storybook spread on cream parchment
> **Theme**: light
> **Source**: https://family.co
> **Refero Style**: https://styles.refero.design/style/1bcae895-2245-4d33-aa43-1c1e80719554
> **Synced**: 2026-09-01

## Overview

Family speaks in a warm parchment-and-marker language: a cream canvas (#fbfaf9) carries hand-drawn characters and scattered confetti shapes in primary-bright fills, while typography stays calm and utilitarian in Inter. The interface itself is deliberately restrained — inset hairline borders define surfaces rather than shadows — so the cartoon illustrations carry all the emotional weight and the chrome stays quiet. Color functions as semantic markers: near-black for the one serious action, blue and orange for status, gold and green for positive signals, red and pink for destructive/attention. Every screen should feel like a children's storybook spread: generous whitespace, big confident headings, and a few vivid characters punctuating an otherwise monochrome layout.

## Color Palette

- **Cream Canvas**: `#fbfaf9` — Page background, nav surface — warm off-white that reads as paper rather than screen [neutral]
- **Stone Surface**: `#f2f0ed` — Card surfaces, secondary panels, inset border tone — one shade darker than canvas to create depth without shadow [neutral]
- **Ink Black**: `#121212` — Headings, primary action fill, dark card surfaces — near-black that stays slightly warm [neutral]
- **Heading Charcoal**: `#343433` — Primary text, nav text, decorative strokes — softened black for readable body [neutral]
- **Body Brown**: `#474645` — Body copy, secondary text — warm desaturated brown rather than cool gray [neutral]
- **Muted Gray**: `#7e7e7d` — Helper text, inactive nav, tertiary labels [neutral]
- **Stone Border**: `#e5d5c3` — Hairline decorative borders on illustrations and shapes [neutral]
- **Link Blue**: `#0086fc` — Inline links, feature list text — vivid blue that reads as actionable without being a button [accent]
- **Sky Blue**: `#64c6ff` — Illustration fill, decorative mascot accents — sky-bright for storybook characters [accent]
- **Alt Blue**: `#00b2ff` — Secondary illustration fill, icon accents — slightly deeper blue for variation [accent]
- **Grass Green**: `#00c978` — Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Mint**: `#00ca48` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]
- **Ember Orange**: `#ff3e00` — Orange text accent for links, tags, and emphasized short phrases [brand]
- **Sun Yellow**: `#ffcd6c` — Illustration fill, decorative shapes, mascot coloring [accent]
- **Gold**: `#d48f00` — Yellow text accent for links, tags, and emphasized short phrases. [accent]
- **Honey**: `#ffbb26` — Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content [accent]
- **Coral Pink**: `#ff58ae` — Purchase badge fill, decorative illustration accent [accent]
- **Plum Violet**: `#9f4fff` — Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color [accent]
- **Alert Red**: `#ff2b3a` — Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]

## Typography

- **Family**
- **Inter**
- **Inter**
- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| micro | 12 | — | 19 |
| caption | 15 | — | 22 |
| body | 17 | — | 26 |
| subheading | 19 | — | 27 |
| heading | 23 | — | 25 |
| heading-lg | 44 | — | 53 |
| display | 68 | — | 75 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 8-12px
- **Section Gap**: 80-120px
- **Border Radius**: {'nav': '10px', 'cards': '10px', 'icons': '40px', 'pills': '9999px', 'small': '2px', 'badges': '6px', 'buttons': '32px', 'illustration': '72px'}

## Layout

Full-width centered layout with max-width ~1200px for content. Hero is a three-column composition: left illustration cluster, centered headline+subtitle+CTA stack, right illustration cluster — all on the cream canvas. Below the hero, content flows in vertical bands separated by generous whitespace (80-120px section gaps). The 'Explore Ethereum' section uses a 3-column card grid with the dark Send/Swap/Receive card as left-column visual anchor, followed by a second row of three lighter feature cards. A second 3-column grid below shows phone mockups. The 'Friends of Family' section is a horizontally-scrolling 4-column tweet card grid. Navigation is a minimal top bar with logo left, center links, and two pill buttons (ghost + dark) right-aligned — no sidebar, no mega-menu. The overall rhythm alternates quiet centered-text sections with colorful illustration-rich sections.

## Surfaces / Elevation

- **Canvas**
- **Stone**
- **Sand**
- **Pure White**
- **Dark Surface**
- **Full Black**

**Shadow tokens:**

## Imagery

Illustration is the primary visual language: hand-drawn cartoon mascots (flower with square face, smiling green blob, yellow triangle character, orange cloud, cat) with dot eyes and stick limbs, rendered in flat fills from the accent palette (sky blue #64c6ff, sun yellow #ffcd6c, grass green #00c978, ember orange #ff3e00, coral pink #ff58ae). Scattered confetti shapes (coins, stars, hearts, gears, leaves, lock icons, QR markers) fill the negative space around them. All illustration strokes are #343433 at thin weight. Mascots use generous organic radii (40-72px). The illustrations are full-bleed on the left and right of the hero, then appear as smaller accents inside cards throughout the rest of the page. Photography is absent; phone mockups in the lower section show dark iOS UI screenshots. Icon style is solid filled circles in saturated brand colors, mono-weight.

## Design Principles

### Do

- Use the custom Family typeface at 44-68px weight 500 for all display and hero headings; never substitute system fonts at this scale
- Use 10px radius as the default for cards and nav surfaces; use 32-9999px only for pill buttons and badges
- Build card definition with a 1px inset border in #f2f0ed rather than a drop shadow — the page should feel pressed into paper, not floating
- Let #ff3e00 carry the 'demo link' and accent text role; keep ember orange for inline links and feature callouts, never as a filled button
- Set body text in Inter 400 at 16-17px with line-height 1.42-1.53 and letter-spacing -0.013 to -0.016em
- Use the cream canvas (#fbfaf9) as the base for every full-bleed section; alternate by introducing the #f2f0ed stone surface for grouped card clusters
- Use illustration clusters of cartoon mascots in primary fills to anchor hero sections; scatter them asymmetrically so the centered text remains the focal point

### Don't

- Never use a drop shadow larger than rgba(0,0,0,0.04) — the design system rejects heavy elevation
- Don't use blue (#0086fc) as a filled CTA background; blue is reserved for inline links and list emphasis text
- Don't introduce gradients — the system is strictly flat with hairline inset borders
- Don't use Inter at the display sizes — display and hero headings must use the Family typeface at weight 500
- Don't separate surfaces with white-on-white; always shift toward #f2f0ed stone or toward #121212 black for clear contrast
- Don't add decoration to pill buttons — dark pill (#121212) and sand pill (#f6f4ef) are the only two pill variants
- Don't use warm reds (#ff2b3a) for anything beyond destructive/error states; the warm accent slot belongs to #ff3e00

## Components

### Hero Illustration Cluster

Hand-drawn cartoon mascots (flower, blob, cat, triangle character) with scattered confetti shapes (stars, coins, hearts, gears, leaves). Uses fills from the accent palette (#64c6ff, #ffcd6c, #00c978, #ff3e00, #ff58ae, #e5d5c3) with thin strokes at #343433. Shapes use organic radii of 40-72px. Two clusters flank a centered text block — they do not overlap the type.

### Ghost Nav Button

Transparent background, text in #343433, no border, font-size 13-14px Inter 400. Sits flush left of the primary CTA in the top nav.

### Dark Pill Button

Background #121212, text white, fully rounded (32px radius), horizontal padding 14px, vertical padding sized to content height (roughly 8-11px). Small, dense, high-contrast — the one moment of darkness in the header.

### Sand Pill Button

Background #f6f4ef (lighter than canvas), text #121212, 32px pill radius, 14px horizontal padding. Pairs beside the dark primary to create tonal contrast.

### Inline Demo Link

Underlined text link, no border, no background padding beyond 4px vertical. Color is #ff3e00 (ember orange) — this is the brand's signature secondary CTA color, used wherever a 'Watch the demo' or 'Manage your collectibles' link sits beneath a feature card. Border-radius 0 to read as text.

### Feature Card (Hairline-Bordered)

White background (#ffffff), 10px radius, 32px padding on all sides. Border is a 1px inset in #f2f0ed (stone surface) rather than a drop shadow — the card is defined by an interior hairline, giving a pressed-into-paper feel. Cards sit in a 3-column grid with 8-12px gaps. Heading is 23px Inter medium, body is 16-17px Inter 400 in #474645.

### Light Tag Surface

Background #fbfaf9 (same as canvas) or #fcfbf9, 12px radius, no shadow, horizontal padding ~23px, vertical padding 14px. Used for the 'Watching Wallets' / 'Wallet Activity' demo blocks. Defines surface through subtle warmth shift rather than contrast.

### Dark Feature Card

Background #000000, 24px left-only radius (asymmetric), 24px soft drop shadow at rgba(0,0,0,0.15), 4px padding. Houses a stacked list of icon+label rows in white/cream text — the only dark surface on the page, creating strong focal contrast against the cream canvas.

### Action Row (Inside Dark Card)

Each row: circular icon in app-brand color (#0090ff, #9f4fff, #00c978, #ff58ae), label in white Inter 500/600, helper text in muted white. Rows separated by 1-2px gaps. The colorful icons are the chromatic punctuation — the rest stays monochrome.

### Status Badge Pill

Fully rounded pill (9999px radius), background in status hue (mint #00ca48 for backing-up, gold #ffbb26 for pending), text in matching dark or light. Padded ~10-12px horizontal, 6-8px vertical. Sits inside light tag surfaces.

### Tweet Card

White background (#ffffff), 10px radius, 1px inset border in #f2f0ed, 32px padding. Avatar circle 40px, handle in #343433, tweet body in #474645 at 15-16px. X-platform icon top-right. Cards sit in a 4-column grid with horizontal scroll overflow.

### Inset-Bordered Surface

The signature border technique: 1px inset box-shadow in #f2f0ed creates an interior hairline on white surfaces. No drop shadows on cards — the system relies entirely on inset strokes and tonal shifts to separate layers. This is what gives the page its flat, pressed-into-paper quality.

## Similar Design Systems

- {'why': 'Same storybook illustration style with cartoon mascots on a light canvas, playful tone with utility-grade Inter typography', 'business': 'Phantom (crypto wallet)'}
- {'why': 'Similar cream-toned palette with playful illustrated characters and restrained typography for a crypto audience', 'business': 'Rainbow Wallet'}
- {'why': 'Same hairline-bordered card aesthetic, inset 1px borders instead of shadows, generous whitespace and quiet interface chrome', 'business': 'Stripe'}
- {'why': 'Same restrained typography hierarchy with custom display face over Inter body, minimal-elevation card system with deliberate restraint', 'business': 'Linear'}
- {'why': 'Same approach of using saturated brand colors as small accents against an otherwise quiet, near-monochrome interface', 'business': 'Coinbase'}

## Agent Prompt Guide

Quick Color Reference:
- text: #343433 (heading), #474645 (body)
- background: #fbfaf9 (canvas)
- border: inset 1px #f2f0ed
- accent (links/demo): #ff3e00
- accent (features): #0086fc
- primary action: #121212 (filled action)

3-5 Example Component Prompts:
1. Create a Primary Action Button: #121212 background, #fbfaf9 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Create a feature card grid (3 columns): white cards (#ffffff), 10px radius, 1px inset border #f2f0ed, 32px padding all sides. Heading at 23px Inter 500, #343433. Body at 16px Inter 400, #474645. 8-12px gap between cards. Underneath each card, an ember-orange (#ff3e00) inline 'Watch the demo' link with underline.

3. Create a dark feature card: background #000000, 24px left-radius (asymmetric), 24px soft shadow at rgba(0,0,0,0.15). Inside, stacked rows each with a 40px circular icon (colors #0090ff, #9f4fff, #00ca48, #ff58ae), label in white Inter 600, helper text in rgba(255,255,255,0.6) at 13px.

4. Create a status badge pill: fully rounded (9999px radius), background #00ca48 (mint) or #ffbb26 (honey), text in #121212 or #ffffff depending on contrast, 10-12px horizontal padding, 6-8px vertical padding. Sits inside a #fcfbf9 light surface with 12px radius.

5. Create a tweet card: white (#ffffff) background, 10px radius, 1px inset border #f2f0ed, 32px padding. 40px circular avatar, handle in #343433 at 15px Inter 600, body in #474645 at 15px Inter 400. X-platform icon in top-right corner. 3-4 cards per row with horizontal scroll.
