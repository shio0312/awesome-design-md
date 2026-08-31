# Gsap — Design System

> **North Star**: animated chalkboard in a design studio. A near-black wall, warm cream chalk, and five color-coded highlighters — one for each animation discipline.
> **Theme**: dark
> **Source**: https://gsap.com
> **Refero Style**: https://styles.refero.design/style/00537a20-e99e-4ef2-b119-c6f532c44cc9
> **Synced**: 2026-09-01

## Overview

GSAP is a dark-canvas design language built for a motion library: a near-black stage where massive cream type, thin outlined pill buttons, and individually color-coded category labels create a typographic showcase rather than a traditional marketing site. The system runs on a single warm cream surface color (#fffce1) against an almost-black background, with category words each wearing their own vivid hue (green for the brand mark, orange for SVG, pink for Scroll, violet for Text, blue for UI) — color functions as taxonomy, not decoration. Typography is the hero: a single sans-serif (Mori) at six weights, pushing to 224px for the main headline with aggressive negative tracking and near-1.0 line-height, so words feel carved rather than laid out. Buttons are almost exclusively ghost-pills with 100px radius and hairline cream borders; there are no filled CTAs, which lets the gradient hero flourish and keeps every interactive element weightless.

## Color Palette

- **Just Black**: `#0e100f` — Page canvas, footer surface, deep section backgrounds [neutral]
- **Surface Cream**: `#fffce1` — Primary text, outlined button borders, nav links, card text, the default surface-light used for ghost controls and headings [neutral]
- **Surface 50**: `#7c7c6f` — Muted secondary text, icon fills at rest, subhead annotations, disabled-state labels [neutral]
- **Surface 25**: `#42433d` — Hairline borders, dividers, low-contrast outlines against the black canvas [neutral]
- **Off Black**: `#191919` — Alternative dark surface for nested panels and code blocks [neutral]
- **Shockingly Green**: `#0ae448` — Green text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Light Green**: `#abff84` — Green text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Orangey**: `#ff8709` — SVG category label, orange-tool icon fills, gradient endpoint in Orange Crush [accent]
- **Pink**: `#fec5fb` — Scroll category label, decorative splashes, gradient endpoint in Summer Fair [accent]
- **Lilac**: `#9d95ff` — Text category label, thin illustrative strokes, gradient endpoint in Purple Haze [accent]
- **Blue**: `#00bae2` — UI category label, gradient endpoint in Skyfall and Emerald City [accent]
- **Core Green**: `#dfffd1` — Subtle brand-tinted background washes for feature cards tied to the GSAP core [brand]
- **Lipstick Pink**: `#f100cb` — Deep gradient stop for expressive decorative gradients, not used for text or UI [accent]

## Typography

- **Mori**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.4 |
| body-sm | 16 | — | 1.15 |
| body | 19 | — | 1.15 |
| body-lg | 23 | — | 1.38 |
| subheading | 34 | — | 1.2 |
| heading-sm | 44 | — | 1.2 |
| heading | 66 | — | 1.2 |
| heading-lg | 101 | — | 1 |
| display | 224 | — | 0.9 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 24px
- **Element Gap**: 16px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '8px', 'pills': '9999px', 'buttons': '100px', 'smallTags': '8px'}

## Layout

The page is full-bleed against a single dark canvas, with content generally respecting a ~1280px max-width and generous 80–120px section gaps. The hero is intentionally edge-bleeding: a 224px headline wraps across two lines, decorative 3D shapes overlap the type, and a curly-bracket annotation plus a single outlined CTA sit in the lower third. Subsequent sections follow a repeating pattern: a curly-bracket eyebrow, then either a centered two-to-three-line headline or a two-column row (large organic illustration left, category label + subhead + body + pill button right). Sections are separated by 1px #42433d hairlines that span the full content width. The Tools section stacks four such two-column blocks vertically. The Showcase section introduces a 2–3 column card grid with 24px gaps. Navigation is a single top bar with tight 6–16px link spacing, cream 16px Mori 400 text, and the wordmark on the far left. The footer shifts to a slightly lighter #191916 surface with multi-column link lists and 60–80px vertical padding.

## Surfaces / Elevation

- **Canvas**
- **Nested Panel**
- **Cream Surface**

**Shadow tokens:**

## Imagery

