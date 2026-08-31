# Seed — Design System

> **North Star**: living organism under laboratory glass
> **Theme**: light
> **Source**: https://seed.com
> **Refero Style**: https://styles.refero.design/style/cd723d5a-e7ea-4e4c-a3bb-6cf56e05057a
> **Synced**: 2026-09-01

## Overview

Seed uses a botanical-clinical language: warm snow-white canvas, deep forest green surfaces, and whisper-light headline weights (300–350) that read more like a peer-reviewed journal than a supplement brand. The palette is almost monochrome — 93% achromatic — with a single vivid lime (#d3fa99) used as functional punctuation for badges and 'New' tags. Components are deliberately weightless: pill-shaped controls, 16px-radius cards, no drop shadows, no gradients, no decorative borders. The visual restraint IS the brand — scientific credibility earned through typographic confidence and chromatic silence, not through visual volume.

## Color Palette

- **Forest Depths**: `#1c3a13` — Primary brand color — filled CTAs, dark section backgrounds, navigation surfaces, and primary body text. A near-black green that reads as ink on snow-white and as depth in dark sections [brand]
- **Lime Pulse**: `#d3fa99` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. [accent]
- **Sage Moss**: `#757c5d` — Product variant accent — DM-02 Daily Multivitamin card and supporting elements. Muted green that harmonizes with Forest Depths without competing [accent]
- **Olive Gold**: `#9f995b` — Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. [accent]
- **Eucalyptus**: `#698e79` — Product variant accent — PM-02 Sleep + Restore card and supporting elements. Cooler green-blue for the evening product [accent]
- **Snow White**: `#fcfcf7` — Page canvas, card surfaces, button text, and primary inverse text. A warm off-white (not pure white) that softens the high-contrast dark green and reads organic rather than clinical-sterile [neutral]
- **Warm Stone**: `#eeeee9` — Secondary surface — alternating section backgrounds, subtle panels, and muted separators. Sits between Snow White and the dark sections to create quiet rhythm [neutral]
- **Frosted Glass**: `#c4c7c4` — Translucent surface and frosted-glass overlay backgrounds (used with backdrop-filter: blur). Also serves as a muted neutral surface for content cards on white sections [neutral]
- **Ash**: `#b3b3b3` — Disabled button backgrounds, muted button states, and low-emphasis borders [neutral]
- **Pewter**: `#666666` — Secondary body text, captions, and low-emphasis helper text. Provides one tier of text de-emphasis below primary Forest Depths [neutral]
- **Ink**: `#000000` — Primary body text on light sections where maximum contrast is needed. Used sparingly — most text defaults to Forest Depths for tonal warmth [neutral]

## Typography

- **Seed Sans**
- **Seed Sans Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| micro | 10 | — | 1 |
| label | 12 | — | 1.5 |
| caption | 14 | — | 1.4 |
| body-sm | 16 | — | 1.5 |
| body | 18 | — | 1.3 |
| subheading | 24 | — | 1.2 |
| heading-sm | 32 | — | 1.5 |
| heading | 36 | — | 1 |
| heading-lg | 40 | — | 1.1 |
| display | 48 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'cards': '16px', 'badges': '1000px', 'inputs': '8px', 'buttons': '1000px', 'large-cards': '32px'}

## Layout

The page uses a max-width 1200px centered grid with consistent 24px horizontal page margins. The hero is a full-bleed lifestyle photograph with left-aligned headline overlay (text-left/image-right at ~50/50 split). Below the hero, sections alternate between Snow White and Forest Depths backgrounds at full-bleed width, creating dramatic dark/light rhythm. The product showcase section uses a 4-column equal-width card grid with equal gutters (16px row/column gap). Content sections use a 2-column asymmetric layout: ~40% text-left, ~60% image-right with generous 64–96px vertical padding. Navigation is a sticky top bar (64–80px) with horizontal link distribution. Section gaps are large (64–96px) creating spacious, editorial breathing room. The overall density is low — the page prioritizes typographic and photographic impact over information density.

## Surfaces / Elevation

- **Page Canvas**
- **Card Surface**
- **Dark Section**
- **Accent Highlight**

## Imagery

Imagery is high-key, naturalistic product photography: supplement jars photographed on organic surfaces (wooden counters, natural light) with shallow depth of field and soft bokeh backgrounds. The product jars themselves are frosted glass with colored contents (dark green for DS-01, olive for AM-02, sage for DM-02, eucalyptus for PM-02) and minimal labeling. The photography style is editorial-science — closer to a Kinfolk magazine spread than a CPG ad. No lifestyle people, no staged scenarios, no stock photography. The second key visual element is a delicate, organic line illustration of branching microbiome structures in muted green — used in science sections to visualize biological concepts with scientific-journal precision. Icons appear to be custom thin-stroke line icons, monochrome in Forest Depths or Snow White depending on background.

