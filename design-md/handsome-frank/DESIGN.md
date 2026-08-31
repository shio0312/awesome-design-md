# Handsome Frank — Design System

> **North Star**: Curator's atelier with living murals — a warm-paper gallery where illustrated worlds bloom against indigo frames.
> **Theme**: light
> **Source**: https://www.handsomefrank.com
> **Refero Style**: https://styles.refero.design/style/19d4103a-9f4a-49f0-ad7d-af6588bab904
> **Synced**: 2026-09-01

## Overview

Handsome Frank operates as a curator's atelier for contemporary illustration: full-bleed illustrated hero scenes give way to warm paper-toned canvases where artist work is presented with museum-label restraint. The system is defined by a single dominant deep indigo (#160572) that anchors navigation, headlines, and the closing footer bar, surrounded by hairline black borders that act like gallery frame edges. Typography is a two-voice conversation — a tight-tracked editorial serif (Millik) for hero/display headlines and a quiet grotesque (Klarheit) for everything structural. Color is deployed as curated punctuation: the hero illustration carries the chromatic spectrum, while the rest of the page stays achromatic with isolated bursts of vivid red, teal, orange, and yellow acting as spotlight accents on links, tags, and project cards.

## Color Palette

- **Indigo Frame**: `#160572` — Navigation strokes, display headlines, footer band — the deepest anchor in the system, commanding authority without shouting [brand]
- **Cream Paper**: `#f2ebe6` — Primary page canvas for content sections — warm eggshell that softens black text and lets illustration breathe [neutral]
- **Pure White**: `#ffffff` — Card surfaces, reversed text on dark bands, and the clean counterpoint to cream — the gallery wall [neutral]
- **Obsidian Hairline**: `#000000` — Dominant border, text, and icon stroke — used as a 1-2px frame line across nav, cards, and decorative elements [neutral]
- **Slate Ink**: `#2c2c2c` — Secondary text and softer borders where pure black feels too severe [neutral]
- **Fog Wash**: `#eef4fb` — Pale blue-tinted background for muted emphasis blocks [neutral]
- **Buttermilk**: `#fef9ee` — Subtle warm wash for highlighted text or callout backgrounds [neutral]
- **Crimson Spotlight**: `#ea0706` — Editorial accent for critical announcements and bold display statements — the marquee marker [accent]
- **Vermillion**: `#d64e2e` — Warm secondary accent on project card titles, links, and illustrative borders [accent]
- **Apricot Whisper**: `#e29675` — Soft warm accent for icon strokes and decorative borders [accent]
- **Peach Blush**: `#eea883` — Mid-warmth accent on icon outlines and link underlines [accent]
- **Tangerine Pop**: `#ff7701` — Filled action button background — the only true filled CTA, used for the play/forward action in the footer [accent]
- **Cobalt Stage**: `#2544a0` — Filled action button background for primary browse/enter actions [accent]
- **Plum Velvet**: `#4b0f4d` — Filled action button background for dark editorial CTAs [accent]
- **Rose Petal**: `#d98199` — Filled action button background for soft secondary entries [accent]
- **Electric Teal**: `#24e3dc` — Interactive link and menu accent — the only cool chromatic in the system, reserved for navigation affordances [accent]
- **Acid Green**: `#24e34c` — Secondary interactive link accent for hover/active states [accent]
- **Daffodil**: `#f9e44d` — Decorative icon and link accent — cheerful punctuation [accent]
- **Highlighter Yellow**: `#ffff00` — Badge background for editorial tags and callout labels [semantic]

## Typography

- **Arial**
- **Millik**
- **Klarheit Grotesk**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.2 |
| body-sm | 14 | — | 1.36 |
| body | 16 | — | 1.36 |
| subheading | 22 | — | 1.28 |
| heading | 32 | — | 1.1 |
| heading-lg | 54 | — | 1 |
| display | 88 | — | 0.95 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 20-24px
- **Element Gap**: 20px
- **Section Gap**: 64-80px
- **Border Radius**: {'nav': '0px', 'cards': '10px', 'buttons': '30px', 'projectCards': '0px'}

## Layout

