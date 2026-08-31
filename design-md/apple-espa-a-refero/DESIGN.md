# Apple (España) — Design System

> **North Star**: obsidian gallery vitrine — a dark showroom where a single titanium object glows against pure black
> **Theme**: mixed
> **Source**: https://www.apple.com/apple-watch-ultra-3
> **Refero Style**: https://styles.refero.design/style/da7e5084-9e5d-4eb2-bb10-4c2d7733a56e
> **Synced**: 2026-09-01

## Overview

Apple's product page is a cinematic dark-stage that lets hardware speak first: full-bleed near-black canvas, a single hero product floating in negative space, white SF Pro Display headlines at massive scale, and one vivid blue Buy button as the only saturated action color on the page. The page alternates between black feature stages and white detail bands, using generous 28px card radii and 36–980px pill buttons to feel premium and tactile. Color is used as functional punctuation: orange for category eyebrows, blue for links and the single CTA, violet/teal for other product categories. Typography is the only chrome — heavy negative letter-spacing, tight line-heights, and weight contrast between SF Pro Text body and SF Pro Display headlines carry all the hierarchy.

## Color Palette

- **Obsidian**: `#1d1d1f` — Primary dark canvas, card surfaces on dark sections, primary text on light backgrounds — the signature near-black that defines Apple's product stage [neutral]
- **Frost White**: `#f5f5f7` — Primary text on dark backgrounds, light section surfaces, subtle dividers — slightly warm white that softens contrast against pure black [neutral]
- **Pure Black**: `#000000` — Deepest dark canvas for hero and feature stages, footer background — used where absolute darkness amplifies product photography [neutral]
- **Paper White**: `#ffffff` — Light section backgrounds, button text on dark fills, icon fills — the bright counterweight in alternating dark/light page rhythm [neutral]
- **Carbon**: `#111111` — Elevated surface above black, badge backgrounds — sits one step lighter than pure black for subtle layered depth [neutral]
- **Platinum**: `#86868b` — Muted body text, secondary descriptions, subtitle lines, caption text — the conversational gray that recedes behind primary copy [neutral]
- **Graphite**: `#333336` — Subtle elevated surfaces, secondary button backgrounds, nav dividers — quiet structural tone between obsidian and black [neutral]
- **Silver Mist**: `#cccccc` — Nav borders, button outlines, inactive UI chrome — the lightest neutral that still reads as structural rather than decorative [neutral]
- **Smoke**: `#424245` — Hairline borders, low-contrast dividers on dark sections [neutral]
- **Apple Blue**: `#0071e3` — Primary CTA fill (Comprar button), primary action background — the single filled chromatic button color on the page, vivid saturated blue against black creates unmistakable tap target [brand]
- **Link Blue**: `#0066cc` — Text links, inline link text, Learn more arrows — deeper than Apple Blue, optimized for readability on white [brand]
- **Halo Blue**: `#2997ff` — Lighter link variant, accent text on dark backgrounds, secondary link color — brighter blue for dark-surface legibility [brand]
- **Signal Orange**: `#f56900` — Orange outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color [accent]
- **Iris Violet**: `#8668ff` — Secondary category accent, alternate product-line color coding — used sparingly to differentiate categories from the orange-tagged ones [accent]
- **Reef Teal**: `#00a1b3` — Tertiary category accent, alternate product-line color coding — cool counterpoint to the warm orange/iris palette [accent]

## Typography

- **SF Pro Display**
- **SF Pro Text**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.83 |
| body | 14 | — | 1.43 |
| heading-sm | 19 | — | 1.21 |
| heading | 24 | — | 1.17 |
| heading-lg | 32 | — | 1.14 |
| display | 56 | — | 1.07 |
| hero | 80 | — | 1.05 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 28px
- **Element Gap**: 10-12px
- **Section Gap**: 88-120px
- **Border Radius**: {'nav': '980px', 'pill': '980px', 'cards': '28px', 'links': '10px', 'buttons': '36px'}

## Layout

