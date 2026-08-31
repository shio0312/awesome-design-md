# Passionfroot — Design System

> **North Star**: Twilight cloud library on warm parchment. A serif headline drifts above cream cards lit by a violet-to-coral sky, where a pastel mascot peeks from the corner.
> **Theme**: mixed
> **Source**: https://www.passionfroot.me
> **Refero Style**: https://styles.refero.design/style/aaaa705d-3042-4355-ad30-13360f04e403
> **Synced**: 2026-09-01

## Overview

Passionfroot operates as a dusk-lit creative workspace: warm parchment canvas (#f8f7f2), a custom serif (new-kansas) for editorial-grade headlines, and a full-spectrum accent palette that treats color as joyful punctuation rather than corporate branding. Screens often open against a twilight sky gradient (deep violet bleeding into coral) before resolving into cream cards and content. The visual language is compact, rounded, and tactile — 12px radii everywhere, pill-shaped interactive chips, warm-toned layered shadows (oklch-tinted, not pure gray) that feel like sunlight on paper, and a 3D mascot that anchors the dreamy atmosphere. Components stay lightweight: thin 1px borders, ghost buttons, white elevated surfaces, no heavy drop-shadows. Color appears as small functional sprinkles — pastel card backgrounds, vivid icon strokes, chromatic borders — never as a single dominant brand color.

## Color Palette

- **Ink Black**: `#1d1d1c` — Primary text, primary borders, dark surface fills — the workhorse neutral that carries all high-contrast text and structural outlines [neutral]
- **Parchment Cream**: `#f8f7f2` — Page canvas, default body background, nav surface — warm off-white that replaces pure white to avoid sterile SaaS feel [neutral]
- **Sand Gray**: `#d8d6ce` — Hairline borders, dividers, soft box-shadow base — the warm-tinted stroke that gives components a paper-on-paper quality [neutral]
- **Linen Beige**: `#edeae4` — Card surfaces, elevated backgrounds, shadow tint — sits one step above Parchment Cream as the secondary surface level [neutral]
- **Paper White**: `#ffffff` — Highest-elevation surfaces, button fills, input fields — the brightest neutral reserved for the focal interactive elements [neutral]
- **Charcoal Stone**: `#43423e` — Secondary text, muted button borders, button text on light fills — the mid-dark neutral for body copy and neutral action outlines [neutral]
- **Ash Gray**: `#99978f` — Muted text, placeholder text, subtle icon strokes, disabled state borders — the warm mid-gray for de-emphasized content [neutral]
- **Slate Warm**: `#7a7974` — Secondary muted text, button labels in ghost variants — one step darker than Ash Gray for slightly more legible de-emphasis [neutral]
- **Electric Violet**: `#b26bf5` — Primary brand accent — the most-prominent chromatic across the system, used for highlighted card surfaces, illustration fills, and brand emphasis; vivid lavender that defines the Passionfroot identity [brand]
- **Twilight Indigo**: `#190922` — Dark hero section base, deep contrast text on light surfaces — the near-black plum that anchors the twilight gradient backgrounds [brand]
- **Bubblegum Pink**: `#f788d2` — Accent card surface, tag pill, illustration fill — one of the pastel punctuation colors in the rainbow accent set [accent]
- **Tangerine**: `#ff9147` — Accent card surface, warm illustration fill, decorative highlight — the sunset-orange accent for warmth and energy [accent]
- **Aqua Teal**: `#4ad5e8` — Accent card surface, cool-toned illustration fill — the bright sky-cyan for variety in the multi-color accent set [accent]
- **Sky Blue**: `#51b1fb` — Accent card surface, cool illustration fill — lighter blue accent used in color card rotation [accent]
- **Sunshine Yellow**: `#ffe747` — Accent card surface, highlight wash — the warm yellow accent for cheerful punctuation in card backgrounds [accent]
- **Lavender Glow**: `#b977f8` — Decorative border, icon stroke, soft accent outline — slightly lighter than Electric Violet for outlined elements [accent]
- **Pale Violet**: `#dab2ff` — Outlined button border, soft accent stroke — the desaturated lavender for ghost/outlined action elements [accent]
- **Lilac Mist**: `#f3e8ff` — Outlined button background wash, soft accent fill — extremely pale violet for subtle tinted button states [accent]
- **Deep Violet**: `#8200db` — Icon border, decorative stroke, bold accent outline — the saturated dark violet for iconography and emphasis strokes [accent]
- **Coral Red**: `#ee5968` — Illustration fill, warm accent, character highlight — the warm coral used in the mascot and decorative artwork [accent]
- **Mint Green**: `#58df8c` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content [accent]
- **Forest Green**: `#00a63e` — Green decorative accent for icons, marks, and small graphic details. Use as a supporting accent, not as a status color [accent]
- **Burnt Orange**: `#eb6928` — Icon border, warm stroke, illustrative accent — darker orange for icon outlines and warm decorative elements [accent]
- **Deep Teal**: `#2c91af` — Icon border, cool stroke, informative accent — the desaturated teal for cool-toned iconography and strokes [accent]
- **Magenta Bloom**: `#b036a4` — Icon border, decorative stroke, pink-magenta accent — the warm magenta for iconography and brand emphasis strokes [accent]
- **Mint Wash**: `#dcfce7` — Gray wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]

