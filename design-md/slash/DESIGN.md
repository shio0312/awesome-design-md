# Slash — Design System

> **North Star**: Midnight vault with gilded ledger lines.
> **Theme**: dark
> **Source**: https://www.slash.com
> **Refero Style**: https://styles.refero.design/style/7c38e84b-aea0-4c8f-b3e9-60b994ee6c6b
> **Synced**: 2026-09-01

## Overview

Slash operates in a midnight gallery mode: an almost-black canvas, white type, and a single warm copper accent that functions as editorial punctuation. Display headings are set in Ivy Presto, a high-contrast didone serif used at extreme sizes (up to 88px) — this serif-versus-sans collision is the system's signature, lending financial seriousness without the stockbroker gravitas of traditional banking. The rest of the UI is deliberately quiet: thin borders, pill-shaped controls, compact 16px body text, and barely-there elevation that lets the serif breathe. A single golden gradient (chart line, micro-accents) injects warmth into an otherwise monochrome system, evoking the warm glow of a Bloomberg terminal rendered for a design audience.

## Color Palette

- **Obsidian**: `#08080a` — Page canvas, footer background, deepest surface — near-black with the faintest blue undertone [neutral]
- **Onyx**: `#040406` — Card surface, secondary backdrop — one step deeper than the page for visual weight [neutral]
- **Carbon**: `#121317` — Elevated panels, subtle UI fills — the first clearly lighter step in the surface stack [neutral]
- **Graphite**: `#1c1d22` — Borders, dividers, icon containers, slider controls — the hairline color that defines structure [neutral]
- **Slate**: `#2e3038` — Secondary borders, muted icon strokes, subtle dividers between content blocks [neutral]
- **Smoke**: `#464853` — Tertiary borders, inactive nav items — barely visible structural lines [neutral]
- **Ash**: `#5e616e` — Muted body text, placeholder content, secondary metadata [neutral]
- **Steel**: `#777a88` — Button borders, icon strokes, secondary text, ghost button outlines [neutral]
- **Fog**: `#9194a1` — Nav text, body descriptions, helper text — the workhorse readable gray [neutral]
- **Mist**: `#acafb9` — Subdued body copy, supplementary text, less-emphasized paragraphs [neutral]
- **Silver**: `#c7c9d1` — Light body text, medium-emphasis paragraphs, secondary headings [neutral]
- **Bone**: `#e2e3e9` — High-emphasis body text, dense data labels, the default text tone across most UI [neutral]
- **Paper White**: `#ffffff` — Primary action button fill, headings, nav active state — the highest contrast color, reserved for elements that must command attention [neutral]
- **Copper**: `#cc9166` — Category labels, editorial links, warm accent punctuation — the only chromatic color, used sparingly to mark curated content and category tags [accent]
- **Gilded Gradient**: `#ae9357` — Chart line stroke, financial data visualization accent — a warm gold-to-cream gradient that brings the only color energy to data displays [accent]

## Typography

- **Ivy Presto**
- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| eyebrow | 13 | — | 1 |
| body-xs | 16 | — | 1.5 |
| body-sm | 18 | — | 1.38 |
| body | 20 | — | 1.38 |
| subheading | 24 | — | 1 |
| heading-sm | 44 | — | 1.38 |
| heading | 52 | — | 1.13 |
| heading-lg | 64 | — | 1.13 |
| display | 88 | — | 1 |

## Spacing & Layout

- **Max Width**: 1216px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 160px
- **Border Radius**: {'nav': '2px', 'tags': '9999px', 'cards': '10px', 'icons': '9999px', 'inputs': '9999px', 'buttons': '9999px'}

## Layout