Full-bleed dark canvas with max-width 1440px content centering. The hero is a full-viewport product showcase — large product image centered, headline and CTA cluster bottom-left, enormous negative space dominating the composition. Below the hero, dark feature sections stack vertically with 88–120px gaps, each containing a large rounded photo card (28px radius) with overlaid white text. The page transitions to white sections partway through, maintaining the same max-width but inverting the surface to Paper White (#ffffff) with two-column image+text layouts. Navigation is a sticky pill bar (980px radius) at the top. Section rhythm alternates dark → dark → light, creating a cinematic three-act structure. Content is always left-aligned text with images either full-bleed-column or centered as oversized single subjects — never card grids, never multi-column text.

## Surfaces / Elevation

- **Pure Black Stage**
- **Carbon Layer**
- **Obsidian Card**
- **Graphite Surface**
- **Frost White Panel**
- **Paper White**

## Imagery

Photography is the dominant visual element. Product shots are rendered on pure black (#000000) with dramatic studio lighting that creates soft metallic highlights on the titanium case. Lifestyle photography is shot in high-contrast black and white (desaturated, no color) to avoid competing with the color product shots — runners, athletes, hands on wrists. No illustration, no abstract graphics, no stock photography. Images are full-bleed within their containers with 28px border-radius on cards or edge-to-edge in light sections. Icon style is minimal: outlined SF Symbols in single-weight strokes, monochrome Frost White on dark and Obsidian on light. The visual density is image-heavy in the hero (product occupies 50%+ of viewport) and text-light in detail bands (photographs on one side, copy on the other).

## Design Principles

### Do

- Use #0071e3 Apple Blue as the filled CTA fill on #000000 backgrounds — it is the only filled chromatic button color permitted
- Use 28px border-radius for all photo cards and content containers; 36px for standard buttons; 980px for pill nav and chip elements
- Set headline type to SF Pro Display 600–700 at 56–80px with negative letter-spacing (-0.84px at 56px, -0.24px at 80px)
- Alternate between Pure Black (#000000) feature stages and Paper White (#ffffff) detail bands with 88–120px section gaps
- Tag category content with Signal Orange (#f56900) eyebrows at 17px SF Pro Text 600 — never apply orange to body text or buttons
- Render all body text in Platinum (#86868b) on white sections and Frost White (#f5f5f7) on dark sections — never use pure #ffffff for paragraph copy
- Use 980px border-radius for the top navigation bar and any pill-shaped interactive elements like chips or toggle selectors

### Don't

- Do not use drop shadows, box-shadows, or any CSS elevation — depth comes from surface contrast between #000000, #111111, and #1d1d1f only
- Do not place more than one filled chromatic button in the same viewport — Apple Blue is the single CTA color
- Do not use card grids, masonry layouts, or multi-column text blocks — content is always single-subject or two-column image+text
- Do not apply the orange/violet/teal accent colors to text paragraphs, backgrounds, or large surfaces — they are category labels only
- Do not use #ffffff for body paragraph text on white backgrounds — use Frost White (#f5f5f7) or Platinum (#86868b) to soften contrast
- Do not add gradients, textures, or decorative backgrounds — the only gradient in the system is the subtle #000000→#111111 black-to-carbon surface transition
- Do not use border-radius values outside the defined set (10px, 28px, 32px, 36px, 980px) — Apple's radii are deliberately restricted

## Components

### Hero Stage

Full-bleed Pure Black (#000000) background, 1440px max-width centered. Product image occupies 50–60% of the viewport height, rendered at extreme scale. No visible card chrome — the product floats directly on the canvas. Headline sits bottom-left at 80px SF Pro Display 700, Frost White (#f5f5f7), letter-spacing -0.24px. Eyebrow label at 17px SF Pro Text 600, Frost White, preceded by a small Apple logo glyph. Price text and CTA cluster aligned below the headline.

### Primary CTA Button (Apple Blue Filled)

Filled pill button: background #0071e3, text #ffffff, 36px border-radius, 10px vertical / 20px horizontal padding, SF Pro Text 14px weight 600, letter-spacing -0.22px. The only filled chromatic button on the page. Sits beside a ghost price label ("Desde 899 €") in a inline flex row.

### Ghost Price Label

Borderless text button: text #ffffff on dark stages, SF Pro Text 14px weight 400, 36px border-radius, transparent background, 10px vertical / 20px horizontal padding. Visually quieter than the filled CTA to avoid competing.

### Category Eyebrow Tag

Plain text label in Signal Orange (#f56900), SF Pro Text 17px weight 600, letter-spacing -0.19px. No background, no border, no chip chrome — color alone signals category. Sits above a feature headline, left-aligned.

### Feature Card (Dark Stage)

Full-bleed card on dark sections: 28px border-radius, internal padding ~28px, contains a full-width photograph (B&W product-in-use) with white text overlay positioned in the upper-left quadrant. Overlay text: SF Pro Text 14–17px Frost White, max 3 lines. No visible card border or shadow — the rounded photo edge is the only container cue.

### Light Section Content Block

Paper White (#ffffff) background, text-left/image-right or image-left/text-right two-column layout. Image is full-bleed within its column with no border-radius (edge-to-edge). Text column: orange eyebrow tag, 56px SF Pro Display 700 headline in Obsidian (#1d1d1f), body in Platinum (#86868b) 14–17px, optional inline sub-feature link with arrow icon.

### Top Navigation Bar

Pure Black (#000000) background, 980px pill border-radius, 10px vertical padding, full-width sticky. Apple logo glyph left, nav items centered as SF Pro Text 12px weight 400 Frost White with 8–10px horizontal gaps, search and bag icons right. Semi-transparent on scroll with backdrop blur.

### Promo Banner

Slim bar above nav: Obsidian (#1d1d1f) background, centered SF Pro Text 12px Frost White text with inline blue link "Comprobar >" in Link Blue (#0066cc). 3px vertical padding, no border-radius.

### Section Headline (Dark)

Large left-aligned headline: SF Pro Display 600–700 at 56–80px, Frost White (#f5f5f7), letter-spacing -0.84px at 56px. Minimal surrounding padding — generous negative space above and below. No subtitle, no eyebrow — the headline stands alone.

### Inline Feature Link

Horizontal row: small circular icon (ArrowUpRight or compass) in Obsidian (#1d1d1f) on a white circle, followed by two-line label in SF Pro Text 17px weight 600 Obsidian. Appears below body copy in light sections as a tertiary drill-in.

### Watch Complication Display

The watch screen in hero shows a wayfinding face: black background, neon green (#a3e635 approximately) digital numerals and compass markers, white time display in SF Pro Display at ~44px. Multiple data complications arranged in concentric rings.

## Similar Design Systems

- {'why': 'Same cinematic product-on-black hero staging with massive negative space, single hero subject, and minimal white headline typography', 'business': 'Bang & Olufsen'}
- {'why': 'Full-bleed dark backgrounds with floating product photography, single vivid blue action color, and two-column dark-then-light section alternation', 'business': 'Tesla (vehicle configurator pages)'}
- {'why': 'Dark product showcase pages with generous 28px card radii, SF-style sans-serif headlines at extreme scale, and orange accent for category tags', 'business': 'Sonos'}
- {'why': 'Product-first page architecture: large dark hero with centered product, white headline overlay, single filled CTA, and high-contrast B&W lifestyle photography in dark feature sections', 'business': 'Dyson'}
- {'why': 'Premium dark-canvas product pages with minimal text chrome, dramatic product photography as the visual anchor, and pill-shaped nav bar at 980px radius', 'business': 'Leica'}

## Agent Prompt Guide

**Quick Color Reference**
- text on dark: #f5f5f7 (Frost White)
- text on light: #1d1d1f (Obsidian)
- background dark: #000000 (Pure Black)
- background light: #ffffff (Paper White)
- border/divider: #333336 (dark) / #d2d2d7 (light)
- primary action: #0071e3 (filled action)
- accent/category: #f56900 (Signal Orange)
- link text: #0066cc

**5 Example Component Prompts**

1. **Hero Stage**: Full-bleed #000000 background, max-width 1440px centered. Product photo at 60% viewport height, centered. Bottom-left content stack: Apple logo + "WATCH ULTRA 3" eyebrow in SF Pro Text 17px weight 600 #f5f5f7, then headline "Una fuerza de la naturaleza." at SF Pro Display 80px weight 700 #f5f5f7 letter-spacing -0.24px, then inline row of price text "Desde 899 €" (SF Pro Text 14px #ffffff) and filled pill button #0071e3 background, #ffffff text, SF Pro Text 14px weight 600, 36px radius, 10px 20px padding.

2. **Category Eyebrow + Headline + Body Block (Light Section)**: White #ffffff background. Orange eyebrow "Running" in SF Pro Text 17px weight 600 #f56900, letter-spacing -0.19px. Below: headline "Tus retos piden paso." in SF Pro Display 56px weight 700 #1d1d1f, letter-spacing -0.84px. Body paragraph: SF Pro Text 17px weight 400 #86868b, line-height 1.47, max-width 460px.

3. **Feature Card (Dark Stage)**: Obsidian #1d1d1f background. Card with 28px border-radius, internal padding 28px. Full-width B&W photograph inside. White overlay text top-left: SF Pro Text 14px weight 400 #f5f5f7, max-width 340px, 3 lines max.

4. **Section Headline (Dark)**: Pure Black #000000 background with 120px vertical padding. Left-aligned SF Pro Display 56px weight 700 #f5f5f7, letter-spacing -0.84px, max-width 980px. No subtitle, no eyebrow.

5. **Inline Sub-Feature Link**: Horizontal flex row. Small 32px circular icon container with #f5f5f7 border, inside an outlined arrow/compass icon in #1d1d1f stroke. Then 2-line text in SF Pro Text 17px weight 600 #1d1d1f on light background.

## Page Rhythm

The page follows a three-act cinematic structure: (1) Dark hero — full-bleed product on black with one CTA; (2) Dark feature stages — stacked rounded photo cards on obsidian with overlaid white text, 88–120px vertical gaps; (3) Light detail band — two-column image+copy on white with orange category labels. Never break this dark→dark→light cadence. Never use card grids. Never use multi-column text. One subject per viewport, generous negative space, color appears only in the CTA and category eyebrows.

## Contrast & Type Density

The typographic signature is aggressive negative letter-spacing that increases with size: -0.037em at 10px caption tightens to -0.003em at 80px hero display. This means display text feels optically dense and weighty while small text remains crisp. Line-heights are tight for display (1.05–1.14) and generous for body (1.43–1.83). The "numr" font feature is used for tabular numerals in product specs and pricing — always use it for any numeric data.
