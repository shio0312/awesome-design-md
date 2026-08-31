# Monad — Design System

> **North Star**: editorial tech journal on warm parchment
> **Theme**: light
> **Source**: https://www.monad.com
> **Refero Style**: https://styles.refero.design/style/fc84e9f0-2058-4a0a-8d26-9cc1ba84ec9c
> **Synced**: 2026-09-01

## Overview

Monad renders its entire interface on a warm parchment canvas (#f6f3f1) that immediately separates it from the typical pure-white SaaS template. Headlines carry editorial weight in Untitled Serif at weight 400 — never bold — while every body, nav, and UI string runs in ABC Diatype Mono, giving the site the texture of a technical manual typeset for a literary magazine. A single vivid Lake Blue (#2b59d1) is the only chromatic accent for primary actions; everything else lives in a warm grayscale, so a periwinkle card surface (#cfdaf5) and soft pastel gradient washes (coral, sky, mint, gold) read as deliberate punctuation rather than noise. Components lean on hairline borders and 100px pill containers rather than shadows, and the rhythm stays calm and spacious with 40px card padding and generous vertical breathing room between sections.

## Color Palette

- **Parchment**: `#f6f3f1` — Page canvas and the majority of surface fills — this warm off-white IS the brand's signature surface, immediately distinguishing the site from pure-white SaaS templates [brand]
- **Lake Blue**: `#2b59d1` — Violet wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color [brand]
- **Periwinkle Mist**: `#cfdaf5` — Muted UI surface for disabled controls, low-emphasis panels, and placeholder blocks. [accent]
- **Sky Blue**: `#a0b5eb` — Decorative gradient stop — appears in atmospheric washes and the pipeline diagram's flow lines, never as a UI fill [accent]
- **Mint**: `#a7fccd` — Supporting palette color for small decorative accents when the core palette needs contrast. [accent]
- **Coral**: `#ff9473` — Supporting palette color for small decorative accents when the core palette needs contrast. [accent]
- **Gold**: `#ecda98` — Decorative gradient stop — warm accent in gradient washes, never used in functional UI [accent]
- **Crimson**: `#f37a0a` — Decorative gradient stop — deep warm tone in gradient washes alongside gold and coral [accent]
- **Off-Black**: `#242424` — High-contrast neutral action fill for primary buttons on light surfaces. [neutral]
- **Ink**: `#000000` — Announcement bar surface and certain heading fills — the black band at the top of the page and select heading contexts [neutral]
- **Graphite**: `#4e4d4d` — Secondary text — body copy and sub-headings that need less weight than primary headlines [neutral]
- **Smoke**: `#797776` — Muted helper text and tertiary links [neutral]
- **Ash**: `#cecac8` — Hairline borders — 1px solid lines separating sections, outlining pipeline diagram nodes, and defining card edges [neutral]

## Typography

- **ABC Diatype Mono**
- **Untitled Serif**
- **Untitled Sans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.2 |
| body-sm | 14 | — | 1.35 |
| body | 16 | — | 1.35 |
| label | 18 | — | 1.2 |
| body-lg | 20 | — | 1.35 |
| subheading | 24 | — | 1.2 |
| heading-sm | 32 | — | 1.2 |
| heading | 40 | — | 1.2 |
| heading-lg | 48 | — | 1.2 |
| display | 80 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 1432px
- **Card Padding**: 40px
- **Element Gap**: 16px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '9999px', 'cards': '40px', 'pills': '9999px', 'buttons': '100px'}

## Surfaces / Elevation

- **Parchment**
- **Periwinkle Mist**
- **Off-Black**
- **Ink**

**Shadow tokens:**

## Imagery

The visual language is dominated by a custom data pipeline diagram: pill-shaped bordered nodes connected by thin curved lines, with small icons inside each node representing data sources (Any Source, Cloud Logs, Vulnerabilities) and destinations (SIEM, Cloud Storage, Data Lake). The diagram uses a soft green radial glow at the center hub to suggest data normalization. Gradient atmospheric washes (Coral → Sky Blue, Sky Blue → Mint) with heavy blur filters create soft color halos behind hero and feature content. Partner logos appear desaturated in a single social-proof row. The 'In-flight Data Transforms' card features a large gradient illustration with overlapping translucent geometric shapes. No photography is used — the brand communicates through typography, diagram, and color wash alone.