Max-width 1216px centered content with 160px vertical section gaps. The hero is a full-width dark canvas with a split composition: left-aligned serif headline at 64–88px with email capture below, and a large product UI card (the dashboard screenshot) on the right at 50% width. Subsequent sections use a single-column centered headline (serif at 44–64px) with subtitle in Inter, followed by 3-column card grids for features/testimonials/blogs. Navigation is a fixed top bar: logo left, center menu (Company, Products, Solutions, Customers, Pricing, FAQ), right-aligned Sign in (ghost) and Get Started (white filled pill). Footer is a dense 5-column link grid with company info and legal. The page alternates between content-rich grid sections and full-bleed stat callouts — rhythm is established by generous whitespace between bands, not by alternating background colors (the entire page is one continuous #08080a canvas).

## Surfaces / Elevation

- **Void**
- **Card**
- **Panel**
- **Floating**

**Shadow tokens:**

## Imagery

Photography is editorial and naturalistic: warm-toned portrait shots of founders and team members in their actual work environments (offices, living rooms, construction sites). Images fill card frames edge-to-edge with no padding. A dark gradient overlay is applied to the bottom portion of testimonial cards for text legibility. The aesthetic is 'LinkedIn meets editorial magazine' — candid, human, slightly desaturated, never stock-photo polished. Article thumbnails mix photography with illustrated concepts (a man standing on a labyrinth, a fireplace with money bags). Product UI is shown in dark mode at full opacity, floating above the page on subtle dark surfaces — these are the hero's centerpiece. Icons are monochrome with 1px strokes in #2e3038 or #777a88, never filled with brand color.

## Design Principles

### Do

- Use Ivy Presto for all display and heading text at 28px and above — never for body copy under 20px.
- Set body text at 16px Inter weight 400 with line-height 1.5 in #e2e3e9 (Bone) — this is the default readable tone.
- Use the white (#ffffff) filled pill button exclusively for the single most important action on each screen — it is a scarce visual resource.
- Apply Copper (#cc9166) only to category labels and editorial links — never to buttons, icons, or large text blocks.
- Use 1px borders in #1c1d22 or #2e3038 for card and table edges; never use drop shadows for elevation.
- Space sections with 160px vertical gaps on desktop — the generous breathing room lets the serif headlines dominate.
- Use 9999px border-radius for all buttons, inputs, tags, and status indicators; use 10px for cards and 2px for nav underlines.

### Don't

- Don't substitute Inter for Ivy Presto on display text — the serif/sans contrast is the brand's identity, not decoration.
- Don't introduce blue, green, or any chromatic color as a brand accent — Copper is the only warm note in the palette.
- Don't use the white filled button more than once per viewport — its power diminishes with repetition.
- Don't add drop shadows to cards, modals, or popovers — use surface color steps and 1px borders instead.
- Don't set body text larger than 20px in Inter — larger sizes belong in Ivy Presto.
- Don't use #ffffff for long-form body copy — switch to #e2e3e9 (Bone) to reduce eye strain on dark backgrounds.
- Don't apply the gilded gradient outside data visualization contexts — it is reserved for chart lines and financial data accents.

## Components

### Primary Action Button

Pill-shaped, 9999px radius. White (#ffffff) fill, black (#000000) text at 14px Inter weight 500. Padding 10px 20px. Used for 'Get Started' CTAs in header and hero. No border. The white-on-black inversion is the system's only loud visual signal — treat it as a rare resource.

### Ghost Outline Button

Transparent fill with 1px white (#ffffff) border, 9999px radius. White text at 14px Inter weight 500. Padding 10px 20px. The 1px outline defines shape without filling — used for 'Sign in' and less-critical actions.

### Pill Tag Button

Transparent background, 1px border in #777a88, 9999px radius, padding 6px 10px. White text at 12–14px Inter. Smaller and more subdued than action buttons — the border color is intentionally cool gray, not white, to read as secondary.

### Hero Chart Card

Dark surface (#040406) with 10px radius. No visible border. Contains a balance header, period filter pill, a golden gradient line chart, and a spend-limit input field. The chart line uses the gilded gradient (linear-gradient 103deg) as its stroke — this is the only place where the copper/gold accent animates the page.

### Transaction List Card

Right-side panel in hero, 10px radius, transparent fill. Contains rows with brand-color icon avatars (Meta blue, Adobe red, Stripe purple, Amazon orange, Etsy orange). Each row: icon well (1px border #2e3038, 9999px) + merchant name + amount right-aligned. Dense vertical rhythm with 2px internal padding.

### Testimonial Video Card

10px radius, image-fill background with a dark gradient overlay for text legibility. White text overlay at bottom: name in 16px Inter weight 500, title/company in smaller muted text. No border. The image fills 100% of the card area — text sits on a bottom-aligned gradient mask.

### Blog Post Card

10px radius, transparent fill. Top: image at native aspect ratio. Below: category eyebrow in Copper (#cc9166) at 13px Inter weight 600, date separator, then title in 18–20px Inter weight 500 in white. Read-time meta at bottom in #acafb9. No border — cards separate through whitespace alone.

### Email Capture Input

Transparent fill, 1px white (#ffffff) border, 9999px radius. Padding 10px 10px 10px 20px. Placeholder text in #777a88. The pill shape matches the primary button — the input and the 'Get Started' button are designed to read as a single unit, with the input's left padding larger to offset the button's visual weight on the right.

### Navigation Link

No background, no border. Text at 14px Inter in #9194a1 (inactive) or #ffffff (active/hover). Dropdown chevron for items with sub-menus (Company, Products, Solutions). Padding 6px 10px for click target. 2px underline radius on hover indicators.

### Status Badge — Active

Small pill, transparent fill with 1px green-toned border. Text in green at 12px Inter weight 500. 9999px radius, 2px vertical padding. The green is a desaturated sage that reads on dark without vibrating.

### Stat Display

Number in 28–44px Ivy Presto weight 400, white. Caption below in 14px Inter weight 400 in #9194a1. Example: '10,000+' headline number with 'businesses' label. The serif numeral creates editorial gravitas for statistics.

### Category Eyebrow

13px Inter weight 600, letter-spacing -0.02em. Copper (#cc9166) for blog categories, #9194a1 for section types. Functions as a typographic period before each content block — a small, precise label that sets up what follows.

### Data Table Row

Transparent fill, 1px bottom border in #1c1d22. No row padding between cells — density is high. Column headers in #9194a1 at 14px. Cell values in #e2e3e9 at 14–15px. Right-aligned numerics. The table relies on hairline dividers, not card containers.

## Similar Design Systems

- {'why': 'Same dark-canvas fintech aesthetic with a single warm accent and serif/sans display pairing — both use generous whitespace, pill-shaped controls, and hairline borders rather than shadows.', 'business': 'Mercury'}
- {'why': 'Shares the midnight-black surface stack, single-accent palette philosophy, and the use of a high-contrast serif for hero headlines to differentiate from generic SaaS fintech.', 'business': 'Arc'}
- {'why': 'Similar compact density, dark mode default, and 9999px pill buttons — though Brex leans more colorful and brand-illustrated, where Slash is monochrome with copper punctuation.', 'business': 'Brex'}
- {'why': "Comparable card-grid layouts and 1216px content width, but Ramp's palette is warmer and more saturated; Slash's is closer to a Bloomberg terminal with editorial restraint.", 'business': 'Ramp'}
- {'why': "Both achieve premium fintech feel through typography discipline and hairline borders over heavy shadows, though Stripe's gradient system is more visible and Slash is nearly monochrome.", 'business': 'Stripe'}

## Agent Prompt Guide

Quick Color Reference:
- text: #e2e3e9 (body) / #ffffff (headings, emphasis)
- background: #08080a (page) / #040406 (card) / #121317 (panel)
- border: #1c1d22 (hairline) / #2e3038 (secondary)
- accent: #cc9166 (Copper — editorial links, category labels)
- primary action: #ffffff (filled action)
- chart accent: gilded gradient (rgb(174,147,87) → rgb(255,240,204))

Example Component Prompts:

1. Create a hero section: #08080a background, max-width 1216px centered. Left column: 88px Ivy Presto weight 400 white headline with 0.01em tracking, 20px Inter weight 400 #9194a1 subtext. Below: a pill-shaped email input (transparent fill, 1px white border, 9999px radius, 10px 20px padding, #777a88 placeholder) joined to a white filled pill button (9999px radius, #000000 text at 14px Inter weight 500, 10px 20px padding). Right column: a dashboard card at #040406 with 10px radius showing a balance number (48px Inter weight 500 white), filter pill, and a golden gradient line chart.

2. Create a 3-column blog card grid: each card with 10px radius, transparent fill, no border. Top: image filling the card width. Below: Copper (#cc9166) category label at 13px Inter weight 600, date in #9194a1 at 13px, title in 20px Inter weight 500 white at 1.38 line-height. Read-time meta at bottom in #acafb9. Cards separated by 16px column gap and 32px row gap.

3. Create a testimonial video card: 10px radius, full-bleed background photo with a 40% black-to-transparent gradient overlay at the bottom. Overlay text: name in 16px Inter weight 500 white, title/company in 14px Inter weight 400 #acafb9. Card aspect ratio 4:3. No border, no shadow.

4. Create a data table for spend limits: transparent background, 1px bottom border in #1c1d22 on each row. Column headers in #9194a1 at 14px Inter weight 500, cell values in #e2e3e9 at 15px Inter weight 400. Right-aligned monetary values. Status column uses a pill badge: 9999px radius, 1px border, 12px Inter weight 500 text.

5. Create a stat callout section: centered layout. Large number in 44px Ivy Presto weight 400 white, caption below in 14px Inter weight 400 #9194a1. 160px vertical padding above and below. Single column, max-width 600px.

## Serif/Sans Collision System

The defining structural choice is the pairing of Ivy Presto (a high-contrast didone serif) exclusively for headings 28px and above with Inter for all UI text below that threshold. This creates a two-tier typographic register: the serif speaks to editorial and aspirational moments (hero, section titles, large numbers), the sans handles functional and informational moments (body, labels, buttons). Never cross the boundary — serif never goes below 28px, sans never goes above 48px. The slight positive tracking on Ivy Presto (0.01em) gives it a printed, almost engraved quality, reinforced by the copper accent and gilded gradient that evoke financial ledgers and gold leaf.
