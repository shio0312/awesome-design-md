# Arva — Design System

> **North Star**: Pastoral editorial magazine spread on a cream field
> **Theme**: light
> **Source**: https://arva.com
> **Refero Style**: https://styles.refero.design/style/15846be3-8df8-42e4-a05c-d9395dcec369
> **Synced**: 2026-09-01

## Overview

Arva uses a pastoral editorial language: warm cream canvas replaces pure white, deep forest green anchors the brand, and quilted pastel surfaces (sky blue, peach, sage, bone) tile across content sections like fields seen from altitude. Typography pairs a refined editorial serif (Reckless) with a neutral sans (Inter), giving the site a printed-magazine feel over a typical SaaS chrome. Buttons are dramatically pill-shaped (100–110px radius), photography dominates above the fold at full-bleed, and the only saturated color besides the brand green appears as a vivid lime marquee strip — a single high-energy accent against an otherwise quiet, earth-toned system.

## Color Palette

- **Forest Ink**: `#07503f` — Primary brand color, header background, nav bar fill, section dividers, footer — deep teal-green against warm cream creates agricultural gravitas [brand]
- **Vivid Lime**: `#e8fe85` — Promotional marquee strip, highlight announcement bars, occasional link hover wash — the only high-energy accent in the palette [brand]
- **Bone**: `#f1efdf` — Page canvas, base background — warm off-white replacing pure white to feel organic and printed [neutral]
- **Pure White**: `#ffffff` — Card surfaces, input fills, button text, icon backgrounds — the bright counterpoint against bone canvas [neutral]
- **Ash Gray**: `#efefef` — Secondary card surface, subtle section dividers [neutral]
- **Charcoal**: `#212529` — Primary body text, headings on light, icon strokes — near-black for high contrast on cream [neutral]
- **Graphite**: `#353535` — Secondary text, link borders, button borders, subdued UI outlines [neutral]
- **Pewter**: `#6d6d6d` — Muted helper text, tertiary button text and borders [neutral]
- **Sky Card**: `#b2cee7` — Decorative card surface — one of the quilted pastel tiles used for partner testimonials and category blocks [accent]
- **Peach Card**: `#fceace` — Decorative card surface — warm pastel tile alternating with sky and sage cards [accent]
- **Sage Card**: `#e6ecd5` — Decorative card surface — soft green pastel tile for agrarian category blocks [accent]
- **Moss**: `#c3cda7` — Subtle borders, input outlines, decorative dividers within body content [accent]

## Typography

- **Inter**
- **Reckless**
- **RecklessLight**
- **sans-serif**
- **Helvetica**
- **FKGrotesk**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.52 |
| subheading | 24 | — | 1.24 |
| heading-sm | 37 | — | 1.22 |
| heading | 45 | — | 1.06 |
| heading-lg | 57 | — | 1.06 |
| display | 80 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 30px
- **Element Gap**: 8px
- **Section Gap**: 50px
- **Border Radius**: {'cards': '20px', 'links': '26px', 'inputs': '33px', 'buttons': '100px', 'nav-pills': '110px', 'hero-cards': '30px'}

## Layout

Full-bleed sections stacked vertically with no max-width container at the section level — each band bleeds to the viewport edge. Internal content is centered at 1200px max-width. Hero is a full-viewport-height image with centered headline + two-button stack + scroll cue. Below the hero, content alternates between bone canvas sections with centered headlines, forest-green interstitial bands with white text, and a 3-column quilted card grid for testimonials/partners. Navigation is a forest-green header bar with centered logo, nav links left, CTA + language selector right. A lime marquee strip sits above the header. Section gaps are roughly 50px; content is spacious and editorial, not information-dense.

## Surfaces / Elevation

- **Bone Canvas**
- **Pure White**
- **Pastel Tiles**
- **Forest Ink**
- **Vivid Lime**

## Imagery

Full-bleed landscape and agricultural photography dominates — aerial drone shots of crop fields in vibrant green and golden brown, on-location portraits of farmers standing in cornfields, close-up product/landscape crops. Photographs are high-resolution, naturalistic, slightly saturated, and always warm-toned. No illustrations or abstract graphics; no icons beyond simple line-art checkmarks and benefit glyphs. Photography treatment is raw (no duotone, no heavy filters, no overlay text boxes with backgrounds). Icons are minimal and line-style when present.

