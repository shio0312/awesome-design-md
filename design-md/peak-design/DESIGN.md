# Peak Design — Design System

> **North Star**: Gallery wall, half lit
> **Theme**: light
> **Source**: https://peakdesign.com
> **Refero Style**: https://styles.refero.design/style/6f3fb64d-d4c9-4ec1-86a1-7983e5180985
> **Synced**: 2026-09-01

## Overview

Peak Design is a gallery-grade commerce experience: a near-monochrome canvas where editorial typography and product photography do all the work. The system alternates between crisp white surfaces and deep near-black panels, creating dramatic split layouts where one side carries an italic serif headline and the other a full-bleed product or lifestyle image. Typography is the brand's primary voice — a tall condensed display serif (Exposure-style) for headlines paired with a neutral grotesque (Geist) for UI and an all-caps compressed sans (bryant) for labels, eyebrows, and buttons. The interface stays disciplined: no chromatic UI elements, no decorative gradients, no shadows — just hairline borders, two corner radii (4 and 8), and a single red accent reserved for rare emphasis. Components feel engineered rather than decorated: thin dividers, flat product cards, pill-shaped filter chips, and ghost buttons that read as architectural annotations.

## Color Palette

- **Carbon Ink**: `#1a211e` — Primary text, dark hero panels, body copy, icons, borders on light surfaces — the near-black that anchors every headline and forms the deep-background panels of split sections [neutral]
- **Paper White**: `#ffffff` — Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color [neutral]
- **True Black**: `#000000` — Maximum contrast elements: headline fills on white, announcement bar, footer treatments, solid icon strokes — appears where the design demands the sharpest edge [neutral]
- **Obsidian**: `#0c0c0c` — Deep panel surfaces and image overlays — slightly softer than true black, used for full-bleed dark sections that need to feel weighty without flat black's harshness [neutral]
- **Fog**: `#eef1f0` — Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color [neutral]
- **Mist**: `#e0e0e0` — Divider lines, disabled states, subtle structural separators — the mid-light gray that defines boundaries between sections on the white canvas [neutral]
- **Graphite**: `#606562` — Muted body text, secondary navigation, metadata labels — the de-emphasized text tone for information that supports but should not compete with headlines [neutral]
- **Ash Border**: `#cccfcd` — Hairline input borders, subtle dividers — a warm-leaning gray that reads as a soft pencil line against white surfaces [neutral]
- **Slate**: `#363537` — Navigation text on light surfaces, mid-weight borders — reads as near-black at small sizes but carries a subtle warmth [neutral]
- **Pewter**: `#4e4e4e` — Supporting neutral for secondary UI, dividers, and muted labels [neutral]
- **Ember Red**: `#cc2e39` — Red supporting accent for decorative details and low-frequency emphasis [accent]

## Typography

- **Geist**
- **Exposure-style serif (Exposure-10)**
- **Bryant-style condensed sans (bryant)**
- **Geist Mono**
- **Exposure-10**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1 |
| button-label | 16 | — | 1.1 |
| heading-sm | 24 | — | 1.2 |
| heading | 32 | — | 1.2 |
| heading-lg | 48 | — | 1.1 |
| display | 80 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 24px
- **Element Gap**: 24px
- **Section Gap**: 80px
- **Border Radius**: {'nav': '4px', 'cards': '8px', 'badges': '9999px', 'images': '8px', 'inputs': '4px', 'buttons': '4px', 'buttonsRounded': '32px'}

## Layout

Full-bleed page sections that alternate between white and near-black, each section spanning the full viewport width with no max-width constraint at the section level. Content within sections is max-width ~1440px and centered. The dominant hero pattern is a 50/50 split: text block (eyebrow + display headline + subtext + buttons) on one side, full-bleed product or lifestyle image on the other. Below the fold, product grids use 4 columns of equal-width product cards with generous 24-32px gaps. Category filter bars sit directly below the main nav as a horizontal row of pill chips. Section rhythm is defined by alternating light/dark bands with 80px vertical padding between sections, creating an editorial magazine cadence. Navigation is a sticky top bar with a thin announcement strip above it.

## Surfaces / Elevation

- **Canvas**
- **Soft Card**
- **Hairline**
- **Deep Panel**

## Imagery

Product photography dominates the visual language: bags, slings, and camera gear shot on pure white backgrounds with no lifestyle context, lit to show material texture and hardware details. Lifestyle imagery appears only in full-bleed editorial sections (e.g., hands holding cameras in a circle) and occupies the full viewport width on one side of a split panel. Images have no border-radius in hero contexts (flush to edges) and 8px radius in card contexts. No illustrations, no abstract graphics, no icon illustrations beyond functional UI icons. The product IS the hero — the photography is studio-grade, consistent angle, consistent lighting, consistent white ground, and the UI steps back to let the objects speak.

