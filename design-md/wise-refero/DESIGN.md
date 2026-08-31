# Wise — Design System

> **North Star**: deep moss with lime voltage. Lime sparks on a near-black forest floor, with massive blocky display type announcing every move.
> **Theme**: light
> **Source**: https://wise.com
> **Refero Style**: https://styles.refero.design/style/367c0c6e-73a7-441c-a8ff-91d139ac60dc
> **Synced**: 2026-09-01

## Overview

Wise speaks in a confident, slightly loud voice: a deep forest green (#163300) carries most of the surface area — text, nav, dark sections, icons — while a single electric lime (#9fe870) acts as functional punctuation on CTAs, active tabs, and key highlights. The display type is almost aggressive: Wise Sans at weight 900, tightly tracked, shouted across the hero in 100px+ block letters. The rest of the system stays restrained on a near-white canvas with soft gray surfaces (#e8ebe6). Components are pill-shaped by default — buttons, nav segments, flag thumbnails, image masks — with gentle 10px radii reserved for cards and inputs. Color rarely gradients; instead, the lime–forest pairing inverts cleanly when sections go dark, creating rhythm without decoration.

## Color Palette

- **Forest Ink**: `#163300` — Dominant brand dark — nav text, dark section backgrounds, primary copy on light surfaces, icon strokes, filled navigation pills. This is the brand's gravity: wherever you need weight or authority, you reach for Forest Ink [brand]
- **Lime Voltage**: `#9fe870` — Green supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Spruce**: `#054d28` — Secondary dark green for card surfaces, supporting iconography, and tonal depth on dark sections where Forest Ink is too heavy [brand]
- **Linen Mist**: `#e2f6d5` — Pale green wash for soft highlight surfaces, tinted card backgrounds, nav hover states. A whisper of the brand green for low-emphasis containers [accent]
- **Signal Blue**: `#0b4c72` — Blue supporting accent for decorative details and low-frequency emphasis [accent]
- **Alarm Red**: `#cb272f` — Red supporting accent for decorative details and low-frequency emphasis. Use as a supporting accent, not as a status color [accent]
- **Charcoal**: `#454745` — Primary text, body copy, dense UI — slightly warm black that feels softer than pure #000 against white [neutral]
- **Obsidian**: `#0e0f0c` — Display headlines, high-contrast headings, pure-black moments in nav and hero. Slightly green-tinted black, not neutral gray [neutral]
- **Pebble**: `#868685` — Muted secondary text, placeholder copy, icon strokes, input borders. The mid-gray that recedes [neutral]
- **Slate**: `#6a6c6a` — Supporting body text, helper labels, subdued iconography. One step darker than Pebble for slightly more emphasis [neutral]
- **Fog**: `#e8ebe6` — Card surfaces, section dividers, subtle panel backgrounds on the white canvas. Green-tinted off-white, not pure neutral [neutral]
- **Paper**: `#ffffff` — Page canvas, inverted card surfaces, button text on lime fill [neutral]

## Typography

- **Inter**
- **Wise Sans**
- **monospace**
- **sans-serif**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| micro | 12 | — | 1.63 |
| caption | 14 | — | 1.55 |
| body-sm | 16 | — | 1.5 |
| body | 18 | — | 1.5 |
| body-lg | 25 | — | 1.3 |
| subheading | 36 | — | 1.25 |
| heading-sm | 45 | — | 1.1 |
| heading | 61 | — | 1.1 |
| heading-lg | 89 | — | 0.85 |
| display | 105 | — | 0.85 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8-12px
- **Section Gap**: 64-80px
- **Border Radius**: {'tags': '9999px', 'cards': '10px', 'inputs': '10px', 'buttons': '9999px', 'imageMasks': '1000px', 'largeCards': '28px', 'navSegments': '9999px'}

## Layout

Max-width 1200px centered container, with hero and dark sections going full-bleed. Hero pattern: centered massive display headline over white space, with a large illustration (globe) breaking the lower edge of the viewport. Section rhythm alternates white → light green band → dark Forest Ink section, creating a natural color cadence. Content arrangement is predominantly centered stacks in the hero, then 2-column text+visual or 3-column feature rows in supporting sections. A 5-column flag grid handles the country directory. Navigation is a single sticky top bar with a segmented pill switcher. The QR badge floats fixed in the bottom-right corner across all scroll positions.

## Surfaces / Elevation

- **Paper**
- **Fog**
- **Linen Mist**
- **Lime Voltage**
- **Forest Ink**

**Shadow tokens:**

## Imagery

Painted 3D-style illustrations of a globe with gold coins establish the brand's visual world — tactile, slightly surreal, rendered with soft gradients and warm light. Photography is minimal; when used, it's high-key and lifestyle-casual. Country flags appear as circular thumbnails in a 5-column grid — the only "icon" system is national identity. No abstract graphics, no stock patterns. The globe and coins are the recurring mascot motif, signaling global reach through a single warm, optimistic object rather than a montage.

## Design Principles

### Do

- Set display headlines in Wise Sans weight 900 with letter-spacing -3.15px at 105px; the extreme heaviness is the brand's signature — don't soften it to 700.
- Use Lime Voltage (#9fe870) exclusively for primary action fills and active states; one lime element per visible viewport section is usually enough.
- Default to 9999px radius for all buttons, tags, and nav segments — pill shapes are foundational, not decorative.
- Use Forest Ink (#163300) for text and dark surfaces, not pure black; the green-tinted near-black is warmer and more on-brand.
- Apply tight negative letter-spacing at large sizes (-0.030em at 100px+ down to -0.003em at 12px); headings should feel compact, not airy.
- Pair a filled primary CTA with an underlined text link as the secondary action — never two filled buttons side by side.
- Invert section backgrounds from white to Forest Ink to create rhythm; the lime text on dark green is the system's built-in emphasis.

### Don't

- Don't use Charcoal (#454745) for display headlines — reserve Obsidian (#0e0f0c) or Forest Ink for maximum contrast at large sizes.
- Don't introduce gradients, drop shadows beyond hairline borders, or decorative blurs — the system is flat by design.
- Don't use Lime Voltage as text color on light backgrounds; its contrast is too low. It only works as fill or on dark green.
- Don't use sharp corners (0–4px radius) on buttons, tags, or nav elements; pills are the default shape language.
- Don't set display headlines in Inter — Wise Sans 900 is the only acceptable voice for 60px+ type.
- Don't stack multiple lime elements close together; space them so the accent reads as a single punctuation mark.
- Don't use #000000 for body text; Charcoal (#454745) at 18px on white is the baseline that keeps the page from feeling harsh.

## Components

### Primary CTA Pill Button

Fully rounded (9999px radius) button with Lime Voltage (#9fe870) fill and Charcoal (#454745) or Forest Ink (#163300) text. Padding 11px vertical, 24px horizontal. Inter weight 500 at 16px. No border, no shadow — the fill does all the work.

### Outlined Pill Button

White fill, 1px Forest Ink border, 9999px radius. Same padding as primary. Used for "Sign up" in the header and non-primary calls to action where the lime would compete with a primary action nearby.

### Text Link Button

Underlined Forest Ink text at 16px Inter weight 500, no background, no border. Pairs with the primary CTA when two adjacent actions are needed (e.g. "Open an account" + "Send money now").

### Top Navigation Bar

White background, 64px height. Logo left, three-segment pill nav (Personal / Business / Platform) with 9999px radius and Forest Ink text, right cluster has language flag, Help, Log in, and outlined Sign up pill.

### Segmented Tab Control

Pill container (9999px radius) holding multiple text labels. Active tab: Lime Voltage fill with Charcoal text. Inactive tabs: transparent with Charcoal text. ~40px height, 12px horizontal padding per segment.

### Display Headline

Wise Sans weight 900 at 89–105px, line-height 0.85, letter-spacing -3.15px. Charcoal (#454745) or Obsidian (#0e0f0c) on light, Lime Voltage on dark sections. Set as block text, often in ALL CAPS for hero moments.

### Feature Row

Single-column-on-mobile, three-column-on-desktop. Icon (24px, Charcoal stroke) at top, heading in Inter 700 at 18px, body in Inter 400 at 16px Pebble. Generous 24px vertical gap between icon and heading.

### Country Grid Item

Circular flag thumbnail (1000px radius, ~56px diameter), 12px gap to country name in Inter 500 at 16px Forest Ink. Name is a text link with no underline at rest, underline on hover. Items sit in a generous grid with ~32px row gap.

### Dark Section Card

Forest Ink (#163300) background, 28px radius, 40px padding. Lime Voltage text for headline, Paper for body. Contains an inset white card (10px radius, 16px padding) for the currency selector.

### Currency Selector Pill

White pill inside a dark section card. Left: circular flag (24px) + country name in Charcoal Inter 500. Right: outlined "Change" button in Forest Ink. 9999px radius, 8px vertical padding.

### Input Field

10px radius, 1px Pebble (#868685) border, 12px vertical and 16px horizontal padding. Inter 400 at 16px. Focus state: Forest Ink border, no glow ring.

### Floating QR Badge

Forest Ink (#163300) rounded square (16px radius), fixed bottom-right, 120px wide. QR code in Paper at top, "Get the Wise app" label in Lime Voltage Inter 500 at 12px below.

### Badge / Tag

9999px radius, 8px vertical and 12px horizontal padding. Linen Mist (#e2f6d5) background with Forest Ink text, or Forest Ink background with Lime Voltage text. Inter 500 at 12px.

## Similar Design Systems

- {'why': 'Same dual-brand color strategy — deep brand color as dominant surface and text, one bright accent for CTAs and highlights, with pill-shaped buttons and large confident headlines.', 'business': 'Revolut'}
- {'why': 'Bright single-accent color system on a neutral canvas, pill-shaped interactive elements, friendly rounded geometry, and display type that speaks directly to the user.', 'business': 'Monzo'}
- {'why': 'High-contrast near-black text on white with a single vivid brand accent, oversized bold headlines as the primary brand expression, minimal decoration.', 'business': 'Cash App'}
- {'why': 'Flat surfaces, hairline borders instead of shadows, generous white space, and a single saturated accent color driving all interactive emphasis.', 'business': 'N26'}

## Agent Prompt Guide

Quick Color Reference
- text: #454745 (Charcoal) for body, #0e0f0c (Obsidian) for display
- background: #ffffff (Paper) canvas, #e8ebe6 (Fog) cards
- border: #868685 (Pebble) for hairlines, #163300 (Forest Ink) for emphasis
- accent: #9fe870 (Lime Voltage) for active states and highlights
- primary action: no distinct CTA color
- dark surface: #163300 (Forest Ink) for inverted sections

Example Component Prompts

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. Feature row (3-column): icon at 24px stroke #454745, 24px gap to heading at 18px Inter 700 in #0e0f0c, 8px gap to body at 16px Inter 400 in #868685. Column gap 32px, centered max-width 1200px.

3. Country grid item: circular flag thumbnail at 56px diameter (1000px radius), 12px vertical gap to country name in Inter 500 at 16px #163300. Arranged in a 5-column grid with 32px row gap and 24px column gap. Hover state: underline appears on the country name.

4. Dark section card: Forest Ink (#163300) background, 28px radius, 40px padding. Headline in Lime Voltage (#9fe870) at 36px Inter 700. Body text in #ffffff at 16px Inter 400. Contains an inset white card (10px radius) for a currency selector: circular flag + country name in Charcoal + outlined "Change" button.

5. Outlined nav button: white fill, 1px solid #163300 border, 9999px radius, 8px 16px padding, Inter 500 at 16px in #163300. Used in the top-right nav cluster for secondary account actions.