## Design Principles

### Do

- Use #f1efdf (Bone) as the page canvas on every light section — never substitute pure #ffffff as the base
- Apply the 100px pill radius to every button regardless of variant; consistency of the pill is a brand signature
- Pair Reckless (serif) at 45–57px for section headlines with Inter (sans) at 14–17px for body — the serif/sans tension defines the editorial voice
- Let the #e8fe85 lime appear only on the marquee strip and promotional micro-accents — it earns attention through scarcity
- Use the four pastel card surfaces (sky, peach, sage, bone) as a rotating palette within a single row, like a quilted series, not randomly distributed
- Fill the nav bar and section dividers solid with #07503f (Forest Ink) — the dark green bands are the structural backbone of the page rhythm
- Set hero headlines at 57–80px in Reckless weight 300 or Inter weight 600, centered, over full-bleed landscape photography

### Don't

- Do not use #ffffff as the page background — always layer it on top of #f1efdf to preserve the warm printed feel
- Do not apply small radii (4–8px) to buttons or cards; the 20px+ and 100px+ radii are non-negotiable
- Do not introduce new saturated colors beyond Forest Ink and Vivid Lime — the pastel tiles carry the chromatic load
- Do not use Reckless below 24px or for body copy — the serif is for headlines and pull-quotes only
- Do not apply shadows or elevation to cards; depth comes from pastel surface color shifts, not box-shadow
- Do not pair multiple pastels within a single card; one surface color per tile
- Do not center body paragraphs — headlines and hero copy can be centered, but supporting text reads left-aligned at max 60ch

## Components

### Pill CTA Button (Forest Filled)

Background #07503f, text #ffffff, 100px border-radius, 10px 24px padding, Inter weight 500–600 at 14–15px with 0.025em tracking. Uppercase or sentence case both observed.

### Pill Outline Button (Cream/Ghost)

Transparent fill, 1px border in #353535 or currentColor, 100px border-radius, 10px 24px padding, Inter at 14px. Used for 'I'm a Company' paired with the filled 'I'm a Farmer' primary.

### Pill Nav Element

Sits on #07503f forest header. White text, Inter at 15px, no background. Dropdown chevrons are 8px. Active states shift to slight white opacity or underline.

### Get In Touch Pill

Pill shape, 110px radius, #ffffff background on forest header, #212529 text, 10px 20px padding, Inter weight 500.

### Full-Bleed Hero with Photography

Full-viewport landscape photograph (aerial field shot, warm greens), centered white serif headline at 57–80px (Reckless or Inter display), two pill buttons below, 'Scroll to Explore' with down-arrow at bottom center. No overlay — image is the background.

### Lime Marquee Strip

Full-bleed #e8fe85 background bar, repeating dark text (Inter at 12–14px) announcing guides and resources, separated by outlined checkmark icons. Runs the full viewport width above the main nav.

### Pastel Quilt Card

