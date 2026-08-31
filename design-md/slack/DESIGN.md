# Slack — Design System

> **North Star**: Aubergine stage with white spotlights. Deep plum dominates dark sections while a near-white canvas lets oversized Avant-Garde headlines breathe.
> **Theme**: light
> **Source**: https://slack.com
> **Refero Style**: https://styles.refero.design/style/e26cb9b0-f876-41ff-9f24-fd67a6b9776c
> **Synced**: 2026-09-01

## Overview

Slack's design language balances a near-white canvas with concentrated pools of aubergine purple — the brand color appears sparingly as CTA fills, dark hero sections, and gradient text highlights while the majority of the page stays airy and monochrome. Type is split into two voices: a geometric display face (Avant-Garde) for oversized headlines at 64-96px, and a humanist sans (Sans) for everything else, keeping body copy at a comfortable 16px. Sections alternate between flat white, faintly lilac washes (#f9f0ff), and fully inverted purple bands, with 16px-radius cards floating over a very subtle 32px ambient shadow. The interface stays quiet so product UI screenshots — rendered in authentic Slack brand chrome — can carry the visual weight.

## Color Palette

- **Aubergine**: `#611f69` — Filled CTA buttons, primary navigation fills, dark hero backgrounds — the brand's signature mid-plum, dense enough to ground without veering black [brand]
- **Deep Plum**: `#481a54` — Largest canvas inversion — full-bleed dark section backgrounds, decorative dark blocks, surface for headline text on white sections [brand]
- **Purple Haze**: `#f9f0ff` — Softest lilac wash for body backgrounds, pill fills, and card surfaces — the quiet brand tint that never competes with text [accent]
- **Lavender Mist**: `#eac8fe` — Mid-saturation lavender for card borders, decorative outlines, and pill borders — bridges white and purple without harsh contrast [accent]
- **Vivid Violet**: `#9602c7` — Headline accent text and gradient text fills on dark sections — the bright punch of color that makes key phrases feel switched on; Diagonal black-to-violet gradient for accent text and decorative text fills on dark sections [accent]
- **Plum Shadow**: `#3d0157` — Darker plum for button text and shadow tones on aubergine surfaces — reads as near-black against purple fills [brand]
- **Iris**: `#730394` — Secondary purple for background fills and link accents — sits between Aubergine and Vivid Violet on the purple ramp [brand]
- **Iris Light**: `#d17dfe` — Decorative card text and bright accents inside feature cards — a lighter iris that adds lift without losing brand identity [accent]
- **Channel Blue**: `#1264a3` — Slack's channel-link blue for in-product references, sidebar highlights, and hyperlink color — appears inside product UI screenshots, not marketing chrome [accent]
- **Mid Blue**: `#0b4c8c` — Blue text accent for links, tags, and emphasized short phrases. [accent]
- **Sky Mist**: `#2f8ab7` — Decorative illustration backgrounds — soft secondary blue used only inside graphic blocks [accent]
- **Carbon**: `#1d1c1d` — Primary body and nav text — Slack's near-black that reads warmer than pure #000 at small sizes [neutral]
- **Charcoal**: `#454245` — Secondary body text, icon fills, muted captions — the middle step between Carbon and Mid Gray [neutral]
- **Mid Gray**: `#696969` — Navigation text, subdued labels, disabled-state text — the working neutral for chrome [neutral]
- **Steel**: `#808080` — Placeholder card backgrounds and neutral fill swatches [neutral]
- **Fog**: `#edeaed` — Hairline borders, divider lines, subtle 1px separators — the structural neutral that holds cards together [neutral]
- **Pure White**: `#ffffff` — Primary surface — card backgrounds, text on dark, pill fills, button text on purple [neutral]
- **Soft White**: `#fefbff` — Page canvas — faintly lilac-tinted white that sets the page apart from harsh #fff [neutral]
- **Ice Blue**: `#e8f5fa` — Cool-tinted surface wash for secondary panels and nav highlights [neutral]
- **Black**: `#000000` — Headline text on light sections, icon fills, deepest emphasis — used at display sizes where maximum weight is needed [neutral]

## Typography

- **Salesforce-Avant-Garde**
- **Salesforce-Sans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| eyebrow | 12 | — | 1.5 |
| caption | 14 | — | 1.56 |
| body-sm | 16 | — | 1.5 |
| body | 18 | — | 1.56 |
| subheading | 32 | — | 1.25 |
| heading-sm | 50 | — | 1 |
| heading | 64 | — | 1.12 |
| heading-lg | 76 | — | 1.2 |
| display | 96 | — | 1.08 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8-12px
- **Section Gap**: 80-100px
- **Border Radius**: {'tags': '4px', 'cards': '16px', 'pills': '999px', 'badges': '90px', 'buttons': '4px'}

## Layout

