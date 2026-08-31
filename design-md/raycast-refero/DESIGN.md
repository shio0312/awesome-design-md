# Raycast — Design System

> **North Star**: Midnight command center, coral neon
> **Theme**: dark
> **Source**: https://raycast.com
> **Refero Style**: https://styles.refero.design/style/3b6a17f0-3bdf-418c-a95e-0b89e5a8b2f8
> **Synced**: 2026-09-01

## Overview

Raycast reads as a dark power-tool cockpit: an almost-black canvas (#040506) with barely-visible elevation steps, a single warm coral accent (#ff6363) that carries brand identity, and quiet white/gray typography in Inter. Components are defined less by shadows and more by hairline borders, inset highlight strokes, and the distinctive 'keyboard key' inner-shadow treatment that makes cards feel pressed and tactile rather than floating. Color is rationed — the page is 98% achromatic, and the coral appears only in the logo, hero artwork, AI badge, and the occasional warm-tinted surface. Navigation floats with a glass-blur effect, and most interactive surfaces are neutral light-gray buttons on dark, not chromatic CTAs. The hero abandons the system entirely with large red/blue gradient geometry, then the rest of the page returns to the austere dark surface — contrast through atmosphere, not decoration.

## Color Palette

- **Void Black**: `#040506` — Page canvas, dominant background — the near-pure-black base that most of the interface sits on [neutral]
- **Ink**: `#07080a` — Card surfaces, elevated panels, image backgrounds — one step up from the canvas for content blocks [neutral]
- **Obsidian**: `#111214` — Subtle surface tint, pressed states, input wells — used for slight depth on form fields and recessed containers [neutral]
- **Graphite**: `#1b1c1e` — Neutral form states, badge text, and quiet UI feedback where color should stay understated. [neutral]
- **Smoke**: `#6a6b6c` — Secondary body text, muted labels — the everyday reading color on dark surfaces [neutral]
- **Ash**: `#9c9c9d` — Light text on dark surfaces, inverse labels, and high-contrast captions. [neutral]
- **Mist**: `#e6e6e6` — Light neutral action fill for buttons on dark surfaces. [neutral]
- **Iron**: `#454647` — Button text on light fills, mid-gray borders — paired with Mist for filled button labels [neutral]
- **Slate**: `#2f3031` — Dark button borders and labels on ghost/dark buttons [neutral]
- **Pure White**: `#ffffff` — Headings, high-emphasis text, reversed text on light buttons — the loudest text color in the system [neutral]
- **Coral Pulse**: `#ff6363` — Brand accent — logo diamond, AI badge fill, hero artwork saturation, the single warm punctuation in an achromatic system [brand]
- **Ember Hush**: `#452324` — Warm-tinted card backgrounds, accent surface tints — desaturated coral used as a muted backdrop for coral-anchored content [brand]
- **Electric Sky**: `#63a1ff` — Hero illustration mid-tone, decorative gradient — appears only in the dramatic abstract hero artwork, not in interface controls [accent]
- **Cobalt Edge**: `#143ca3` — Hero illustration stroke, deep gradient anchor — paired with Electric Sky in the hero's blue geometry [accent]
- **Deep Space**: `#02193b` — Hero illustration fill, darkest blue in the artwork gradient — not a UI token [accent]
- **Info Blue**: `#56c2ff` — Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]
- **Success Green**: `#59d499` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]

## Typography

- **Inter**
- **GeistMono**
- **SF Pro Text**
- **SF Pro**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| eyebrow | 11 | — | 0.91 |
| body | 16 | — | 1.15 |
| body-lg | 18 | — | 1.15 |
| subheading | 20 | — | 1.2 |
| heading-sm | 24 | — | 1.15 |
| heading | 32 | — | 1.15 |
| heading-lg | 56 | — | 1.17 |
| display | 64 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8-16px
- **Section Gap**: 80-120px
- **Border Radius**: {'cards': '16px', 'pills': '9999px', 'badges': '6px', 'inputs': '8px', 'buttons': '8px', 'largeCards': '20px', 'iconContainers': '99999px'}

## Layout

Page model is max-width ~1200px centered with generous horizontal padding, but the hero and atmospheric sections are full-bleed. The nav bar is a floating pill that sits over the hero with backdrop-blur. Hero is full-viewport height with centered headline (56px Inter 400) over a dramatic red/blue gradient composition. Below the hero, content shifts to contained max-width sections with generous vertical rhythm (80–120px between sections). Card grids appear for features and extensions — 3-column for compact tiles, 2-column for wider feature blocks. Section rhythm is consistent: dark-on-dark bands with hairline dividers, no alternating light/dark sections. Navigation is a single floating glass bar; no sidebar, no mega-menu. The overall density is spacious — the system prefers one strong typographic statement per section over dense information layout.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Recessed**
- **Badge**
- **Accent Tint**

**Shadow tokens:**

