# Flowmapp — Design System

> **North Star**: White blueprint desk with one blue pen
> **Theme**: light
> **Source**: https://flowmapp.com
> **Refero Style**: https://styles.refero.design/style/caca412f-7fc7-4510-aacc-5664d4f8ce9f
> **Synced**: 2026-09-01

## Overview

Flowmapp uses a bright, airy, almost lab-notebook language: near-pure white canvas, oversized bold black headlines, pill-shaped blue CTAs, and a constellation of small floating product mockups that act as proof rather than decoration. The system relies on a single vivid blue (#0080ff) as the only saturated signal, with everything else staying achromatic or near-gray so that color reads as action, not as noise. Shapes are aggressively rounded — cards arc at 20–32px, buttons and tags become full pills at 1600px, and the hero CTA even has a hand-drawn wavy tail that makes the primary action feel sketched rather than templated. Layout is max-width contained with generous breathing room; content is broken by small product screenshots, floating UI fragments, and a row of pastel circular icon badges that punctuate long-form copy.

## Color Palette

- **Signal Blue**: `#0080ff` — Blue supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Voltage Violet**: `#0050ff` — Decorative card border glow, hero gradient bloom, chromatic outline accents on floating mockups — sits one notch deeper than Signal Blue for layered brand moments [accent]
- **Sky Wash**: `#c5e0fb` — Gray supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [accent]
- **Pencil Gray**: `#8c9baa` — Muted body text, hairline borders, nav dividers, step badges, tertiary metadata [neutral]
- **Graphite**: `#636f7b` — Secondary body copy, inactive nav items, supporting descriptions [neutral]
- **Ink**: `#000000` — Headlines, primary body, button text, logo wordmark — the dominant voice of the system at AAA contrast on white [neutral]
- **Carbon**: `#222222` — Navigation text, dense UI labels where pure black feels heavy [neutral]
- **Paper**: `#ffffff` — Page background, card surface, button text on Signal Blue, inverted surfaces [neutral]

## Typography

- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.4 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.4 |
| heading-sm | 24 | — | 1.3 |
| heading | 36 | — | 1.14 |
| heading-lg | 48 | — | 1.09 |
| display | 72 | — | 1 |
| display-xl | 118 | — | 0.94 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 96px
- **Border Radius**: {'nav': '6px', 'tags': '1600px', 'cards': '20px', 'images': '24px', 'inputs': '12px', 'buttons': '1600px', 'iconBadges': '1600px', 'featureCards': '32px'}

## Layout

Layout is max-width contained at 1200px, centered, with generous 96px+ vertical section gaps. The hero is a centered headline stack with floating product mockups scattered asymmetrically around it — not a split text+image layout. Below the hero, sections alternate between a 'logo trust bar' (full-width, centered, low-density) and two-column 'text-left / mockup-right' feature blocks that always lead with an oversized left-aligned heading. Feature blocks use a rounded 20–32px card as a frame for the mockup. The page never goes full-bleed colored, never uses a sidebar, and relies on a sticky top nav with a 6px-radius logo container, centered links, and a black pill CTA on the right.

## Surfaces / Elevation

- **Paper**
- **Card**
- **Elevated**
- **Signal**

**Shadow tokens:**

## Imagery

Imagery is dominated by in-app product mockups rather than photography: phone-frame UI screenshots, small floating annotation cards, sitemap tree node cards, and AI-generator tile previews. These are treated as physical objects — given soft shadows, slight rotation, and connected with thin curved blue lines. A secondary motif is the pastel circular icon badge (yellow, mint, pink, lavender, peach at ~28px) placed inline within body copy to punctuate feature mentions. The avatar trust row uses real human photos at 28px with white ring borders. The overall density is light: roughly 60% text, 40% product mockup, with no lifestyle photography, no hero video, and no decorative illustrations beyond the UI fragments themselves.

## Design Principles

### Do

- Use Signal Blue (#0080ff) as the only saturated color on the page — never introduce a second brand hue for actions, links, or highlights.
- Make every interactive control a pill (1600px radius) unless it is a form input, which uses 12px.
- Set display headlines at 48–118px Inter 700 with letter-spacing between -0.036em and -0.06em so the type compresses into a tight typographic block rather than spreading airy.
- Use 1px Pencil Gray (#8c9baa) borders to separate cards from the white canvas instead of relying on shadow — shadows are reserved for floating hero elements only.
- Anchor long-form copy with pastel circular icon badges placed inline (radius 1600px, 28–32px) so feature lists scan visually.
- Pad feature cards at 24–48px on all sides and use 20–32px radii — never use sharp corners on any card surface.
- Float product UI mockups in the hero with the soft rgba(0,0,0,0.06) 18px shadow and connect them with thin Signal Blue curved lines to act as visual proof.

### Don't

- Don't add a second saturated brand color for buttons, links, or active states — the system is monochrome with one blue signal.
- Don't use square corners on cards, buttons, or tags; everything visible to the user is rounded to at least 6px and most controls are full pills.
- Don't use heavy drop shadows on content cards; the only allowed shadow is the 0.06 alpha 18px blur, and only for floating product mockups and modals.
- Don't let body copy exceed 16–18px or use weight above 500 — anything heavier belongs in a heading.
- Don't use display weight below 600 for headings; the system relies on bold voice to carry its minimal color palette.
- Don't fill sections with solid blue, gradient meshes, or colored bands — backgrounds stay white, color appears only as accent or glow.
- Don't use a neutral gray for primary action text or fills — the only text color for buttons is white on Signal Blue or Ink, never Pencil Gray.

## Components

### Hero CTA Button

Pill shape (1600px radius) with a distinctive wavy/lozenge right tail extension. Fill: Signal Blue (#0080ff). Text: white, Inter 600 at 18–24px, letter-spacing -0.02em. Padding: 16px 32px (with extra right padding to accommodate the wavy tail). Subtle Sky Wash glow shadow at rgba(197,224,251,0.6) offset 18px. No border.

### Nav Login Button

Outlined pill, 1600px radius, 1px Pencil Gray border (#8c9baa), transparent fill, Carbon (#222222) text at 14px weight 500. Padding: 8px 20px.

### Nav Try For Free Button

Filled pill, 1600px radius, Ink (#000000) background, white text, 14px weight 500. Padding: 8px 20px. Small right-arrow icon at 12px.

### Step Badge

Pill (1600px radius) with 1px Pencil Gray border, transparent fill. Left: Ink 'STEP 1' at 11px weight 600, uppercase. Separator dot. Right: Pencil Gray descriptor at 11px weight 400. Padding: 6px 12px.

### Feature Card (Two-Column)

White surface, 20–32px radius, 1px Pencil Gray border (#8c9baa at 1px). Padding: 32–48px. Left column: 16–18px Pencil Gray icon above heading at 16–18px weight 600 in Ink, then body at 14–16px Pencil Gray weight 400. Right column: product screenshot or mockup with 24px radius.

### Section Heading Block

Display weight 700, sizes 48–72px, line-height 1.0–1.09, letter-spacing -0.036 to -0.053em, Ink color. No max-width clamp — text wraps naturally at 2–4 lines. Centered or left-aligned depending on section.

### Icon Badge (Pastel Circles)

Full-pill radius (1600px) circles at 28–32px diameter. Soft pastel fills (yellow, mint, pink, lavender, peach) with 1–1.5px dark icon stroke inside. Placed inline within body text to punctuate feature lists.

### Product Phone Mockup

Vertical phone frame with 32–48px outer radius, white inner surface, 1px Pencil Gray border. Contains stacked UI sections (Header, Menu, Cards) each as a colored chip: pastel yellow, mint, pink, peach. Drop shadow: rgba(0,0,0,0.06) 0px 0px 18px.

### Feature Tile Card (AI Generator)

White card, 20px radius, 1px border. Contains a small uppercase tag in pastel color (e.g. 'AI GENERATOR' in pink), a dark pill button inside (Ink fill, white text, '✨ Generate Sitemap'), and a cursor illustration. Padding: 24px.

### Sitemap Node Card

Small white card, 12px radius, 1px Pencil Gray border. Contains: title row, color-coded label chip (yellow/pink/green at 6px radius), thumbnail, and footer meta. Used in tree/graph layouts.

### Top Rated Product Badge

Small pill, 1600px radius, white fill, 1px Pencil Gray border, 'Top Rated Product' at 12px weight 500 in Ink with a small green check icon. Padding: 4px 12px.

### Avatar Stack

Horizontal row of 5–6 circular avatars at 28px diameter, overlapping by -8px, each with 2px white ring border. Below: 'Over 400,000 users' caption in Pencil Gray at 13px.

### Logo Trust Bar

Full-width centered row of 6 grayscale corporate logos (Intel, IBM, Tesla, EA, UNICEF, Deloitte) at ~60% opacity, 24px height, Pencil Gray fill. Topped by 'You're in good company' caption in 13px Pencil Gray. Padding: 48px 0.

### Floating Annotation Card

Small white card, 12px radius, soft shadow rgba(0,0,0,0.06) 0px 0px 18px. Contains a 2-line annotation: bold label + Pencil Gray description. Connected to hero elements via thin curved Signal Blue stroke.

## Similar Design Systems

- {'why': 'Shares the single-accent-color discipline (one vivid blue against achromatic UI) and pill-shaped CTAs with tight-tracked display headlines', 'business': 'Linear'}
- {'why': 'Same product-marketing playbook: white canvas, oversized bold display type, floating product mockups scattered in the hero, pastel accent chips', 'business': 'Framer'}
- {'why': 'Matches the 1px-bordered card surfaces with minimal shadows, full-pill button geometry, and black-on-white with one chromatic accent', 'business': 'Pitch'}
- {'why': 'Similar restrained two-color palette, Inter-style geometric sans for everything, and the habit of showing the product as floating UI fragments in the hero', 'business': 'Notion'}

## Agent Prompt Guide

## Quick Color Reference
- Text: #000000 (headlines, primary copy), #222222 (nav), #636f7b (secondary), #8c9baa (muted/borders)
- Background: #ffffff (canvas, cards)
- Border: 1px solid #8c9baa
- Accent: #0080ff (Signal Blue) — links, active states, brand wordmark arrow
- primary action: no distinct CTA color
- Decorative glow: #c5e0fb (Sky Wash), #0050ff (Voltage Violet, accent borders only)

## Example Component Prompts

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Feature Section Card**: White surface, 32px radius, 1px solid #8c9baa border. 48px padding all sides. Left column: 20px dark icon (Inter or outline stroke) above 18px Inter 600 #000000 heading, then 16px Inter 400 #636f7b body. Right column: product mockup with 24px radius and rgba(0,0,0,0.06) 0px 0px 18px shadow.

3. **Display Heading Block**: Inter 700, 72px, line-height 1.0, letter-spacing -0.053em, color #000000. Centered, no max-width clamp — let it wrap at 2–3 lines naturally.

4. **Step Badge**: 1600px pill radius, 1px solid #8c9baa border, transparent fill. Left segment: 'STEP 1' in Inter 600 11px #000000, uppercase. Right segment after • separator: 'AI SITEMAP' in Inter 400 11px #8c9baa. Padding 6px 12px.

5. **Pastel Icon Badge**: 1600px full circle, 32px diameter. Fill one of {pastel yellow #fff3c4, mint #c8f0d8, pink #ffd6e0, lavender #e0d4ff, peach #ffe0c4}. 1.5px dark stroke icon centered inside. Use inline within body text to mark feature names.

## Typography Voice

The voice of this system is 'oversized and quiet.' Headlines dominate the page at 48–118px Inter 700 but carry no color signal — they are pure black. The contrast between the enormous type and the single Signal Blue action creates a hierarchy where the user knows exactly where to click without ever reading a label. Body copy is small (14–16px), gray, and conversational, with the pastil icon badges acting as visual bullet points. The CTAs and headings do the talking; everything else is supportive.

## Button Geometry

The signature button geometry is the 1600px-radius pill, but the hero CTA takes this further: its right edge is not a perfect semicircle but a hand-drawn wavy contour (like a wave or brushstroke), giving the primary action a sketched, anti-corporate personality. All other buttons (nav login, nav try-free, in-card actions) are standard pills. Use the wavy-tail geometry only on the single most important CTA per page — never on secondary actions or repeated buttons.