Imagery is dominated by soft 3D-rendered organic shapes — pills, domes, liquid blobs, abstract splashes — rendered with multi-stop gradients in the discipline accent colors (e.g. pink-to-blue for Scroll, orange-to-amber for SVG). No photography of people or places appears. The shapes are loosely contained and intentionally overlap adjacent type to suggest motion, which aligns with the product's purpose. Icons in the nav are monochrome cream and stroked at roughly 1.5px. Backgrounds are always the flat dark canvas; visual richness comes from foreground shapes and gradient typography, not from photographic content.

## Design Principles

### Do

- Set body text and all primary UI in Mori weight 400 at 16–19px with line-height 1.15; this is the system's resting rhythm.
- Use the five-discipline color mapping (Green = GSAP, Orange = SVG, Pink = Scroll, Violet = Text, Blue = UI) for every category label — never reuse a color for a different discipline.
- Render every button as a 100px-radius ghost pill with a 1px cream border and #fffce1 text at Mori 600 18px; the only exception is the primary CTA, which uses a 1.5px green-to-light-green gradient stroke.
- Push the hero headline to 224px weight 600 with line-height 0.9 and -0.02em tracking; let it bleed to the viewport edge rather than centering it inside a max-width container.
- Introduce every section with a curly-bracket annotation in `{ }` at 16–19px Mori 400 — this bracket pair is the site's recurring signature.
- Place a 1px #42433d hairline divider between tool feature blocks, full section width, with no padding around it.

### Don't

- Don't add filled, solid-color CTA buttons — the system is outlined-only; the gradient-stroked pill is the maximum chromatic escalation allowed.
- Don't use pure white (#ffffff) for text or #000000 for the background — the warmth of #fffce1 cream and #0e100f off-black is what gives the system its character.
- Don't set body type below 14px or above 23px; the type scale is binary between editorial display (66–224px) and compact UI (14–23px).
- Don't introduce new category colors beyond the five-discipline palette; adding a sixth color dilutes the taxonomy that makes the system legible.
- Don't apply drop shadows to cards or illustrations — depth is communicated only through gradient washes and surface-step shifts, never via box-shadow.
- Don't break the cream-on-black pairing with reversed (cream background, black text) cards unless the design calls for a deliberate callout; the dark canvas should remain unbroken across the scroll.
- Don't use Inter, Roboto, or system sans defaults; the Mori humanist warmth is load-bearing, and a geometric substitute collapses the editorial tone.

## Components

### Outlined Cream Pill Button

Transparent background, #fffce1 text and 1px cream border, 100px border-radius, 15px vertical and 24px horizontal padding, Mori 18px weight 600 lh 1.05. Used for 'Tools', 'Explore Scroll', 'Explore SVG', 'Explore Text', 'Explore UI', 'Explore All Showcases'. The 100px radius plus thin border gives a high-tech, minimal-control feel; never fill these with color.

### Ghost Nav Link

No background, no border, #fffce1 or #7c7c6f text at 16px Mori 400 lh 1.15. Underline on hover via color shift to #fffce1. Nav row gap 6px, vertical padding 10px. Group spacing tight (6–16px) to keep the nav bar compact and editorial.

### Gradient-Stroked CTA Pill

Ghost button (transparent fill) with a 1.5–2px gradient border from #0ae448 to #abff84 along 114.41deg, cream text, 100px radius, 15px/24px padding. Implemented via the --color-core-button-gradient token on the border or as a border-image. This is the only chromatic control in the system; it carries the brand green and reads as 'actionable' without violating the outlined-only rule.

### Borderless Icon Button

Fully round (50% radius), no background, cream icon, 0px padding. Used sparingly for icon-only controls like the mobile menu trigger.

### Category Color Label

Mori 19–24px weight 400, single-word, rendered in a discipline-specific hue: Scroll #fec5fb, SVG #ff8709, Text #9d95ff, UI #00bae2, GSAP #0ae448, Other #abff84. Functions as the visual anchor for each section and appears as both a heading label and a nav item in the same hue. The color-to-discipline mapping is the site's signature taxonomy.

### Announcement Banner

Full-bleed band, cream text on near-black, centered single line at 14px Mori 400. Optional inline link rendered in Shockingly Green #0ae448. Sits at 0–40px from the top of the viewport and never carries a background tint.

### Hero Display Headline

