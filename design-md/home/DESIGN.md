# Home — Design System

> **North Star**: editorial broadsheet in a green room
> **Theme**: light
> **Source**: https://www.newformcap.com
> **Refero Style**: https://styles.refero.design/style/1a519123-071a-449f-b5df-0def73ed7f35
> **Synced**: 2026-09-01

## Overview

New Form reads like a printed financial broadsheet reimagined for the web: monumental serif and grotesque headlines dominate the page, small-caps micro-labels run the navigation, and a single saturated neon green acts as a highlighter pen over an otherwise monochrome canvas. The page is overwhelmingly typographic — photographs are treated as grayscale, duotone-tinted rectangular inserts that interrupt the text flow rather than float above it. The layout is spacious and almost editorial-magazine in its rhythm: oversized display type, generous breathing room, and a footer that flips to near-black with green band accents. Buttons are pill-soft with green-tinted shadows; the rest of the UI stays stripped back to type and hairline structure.

## Color Palette

- **Bone White**: `#fafffa` — Page canvas, card surfaces, primary text on dark sections — a warm-tinted near-white that keeps the page reading like paper rather than screen [neutral]
- **Press Black**: `#121613` — Primary headline color, footer background, dominant surface — near-true black with a faint green-cool bias that ties it to the accent [neutral]
- **Typesetter Ink**: `#000000` — Primary headings, body text, and icon fills on light surfaces. Do not promote it to the primary CTA color [neutral]
- **Slate Verdant**: `#232924` — Secondary surface, bordered sections, muted dark accent — sits between Press Black and the white canvas [neutral]
- **Newsprint Gray**: `#516254` — Muted captions, helper text, and de-emphasized UI labels. [neutral]
- **Muted Sage**: `#c8d2c8` — Light text on dark surfaces, inverse labels, and high-contrast captions. [neutral]
- **Highlighter Green**: `#2bee4b` — Primary action fill, active nav underline, and full-bleed footer band — the single vivid accent, used like a marker swipe over the monochrome page [brand]
- **Shadow Moss**: `#93b799` — Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [accent]
- **Echo Green**: `#c4e4c9` — Gray supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [accent]

## Typography

- **TWK Lausanne**
- **PP Mondwest**
- **Editorial New**
- **Times**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.1 |
| body-sm | 14 | — | 1.1 |
| body | 18 | — | 1 |
| subheading | 60 | — | 0.9 |
| heading-sm | 72 | — | 1 |
| heading | 96 | — | 1 |
| heading-lg | 155 | — | 1 |
| display | 295 | — | 0.9 |

## Spacing & Layout

- **Max Width**: 1400px
- **Card Padding**: 0px
- **Element Gap**: 20px
- **Section Gap**: 80px
- **Border Radius**: {'pills': '10px', 'round': '9999px', 'images': '14px', 'buttons': '5px'}

## Layout

