# Apple (España) — Design System

> **North Star**: Cathedral of white space with whispered headlines. A vast pale hall where massive weight-700 type hangs in the air, tethered only by pastel product colors and a single blue thread.
> **Theme**: light
> **Source**: https://www.apple.com/macbook-neo
> **Refero Style**: https://styles.refero.design/style/c9cabb96-32fa-4896-837a-f2497ce1c856
> **Synced**: 2026-09-01

## Overview

Apple's product page language is a study in typographic generosity: oversized SF Pro Display headlines floating on near-white canvas, surrounded by enormous negative space that makes every word feel deliberate. The palette is almost monochrome — text at #1d1d1f, canvas alternating between #ffffff and #f5f5f7 — with a single blue accent (#0071e3) reserved exclusively for interactive moments. Color appears in the product imagery itself (the pastel finishes), never as UI decoration. Components are borderless: rounded cards with 28px radii, pill-shaped buttons that nearly touch the page edges with no visible containers, and zero shadow. Rhythm comes from alternating white/gray bands rather than dividers or borders.

## Color Palette

- **Primary Ink**: `#1d1d1f` — Headlines, body text, button labels — the dominant foreground tone across all surfaces; Hero product image background — fades from solid #1d1d1f at top into chromatic blue [neutral]
- **Mid Gray**: `#707070` — Secondary text, nav inactive state, muted UI labels [neutral]
- **Deep Gray**: `#474747` — Navigation text and iconography at medium emphasis [neutral]
- **Hairline**: `#d6d6d6` — Hairline borders between sections and UI elements [neutral]
- **Canvas**: `#f5f5f7` — Alternating section backgrounds — the gray band that breaks up white sections [neutral]
- **Paper**: `#ffffff` — Card surfaces, primary page background, button text on dark fills [neutral]
- **Cool Wash**: `#e8e8ed` — Subtle button backgrounds, hovered surfaces, pagination dot fills [neutral]
- **Faded Surface**: `#fafafc` — Global nav opened state, elevated panel surfaces [neutral]
- **Quiet Dot**: `#777779` — Pagination indicator fills, tertiary interactive state [neutral]
- **Electric Blue**: `#0071e3` — Filled action buttons — the only chromatic accent in the UI, used sparingly for CTAs [brand]
- **Link Blue**: `#0066cc` — Inline body text links, arrow-link chevron text [brand]
- **Ember**: `#b64400` — Orange state accent for badges, validation surfaces, and short status labels. [accent]
- **Sky**: `#c8d8e0` — Product finish swatch — pastel blue surface option [accent]
- **Citrus**: `#dddc8c` — Product finish swatch — pastel yellow-green surface option [accent]
- **Starlight**: `#f0e4d3` — Product finish swatch — warm cream surface option [accent]
- **Silver**: `#e3e4e5` — Product finish swatch — cool gray surface option [accent]
- **Blush**: `#e8d0d0` — Product finish swatch — soft pink surface option [accent]
- **Indigo**: `#596680` — Product finish swatch — muted indigo surface option [accent]
- **Midnight**: `#2e3642` — Product finish swatch — deep charcoal surface option [accent]
- **Citrus Gradient**: `#3b3b23` — Product hero alternative finish — dark base fading through yellow-green highlight [brand]

## Typography

- **SF Pro Display**
- **SF Pro Display**
- **SF Pro Text**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| micro | 12 | — | 16 |
| caption | 14 | — | 18 |
| body-sm | 17 | — | 25 |
| body | 21 | — | 29 |
| body-lg | 28 | — | 32 |
| subheading | 32 | — | 36 |
| heading-sm | 40 | — | 48 |
| heading | 56 | — | 60 |
| heading-lg | 80 | — | 84 |
| display | 96 | — | 100 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 28px
- **Element Gap**: 8-10px
- **Section Gap**: 100-120px
- **Border Radius**: {'cards': '28px', 'links': '10px', 'badges': '36px', 'buttons': '980px', 'smallButtons': '999px', 'productImages': '28px'}

## Layout

Full-bleed sections that stretch edge-to-edge with generous internal padding (~40–80px sides). Content max-width effectively 1200px centered within each band. The hero is a centered stack: eyebrow label, oversized headline, single CTA button, pricing line, then product image filling the lower 60% of the viewport. Sections follow a repeating pattern: heading left-aligned in a band, then either a 2-column feature layout (text-left/image-right or alternating), a 3-column card grid, or a centered visual showcase. Content rhythm is controlled entirely by alternating white/#f5f5f7 backgrounds with 100–120px vertical gaps — no dividers, no cards wrapping features. The global nav is a single 44px sticky bar. Product spec sections use full-width bands with generous internal whitespace, where text sits in narrow columns (~560px) centered against a wider visual area.

