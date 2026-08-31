# amp — Design System

> **North Star**: warm orange pill on cool white. The design feels like a premium fitness product photographed in a sunlit loft: one object, one accent, one confident typeface doing all the work.
> **Theme**: light
> **Source**: https://ampfit.com
> **Refero Style**: https://styles.refero.design/style/261a4ad3-e835-4f7a-beb7-72187f84d462
> **Synced**: 2026-09-01

## Overview

amp is a single-color, single-typeface system: one warm orange against an achromatic canvas, and one custom sans-serif used at every size. The page reads like a product photography spread — generous whitespace, large editorial headlines, and a single device (the amp column) photographed in a soft beige interior. Orange is rationed: it marks the buy button, the current step indicator, and a thin accent rule. Everything else stays in white, off-white, and near-black, so the accent does the talking. Cards and inputs use small 5px corners; the primary CTA is a 50px pill with a brand-colored glow; secondary controls round to 24px. Typography is one family (PublicaSans) at weights 300/400/500, tightening its tracking aggressively as sizes scale up — -0.036em at display, almost zero at body.

## Color Palette

- **Amp Orange**: `#ff6105` — Primary action fill, active step badge, accent rule, and brand strokes — the only chromatic color in the interface. Used at high contrast on white surfaces (7.0:1 against #ffffff) and as a warm border tint on cards and inputs [brand]
- **Amp Glow**: `#ffa069` — Orange supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Peach Wash**: `#ffdfcd` — Soft highlight surface for featured cards and step accents. A near-gray peach that stays quiet while adding warmth to a card stack [accent]
- **Ink**: `#0a0a0a` — Primary text, logo mark, button text. 19.8:1 against white — the highest-contrast neutral in the stack [neutral]
- **Carbon**: `#292b2a` — Secondary text and nav links, slightly softer than Ink. Icon strokes also draw from this level [neutral]
- **Slate**: `#7a7b7b` — Neutral form states, badge text, and quiet UI feedback where color should stay understated. [neutral]
- **Ash**: `#a2a3a2` — Disabled link text and placeholder-level text — the quietest text tone before disappearing [neutral]
- **Graphite Hairline**: `#e5e5e5` — The dominant border color across the site — dividers, card borders, button outlines, and structural rules. By far the most-used neutral (1628+ borderColor occurrences) [neutral]
- **Fog**: `#dfe0df` — Soft border for cards and body blocks where #e5e5e5 reads as too crisp against off-white [neutral]
- **Bone**: `#e5e7eb` — Neutral button fill (88 occurrences) — the ghost/secondary button background. A light step above canvas [neutral]
- **Canvas White**: `#ffffff` — Page background, card surfaces, button text on dark and orange fills. The base of the surface stack [neutral]
- **Linen**: `#f3f4f3` — Off-white alt surface — secondary button fills and surface tints where pure white is too clinical [neutral]
- **Charcoal**: `#202120` — Dark elevated surface for cards, headers, and contained panels. [neutral]
- **Smoke**: `#3c3e3d` — Heading underline accent in dark sections, heavier than Carbon [neutral]

## Typography

- **PublicaSans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.56 |
| subheading | 18 | — | 1.5 |
| heading-sm | 24 | — | 1.33 |
| heading | 32 | — | 1.22 |
| heading-lg | 48 | — | 1.2 |
| display | 72 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 5-8px
- **Section Gap**: 80px
- **Border Radius**: {'nav': '40px', 'cards': '5px', 'images': '8px', 'inputs': '50px', 'buttons-small': '8px', 'buttons-primary': '50px', 'buttons-secondary': '24px'}

## Layout

Max-width 1200px centered, with full-bleed sections that break out for product photography and dark feature bands. Hero is a full-viewport product image with a single Buy Now CTA pill anchored at the bottom-center. The 'How to use amp' section uses a 2-column layout (50/50) — step list left, phone mockup right. The press strip is a single horizontal row. The dark feature band ('Designed to move you') is a full-bleed photo with a centered headline and accent rule. Vertical rhythm is generous: 80-120px between sections. Navigation is a simple top bar with no sidebar or mega-menu. The system favors centered stacks and split text+image compositions over asymmetric or grid-heavy layouts.

## Surfaces / Elevation

- **Canvas**
- **Linen**
- **Bone**
- **Peach Wash**
- **Charcoal**

**Shadow tokens:**

## Imagery

Full-bleed product photography is the dominant visual asset — the amp column photographed in a warm beige interior with soft directional lighting. No lifestyle scenes, no people-only shots, no illustration system. Phone mockups appear in onboarding sections, framed by Peach Wash cards. Image radius is 8px consistently. The product is always shot isolated on a neutral surface — the object IS the hero. Press logos in the social proof band are desaturated to single-tone Ink.

## Design Principles

### Do

- Use #ff6105 only for the primary CTA fill, the active step badge, the accent rule, and key brand strokes — never for body text or large background washes.
- Set display headlines at 48-78px in weight 300 with tracking between -0.030em and -0.036em; this is the signature editorial moment of the system.
- Round the primary CTA to 50px, secondary buttons to 24px, and cards to 5px — the radius ladder (5 / 8 / 24 / 32 / 50) defines component hierarchy.
- Apply the two-layer shadow stack (orange glow + neutral 1px lift) only to the primary CTA — no other element should carry elevation.
- Stack the surface ladder in this order: #ffffff → #f3f4f3 → #e5e7eb → #ffdfcd → #202120. Each step should feel like a deliberate lift, not a tint shift.
- Keep body copy in PublicaSans 16px weight 400 at line-height 1.5 with -0.01em tracking; reserve weight 500 for buttons, step titles, and short labels.
- Use the 2-3px #ff6105 accent rule beneath editorial headlines at roughly one-third of the heading width — it is the visual punctuation mark of the brand.

### Don't

- Don't introduce a second accent color or a secondary brand hue — the system is monochrome + one orange, and any chromatic addition breaks the rationing.
- Don't use weight 600 or 700 in PublicaSans; the system tops out at 500. Heavier weights are not part of the type scale.
- Don't apply shadows to cards, images, or non-primary buttons. Flat-with-hairline-border is the default; elevation is a privilege, not a default.
- Don't use the 50px radius on anything except the primary CTA and inputs. 24px is the cap for secondary buttons, 5px for cards.
- Don't set display text in all-caps or with positive letter-spacing. Tracking only tightens as size grows; never loosens.
- Don't fill large areas with #ff6105. The orange is a punctuation mark — let it punctuate, not paint.
- Don't mix rounded and square corner systems on the same page. Pick from the 5 / 8 / 24 / 32 / 50 ladder and stay on it.

## Components

### Primary Pill Button

Fill #ff6105, white text, 50px border-radius, 16px vertical / 32px horizontal padding, PublicaSans weight 500 at 16px. Carries the only shadow in the system: rgba(255,97,5,0.6) 1px 6px 14px 0 layered with rgba(0,0,0,0.06) 0 1px 4px 0 — the orange glow is the brand signature. Trailing chevron icon optional.

### Secondary Pill Button

Fill #ffffff or #f3f4f3, 1px border #e5e5e5, #292b2a text, 24px border-radius, 14px / 24px padding, weight 400. The tighter radius (not 50px) signals it is the secondary action.

### Nav Buy Now Button

Fill #ff6105, white text, 40px border-radius, smaller scale than the hero CTA. Mirrors the Primary Pill Button at nav density.

### Step Indicator Row

Active step: small orange pill badge reading 'Step 1' in white on #ff6105, weight 500 at 12px, 8px radius. Step title in Ink 18px weight 500 with a 2px #e5e5e5 underline. Inactive steps: 'Step 2' / 'Step 3' in Ash 12px, title in #292b2a 18px weight 400, underline 1px #e5e5e5.

### Press Logo Strip

Single row, 80-100px height, logos desaturated to Ink (#0a0a0a) or Carbon. Spacing 40-60px between logos. The eyebrow label 'FEATURED ON' in 12px tracked uppercase Ash.

### Editorial Section Heading

PublicaSans weight 300 at 48-72px, tracking -0.030em to -0.036em, color Ink. A 2-3px #ff6105 accent rule sits below the heading at roughly 1/3 of the heading width — the only chrome on the page.

### Dark Feature Band

Background #202120 with a 60-70% dark overlay over a full-bleed product photograph. Headline in white at 48px weight 300, accent rule in #ff6105. Padding 120px vertical.

### Featured Card (Peach)

Fill #ffdfcd (Peach Wash), 5px radius, 16-20px padding, with a phone/product mockup on the right. The peach fill is reserved for a single card per section to maintain scarcity.

### Ghost Card

Fill #ffffff, 1px border #e5e5e5, 5px radius, 16-24px padding. No shadow. Image radius 8px. Heading 24px weight 500 Ink, body 16px weight 400 Carbon.

### Announcement Bar

Background Linen (#f3f4f3), 40-48px height, centered text 14px weight 400 Carbon with a right-side text-link 'Let's Go →' in Ink weight 500.

### Top Navigation

Background #ffffff, 64-72px height, logo left, 5 center links in 14px weight 400 Carbon with 30-40px horizontal gaps, nav Buy Now button right. Optional thin 1px #e5e5e5 bottom border.

### Input Field (Pill)

50px border-radius, 1px border #e5e5e5, 16px horizontal padding, PublicaSans 16px weight 400. Placeholder text in Ash #a2a3a2. Focus ring 2px #ff6105 at 40% opacity.

## Similar Design Systems

- {'why': 'Same single-product hero photography on a near-white canvas, with a confident sans-serif headline and a single saturated accent for the buy CTA.', 'business': 'Tonal'}
- {'why': 'Editorial product spreads, large light-weight headlines, and a monochrome interface that lets one accent color carry the call-to-action.', 'business': 'Peloton (equipment pages)'}
- {'why': 'Generous whitespace, custom geometric sans, nearly colorless UI with a single warm accent and hairline 1px borders as the primary structural device.', 'business': 'Whoop'}
- {'why': 'Same restraint: one product, one typeface, one accent color, pill-shaped primary buttons, and flat cards with minimal border treatment.', 'business': 'Forme'}

## Agent Prompt Guide

**Quick Color Reference**
- text primary: #0a0a0a
- text secondary: #292b2a
- text muted: #7a7b7b
- background: #ffffff
- surface alt: #f3f4f3
- border hairline: #e5e5e5
- primary action: #ff6105 (filled action)

**Example Component Prompts**

1. *Primary CTA pill*: Fill #ff6105, white text, 50px border-radius, padding 16px vertical / 32px horizontal. PublicaSans weight 500, 16px, letter-spacing -0.01em. Box-shadow: rgba(255,97,5,0.6) 1px 6px 14px 0, rgba(0,0,0,0.06) 0 1px 4px 0. Optional trailing chevron in white.

2. *Editorial section heading*: PublicaSans weight 300, 48px, color #0a0a0a, letter-spacing -0.030em, line-height 1.2. Below the text, a 2px tall, 120px wide accent rule in #ff6105, aligned to the start of the heading. Section padding 80px top, 80px bottom.

3. *Featured onboarding card*: Fill #ffdfcd, 5px border-radius, padding 24px. Contains a phone mockup on the right (200px wide, 8px radius image frame). Step badge: orange pill #ff6105, white text 'Step 1', 8px radius, 12px / 12px padding. Step title in PublicaSans 18px weight 500 #0a0a0a with a 2px #e5e5e5 underline rule.

4. *Dark feature band*: Full-bleed background #202120 with a darkened product photo overlay at 65% opacity. White headline in PublicaSans weight 300, 48px, letter-spacing -0.030em, centered. A 60px wide, 2px tall #ff6105 accent rule centered below. Vertical padding 120px.

5. *Press logo strip*: Single horizontal row, logos rendered in #0a0a0a at 24-28px height, spaced 60px apart. Above the row, a 12px uppercase tracked label 'FEATURED ON' in #7a7b7b. Background #ffffff, padding 40px vertical.
