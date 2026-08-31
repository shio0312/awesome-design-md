# Render — Design System

> **North Star**: Blueprint on brushed aluminum. The interface reads as a clean, geometric engineering document — white space, hairline rules, and one violet marker line drawing the eye to the action.
> **Theme**: light
> **Source**: https://render.com
> **Refero Style**: https://styles.refero.design/style/c14bfde7-6f08-4b54-bd9b-39989d10cfef
> **Synced**: 2026-09-01

## Overview

Render presents a clinical, paper-white canvas for cloud infrastructure — an interface that feels like a well-organized technical schematic rather than a marketing surface. The system is overwhelmingly achromatic: #0d0d0d text on #ffffff surfaces, separated by hairline #e3e3e3 borders, with one vivid violet (#8a05ff) acting as the singular brand punctuation and a warm-to-cool gradient (violet→orange) reserved for hero emphasis. Typography is the primary expressive tool — Roobert at light weight 300 with tight tracking carries headlines with geometric quietness, while PPNeueMontreal handles UI with workmanlike neutrality. Code-adjacent elements use PPNeueMontrealMono, lending technical credibility without resorting to cliché terminal aesthetics. Components are square-cornered, border-defined, and low-elevation; the interface reads as a grid of confident panels rather than floating cards. Color appears sparingly — a violet step number, a soft tinted surface, a gradient text phrase — so when it does appear, it carries weight.

## Color Palette

- **Obsidian**: `#0d0d0d` — Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color [neutral]
- **Paper White**: `#ffffff` — Page canvas, card surfaces, button text on dark fills — the dominant base against which all content rests [neutral]
- **Graphite Hairline**: `#e3e3e3` — Borders, dividers, subtle surface tints — the workhorse neutral at 4000+ occurrences that defines structural edges throughout the UI [neutral]
- **Smoke**: `#4d4d4d` — Secondary text, muted nav, footer copy — the soft mid-gray for de-emphasized but still readable text [neutral]
- **Ash**: `#6b6b6b` — Tertiary text, helper labels, inactive metadata — the quietest text tier for non-essential guidance [neutral]
- **Carbon**: `#272727` — Deep surface tone for code blocks, terminal-style badges — a near-black with a whisper of warmth for developer-flavored elements [neutral]
- **Plasma Violet**: `#8a05ff` — Brand accent — step indicators, decorative illustration fills, link highlights, gradient text origin — the single chromatic mark that makes this interface feel like Render; Hero emphasis text and promotional banners — the signature warm-to-cool transition that defines Render's expressive typography moments [brand]
- **Wisteria Tint**: `#e6daff` — Soft violet surface wash for tinted cards, hero illustration backgrounds, highlight panels — a 12% saturation tint of the brand violet that creates brand presence without commitment; Soft highlight wash behind hero text and illustration panels — a barely-there violet tint that signals brand presence on neutral surfaces [brand]
- **Deep Indigo**: `#48008c` — Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Marigold**: `#d67f2e` — Gradient text terminus (violet→orange), warm accent in illustrations — the chromatic counterweight to Plasma Violet in the signature gradient [accent]
- **Coral**: `#e96770` — Decorative illustration accent, infographic data points — used in product mockups to add warmth and color variety [accent]
- **Mint Signal**: `#006d4c` — Green supporting accent for decorative details and low-frequency emphasis [accent]
- **Sky Pulse**: `#33acff` — Decorative accent in product illustrations, secondary data visualization — a clear electric blue for chart and metric highlights [accent]
- **Fuchsia Pop**: `#f347ff` — Decorative accent in gradient text and illustration hotspots — the highest-chroma pink used sparingly for energy bursts [accent]

## Typography

- **PPNeueMontreal**
- **Roobert**
- **PPNeueMontrealMono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.38 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.33 |
| heading-sm | 24 | — | 1.21 |
| heading | 32 | — | 1.1 |
| heading-lg | 40 | — | 1.08 |
| heading-xl | 48 | — | 1.07 |
| display | 64 | — | 1.05 |
| display-lg | 80 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 16-20px
- **Section Gap**: 80-96px
- **Border Radius**: {'cards': '2px', 'pills': '937px', 'badges': '2px', 'buttons': '2px'}

## Layout

The page is a max-width 1200px centered layout on a white canvas. The hero is a two-column split: left column holds the headline (Roobert 80px weight 300), supporting copy, and dual CTAs (dark filled + ghost outline); right column holds a tilted illustration panel showing product UI cards. Below the hero, a full-width logo cloud band with 5-column grid separates social proof from the next content block. The 'Click, click, done' section uses a 3-column step layout with violet numbered squares, heading, body text, and a visual beneath each. Section gaps are 80-96px, creating comfortable vertical rhythm. Navigation is a single horizontal bar: logo left, 5 nav links center, contact/sign-in/CTA right. The page has no sidebar, no sticky elements beyond the header, and no full-bleed colored sections — it stays white from edge to edge.

## Surfaces / Elevation

- **Paper White**
- **Wisteria Tint**
- **Lilac Wash**
- **Carbon**
- **Obsidian**

