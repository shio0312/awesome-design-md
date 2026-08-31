# Authkit — Design System

> **North Star**: Frosted glass cathedral at midnight
> **Theme**: dark
> **Source**: https://authkit.com
> **Refero Style**: https://styles.refero.design/style/e80231a2-e4d6-406a-a2c9-2e6109679690
> **Synced**: 2026-09-01

## Overview

AuthKit renders a midnight product-launch aesthetic: a near-black canvas with frosted-glass surfaces, a grid of faint blueprint lines, and luminous text that appears lit from behind a glass layer. Type is almost entirely white-on-dark with one vivid violet as the single functional accent — every interactive surface wears a soft inset hairline of cool blue-white rather than a hard border. Components sit on translucent layers stacked above ambient glows, with cards that look like glass plates lit from below rather than paper panels. Spacing is generous and rhythmic; the hero is a single full-bleed illuminated wordmark surrounded by floating glass cards rather than a conventional split layout.

## Color Palette

- **Midnight Canvas**: `#05060f` — Page background, deepest card surface, badge fills — the near-black base everything else floats on [neutral]
- **Steel Plate**: `#2f343e` — Elevated surface, button fills for ghost/secondary actions, subtle panel backing [neutral]
- **Fog Veil**: `#9da7ba` — Muted body copy, card text — readable but stepped back from headlines [neutral]
- **Moon Mist**: `#c7d3ea` — Body text, secondary labels, muted helper copy [neutral]
- **Frost Glow**: `#d1e4fa` — Primary text fill for body and links, badge text, icon fills — the default luminous foreground [neutral]
- **Ice Highlight**: `#d8ecf8` — Light text on dark surfaces, inverse labels, and high-contrast captions. Do not promote it to the primary CTA color; Headline gradient — top-to-bottom fade from Ice Highlight to soft blue, used on the AuthKit wordmark and key headings [neutral]
- **Pure White**: `#ffffff` — Button text, input text, maximum-emphasis foreground [neutral]
- **Void Violet**: `#663af3` — Primary CTA fill — the only chromatic accent, used exclusively for the Continue/Submit button inside auth forms; vivid violet against near-black creates focused urgency without breaking the monochromatic mood [brand]
- **Blueprint Blue**: `#b6d9fc` — Decorative icon accent, soft highlight wash on feature illustrations [accent]
- **Ember Glow**: `#e46d4c` — Secondary accent — appears in demo/showcase contexts (logo recoloring swatches) for brand-color customization display [accent]
- **Signal Blue**: `#027dea` — Secondary accent — appears in customization swatch grids to demonstrate brand-color options [accent]
- **Deep Teal**: `#269684` — Secondary accent — appears in customization swatch grids [accent]
- **Gridline Blue**: `#3f4959` — Shadow color for outer card drop-shadows — cool dark blue-grey gives elevation a tinted, on-brand feel rather than neutral black [neutral]
- **Glass Edge**: `#bad7f71f` — Hairline borders on buttons, inputs, and links — inset 1px stroke of frosted blue-white that defines edges without hard lines [neutral]
- **Luminous Fill**: `#c7d3ea1f` — Badge fill and soft surface tint — translucent cool white for tag backgrounds and subtle UI washes [neutral]

## Typography

- **Untitled Sans**
- **aeonikPro**
- **dotDigital**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.33 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.33 |
| heading-sm | 24 | — | 1.17 |
| heading | 28 | — | 1.14 |
| heading-lg | 44 | — | 1.16 |
| display | 48 | — | 1.17 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 16px
- **Section Gap**: 120px
- **Border Radius**: {'cards': '16px', 'badges': '6px', 'inputs': '6px', 'modals': '16px', 'buttons': '999px', 'iconContainers': '9999px'}

## Layout

Full-bleed dark canvas, max-width 1200px content container centered. Hero is a single centered illuminated wordmark ('AuthKit' in gradient display type) under a small eyebrow label, with three floating glass auth-form cards layered behind/below in an overlapping fan (left card tilted left, center card scaled largest, right card tilted right). Below the hero, a light/dark theme toggle sits centered. Feature row is a horizontal 6-icon timeline with thin connecting lines between circular icon tiles. Section rhythm: every section opens with a centered eyebrow label flanked by fading horizontal lines, then a large centered heading (44-48px), then a single line of muted body copy (16-18px), max ~640px width. Customization section features a mock browser-window frame with the auth card centered, surrounded by floating UI inspector panels (color swatches, radius sliders, logo icon picker, button text field, page background field) positioned at the corners of the canvas like a design-tool workspace.

## Surfaces / Elevation

- **Midnight Canvas**
- **Steel Plate**
- **Frosted Glass**
- **Deep Glass**

**Shadow tokens:**

## Imagery

