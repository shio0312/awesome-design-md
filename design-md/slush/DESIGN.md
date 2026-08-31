# Slush — Design System

> **North Star**: inflatable sticker universe on pastel paper
> **Theme**: light
> **Source**: https://slush.app
> **Refero Style**: https://styles.refero.design/style/8b6b547f-a357-4f1b-9842-4579c62dd42b
> **Synced**: 2026-09-01

## Overview

Slush runs on a sticker-book logic: pastel paper canvas, huge inflated 3D ribbons in electric blue, and a full rainbow of vivid sticker accents scattered like confetti. Display type is enormous and crushed (Lateral 800 at 200–640px, line-height 0.75–0.80) so the words become sculptural objects, not sentences. The six saturated brand colors function as a shared sticker palette — every color appears as a filled sticker, a card surface, or a decorative wash, never as a restrained accent. Components are rounded to the point of softness (20–40px on cards, pill-shaped on nav) and outlined in black for a hand-cut feel. The result reads less like a fintech landing page and more like a physical collage pinned to a pale wall.

## Color Palette

- **Carbon**: `#000000` — Primary text, card borders, filled CTA background, logo mark — creates the hand-cut sticker outline effect against pastel surfaces [neutral]
- **Paper White**: `#ffffff` — Page canvas, card surfaces, outlined button fills, text on dark fills [neutral]
- **Sky Wash**: `#dceeff` — Hero section background, light blue pastel ground [neutral]
- **Concrete Gray**: `#cccccc` — Secondary section background, neutral interlude surface [neutral]
- **Soft Mist**: `#e9e9e9` — Subtle button and surface tints, disabled states [neutral]
- **Electric Blue**: `#4da2ff` — Dominant brand color — 3D ribbon sculptures, body backgrounds, card washes, the visual signature that anchors every screen [brand]
- **Mint Pop**: `#55db9c` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content [accent]
- **Lavender**: `#e9ccff` — Soft accent wash for cards, tags, sticker fills — the gentlest color in the palette [accent]
- **Ember**: `#fb4903` — Hot accent for sticker icons, badge fills, rocket body — warmest hit in the rainbow [accent]
- **Sunburst**: `#ffd731` — Sticker coin fills, highlight accents, yellow sticker decorations — never used for text backgrounds [accent]
- **Voltage Violet**: `#5c4ade` — Deep accent for wallet stickers, QR download cards, secondary CTAs — the anchor purple in the sticker set [accent]

## Typography

- **Lateral**
- **Aeonik Pro**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.56 |
| body-lg | 15 | — | 1.39 |
| subheading | 24 | — | 1.2 |
| heading-sm | 30 | — | 1.1 |
| heading | 64 | — | 1 |
| display | 200 | — | 0.8 |
| display-lg | 640 | — | 0.75 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 24px
- **Element Gap**: 4-12px
- **Section Gap**: 48px
- **Border Radius**: {'nav': '1600px', 'body': '30px', 'cards': '20px', 'pills': '1600px', 'buttons': '1600px', 'wallet-icon': '16px', 'cards-elevated': '40px'}

## Layout