## Design Principles

### Do

- Use Forest Depths (#1c3a13) for all primary CTAs, dark sections, and primary text — it is the only chromatic authority on the page
- Use weight 300–350 for all display and heading text (32px and above); reserve weight 400–500 for body, buttons, and labels
- Apply Lime Pulse (#d3fa99) only for sale badges, highlight pills, and small functional emphasis — never for backgrounds larger than a badge or for body text
- Use 1000px border-radius for all buttons, badges, tags, and pill-shaped elements — the fully rounded shape is a defining visual signature
- Set section backgrounds to either Snow White (#fcfcf7) or Forest Depths (#1c3a13) — avoid introducing intermediate surface colors
- Apply the -0.015em to -0.02em letter-spacing tightening at all display sizes (24px and above) to match the brand's refined, journal-like typographic texture
- Use Seed Sans Mono for all product codes (DS-01®, DM-02™) and ingredient/spec lists to reinforce the clinical-scientific tone

### Don't

- Do not introduce drop shadows, box-shadows, or elevation effects — the design is intentionally flat; shadows would break the weightless aesthetic
- Do not use gradients of any kind — the system is purely flat color fields, including on CTAs and hero sections
- Do not use weight 600+ for headlines — bold or black weights would shatter the whisper-light, scientific-journal voice
- Do not use saturated colors outside the five accent greens (#1c3a13, #d3fa99, #757c5d, #9f995b, #698e79) — no blues, reds, or purples in the brand system
- Do not use pure white (#ffffff) — always use Snow White (#fcfcf7); the warm tint is what makes the palette feel organic rather than clinical
- Do not use square or 4–8px radii on buttons or badges — the pill shape (1000px) is non-negotiable for primary interactive elements
- Do not fill large areas with Lime Pulse (#d3fa99) — it is an accent color, not a surface; confine it to badges and small emphasis elements

## Components

### Primary Filled Button

Pill-shaped (1000px radius), Forest Depths (#1c3a13) background, Snow White (#fcfcf7) text, Seed Sans 16px/400. Padding 16px vertical × 24px horizontal. No border, no shadow. This is the only filled button style and carries the highest visual weight on the page.

### Ghost Outlined Button

Transparent background, 1.5px solid Snow White (#fcfcf7) border, Snow White text, 1000px radius, 16px/24px padding. Used for 'Sign in' and actions over imagery or dark green sections.

### Inverted Light Button

Snow White (#fcfcf7) background, 1.5px solid Forest Depths (#1c3a13) border, Forest Depths text, 1000px radius, 16px/24px padding. Mirrors the ghost button for light-surface contexts.

### Text Link with Arrow

No background, no border, 0px radius. Forest Depths text, 1.5px solid underline, 7px/10.5px padding. Appended with a right-arrow glyph (→) for 'Shop Now', 'Shop All', 'Shop Sale' style links.

### Sale Badge

Lime Pulse (#d3fa99) background, Forest Depths text, 1000px radius, 6px vertical × 8px horizontal padding. The only badge style using the vivid accent color. Small but immediately scannable.

### Product Tag Badge

Translucent Snow White background (rgba(252,252,247,0.2)), Snow White text, 1000px radius, 6px/8px padding. Sits on the top-left of product cards over the product photo.

### Product Card (Dark Section)

Transparent background within the dark green section, 16px border-radius, no shadow, no border. Contains: product code in pill outline, product name (Seed Sans 24px/350), product photo, 'Shop Now' button, and price text (Seed Sans 12px/500 uppercase). Cards sit directly on the dark surface with no visible container.

### Feature Card (Light Section)

Transparent or Frosted Glass (#c4c7c4) background, 16px border-radius, no shadow. Used for science modules, ingredient breakdowns, and quiz steps. Frosted Glass variant uses backdrop-filter: blur(37.5px) for an apothecary-glass effect.

### Navigation Bar

Full-width Snow White background, sticky. Left: 'Seed' wordmark + green dot accent. Center/left: nav links (Shop, Science, Learn). Right: 'Sign in' ghost button + 'Get Started' primary filled button. Height 64–80px. Horizontal padding 24–48px.

### Promo Banner

Full-bleed thin band at the very top (40px height). Snow White background, Forest Depths text, 12px/500 uppercase Seed Sans. Contains a small icon + short announcement + inline link.

### Input Field

Transparent background, 1.5px solid Snow White border, Snow White text, 8px border-radius, 14px/20px padding. Placeholder text in semi-transparent Snow White. Used on dark green sections only.

### Product Code Pill

1.5px solid outline in Snow White or Forest Depths (depending on background), 1000px radius, 6px/8px padding. Text in Seed Sans 12px/500. The outline + pill combo creates a 'specimen label' aesthetic.

## Similar Design Systems

- {'why': 'Same near-monochrome palette (deep brown/green + warm off-white), whisper-light serif/sans headlines, and pill-shaped minimal buttons with scientific-apothecary restraint', 'business': 'Aesop'}
- {'why': 'Same flat-design approach with no shadows, generous whitespace, and a single dominant brand color applied as full-bleed dark sections alternating with white', 'business': 'Allbirds'}
- {'why': 'Same light display weights at large sizes creating a conversational, non-corporate headline voice, paired with pill buttons and flat surfaces', 'business': 'Oatly'}
- {'why': 'Same dark-band-meets-white-section alternating rhythm with tight typographic tracking and product-forward card grids on saturated dark backgrounds', 'business': 'Whoop'}
- {'why': 'Same pill-button system, full-bleed dark product sections with white text, and botanical/clinical brand positioning expressed through restrained color use', 'business': 'Hims'}

## Agent Prompt Guide

## Quick Color Reference
- Primary text: #1c3a13 (Forest Depths)
- Page background: #fcfcf7 (Snow White)
- Dark section background: #1c3a13 (Forest Depths)
- Accent / badge: #d3fa99 (Lime Pulse)
- Secondary surface: #eeeee9 (Warm Stone)
- primary action: #1c3a13 (filled action)

## Example Component Prompts

1. **Primary CTA Button**: Create a pill button with 1000px border-radius, background #1c3a13 (Forest Depths), text #fcfcf7 (Snow White), Seed Sans 16px weight 400, padding 16px vertical × 24px horizontal. No border, no shadow. Use for all main calls-to-action.

2. **Hero Headline**: Set a display headline at 48px in Seed Sans weight 350, color #1c3a13, line-height 1.1, letter-spacing -0.72px. Pair with body text at 16px weight 400 in #1c3a13, line-height 1.5. The whisper-light weight at display size is the signature.

3. **Product Card**: Build a card on a Forest Depths (#1c3a13) section background. 16px border-radius, no shadow, no visible border. Include a product code pill (1.5px solid #fcfcf7 outline, 1000px radius, 12px/500 uppercase text), product name in Seed Sans 24px/350 in #fcfcf7, a product jar image, and a 'Shop Now' primary filled button.

4. **Sale Badge**: Create a small pill badge: 1000px radius, background #d3fa99 (Lime Pulse), text #1c3a13 (Forest Depths) in Seed Sans 12px weight 500, padding 6px vertical × 8px horizontal. Place top-left on promotional cards.

5. **Dark Section with Content**: Build a full-bleed section with #1c3a13 background. Left column (40%): heading in Seed Sans 40px/350 in #fcfcf7, subtext in 16px/400 in #fcfcf7, and a ghost button (transparent bg, 1.5px solid #fcfcf7 border, #fcfcf7 text, 1000px radius). Right column (60%): scientific illustration or product image.

## Color Philosophy

The palette is built on a single chromatic pillar (Forest Depths #1c3a13) supported by one warm neutral (Snow White #fcfcf7) and one vivid accent (Lime Pulse #d3fa99). The deep green is so dark it reads as near-black, giving the brand the gravity of black-on-white editorial design while maintaining botanical identity. Lime Pulse is the only color that feels 'switched on' — it appears only where the system needs to shout (sales, newness, emphasis). This extreme restraint (93% achromatic content) is the visual argument: a microbiome brand that trusts science over marketing spectacle.

## Typography Philosophy

Seed Sans at weights 300–350 for display sizes is the most distinctive typographic choice. At 40–48px, weight 350 creates a 'whisper headline' effect — the text is present and authoritative but never aggressive. The tight letter-spacing (-0.72px at 48px) pulls the light strokes together, preventing them from looking anemic. The contrast between whisper-light headlines and confident 400-weight body text creates a dual-voice system: science journal (headlines) meets clinical reference (body). The custom 'ss05' stylistic set should always be enabled.
