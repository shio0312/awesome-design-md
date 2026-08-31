# Brex — Design System

> **North Star**: White concrete, single ember — a clinical financial instrument where one orange spark does all the talking.
> **Theme**: light
> **Source**: https://brex.com
> **Refero Style**: https://styles.refero.design/style/b58d92f6-68a8-4358-8fc9-6ea58e6d483b
> **Synced**: 2026-09-01

## Overview

Brex is a white concrete financial workbench lit by a single orange ember. The interface lives on a near-pure white canvas with tight, almost compressed Inter type and a custom Flecha display face, and the only chromatic voice in the system is #ff5900 — a vivid ember that marks every primary action, link, and tab indicator without ever becoming decorative. Dark surfaces (#000710 footer, #15191 announcement bar) frame the bright body, creating a hard light/dark bookend that makes the white sections feel taller. Components are flat with a 12px radius, minimal shadows, hairline borders, and generous 48px section gaps — the system is designed to feel like a precision instrument for finance teams, not a marketing site.

## Color Palette

- **Ember**: `#ff5900` — Orange supporting accent for decorative details and low-frequency emphasis; Orange supporting accent for decorative details and low-frequency emphasis. [brand]
- **Abyss**: `#000710` — Footer background, deepest dark surface — a near-black with a barely-perceptible blue cast that distinguishes it from pure black at section transitions [neutral]
- **Carbon**: `#15191e` — Announcement bar, dark mode headers, elevated dark surfaces — softer than Abyss, used where dark needs to feel like product chrome rather than footer [neutral]
- **Ink**: `#000000` — Primary headings, body text, heavy borders — the dominant text color across light surfaces [neutral]
- **Paper**: `#ffffff` — Page background, card surfaces, button text on dark fills — the primary canvas [neutral]
- **Fog**: `#f3f3f7` — Secondary surface, input field backgrounds, subtle section dividers — the only off-white that creates layered card stacks on the Paper canvas [neutral]
- **Mist**: `#b9bbc6` — Hairline borders, dividers, disabled states — the structural gray that keeps cards and inputs defined without visual weight [neutral]
- **Steel**: `#8b8d98` — Muted icon strokes, placeholder text, secondary nav text — the mid-gray for chrome that shouldn't compete with content [neutral]
- **Pewter**: `#6f737b` — Tertiary body text, caption-level labels, helper text — a step between Steel and Graphite for mid-importance copy [neutral]
- **Graphite**: `#60646c` — Secondary body text, subhead descriptions, muted link text — the workhorse gray for any paragraph that isn't a heading [neutral]

## Typography

- **Inter**
- **Flecha**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.33 |
| heading | 36 | — | 1.21 |
| heading-lg | 48 | — | 1.2 |
| display | 72 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24-32px
- **Element Gap**: 8-16px
- **Section Gap**: 48-80px
- **Border Radius**: {'tags': '6px', 'cards': '12px', 'inputs': '12px', 'buttons': '12px'}

## Layout

The page is a full-bleed vertical stack of max-width 1200px centered content bands. The hero uses an asymmetric split: left-aligned text block (headline + subtext + email capture + ghost link) occupies roughly 45% width, with a product visual (angled card stack on phone mockup) on the right. Below the hero, a Fog-banded logo grid provides social proof with generous vertical padding. Feature sections alternate between centered headlines over horizontal card strips and tabbed product category selectors. Article/resource sections use a 4-column card grid with carousel overflow. The footer is a full-bleed dark Abyss band with multi-column link groups. Vertical rhythm is consistent: 48–80px between major sections, 24–32px card padding, 8–16px element gaps.

## Surfaces / Elevation

- **Paper Canvas**
- **Fog Section**
- **Card Surface**
- **Dark Chrome**
- **Abyss Footer**

## Imagery

Product photography is the dominant visual: physical credit cards, iPhone screens showing the Brex app, and receipt/transaction interfaces, all shot on clean white or light surfaces. Photography is high-key and product-focused — no lifestyle context, no human subjects in marketing imagery. Customer logos in the trust band are rendered monochrome (Steel/Mist) to create visual uniformity regardless of original brand color. Article and blog cards use editorial photography with varied subjects (interior spaces, workspace shots, product mockups) treated as contained 16:9 crops within 12px-radius card frames. The app is icon-light in chrome areas, using simple line icons in Steel or Ember weight.

## Design Principles

### Do