Max-width 1200px centered content with sections that break full-bleed. Hero is a centered stack: oversized headline at 64px/700, subtitle at 18px, twin CTAs (filled + ghost), then trust-logo strip, then a large product screenshot card floating below. Section rhythm alternates: white canvas → inverted #481a54 dark band → white canvas → light #f9f0ff wash. Feature sections use a split layout — text-left at ~45% width paired with a product screenshot card-right at ~50%, with vertical centering. Card grids use 3-column layouts for feature cards with lavender borders. Navigation is a sticky top bar that floats with subtle shadow on scroll, containing logo + 5-item menu + search + sign-in + filled CTA. The overall vertical rhythm uses ~96px section gaps to let oversized headlines breathe between bands.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Wash**
- **Cool Wash**
- **Inverted**

**Shadow tokens:**

## Imagery

Imagery is overwhelmingly product-UI screenshots — authentic Slack app windows rendered at scale with real channel chrome, avatars, and message threads. These screenshots sit inside floating cards with 16px radius and a 32px ambient shadow. Secondary imagery is logo lockups for 'Trusted by' social proof (GM, OpenAI, Target, Paramount, Stripe, IBM — all rendered as grayscale SVG wordmarks). The dark hero band uses minimal geometric ornament — scattered white four-point star shapes and soft radial color washes (pink, blue, green, yellow at 25% opacity) at the edges. No lifestyle photography, no human imagery, no illustrations outside the product UI context. The object-as-hero approach means screenshots occupy 40-60% of viewport width on most feature sections.

## Design Principles

### Do

