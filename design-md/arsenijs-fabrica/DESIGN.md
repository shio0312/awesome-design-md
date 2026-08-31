# Arsenijs Fabrica — Design System

> **North Star**: Editorial beauty spread under gallery lights. Pure-white gallery walls, a single warm strobe pulsing orange against the monochrome, type set thin as glass and hung with generous negative space.
> **Theme**: light
> **Source**: https://www.arsenijsfabrica.com
> **Refero Style**: https://styles.refero.design/style/eb3bf6c1-a18f-4d72-801e-50c2cdbbaa21
> **Synced**: 2026-09-01

## Overview

Arsenijs Fabrica operates as an editorial beauty spread: expansive white surfaces, whisper-weight display type that floats across the canvas, and a single vivid orange that cuts through monochrome like a studio strobe. The brand voice in type is restrained and continental — weights 200-300 at hero scale, near-black text on pure white, generous breathing room between sections. Orange appears as functional punctuation: filled CTAs, modal backgrounds, card borders, and link accents — never as a wash or gradient field. Components feel fashion-magazine lightweight: hairline 1px borders, 10px card corners, 600px pill buttons, and a deliberate absence of shadows across the structural layer.

## Color Palette

- **Ember Orange**: `#f15730` — Filled CTA buttons, primary action backgrounds — deep saturated orange that reads as confident rather than playful, the only color with enough chroma to anchor a click target against the white field [brand]
- **Tangerine Blaze**: `#f7651a` — Promotional surface fills (email capture modal, featured product cards, stat callout backgrounds) — slightly brighter and more luminous than Ember, used where orange must own an entire region of the layout [brand]
- **Apricot Whisper**: `#ff8562` — Borders on outlined cards, link underlines, icon strokes, accent hairlines — the lightest orange, functioning as a warm-tinted structural color rather than a fill [accent]
- **Graphite Black**: `#111111` — Body text, default borders, the dominant structural color — a true near-black, not warm, used for the bulk of hairline rules and paragraph copy [neutral]
- **Inkwell**: `#0d1717` — Heading text, navigation text, primary headings — a deep black with the faintest cool-green undertone that gives headlines a quiet cast against pure white [neutral]
- **Pure White**: `#ffffff` — Page canvas, card surfaces, text on dark/orange surfaces — the unchanging ground tone across every section [neutral]
- **Mist Gray**: `#eeeeee` — Soft card borders, hairline dividers on white surfaces where Graphite would feel too heavy [neutral]
- **Smoke**: `#818181` — Secondary captions, muted helper text, subdued icon strokes — the only mid-gray in the palette, used sparingly to fade metadata without going fully light [neutral]

## Typography

- **Onest**
- **Times**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption-lg | 12 | — | 1.2 |
| body-sm | 14 | — | 1.4 |
| body | 16 | — | 1.55 |
| subheading-sm | 20 | — | 1.21 |
| subheading | 23 | — | 1.18 |
| heading-sm | 32 | — | 1.08 |
| heading | 48 | — | 1.04 |
| heading-lg | 52 | — | 1 |
| display | 152 | — | 0.9 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 20px
- **Element Gap**: 10px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '30px', 'cards': '10px', 'images': '15px', 'inputs': '30px', 'avatars': '3000px', 'buttons': '600px'}

## Layout

Full-bleed page with a max-width 1280px content container. The hero is a full-viewport-width product photograph with a bottom-left display headline overlay and a white pill CTA. The email capture modal centers on a dimmed page (rgba black ~60%). Below the hero, sections flow in a vertical rhythm with 80px section gaps: a product grid (3-column on desktop, orange-bordered cards), a stat callout (98%) sitting in generous whitespace, and a trust-signal row (icons + labels) anchoring the fold. Navigation is a single sticky white header; the announcement bar is a fixed dark strip above it. Asymmetric compositions dominate — large left-aligned text blocks, right-anchored floating annotations, never centered content outside the modal.

## Surfaces / Elevation

- **Canvas**
- **Card White**
- **Orange Surface**
- **Dark Surface**

## Imagery

