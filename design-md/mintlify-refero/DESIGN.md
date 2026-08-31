# Mintlify — Design System

> **North Star**: Cloud garden over a glass desk. A hand-illustrated sky and a documentation product share the same frame — the only place color and concept collide before the page settles into monastic white.
> **Theme**: light
> **Source**: https://mintlify.com
> **Refero Style**: https://styles.refero.design/style/80d7ef36-ed7e-48bb-b558-f772eb40106f
> **Synced**: 2026-09-01

## Overview

Mintlify operates on a near-total monochrome discipline: white canvas, near-black text, and a single vivid green as the only chromatic spark across the entire interface. The hero is the deliberate exception — a hand-illustrated cloud landscape on a dark teal gradient, with the documentation product floating in the foreground as living proof. Everything downstream reverts to austere white surfaces, tight Inter typography, and component geometry that stays square (4px button radii, 16–24px card radii) rather than pill-shaped or overly rounded. Color appears as functional punctuation: green for active states, brand links, and decorative icons; black for the sole filled button variant. Elevation is whispered, never declared — shadows sit at 0.03–0.05 opacity and are felt more than seen.

## Color Palette

- **Mint Green**: `#0c8c5e` — Brand links, active nav state, feature icons, decorative dots in eyebrow labels, the thin underline on inline code references — the only chromatic accent in a monochrome system, applied sparingly to make functional moments feel switched on [brand]
- **Ink Black**: `#08090a` — Dark supporting neutral for text, icons, and strong contrast. Do not promote it to the primary CTA color [neutral]
- **True Black**: `#000000` — Body text, link defaults before hover, icon strokes, and footer rules — the workhorse neutral that carries most of the typography load [neutral]
- **Paper White**: `#ffffff` — Page canvas, card surfaces, button text on dark fills, input fields — the base layer everything else sits on [neutral]
- **Mist Gray**: `#f2f2f2` — Subtle dividers, hairline strokes on cards, low-emphasis backgrounds, and the faintest hover wash [neutral]
- **Cloud Gray**: `#dddddd` — Input borders, card outlines on hover states, secondary divider lines that need a step more visibility than Mist [neutral]

## Typography

- **Inter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.3 |
| heading-sm | 24 | — | 1.33 |
| heading | 40 | — | 1.15 |
| display | 57 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 12px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '4px', 'cards': '16px', 'inputs': '4px', 'buttons': '4px', 'largeContainers': '24px'}

## Layout

The page opens with a full-viewport dark hero (teal gradient + cloud illustration) containing a centered headline stack, email input, and a large floating documentation product mockup that overlaps the bottom edge of the hero into the white section below. The product mockup acts as a visual bridge between the expressive hero and the austere content sections. Below the hero, the layout shifts to a 1200px max-width centered container with 80px section gaps. Sections alternate between centered headline + paragraph + card grids (3-column for customer stories, 2-column for feature cards) and logo wall bands. Navigation is a single horizontal top bar, sticky on scroll, transparent on the hero and white on content sections. The page is spacious — comfortable density, generous breathing room, no dense information blocks or multi-column body content.

## Surfaces / Elevation

- **Paper White**
- **Mist Gray**
- **Hero Teal**
- **Ink Black**

**Shadow tokens:**

## Imagery

The visual language splits into two registers. The hero carries a hand-illustrated cloud landscape — soft volumetric cumulus clouds in warm yellow and cream tones, set against a deep teal-to-mint gradient sky, painted in a style closer to children's book illustration than tech marketing. This is the only expressive visual on the entire site. Below the fold, imagery shifts to product screenshots and customer photography: customer story cards use 16:9 photographic stills with subtle gradient overlays that fade the bottom edge for text legibility. Partner logos are rendered in grayscale. There are no abstract 3D renders, no geometric patterns, no decorative gradients. The product UI itself (the documentation mockup in the hero) is treated as the primary visual asset on the page.

## Design Principles

### Do

