# ORYZO AI — Design System

> **North Star**: Darkroom product editorial. A lone object floating in warm darkness, cream typography the only decoration.
> **Theme**: dark
> **Source**: https://oryzo.ai
> **Refero Style**: https://styles.refero.design/style/1f204e95-454a-437e-845b-c1b169d35607
> **Synced**: 2026-09-01

## Overview

The ORYZO visual system treats a single product object like a museum artifact: full-bleed warm-dark canvas, cream typography floating in generous negative space, and zero UI chrome competing with the form. Every text element is uppercase at weight 500, with the sole exception of body copy at 29px/400 which is the system's only conversational voice. A single vivid orange appears only for credit lines and the studio link — never for buttons or CTAs — earning its rarity. The layout alternates between two modes: photographic hero (the product in context with tools and materials) and void-mode reveal (the product isolated on warm dark), connected by hairline dashed dividers and pill-shaped controls.

## Color Palette

- **Warm Cream**: `#ffedd7` — Light text on dark surfaces, inverse labels, and high-contrast captions. [neutral]
- **Walnut Shadow**: `#100904` — Page canvas and deepest background — warm near-black, not pure black. The void behind every product reveal [neutral]
- **Bark Brown**: `#382416` — Elevated surface and filled button background — the one chromatic step above the canvas, used for the single solid CTA [neutral]
- **Cork Border**: `#40372e` — Hairline dividers, dashed section separators, subtle container borders — warmer than the canvas by one step [neutral]
- **Driftwood**: `#6c5f51` — Mid-tone warm gray for secondary dividers and muted structural elements — the bridge between Bark and Cream [neutral]
- **Ember Accent**: `#dc5000` — Orange text accent for links, tags, and emphasized short phrases. [accent]
- **Pure Black**: `#000000` — SVG icon fills and decorative vector elements only — never used as a background or text color [neutral]

## Typography

- **halyard-display-variable**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| subheading | 18 | — | 1 |
| heading-sm | 24 | — | 1.09 |
| body | 29 | — | 1.26 |
| heading | 41 | — | 0.9 |
| display | 51 | — | 0.9 |

## Spacing & Layout

- **Card Padding**: 24px
- **Element Gap**: 18px
- **Border Radius**: {'cards': '12px', 'inputs': '0px', 'full-round': '9999px', 'buttons-pill': '36px', 'buttons-outlined': '22.5px'}

## Layout

Full-bleed throughout — no max-width container, every section spans 100vw. Hero: full-viewport top-down photograph with a massive ORYZO wordmark (51px+) in the upper-left, tagline above, fixed minimal nav upper-right, vertical sidebar label running down the right edge, semi-transparent info card lower-left, video thumbnail lower-right. Subsequent sections: full-viewport Walnut Shadow canvas with a centered 3D product render flanked by left-aligned heading and right-aligned body copy — a three-column grid (text / object / text) with generous 18px gutters. Section transitions are seamless dark-on-dark; the only breaks are hairline dashed dividers. Navigation is fixed, transparent, and 4 items max. No sidebar, no footer chrome, no cards-within-cards — every screen is a single statement.

## Surfaces / Elevation

- **Walnut Shadow**
- **Bark Brown**
- **Cork Border**
- **Warm Cream**

## Imagery