## Design Principles

### Do

- Use the Exposure-style serif italic only for hero and section-display headlines at 48px or larger; never for body, UI labels, or anything below 40px.
- Set body text in Geist 400 at 16px with 1.5 line-height; reserve Geist 600/700 for product names and inline emphasis only.
- Use bryant 700 uppercase with positive tracking (0.038em at 14px, 0.057em at 16px) for every navigation label, button, and eyebrow text — never set bryant in mixed case.
- Alternate between white (#ffffff) and near-black (#0c0c0c or #1a211e) full-bleed sections to create editorial split layouts; never use both tones within a single product card or form.
- Maintain 8px border-radius for all cards and product images, 4px for all buttons, inputs, and nav elements, and 9999px for all badges and filter pills.
- Use #cc2e39 Ember Red only for single-instance emphasis (a sale indicator, urgency badge, or brand punctuation); never apply it to standard buttons, links, or repeated UI elements.
- Keep product cards borderless and shadowless — separate them from the canvas with 24px+ whitespace, not with containers or elevation.

### Don't

- Do not introduce colored backgrounds for buttons, cards, or section panels — the system is deliberately monochromatic with black/white/gray only.
- Do not add box-shadow or drop-shadow to any element; the design relies on flat color contrast and hairline borders for separation.
- Do not set body or UI text in the Exposure serif — it is a display face only and loses legibility below 32px.
- Do not use mixed case with the bryant font; it is designed for compressed uppercase labels and reads as a different typeface in lowercase.
- Do not place the full-color Ember Red on more than one element per viewport; its power comes from scarcity in a grayscale system.
- Do not use rounded corners larger than 8px on cards or images, and never apply 32px or 9999px radius to anything other than buttons and badges respectively.
- Do not center-align body copy or product descriptions — the layout language is left-aligned and editorial, with centered alignment reserved for hero headlines and section labels only.

## Components

### Announcement Bar

Full-width black (#1a211e) strip, ~32px tall, white (#ffffff) text at 14px bryant weight 700 uppercase with 0.057em tracking. Content centered horizontally. Provides shipping/warranty/return info and secondary navigation entry points (store finder, mission).

### Primary Navigation

White (#ffffff) background, ~64px tall, with hairline bottom border (#e0e0e0). Left: Peak Design diamond/peak logo in #1a211e. Center-left: category links in bryant 700 16px uppercase (#363537), letter-spacing 0.057em. Center: full search input field with #eef1f0 background, #cccfcd border, 4px radius, 14px Geist placeholder text in #606562. Right: Support link, account icon, cart icon — all in #1a211e. No background fill, no elevation.

### Category Filter Bar

Pill-shaped filter chips below the main nav, 8px row gap between chips. Active state: #1a211 fill with #ffffff text. Inactive: transparent fill with #363537 text and #cccfcd border. Text: bryant 700 16px uppercase. Height ~40px, horizontal padding 20px, border-radius 9999px. Arrow buttons on right edge for overflow.

### Product Card

White (#ffffff) background, no visible border. Product image fills the card top with 8px border-radius. No padding between image and text. 'New' badge: #4e4e4 pill at top-left of image, white bryant 700 14px text, padding 2px 8px, 9999px radius. Product title: Geist 400 16px #1a211, 4px gap to brand label. Brand label 'Kelp': Geist 400 14px #606562. Price: Geist 400 16px #1a211, 8px below brand label. Card has no shadow or border — content separates by whitespace alone.

### Hero Split Panel

Two-column 50/50 split, full viewport width, 400-600px height. Left panel: #0c0c0c or #1a211 background with eyebrow label in bryant 700 14px white uppercase, then display headline in Exposure-style serif 48-80px italic #ffffff with -0.025em tracking, line-height 1.10. Subtext in Geist 400 16px white at 80% opacity. Right panel: full-bleed product or lifestyle image with no border-radius (flush to viewport edge). Vertical centering of text content within left panel.

### Filled Button (on dark)

White (#ffffff) fill, no border, 4px corner radius. Padding: 12px vertical, 20px horizontal. Text: bryant 700 16px uppercase in #1a211, letter-spacing 0.057em. No shadow, no hover state with elevation shift — the button is a solid rectangle of contrast.

### Outlined Button (on dark)

Transparent fill, 1px white (#ffffff) border, 4px corner radius. Padding: 12px vertical, 20px horizontal. Text: bryant 700 16px uppercase in #ffffff, letter-spacing 0.057em. Border is thin enough to read as an annotation rather than a container.

### Ghost Button (on light)

No background, no border. Text: bryant 700 14-16px uppercase in #1a211, letter-spacing 0.057em. Used for inline links and low-emphasis actions that should feel like annotations on the page.

### Carousel Pagination Dots

Horizontal row of 4-6 dots, 8px gap. Active dot: ~8px wide solid #1a211 rounded pill. Inactive: ~8px circle in #cccfcd. Centered below the product row.

### Search Field

#eef1f0 background fill, 1px #cccfcd border, 4px corner radius. Height ~40px, width fills available nav space. Left icon (magnifying glass) in #606562 at 16px. Placeholder text 'Search for packing cubes' in Geist 400 14px #606562.

### Section Heading Block

Large display serif in #1a211, left-aligned, 48-80px size, line-height 1.10. Optional em-dash suffix (—) as a visual terminal. Appears at the top of content sections with 64px top padding from the previous section.

### Navigation Icon Button

No background, no border. Icon only at 20-24px, stroke weight 1.5px, color #1a211e. 8px padding around clickable area. No hover state with background fill — the icon darkens slightly on interaction.

## Similar Design Systems

- {'why': 'Same restrained editorial typography with serif display + clean sans body, monochromatic warm-neutral palette, generous whitespace, and product photography on pure backgrounds', 'business': 'Aesop'}
- {'why': 'Same premium bag/accessories commerce aesthetic with split hero sections, condensed uppercase nav labels, and near-monochrome palette with black hero panels', 'business': 'Mismo'}
- {'why': 'Same product-grid-first commerce layout with flat product cards, hairline borders, compressed sans nav, and alternating light/dark section bands', 'business': 'Bellroy'}
- {'why': 'Same flat-shaded minimalism with no shadows or gradients, typographic hierarchy as the only visual structure, and a system where whitespace does the work of decoration', 'business': 'Muji'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #1a211e
- background: #ffffff
- dark panel: #0c0c0c
- border: #e0e0e0
- muted text: #606562
- accent: #cc2e39 (rare emphasis only)
- primary action: no distinct CTA color

**Example Component Prompts**

1. **Hero Split Panel**: Full-viewport-width section, 50/50 split. Left half: #0c0c0c background, vertical-center aligned. Eyebrow text in bryant 700 14px white uppercase, letter-spacing 0.91px, margin-bottom 8px. Display headline in Exposure-style serif italic 56px #ffffff, letter-spacing -1.4px, line-height 1.10, max-width 480px. Subtext in Geist 400 16px white, 12px margin-top. Right half: full-bleed product image, no border-radius, object-fit cover, flush to viewport edge.

2. **Product Grid Card**: White background, no border, no shadow. Product image at top with 8px border-radius, aspect-ratio 1:1. 'New' badge: absolute top-left 8px from edge, #4e4e4e fill, bryant 700 12px white text, padding 2px 8px, 9999px radius. Below image, 12px gap, then product title in Geist 400 16px #1a211e. 4px gap, brand label 'Kelp' in Geist 400 14px #606562. 4px gap, price in Geist 400 16px #1a211e.

3. **Outlined Hero Button**: Transparent fill, 1px #ffffff border, 4px radius. Padding 12px 20px. Text: bryant 700 16px uppercase in #ffffff, letter-spacing 0.91px. No hover state changes background — only opacity shifts to 0.85.

4. **Category Filter Pill (Active)**: #1a211e background, no border, 9999px radius, padding 8px 20px. Text: bryant 700 14px white uppercase, letter-spacing 0.53px. Inactive variant: transparent background, 1px #cccfcd border, text in #363537.

5. **Search Field**: Full-width within nav, height 40px. #eef1f0 background, 1px #cccfcd border, 4px radius. Left padding 36px for icon. Magnifying glass icon 16px in #606562, absolute left 12px. Placeholder text in Geist 400 14px #606562.

## Editorial Section Patterns

Peak Design's layout language follows three repeating section archetypes: (1) Split hero — 50/50 dark-left/text + light-right/image, with the display serif doing the work; (2) Product carousel — horizontal row of 4 product cards under a left-aligned display heading, with pagination dots below; (3) Manifesto blocks — centered or left-aligned display serif text on white, with optional em-dash terminal, followed by a single ghost or outlined button. Every full-bleed section alternates polarity (white → black → white) to maintain editorial rhythm. No section uses a gradient, image overlay with text, or colored background.
