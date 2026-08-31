# Intercom — Design System

> **North Star**: Warm cream editorial spread
> **Theme**: light
> **Source**: https://intercom.com
> **Refero Style**: https://styles.refero.design/style/12255b63-e506-4bc1-a4cd-d05487de32f3
> **Synced**: 2026-09-01

## Overview

Intercom's design language reads like an editorial magazine printed on warm cream paper: an off-white canvas (#faf9f6) replaces the cold SaaS gray, all body and display type sits at weight 300 for a whisper-light confidence, and a single vivid violet (#0007cb) does nearly all the chromatic work in small, deliberate doses. Sharp 4px corners on every control reject the rounded-softness trend in favor of architectural precision, and SaansMono at wide tracking acts as a labeling system — the way captions and tags function in print. Serrif at 300 weight appears inside body copy as a quiet editorial counterpoint, the one concession to typographic richness in an otherwise austere system. Components feel weightless: thin hairline borders in warm stone (#dedbd6), no decorative shadows, black-filled primary buttons that anchor without weight.

## Color Palette

- **Electric Violet**: `#0007cb` — Brand accent — used sparingly for emphasis moments, selected icon strokes, and tag punctuation; the only saturated color in the system creates instant focus when it appears against the warm neutral canvas [brand]
- **Pure White**: `#ffffff` — Card surfaces, product screenshot backgrounds, inverted button text [neutral]
- **Canvas Cream**: `#faf9f6` — Primary page canvas — the warm off-white that defines the entire surface temperature; every screen lives on this tone [neutral]
- **Linen**: `#f1eee9` — Secondary surface for sectioned blocks, elevated cards, and alternating content bands — one step warmer than canvas [neutral]
- **Stone**: `#d3cec6` — Decorative texture wash, large background fields, subtle warmth blocks [neutral]
- **Hairline**: `#dedbd6` — Hairline borders, dividers, input outlines, nav separators — the warm border tone that never feels cold [neutral]
- **Ink**: `#111111` — Primary text, headings, body copy — slightly softer than pure black for comfortable reading on cream [neutral]
- **Carbon**: `#000000` — Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color [neutral]
- **Iron**: `#414141` — Secondary text, supporting copy, muted descriptions [neutral]
- **Graphite**: `#585858` — Tertiary text, helper copy, less-prominent body [neutral]
- **Smoke**: `#888888` — Disabled state text, placeholder copy, very muted labels [neutral]
- **Ash**: `#a0a0a0` — Muted headings in secondary contexts, low-emphasis text [neutral]
- **Silver**: `#b8b8b8` — Icon strokes in resting state, low-emphasis glyphs [neutral]

## Typography

- **Saans**
- **SaansMono**
- **Serrif**
- **MediumLL**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.4 |
| body-sm | 14 | — | 1.4 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.25 |
| heading-sm | 24 | — | 1.4 |
| heading | 32 | — | 1.43 |
| heading-lg | 40 | — | 1.25 |
| display | 54 | — | 1 |
| display-lg | 80 | — | 0.95 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24-32px
- **Element Gap**: 8-16px
- **Section Gap**: 64-96px
- **Border Radius**: {'nav': '4px', 'tags': '4px', 'cards': '4px', 'inputs': '4px', 'buttons': '4px'}

## Layout

Intercom uses a max-width 1200px centered container with generous side padding (48–80px). The page rhythm is: thin announcement bar → transparent nav bar → 80px display headline hero (left-aligned, 60% width) with subtext column to the right → horizontal image strip → tabbed product section → 6-column customer logo grid → alternating 2-column editorial feature blocks (text+image, 50/50 split). Section vertical spacing is 64–96px, creating slow, measured scrolling. No full-bleed sections — everything sits within the contained column. Navigation is a single top bar (not sticky in the data shown), with no sidebar or mega-menu complexity. The layout philosophy is editorial-magazine: every section is a 'spread' with clear top and bottom margins, and content alternates which column carries the image.

## Surfaces / Elevation

- **Canvas**
- **Section Warm**
- **Textured Stone**
- **Card White**

## Imagery