Visuals are dominated by glass-morphism auth-form mockups (email/password inputs, social-login buttons, passwordless code-entry) rendered as floating translucent cards against the midnight canvas. Feature icons are line-art mono glyphs in #d1e4fa inside circular frosted tiles. A faint blueprint grid (1px lines at rgba(186,215,247,0.06)) covers the full page as ambient atmosphere, and a conic-gradient spotlight halo glows at the top of the hero. No photography, no lifestyle imagery, no product screenshots — the product IS the visual: login boxes arranged like glass prototypes in a dark studio.

## Design Principles

### Do

- Use 999px radius for all interactive elements (buttons, social-login buttons, tag toggles); reserve 16px radius exclusively for cards and modals, 6px for badges and inputs, and 9999px for circular icon containers.
- Build elevation from inset frost highlights + soft outer halos rather than conventional drop-shadows: pair inset rgba(216,236,248,0.2) 1px top edge with a 24-48px inset glow and a dark cool drop.
- Use Void Violet (#663af3) exclusively for the auth-form Continue/submit CTA — never as a decorative accent or non-auth button background.
- Set headline text in aeonikPro weight 500 at 44-48px with the Skywash vertical gradient (#d8ecf8 → #98c0ef); body and UI in Untitled Sans 400-500.
- Place all-caps eyebrow labels (dotDigital, 15px, 0.10em tracking, #c7d3ea) centered and flanked by fading horizontal lines at rgba(186,215,247,0.12) to mark every section opening.
- Use rgba(186,215,247,0.12) as the universal hairline border — never solid strokes; the frosted-inset edge is the system's border language.
- Set section gaps at 120px and card padding at 24px; rhythm should feel cathedral-like rather than dense SaaS.
- Render text in the Ice Highlight → Frost Glow → Moon Mist → Fog Veil progression (#d8ecf8 → #d1e4fa → #c7d3ea → #9da7ba) for heading → body → muted body → helper copy.
- Use the conic-gradient spotlight halo (rgba(124,145,182,0.5) at center, fading outward) at the top of every full-bleed hero to anchor the composition.

### Don't

- Do not introduce additional chromatic accents — the palette is monochromatic with one violet CTA; any extra hue breaks the system.
- Do not use solid colored borders; replace them with 1px inset rgba(186,215,247,0.12) strokes to preserve the glass aesthetic.
- Do not use bold weights (600+) on aeonikPro display headings — the wordmark's authority comes from weight 500 at large size, not volume.
- Do not apply conventional drop-shadows; the system reads elevation through inset glow + dark halo.
- Do not mix radius families on the same component type — every button is pill, every card is 16px, every badge is 6px.
- Do not place white (#ffffff) on background tints brighter than rgba(186,214,247,0.12) — the contrast floor collapses.
- Do not use the Skywash gradient on body text or buttons; reserve it for the display wordmark and the largest headings only.
- Do not introduce light-theme colors into core tokens even though the product supports light mode; the marketing site is dark-first, and light-mode demos are a product feature, not a design-system palette.

## Components

### Pill Button (Primary Ghost)

999px radius, padding 8px 16px, background rgba(186,214,247,0.06) (faint frost wash), text #ffffff, 1px inset border rgba(186,215,247,0.12) of frosted blue-white. Weight 500, 14px Untitled Sans. Hover lightens the frost wash to rgba(186,214,247,0.12).

### Pill Button (Outlined)

999px radius, padding 8px 16px, transparent background, text #d1e4fa, 1px inset border rgba(186,215,247,0.12). Same geometry as primary ghost; only the fill differs.

### Violet CTA Button

Solid fill #663af3, white text, 6px radius, padding 12px 24px, weight 500. The only place a non-monochrome button appears; its vivid violet punches against the midnight palette.

### Glass Card (Feature)

16px radius, background rgba(186,214,247,0.03) (nearly invisible frost tint), padding 24px, no hard border. Elevation built from inset frost highlight + soft outer halo — reads as a glass plate lit from behind.

### Auth-Form Modal Card

16px radius, background rgba(5,6,15,0.97), padding 24-32px. Three-layer shadow stack: top inset frost (#d8ecf8 20%), mid inset glow (#a8d8f5 6%), bottom drop (#000 30%). Floats above the hero with the central card scaled larger than its siblings.

### Text Input

6px radius, background rgba(199,211,234,0.06), text #ffffff, placeholder #c7d3ea at ~60% opacity, 1px inset border rgba(186,215,247,0.12). Padding 10px horizontal. Focus state increases the border opacity to 0.24.

### Provider Button (Social Login)

Full-width pill (999px or 6px radius variant), padding 12px 16px, background rgba(199,211,234,0.06), white text, provider icon left-aligned. Divider 'OR' sits between email submit and social options in 12px muted caps.

### Section Eyebrow Label

15px dotDigital, weight 400, letter-spacing 0.10em, color #c7d3ea, centered. Flanked by thin horizontal lines that fade from transparent to rgba(186,215,247,0.12) and back.

### Feature Icon Tile

9999px radius (perfect circle), ~56-64px square, background frosted tint, outlined glyph icon in #d1e4fa. Icons are line-art (1.5px stroke), mono — no fill, no color variation between tiles.

### Badge / Tag

6px radius, background rgba(199,211,234,0.12), text #d1e4fa, padding 4px 8px, 12px Untitled Sans weight 500. Multi-layer inset shadow gives a faint inner glow.

### Logo Mark (WorkOS / AuthKit)

WorkOS wordmark is Untitled Sans weight 500 at 16px in #d1e4fa. The AuthKit hero wordmark is aeonikPro weight 500 at ~140-180px (display size extrapolated), filled with the Skywash vertical gradient (#d8ecf8 → #98c0ef).

### Background Grid Layer

Full-bleed SVG/div layer with 1px lines at rgba(186,215,247,0.06), ~80-100px cell spacing, masked to fade at edges. A conic gradient halo sits at the top center creating a spotlight effect.

### Theme Toggle (Light/Dark)

Pill-shaped segmented control, 999px radius, two segments (moon icon / sun icon), 32px tall. Active segment has a slightly brighter frost background; inactive is transparent.

### Customization Swatch

Small 20-24px squares, 4-6px radius, filled with the brand color (violet, blue, teal, orange). Arranged in a row with 4px gaps. Labeled 'Colour' in 12px muted text.

## Similar Design Systems

- {'why': 'Same near-black canvas, monochromatic blue-white text, single vivid violet as the only chromatic accent, and floating glass-morphism product cards', 'business': 'Linear'}
- {'why': 'Dark-first marketing surfaces with gradient-filled display type, frosted glass UI mockups, and minimal hairline borders at low opacity', 'business': 'Vercel'}
- {'why': 'Devtools auth-product landing with dark canvas, glass-card auth-form mockups as the hero visual, and monochrome-with-one-accent palette', 'business': 'Clerk'}
- {'why': 'Companion brand — shares the WorkOS/Radix visual lineage with blueprint-grid backgrounds, frosted surfaces, and dot-tracked all-caps eyebrow labels', 'business': 'Radix'}
- {'why': 'Gradient-filled display headings on dark backgrounds, translucent glass cards as product showcases, and restrained palette with one signature accent', 'business': 'Stripe'}

## Agent Prompt Guide

Quick Color Reference:
- canvas: #05060f
- surface (frosted glass card): rgba(186,214,247,0.03)
- surface (elevated modal): rgba(5,6,15,0.97)
- text (headline): #d8ecf8
- text (body): #d1e4fa
- text (muted): #c7d3ea
- text (helper): #9da7ba
- border (hairline): rgba(186,215,247,0.12)
- accent / primary action: #663af3 (filled action)

Example Component Prompts:

1. Create a Primary Action Button: #663af3 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. Section eyebrow + heading stack: eyebrow is 15px dotDigital weight 400 letter-spacing 0.10em #c7d3ea, centered, flanked by fading horizontal lines (gradient from transparent to rgba(186,215,247,0.12) to transparent). Below, heading is 44px aeonikPro weight 500 in #d8ecf8, centered. Body below is 16px Untitled Sans 400 in #c7d3ea, max-width 640px centered.

3. Feature icon tile row: six circular tiles (9999px radius, 56px), background rgba(186,214,247,0.06), outlined line-art icon centered in #d1e4fa, label below in 14px Untitled Sans #c7d3ea. Tiles connected by 1px horizontal line at rgba(186,215,247,0.12).

4. Ghost pill button: 999px radius, padding 8px 16px, background rgba(186,214,247,0.06), 1px inset border rgba(186,215,247,0.12), text #ffffff, 14px Untitled Sans weight 500.

5. Background canvas with grid: #05060f base, 1px grid lines at rgba(186,215,247,0.06) at 80px intervals, full-bleed, masked to fade at edges. Conic-gradient spotlight at top center: conic-gradient(at 50% -5%, transparent 45%, rgba(124,145,182,0.3) 49%, rgba(124,145,182,0.5) 50%, rgba(124,145,182,0.3) 51%, transparent 55%).

## Gradient System

The system uses three gradient layers stacked vertically: (1) Skywash linear gradient (#d8ecf8 → #98c0ef, 0deg) fills the display wordmark and largest headings; (2) Fading hairline gradients (transparent → rgba(186,215,247,0.12) → transparent) create the section divider lines flanking every eyebrow label; (3) Conic-gradient spotlight halos (transparent → rgba(124,145,182,0.5) → transparent) sit at the top of full-bleed sections as ambient illumination. All gradients are cool-tinted; never introduce warm gradients — the palette stays in the blue-violet spectrum.