The page is a vertical scroll of full-bleed and max-width-contained sections alternating. The hero is 100% viewport, illustration-only with overlaid white type at lower-left. Content sections are max-width ~1200px centered on a cream (#f2ebe6) canvas, with generous vertical breathing room (64-80px section gaps). The artist grid is a 4-column row of square thumbnails with 20-24px gaps. The featured project section uses a 4-column grid of full-bleed solid-color cards with centered circular image cutouts. The announcement banner spans full-width with centered or split content. The closing footer is a full-bleed indigo band, ~100-120px tall, with centered pill button + label. Navigation is minimal: a fixed script wordmark top-left and a circular teal hamburger top-right — no nav bar, no breadcrumbs. The rhythm is: immersive hero → quiet cream gallery → bold color wall → quiet announcement → bold indigo close.

## Surfaces / Elevation

- **Cream Paper**
- **Pure White**
- **Indigo Band**
- **Obsidian**

## Imagery

The site is defined by full-bleed, edge-to-edge illustration as its primary visual language. The hero is a rich, densely composed tropical jungle scene with vibrant birds in red, blue, teal, orange, and yellow against layered dark green foliage — a maximalist botanical mural. Subsequent sections showcase artist work as flat, full-color square or circular thumbnails with no borders or treatments applied; the artwork is always raw and unframed. Photography does not appear — every image is hand-illustrated. Iconography is minimal (hamburger lines, play triangle, social glyphs), all in white or black line. The illustration carries the chromatic spectrum; the UI chrome stays achromatic except for the indigo structural color.

## Design Principles

### Do

- Use Millik serif for all display headlines and editorial titles; let it carry the personality with negative letter-spacing and tight line-height (0.95-1.10)
- Reserve #160572 indigo for navigation strokes, editorial headlines, and the closing footer band — it is the thread that stitches the page together
- Use the full pill shape (30px radius) for all filled action buttons, and pick from the four chromatic button backgrounds (#2544a0, #ff7701, #4b0f4d, #d98199) by context
- Apply 1-2px solid #000000 hairlines as decorative frames around cards, nav elements, and illustration containers — the gallery-frame motif
- Let illustrated or photographic content fill its container edge-to-edge with no border or radius — the artwork defines its own boundary
- Use #ffff00 as a flat badge/tag background with black text for editorial callouts — treat it like a highlighter pen mark
- Keep body text at 16px Klarheit Grotesk Regular with line-height 1.36 on the cream (#f2ebe6) canvas — the warmth softens the otherwise stark black/white system

### Don't

- Don't use neutral grays for primary buttons — the system has no gray CTA; buttons are always chromatic and pill-shaped
- Don't apply border-radius to project cards, illustration thumbnails, or content cards — only pill buttons get curves (30px), everything else stays sharp-edged
- Don't use the chromatic accent colors (teal, green, red, yellow, orange) for body text or large text blocks — they are reserved for links, icons, badges, and decorative strokes only
- Don't drop shadows on cards or images — the design uses hairline borders and flat color blocks for separation, never elevation
- Don't set body text below 14px or use letter-spacing looser than normal on small sizes — the system relies on compact, confident type
- Don't use gradient backgrounds or colored overlays on imagery — illustrations and photos display raw, edge-to-edge, on their own colors
- Don't center-align body paragraphs or nav items — the layout is left-aligned for text blocks and centered only for display headlines and footer CTAs

## Components

### Full-Bleed Illustrated Hero

Edge-to-edge illustration covering 100% viewport width and height. No padding or margin. Text overlay is white, left-aligned, positioned at lower-third. Logo sits top-left in white script. Single teal circular hamburger menu top-right. The illustration IS the surface — no card, no frame, no overlay tint.

### Hero Display Headline

Millik 88px, weight 400, line-height 0.95, letter-spacing -4.4px, color #ffffff. Sits directly on the illustrated hero. One bold sentence + one supporting tagline (Millik 22px, weight 400, line-height 1.36). No drop shadow — the contrast against the dark foliage carries readability.

### Script Wordmark

Custom calligraphic script reading 'Handsome Frank'. White on dark sections, indigo on light sections. Fixed top-left, ~24-32px height. Stays present across scroll.

### Circular Menu Trigger

Solid teal (#24e3dc) circle, ~48px diameter, three white horizontal lines (hamburger). Fixed top-right. No border, no shadow. The only persistent interactive chrome.

### Editorial Section Headline

Millik 32-42px, weight 400, line-height 1.00-1.10, color #160572. Centered, sits above a row of cards. Generous 40-60px margin-top, 30-40px margin-bottom. The indigo color is the thread connecting nav, headline, and footer.

### Artist Portfolio Card

Square or near-square thumbnail of the artist's signature illustration. No border, no radius — the artwork's own edges define the card. Artist name below in Klarheit Grotesk 14px bold, centered. Background: cream paper. Gap between cards: 20-24px. 4-column grid on desktop.

### Featured Project Card

Full-bleed solid color card (#2544a0, #ff7701, #4b0f4d, #d98199 used as card backgrounds). Large circular image cutout (radius 50%) centered in the card. Project title in Klarheit Grotesk 22px bold, white, top-left aligned. 4-column grid. Cards have no radius — they are bold flat color blocks.

### Pill Button (Filled)

Border-radius 30px (full pill). Background: one of the filled chromatic colors (#2544a0, #ff7701, #4b0f4d, #d98199). Text: Klarheit Grotesk 14-16px bold, white. Padding: 12-16px vertical, 28-38px horizontal. No border, no shadow. The pill shape is the signature button form — used sparingly for browse/enter actions only.

### Outlined Link

Klarheit Grotesk 14-16px, color matching the accent palette (teal, green, red, orange, yellow). Underlined with a 1-2px solid border in the same color, 2-4px offset from baseline. No background. The colored underline IS the link affordance — no button shape needed.

### Highlighter Badge

Background #ffff00 (highlighter yellow). Text: Klarheit Grotesk 12px bold, #000000. No border, no radius. Padding: 4-6px vertical, 8-10px horizontal. Mimics a physical highlighter pen mark on a page.

### Announcement Banner

Sits above the footer. Cream or white background. Headline in Millik 54px weight 700, color #ea0706 (crimson). A small circular avatar thumbnail precedes the text. Follow CTA in Klarheit Grotesk 22px bold to the right. The red headline is the loudest single moment on an otherwise quiet page.

### Indigo Footer Band

Full-bleed #160572 background, ~100-120px tall. Centered content: a tangerine pill button with white play-icon glyph, followed by 'Browse Illustrators.' in Klarheit Grotesk 22px bold, white. The contrast between the orange button and indigo bar is the strongest color pairing in the system.

### Hairline Border Frame

1-2px solid #000000 border. Used on cards, nav elements, decorative containers, and section dividers. The black hairline is the connective tissue — it gives every element gallery-frame presence without weight.

## Similar Design Systems

- {'why': 'Same editorial-creative-agency energy: curated artist spotlights, full-bleed illustration heroes, serif display headlines, and a quiet achromatic page that lets the work speak', 'business': "It's Nice That"}
- {'why': 'Same confident use of full-bleed illustration as primary content, large editorial serif type, and a cream/warm-paper canvas for secondary sections', 'business': 'WeTransfer / Paper by FiftyThree'}
- {'why': 'Same flat-color-block project cards with circular image cutouts, bold chromatic backgrounds behind featured work, and a dark closing band', 'business': 'Studio Brasch'}
- {'why': 'Same minimal navigation chrome (wordmark + circular menu), generous section breathing room, and a two-voice typography system pairing a display serif with a quiet grotesque', 'business': 'Apt Studio'}

## Agent Prompt Guide

## Quick Color Reference
- Text: #000000 (primary), #2c2c2c (secondary), #160572 (headlines/brand)
- Background: #f2ebe6 (cream canvas), #ffffff (cards), #160572 (footer band)
- Border: #000000 hairline 1-2px (structural frames)
- Accent: #24e3dc (teal, interactive), #ea0706 (crimson, editorial)
- primary action: #ff7701 (filled action)

## Example Component Prompts

1. **Full-Bleed Illustrated Hero**: Full-viewport (100vw × 100vh) illustrated background with no padding, no border, no overlay. White script wordmark 'Handsome Frank' fixed top-left at 28px height. Teal (#24e3dc) circular hamburger button 48px diameter fixed top-right with three white lines. White display headline at 88px Millik weight 400, line-height 0.95, letter-spacing -4.4px, positioned at 40% from top, left-aligned with 80px left margin. Supporting tagline at 22px Millik weight 400, line-height 1.36, white, directly below.

2. **Artist Portfolio Card Grid**: 4-column grid on cream (#f2ebe6) background, 20px gap. Each card is a square (1:1) illustration thumbnail with no border, no radius — artwork fills the container. Artist name below in Klarheit Grotesk 14px weight 700, color #000000, centered, 12px margin-top from card.

3. **Featured Project Card**: Full-bleed solid color block (choose from #2544a0, #ff7701, #4b0f4d, #d98199), no border, no radius. 200px circular image cutout (border-radius 50%) centered horizontally, positioned 40% from top. Project title in Klarheit Grotesk 22px weight 700, white, top-left aligned with 24px padding.

4. **Outlined Link**: Klarheit Grotesk 16px weight 400, color #24e3dc (teal) or other accent. Underline is a 2px solid border-bottom in the same color, offset 4px from text baseline. No background, no button shape, no padding.

5. **Indigo Footer Band**: Full-bleed #160572 background, 120px tall, centered content. Tangerine (#ff7701) pill button 48px tall, 30px border-radius, white play triangle glyph. Button label 'Browse Illustrators.' in Klarheit Grotesk 22px weight 700, white, 16px to the right of the button.

## Gallery-Frame Motif

The 1-2px solid black hairline border is not just a separator — it is the design's signature gesture. Every card, every nav element, every decorative container is treated as an object hung on a gallery wall. The border gives each element presence and weight without using shadow or fill. When in doubt about how to separate two elements, add a 1px #000000 border rather than increasing whitespace, changing background color, or adding elevation. This is the system's way of saying: this is curated, this is framed, this matters.
