# dope.security — Design System

> **North Star**: Midnight terminal with violet beacons
> **Theme**: dark
> **Source**: https://dope.security
> **Refero Style**: https://styles.refero.design/style/e1f18a7e-5af1-46b3-8f89-bce6c78b80d4
> **Synced**: 2026-09-01

## Overview

dope.security is a midnight terminal aesthetic: near-black canvas, a single vivid violet signal flare, and typography that borrows from luxury travel editorial. The system pairs a geometric sans (Whyte Inktrap) with an italic display serif (GrandSlang) for hero drama and a monospaced inktrap with extreme tracking for the section labels that feel stamped from a boarding pass. Surfaces are flat and borderless; elevation comes from hairline strokes and translucent washes, never shadows. Color is rationed — the violet only appears as a glow, a fill on a single feature, and accent strokes — while the rest of the interface stays in a tight achromatic scale from #f7f9fa down to #090909. The result reads as confident, expensive, and slightly secretive, like a premium lounge at 2am with a single neon sign.

## Color Palette

- **Near Black**: `#090909` — Page canvas, card surfaces, filled button backgrounds — the default void everything else floats in [neutral]
- **Almost White**: `#f7f9fa` — Primary text, icon strokes, nav labels, and 1px borders — the paper-white that does all the talking against the void [neutral]
- **Soft White**: `#f0f0f0` — Section label text in the stamped uppercase style — same family as Almost White but slightly dimmer for hierarchy [neutral]
- **Steel**: `#828384` — Muted secondary text, inactive button surfaces, subdued borders [neutral]
- **Graphite**: `#474747` — Card internal text and subtle dividers — readable on the near-black without competing with the primary text [neutral]
- **Iron**: `#423738` — Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color [neutral]
- **Ash**: `#6b6b6b` — Nav border dividers, helper text, low-emphasis body copy [neutral]
- **Signal Violet**: `#af50ff` — The only chromatic voice: feature card glow, primary action fill, and accent strokes — rationed like runway lighting, not decoration [brand]
- **Lavender Mist**: `#e1bdff` — Soft tint paired with Signal Violet for contrast-safe text and washed background accents [accent]

## Typography

- **Whyte Inktrap**
- **Whyte Inktrap Mono**
- **GrandSlang**
- **system-ui**
- **Karla**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1 |
| heading-sm | 32 | — | 1.2 |
| heading | 48 | — | 1.2 |
| heading-lg | 64 | — | 1.2 |
| section-stamp | 74 | — | 0.9 |
| display | 88 | — | 0.8 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 40px
- **Element Gap**: 16px
- **Section Gap**: 120px
- **Border Radius**: {'cards': '19.2px', 'pills': '1584px', 'buttons': '8px', 'smallControls': '6px'}

## Layout

Full-bleed sections with a 1200px content max-width centered inside. The hero is a split composition: roughly 55/45 text-to-card, with a transparent boarding-pass card overlaying the right side of the atmospheric photograph. Below the hero, the system shifts to edge-to-edge dark bands with no visual dividers between them — rhythm comes from generous sectionGap (~120px) and the stamped 74px section labels. The 'Features' section uses a stacked monospace heading above a list of rows; the comparison block uses a 4-column card grid connected by a horizontal route line. Navigation is a single sticky frosted bar with brand left, links center, two buttons right. Density is comfortable — every section breathes. The page never uses multi-column text or card grids denser than 4 across.

## Surfaces / Elevation

- **Void Canvas**
- **Translucent Panel**
- **Iron Wash**
- **Violet Bloom**

**Shadow tokens:**

## Imagery

Photography is treated as a single dramatic hero asset: a wide-format twilight sky with purple and lavender clouds over a glowing horizon, a single airplane light streaking across. The image is not cropped or masked — it fills the full viewport and the text sits directly on it. After the hero, the page goes almost entirely iconographic: no product screenshots, no lifestyle photos, no stock imagery. The comparison section uses soft radial gradient blooms (blue, pink, purple) as card backgrounds, acting as abstract color studies rather than literal images. Icons are minimal line glyphs (heart, +, arrow) drawn in #f7f9fa. The overall ratio is text-and-rule dominant: imagery occupies less than 15% of the page.