- Use #611f69 for filled CTAs only — never as background fills for hero sections or large surfaces; reserve #481a54 for those.
- Set display headlines at 64-96px using Salesforce-Avant-Garde with -0.012em tracking; the compressed wide forms are what make Slack's hero feel architectural.
- Apply the gradient text fill (black → #ba01ff) to single keywords inside white-section headlines — not to entire headlines or body copy.
- Use 16px radius on all cards and content surfaces; pair with 1px lavender (#eac8fe) borders instead of heavy shadows for the default card state.
- Reserve the 32px ambient shadow (rgba(0,0,0,0.1) 0px 0px 32px 0px) for product screenshot cards and floating overlays only — not for static content cards.
- Alternate white canvas sections with #481a54 dark hero bands to create rhythm; use #f9f0ff as a quieter mid-tone when transitioning without full inversion.
- Set eyebrow labels at 12px/700 with 0.057em uppercase tracking — this is the tag pattern for 'New Feature' and section categories.

### Don't

- Do not use pill-radius (999px) on primary CTA buttons — Slack's filled actions are always rectangular with 4px corners.
- Do not apply the #eac8fe lavender border to product screenshot cards — those need white or transparent backgrounds to let the embedded UI breathe.
- Do not use Vivid Violet (#9602c7) or Iris Light (#d17dfe) for body text on white backgrounds — contrast ratios are too low; reserve for dark-section accents and card-only contexts.
- Do not mix Channel Blue (#1264a3) into marketing-page CTAs — that blue belongs inside Slack product UI screenshots, not the marketing chrome.
- Do not add drop shadows to text inside the dark hero band; the band itself provides enough contrast.
- Do not use gradient fills on UI surfaces (buttons, cards, inputs) — the gradient treatment is text-only and decorative.
- Do not set body copy below 14px or above 18px; the 16px/1.5 lineHeight is the working standard for readability across marketing and feature copy.

## Components

### Primary CTA Button (Aubergine Fill)

Filled rectangle in #611f69 with white text at 16px/700, 4px radius, 19px top / 20px bottom / 40px horizontal padding. The signature Slack button — compact, rectangular, never pill-shaped at this scale.

### Ghost CTA Button

Transparent background, #3d0157 text, 4px radius, same vertical/horizontal padding as primary. Border-less; relies on color contrast alone to signal actionability.

### Nav Pill Button

Transparent background, #3d0157 text, 90px (full pill) radius, 12px square padding. Used for compact nav-level triggers like feature toggles.

### Header Request Demo Link

Transparent background, #1d1c1d text, no border, 4px radius. Sits inline with primary nav, visually subordinate to the filled CTA.

### Sign In Link

Transparent background, #1d1c1d text, sits in nav utility area. Styled as a plain link with no chrome.

### Feature Card (Lavender Border)

Transparent background, 1px #eac8fe border, 16px radius, no shadow. The 'card' variant that defines Slack's quiet card language — border over fill, no elevation.

### Product Screenshot Card

Transparent or #808080 background, 16px radius, floating with rgba(0,0,0,0.1) 0px 0px 32px 0px shadow. Houses authentic Slack app screenshots — these carry visual weight that marketing cards don't.

### Floating Sticky Nav

White background (#ffffff), 0.08 shadow on scroll (rgba(0,0,0,0.08) 0px 1px 3px), rounded bottom corners, 80px height. Becomes elevated with 0px 5px 20px rgba(0,0,0,0.1) on active state.

### Eyebrow Label / Tag

12px Salesforce-Sans / 700, uppercase, 0.057em tracking. Used for 'New Feature', 'Partner Apps MCP' tags above feature cards.

### NEW Badge

Small inline badge, #0b4c8c text on light fill, pill or rounded-rect shape. Marks recently launched features.

### Ask Slackbot Pill

Dark plum fill (#3d0157 or near-black), white text, fully rounded, sits above section as a prompt trigger.

### Gradient Text Highlight

Specific words within display headlines use the black-to-violet linear-gradient fill (#000 → #ba01ff). Creates the 'this word is special' effect without color noise.

### Dark Hero Band

#481a54 background, white text at 64px/700, soft radial color washes (pink, blue, green, yellow at 25% opacity) decorating edges. Inverted canvas that breaks the white-page rhythm.

### Star-spark Decoration

White four-pointed star shapes scattered against #481a54 — minimal geometric ornament, no gradients or glow.

## Similar Design Systems

- {'why': 'Same split between geometric display headings and humanist body sans, same restrained use of a single saturated brand color against near-white canvas, same rectangular-not-pill primary buttons with 4px radius', 'business': 'Linear'}
- {'why': 'Similar dark hero band alternating with white canvas rhythm, oversized condensed headlines that let the canvas breathe, product-UI screenshots doing the visual heavy lifting instead of lifestyle photography', 'business': 'Notion'}
- {'why': 'Shared pattern of gradient-text keyword emphasis inside large display headlines, lavender/purple accent borders on feature cards, rectangular filled CTAs in a single brand hue', 'business': 'Webflow'}
- {'why': 'Identical layout grammar — centered hero stack with twin CTAs, product screenshot card floating below, 3-column feature grids with bordered cards, alternating light/dark section bands', 'business': 'Stripe'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #1d1c1d (primary), #454245 (secondary), #696969 (muted)
- background: #fefbff (canvas), #ffffff (card), #f9f0ff (wash), #481a54 (dark band)
- border: #edeaed (hairline), #eac8fe (lavender card border)
- accent: #9602c7 (gradient text), #d17dfe (card accent)
- primary action: #611f69 (filled action)

**Example Component Prompts**

1. Create a Primary Action Button: #611f69 background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

2. **Feature Card with Lavender Border**: Transparent background, 1px #eac8fe border, 16px radius, 24px padding. Eyebrow label at 12px/700 uppercase with 0.057em tracking in #696969. Heading at 22px Salesforce-Avant-Garde weight 600, #1d1c1d. Body at 16px/1.5 Salesforce-Sans, #454245.

3. **Product Screenshot Card**: #ffffff background, 16px radius, padding 0, with rgba(0,0,0,0.1) 0px 0px 32px 0px shadow. Contains authentic Slack UI screenshot with #4a154b sidebar and white message area. Aspect ratio ~16:10.

4. **Dark Hero Band**: Full-bleed #481a54 background, 96px top/bottom padding. Headline at 64px Salesforce-Avant-Garde weight 700, #ffffff. Body at 18px Salesforce-Sans weight 400, #ffffff at 85% opacity. Decorative white four-point stars scattered at 30% opacity. Optional radial color washes (pink/blue/green/yellow at 25%) at edges.

5. **Sticky Nav Bar**: #ffffff background, 80px height, full-width. Contains logo left, 5-item menu (Features, Solutions, Enterprise, Resources, Pricing) at 15px/700 in #1d1c1d, search icon, 'Sign in' link, and 'Request a demo' filled CTA in #611f69. On scroll: rgba(0,0,0,0.08) 0px 1px 3px 0px shadow appears.

## Gradient System

Gradients are used sparingly and only for text decoration. The signature black-to-violet gradient (linear-gradient(104deg, rgb(0,0,0) 9.56%, rgb(186,1,255) 102.66%)) is applied as a background-clip: text fill on individual keywords within white-section headlines. On dark hero bands, radial color washes at 25% opacity (pink, blue, green, yellow) sit at viewport edges to add warmth without competing with the plum background. No gradients are used on UI surfaces (buttons, cards, inputs) — gradients are text-only and decorative-only in this system.

## Animation Philosophy

Motion personality is expressive: primary duration is 0.42s with ease timing for most UI transitions, while decorative background-swap animations run at 4s and 8s for ambient effects. The cubic-bezier(0.165, 0.84, 0.44, 1) curve appears 40 times — it's the signature ease-out used for reveals and slide-ins. Transitions focus on transform, max-height (for expanding content), and box-shadow (for nav elevation changes). The system favors physical-feeling motion over flat fades.