Surface in one of four pastel tones (#b2cee7 sky, #fceace peach, #e6ecd5 sage, #efefef bone), 20px radius, 30px padding, centered content with brand logo at top, quote in body, author name + role at bottom. Cards sit side-by-side in a 3-column row.

### Forest Section Banner

Full-bleed #07503f background, white serif headline, white body copy, small white icon-and-text benefit blocks arranged in a 2×2 grid with icons in circular 30–40px containers.

### Input Field

White fill, 1px border in #c3cda7 (moss) or #353535, 33px radius (distinctly more pill than card), 12px vertical padding, Inter at 16px. Focus ring in #07503f.

### Header Logo Lockup

White lowercase 'arva' wordmark with a green triangular leaf icon to the left. Sits centered on the forest header at roughly 28–32px height.

### Section Divider Header

Left-aligned serif headline (Reckless at 45–57px, #212529) on bone canvas, with optional 1–2 line body intro in Inter at 17px below. No decorative element — the typography carries the hierarchy.

### Partner Logo Card

20px radius, white or pastel surface, centered brand logo at top (raster, full color), blockquote in Inter at 14–15px, author name + title in Inter weight 500–600 at 14px. Cards have generous 30px+ padding.

### Footer (Forest)

Background #07503f, white text and links, multi-column link grid, Inter at 14–15px, logo lockup repeated. 110px top padding or more for breathing room.

## Similar Design Systems

- {'why': 'Same earth-tone editorial identity with full-bleed nature photography and warm cream canvas; both use a single brand color to anchor the page rhythm', 'business': 'Patagonia'}
- {'why': 'Similar generous pill-button radius and clean white/card layering, though Arva swaps the cool grays for warm cream and introduces a serif voice', 'business': 'Stripe'}
- {'why': 'Editorial serif + sans pairing, warm off-white canvas, muted restrained palette, photography that does the heavy visual lifting', 'business': 'Aesop'}
- {'why': 'Playful oversized pill buttons and a single saturated brand color, though Arva replaces the cartoon illustration system with pastoral landscape photography', 'business': 'Mailchimp'}
- {'why': 'Same regenerative-agriculture visual language: deep forest green brand, cream canvas, full-bleed field photography, and warm pastel content surfaces', 'business': 'Wren (offset.earth)'}

## Agent Prompt Guide

primary action: #07503f (filled action)
Create a Primary Action Button: #07503f background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
**Quick Color Reference**
- text: #212529
- background: #f1efdf
- card surface: #ffffff
- border: #c3cda7 or #353535
- brand accent: #07503f
- promotional highlight: #e8fe85

**Example Component Prompts**

1. Build a full-bleed hero: background is a landscape field photograph at 100vh. Centered white headline 'Regenerative supply chains for a better world' in Reckless weight 300 at 57px, letter-spacing -0.012em. Below: two pill buttons side by side — filled #07503f with white text 'I'M A FARMER' (100px radius, 10px 24px padding, Inter 14px weight 600), and ghost outlined 'I'M A COMPANY' (1px white border, 100px radius). At bottom center: 'Scroll to Explore ↓' in Inter 13px.

2. Build a partner testimonial row: 3 cards in a row on #f1efdf canvas. Each card is 20px radius with 30px padding. Card 1 surface #b2cee7, Card 2 #fceace, Card 3 #e6ecd5. Each card: centered brand logo (raster, ~120px wide), 15px Inter body quote, 14px Inter weight 600 author name, 13px Inter weight 400 role. 24px gap between cards.

3. Build a forest interstitial section: full-bleed #07503f background, 80px vertical padding. White Reckless 300 headline at 45px, white Inter 17px body paragraph (max 60ch, left-aligned). Below: 2×2 grid of benefit blocks — each has a small white circular icon container, bold Inter 15px headline, Inter 14px body. 30px gap between grid items.

4. Build a header bar: #07503f background, 60px height, centered white 'arva' wordmark with green leaf icon. Left side: nav links in Inter 15px white (For Farmers, For Companies, For Channel Partners, Our Services ▾). Right side: white pill 'GET IN TOUCH' (110px radius, 10px 20px padding) and US flag + 'US ▾'.

5. Build a marquee strip: full-bleed #e8fe85 background, 32px height, horizontal repeating text 'Arva's Guide to 45Z: Agronomy & Energy Policy' in Inter 13px #212529, separated by small outlined checkmark icons. Sits flush above the header bar.

## Color Philosophy

The palette is deliberately restrained to four surface families: warm bone (the canvas), pure white (cards), pastel tints (quilted tiles), and deep forest green (structural bands). Vivid lime is reserved for a single promotional strip. This scarcity means that when a pastel tile appears, it feels intentional and warm — like a field of crops seen from above. Never introduce blues, reds, or purples beyond the four designated pastels.

## Typography Philosophy

Reckless (or a high-quality serif substitute like GT Sectra) carries the editorial voice at 24px and above. Inter handles everything functional below 24px. The two-font pairing replaces the typical sans-only SaaS stack with a magazine sensibility — headlines feel written, not engineered. The ultra-light weight (100–300) of Reckless is a deliberate anti-convention choice: most sites push to weight 700 for authority, but Arva whispers. The serif at weight 300 at 57px is more confident than a bold sans would be.

## Shape Language

Radii are disproportionately large for the system size. Cards at 20px, buttons at 100–110px, inputs at 33px. The pill is the dominant shape — it appears on every interactive element, making the site feel soft, approachable, and distinctly non-corporate. There are no sharp 90° corners on any interactive surface. The shape language signals 'this is a field, not a dashboard.'