## Surfaces / Elevation

- **Canvas White**
- **Canvas Gray**
- **Hover Wash**
- **Nav Elevated**

## Imagery

Apple's visual language is product-first photography: tightly cropped hardware renders on pure white or finish-colored backgrounds, with no lifestyle context or staging. The hero shows hands holding a pastel-green MacBook Neo — the human element is incidental, showing scale and texture rather than emotion. Product variant sections pair two devices side-by-side on their respective finish colors (pink, green, silver, sky blue), each card a flat color field with the product centered. Detail shots use extreme close-ups (laptop hinge, camera module) against neutral backgrounds. There are no illustrations, no abstract graphics, no decorative imagery — the product IS the visual. Iconography throughout is monochrome SF Symbols-style line icons at 1.5–2px stroke weight, drawn from Apple's system icon set. Photography treatment is always high-key: even, shadowless lighting that flattens the product into a graphic shape rather than a dimensional object.

## Design Principles

### Do

- Use SF Pro Display weight 700 for hero headlines at 80–96px with negative tracking up to -1.44px — the tight tracking on huge type is what makes Apple headlines feel architectural.
- Set section backgrounds to alternate between #ffffff and #f5f5f7 to create visual rhythm without borders or dividers.
- Use 28px border-radius on all cards and product images — this is the signature rounding that softens the entire system.
- Reserve #0071e3 for filled CTA buttons only — never as text color, never as decoration. Inline links use #0066cc instead.
- Use pill buttons at 980px or 9999px radius. Square or lightly rounded buttons break the system's fluid feel.
- Set body copy at 17px SF Pro Text weight 400 with -0.022em letter-spacing — this is the canonical reading size across all Apple pages.
- Apply the "numr" font-feature-setting on all numeric content for consistent tabular figures.
- Keep line-height tight on display sizes (1.04–1.07) and open up for body (1.47) — the contrast creates hierarchy without size jumps.
- Let product imagery carry the color. The UI stays monochrome; the MacBook, iPhone, or finish swatch provides all chromatic interest.

### Don't

- Don't use shadows or elevation on cards. The system relies on background-color alternation and 28px radii to establish hierarchy.
- Don't introduce accent colors beyond #0071e3 and #0066cc. Even the orange "Nuevo" badge is used at most once per page.
- Don't set headlines below 40px. Apple's system depends on oversized type to create its cathedral-of-white-space feel.
- Don't use borders to separate sections. Alternate the canvas color (#ffffff ↔ #f5f5f7) instead.
- Don't apply border-radius below 10px to interactive elements. Pills and 28px corners are non-negotiable.
- Don't put decorative gradients on UI surfaces. The complex product-color gradients belong inside product renders, not buttons or cards.
- Don't use weight below 400 for body text or below 600 for headings. The system speaks in clear, weighty voices.
- Don't add background fills to text links. Use color and arrow glyphs only — never boxes around inline links.
- Don't center body paragraphs. Apple headlines can be centered, but multi-line descriptions and supporting copy are left-aligned.

## Components

### Filled Pill Button (Primary CTA)

Pill shape at 980px radius. Background #0071e3, white text. 17px SF Pro Text weight 400. Horizontal padding 16px, vertical 11px. Used for "Comprar" and "Más información" — appears once per section maximum.

### Ghost Pill Button

Transparent fill, 1px border at #1d1d1f or rgba(0,0,0,0.8). 999px radius. Text in #1d1d1f at 17px weight 400. Padding 16px horizontal.

### Text Link with Arrow

No background, no border. Text color #0066cc with trailing arrow glyph (› or →). 17px SF Pro Text weight 400. Underline only on hover.

### Hairline Underlined Link

Transparent fill, text #1d1d1f or #474747, bottom border 1px solid matching text color. 12–14px SF Pro Text. Used in global nav and footer.

### Feature Showcase Card

28px border-radius. White or #f5f5f7 background. Padding 28–40px internal. Contains headline at 40–56px SF Pro Display, supporting body at 17px, and optional CTA. No visible stroke.

### Product Finish Swatch

Small rounded square (~80px) at 28px radius, filled with one of the product finish colors (Sky, Citrus, Starlight, etc). No border, no label inside — color IS the content.

### Section Header

28–32px SF Pro Display weight 600, color #1d1d1f. Followed by optional supporting paragraph at 21px. Left-aligned with generous left/right padding matching page grid. Letter-spacing slightly positive (+0.007em) makes mid-size headings feel warmer.