Full-bleed scroll-based layout with no sidebar or persistent container. The marquee banner and a minimal top nav (logo left, pill nav center, filled CTA right) persist at the top. Each section is a full-viewport color band (#dceeff → #ffffff → #cccccc) with oversized Lateral display text centered or left-aligned, wrapped by 3D blue ribbons. Content arrangement is deliberately loose and collage-like rather than grid-locked: stickers overlap display type, ribbons cross behind text, and the QR card sits off-center in the secondary section. Vertical rhythm is generous (48px section gaps) but horizontal composition is intentionally asymmetric. The page reads top-to-bottom as three large color bands, each a self-contained poster.

## Surfaces / Elevation

- **Sky Wash**
- **Paper White**
- **Concrete Gray**
- **Sticker Surfaces**

## Imagery

The visual language is dominated by 3D-rendered blue ribbons — a single signature motif that appears as a grainy, inflatable tubular form in Electric Blue (#4da2ff), wrapping around or behind display text in every section. Decorative 2D stickers (rocket, gold coin, green checkmark, purple wallet) float around headlines like physical cut-outs pinned to a board, each with a 1px black outline. No photography appears anywhere. No traditional illustration grids — everything is collage-like and asymmetrically placed. The 3D ribbons do the heavy atmospheric lifting; stickers add playfulness; the rest is type and color.

## Design Principles

### Do

- Use Lateral 800 at 200–640px with line-height 0.75–0.80 for any display headline; the crushed leading is non-negotiable for the sculptural text effect.
- Apply the six-color sticker palette (Electric Blue, Mint Pop, Lavender, Ember, Sunburst, Voltage Violet) as a shared set — use multiple colors per screen, never pick one as 'the' accent.
- Set all interactive elements (nav, buttons, cards) to 1px solid #000000 borders; the hand-cut outline is part of the visual language, not a fallback.
- Round nav, buttons, and tags to 1600px (pill shape) and cards to 20–40px; softness is the system default.
- Pair every display headline with a 3D blue ribbon or sticker cluster — display type never appears alone on a flat background.
- Use Aeonik Pro 700 with 0.030–0.032em letter-spacing for all nav, button, and uppercase label text to give pill controls breathing room.
- Alternate section backgrounds across #dceeff, #ffffff, and #cccccc to create visible scroll rhythm without dividers or shadows.

### Don't

- Do not use any border-radius under 16px for cards or under 1600px for buttons/tags; sharp corners break the soft sticker-book feel.
- Do not set line-height above 0.85 on Lateral display text — the crushed leading is what makes the type sculptural rather than typographic.
- Do not use blue (#4da2ff) as a CTA fill or link color; it is a decorative/brand surface color, not an action color. CTAs are black-fill or outlined-black only.
- Do not add box-shadows to cards, buttons, or surfaces; elevation is communicated through color bands and black outlines, never shadows.
- Do not use green (#55db9c) as a success state color — it is a sticker accent, not a semantic state. Reserve it for decorative/checkmark stickers.
- Do not constrain the page to a max-width under 1280px; the inflated display type and 3D ribbons need horizontal room to breathe.
- Do not use gradients anywhere; the 3D ribbons carry all dimensional weight, and flat color fills preserve the sticker/paper aesthetic.

## Components

### Pill Nav Button

1600px border-radius, 1px solid #000000 border, #ffffff fill, Aeonik Pro 700 at 12–14px with 0.032em letter-spacing, 15px vertical padding, 12px horizontal padding. Sits inline in the nav bar with 4px gaps.

### Filled CTA Button

40px border-radius, #000000 background, #ffffff text, Aeonik Pro 700 at 13–14px, 10px vertical and 12px horizontal padding, 1px solid #000000 border (invisible against fill). Used for the single highest-priority action per screen.

### Outlined Ghost Button

1600px border-radius, 1px solid #000000 border, #ffffff background, #000000 text, Aeonik Pro 700 at 13–14px with 0.032em letter-spacing, 10px vertical and 12px horizontal padding. Pairs beside or below the filled CTA.

### Logo Mark

Circular black-outlined 'S' badge, 1600px radius, 1px #000000 border on #ffffff fill. Sits top-left at fixed position across all sections.

### Plus Menu Button

Circular icon button, 1600px radius, 1px #000000 border, #ffffff fill, contains a + glyph in Aeonik Pro 700.

### QR Download Card

20px border-radius card, #5c4ade background, split into QR code panel (white) and label panel (#5c4ade with white Aeonik Pro 700 'DOWNLOAD' text). Black hairline border on the QR panel.

### Sticker Decoration

Flat illustrated stickers (rocket, coin, wallet, checkmark) with 1px #000000 outline, 16–20px radius, filled with one of the six brand colors. Positioned as overlapping, rotated decorative elements around display type — never grid-aligned.

### Marquee Banner

Full-bleed horizontal band at page top, #000000 background, #ffffff Aeonik Pro 700 uppercase text at 12–13px with 0.032em letter-spacing, repeating message. Separates from the page edge with no padding.

### Display Headline Block

Lateral 800 at 200–640px, line-height 0.75–0.80, #000000 fill. Treated as a physical object that the 3D blue ribbon wraps behind. Always paired with a smaller Aeonik Pro tagline below.

### Tagline Subhead

Aeonik Pro 500 at 24–64px, #000000, sits centered or left-aligned directly below the Lateral display block. The size step (24–64px) keeps it readable without competing with the display.

### 3D Ribbon Element

Rendered 3D blue (#4da2ff) tubular form with a rough/grainy surface texture, full-bleed, wrapping behind display text. Functions as a brand symbol more than decoration — appears in every section.

### Section Background Panel

Alternates between #dceeff (light blue), #ffffff (white), and #cccccc (gray) across scroll. No border or shadow — sections are defined purely by color bands.

## Similar Design Systems

- {'why': 'Same sticker-on-pastel approach with a multi-color accent palette and rounded pill buttons, though Rainbow leans darker', 'business': 'Rainbow.me'}
- {'why': 'Similar pastel hero with oversized display type and decorative 3D elements wrapping behind text', 'business': 'Phantom Wallet'}
- {'why': 'Shared vivid multi-color sticker palette, rounded card surfaces, and playful 3D decorative elements on a light canvas', 'business': 'Backpack Wallet'}
- {'why': 'Same bold display typography with tight leading and full-bleed colored section bands, though Magic Eden uses more photography', 'business': 'Magic Eden'}

## Agent Prompt Guide

Quick Color Reference:
- text: #000000
- background: #ffffff / #dceeff / #cccccc (section-dependent)
- border: #000000 (1px outlines everywhere)
- accent: #4da2ff (3D ribbon blue — decorative only)
- sticker palette: #55db9c, #e9ccff, #fb4903, #ffd731, #5c4ade
- primary action: #ffffff (filled action)

Example Component Prompts:
1. Create a Primary Action Button: #ffffff background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Build a hero section: #dceeff full-bleed background. Centered Lateral 800 200px #000000 display headline with line-height 0.80. A 3D Electric Blue (#4da2ff) grainy tubular ribbon wrapping behind the text. Tagline below: Aeonik Pro 500 24px #000000, letter-spacing -0.01em. Two ghost buttons beneath: 'Launch Web App' and 'Download for Chrome' — both 1600px radius, 1px #000000 border, #ffffff fill, Aeonik Pro 700 13px 0.032em #000000 text, 10px/12px padding. Decorative stickers (rocket in Ember #fb4903, coin in Sunburst #ffd731, wallet in Voltage Violet #5c4ade) floating around the headline with 1px #000000 outlines, 20px radius, slight rotation.

3. Build a QR download card: 20px radius, #5c4ade background, 1px #000000 border. Split layout — left half is a #ffffff QR code square with 8px internal padding; right half shows 'DOWNLOAD' in Aeonik Pro 700 14px 0.032em #ffffff text centered vertically.

4. Build a marquee strip: #000000 full-bleed background, 1px top and bottom #000000 border. Scrolling Aeonik Pro 700 12px 0.032em #ffffff uppercase text repeating a promotional message. No padding inside — text sits flush to the band edges.

5. Build a secondary section: #cccccc full-bleed background. Asymmetric placement: Lateral 800 281px #000000 display text at 0.76 line-height on the left, with a 3D #4da2ff ribbon arcing across the top. A green checkmark sticker (#55db9c fill, 1px #000000 border, 20px radius) on the far left, and a purple wallet sticker (#5c4ade fill, 1px #000000 border, 16px radius) on the far right, both overlapping the display type.

## Gradient System

No gradients. The 3D ribbon elements carry all dimensional weight, and all flat surfaces (backgrounds, cards, buttons, stickers) use solid fills. This is a hard rule — gradients would undermine the sticker-on-paper aesthetic.

## Animation Philosophy

The marquee strip scrolls horizontally on a continuous loop. The 3D ribbons are static 3D renders, not animated. Sticker decorations are static. The site reads as a printed collage, not a kinetic experience — motion is restricted to the marquee and minimal hover transitions on buttons.