## Imagery

Illustrations are schematic product mockups rather than photography: light violet (#e6daff) panel backgrounds containing floating white cards with hairline borders, miniature line charts in Plasma Violet, and inline status badges. No lifestyle photography, no 3D renders, no abstract decorative graphics. The visual language is 'screenshot of the actual product, gently abstracted' — the product UI IS the hero imagery. Icons (visible in the logo cloud and step indicators) are flat, single-weight, monochrome silhouettes. The only photographic-style content is the very thin gradient strip at the very top of the page (violet to warm orange).

## Design Principles

### Do

- Use #0d0d0d for all primary filled buttons — never introduce a chromatic CTA color; the dark-on-white contrast is the system's defining emphasis pattern.
- Set display headlines (64-80px) in Roobert weight 300 with letter-spacing -0.025em to -0.03em — the whisper-weight with tight tracking is the signature voice.
- Apply the violet→orange gradient text treatment to a maximum of one phrase per section — typically the last 1-3 words of a hero headline that carry the value proposition.
- Use PPNeueMontrealMono 12-14px with 0.02em tracking for any code, command, or technical string — the mono face signals developer-facing content at a glance.
- Reserve #8a05ff Plasma Violet for step indicators, accent icons, and the first word of emphasis — never for backgrounds of primary buttons or large surface fills.
- Set border-radius to 2px on all rectangular elements (cards, inputs, buttons) and 937px only for pill-shaped badges and nav CTAs — the sharp corners are essential to the engineering-document feel.
- Maintain #e3e3e3 at 1px for all structural borders and dividers — this is the single most-used color in the system and defines the grid.

### Don't

- Do not use pure #000000 for body text or primary buttons — use #0d0d0d; the slight warmth prevents the harsh contrast of pure black on white.
- Do not apply the brand violet (#8a05ff) as a large fill or background — keep it to accents under 40px and to step indicators; overuse dilutes its signaling power.
- Do not use the chromatic accent colors (coral, fuchsia, sky blue) as functional UI colors — they are decorative illustration tones, not status or category indicators.
- Do not introduce a second heading font — Roobert carries all display type; mixing faces breaks the two-font (display + UI + mono) discipline.
- Do not add drop shadows or elevation to cards or panels — the system relies on hairline borders and surface tint, not shadow depth, for hierarchy.
- Do not use border-radius above 4px on any rectangular component — the 2px standard is a defining trait; rounded corners would push the system toward generic SaaS softness.
- Do not center-align body text or feature descriptions — left-align is the norm; centering is reserved for hero headlines and the notification banner.

## Components

### Primary Dark Button

Filled #0d0d0d button with white text, 2px radius, 20px horizontal padding and 10px vertical padding. PPNeueMontreal 16px weight 500. Optional right-arrow chevron in white. Used for 'Start for free' and 'Get Started' — the dark fill against white canvas creates the strongest possible contrast emphasis without resorting to chromatic color.

### Ghost Outline Button

Transparent fill with 1px #0d0d0d border, 2px radius, same padding as primary. PPNeueMontreal 16px weight 500 in #0d0d0d. Used for 'Get in touch' beside the hero primary. The outlined treatment signals secondary hierarchy without introducing a second fill color.

### Pill Navigation CTA

Fully rounded (937px radius) #0d0d0d fill with white text. PPNeueMontreal 14px weight 500, 10px 16px padding. Distinct from the rectangular hero buttons — the pill shape signals 'quick entry point' in the persistent header context.

### Step Indicator Badge

8x8 or 10x10 square (2px radius) filled with #8a05ff Plasma Violet, containing a white numeral in PPNeueMontrealMono 12px weight 500. The violet square against the white page is the most prominent use of brand color in the system — reserved for numbered processes to make the sequence scannable.

### Logo Cloud Bar

Full-width section with logos in #0d0d0d on white, arranged in a responsive grid (5 columns visible). No cards or containers — logos float directly on the page background. Generous vertical padding (80px+) separates this band from surrounding sections.

### Feature Card

White surface on white page, no card shadow or fill. Content separated by typography and spacing alone. 2px radius on any embedded UI elements (input fields, dropdowns shown in illustrations). Uses generous left-aligned text with 20-24px element gaps between heading, description, and visual.

### Terminal Badge

#272727 Carbon background, 2px radius, PPNeueMontrealMono 14px weight 400, white text. 6-8px vertical padding, 10-12px horizontal. The dark mono badge is the signature developer credibility marker — a small block of code language embedded directly in marketing copy.

### Top Notification Banner

Thin (1px) strip with a subtle gradient background (violet to warm). PPNeueMontreal 12px weight 400 in white text. Centered or left-aligned content with inline link and optional CTA. This is the only place where the gradient system appears at a structural level.

### Header Navigation

White background with no border or shadow — sits directly on the page canvas. Logo left, nav links center (PPNeueMontreal 14px weight 500, #0d0d0d), contact/sign-in/CTA right. Sticky behavior implied. No dropdown menus visible at the top level.

### Illustration Panel (Product Mockup)

Light #e6daff Wisteria Tint background panel with floating product UI cards inside. The cards are white with 2px radius and thin #e3e3e3 borders, containing miniature line charts, status badges, and service names. The tinted background creates a 'stage' for the product preview without using heavy elevation.

### Dropdown / Select Input

White fill, 1px #e3e3e3 border, 2px radius. PPNeueMontreal 14px weight 400 in #0d0d0d for value text, #6b6b6b for placeholder. 10-12px padding. No focus ring visible in static state — relies on border darkening to #0d0d0d on interaction.

### Status Badge (Success/Deploying)

Pill shape (9999px) with light tinted background and dark text. E.g., 'Deploying' uses #e3e3e3 fill with #0d0d0d text; 'Available' uses #dffeed fill (very light green) with #006d4c text. PPNeueMontrealMono 12px. These appear inside illustration panels to show live product states.

### Metric Sparkline

2px stroke line chart in #8a05ff Plasma Violet, 60-80px wide, 24-32px tall. No axis labels or gridlines. Appears inside service cards in the hero illustration to suggest live monitoring without literal chart furniture.

## Similar Design Systems

- {'why': 'Same achromatic white canvas with hairline gray borders, dark-filled primary CTAs, and a single brand accent color (Vercel uses black, Render uses violet) — both present developer infrastructure as quiet, document-like surfaces', 'business': 'Vercel'}
- {'why': 'Both use whisper-weight display type (Linear at 400-500, Render at 300) with aggressive negative tracking, creating architectural headlines; both rely on hairline borders and zero drop shadows for hierarchy', 'business': 'Linear'}
- {'why': "Similar gradient-text hero treatment (Stripe uses gradient on key nouns, Render uses violet→orange gradient on 'apps & agents'); both use clean geometric sans-serifs with tight tracking and minimal chromatic UI", 'business': 'Stripe'}
- {'why': 'Both target developers with mono-font code badges, terminal aesthetics, and purple/violet brand accents; both present infrastructure-as-a-service as precise, almost schematic interface panels', 'business': 'Railway'}
- {'why': 'Shared developer-infrastructure visual language: white canvas, hairline borders, violet brand accent, monospaced code elements, and weight-300 display headlines that let the product UI illustrations do the visual heavy lifting', 'business': 'Planetscale'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #0d0d0d
- background: #ffffff
- border: #e3e3e3
- accent: #8a05ff (Plasma Violet)
- gradient text: #8a05ff → #d67f2e
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. **Hero section**: White background. Headline 'Your fastest path to production for apps & agents' in Roobert 80px weight 300, #0d0d0d, letter-spacing -0.03em, line-height 1.0. The phrase 'apps & agents' uses a gradient fill from #8a05ff to #d67f2e. Subtext in PPNeueMontreal 18px weight 400, #4d4d4d. Two buttons: primary 'Start for free' (filled #0d0d0d, white text, 2px radius, 10px 20px padding, PPNeueMontreal 16px weight 500, optional right chevron), and secondary 'Get in touch' (transparent fill, 1px #0d0d0d border, same padding and type).

2. **Three-step process card**: White surface, no shadow. Violet 8x8 square (2px radius, #8a05ff fill) with white '1' in PPNeueMontrealMono 12px weight 500. Heading 'Select a service' in Roobert 32px weight 300, #0d0d0d, letter-spacing -0.01em. Body text in PPNeueMontreal 16px weight 400, #4d4d4d, 1.5 line-height. Below: a mini illustration of a dropdown with 2px radius, 1px #e3e3e3 border, PPNeueMontreal 14px text.

3. **Terminal code badge**: Inline element. 6px 12px padding, #272727 background, 2px radius. Text '$ git push' in PPNeueMontrealMono 14px weight 400, #ffffff, letter-spacing 0.02em. Use this badge floating near hero illustrations to signal developer context.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

5. **Product illustration panel**: #e6daff Wisteria Tint background, 2px radius, 20px padding. Inside: 3-4 white product cards (2px radius, 1px #e3e3e3 border, 16px padding) each containing a service name in PPNeueMontrealMono 12px, a 'Deploying' or 'Available' status pill, and a 2px Plasma Violet sparkline chart. This panel sits to the right of the hero headline in a 2-column layout.

## Type System Philosophy

Render's type system operates on three tiers with strict role separation. **Roobert** (300, 400) carries all display and heading work — its light weight at 64-80px creates the signature whisper-voice headline. **PPNeueMontreal** (400, 500) handles all UI and body content with workmanlike neutrality. **PPNeueMontrealMono** (400, 500) appears only for code, commands, and step numbers. Letter-spacing tightens aggressively with size: -0.01em at body sizes, -0.02em at 40-48px, -0.03em at 80px. Line-heights compress to 1.0-1.1 at display sizes (creating tight, architectural headlines) and open to 1.4-1.5 at body sizes. The mono face uses positive tracking (0.02-0.025em) to improve readability of technical strings at small sizes. Never mix more than these three faces on a single screen.