### Global Navigation Bar

Height 44px. Background transitions from white/transparent to #fafafc on scroll (backdrop-filter blur 20px). Logo + 7 product links + search + bag icon. Links at 12px SF Pro Text weight 400, color #1d1d1f, separated by 8–10px gaps.

### Promo Ribbon

Centered single-line text at 12–14px SF Pro Text. Black text on white. Optional inline link in #0066cc.

### Product Hero

White background. Product name (e.g., "MacBook Neo") at 17px centered. Hero headline at 96px SF Pro Display weight 600, color #1d1d1f, letter-spacing -1.44px. CTA button below, then pricing text at 17px. Product image fills lower half with rounded or full-bleed edges depending on product type.

### Color Variant Showcase

Two side-by-side cards at 28px radius, each containing a product render on its finish-colored background. Cards sit on #f5f5f7 canvas. No text inside — the visual does the work.

### "Nuevo" Badge

Inline text only, no background or shape. Text "Nuevo" in #b64400 (warm orange) at 12–14px SF Pro Text weight 500. Sits above product name as a warm punctuation against the cool palette.

### Dot Pagination Indicator

Small circles ~8px diameter. Active dot at #1d1d1f, inactive dots at #777779. Horizontal spacing 7px between dots.

### Section Divider (Implicit)

No explicit divider line. Sections alternate between #ffffff and #f5f5f7 backgrounds, and the color shift alone signals separation. Vertical spacing 100–120px between bands.

### Footer Legal Block

Background #f5f5f7. Body copy at 12px SF Pro Text weight 400, color #707070. Inline links in #0066cc. Tight line-height 1.33.

## Similar Design Systems

- {'why': 'Same oversized SF Pro Display headlines floating on alternating white/#f5f5f7 bands, same 28px card radii, same pill-shaped blue CTAs, same borderless flat surfaces with zero shadow', 'business': 'Apple iPhone product pages'}
- {'why': 'Same typographic generosity, same monochrome UI with single blue accent, same product-color gradients used only inside hero imagery, same cathedral-of-white-space layout rhythm', 'business': 'Apple Vision Pro pages'}
- {'why': 'Identical component language — pill buttons at 980px radius, 17px body copy with -0.022em tracking, alternating canvas bands without dividers, color presented through product finish swatches not UI decoration', 'business': 'Apple AirPods Max pages'}
- {'why': 'Same font-first hierarchy, same generous whitespace, same near-monochrome UI that lets typography carry all weight', 'business': 'Nothing.tech product pages'}
- {'why': 'Same deliberate restraint — the UI itself is so quiet that the product and its color options become the only visual interest, achieved through identical flat surfaces and absence of decorative chrome', 'business': 'Teenage Engineering'}

## Agent Prompt Guide

Quick Color Reference:
- Text: #1d1d1f (primary), #707070 (secondary), #474747 (nav)
- Background: #ffffff (canvas), #f5f5f7 (alternating bands)
- Border: #d6d6d6 (hairlines only — rarely used)
- Accent: #0071e3 (filled button), #0066cc (inline link text), #b64400 (Nuevo badge)
- primary action: #0071e3 (filled action)

3 Example Component Prompts:

1. Product Hero Section: White (#ffffff) background. Eyebrow text "MacBook Neo" at 17px SF Pro Text weight 400, #1d1d1f, centered. Headline "Hola, Neo." at 96px SF Pro Display weight 600, #1d1d1f, letter-spacing -1.44px, centered. Blue CTA button "Comprar" — #0071e3 fill, white text at 17px weight 400, 980px radius, 16px horizontal padding, 11px vertical. Pricing text "Desde 799 €" at 17px SF Pro Text, #707070, centered below. Product image fills lower section, centered.

2. Feature Showcase Band: #f5f5f7 background. Section padding 100px vertical. Left-aligned heading "Lo principal." at 28px SF Pro Display weight 600, #1d1d1f, letter-spacing 0.007em. Below: single large card with 28px radius, white (#ffffff) background, 40px internal padding, containing headline at 40px SF Pro Display weight 600 and body at 17px SF Pro Text weight 400, #707070.

3. Color Variant Grid: Two cards side-by-side on #f5f5f7 canvas, each 28px radius, no border, no shadow. First card: pastel green (#dddc8c) background with centered product image. Second card: soft pink (#e8d0d0) background with centered product image. 20px gap between cards. Cards fill ~45% width each.

General Rules: Always use SF Pro Display weight 600–700 for headings, SF Pro Text weight 400 for body. Always alternate white and #f5f5f7 between sections. Never use shadows. Never use border-radius below 10px.
