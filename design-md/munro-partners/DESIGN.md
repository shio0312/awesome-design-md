# Munro Partners — Design System

> **North Star**: Editorial parchment under alpine light — a warm cream canvas holding generous whitespace, a whisper-weight grotesque, and full-bleed mountain photography where the landscape does the talking and the interface stays nearly invisible.
> **Theme**: light
> **Source**: https://www.munropartners.com.au
> **Refero Style**: https://styles.refero.design/style/d2e327b2-1181-4203-82a6-2dc15a72078a
> **Synced**: 2026-09-01

## Overview

Munro Partners operates in a quiet, editorial register: a warm cream canvas (#fff9ee) holds generous whitespace, with every interface element trimmed in a single warm dark brown (#3f322a) that reads as ink rather than black. The Neue Haas Grotesk typography is set tight and small, with a 68px display headline at weight 400 that whispers against full-bleed mountain photography rather than shouting. A single deep teal (#004e4e) is reserved for the most important interactive moments, while muted violets, aubergine, and ice blue appear as thin accent borders on cards and data treatments. The system feels less like a financial product and more like a printed annual report — calm, spacious, and confident enough to let landscape imagery carry the emotional weight.

## Color Palette

- **Cream Parchment**: `#fff9ee` — Page canvas, section backgrounds, card surfaces, nav bar fill — the warm off-white that defines the entire mood and replaces what would normally be pure white [neutral]
- **Paper White**: `#ffffff` — Elevated card surfaces, video embed containers, contrast panels against the cream canvas [neutral]
- **Bark Brown**: `#3f322a` — Primary text, all borders, nav links, body copy, headings — replaces black throughout the system, giving every line a warm ink-like quality [neutral]
- **Warm Gray**: `#9f968c` — Secondary text, subtle borders, nav dividers — the mid-tone that bridges Bark Brown headings and lighter dividers [neutral]
- **Stone**: `#c5bdb3` — Hairline dividers, image borders, subtle separators between sections [neutral]
- **Driftwood**: `#b3aea7` — Input field borders, form element outlines [neutral]
- **Earth**: `#796e65` — Secondary headings, muted label text [neutral]
- **Light Stone**: `#e5e5e5` — Lightest border tone, disabled states, subtle structure lines [neutral]
- **Ink**: `#000000` — Input text color, high-contrast form text — the only context where true black appears [neutral]
- **Deep Teal**: `#004e4e` — Primary action buttons, filled CTAs — the single chromatic fill color permitted for interactive moments, creating quiet authority against the cream [brand]
- **Aubergine**: `#560e4b` — Decorative card borders, heading accent strokes, editorial highlight containers [accent]
- **Iris**: `#a56eff` — Decorative card borders, accent strokes on data containers [accent]
- **Cobalt**: `#3074f9` — Link accents, decorative borders on blue-themed content blocks [accent]
- **Ice Blue**: `#bfebfe` — Input field backgrounds, soft highlight washes on data rows, subtle surface tint [accent]
- **Saffron**: `#feed5a` — Occasional button accent for editorial highlight CTAs [accent]
- **Amber**: `#c67700` — Occasional button accent for warm-themed CTAs [accent]

## Typography

- **Neue Haas Grotesk Display**
- **Neue Haas Grotesk Text**
- **Font Awesome 5 Brands**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.8 |
| body | 14 | — | 1.43 |
| heading-sm | 22 | — | 1.2 |
| heading | 30 | — | 1.13 |
| heading-lg | 43 | — | 1.09 |
| display | 68 | — | 1.05 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 20px
- **Element Gap**: 20px
- **Section Gap**: 64px
- **Border Radius**: {'cards': '2px', 'links': '15px', 'badges': '2px', 'images': '15px', 'inputs': '2px', 'buttons': '2px'}

## Layout

Full-bleed hero photography at the top of the page, then a transition to a max-width 1280px centered content area on Cream Parchment. The hero is a full-viewport-width image with overlaid text at bottom-left and a large vertical wordmark at the right edge. Below the hero, content flows in a single editorial column or a two-column split (video left, data table right) with generous vertical spacing (64px between sections). Section rhythm is consistent: hairline divider, then a section label in small-caps, then content. No alternating dark/light bands — the entire body is cream. Navigation is a minimal slim bar at the top with hamburger menu left and wordmark right. Grid usage is minimal — mostly single-column editorial flow with occasional 2-column splits. The overall density is spacious, magazine-like, and unhurried.

## Surfaces / Elevation

- **Cream Parchment**
- **Paper White**
- **Ice Blue Wash**

## Imagery

Full-bleed landscape photography dominates the visual language — Scottish Highland mountains, winding single-lane roads through green valleys, open terrain under overcast skies. Treatment is naturalistic, high-resolution, and unfiltered; no duotone, no color grading overlays, no vignettes. Images are always full-bleed (no rounded corners when used as heroes) but use 15px radius when inset as content images. Photography is the primary visual content; illustration and abstract graphics are absent. Icon style is minimal line icons (hamburger menu visible in nav) with thin strokes. Density is image-heavy at section openings, text-dominant in body sections. The imagery role is emotional atmosphere and brand storytelling — nature as metaphor for long-term investing.

## Design Principles

### Do

- Set body text in Neue Haas Grotesk Display 14px/1.43 in Bark Brown (#3f322a) on Cream Parchment (#fff9ee) — never invert this pairing
- Use 2px border-radius for all buttons, badges, inputs, and accent-border cards — the near-square edge is a signature
- Use 15px border-radius exclusively for image containers and decorative links
- Reserve Deep Teal (#004e4e) for the single primary action per view — filled buttons in any other chromatic color are forbidden
- Set display headlines at 68px weight 400 with letter-spacing 0.54px — the whisper-weight is the defining typographic choice
- Separate content blocks with 1px Stone (#c5bdb3) hairlines, not card containers or background fills
- Use full-bleed landscape photography as section heroes with white text overlays — let imagery carry emotional weight
- Set section labels in 12px weight 700 uppercase with letter-spacing 0.017em — the casing and weight do the hierarchy work

### Don't

- Never use #000000 for body text, headings, or borders — Bark Brown (#3f322a) replaces black throughout the system
- Never use pure white (#ffffff) as the page canvas — Cream Parchment (#fff9ee) is the only acceptable base
- Never use border-radius greater than 2px on buttons, badges, or inputs — large radii break the editorial register
- Never stack multiple chromatic accent colors within a single component — one accent per container
- Never use weight 700 for editorial body copy or long-form text — reserve 700 for labels and wordmarks
- Never apply box-shadows or drop-shadows to cards or surfaces — the system is flat, separated only by hairlines
- Never use gradients of any kind — the system is entirely flat color
- Never use #feed5a or #c67700 for primary CTAs — these are one-off editorial accents, not system action colors
- Never set body text larger than 16px or smaller than 14px — the editorial scale stays tight

## Components

### Full-Bleed Hero Image

Full-bleed landscape photograph (mountains, winding roads, open terrain) spanning 100% viewport width and 60–80vh height. No border-radius. Text overlay sits at bottom-left in white (#ffffff) using display weight 400 at 68px. A large vertical wordmark in white at 100–200px weight 700 anchors the right edge.

### Editorial Wordmark

The text 'MUNRO' set in Neue Haas Grotesk Display weight 700, all uppercase, letter-spacing 0.09em. Functions as nav logo at 16px (top-right) and as oversized decorative element at 100–200px (right edge of hero). White on dark photography, Bark Brown (#3f322a) on cream.

### Slim Navigation Bar

Full-width bar on Cream Parchment (#fff9ee) background, 48–56px height. Left: hamburger menu icon + 'MENU' label in Neue Haas Grotesk Text 12px weight 500, letter-spacing 0.018em, color Bark Brown. Right: 'MUNRO' wordmark. No background fill change on scroll, no shadow — the bar is flat and barely visible.

### Filled Teal CTA Button

Background Deep Teal (#004e4e), text white, Neue Haas Grotesk Display 12px weight 600, letter-spacing 0.018em, uppercase. Padding 10px vertical, 20px horizontal. Border-radius 2px. No shadow. This is the system sole filled action color — use it for exactly one primary action per view.

### Ghost Text Button

No background, no border. Text only in Bark Brown (#3f322a), Neue Haas Grotesk Display 12px weight 600, uppercase, letter-spacing 0.018em. Padding 10px vertical, 12px horizontal. Underline on hover.

### Section Label

Neue Haas Grotesk Display 12px weight 700, uppercase, letter-spacing 0.017em, color Bark Brown (#3f322a). No accent line or decorative element — the typography weight and casing does all the work. Examples: 'OUR GLOBAL GROWTH FUNDS'.

### Display Headline

Neue Haas Grotesk Display 68px weight 400, line-height 1.05, letter-spacing 0.54px. White when overlaid on photography, Bark Brown (#3f322a) on cream. The weight-400 choice is the signature — it whispers rather than shouts, creating authority through restraint.

### Video Embed Card

16:9 aspect ratio container with Paper White (#ffffff) background, 2px border-radius. Video thumbnail fills the container. Title overlaid top-left in white Neue Haas Grotesk Display 22px weight 400 with a subtitle at 12px. Play button centered.

### Financial Data Table

Full-width rows separated by 1px Stone (#c5bdb3) hairline borders. Left column: label in Neue Haas Grotesk Display 14px weight 400, color Earth (#796e65). Right column: value in same size, color Bark Brown (#3f322a), right-aligned. No table header, no alternating row colors — pure hairlines and typography do the work.

### Editorial Body Paragraph

Neue Haas Grotesk Display 16px weight 400, line-height 1.41, color Bark Brown (#3f322a) on Cream Parchment (#fff9ee). Max-width 680px for readability. Generous margin-bottom (24–32px) between paragraphs.

### Underlined Input Field

No visible box, no background fill. Bottom border 1px in Ink (#000000) or Driftwood (#b3aea7). Placeholder text in Warm Gray (#9f968c) at 14px. On focus: bottom border thickens to 2px in Deep Teal (#004e4e). No border-radius — sharp bottom edge only.

### Accent Border Card

Cream Parchment (#fff9ee) background, 1px border in a chromatic accent (Aubergine #560e4b, Iris #a56eff, Cobalt #3074f9, or Ice Blue #bfebfe). Border-radius 2px. Padding 20px. No shadow, no fill change. The colored border is the differentiator — multiple cards on a page may use different accent colors.

### Hairline Divider

1px horizontal line in Stone (#c5bdb3), full container width, 1px height. No margin — sits flush within section spacing rhythm.

### Image Container

Images sit in containers with 15px border-radius. No border. Full-bleed within container. Used for editorial photography, team portraits, and landscape shots.

## Similar Design Systems

- {'why': 'Same warm cream canvas and restrained editorial typography approach to investment management branding', 'business': 'Stewart Investors'}
- {'why': 'Same full-bleed landscape photography + whisper-weight grotesque headline pattern, treating investing as a long journey', 'business': 'Orbis'}
- {'why': 'Same cream parchment background, minimal chrome, and editorial restraint in financial communications', 'business': 'Walter Scott Investment Partners'}
- {'why': 'Same warm off-white palette and premium grotesque typography in Australian investment management context', 'business': 'First Sentier Investors'}
- {'why': 'Same editorial publication feel with landscape photography and generous whitespace as brand differentiator', 'business': 'Magellan Asset Management'}

## Agent Prompt Guide

**Quick Color Reference**
- Text: #3f322a (Bark Brown)
- Background: #fff9ee (Cream Parchment)
- Border: #c5bdb3 (Stone) for hairlines, #3f322a for structure
- Accent: #004e4e (Deep Teal) for primary action
- primary action: #a56eff (filled action)

**Example Component Prompts**

1. **Hero section**: Full-bleed landscape photograph filling 100vw × 70vh. Headline 'Invest in the journey' overlaid bottom-left in white, Neue Haas Grotesk Display 68px weight 400, letter-spacing 0.54px. Vertical 'MUNRO' wordmark on right edge in white, weight 700, 120px size, letter-spacing 0.09em. No border-radius on the image.

2. **Section label + body**: Section label 'OUR GLOBAL GROWTH FUNDS' in Neue Haas Grotesk Display 12px weight 700, uppercase, letter-spacing 0.017em, color #3f322a. Below it, body paragraph in 16px weight 400, line-height 1.41, color #3f322a, max-width 680px. 1px #c5bdb3 hairline divider above the label.

3. **Data table**: Stacked rows, each separated by 1px #c5bdb3 border. Left column label in 14px weight 400, color #796e65. Right column value in 14px weight 400, color #3f322a, right-aligned. No header row, no alternating fills.

4. Create a Primary Action Button: #a56eff background, #3f322a text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

5. **Accent border card**: Background #fff9ee, 1px border in #560e4b (Aubergine), border-radius 2px, padding 20px. Content inside in 14px weight 400, color #3f322a. No fill change, no shadow.

## Elevation Philosophy

This system intentionally avoids shadows as a design principle. All surface separation is achieved through three mechanisms: (1) hairline 1px borders in Stone (#c5bdb3) or Bark Brown (#3f322a), (2) contrast between Cream Parchment (#fff9ee) and Paper White (#ffffff) surfaces, and (3) the visual edge where full-bleed photography meets the cream canvas. Never apply box-shadow, drop-shadow, or any blur-based elevation — it would break the flat editorial register.

## Border-Radius System

The system uses exactly two border-radius values to create a deliberate tension: 2px for all interactive and structural elements (buttons, badges, inputs, accent-border cards) — this near-square edge reads as editorial, typeset, printed. 15px for all image containers and decorative links — this generous rounding softens photography and gives visual assets warmth. Never mix these radii on the same element type. The contrast between the two is part of the identity: the page feels both sharply editorial and warmly human.