## Design Principles

### Do

- Use Signal Violet (#af50ff) only for one feature card glow, one filled action, and one accent stroke per page — treat it as signal lighting, not theme color
- Set section headings in Whyte Inktrap Mono 74px uppercase with 0.2em tracking; the letterspaced breath is the heading style
- Default all cards to 19.2px radius and 0 padding internally — let layout create the boundary, not a fill or border
- Use 1px or 0.5px solid #f7f9fa borders at low opacity for separation instead of shadows or fills
- Reach for GrandSlang italic at 88–146px for the two or three largest display moments on a page — never for body or nav
- Use the frosted nav pattern: rgba(51,50,72,0.7) background + backdrop-filter blur(10px) + 1px bottom border
- End pages with a coordinate stamp footer in Whyte Inktrap 14px — it is the brand's signature closing gesture

### Don't

- Don't apply box-shadows beyond the nav's single 1px hairline — the system is shadowless by design
- Don't use Signal Violet for borders, text, or body backgrounds — it is reserved for fills and glows only
- Don't use GrandSlang italic for anything smaller than 32px — the warmth of the brush-italic collapses at small sizes
- Don't mix Whyte Inktrap Mono with GrandSlang on the same line — the mechanical stamp voice must stay in its own band
- Don't introduce a new accent color — the palette is 95% achromatic and one violet, adding a third color breaks the system
- Don't center body copy or use multi-column text layouts — the page rhythm is left-aligned with generous side margins
- Don't round buttons to 0px or 4px; the system uses 8px for control buttons and 1584px for pill CTAs — those are the only two button radii

## Components

### Hero Boarding Pass

Full-viewport dark hero on the atmospheric sky photograph. Left column: GrandSlang italic at 146px for 'Your new', Whyte Inktrap weight 400 at 64px for the main 'Secure Web Gateway', GrandSlang italic again for 'with AI DLP'. Body subhead in Whyte Inktrap 20px weight 300, muted Almost White. Right column: 19.2px radius card with rgba(237,195,196,0.05) fill, 1px white border, 'Boarding Pass' label, 'LEGACY → DS' origin/destination line, and a vertical barcode. Two pill CTA buttons inside: 1584px radius, 20px 32px padding, white text on the faint pink wash.

### Stamped Section Heading

Whyte Inktrap Mono 74px weight 400, uppercase, 0.2em letter-spacing, Soft White (#f0f0f0). Rendered as a single line that fills the container. Each letter spaced far enough apart to read as a stamp, not a heading. No underline, no decoration — the tracking IS the design. Example: 'S S L   I N S P E C T I O N'.

### Filled Action Button

Background #090909, 1px solid #f7f9fa border, 8px radius, 16px all-around padding, white text in Whyte Inktrap 16px weight 400. Used for 'Book a Demo' and 'Log In' in the nav. The button is almost the same color as the page — the border does the work.

### Ghost Pill Button

Background rgba(237,195,196,0.05), no border, 1584px radius (effectively full pill), 20px 32px padding, text #f7f9fa. Example: 'Try now with Google' and 'Try now with Microsoft'. A small brand-color logo glyph sits left of the label.

### Compact Outlined Button

Background rgba(247,249,250,0.08), 1px solid #f7f9fa border, 6px radius, 9px 15px padding. Lighter density than the filled button — used in compact toolbars and table rows.

### Text-Only Nav Link

Transparent background, 0px radius, 10.4px vertical padding, text in #475467 (muted steel). Underline appears on hover. This is the lightest-weight interactive in the system — quiet enough to recede into the nav bar.

### Frosted Nav Bar

Fixed top bar, background rgba(51,50,72,0.7) (--nav-bg-color), backdrop-filter: blur(10px), 1px bottom border in #6b6b6b. Brand wordmark on the left in Whyte Inktrap weight 500. Nav items in Whyte Inktrap 12px uppercase with 0.07em tracking. The blur is the design — it lets the atmospheric hero breathe through.

### Comparison Card

19.2px radius, full-bleed gradient or violet bloom background, 40px padding, no border, no shadow. Each card carries a faint oversized number (01–04) behind a small label like 'COMPLEX 15-STEP CONFIGURATION' and a white 'vs. Competitor →' link. The cards are connected by a horizontal line and circular node markers between them, like a flight route.

### Feature Row Card

Transparent background, 19.2px radius, no padding. Left: 20px link 'Learn More'. Right: Whyte Inktrap 18px weight 400 body copy. The card IS the row — no visible container, the spacing creates the boundary.

### Violet Bloom Card

Background #af50ff or radial-gradient violet bloom, 19.2px radius, 40px padding. Used sparingly for the 'See how in 140s' play CTA or the 'dope.swg' badge. The violet is rationed to one or two cards per page — when it appears, it should feel like a signal, not a theme.

### Coordinate Footer

Full-bleed dark band, no background fill, 0px padding. Left: small '+' icon, 'Fly Direct' and 'Secure Web Gateway' labels in Whyte Inktrap 14px. Right: a live-updating GPS coordinate in Whyte Inktrap 14px + a heart icon. This is the signature: the brand writes its footer as if signing a postcard from a city.

### Hairline Divider

0.5px or 1px solid stroke in #f7f9fa at 10-20% opacity. Replaces shadows and heavy borders everywhere. The system trusts line weight, not depth, to create rhythm.

## Similar Design Systems

- {'why': 'Same dark monochrome canvas with a single saturated accent color rationed across the interface', 'business': 'Linear'}
- {'why': 'Identical shadowless discipline — flat surfaces, hairline borders, generous dark space — paired with a minimal typographic system', 'business': 'Vercel'}
- {'why': 'Same editorial display serif + geometric sans pairing, same luxury-product restraint on a dark canvas', 'business': 'Arc Browser'}
- {'why': 'Same boarding-pass / travel-coded editorial language, same extreme letter-spacing on uppercase stamps', 'business': 'Stripe Press'}
- {'why': 'Same dot-matrix mono typography and inktrap geometric sans, same monochrome-with-one-glow color strategy', 'business': 'Nothing.tech'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #f7f9fa
- background: #090909
- border: rgba(247,249,250,0.2)
- accent / brand signal: #af50ff
- muted text: #828384
- primary action: #af50ff (filled action)

**Example Component Prompts**

1. *Stamped Section Heading:* Render 'SSL INSPECTION' as a single line in Whyte Inktrap Mono, 74px, weight 400, uppercase, letter-spacing 0.2em, color #f0f0f0, on a #090909 background. No underline, no decoration.

2. *Hero Boarding Pass Card:* Create a right-aligned card on the hero, 19.2px radius, background rgba(237,195,196,0.05), 1px solid rgba(247,249,250,0.2) border, 40px padding. Inside: a small icon + 'Boarding Pass' label in Whyte Inktrap 12px uppercase, an 'ORIGIN LEGACY → DESTINATION DS' line in 14px, a Whyte Inktrap 32px heading 'Deploys on device in minutes', and two pill buttons (1584px radius, 20px 32px padding, white text, faint pink wash background) reading 'Try now with Google' and 'Try now with Microsoft'.

3. *Filled Action Button:* Build a 8px-radius button with #090909 background, 1px solid #f7f9fa border, 16px padding, white 'Book a Demo' text in Whyte Inktrap 16px weight 400.

4. *Violet Bloom Feature Card:* A 19.2px-radius card filled with #af50ff, 40px padding, containing Whyte Inktrap 32px weight 400 white heading 'dope.swg' and a 14px body line. One per page maximum.

5. *Coordinate Footer:* A full-width band on #090909 with a '+' icon, 'Fly Direct' and 'Secure Web Gateway' labels in Whyte Inktrap 14px on the left, a live GPS coordinate in 14px on the right, and a small heart icon in #f7f9fa.