## Design Principles

### Do

- Use Untitled Serif at weight 400 for all headings — never go bold; the serif's stroke contrast and -0.02em tracking carry the weight visually
- Use ABC Diatype Mono for all body copy, buttons, nav labels, badges, and functional UI text — the monospace IS the brand voice
- Set all button and tag border-radius to 100px or 9999px — pill shapes are the container language of this system
- Use Parchment (#f6f3f1) as the page canvas — never substitute pure white (#ffffff); the warm tint is signature
- Reserve Lake Blue (#2b59d1) exclusively for the single primary action per screen; all other buttons use Off-Black or ghost variants
- Use 1px solid Ash (#cecac8) for all borders and dividers — avoid thicker weights or darker border colors
- Apply uppercase + tight tracking to all nav labels, buttons, and tag text via the monospace family

### Don't

- Never set headings in bold or 600+ weight — Untitled Serif headlines stay at 400 across all sizes
- Never use pure white (#ffffff) as a page background — always use Parchment (#f6f3f1) to preserve the warm surface
- Never use Lake Blue (#2b59d1) for anything other than the single primary action fill — it loses meaning if scattered
- Never substitute a sans-serif for the monospace body font — the mono/serif pairing is the defining typographic gesture
- Never apply drop shadows to cards — use 1px Ash borders and surface color contrast (Parchment → Periwinkle) for elevation instead
- Never use corner radii below 16px on cards or below 100px on buttons — the system is pill-and-soft-rect, never sharp
- Never introduce additional accent colors for UI elements — the pastel palette (Sky, Mint, Coral, Gold) is decorative-only and belongs in illustrations and gradient washes

## Components

### Announcement Bar

Full-width black (#000000) bar, ~40px tall, containing mono text in white (#f6f3f1) at 14px and a small white pill button (9999px radius, white border, 12px uppercase text) anchored right. Close icon (×) in white at far right.

### Primary Pill Button (Blue)

Lake Blue (#2b59d1) fill, white text in ABC Diatype Mono at 14px uppercase, 100px border-radius, 16px 32px padding, with a trailing arrow (▸) glyph in white. Height ~48px. This is the only saturated fill in the system.

### Primary Pill Button (Black)

Off-Black (#242424) fill, white text in ABC Diatype Mono at 14px uppercase, 100px border-radius, 16px 32px padding, no arrow. Height ~48px.

### Ghost Pill Button

Transparent fill, 1px Off-Black (#242424) border, Off-Black text in ABC Diatype Mono at 14px uppercase, 100px border-radius, 16px 32px padding. Height ~48px.

### Text Link with Arrow

Transparent fill, Off-Black (#242424) text in ABC Diatype Mono at 14px, trailing rightward arrow (→) in Off-Black. No background or border. Uppercase tracking.

### Pipeline Node Tag

Parchment (#f6f3f1) fill, 1px Ash (#cecac8) border, 9999px border-radius (full pill), small mono icon (12px) + 14px mono uppercase text, 12px 20px padding. Connected by thin curved Ash lines to adjacent nodes.

### Feature Card

Transparent or Parchment fill, 1px Ash (#cecac8) border, 40px border-radius, 40px padding. Small mono icon (20px) in top-left at 16px padding offset. Title in Untitled Serif at 24px weight 400, Off-Black. Body in ABC Diatype Mono at 16px weight 400, Graphite (#4e4d4d). No shadow.

### Elevated Feature Card (Periwinkle)

Periwinkle Mist (#cfdaf5) fill, 40px border-radius, 40px padding. Contains a large gradient illustration on the right side using Coral → Sky Blue → Mint washes. Title in Untitled Serif 24px, body in mono 16px. This is the one card that uses a colored surface to draw the eye.

### FAQ Accordion Item

Full-width row, 40px vertical padding, 1px Ash (#cecac8) bottom border (no top border). Question text in Untitled Serif at 24px weight 400, Off-Black. Trailing chevron icon (↓) in Off-Black, 20px, right-aligned. No background fill change on hover.

### Logo Strip

Single horizontal row of 6-7 partner logos in grayscale (desaturated from original brand colors), evenly spaced with ~32px gaps, left-aligned within max-width container. No logo lockup borders or cards.

### Gradient Atmospheric Wash

Large blurred radial/linear gradient using Coral (#ff9473 80% opacity) → Sky Blue (#a0b5eb 80% opacity) or Sky Blue → Mint (#a7fccd), rendered with blur(50-75px) filter, positioned behind hero or feature content. Never sharp-edged, always softly diffused.

### Navigation Bar

Transparent or Parchment background, logo on far left (monad wordmark + circular dot mark), 4-5 nav text links centered or left-grouped in ABC Diatype Mono 18px uppercase Off-Black, action buttons (Login ghost + Get a Demo blue pill) right-aligned. ~80px height, no visible border.

### Hero Section

Full-width Parchment background, centered content stack: Untitled Serif headline at 80px weight 400 Off-Black, monospace subtext at 20px Graphite (#4e4d4d) at 1.35 line-height, two pill buttons centered below. No background image — pure typographic hero.

## Similar Design Systems

- {'why': "Shares the restrained monochrome palette and minimal-elevation card approach, though Monad's warm Parchment canvas and serif headlines set it apart from Linear's cooler white surface", 'business': 'Linear'}
- {'why': 'Both use custom editorial serif typefaces for headlines with tight letter-spacing and -0.02em tracking, treating the homepage as a typographic composition rather than a product screenshot', 'business': 'Stripe'}
- {'why': 'Shares the comfortable-density spacing, generous section gaps, and pill-shaped button language, though Monad adds the warm canvas and mono body twist', 'business': 'Vercel'}
- {'why': 'Both target developer audiences with a monospace-leaning UI vocabulary and minimal decoration, but Monad layers in the editorial serif for a more literary feel', 'business': 'Railway'}
- {'why': 'Both use warm off-white surfaces rather than pure white, and both treat the page as a designed editorial artifact rather than a typical SaaS template', 'business': 'Arc Browser'}

## Agent Prompt Guide

Quick Color Reference:
- text: #242424 (Off-Black)
- background: #f6f3f1 (Parchment)
- border: #cecac8 (Ash)
- accent: #2b59d1 (Lake Blue)
- primary action: no distinct CTA color

Example Component Prompts:

1. Create a hero section on Parchment (#f6f3f1) background. Centered headline in Untitled Serif at 80px weight 400, color #242424, letter-spacing -1.6px. Subtext below in ABC Diatype Mono at 20px weight 400, color #4e4d4d, line-height 1.35. Two centered pill buttons: primary Lake Blue (#2b59d1) with white text, and ghost (1px #242424 border, transparent fill, #242424 text), both 100px border-radius, 16px 32px padding, ABC Diatype Mono 14px uppercase.

2. Create a feature card on Parchment background. 1px solid #cecac8 border, 40px border-radius, 40px padding. Small 20px mono icon top-left at #242424. Title in Untitled Serif 24px weight 400, #242424. Body in ABC Diatype Mono 16px weight 400, #4e4d4d. No shadow.

3. Create a secondary pill button: Off-Black (#242424) fill, white text in ABC Diatype Mono 14px uppercase, 100px border-radius, 16px 32px padding, no arrow.

4. Create an FAQ accordion row: full-width, 40px vertical padding, 1px solid #cecac8 bottom border only. Question in Untitled Serif 24px weight 400, #242424. Trailing down-chevron icon (↓) in #242424 at 20px, right-aligned. No background fill.

5. Create a pipeline diagram node tag: Parchment (#f6f3f1) fill, 1px solid #cecac8 border, 9999px border-radius, 12px 20px padding. Small 12px icon + 14px text in ABC Diatype Mono uppercase, #242424.

## Typography Pairing Philosophy

The serif-mono pairing is the single most distinctive design choice in this system. Untitled Serif handles all hierarchical display text (headlines, section titles, feature card titles, FAQ questions) — it carries editorial authority through its stroke contrast and refined letterforms, not through weight (always 400). ABC Diatype Mono handles everything functional: body paragraphs, navigation, button labels, badges, tags, and inline UI text. This creates a consistent voice: the serif announces, the mono instructs. A page that swapped in a sans-serif for body would lose its identity immediately.