Photography is editorial, top-down, and in-context: the cork coaster sits on a green cutting mat surrounded by pencils, a craft knife, and a paperclip — tools of the craft visible in frame. The green cutting mat (#445231) is a hero-only element, not a UI token. 3D renders dominate the product reveal sections: the cork coaster is shown isolated against Walnut Shadow, lit from the upper right with a warm rim light, rotating from top-down to 3/4 angle between sections. No lifestyle photography, no people, no stock imagery — the object is the hero and the tools are its context. Images are full-bleed, sharp-edged (no rounded masks), and treated with high contrast and warm grading.

## Design Principles

### Do

- Set all UI text in #ffedd7 (Warm Cream) — never use pure #fff; the warm tint is the system's signature.
- Use #dc5000 (Ember) only for credit lines, the "Built by" label, and the Lusion studio link — a single accent earns its rarity through restraint.
- Set type in uppercase weight 500 across the entire interface; use weight 400 / mixed case only for the 29px body copy that explains the product.
- Use 36px border-radius for the one filled CTA and 22.5px for outlined ghost buttons; 12px for cards; 0px for inputs and inline links — these four values are the entire radius vocabulary.
- Set section gaps at 100vh — each section gets its own full viewport, never compress product reveals into bands.
- Use 1px dashed lines in #40372 for section dividers; avoid solid dividers and avoid any divider thicker than 2px.
- Center the 3D product render in every void-mode section with text flanking symmetrically left and right at 18px gutters.

### Don't

- Never use pure #fff for text or #000 for backgrounds — the warm cream and walnut shadow are the system; purity reads as wrong here.
- Never apply #dc5000 to buttons, CTAs, or interactive surfaces — the orange is editorial credit only.
- Never use lowercase or sentence-case for headings, nav, or labels; the only mixed-case text is the 29px body description.
- Never add drop shadows to cards, buttons, or sections — depth comes from the two-step surface stack (#100904 → #382416), not from blur.
- Never use border-radius below 12px on containers — the geometry is deliberately chunky, not sharp.
- Never use more than one filled button per section; restraint is the design language.
- Never center-align body copy — headings and body text are always left-aligned, even when flanking a centered image.

## Components

### Pill Button (Filled)

36px border-radius, Bark Brown (#382416) background, Warm Cream (#ffedd7) text, 14px 24px vertical/horizontal padding, weight 500, uppercase, 8–14px size. The only filled action surface in the system — its rarity is the signal.

### Outlined Ghost Button

22.5px border-radius, transparent background, 1px Warm Cream border, Warm Cream text, 7.5px vertical padding, 0px horizontal padding, weight 500, uppercase, 8–14px. Border does the work; no fill needed.

### Underline Text Link

0px radius, transparent background, Warm Cream text, 0px padding, weight 500, uppercase, 12–14px. The default interaction — no container, just text with an underline indicator.

### Input Field (Underline Only)

0px radius, transparent background, 1px Warm Cream bottom border, Warm Cream text, 1px 2px padding, 36px right padding for an inline action. The form mirrors the ghost-button restraint — no boxes, just a line.

### Fixed Top Navigation

Logo wordmark "ORYZO" left-aligned in Warm Cream at 12–14px weight 500 uppercase. Right-aligned nav items: INTRO (with dashed underline indicator for active), FEATURES, PRODUCT, CONTACT — all 12px weight 500 uppercase, Warm Cream. Transparent background over the hero photograph.

### Vertical Sidebar Label

Rotated 90° text "ORYZO 1-MODEL" in Warm Cream, 10–12px uppercase, sits flush right. Functions as a product serial number — a physical-product artifact translated to UI.

### Logo Wordmark

"ORYZO" in Halyard Display Variable weight 500 uppercase, up to 51px+ at display scale with 0.9 line-height. Used at two sizes: navigation lockup (12–14px) and hero lockup (51px+). No icon, no symbol — pure typographic identity.

### Hero Overlay Info Card

12px border-radius, semi-transparent Warm Cream or dark fill with low opacity, contains uppercase heading "DESIGNED BY LUSION, THE AWARD-WINNING DESIGN STUDIO." plus a dashed divider and body text. Overlays the hero photograph bottom-left.

### Product Reveal Section

100vh height, Walnut Shadow (#100904) background, centered 3D product render, left-aligned heading at 41px uppercase "ISN'T JUST A COASTER.", right-aligned body copy at 29px weight 400 mixed-case. The signature layout pattern — three columns, generous gutters.

### Section Divider (Dashed Hairline)

1px dashed line in Cork Border (#40372e) or Driftwood (#6c5f51). Used sparingly between text blocks, never as decoration — always carrying structural meaning.

### Video Thumbnail Card

Small rectangular card, 12px radius, positioned in the lower-right of the hero. Contains a miniature ORYZO wordmark and a play icon. Functions as a secondary entry point without competing with the primary CTA.

### Legal/Disclaimer Text

Fallback font (Arial 8px weight 500 uppercase) for things like "* ADOBE ILLUSTRATOR" footnotes. Visually subordinate — intentionally uses a different typeface to signal "this is not design, this is compliance."

## Similar Design Systems

- {'why': 'Same warm-dark editorial canvas, single-product hero treatment, pill-button controls, and 3D product renders as the visual centerpiece', 'business': 'Lusion (the studio credited in the design)'}
- {'why': 'Full-bleed dark mode with a single interactive 3D object commanding the viewport, minimal UI chrome, and oversized uppercase type', 'business': 'Active Theory'}
- {'why': 'Editorial product-showcase sites with top-down craft photography, warm grading, and typography that steps back to let the object speak', 'business': 'Resn'}
- {'why': 'Studio portfolio sites that treat a single concept object with museum-presentation gravity — dark void, cream labels, generous negative space', 'business': 'Tool of North America'}
- {'why': 'Work-reveal layouts that alternate between photographic context and isolated product renders against near-black backgrounds', 'business': 'Buck (studio)'}

## Typography Voice

The system has exactly two typographic modes:

1. UPPERCASE WEIGHT 500 — the default for everything: nav, headings, labels, links, button text, legal. The voice is declarative, confident, museum-label. Sizes range from 8px (legal) to 51px (display). Line-height tightens with size: 1.2 at caption, 1.0 at body-sm, 0.9 at display. No letter-spacing adjustment — the font's geometry is tight enough at every scale.

2. MIXED CASE WEIGHT 400 — the exception, used only at 29px for the descriptive body copy that explains the product. This is the system's only conversational voice: "Designed to lift, insulate, and grip in all the right ways. Oryzo makes the simplest moment feel considered." The weight drop and case change are the signal — when the text shifts from 500/UPPER to 400/mixed, the user knows they are reading description, not label.

The bold signature: line-height 0.9 at 41–51px display sizes. This is unusually tight — most editorial sites use 1.0–1.1. At 0.9, the uppercase letterforms overlap their line-height bounds, creating a sculptural block effect. The display type doesn't sit in lines; it stacks as solid form.

## Agent Prompt Guide

## Quick Color Reference
- text: #ffedd7 (Warm Cream)
- background: #100904 (Walnut Shadow)
- surface: #382416 (Bark Brown)
- border: #40372e (Cork Border)
- accent: #dc5000 (Ember)
- primary action: no distinct CTA color

## 3-5 Example Component Prompts

1. **Hero Lockup:** Full-bleed Walnut Shadow (#100904) canvas. ORYZO wordmark at 51px Halyard Display Variable weight 500 uppercase, line-height 0.9, color #ffedd7, positioned upper-left with 24px margin. Tagline "MADE FOR MUGS, BUILT FOR TABLES." at 12px weight 500 uppercase above the wordmark, also #ffedd7.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

3. **Ghost Outline Button:** Transparent background, 1px Warm Cream (#ffedd7) border, 22.5px border-radius, 7.5px vertical padding, Warm Cream text at 12px weight 500 uppercase. The secondary action vocabulary.

4. **Product Reveal Section:** Full-viewport (100vh) Walnut Shadow (#100904) background. Centered 3D product render occupying the middle 40% of width. Left column: heading "ISN'T JUST A COASTER." at 41px weight 500 uppercase, line-height 0.9, #ffedd7, left-aligned. Right column: body copy at 29px weight 400 mixed-case, line-height 1.26, #ffedd7, left-aligned within the column. 18px gutter between the centered object and each text column.

5. **Top Navigation:** Fixed position, transparent background, full-width. Left: ORYZO wordmark at 12px Halyard weight 500 uppercase #ffedd7. Right: four nav items (INTRO, FEATURES, PRODUCT, CONTACT) at 12px weight 500 uppercase #ffedd7, with a 1px dashed #40372e underline beneath the active item.