Intercom's visual language mixes editorial photography, hand-drawn illustration, and product screenshots with equal weight. Photography tends toward warm, lifestyle-framed human shots (portraits, sunsets, candid scenes) with natural color grading — never stock-clinical. Illustrations are loose, organic, often black-and-white ink-style (sketched figures, abstract line art) that echo the serif typography's humanist warmth. Product screenshots are always presented on warm cream backgrounds, never floating on white, to keep them embedded in the system's tone. The customer logo grid is treated as a quiet social-proof band in muted gray rather than as a visual centerpiece. Overall density is text-dominant — imagery serves as punctuation and atmosphere, not as the hero. Icons throughout are thin-stroke, 1.5px, monochromatic in #111111 or #b8b8b8.

## Design Principles

### Do

- Set all display headlines at weight 300, not 400 or 700 — the whisper-weight is the brand's most recognizable choice
- Use warm cream (#faf9f6) as the default page background, not pure white or cool gray — the warmth is non-negotiable
- Apply SaansMono at 12px with 1.2px letter-spacing for any tag, label, or micro-copy element
- Use black (#000000) for filled primary buttons — never the brand violet, never a tinted neutral
- Apply 4px border-radius universally — buttons, nav, cards, inputs, tags all share the same sharp radius
- Allow display headlines to reach 80px with line-height 0.95 and letter-spacing -2.4px — extreme size at light weight needs the tight tracking to remain readable
- Pair Saans display with Serrif 300 in body copy to create editorial contrast within the same weight register
- Use the vivid violet (#0007cb) sparingly — maximum once or twice per screen, in small functional doses (icons, emphasis links, tag accents)
- Set section vertical gaps at 64–96px to create the slow, editorial page rhythm
- Render all third-party customer logos in grayscale (#b8b8b8 or #888888) to maintain system color discipline

### Don't

- Never set display type at weight 700 or above — the 300-weight whisper is the entire identity
- Never use pure white (#ffffff) as the primary page canvas — always use warm cream (#faf9f6)
- Never apply border-radius above 4px — no 8px, no 12px, no 9999px pills
- Never use cool grays (blue-tinted) for neutrals — all grays must have a warm undertone to live in the cream system
- Never use the brand violet as a button fill — it is an accent, not an action color
- Never use shadows or drop-shadows on cards, buttons, or panels — depth comes from background tone shifts, not elevation
- Never render customer logos in their native brand colors — grayscale only to prevent color pollution
- Never add a hard divider line between sections — let background tone and spacing create separation
- Never set body copy above 20px or below 14px — the editorial scale is tight
- Never use a gradient — the entire system is flat, warm, and untextured except for the surface tone progression

## Components

### Filled Primary Button

Background #000000, text #ffffff, 4px border-radius, padding 14px 16px, Saans 14px/400. No shadow, no gradient — just a solid black block that anchors visually against the warm cream canvas. The starkness of the black-on-cream pairing is the signature.

### Ghost Text Button

No background, text #111111, 4px optional border, padding 14px 16px, Saans 14px/400. Renders as plain text or with a thin outline; never filled. Sits beside the filled primary without competing for weight.

### Outlined CTA Button

White background #ffffff, 1px solid #111111 border, 4px radius, padding 14px 16px, Saans 14px/400 with #111111 text. Used for product-feature CTAs that need to stand apart from the standard filled/ghost pair.

### Announcement Banner

Full-width band, light neutral background (#f1eee9 or #faf9f6), Saans 12–14px body text in #111111 with an inline link underlined. Dismissible with × icon at right. No background color — sits as a quiet info layer.

### Top Navigation Bar

White or transparent over canvas, 4px radius on interactive elements. Left: logo mark + 4 nav items (Product, Customers, Resources, Pricing) with dropdown carets. Right: icon, 'Contact sales', 'View demo', filled black 'Start free trial', outlined 'Fin AI Agent →'. Saans 14px/400, 16px horizontal padding in nav items.

### Hero Display Headline

Saans weight 300, 80px on desktop, 54px tablet, line-height 0.95, letter-spacing -2.4px at 80px, color #111111. Multi-line, left-aligned, fills roughly 60% of viewport width. The whisper-weight at extreme size is the defining Intercom signature — no other SaaS brand uses 300 at this scale.

### Hero Subtext Block

Saans 16px/1.5 or Serrif 16px/1.4 weight 300, color #414141 or #585858, max-width 380–420px. Sits to the right of the headline or below it, constrained to a narrow column to preserve the editorial feel.

### Image Grid Strip

6–7 image tiles in a single horizontal row, each ~120–160px square, full-bleed, no gap or 4px gap. Mix of photography, illustration, and abstract art. Serves as visual texture and social proof of the brand's human side.

### Tab Navigation

Horizontal row of 4 tab labels, Saans 14–16px/400, active tab has a black underline bar (2px) beneath. Inactive tabs in #888888. No background change — the underline is the only state indicator.

### Product Screenshot Panel

Large rounded container (4px radius) holding a product screenshot on a warm background (#f1eee9 or textured). Screenshot itself has subtle internal 4px radius. The warm surround makes the product UI feel embedded, not floating.

### Customer Logo Grid

6-column grid of customer wordmarks, each rendered in #b8b8b8 or #888888 (monochrome gray), no color logos. Saans 16–20px display weight. The grayscale treatment is intentional — it prevents competing brand colors from polluting the warm cream system.

### Two-Column Feature Section

50/50 split. Left column: Saans 300 display headline (40–54px) + body copy (Serrif 16px/300 or Saans 400) + button pair. Right column: editorial illustration or product visual on warm background. Generous 64–96px vertical padding above and below.

### Nav Dropdown Caret

Tiny downward chevron icon, 8px, stroke 1.5px, color #111111. No background, no border — just the glyph appended to nav labels with 6px spacing.

### Section Divider

Invisible — no lines, no gradients. Sections are separated purely by warm background tone shifts (#faf9f6 → #f1eee9 → #d3cec6) and vertical spacing (64–96px). The absence of hard dividers reinforces the editorial flow.

## Similar Design Systems

- {'why': 'Same whisper-weight display typography (300 at large sizes) and sharp 4px-radius controls, though Linear operates in dark mode', 'business': 'Linear'}
- {'why': 'Monochrome restraint with minimal color use, sharp corners, and editorial-feeling display headlines', 'business': 'Vercel'}
- {'why': 'Editorial white-paper aesthetic with warm-neutral backgrounds, restrained color palette, and generous section spacing', 'business': 'Stripe'}
- {'why': 'Flat surfaces, no shadows, warm off-white canvas, and typographic confidence at large display sizes', 'business': 'Notion'}
- {'why': 'Editorial typography choices, warm canvas tones, and willingness to use weight 300 as a brand signature', 'business': 'Arc browser'}

## Agent Prompt Guide

**Quick Color Reference**
- text primary: #111111
- background canvas: #faf9f6
- border hairline: #dedbd6
- accent: #0007cb
- primary action: no distinct CTA color

**3-5 Example Component Prompts**

1. Create a hero section: canvas background #faf9f6. Display headline at 80px Saans weight 300, color #111111, letter-spacing -2.4px, line-height 0.95. Subtext in a 400px column to the right at 16px Saans weight 400, color #414141. Below: filled black button (bg #000000, text #ffffff, 4px radius, padding 14px 16px) + ghost text button (no bg, text #111111) side by side with 8px gap.

2. Create a customer logo grid: 6-column layout, each cell centered, logos rendered at 16px in #b8b8b8 (no native brand colors). 32px row gap, 24px column gap. Section sits on #faf9f6 canvas with 64px padding above and below.

3. Create a tab navigation row: 4 tab labels in Saans 14px/400, active tab has a 2px solid #111111 underline bar, inactive tabs in #888888. Tabs separated by 32px horizontal gap. On a #faf9f6 background, no container border.

4. Create a product screenshot panel: container with 4px border-radius, background #f1eee9 (warm stone), padding 32px. Inside: a product UI screenshot at full container width, internal 4px radius, no shadow. Add a section label above in SaansMono 12px/1.2px tracking, color #585858.

5. Create a two-column editorial feature block: left column (50%) with Saans 54px/300 headline (#111111, letter-spacing -1.62px) + Serrif 16px/300 body copy (#414141) + filled black button. Right column (50%) with an illustration on #f1eee9 background, 4px radius. 96px vertical padding around the entire block.

## Typographic Voice

Intercom's typographic system is defined by what it does NOT do: it never sets display type at weight 700. The entire identity rests on the counterintuitive choice of weight 300 at 80px — a whisper where competitors shout. This creates authority through restraint, not volume. The secondary signature is the SaansMono labeling system: monospace at 12px with 1.2px (100em) letter-spacing creates typographic badges that function like print magazine captions. The Serrif 300 body copy is the third voice — a humanist, almost literary counterpoint that prevents the system from feeling purely corporate. Never mix more than two of these voices on a single screen.