## Imagery

Imagery is dominated by the hero: massive abstract red/blue geometric shapes (diagonal bars, radial glows) that feel like a motion-graphics title sequence rather than product photography. Below the hero, the system shifts to in-context product screenshots that show the actual app interface — a dark command bar, result list, and extension icons rendered as if floating on the page. Photography is absent. The visual density shifts dramatically from the cinematic hero to austere product mockups and then to text-heavy feature sections with no imagery at all. Icon style: SF Pro Text system glyphs at 16–24px, weight 500, rendered in Mist (#e6e6e6) on dark surfaces. No photographic, lifestyle, or stock imagery — the product UI is the hero.

## Design Principles

### Do

- Use #040506 as the only page background — never introduce lighter or grayer canvas colors
- Reserve #ff6363 (Coral Pulse) for the logo, hero artwork, AI badge, and warm-tinted card surfaces — never use it for general accent text, icons, or borders in the body of the page
- Use the 'keyboard key' inner shadow stack (rgba(255,255,255,0.05) inset top + rgba(255,255,255,0.25) outer ring + rgba(0,0,0,0.2) inset bottom) on all elevated cards and feature blocks
- Set hero headlines at 56px/400 in Inter with +0.22px letter-spacing — the regular weight at large size is a signature, not a mistake
- Use Mist (#e6e6e6) filled buttons with Iron (#454647) text for all primary actions — the system has no chromatic CTA
- Use 8px radius for buttons, inputs, and badges; 16–20px radius for cards; 9999px for pills; 99999px for circular icon containers
- Separate footer metadata with vertical pipes and render in Geist Mono 12px to signal technical information

### Don't

- Don't use chromatic action buttons — the CTA system is deliberately neutral (Mist on dark), not blue/red/green
- Don't add drop-shadows to cards or panels — elevation comes from the inset key shadow stack, not outer shadows
- Don't use negative letter-spacing on large display text — the system uses slightly positive tracking (0.0040em at 56px) which is anti-convention and intentional
- Don't introduce light theme sections or alternating light/dark bands — the page is dark throughout
- Don't use #ff6363 for body text, link colors, or general icon accents — it is a brand mark, not a functional color
- Don't use multiple accent colors in the same surface — the system is monochromatic with one coral accent, not a multi-hue palette
- Don't use SF Pro Text for body copy — reserve it for icons and numeric stat callouts at 24–32px; body text is always Inter
- Don't break the 8px spacing grid — all padding, gaps, and margins should snap to 8/12/16/24/40 values

## Components

### Glass Navigation Bar

Floating pill-shaped bar with backdrop-blur(48px), 1px solid border at #363739, 8px radius, transparent dark fill (sits over #040506). Logo at left (red diamond + 'Raycast' wordmark in white, 13px/500), nav links centered at 13–14px in #9c9c9d, and a light-gray Download button at right. Padding approximately 8px vertical, 16px horizontal internally.

### Neutral Filled Button (Download CTA)

Light Mist (#e6e6e6) fill, Iron (#454647) text at 13–14px/500, 8px radius, 8px 12px padding. Sometimes paired with a small black/dark icon (Apple, Windows logo) at 15px. This is the only filled action surface in the system — deliberately neutral rather than chromatic, letting the dark page do the contrasting.

### Ghost Nav Link

Transparent background, Ash (#9c9c9d) text at 13–14px, no border, no padding. Hover state transitions to Pure White. 0px radius — the nav bar's outer pill provides the visual containment.

### Feature Card with Key Shadow

16px radius, 24px padding, 8px internal padding on content blocks. Signature treatment uses the 'keyboard key' shadow stack: rgba(255,255,255,0.05) inset top highlight, rgba(255,255,255,0.25) outer 1px ring, rgba(0,0,0,0.2) inset bottom shadow. This creates a pressed, tactile surface — not a floating card but a recessed key cap. Background is transparent on the card surface so the canvas shows through.

### Edge-Highlight Card

16–20px radius, transparent fill, defined by 1px solid #363739 border plus the inset highlight stack. Used when a card needs to be defined by edge rather than surface — the border does the work that a background would on a lighter system.

### Inset Input Field

8px radius, rgba(255,255,255,0.05) fill, 8px 12px padding, Pure White text at 16px/400. Sits recessed in the surface — the slight white tint reads as 'this is a well you can type into' against the dark canvas. Placeholder text in Ash.

### Badge Tag

Graphite (#1b1c1e) fill, Pure White text, 6px radius, 0 6px padding (tight horizontal pill). Used for version numbers, 'beta' tags, and category labels. Compact and quiet — never draws attention away from the content it annotates.

### Circular Icon Container

99999px radius (perfect circle), 20px padding, subtle dark surface fill. Contains a 24–32px SF Pro Text glyph or product icon. The circular frame makes app/extension icons feel like dock items.

### Hero Gradient Banner

Full-bleed dramatic composition using the red/blue gradient geometry: the radial gradient from rgba(4,63,150,0.7) to rgba(6,18,37,0.25) anchors a blue atmospheric wash, while diagonal red/coral shapes (Coral Pulse with 40px+ blur) cut across the center. This is the one place the system breaks its own rules — color, blur, and scale are cranked to maximum for a 'cinematic' moment before the page returns to the austere dark surface below.

### Footer Meta Strip

Centered row of Geist Mono 12px/400 text in Ash, separated by vertical pipe characters. Contains version string (v1.104.21), platform requirement (macOS 13+), and install command. Sits below the download buttons with 8px gap — the monospace treatment signals 'this is technical metadata' without needing a label.

### App Window Mockup

Recreated app interface shown in screenshots — 12px radius outer frame, 16px radius for the command bar at top, 8px radius for result list items. Uses the 'keyboard key' inner shadow stack on the window chrome to make it feel like a physical object. Internal UI uses Pure White text on #07080a, with a single Coral Pulse highlight on the selected/active row.

## Similar Design Systems

- {'why': 'Same dark-near-black canvas with single-hue accent strategy, same Inter-based typography, same restrained component library with hairline borders instead of heavy shadows', 'business': 'Linear'}
- {'why': 'Same full-bleed dark hero with gradient/geometric backdrop, same max-width contained content sections below, same neutral filled button approach against dark surfaces', 'business': 'Vercel'}
- {'why': 'Same dramatic colored hero artwork on a dark canvas, same coral/warm accent that punctuates an otherwise achromatic system, same browser/product-as-artifact aesthetic', 'business': 'Arc Browser'}
- {'why': 'Same dark product-site language with clean Inter type, same hairline-bordered feature cards, same minimal navigation over atmospheric hero', 'business': 'Cron (Notion Calendar)'}
- {'why': 'Same power-user productivity tool positioning with dark UI, same tight typographic scale, same use of subtle warm accents against near-black backgrounds', 'business': 'Tana'}

## Agent Prompt Guide

Quick Color Reference:
- text primary: #ffffff
- text secondary: #9c9c9d
- text muted: #6a6b6c
- background: #040506
- card surface: #07080a
- border: #363739
- brand accent: #ff6363
- primary action: #e6e6e6 (filled action)

Example Component Prompts:

1. Glass Navigation Bar: Floating pill nav with backdrop-filter blur(48px), 1px solid #363739 border, 8px radius, transparent dark fill. Left: red diamond logo (#ff6363) + 'Raycast' wordmark in #ffffff at 13px Inter 500. Center: ghost nav links in #9c9c9d at 13px Inter 500 (Store, Pro, AI, iOS, Windows, Teams, Enterprise, Blog, Pricing) with no padding. Right: neutral filled button — Mist #e6e6e6 fill, Iron #454647 text 'Download' at 13px/500, 8px radius, 8px 12px padding, with a 15px Apple icon.

2. Hero Section: Full-bleed dark (#040506) background. Centered headline 'Your shortcut to everything.' at 56px Inter 400, #ffffff, letter-spacing 0.22px. Subheadline at 16px Inter 400, #9c9c9d, max-width ~480px. Behind the text: large abstract red/blue gradient composition — diagonal coral (#ff6363 with 40px blur) bars cutting across, blue radial gradient wash (rgba(4,63,150,0.7) to rgba(6,18,37,0.25)) at 50% 26%. Below: two neutral filled buttons side by side (Mist fill, Iron text) with Apple/Windows icons, then a Geist Mono 12px footer line: 'v1.104.21 | macOS 13+ | Install via homebrew' in #6a6b6c.

3. Feature Card: 16px radius, transparent fill on #07080a card surface, 24px padding. Apply the 'key' shadow stack: rgba(255,255,255,0.05) 0px 1px 0px 0px inset, rgba(255,255,255,0.25) 0px 0px 0px 1px, rgba(0,0,0,0.2) 0px -1px 0px 0px inset. Inside: 99999px-radius circular icon container (20px padding, dark fill) with a 24px SF Pro Text glyph in #e6e6e6, then a 20px Inter 500 subheading in #ffffff, then 16px Inter 400 body in #9c9c9d.

4. Extension Tile: 8px radius, 8px padding, 1px solid #363739 border. Circular icon container (99999px) with extension icon, extension name in 14px Inter 500 #ffffff, category in 12px Inter 400 #6a6b6c. Tight 8px gap between tiles in a grid.

5. Download Button Group: Two neutral filled buttons side by side with 8px gap. Each: Mist #e6e6e6 fill, Iron #454647 text at 13px Inter 500, 8px radius, 8px 12px padding. Left button: 15px black Apple icon + 'Download for Mac'. Right button: 15px Windows icon + 'Download for Windows (beta)'. Below: Geist Mono 12px version metadata in #6a6b6c, centered.