Photography dominates the visual language: warm-toned, editorial beauty product shots — close crops of face mask containers, orange-tinted product packaging, and lifestyle skin imagery. Hero and product backgrounds are full-bleed with a slight darkening overlay to support white text. The 152px display type sits directly on top of photography without a scrim, relying on the photo's own contrast. Icons are exclusively 1.5-2px line-art in Graphite Black, monoline, geometric (leaf, rabbit, heart, search, user, cart). No illustrations, no 3D renders, no decorative graphics — the product photography is the brand's only visual storytelling medium.

## Design Principles

### Do

- Set all display sizes (48px and above) in Onest weight 200-300 — the whisper-weight headline is the brand's editorial signature
- Use letter-spacing in negative em values across the entire type scale, tightening to -0.091em at 152px display
- Reserve Ember Orange (#f15730) for filled buttons and Tangerine Blaze (#f7651a) for entire promotional surfaces; never mix them in the same component
- Use Apricot Whisper (#ff8562) for 1-2px hairline borders on cards and link underlines — not for fills
- Apply 600px border-radius to every button and 30px to every input — the pill is non-negotiable for actions
- Default card corners to 10px and product image corners to 15px
- Use Mist Gray (#eeeeee) for borders only on white surfaces where Graphite would feel too heavy

### Don't

- Don't apply box-shadows to cards, buttons, or modals — the system communicates depth with borders and color alone
- Don't use Orange for body text — its contrast on white fails accessibility, keep it for fills, borders, and large display numbers only
- Don't use weights 600-800 for body text or UI labels — reserve them for the rare emphasis moment
- Don't introduce a second accent color or hue — the orange must remain the single chromatic note
- Don't use 0px or 4px border-radius on cards or images — the 10px/15px minimum is part of the soft editorial feel
- Don't center product card text — left-align all UI copy; centering is reserved for the hero overlay and modal content
- Don't apply gradients to surface fills — the only observed gradient is a single progress-bar indicator on a dark surface

## Components

### Top Announcement Bar

Full-bleed, ~32px tall, background #111111, text #ffffff at 11px Onest weight 400 centered. Anchors the page with a dark cap.

### Main Navigation

White background, ~64px tall, logo in Onest 600 uppercase letterspacing-tight left, nav links in Onest 400 14px Inkwell (#0d1717) with 24px horizontal gaps, utility icons right with 20px gaps. No background tint, no shadow — separates from page by proximity alone.

### Hero Overlay Section

Background: full-width product lifestyle photo (face mask containers, warm tones). Overlay text bottom-left: 'brand of modern and innovative cosmetics' in Onest 200 at 52px Inkwell, with line-height 1.00 and letter-spacing -2.91px. CTA: white pill button (600px radius), 15px vertical / 40px horizontal padding, Onest 500 14px Graphite. Right side carries small floating UI annotations at Smoke gray ('Percentage of natural ingredients 98%').

### Pill CTA Button (Primary)

Background Ember Orange (#f15730), text #ffffff, border-radius 600px (fully pill), padding 15px 40px, Onest 500 14px. No border. On hover, shifts to Tangerine Blaze (#f7651a).

### Pill CTA Button (Ghost/White)

Background #ffffff, text Graphite Black (#111111), border-radius 600px, padding 15px 40px, Onest 500 14px. Reads as the inverted version of the primary pill.

### Pill Button (On Orange Modal)

Background #ffffff, text Ember Orange (#f15730), border-radius 600px, padding 15px 48px, Onest 500 16px. The white-on-orange inversion makes the submit action pop against the Tangerine Blaze modal fill.

### Email Capture Modal

Tangerine Blaze (#f7651a) background, 10px border-radius, ~480px wide, centered on a dimmed page. Header: small heart icon + 'skincare community' in Onest 300 italic at 32px #ffffff. Body text: Onest 400 16px #ffffff. Email input: transparent fill with 2px #ffffff border, 30px radius, padding 13px 20px, white placeholder text. Submit: white pill (see above). Close X: top-right, 2px #ffffff stroke.

### Outlined Product Card

Background #ffffff, border 1.5px Apricot Whisper (#ff8562), border-radius 10px, padding 20px. Product image fills card width with 0px internal margin. Title below image in Onest 500 16px Inkwell. Price/CTA in Onest 400 14px Graphite. The orange border is the card's only accent — no shadow, no fill.

### Stat Callout Block

Number in Onest 200 at 152px Graphite Black with line-height 0.90 and letter-spacing -13.83px — the type scale's largest size, creating a single-character-wide visual punch. Label in Onest 400 14px Smoke (#818181), sitting tight beneath the number. No background fill, no border.

### Feature Row

Inline row, no card. Each item: 20px line-art icon in Graphite Black + 10px gap + label in Onest 400 14px Graphite. Items separated by 40px horizontal space. No background, no border, sits flush against the section baseline.

### Close Button (Modal X)

2px stroke #ffffff line forming an X, ~20px square, positioned absolute top-right of the modal with 16px margin. No background, no border, no radius.

### Navigation Icon Button

No background, 1.5px Graphite Black line-art icon at ~20px, optional circular badge count in Tangerine Blaze with #ffffff text at 9px. Icons sit 20px apart.

## Similar Design Systems

- {'why': 'Same light-cosmetics palette with a single warm pink-coral accent and large editorial display type on white', 'business': 'Glossier'}
- {'why': 'Whisper-weight serif-adjacent sans serif, near-black text on warm white, product-photography-forward layout with zero shadows', 'business': 'Aesop'}
- {'why': 'Editorial fashion-cosmetics crossover with extreme display type sizes and pill-shaped CTAs', 'business': 'By Far'}
- {'why': 'Minimal skincare product card grid with hairline colored borders and monochrome typography', 'business': 'Cult51'}
- {'why': 'Bold color-blocked promotional modals interrupting an otherwise white editorial product layout', 'business': 'Milk Makeup'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #111111 (body) / #0d1717 (headings)
- background: #ffffff
- border: #111111 (structural) / #ff8562 (accent hairlines)
- accent: #ff8562 (borders, icons, links)
- primary action: #f15730 (filled action)
- promotional surface: #f7651a (modals, featured blocks)

**Example Component Prompts**

1. Create a Primary Action Button: #f15730 background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Email capture modal**: Centered on dimmed page. Background #f7651a, 10px radius, ~480px wide. Header heart icon (2px #ffffff stroke) + 'skincare community' in Onest 300 italic 32px #ffffff. Body copy Onest 400 16px #ffffff. Email input: transparent, 2px #ffffff border, 30px radius, 13px 20px padding. Submit button: background #ffffff, text #f15730, 600px radius, 15px 48px padding, Onest 500 16px. Close X top-right: 2px #ffffff lines.

3. **Product card**: Background #ffffff, border 1.5px #ff8562, 10px radius, 20px padding. Product image fills card width. Title below in Onest 500 16px #0d1717. No shadow.

4. **Stat callout**: '98%' in Onest 200 at 152px #111111, line-height 0.90, letter-spacing -13.83px. Label 'Percentage of natural ingredients' in Onest 400 14px #818181 directly beneath. No background, no border.

5. **Trust signal row**: Horizontal inline list. Each item: 20px line-art icon in #111111 + 10px gap + label in Onest 400 14px #111111. 40px gap between items. No background fill.

## Type Signature

The combination of Onest weight 200 at 152px with -0.091em letter-spacing is the single most identifiable element of the visual system. This pairing produces a display headline so thin and so tightly tracked that the letters nearly touch at their widest stems — it reads as engraved rather than printed. Any new page should feature at least one instance of this display treatment; without it, the system loses its editorial identity. Body text (14-16px) uses weight 400-500 with far less aggressive tracking (-0.019em to -0.022em), keeping long passages legible.

## Border System

Three border weights and three border colors, no exceptions: 1.5px (product cards, icon strokes) in Apricot Whisper #ff8562; 1px (structural dividers, card edges on white) in Graphite #111111; 2px (modal inputs, close X, on-image annotations) in white #ffffff or current accent. Borders carry all the structural information — there are no shadows, no colored fills behind borders, and no borderless filled regions outside the orange promotional surfaces.
