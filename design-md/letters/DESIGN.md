# Letters — Design System

> **North Star**: morning clinic under open sky — a sterile white desk beneath a wash of soft blue, dotted with surgical-blue instruments.
> **Theme**: light
> **Source**: https://letters.app
> **Refero Style**: https://styles.refero.design/style/04109c48-f591-4110-9739-622243d4ecc2
> **Synced**: 2026-09-01

## Overview

Letters is a medical letterwriting tool that opens with an open-sky gradient hero — a soft blue atmospheric band that sets a calm, clinical tone before dropping into a clean white workspace. The system is 99% monochrome: pure white canvas, near-black text (#070709), pill-shaped dark CTAs, and 18px rounded cards floating on hairline shadows. One vivid blue (#2597d0) is reserved for functional punctuation — icons, micro-graphics, waveform players — never for buttons or large fills. Typography leans on Open Runde, a geometric humanist sans with aggressive negative tracking at display sizes (-0.04em at 80px) that tightens headlines into confident blocks. Components feel medical-instrument light: thin borders, generous card padding, pill buttons, and a reserved use of elevation that lets the sky hero do the emotional work.

## Color Palette

- **Obsidian**: `#070709` — Primary text, filled CTA buttons, and dark UI surfaces — near-black chosen over pure #000 to soften contrast against white canvas [neutral]
- **Paper White**: `#ffffff` — Page background, card surfaces, and button text — the primary canvas across all sections below the hero [neutral]
- **Cloud Gray**: `#f5f5f5` — Secondary card surfaces and section backgrounds — separates feature blocks from main canvas [neutral]
- **Sky Tint**: `#d7e6f5` — Card box-shadow tint and subtle blue-toned surface — keeps elevation feeling atmospheric rather than gray [neutral]
- **Charcoal**: `#60606c` — Body text, secondary copy, and muted borders — the dominant neutral for non-heading content [neutral]
- **Slate**: `#8b8b8b` — Tertiary text and inactive border states — used for placeholder labels and disabled affordances [neutral]
- **Ink**: `#151515` — Heading color and strong dividers — slightly lighter than Obsidian for less severe emphasis [neutral]
- **Surgical Blue**: `#2597d0` — Icon strokes, mic glyph, waveform player, and small functional accents — the single chromatic note across the interface [brand]
- **Sky Gradient**: `#779bc1` — Hero background — vertical wash from medium blue to near-white that establishes the medical-aspirational mood [accent]

## Typography

- **sans-serif**
- **Open Runde**
- **Inter**
- **The Doctor FreeVersion**
- **Open Runde Semibold**
- **Open Runde Medium**
- **Open Runde Regular**
- **Open Runde Bold**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.2 |
| body-sm | 14 | — | 1.4 |
| body | 16 | — | 1.49 |
| body-lg | 18 | — | 1.4 |
| subheading | 20 | — | 1.4 |
| heading-sm | 28 | — | 1.2 |
| heading | 44 | — | 1.1 |
| display | 80 | — | 0.9 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 40-48px
- **Element Gap**: 12-16px
- **Section Gap**: 80-120px
- **Border Radius**: {'tags': '100px', 'cards': '18px', 'icons': '8px', 'inputs': '12px', 'buttons': '100px', 'nav-pills': '100px', 'large-cards': '32-48px'}

## Layout

Full-bleed sky gradient hero with centered headline and subtext, CTA pill below. Transitions seamlessly to a white content area with generous section padding (80-120px). Feature sections use a 2-column grid of large rounded cards (18-32px radius) with equal proportions. Section headings are always centered, single-column, above the card grid. Navigation is a sticky white top bar with center-aligned link cluster and right-aligned auth actions. Overall rhythm: one atmospheric hero band, then alternating white and #f5f5f5 sections with consistent vertical breathing room. No sidebar, no mega-menu, no asymmetric layouts — the page reads as a calm, symmetrical column.

## Surfaces / Elevation

- **Sky Canvas**
- **Paper Canvas**
- **Cloud Surface**
- **Sky Tint Surface**
- **Obsidian Surface**

**Shadow tokens:**

## Imagery

Imagery is almost entirely UI-product — no lifestyle photography, no abstract 3D renders. The visual language is built from product cards showing the app's own interface: a Before/After document comparison, an upload zone with dashed border, and a waveform audio player. The only atmospheric visual is the sky gradient hero. Icons are flat, single-color line icons in #2597d0 (envelope, microphone, checkmark) — consistent stroke weight, no filled variants. Illustration style is restrained: product mockups on white with subtle rotation for depth, never tilted dramatically. The handwritten font (The Doctor) provides the only organic/handmade element, used exclusively to evoke clinical penmanship in the Before card.

## Design Principles

### Do

- Use 100px border-radius for all buttons, tags, and pill-shaped elements — full rounding is the signature shape language
- Set display headings at 80px Open Runde weight 600 with letter-spacing -0.04em and line-height 0.90 — the tight stack is a defining rhythm
- Use #070709 (Obsidian) for all filled CTAs — never a chromatic button background, the near-black is the action color
- Apply the sky gradient only to the hero band; keep all other sections on pure white or #f5f5f5
- Reserve #2597d0 (Surgical Blue) for icons, waveform players, and small functional accents under 24px — never as a button fill or large surface
- Use the blue-tinted shadow stack (rgba(16,55,132,0.03) at large blur radii) for feature cards to keep elevation feeling atmospheric rather than corporate
- Center-align section headings and hero text — the layout rhythm is symmetrical, not asymmetric
- Use 40-48px internal padding on feature cards to maintain the spacious, clinical density

### Don't

- Never use a chromatic color as a CTA button background — the system is intentionally monochrome for action
- Never flatten the letter-spacing on large headings — the -0.04em at 44px+ is what makes Open Runde feel confident rather than generic
- Never apply the sky gradient below the hero — it loses meaning if repeated across sections
- Never use shadows with high opacity (>0.1) on cards — the system relies on barely-visible, large-radius shadows
- Don't pair Open Runde with other geometric sans-serifs like Helvetica or Roboto — the specific humanist geometry is part of the brand
- Never use The Doctor font for functional UI text — it is decorative only, for the handwritten note illustrations
- Don't place white cards directly on the sky gradient without internal padding — the cards need breathing room from the atmospheric background
- Avoid using #2597d0 for text longer than 2 words — it is for icons and micro-graphics, not body copy

## Components

### Pill Primary Button

Filled pill button, 100px border-radius, 12-16px vertical padding, 24px horizontal padding. Background: #070709 (Obsidian). Text: white, Open Runde 14-16px weight 500, letter-spacing -0.01em. Carries a four-layer soft drop shadow: rgba(36,36,40,0.1) 0 1px 2px, rgba(36,36,40,0.09) 0 3px 3px, rgba(36,36,40,0.05) 0 6px 4px, rgba(36,36,40,0.01) 0 11px 4px — a barely-perceptible lift.

### Outlined Ghost Button

Pill-shaped (100px radius) with transparent fill, 1px border in #000 or #bebecc, Open Runde 14px weight 500 in #070709. Used in the nav bar for 'Login' — sits beside the filled Sign up button for visual contrast without competing for weight.

### Feature Card

White surface, 18-32px border-radius, generous 40-48px internal padding. Carries the signature blue-tinted shadow: rgba(16,55,132,0.03) 0 17px 37px, 0 67px 67px, 0 150px 90px — large, very low-opacity, atmospheric. Inside: pill tag at top with icon (envelope/mic in #2597d0), 28-44px heading in Open Runde weight 600, supporting copy in #60606c.

### Upload Drop Zone

Dashed 1px border in #bebecc, 12px radius, 16px padding. Centered icon (envelope in #2597d0) above 12px Open Runde label. On hover: border darkens to #8b8b8b, no fill change.

### Waveform Audio Player

White card with 12px radius, 16px padding. Horizontal waveform rendered in #2597d0 (surgical blue) against white — the single most expressive use of chromatic color in the product UI. Play/pause dot in matching blue.

### Before/After Document Card

Two overlapping white cards, 12-18px radius, slight rotation for stacked effect. 'Before' card uses The Doctor FreeVersion font with cursive text; 'After' card uses Open Runde body text. Each card has a small pill tag with checkmark/icon in #2597d0 at the top.

### Top Navigation Bar

Sticky top bar, white background, 1px bottom border in #000 or transparent. Left: logo (Letters wordmark + icon). Center: horizontal nav links — 'Use cases', 'Features', 'Pricing', 'Our doctors' in Inter 14px weight 500, #070709. Right: 'Login' ghost button + 'Sign up' filled pill button (same as hero CTA).

### Pill Tag / Chip

100px radius, 4-6px vertical padding, 10-14px horizontal padding. White background with 1px border in #000. Icon (envelope/mic in #2597d0) + label in Open Runde 12-14px weight 500, #070709.

### Section Heading Block

Centered stack: 28-44px Open Runde heading, weight 600, letter-spacing -0.04em, #070709. Optional inline number/emoji in #2597d0 for emphasis. No subtitle — heading stands alone on white.

### Hero Headline

80px Open Runde weight 600, line-height 0.90, letter-spacing -0.04em, white text. Two lines, tight stacked rhythm. Sits centered on the sky gradient with 20-28px between lines.

### Hero Subtext

16-18px Open Runde weight 400, line-height 1.49, letter-spacing -0.01em, white. Two short lines, centered, max-width ~480px. Color is white at 90% opacity over the sky gradient for softness.

## Similar Design Systems

- {'why': 'Same monochrome discipline with one restrained accent color, pill-shaped CTAs, and tight geometric sans-serif headings with negative tracking', 'business': 'Linear'}
- {'why': 'Comfortable density with rounded cards floating on near-white surfaces and a minimal icon-driven visual language', 'business': 'Notion'}
- {'why': 'Light theme with generous card padding, 18-32px rounded corners, and a single brand color used sparingly for icons and micro-interactions', 'business': 'Cal.com'}
- {'why': 'Near-black filled pill CTAs against white surfaces, clinical spaciousness, and the use of gradient hero bands as the only atmospheric color moment', 'business': 'Mercury'}
- {'why': 'Minimal monochrome palette with sharp typographic hierarchy and pill-shaped interactive elements throughout', 'business': 'Vercel'}

## Agent Prompt Guide

## Quick Color Reference
- text (primary): #070709 Obsidian
- text (secondary): #60606c Charcoal
- background: #ffffff Paper White
- surface (alt): #f5f5f5 Cloud Gray
- border: #000000 / #bebecc (use #bebecc for hairlines)
- accent: #2597d0 Surgical Blue (icons/waveforms only)
- primary action: #070709 (filled action)

## 3-5 Example Component Prompts
1. **Hero section**: Full-bleed sky gradient background (linear-gradient 180deg, #779bc1 → #cbdcec). Centered 80px Open Runde weight 600 headline in white, letter-spacing -0.04em, line-height 0.90. Subtext: 18px Open Runde weight 400, white at 90% opacity, max-width 480px. Below: filled pill button — #070709 background, 100px radius, white text 'Sign up for free', 12px 24px padding, with the four-layer soft shadow stack.

2. **Feature card**: White surface, 18px border-radius, 48px padding. Pill tag at top (100px radius, 1px black border, 4px 12px padding) with envelope icon in #2597d0 + label 'Letters' in Open Runde 12px weight 500. Below: 28px Open Runde weight 600 heading, then 16px weight 400 body in #60606c. Drop shadow: rgba(16,55,132,0.03) at 17px/67px/150px blur radii.

3. **Upload drop zone**: 12px border-radius, 1px dashed border in #bebecc, 16px padding. Centered envelope icon in #2597d0, 12px label below in Open Runde weight 500. On hover: border darkens to #8b8b8b.

4. **Waveform audio player**: White card, 12px radius, 16px padding. Horizontal audio waveform rendered in #2597d0 Surgical Blue across full width. Play/pause dot in matching blue at left.

5. **Before/After document pair**: Two overlapping white cards (18px radius) with 8px rotation difference for stacked effect. Before card: The Doctor font cursive handwriting. After card: Open Runde 14px weight 400 body text. Each has a small pill tag with checkmark icon in #2597d0 at the top center.

6. **Top navigation**: Sticky white bar, 1px bottom border. Left: 'Letters' wordmark + icon. Center: 4 nav links in Inter 14px weight 500, #070709. Right: outlined ghost 'Login' button (1px black border, 100px radius) + filled pill 'Sign up' button (#070709, 100px radius, white text).

## Typography Quick Reference
- Display: 80px / 0.90 / -0.04em / weight 600
- Heading: 44px / 1.10 / -0.04em / weight 600
- Subheading: 28px / 1.20 / -0.04em / weight 600
- Body: 16-18px / 1.40-1.49 / -0.01em / weight 400
- Caption: 12px / 1.20 / -0.01em / weight 500