## Typography

- **new-kansas**
- **Nunito Sans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.4 |
| heading-sm | 28 | — | 1.35 |
| heading | 48 | — | 1.2 |
| display | 64 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'cards': '12px', 'pills': '9999px', 'inputs': '12px', 'buttons': '12px', 'special': '24px', 'large-cards': '16px'}

## Layout

The page uses a max-width 1200px centered content model with full-bleed atmospheric sections. The hero is full-viewport with a centered text composition (headline + subhead + dual-button row) layered over a twilight sky gradient, with floating product UI cards arranged in a loose 2-3 card cluster below the text and a 3D mascot character at the bottom-right. Section rhythm alternates: dark hero → cream canvas section with logo bar → another twilight illustration section → white card section (tab navigation + prompt input) → testimonial. The white card section (Meet Zest) uses a rounded white panel (16-24px radius) that sits ON TOP of the illustration, creating a paper-on-sky layering effect. Content within cards is centered. The logo bar is a single horizontal row with wide gaps. Tab interfaces use simple text-with-underline active states. Grid usage is minimal — most layouts are centered single-column or paired card compositions rather than multi-column grids. Navigation is a floating top bar (transparent over hero, solid cream over content) with brand left, nav center, CTA right.

## Surfaces / Elevation

- **Twilight Sky**
- **Parchment Canvas**
- **Linen Card**
- **Paper White**

**Shadow tokens:**

## Imagery

The visual language is dominated by 3D-rendered illustration rather than photography. A pink/coral blob-shaped mascot character (rounded body, small green leaf on top, large black eyes) appears as a brand anchor, peeking from the bottom-right of the hero and floating among clouds in secondary sections. Hero backgrounds feature a photorealistic purple-to-coral sunset sky with volumetric clouds and a starfield — this gradient sky is the primary atmospheric device, not a photograph of a real sky but a CGI/3D rendered environment. The clouds are bulbous, rounded, almost candy-like in their softness. Product screenshots are simulated through floating UI cards (metric cards, chart cards, AI input fields) rather than literal app captures, creating a 'product peek' composition. No human photography is present. The illustration style is warm, dreamy, slightly surreal — a children's-book-meets-tech aesthetic that signals approachability and creativity over corporate polish.

## Design Principles

### Do