- Use Inter for everything — there is no display face or mono override in the system.
- Apply Mint Green (#0c8c5e) only for active states, brand links, decorative icons, and eyebrow labels — never as a large surface fill or button background.
- Set button radius to 4px and card radius to 16px — the system is square, not pill-shaped.
- Tighten letter-spacing to -0.02em at 57px and -0.01em at 40–16px; loosen to +0.05em only on uppercase 13px eyebrow labels.
- Use Ink Black (#08090a) for the filled button background and true black (#000000) for body text — keep these two neutrals in their separate roles.
- Let the hero be the only colorful moment on the page — revert to white surfaces and black text for everything below the fold.
- Limit shadows to 2px offset at 3–5% opacity; if a component needs more separation, use a 1px #dddddd border instead.

### Don't

- Do not introduce pill buttons, 9999px radii, or rounded avatars — the system commits to 4px / 16px / 24px.
- Do not place Mint Green on button fills, large backgrounds, or hero text — it loses identity when used at scale.
- Do not use a second accent color — the monochrome-plus-one-green rule is the brand's anchor.
- Do not set body text below 14px or use a line-height looser than 1.5 — readability is non-negotiable.
- Do not add gradients, glassmorphism, or colored shadows — the elevation language is flat and forensic.
- Do not use illustration style outside the hero cloud landscape — the rest of the site is pure UI.
- Do not set page background to anything other than white — no off-white canvas, no dark mode surfaces in the content sections.

## Components

### Primary Filled Button

4px radius, Ink Black (#08090a) background, Paper White (#ffffff) text, Inter at 14–15px weight 500, padding 8px 16px. Carries the 0.03-opacity lab shadow. Used for 'Start for free' and the email submit arrow.

### Ghost Navigation Button

Transparent background, True Black text, no border, 14px Inter weight 500, hover adds a subtle Mist Gray background wash. Used for 'Contact sales' in the nav.

### Hero Email Input

White background, Cloud Gray border, 4px radius on the outer pill, inner text field sits flush with a circular dark submit button on the right containing a right-arrow icon. Placeholder 'Email address' in muted gray, 14–15px Inter.

### Documentation Product Card

16px radius, white surface, the 0.05-opacity lab shadow, padded internally with ~24px. Contains a left sidebar (Mint Green active state, icon + label rows), a main content area with tab navigation, and a right-side 'On this page' TOC. This is the only place Mint Green is used as a sidebar active indicator.

### Customer Story Card

16px radius, white surface, 1px #f2f2f2 border, 24px internal padding. Top half is a full-bleed image with a subtle gradient overlay; bottom half holds a description paragraph (16px, weight 400) and a 'Read story →' text link in Inter weight 500.

### Feature Capability Card

16px radius, light Mint-tinted background wash, 24px padding, eyebrow label in small caps Mint Green at 13px letter-spacing +0.05em, body copy in Ink Black at 16px.

### Partner Logo Tile

No background, no border, rendered at grayscale on the white page. Logos sit on a uniform baseline grid, 4 per row with 24px column gap. No hover state — these are static trust markers.

### Top Navigation Bar

White background, sits on top of both the dark hero and white content sections. Logo on far left (Mint Green mark + black wordmark), nav links center-left in Inter 14px weight 500 True Black, 'Contact sales' ghost button and 'Start for free' filled button right-aligned. No bottom border — the nav reads as floating on the page.

### Sidebar Navigation Item

16px Inter weight 400, True Black text, 6px vertical padding, 8px left indent. Active state fills the row with a faint Mint-tinted background and switches text to Mint Green. Icons are 16px stroke 1.5, Mint Green on active, True Black on inactive.

### Eyebrow Label

13px Inter weight 500, Mint Green, letter-spacing +0.05em, uppercase. Reads as a category tag, not a heading — always paired with a larger heading below.

## Similar Design Systems

- {'why': 'Same single-accent discipline — monochrome interface with one vivid color doing all the brand work, Inter typography, square-cornered buttons, forensic shadows', 'business': 'Linear'}
- {'why': 'Same near-black ink on pure white canvas, single chromatic moment per page, tight Inter tracking, 4px button radii', 'business': 'Vercel'}
- {'why': 'Same monochrome-plus-one-accent pattern with Inter, product-as-hero composition, and the same commitment to whitespace between sections', 'business': 'Resend'}
- {'why': 'Same documentation-product-as-marketing approach, clean white sections, and restrained use of color for functional states only', 'business': 'Notion'}

## Agent Prompt Guide

Quick Color Reference:
- primary action: no distinct CTA color
- accent / brand: #0c8c5e (Mint Green)
- text: #000000 (body) / #08090a (headings, button surface)
- background: #ffffff (Paper White)
- border / divider: #f2f2f2 (Mist Gray) / #dddddd (Cloud Gray)

Example Component Prompts:
1. Create a top navigation bar: white background, no bottom border, 1200px max-width centered. Logo on left (Mint Green #0c8c5e mark + black wordmark). Nav links center-left in Inter 14px weight 500, #000000. Right side: 'Contact sales' ghost text link and a filled button — Ink Black #08090a background, white text, 4px radius, 8px 16px padding, Inter 14px weight 500.
2. Create a hero section: full-bleed dark teal background (#0c8c5e) with an illustrated cloud landscape. Centered headline in Inter 57px weight 600, #ffffff, letter-spacing -1.14px. Subtext in Inter 18px weight 400, #ffffff at 80% opacity. Email input: white background, 4px radius, 1px #dddddd border, placeholder 'Email address' in muted gray, with a circular dark submit button on the right containing a white right-arrow icon.
3. Create a customer story card: white surface, 16px radius, 1px #f2f2f2 border, 24px padding. Top half is a 16:9 photographic image filling the card edge-to-edge with a bottom gradient fade. Below: description in Inter 16px weight 400, #000000, two lines max. Bottom: 'Read story →' text link in Inter 14px weight 500, #000000.
4. Create a feature capability card: light Mint-tinted background (rgba of #0c8c5e at ~6% opacity), 16px radius, 24px padding. Eyebrow label in Inter 13px weight 500, #0c8c5e, letter-spacing 0.65px, uppercase. Body heading in Inter 20px weight 600, #08090a. Description in Inter 16px weight 400, #000000.
5. Create a partner logo wall: white background, no container, 4 logos per row with 24px column gap, all logos rendered in grayscale, vertically centered on a uniform baseline. No hover state, no borders.