Full-bleed editorial canvas capped at ~1400px content width. The hero is a typographic wall: oversized Mondwest/Editorial New headline (165–295px) with small grayscale photo tiles floated between the lines. Navigation is a minimal top bar — wordmark left, 'Menu' with a green three-bar icon right. Below the hero, content alternates between wide Bone White sections with 80px vertical breathing room and a near-black (#121613) editorial block containing ghost-outline buttons. A category grid uses 3–4 columns with muted sage tags and stat callouts in Newsprint Gray. The page closes with a dark footer followed by a full-bleed #2bee4b accent band. Section gaps are generous (80px), element gaps sit at 20px, and the page reads vertically like a printed broadsheet rather than a SaaS dashboard.

## Surfaces / Elevation

- **Canvas**
- **Dark Section**
- **Accent Band**

## Imagery

All photography is grayscale processed through a filter chain (grayscale → invert 0.27 → sepia 0.07 → saturate 10.67 → hue-rotate 80deg) that tints shadows toward the brand green. Images are cropped as small rectangular tiles (roughly 200×140px), radius 14px, placed inline between lines of display type rather than in grid cells. No full-bleed hero image, no overlapping media, no lifestyle photography — every image is a documentary-style editorial insert (architecture, people in financial contexts) that interrupts the typographic flow. Icons are minimal stroke marks in #000000 or #fafffa, no multicolor iconography.

## Design Principles

### Do

- Set the hero headline in PP Mondwest 400 at 165–295px with lineHeight 0.9 and letterSpacing -0.04em — the tight tracking is what makes the type read as printed ink
- Use #2bee4b fill + #93b799 green-tinted shadow for the primary action; never use a gray drop shadow on the accent button
- Apply the grayscale + hue-rotate(80deg) filter to every photographic asset so all images read as the same tonal family as the page
- Keep the canvas at #fafffa (warm bone white) — do not use pure #ffffff, the warm tint is what separates this from a standard SaaS surface
- Use TWK Lausanne 11px / 550 uppercase with +0.01em tracking for every micro-label, nav item, and button — micro-typography does the work of chrome here
- Float editorial photo tiles (radius 14px) inline between display-type lines rather than in a grid, mirroring print layout
- Anchor every page with the full-bleed #2bee4b band before the footer; it functions as the closing signature

### Don't

- Do not introduce a second saturated accent color — green is the only chromatic note on an otherwise monochrome page
- Do not use rounded pill shapes (9999px) on the primary action button; 5px keeps it sharp and rectangular, matching the editorial tone
- Do not set body copy larger than 18px — the design relies on the size gap between 18px body and 96px+ display to create rhythm
- Do not use box-shadow on cards or content blocks; elevation lives only on the green button
- Do not render photographs in full color — they must pass through the grayscale-to-green filter to belong to the system
- Do not use sans-serif for display headlines; the Mondwest / Editorial New contrast is what gives the page its editorial voice
- Do not exceed a 1400px content width — the wide canvas with oversized type is what makes the page feel like a broadsheet

## Components

### Highlighter Green Action Button

Fill #2bee4b, label #000000 in TWK Lausanne 11px / 550 uppercase with +0.01em tracking. Padding 20px 30px, radius 5px. Outer shadow rgba(16,94,29,0.45) 1px 8px 20px 0 (green-tinted, not gray) so the elevation reads as the same green bleeding outward.

### Ghost Outline Button

Transparent fill, 1px border in #fafffa, label #fafffa in TWK Lausanne 11px / 550 uppercase. Radius 10px, padding 50px 20px — the tall vertical padding makes these read as full-height menu items rather than compact buttons.

### Underlined Text Link

No fill, no border, Times 16px / 400 with a 1px black or white underline that hugs the baseline. Underline thickness is the only structural treatment — links do not change weight or color.

### Editorial Photo Insert

Grayscale photographs (filter: grayscale(1) saturate(1) invert(0.27) sepia(0.07) saturate(10.67) hue-rotate(80deg) brightness(1.02) contrast(0.83)) cropped to small rectangular tiles, radius 14px, floating between lines of display type rather than in a grid.

### Stat Callout

Set in Newsprint Gray #516254 at display scale, no decoration — the muted color is what makes it read as editorial data rather than a hero number.

### Category Tag

Muted Sage #c8d2c8, TWK Lausanne 14px / 350, +0.01em tracking. No background, no border — just a tinted uppercase label.

### Navigation Wordmark

TWK Lausanne bold 'New Form' with a 2px Highlighter Green underline beneath 'New'. The underline is the entire logo treatment — no icon, no lockup frame.

### Full-Bleed Accent Band

Edge-to-edge #2bee4b fill, ~640px tall, used as a visual full stop between content and footer. Contains only the wordmark 'N' in white at the top-left.

### Dark Editorial Section

Background #121613, headline type in #fafffa at 96px / TWK Lausanne 550, body in #fafffa at 18px / 200. Ghost buttons replace filled ones on this surface.

### Footer

Background #121613, small-caps TWK Lausanne 11px / 550 in #fafffa for nav columns, 18px / 200 body for contact lines. Followed by the full-bleed Highlighter Green band that closes the page.

## Similar Design Systems

- {'why': 'Same generous white-canvas editorial typography at massive scale, with the brand voice carried by type weight rather than color', 'business': 'Stripe'}
- {'why': 'Same brutalist-meets-editorial approach: oversized mixed serif/grotesque display type, monochrome pages, a single vivid accent', 'business': 'Koto Studio'}
- {'why': 'Same investment-firm broadsheet language — typographic hero, small grayscale documentary inserts, near-black section breaks, no decorative chrome', 'business': 'Index Ventures'}
- {'why': 'Same single-accent-on-monochrome treatment with the accent functioning as a highlighter over otherwise black-and-white layouts', 'business': 'A24'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #121613 on light surfaces, #fafffa on dark surfaces
- background (canvas): #fafffa
- surface (dark section / footer): #121613
- border: #232924 or hairline #000000
- accent (footer band, active nav): #2bee4b
- primary action: #2bee4b (filled action)

**Example Component Prompts**
1. *Hero editorial headline block*: 1400px max-width centered on #fafffa canvas. Headline in PP Mondwest at 165px, weight 400, lineHeight 0.9, letterSpacing -6.6px, color #121613. Three grayscale photo tiles (radius 14px) floated inline between the lines, each passing through filter: grayscale(1) saturate(1) invert(0.27) sepia(0.07) saturate(10.67) hue-rotate(80deg) brightness(1.02) contrast(0.83).
2. *Highlighter Green action button*: Fill #2bee4b, label in TWK Lausanne 11px / 550 uppercase, letterSpacing +0.11px, color #000000. Padding 20px 30px, border-radius 5px, box-shadow rgba(16,94,29,0.45) 1px 8px 20px 0. Arrow icon in #000000 sits to the right of the label.
3. *Dark editorial section*: Full-width #121613 background, max-width content container 1400px. Headline at 96px TWK Lausanne 550, lineHeight 1.0, letterSpacing -1.92px, color #fafffa. Body copy 18px TWK Lausanne 200, lineHeight 1.0, letterSpacing -0.36px, color #fafffa. Ghost button: transparent fill, 1px solid #fafffa border, radius 10px, padding 50px 20px, label 11px uppercase #fafffa.
4. *Category tag row*: Muted Sage #c8d2c8 label, TWK Lausanne 14px / 350, letterSpacing +0.14px. No fill, no border, 20px gap between tags. Used above section headlines and in stat grids.
5. *Full-bleed accent band*: Edge-to-edge #2bee4b fill, 640px tall. Wordmark 'N' in TWK Lausanne bold #fafffa, positioned top-left with 50px padding. No additional content — the band is the closing signature.

## Typography Stacking

The system relies on three display faces playing off each other: PP Mondwest (serif, weight 400, tightest -0.04em) for the wordmark and biggest statements; Editorial New (lighter serif, weight 300) for italic-leaning editorial pull-quotes; TWK Lausanne (grotesque) for everything UI and for the 96–155px sub-display headlines that alternate with the serif. The contrast between Mondwest's heavy block and Lausanne's sharp sans at the same physical size is what makes the page feel like a printed spread rather than a single-voice website. Body and micro-labels stay in TWK Lausanne at 11–18px; the system Times fallback handles any rendered browser text.

## Image Treatment

Every photographic asset passes through the same filter chain: grayscale(1) saturate(1) invert(0.27) sepia(0.07) saturate(10.67) hue-rotate(80deg) brightness(1.02) contrast(0.83). The 80-degree hue rotation after a partial invert pushes the monochrome into the green family — blacks become deep green-blacks, whites become bone, midtones pick up a sage cast. This filter is applied at the asset level so it works on any uploaded image without per-asset color grading. Result: the entire site reads as a two-tone green duotone regardless of the original photograph's content.
