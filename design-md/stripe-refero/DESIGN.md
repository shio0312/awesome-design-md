# Stripe — Design System

> **North Star**: indigo-ink ledger on frosted glass
> **Theme**: light
> **Source**: https://stripe.com
> **Refero Style**: https://styles.refero.design/style/48e5de76-05d5-4c4e-a269-c7c245b291ec
> **Synced**: 2026-09-01

## Overview

Stripe uses a near-monochrome financial-instrument language: a soft cool-white canvas with deep navy headings, almost no decorative chrome, and one vivid indigo (#533afd) that earns the right to be a button, link, or icon stroke. Typography is exclusively sohne-var at weight 300 — even at 56px display size — which reads as confident restraint rather than corporate shouting; letter-spacing tightens aggressively as size grows. Buttons are small, squared at 4px, and use violet fills or hairline violet outlines. The system avoids shadows entirely; depth comes from background tint shifts (white → #f8fafd → #e5edf5 → violet washes) rather than elevation. The whole interface behaves like a ledger or terminal: dense information, crisp rules, generous whitespace between sections, and color appearing only when something needs to be acted on.

## Color Palette

- **Indigo Ink**: `#533afd` — Violet action color for filled buttons, selected navigation states, and focused conversion moments. [brand]
- **Indigo Hover**: `#7389ff` — Violet text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Midnight Ink**: `#061b31` — Primary heading and body text — deep near-black with a cool blue undertone that anchors the entire type system [neutral]
- **Slate**: `#64748d` — Gray text accent for links, tags, and emphasized short phrases. [neutral]
- **Steel**: `#50617a` — Tertiary body text and helper copy — sits between slate and the muted violet tints used on sub-labels [neutral]
- **Smoke**: `#839bc8` — Muted violet-tinted text for large decorative headings and supporting copy — never for body paragraphs [neutral]
- **Pure White**: `#ffffff` — Page canvas and elevated card surfaces; the default background against which everything else is measured [neutral]
- **Mist**: `#f8fafd` — Footer background and section banding — a barely-perceptible cool tint that separates regions without a visible line [neutral]
- **Frost**: `#e5edf5` — Primary border color, subtle surface tint, and button hover backgrounds; the workhorse neutral that divides content [neutral]
- **Lavender Border**: `#b9b9f9` — Hairline outline button border (1px) — the violet companion to indigo fills; pairs with white text for ghost CTAs [accent]
- **Lilac Border**: `#d6d9fc` — Secondary outline button border and softer dividers; a paler sibling of lavender for tertiary ghost actions [accent]
- **Periwinkle Wash**: `#e8e9ff` — Lightest violet surface — soft tinted backgrounds for highlighted cards, tag pills, and subtle emphasis blocks [accent]
- **Deep Violet**: `#182659` — Heaviest accent stroke — rare use for emphasized borders or graphic frames; reads almost as a navy [accent]
- **Amethyst Edge**: `#7f71e6` — Mid-violet outline border for developer-facing buttons; sits between indigo ink and lavender border [accent]

## Typography

- **sohne-var**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.45 |
| body-sm | 14 | — | 1.4 |
| body | 16 | — | 1.2 |
| body-lg | 20 | — | 1.4 |
| subheading | 22 | — | 1.1 |
| heading-sm | 26 | — | 1.12 |
| heading | 32 | — | 1.1 |
| heading-lg | 48 | — | 1.03 |
| display | 56 | — | 1.03 |

## Spacing & Layout

- **Max Width**: 1320px
- **Card Padding**: 32px
- **Element Gap**: 8px
- **Section Gap**: 96px
- **Border Radius**: {'tags': '9999px', 'cards': '4px', 'inputs': '4px', 'buttons': '4px'}

## Layout

Max-width ~1320px centered content column on a white canvas. Hero is a left-aligned text block at full display size (56px) with two CTAs below, no hero image — the typography IS the hero. Sections are stacked vertically with consistent 96px gaps and 1px #e5edf5 dividers; no alternating dark/light bands. Each section follows a repeating pattern: small uppercase section label (smoke color, 12px), then a 32–48px heading, then a 22px slate paragraph, then a grid of product cards (3-column at desktop) or a 2-column text-plus-visual block. Customer logos appear in a narrow left-aligned vertical rail. Footer is a single wide #f8fafd band with multi-column link lists. The overall rhythm is slow, deliberate, and text-dominant — information density is low despite long scroll length.

## Surfaces / Elevation

- **Canvas**
- **Band**
- **Frosted Card**
- **Lavender Card**
- **Indigo Surface**

## Imagery

Imagery is restrained and documentary-style. Full-bleed photographs appear only in editorial case-study sections (e.g., aerial traffic photography for Hertz), shot from above or at a dramatic angle with natural color — no duotone or color treatment. Product UI screenshots are used inside feature cards, rendered with sharp corners and 1px borders, no device frames. Logo rails show partner brands in their native colors without any wrapping container. There are no illustrations, no 3D renders, no decorative abstract graphics. Icons are uniform: 1.5px stroke weight, #533afd stroke on white, geometric line-art style (chevrons, arrows, checkmarks, document marks). The page is predominantly text-and-whitespace; images occupy less than 15% of total visual area.

## Design Principles

### Do

- Use #533afd exclusively for primary actions, active links, and icon strokes — never for body text, backgrounds spanning large areas, or decorative elements
- Set all headings and body text to sohne-var weight 300 — the whisper-weight is the signature; do not use weight 600 or 700 anywhere except the Stripe wordmark
- Tighten letter-spacing as type size grows: -0.0100em up to 26px, -0.0200em at 32–48px, -0.0250em at 56px, -0.0300em above 56px
- Apply font-feature-settings: 'ss01' on, 'tnum' on to all text — tabular numerals are essential for the metric/stat blocks and pricing displays
- Use 4px border-radius on all buttons, inputs, and cards — never 0px (too sharp), never pill (too friendly), never 8px+ (too soft)
- Separate sections with 1px #e5edf5 horizontal rules and 96px vertical gaps — do not use background color shifts, shadows, or card containers to divide content
- Pair each filled primary button with a ghost outline button (lavender #b9b9f9 border) as its secondary action — never present a filled button alone

### Don't

- Do not use shadows, blurs, or any form of CSS elevation on cards, buttons, or images — depth comes from background tint, never from box-shadow
- Do not introduce additional accent colors — the system is monochromatic plus one indigo; adding greens, oranges, or pinks breaks the ledger aesthetic
- Do not use semibold or bold weights for headings — weight 300 at display size is the entire typographic identity
- Do not use rounded corners beyond 4px — pill buttons, large radii, or fully circular elements break the precision-tool feel
- Do not fill large areas with #533afd — the indigo should appear in small functional doses (buttons, links, icon strokes); large indigo backgrounds belong only to feature cards designed for contrast
- Do not center body copy or headings — Stripe text blocks are always left-aligned within their column; centering is reserved for logo marks and a few isolated stat displays
- Do not use #64748d or #50617a for anything longer than a sentence — these are muted text colors for labels and captions, not for paragraphs

## Components

### Primary Filled Button

Background #533afd, white text (#ffffff), 4px radius, padding 15.5px 24px (vertical slightly asymmetric due to optical alignment). Typography: sohne-var weight 400 at 14px. On hover, lightens to #7389ff or shifts background. No shadow. The 4px radius — not pill, not square — is a deliberate middle ground that reads as professional rather than friendly.

### Ghost Outline Button

Transparent background, violet text (#533afd), 1px border in #b9b9f9 (lavender), 4px radius, padding 14.5px 24px. Same typographic spec as the filled button (sohne-var 400 at 14px). The lavender border is intentionally lighter than the text — the text is the loud element, the border whispers.

### Tertiary Outline Button

Transparent background, violet text, 1px border in #d6d9fc (lilac, paler than lavender), 4px radius, smaller padding. Used when a button is needed but shouldn't compete with the primary action above it.

### Text Link Button

No border, no background. Text in #533afd with a trailing chevron character. Typography: sohne-var weight 400 at 16px, inheriting body line-height. Often paired with a brief description above it. The chevron is part of the visual identity — directional without being aggressive.

### Underline Link

Text in #533afd with a 1px underline in the same color. No border, no background. Used for inline references within body copy where the chevron pattern would feel too heavy.

### Section Heading Block

Display-size heading (48–56px sohne-var weight 300, #061b31, letter-spacing -0.96 to -1.40px) on one or two lines, followed by a slate (#64748d) supporting paragraph at 22–26px weight 300. Generous vertical gap (32–48px) between heading and paragraph. This is the 'Stripe statement' pattern — confident headline, quiet explanation.

### Product Feature Card

White (#ffffff) surface on white canvas, no shadow, no visible border by default. Content: small violet-tinted label or tag at top, then heading-sm (32px weight 300 #061b31), then body paragraph. Generous internal padding (~32px). Cards are distinguished only by layout and whitespace, never by chrome.

### Customer Logo Rail

Logos rendered at their native brand colors on white background, vertically stacked with consistent spacing. Logos retain their original palette — the rail itself uses no Stripe chrome. Functions as a 'who trusts us' signal without visual competition with surrounding content.

### Navigation Bar

White background, hairline #e5edf5 bottom border (1px). Stripe wordmark on left in #061b31. Menu items (Productos, Soluciones, Desarrolladores, Recursos, Tarifas) in sohne-var weight 400 at 14px, #061b31, with 8px gap between items. Right side: ghost outline 'Inicia sesión' link and filled primary 'Contacta con ventas' button. Fixed height ~76px.

### Metric/Stat Block

Number rendered at display size (48–56px sohne-var weight 300 #061b31, tight letter-spacing) with a slate-colored label below it at body size. No card, no border — the number itself carries the visual weight. The combination of whisper-weight type and enormous size creates a distinctive 'quiet monument' effect.

### Hero CTA Pair

Filled primary button ('Empieza ahora') directly followed by ghost outline button ('Accede con tu cuenta de Google') with 8px gap. Both at the same height (14px text, ~48px total). The ghost button features a small Google 'G' icon before its text — a rare instance of an inline icon in a button.

### Section Divider

A 1px solid line in #e5edf5 spanning the full content width. No decorative elements — just a quiet horizontal rule that resets the page rhythm. This is the primary structural element of the layout; there are no shadows, no background shifts between sections.

## Similar Design Systems

- {'why': 'Same sohne-var weight 300 headline approach, same tight letter-spacing at large sizes, same single-accent-color-on-monochrome discipline, same avoidance of shadows', 'business': 'Linear'}
- {'why': 'Same whisper-weight display headlines, same minimal-chrome card design, same restraint with color — but Vercel uses black instead of indigo as the accent', 'business': 'Vercel'}
- {'why': 'Same left-aligned text-led layout with generous section gaps and 1px hairline dividers instead of shadows or card containers', 'business': 'Notion'}
- {'why': 'Same monochromatic base with one vivid accent for actions and icons, same hairline borders, same flat-surface philosophy', 'business': 'Figma'}
- {'why': 'Same playful-but-precise typographic voice at weight 300, same trust in whitespace rather than chrome', 'business': 'Arc browser'}

## Agent Prompt Guide

## Quick Color Reference
- Text primary: #061b31
- Text secondary: #64748d
- Text muted: #50617a
- Background canvas: #ffffff
- Background band: #f8fafd
- Border / divider: #e5edf5
- Accent / link / icon stroke: #533afd
- Hover accent: #7389ff
- Ghost button border: #b9b9f9
- primary action: #533afd (filled action)

## Example Component Prompts

1. Create a Primary Action Button: #533afd background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Product feature card grid**: White (#ffffff) cards on white canvas, no shadow, no border. Each card: 32px padding, 8px gap between label and heading. Label at 12px sohne-var weight 300 in #839bc8. Heading at 32px weight 300 in #061b31, letter-spacing -0.64px. Body at 16px weight 400 in #50617a, line-height 1.40. 3-column grid with 24px column gap. Separate cards by whitespace alone — no visible borders.

3. **Section heading + stat block**: 96px top padding. Section label at 12px sohne-var weight 300 in #64748d, text-transform uppercase, letter-spacing 0.5px. Heading at 48px weight 300 in #061b31, letter-spacing -0.96px. Below: a large stat — number at 56px weight 300 in #061b31, with a slate (#64748d) 18px label below it. 32px gap between heading and stat.

4. **Ghost outline button**: Transparent background. Text at 14px sohne-var weight 400 in #533afd. 1px solid border in #b9b9f9. 4px border-radius. Padding: 14.5px top, 24px left/right, 15.5px bottom. No shadow. Optional inline icon at 16px to the left of text, rendered as 1.5px stroke #533afd line-art.

5. **Section divider**: 1px solid horizontal line in #e5edf5, spanning the full content width (max 1320px), centered. 96px vertical space above and below.