Mori weight 600, 224px, line-height 0.9, letter-spacing -0.02em (-4.48px), color #fffce1. The headline wraps across two lines and is allowed to bleed into the viewport edge; no max-width container. Decorative organic splashes (pinks, oranges, greens) overlap the type rather than sitting beside it.

### Curly-Bracket Annotation

Small 16–19px Mori 400 cream text wrapped in literal curly braces `{ }`. Functions as a typographic signature — every section is introduced by this bracket pair. No background, no border; the brackets are the visual system.

### Tool Feature Block

Two-column row inside the Tools section: left side holds a large soft-rendered 3D-style shape in the tool's accent color (with internal gradient and ambient lighting); right side holds the category label in its hue, a 34–44px cream subhead, body copy at 23px, and an outlined cream pill 'Explore' button. Divided from the next block by a 1px #42433d hairline that spans the section width.

### 3D Organic Illustration

Soft 3D shapes (pill, dome, liquid blob) rendered with multi-stop gradients — typically a tool's accent color graduating into a lighter tint (e.g. blue-to-pink for Scroll, orange-to-amber for SVG). No drop shadows on the canvas; the shapes are lit from within via gradient. Containment is loose; they overlap adjacent type rather than respecting a frame.

### Footer

Off-black #191919 background, 1px #42433d top divider, multi-column nav with cream links at 16px Mori 400, generous 60–80px vertical padding. Includes the GSAP wordmark, link columns, and social/secondary nav. The footer shifts one surface step lighter than the page, creating a subtle terminator.

### Showcase Card

Near-black surface with 8px corner radius, cream heading at 24–33px, no visible border, and a contained 16:9 or 1:1 preview area. Sits in a 2–3 column grid with 24px gaps. Padding 24px on all sides; preview art overflows the card slightly to suggest motion.

## Similar Design Systems

- {'why': 'Same single-dark-canvas treatment with massive display headlines and outlined ghost controls; both lean on typographic scale rather than color to create hierarchy.', 'business': 'Framer'}
- {'why': 'Dark UI with a single chromatic accent reserved for the primary action, and category-level color coding for navigation items.', 'business': 'Linear'}
- {'why': 'Near-black canvas, cream/off-white type, hairline section dividers, and an outlined-only button system that never uses solid fills.', 'business': 'Vercel'}
- {'why': 'Shares the editorial-display headline scale (100–200px) and the warm cream-on-dark palette, plus the sponsor-bys relationship GSAP has with Webflow.', 'business': 'Webflow'}
- {'why': 'Both feature soft 3D organic shapes as primary imagery, rendered with internal multi-stop gradients that simulate ambient lighting rather than drop shadows.', 'business': 'Spline'}

## Agent Prompt Guide

## Quick Color Reference
- Background: #0e100f
- Text: #fffce1 (primary), #7c7c6f (muted)
- Border: #42433d (hairline dividers), #fffce1 (outlined buttons)
- Accent (GSAP brand): #0ae448
- Accent (discipline labels): #fec5fb Scroll, #ff8709 SVG, #9d95ff Text, #00bae2 UI
- primary action: no distinct CTA color

## Example Component Prompts
1. **Hero Headline**: Create a full-bleed section on #0e100f with a two-line headline at 224px Mori weight 600, line-height 0.9, letter-spacing -4.48px, color #fffce1. A soft pink-to-blue gradient 3D blob overlaps the right edge of the second line. No max-width container; let the type breathe to the viewport edge.

2. **Outlined Explore Button**: A pill button with 100px border-radius, 1px solid #fffce1 border, transparent fill, text 'Explore Scroll' at 18px Mori 600 lh 1.05 in #fffce1, padding 15px vertical / 24px horizontal. No hover fill — only a 1px shift to opacity 0.8 on the border.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

4. **Tool Feature Block**: Two-column row at 1280px max-width, 80px vertical gap. Left column holds a 480px soft 3D dome with a linear gradient from #fec5fb to #00bae2. Right column starts with '{ GSAP® Tools }' in 16px Mori 400 #fffce1, then 'Scroll' at 19px Mori 400 #fec5fb, then a 44px Mori 600 #fffce1 subhead, then a 23px Mori 400 #fffce1 body paragraph, then the outlined explore button.

5. **Category Label Pill**: A single word 'SVG' at 34px Mori 600 lh 1.0 in #ff8709, no background, no border. Functions as the section anchor — appears identically sized in both the section header and the corresponding nav item.