- Use Ember (#ff5900) for exactly one purpose per region: the primary action. Never use it for decorative fills, backgrounds, or multiple competing elements on the same screen.
- Apply Inter's negative tracking to every size: -0.01em at 24px and below, -0.02em at 36px, -0.03em at 72px. The compression is the signature.
- Use 12px border-radius on all interactive surfaces (buttons, inputs, cards). Use 6px only for inline tags and small chips.
- Keep section gaps at 48–80px and card padding at 24–32px. The system breathes; do not pack content.
- Default to Paper (#ffffff) canvas with Fog (#f3f3f7) for section-level contrast. Reserve Abyss and Carbon for header/footer dark frames only.
- Use Graphite (#60646c) for body paragraphs and Pewter (#6f737b) for helper/caption text. Never use Steel for anything longer than a label.
- Set font-feature-settings to disable calt and liga on Inter — the system intentionally avoids contextual alternates and ligatures for a neutral engineered feel.

### Don't

- Don't introduce a second accent color. The single-ember system is the brand; adding blue, green, or purple breaks the visual contract.
- Don't use shadows for card elevation. The system relies on Paper/Fog contrast and 1px Mist borders — drop shadows are out of system.
- Don't use Flecha for body or sub-headings. It is a display face only; Inter handles everything below 48px.
- Don't center body text paragraphs. Headlines can be centered, but Inter body copy at 16px is left-aligned with max-width ~640px.
- Don't use Ember for text links inside paragraphs — reserve it for CTA buttons and standalone link phrases. Inline body links use Ink with an underline.
- Don't mix border-radius values within a component group. All buttons get 12px, all cards get 12px, all tags get 6px — never 8px or 10px as compromises.
- Don't use the announcement bar background (#15191e) as a generic dark surface inside the body. It belongs only at the very top of the page.

## Components

### Top Announcement Bar

Full-bleed Carbon (#15191e) background, 1px vertical padding, centered Inter 12px weight 500 white text with inline Ember-colored link. No close button visible in standard use.

### Primary Navigation Bar

White background, 12px radius on the right-side CTA only. Left: Brex wordmark in Ink (#000000). Center: Inter 14px weight 500 Ink nav items with caret indicators. Right: 'Sign in' and 'See a demo' as plain text links (Ink), followed by 'Get started' as a filled Ember button (12px radius, 8px 16px padding, Inter 14px weight 600, white text).

### Ember CTA Button (Filled)

Background Ember (#ff5900), white text, 12px border-radius, 8px vertical × 16px horizontal padding, Inter 14–16px weight 600, no border. On dark backgrounds the same fill applies with Paper text. The vivid orange against white creates immediate visual priority without needing size or weight escalation.

### Ghost Link Button

No background, no border, Ink (#000000) text at Inter 14px weight 500, often prefixed with a small Ember-colored icon (play circle, arrow). Sits beside or below filled CTAs as a lower-commitment alternative.

### Email Capture Input

White background, 1px Mist (#b9bbc6) border, 12px radius, 12–16px padding. Placeholder text in Steel (#8b8d98). The Ember 'Get started' button is attached or adjacent, creating a horizontal field+button pair with a 4–8px gap.

### Feature Category Card

White background, 12px radius, 24–32px padding, no visible border, subtle separation by spacing alone. Heading in Ink Inter 20–24px weight 600, body in Graphite 14–16px weight 400. Selected/active card shows Ember-colored text or underline. Product images (cards, phones, charts) anchor the bottom of the card.

### Customer Logo Grid

Fog (#f3f3f7) background section, heading in Ink Inter ~36px weight 600 centered. Logos arranged in a 6×2 grid (or 4–5 per row on narrower layouts), all rendered in Steel/Mist monochrome. No logo gets a colored treatment — the uniformity reinforces enterprise scale.

### Article / Resource Card

White background, 12px radius, no border. Top: full-bleed image (16:9 or 4:3) within the card radius. Below: Inter 20px weight 600 Ink headline, Graphite 14px weight 400 excerpt, 2–3 lines max. Carousel uses circular Paper buttons with Ink arrows at the section's left edge.

### Dark Footer

Abyss (#000710) background, full-bleed. Brex wordmark in Paper at top-left. Multi-column link groups in Inter 14px weight 400 with column headers in weight 600 Paper. Link text in a slightly lighter gray against Abyss for hierarchy. Generous 48–64px vertical padding.

### Cookie Consent Dialog

White background, 12px radius, subtle shadow, max-width ~480px. Title 'Cookie Consent' in Inter 16px weight 600 Ink. Body in Graphite 14px. Three buttons in a row: 'Accept all' (filled Ember), 'Reject all' (outlined with Mist border), 'More choices' (text link). Floats above content with a 24px bottom margin.

### Carousel Navigation Controls

Circular Paper buttons, 32–40px diameter, containing left/right Ink arrow icons. Positioned at the far left of the scroll strip with a faint horizontal line indicating scroll progress.

## Similar Design Systems

- {'why': 'Same monochrome-first fintech aesthetic with a single saturated accent for CTAs, Inter-based type, and 12px card radii', 'business': 'Stripe'}
- {'why': 'Same aggressive negative letter-spacing on Inter, near-pure white canvas, and minimal-shadow flat card system', 'business': 'Linear'}
- {'why': "Direct fintech competitor with the same 'finance product as precision instrument' visual language — white canvas, single accent, tight compressed type", 'business': 'Ramp'}
- {'why': 'Same hairline-border card system on near-white canvas with generous breathing room and no decorative shadows', 'business': 'Notion'}

## Agent Prompt Guide

**Quick Color Reference**
- background: #ffffff
- surface alternate: #f3f3f7
- text primary: #000000 (Ink)
- text secondary: #60646c (Graphite)
- border: #b9bbc6 (Mist)
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Create a hero section:* White (#ffffff) background, max-width 1200px centered. Headline at 72px Inter weight 600, #000000, letter-spacing -0.03em, line-height 1.0. Subtext at 20px Inter weight 400, #60646c. Email input (white, 1px #b9bbc6 border, 12px radius, Steel #8b8d98 placeholder) paired with an Ember (#ff5900) filled button (12px radius, 8px 16px padding, white Inter 16px weight 600 text).

2. *Create a feature category card:* White background, 12px radius, 32px padding, no border. Heading Inter 24px weight 600 #000000. Body Inter 16px weight 400 #60646c. Product image anchored at the bottom within the card's 12px radius.

3. *Create a customer logo band:* Fog (#f3f3f7) full-width section, 80px vertical padding. Centered heading Inter 36px weight 600 #000000. Logos in 6-column grid, all rendered in #8b8d98 monochrome at uniform 32px height.

4. *Create the footer:* Abyss (#000710) full-bleed background, 64px vertical padding, max-width 1200px content. Brex wordmark in #ffffff at top-left. Four columns of links: column headers in Inter 14px weight 600 #ffffff, links in Inter 14px weight 400 #b9bbc6.

5. *Create a dark announcement bar:* Carbon (#15191e) full-bleed, 1px vertical padding, centered Inter 12px weight 500 #ffffff text with an inline #ff5900 link.