- Use new-kansas (or DM Serif Display) at 48-64px weight 400 for all display headlines — the light weight is the signature, not a fallback for 700
- Set page background to Parchment Cream (#f8f7f2), never pure white — the warm tint is what makes the system feel like paper rather than screen
- Apply 12px radius consistently across cards, buttons, and inputs — this is the single most defining shape token in the system
- Use 9999px radius exclusively for tag pills and suggestion chips — full pills create a distinct typographic category from standard buttons
- Layer shadows with oklch warm-tinted colors (not pure rgba(0,0,0,0.1)) — the 237/234/228 base color makes elevation feel like soft sunlight on paper
- Pair the rainbow accent set (violet, pink, orange, teal, blue, yellow, green) as card backgrounds in feature grids — color rotation creates visual rhythm without illustration
- Use Ink Black (#1d1d1c) for all primary text and structural borders — the warm-tinted near-black is softer than #000 and more distinctive than pure gray

### Don't

- Do not use weight 700 for display headlines — the 400 weight new-kansas is intentional restraint; bolding it destroys the whisper-quiet authority
- Do not use pure white (#ffffff) as a page background — the warm cream canvas is a signature trait, not an oversight
- Do not use pure black (#000000) for text — Ink Black (#1d1d1c) is warmer and the correct token
- Do not add heavy drop-shadows with gray/black tints — shadows must use oklch warm tones to stay on-brand
- Do not create a single-color CTA (e.g. solid Electric Violet button) — the system uses neutral filled buttons (white/ink) with chromatic accents reserved for decorative elements
- Do not use radii other than 12px, 16px, 24px, or 9999px — these four values are the complete shape vocabulary
- Do not mix the serif and sans-serif at body sizes — new-kansas stays at 28px and above; Nunito Sans owns everything below

## Components

### Filled Action Button

White background (#ffffff), Ink Black text (#1d1d1c), 12px radius, padding 10px 20px. Nunito Sans 14-16px weight 500-600. No visible border, but subtle layered shadow: oklch(0.23 0.002 98 / 0.04) at multiple offsets creating soft elevation. Label text uses -0.011em letter-spacing. The 'Start for free' button is the canonical example.

### Ghost Action Button

Transparent or very dark transparent background, white/cream text (#f8f7f2), 12px radius, padding 10px 20px. No border in hero context. Includes a play icon (▷) for trailer actions. Uses Nunito Sans 14-16px weight 500.

### Outlined Violet Button

Pale Violet background (#f3e8ff), Pale Violet border (#dab2ff) at 1px, Ink Black text, 12px radius, padding 10px 16px. The chromatic border gives it personality without overwhelming. Nunito Sans 14px weight 500.

### Neutral Bordered Button

Paper White background (#ffffff), Charcoal Stone border (#43423e) at 1px, Ink Black text, 12px radius, padding 8px 16px. Includes a subtle shadow: oklch(0.876 0.011 98) ring + soft layered drop-shadow. Used for form actions and neutral interactions.

### Metric Card

White background (#ffffff), Sand Gray border (#d8d6ce) at 1px, 12px radius, padding 12-16px. Contains a label in Nunito Sans 12px Ash Gray (#99978f) and a value in new-kansas or Nunito Sans 16-20px weight 500 Ink Black. Optional small positive delta (e.g. '+54%') in Forest Green. Cards float with layered oklch shadows and slight rotation for dimensional playfulness.

### Chart Card

White background, 12px radius, 16px padding. Contains a chart label in Nunito Sans 12px, and a chart with brand-colored data: Tangerine bars, Electric Violet line strokes, Forest Green for positive trends. Legend dots in matching chromatic colors at 8px circles.

### AI Prompt Input

White background (#ffffff), Sand Gray border at 1px, 12px radius, padding 12px 16px. Contains placeholder text in Ash Gray Nunito Sans 14px, an '@' mention chip with Pale Violet background, and a dark circular send button (Ink Black, 32px, white arrow icon) at the right. The 'How many people did our @Q1 Campaign reach?' field is canonical.

### Tab Navigation

Horizontal row of text tabs in Nunito Sans 14-16px. Active tab: Ink Black text with 2px Ink Black underline. Inactive: Ash Gray text, no underline. 8px gap between tabs. The 'Launch a product / Announce a fundraiser / Stay top of mind' tab set is canonical.

### Pill Tag/Chip

12px to 9999px (full pill) radius, padding 4px 10px. Background varies: Pale Violet for mentions (#f3e8ff), Paper White for suggestions. Text in Nunito Sans 12-14px weight 500. Includes optional small icon (8-12px). The 'Plan strategy / Run campaign / Measure results' suggestion chips are canonical.

### Logo Bar Row

Horizontal scrollable row of company logos on Parchment Cream background (#f8f7f2). Logos rendered in Charcoal Stone (#43423e) or Ash Gray (#99978f) at uniform 24-32px height. Even spacing with 32-48px gaps. Overline text above: 'Trusted by B2B marketing and growth teams' in Nunito Sans 12-14px weight 500, Ash Gray, centered.

### Floating Product Card Stack

Multiple cards (Metric, Chart, AI Prompt Input) arranged in a loose floating composition with slight rotations (-2° to 2°). Each card has white background, 12px radius, warm layered shadows (oklch-tinted at 1px, 3px, 6px, 12px offsets), and 1px Sand Gray border. The stack creates depth and signals 'real product' without showing the full app.

### Hero Section

Full-bleed background using Twilight Indigo (#190922) at top blending into a purple-pink-orange gradient (resembling sunset clouds). Centered content with max-width ~800px. Display headline in new-kansas 64px weight 400, white text, -0.023em letter-spacing. Subhead in Nunito Sans 16-18px weight 400, warm cream/white at reduced opacity. Button row centered below.

### Testimonial Block

Parchment Cream background. Large quote text in new-kansas or Nunito Sans 28-48px weight 400, Ink Black, centered, with a large opening quotation mark. Below: small avatar circle (32px) in Sand Gray placeholder, name in Nunito Sans 14px weight 500, title in Nunito Sans 12px Ash Gray.

### Navigation Bar

Transparent or Parchment Cream background, positioned over hero. Left: brand wordmark 'passionfroot' in Nunito Sans 14px weight 700, lowercase. Center: nav items in Nunito Sans 14px weight 400. Right: text links + 'Get access' filled button (Ink Black bg, white text, 12px radius, small arrow icon).

### Accent Color Card Set

Cards with full-saturation pastel backgrounds from the accent set: Electric Violet, Bubblegum Pink, Tangerine, Aqua Teal, Sky Blue, Sunshine Yellow, Mint Green. 12px radius, 16-20px padding, Ink Black text. Nunito Sans 14-16px for labels. Used in feature grids to create rhythm and energy without needing photographic imagery.

## Similar Design Systems

- {'why': 'Same compact 12px-radius cards, warm-toned layered shadows, and dark-to-light section transitions with floating product UI', 'business': 'Linear'}
- {'why': 'Same playful mascot-as-brand-anchor approach, warm cream canvas with pastel accent palette, and editorial serif mixed with functional sans-serif', 'business': 'Notion'}
- {'why': 'Same dreamy atmospheric gradients, rainbow accent palette treated as joyful punctuation, and 3D illustration over flat UI', 'business': 'Arc Browser'}
- {'why': 'Same warm parchment aesthetic, compact rounded components, and twilight/dusk atmospheric color stories in hero sections', 'business': 'Pitch'}
- {'why': 'Same serif-meets-sans-serif typographic pairing, floating product card compositions, and violet-dominant accent strategy', 'business': 'Framer'}

## Agent Prompt Guide

## Quick Color Reference
- text: #1d1d1c (Ink Black)
- background: #f8f7f2 (Parchment Cream)
- surface/elevated: #ffffff (Paper White)
- border: #d8d6ce (Sand Gray)
- muted text: #99978f (Ash Gray)
- brand accent: #b26bf5 (Electric Violet)
- primary action: #43423e (filled action)

## Example Component Prompts
1. **Hero headline block**: Background: twilight gradient (#190922 to #8200db). Headline: 64px new-kansas weight 400, white (#ffffff), letter-spacing -0.023em. Subhead: 18px Nunito Sans weight 400, #f8f7f2 at 80% opacity. Button row centered: 'Start for free' (white bg, #1d1d1c text, 12px radius, 10px 20px padding) + 'Watch the trailer' ghost button (transparent bg, white text, 12px radius).

2. **Metric card**: White background (#ffffff), 12px radius, 1px #d8d6ce border, padding 16px. Label: 'Total impressions' in 12px Nunito Sans #99978f. Value: '1.4M' in 20px Nunito Sans weight 500 #1d1d1c. Delta: '+54%' in 12px Nunito Sans weight 500 #00a63e. Layered shadow with warm oklch tints.

3. **AI Prompt Input**: White background, 1px #d8d6ce border, 12px radius, padding 12px 16px. Placeholder text: 'How many people did our @Q1 Campaign reach?' in 14px Nunito Sans #99978f. Mention chip '@Q1 Campaign' with #f3e8ff background, #8200db text, 9999px radius, 4px 10px padding. Send button: 32px circle, #1d1d1c background, white arrow icon.

4. **Tab Navigation**: Horizontal row, 8px gap. Active tab: 14px Nunito Sans weight 500, #1d1d1c, 2px #1d1d1c underline. Inactive: 14px Nunito Sans weight 400, #99978f, no underline. Pairs with prompt input below.

5. **Accent Color Feature Card**: Full background fill from accent set (#b26bf5, #f788d2, #ff9147, #4ad5e8, #51b1fb, #ffe747, #58df8c — rotate). 12px radius, 20px padding. Title: 16px Nunito Sans weight 600 #1d1d1c. Body: 14px Nunito Sans weight 400 #1d1d1c at 85% opacity.
