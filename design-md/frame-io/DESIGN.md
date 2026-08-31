# Frame.io — Design System

> **North Star**: Midnight cinema projection room.

A dark suite where a single blue spotlight does all the work and the UI recedes so creative content can project forward.
> **Theme**: dark
> **Source**: https://frame.io
> **Refero Style**: https://styles.refero.design/style/30c3aa18-4323-4448-8ddd-3ca933fe5780
> **Synced**: 2026-09-01

## Overview

Frame.io is a midnight projection room for creative teams: a near-black canvas layered with deep cosmic gradients, where large confident display type floats above product surfaces like film titles above a reel. The palette is almost entirely achromatic — only one vivid blue (#6199f6) and a muted violet border tone (#4f4f80) break the monochrome, used sparingly for icons, eyebrow labels, and card edges. Typography is the loudest voice: a single geometric sans (FrameGothic) carries everything from 80px display headlines to 14px body copy, with custom inktrap letterforms reserved for tiny all-caps section labels. Components stay thin and editorial: pill-shaped nav buttons, ghost CTAs, 10px-radius cards with violet-tinted borders, and zero decorative ornament — every element exists to frame the work, not compete with it.

## Color Palette

- **Carbon Vellum**: `#fcfcfc` — Primary text, inverse button text, icon strokes — near-white reads as paper against the void [neutral]
- **Obsidian**: `#0a0a13` — Primary page canvas and dominant background; the slight blue undertone keeps it from feeling flat black [neutral]
- **Pitch**: `#000000` — Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color [neutral]
- **Void**: `#040407` — Secondary canvas layer and topmost nav background, one shade lighter than Pitch [neutral]
- **Graphite**: `#08080c` — Card surface for elevated product mockups, sits one step above Obsidian [neutral]
- **Smoke**: `#757580` — Secondary body text and metadata — cool gray, never warm, stays quiet under headlines [neutral]
- **Ash**: `#a3a3b3` — Tertiary text, card descriptions, inactive nav, most frequently used muted foreground [neutral]
- **Charcoal**: `#2a2a32` — Subtle card border on light-mode-adjacent surfaces; hairline divider [neutral]
- **Iris Glow**: `#6199f6` — Sole chromatic accent — icons, eyebrow labels, links, active states, feature marks. One blue, used surgically, carries the entire brand identity [brand]
- **Twilight**: `#4f4f80` — Muted violet used for card borders, glow halos, and atmospheric tints — the only color allowed to live near content surfaces [accent]
- **Specter Lilac**: `#dedfee` — Soft highlight on violet accents and light-mode card edges; cool, desaturated lavender [accent]

## Typography

- **Times**
- **FrameGothic**
- **NeueMachinaInktrap**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.45 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.45 |
| subheading | 18 | — | 1.3 |
| heading-sm | 24 | — | 1.25 |
| heading | 38 | — | 1.04 |
| heading-lg | 48 | — | 1.02 |
| display | 80 | — | 0.96 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 24px
- **Element Gap**: 24px
- **Section Gap**: 80px
- **Border Radius**: {'nav': '100px', 'cards': '10px', 'pills': '100px', 'buttons': '100px', 'dividers': '1px', 'featureCards': '24px'}

## Layout

Full-bleed dark canvas with all content constrained to a max-width of ~1280px centered. The hero is a split composition: left half carries the display headline and stacked CTAs (left-aligned), right half shows the product UI mockup floating against the cosmic gradient. Section rhythm alternates between text-dominant bands and product-visual bands, with 80px vertical gaps. Mid-page uses a 4-column feature grid (icon + heading + body) that reads more like editorial columns than cards. No sidebar, no mega-menu — navigation is a single slim top bar with pill buttons. Lower sections are full-width video showcases with centered text above. The overall density is spacious and cinematic — sections breathe, with generous padding and a single horizontal scroll metaphor implied by the flowing gradient background.

## Surfaces / Elevation

- **Cosmic Canvas**
- **Nav Veil**
- **Product Surface**
- **Card Halo**

**Shadow tokens:**

## Imagery

Imagery is the product itself: high-fidelity screenshots of the Frame.io app interface dominate the hero, showing real video thumbnails, review threads, and version stacks. Below the fold, cinematic stills from actual films/projects (a silhouetted figure against warm light, a close-up portrait of a performer) are presented as full-bleed video showcases with minimal player chrome. No stock photography, no abstract illustrations, no 3D renders — the visual language is 'show, don't decorate.' The cosmic gradient backgrounds (deep purples, midnight blues, near-black) create an atmosphere of a dark editing suite or projection room. Icons throughout the UI are thin-stroke, single-color Iris Glow, 24px, outlined style. No filled iconography anywhere.

## Design Principles

### Do

- Use 100px border-radius for all buttons, nav items, and pills — the pill geometry is the brand's most repeated shape
- Set display headlines at weight 400 with tight negative letter-spacing (-1.92px at 48px, -3.6px at 80px) — never go bold for impact
- Reserve Iris Glow (#6199f6) for icons, eyebrow labels, links, and active states — one accent color, used surgically
- Place the NeueMachinaInktrap eyebrow label (12px, uppercase, 0.06em tracking) above every section headline as a section marker
- Layer at least one gradient on every page background — never use flat #0a0a13 alone, the cosmic atmosphere requires depth
- Set the max content width to 1280px and center all content within it, while backgrounds run full-bleed
- Use FrameGothic at 14–18px for all body and feature text in #a3a3b3 or #757580 — these two grays carry all secondary information
- Frame product imagery in 10px-radius containers with a 1px #4f4f80 violet border — the halo is the only frame allowed

### Don't

- Do not use weight 600 or 700 for display headlines — the 400 weight is a signature restraint choice
- Do not introduce additional accent colors — Iris Glow is the only chromatic accent in the system
- Do not use flat black (#000000) as a full-page background — always layer gradients to create the cosmic atmosphere
- Do not add card backgrounds or heavy borders to feature columns — they are typographic blocks, not cards
- Do not use serif fonts, decorative typefaces, or any font other than FrameGothic, NeueMachinaInktrap, or system fallbacks
- Do not add drop shadows to buttons or nav items — the fill contrast alone carries the hierarchy
- Do not center-align body paragraphs — left-align with a max-width of ~560px for readable line lengths
- Do not use the eyebrow label style (NeueMachinaInktrap caps) for any text other than section identifiers — it's a stamp, not a label

## Components

### Pill Navigation Button

100px border-radius pill, 12px 20px padding, Carbon Vellum fill, Obsidian text at 14px FrameGothic 500. Zero border, no shadow. The pill geometry is the brand's most repeated shape.

### Ghost Nav Link

Transparent fill, no border, Carbon Vellum text at 14px FrameGothic 400. Underline appears on hover; no background shift. Stays nearly invisible until interacted with.

### Sign In Text Link

Plain text button, Carbon Vellum at 14px FrameGothic 400, no background, no border. The lightest possible interactive element.

### Hero CTA Pill

100px radius, Carbon Vellum fill, Obsidian text, 14px FrameGothic 500, 14px 28px padding. Casts no shadow. The white pill against the cosmic gradient is the page's most contrasting element.

### Ghost CTA Button

100px radius, transparent fill, 1px Carbon Vellum border, Carbon Vellum text, 14px FrameGothic 400, 14px 28px padding. Inverts to filled Carbon Vellum on hover.

### Announcement Banner

Full-width strip with deep blue-to-violet gradient, Carbon Vellum text at 13px centered, dismiss 'x' on the right. Height ~40px, sits above the main nav.

### Eyebrow Label

NeueMachinaInktrap 12px, weight 400, letter-spacing 0.06em, color Iris Glow (#6199f6) or Smoke. Line-height 0.90. Always sits above the section headline, left-aligned.

### Display Headline

FrameGothic 400 at 48–80px, line-height 0.96–1.02, letter-spacing -1.92 to -3.6px, Carbon Vellum. Weight 400 (not bold) is a deliberate restraint choice — the size does the work, the weight whispers.

### Subheadline Paragraph

FrameGothic 400 at 18px, line-height 1.30, Smoke (#757580). Max-width ~560px. Stays quiet — its job is to inform, not to compete with the headline.

### Feature Column Card

Transparent background, no card surface. Layout: Iris Glow icon (24px) at top, FrameGothic 500 18px Carbon Vellum heading, 14px Smoke body copy below. 24px column gap. The feature 'card' is really just a typographic block — no border, no background.

### Product UI Mockup Container

10px border-radius, 1px Twilight (#4f4f80) border, inner surface is the native dark UI of the product (Graphite, ~#181826 with violet shadow #181826). The container is intentionally minimal — a thin violet halo, nothing else.

### Video Showcase Player

10px border-radius, embedded video player with Iris Glow play button overlay (48px circle, 60% opacity). Caption strip below at 12px Smoke. The video itself is the hero — the player chrome is nearly invisible.

### Section Divider

No physical divider — sections flow seamlessly using the cosmic gradient background. When separation is needed, a 1px Charcoal (#2a2a32) hairline.

### Adobe Logo Mark (nav)

Tiny stacked-triangle Adobe 'A' mark at far right of nav, Carbon Vellum, 16px height. Pure brand signal, no interaction.

## Similar Design Systems

- {'why': 'Same dark editing-suite atmosphere with deep purple gradient backgrounds and one blue accent for active tools', 'business': 'Adobe Premiere Pro'}
- {'why': 'Dark-mode creative platform with pill-shaped CTAs and video-first product mockups dominating the hero', 'business': 'Vimeo'}
- {'why': 'Similar commitment to a single accent color against near-black, with display type at weight 400 and tight letter-spacing doing all the visual work', 'business': 'Linear'}
- {'why': 'Dark product pages with cosmic gradient backgrounds, oversized thin-weight headlines, and one vivid accent for interactive elements', 'business': 'Pitch'}

## Agent Prompt Guide

## Quick Color Reference
- background: #0a0a13 (cosmic canvas) or full cosmic gradient
- text: #fcfcfc (primary), #757580 (secondary), #a3a3b3 (tertiary)
- border: #4f4f80 (violet halo) or #2a2a32 (charcoal hairline)
- accent: #6199f6 (Iris Glow — icons, eyebrow labels, links)
- primary action: no distinct CTA color
- secondary action: ghost border in #fcfcfc

## Example Component Prompts

**1. Hero Section with Display Headline**
Full-bleed cosmic gradient background (linear: #0a0010 → #02000a → #0c1d32). Left half: eyebrow label 'THE FRAME.IO PLATFORM' in NeueMachinaInktrap 12px, #6199f6, letter-spacing 0.06em. Display headline below in FrameGothic 400, 80px, line-height 0.96, letter-spacing -3.6px, color #fcfcfc. Subheadline at FrameGothic 400, 18px, #757580, max-width 560px. Two CTAs stacked: filled pill (#fcfcfc bg, #0a0a13 text, 100px radius, 14px 28px padding) and ghost pill (transparent, 1px #fcfcfc border, #fcfcfc text). Right half: product UI mockup in 10px-radius container with 1px #4f4f80 border.

**2. Feature Column**
Four-column grid, 24px gap. No card background. Iris Glow (#6199f6) outlined icon at 24px at top. FrameGothic 500, 18px, #fcfcfc heading. FrameGothic 400, 14px, line-height 1.50, #a3a3b3 body copy below heading.

**3. Eyebrow Label + Section Headline**
Stack with 6px gap. Eyebrow: NeueMachinaInktrap 12px, #6199f6, uppercase, letter-spacing 0.06em, line-height 0.90. Headline: FrameGothic 400, 48px, line-height 1.02, letter-spacing -1.92px, #fcfcfc.

**4. Video Showcase Block**
Full-width container with 80px top padding. Centered eyebrow label and headline above. Below: video player in 10px-radius frame, Carbon Vellum play button overlay, 1px #4f4f80 border, subtle shadow (0 24px 48px rgba(0,0,0,0.5)). Optional caption strip at 12px #757580.

**5. Ghost Nav Item**
Transparent, no border, FrameGothic 400, 14px, #fcfcfc. On hover: underline appears. No background change ever.

## Gradient System

Frame.io's background is not a flat color — it's a layered cosmic atmosphere built from 3-4 radial and linear gradients stacked on the Obsidian canvas. The hero combines a diagonal linear gradient (195deg, #0a0010 → #02000a → #0c1d32) with a radial glow (centered bottom, #000b35 → transparent). Mid-page sections use a different radial (top-left origin, #0e0f20 → #0c0c19 → #000000) to shift the light. The result: a page that feels like the same dark room but with light pooling in different corners. Never use a flat #000000 for a full background — always layer at least one gradient to create depth. Gradient colors should stay within the palette: deep indigos (#0c1d32), midnight purples (#0a001e), and near-blacks with blue undertones (#0e0f20).

## Type as Identity

Frame.io's typographic system is its strongest brand signal after the accent color. Three rules carry the entire identity: (1) Display type is always weight 400, not 700 — the size and tight letter-spacing do the heavy lifting, the weight whispers. This is a deliberate anti-SaaS-hero choice. (2) The NeueMachinaInktrap eyebrow label is the only place where the inktrap geometry appears; it stamps each section like a mechanical serial number. (3) Letter-spacing scales inversely with size: -0.045em at 80px, -0.01em at 16px, +0.06em at 12px caps. Large type compresses, body type relaxes, labels expand. Do not flatten this — each size has its own tracking value.
