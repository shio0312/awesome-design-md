# monday.com — Design System

> **North Star**: white workshop with pastel sticky notes
> **Theme**: light
> **Source**: https://monday.com
> **Refero Style**: https://styles.refero.design/style/77ee57e9-9f8e-4ec1-93f7-cc1c4b84307a
> **Synced**: 2026-09-01

## Overview

monday.com runs a white-canvas productivity language with violet as its singular brand voice. The page breathes through generous whitespace, near-black typography, and pastel-colored card surfaces that borrow from a crayon-box palette — soft green, powder blue, peach, lavender, mint — creating a playful, human feeling that contrasts the serious SaaS market. Violet (#6161ff) owns the primary action and brand surfaces, while gradient text (pink→orange, cyan→violet) carries the hero's emotional charge. Components are pill-shaped and generously rounded: 160px buttons, 24px cards, 6px tags. The visual rhythm alternates between flat text-heavy sections and elevated product/board mockups that peek above the page edge, blurring the boundary between marketing and product.

## Color Palette

- **Monday Violet**: `#6161ff` — Primary CTA buttons, brand backgrounds, active states, gradient stops — saturated indigo reads as confident but approachable, not corporate [brand]
- **Ink**: `#333333` — Primary body text, headings, button labels — near-black with a hint of warmth avoids the harshness of pure #000 [neutral]
- **Slate**: `#535768` — Secondary text, nav links, icon fills, footer copy — cool gray supports hierarchy without competing with headings [neutral]
- **Iron**: `#808080` — Muted helper text, disabled icon strokes, tertiary borders [neutral]
- **Fog**: `#cacbcd` — Card and container borders, subtle dividers between content blocks [neutral]
- **Mist**: `#d0d4e4` — Light card borders, the standard outline color for elevated card surfaces [neutral]
- **Pebble**: `#dddfeb` — Badge borders, pill-button outlines, input borders [neutral]
- **Cloud**: `#f5f6f8` — Page canvas, section backgrounds, neutral button fills — the floor color everything floats on [neutral]
- **Snow**: `#ffffff` — Card surfaces, button text, nav background, input fields [neutral]
- **Shadow Dust**: `#e6e7ea` — Box-shadow tint, barely-there surface lifts [neutral]
- **Mint**: `#bcfe90` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content [accent]
- **Sky**: `#abf0ff` — Blue wash for highlight backgrounds, decorative bands, and soft emphasis behind content [accent]
- **Apricot**: `#ff8940` — Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content; Hero headline gradient stop, warm accent in pink-to-orange text [accent]
- **Lavender**: `#eddff7` — Decorative card background, soft category surface [accent]
- **Periwinkle**: `#e7ecff` — Decorative card background, light brand-tinted surface [accent]
- **Cornflower**: `#93beff` — Decorative card background, secondary brand surface [accent]
- **Aqua**: `#d1faff` — Decorative card background, cyan accent surface [accent]
- **Cotton Candy**: `#e98dfe` — Card border accent, playful highlight stroke [accent]
- **Ultra Violet**: `#9450fd` — Saturated button alternative, deep brand accent [accent]
- **Electric Cyan**: `#3ac9ff` — Saturated button alternative, AI/feature highlight [accent]
- **Forest**: `#2a5c4e` — Teal action color for filled buttons, selected navigation states, and focused conversion moments [accent]
- **Peony**: `#fcd0f8` — Saturated button alternative, soft pink fill [accent]
- **Periwinkle Wash**: `#dbdbff` — Badge and tag background — tints pill elements with brand warmth [accent]
- **Prism**: `#8181ff` — Supporting palette color for small decorative accents when the core palette needs contrast. [brand]

## Typography

- **Poppins**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.45 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.4 |
| heading-sm | 24 | — | 1.3 |
| heading | 36 | — | 1.2 |
| heading-lg | 48 | — | 1.15 |
| display | 64 | — | 1.15 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'nav': '6px', 'cards': '24px', 'badges': '6px', 'images': '12px', 'inputs': '6px', 'buttons': '160px'}

## Layout

Max-width ~1200px centered content with full-bleed product mockups that break the container. Hero is a centered single-column headline with gradient text and one CTA. Below: social-proof logo strip, then alternating 2-column text+product sections. The AI feature uses a 50/50 split with a violet brand panel on the right housing a product mockup. Vertical rhythm is generous (64px section gaps) with soft gray bands (#f5f6f8) breaking up white sections. Navigation is a single sticky white top bar with logo left, links center, dual CTAs right. No sidebar, no mega-menu visible on this page.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Brand Panel**
- **Tinted Accent**

**Shadow tokens:**

## Imagery

Visuals are dominated by product UI mockups — actual monday.com board screens with colored status pills, avatar stacks, and AI sidebar panels — rather than photography or illustration. The product IS the hero: boards peek above section edges at skewed angles, creating a 'leaking into the marketing page' effect. Logo strip uses monochrome black wordmarks. No lifestyle photography, no human portraits, no stock imagery. The only decorative visual is the conic-gradient prism mark in the logo.

## Design Principles

### Do

- Use 160px border-radius for all buttons and CTAs — the pill shape is non-negotiable and defines the brand's friendly tone
- Reserve #6161ff for primary actions and brand panels; let it carry the most important decision on every screen
- Apply pastel accent backgrounds (Mint, Sky, Apricot, Lavender) to feature cards, not to buttons or text
- Set display headlines at 48–64px Poppins weight 300 with negative letter-spacing (-0.04em to -0.02em) — thin geometric headlines distinguish this from typical 700-weight SaaS heroes
- Use 24px radius for cards and 6px for badges/inputs — keep these two tiers consistent
- Apply the conic-gradient prism (#8181ff → teal → green → yellow → pink → back to violet) to brand dividers, the logo mark, and loading states only
- Use gradient text (pink→orange or cyan→violet) exclusively on hero headlines to inject warmth into the white canvas

### Don't

- Don't use square or 4px-radius buttons — the pill shape is the signature
- Don't apply pastel accent colors to body text, borders, or icons — they are surface treatments only
- Don't set type below weight 400 for body or below 500 for UI labels — weight 300 is reserved for display headlines
- Don't use pure #000000 for large text blocks — #333333 is warmer and reads as the system's true black
- Don't stack more than 3-4 pastel colors in adjacent cards — pick a 2-3 color accent set per section
- Don't use heavy drop shadows on cards — the system uses a single soft 48px-blur lavender-tinted shadow at 40% opacity
- Don't introduce new chromatic CTA colors — #6161ff is the single action color; saturated button alternatives exist for product UI, not marketing

## Components

### Primary Pill Button

Filled violet #6161ff background, white text in Poppins 16px weight 500, 160px border-radius (full pill), 13px vertical / 24px horizontal padding, inline arrow icon. Drives the hero 'Get Started' and any conversion moment.

### Outlined Pill Button

Transparent background, 1px #535768 border, 160px border-radius, 13px vertical / 20px horizontal padding, Ink text. Used for 'Contact sales' next to the primary CTA.

### Text Link Button

No background or border, Slate (#535768) text weight 500, often paired with a dropdown chevron. 8–10px horizontal padding for nav items.

### Pastel Feature Card

Soft-tinted background (one of the accent palette: Mint, Sky, Apricot, Lavender, Periwinkle, Aqua), 24px border-radius, 24px internal padding, small monochrome icon, Poppins 16px weight 500 label. The 2:3 aspect ratio card is the system's workhorse tile.

### Board Mockup Card

White #ffffff surface, Mist (#d0d4e4) 1px border, 16–24px radius, soft shadow rgba(205,208,223,0.4) 0 2px 48px. Contains monday.com board rows with colored status pills and avatar stacks.

### AI Prompt Card

White surface, 6px radius, 12–16px padding, with a left brand-color icon, placeholder text in Slate, mic and send icons on the right. Hovers with subtle shadow lift.

### Brand Gradient Panel

Violet #6161ff background fills the entire right column, white card sits on top with 24px radius. Used in the AI section to create a 50/50 split with visual contrast against the white left column.

### Status Pill

Small pill (6px radius), tinted background matching status color (green/mint for done, orange for working, blue for stuck, red for stuck). Poppins 12–13px weight 500 label, 2px vertical / 8px horizontal padding.

### Avatar Stack

Circular avatars (full radius), 24–32px diameter, white 2px border separating overlapping members, slight negative margin between them.

### Logo Strip

Single-row horizontal layout of monochrome black wordmarks at ~60% opacity, centered, generous horizontal spacing. No card backgrounds or dividers between logos.

### Exploration Grid Card

White card, Mist 1px border, 6px radius, small square icon, 2-line Poppins label. Arranged in a 3-column grid on white panel with subtle shadow.

### Navigation Bar

White #ffffff background, sticky top, 8px vertical / 16px horizontal padding for nav items, monday.com wordmark on left, primary actions ('Contact sales' outlined, 'Get Started' filled) on right. Logo uses full-color spectrum conic gradient mark.

## Similar Design Systems

- {'why': 'Same product-as-hero pattern with embedded UI mockups and generous whitespace, though Asana leans warmer/coral while monday.com owns violet', 'business': 'Asana'}
- {'why': 'Both use soft pastel card surfaces and playful multi-color category tiles, though Notion is more text-dense and monday.com is more visually bold', 'business': 'Notion'}
- {'why': "Similar feature-rich SaaS marketing with product screenshots breaking the page boundary, though ClickUp's palette is more saturated and monday.com stays pastel", 'business': 'ClickUp'}
- {'why': "Shared single-accent-color brand strategy (Linear's purple = monday.com's violet) with minimal chrome and geometric sans typography", 'business': 'Linear'}
- {'why': "Comparable 'friendly enterprise' positioning with colored record-type cards, though Airtable uses sharper corners and a wider accent palette", 'business': 'Airtable'}

## Agent Prompt Guide

primary action: #6161ff (filled action)
Create a Primary Action Button: #6161ff background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
## Quick Color Reference
- Primary text: #333333
- Secondary text: #535768
- Page background: #f5f6f8
- Card surface: #ffffff
- Card border: #d0d4e4
- Brand accent: #6161ff

## 5 Example Component Prompts


2. **Pastel Feature Card**: Background #abf0ff (or one of the accent palette: #bcfe90, #ff8940, #eddff7, #93beff, #d1faff). 24px border-radius. 24px internal padding. Small monochrome icon top-left, Poppins 16px weight 500 label below in #333333.

3. **Board Mockup Card**: White #ffffff surface, 1px #d0d4e4 border, 24px border-radius, soft shadow rgba(205,208,223,0.4) 0 2px 48px. Contains rows with colored status pills (6px radius, tinted backgrounds like #bcfe90, #ff8940) and circular avatar stacks.

4. **AI Prompt Card**: White surface, 6px border-radius, 16px padding, brand-color icon left, placeholder text 'Analyze sales pipeline' in Poppins 16px weight 500 #333333, mic and send icons right.

5. **Logo Trust Strip**: Centered eyebrow text 16px Poppins weight 400 #535768 reading 'Trusted by over 60% of the Fortune 500'. Below: single horizontal row of 7–8 monochrome black wordmarks (Holt Renfrew, Universal, Coca-Cola, Lionsgate, Carrefour, BD, Glossier style) at ~60% opacity, generous 32–48px gap between logos, no dividers.

## Gradient System

Gradients serve three roles: (1) **Hero headline text** — linear pink-to-orange #fe81e4 → #fda900 injected into display copy to create emotional warmth against the white canvas. (2) **Brand prism** — conic gradient cycling violet → teal → green → yellow → pink → violet, used only for the logo mark and divider lines, never as a surface fill. (3) **CTA and illustration accent gradients** — short 2-stop linear gradients (cyan→violet, orange→pink) used sparingly on dark product panels and feature illustrations. Gradients are never applied to body text or button backgrounds.

## Component Visual Language

The system follows a **flat-with-soft-shadow** approach: components are mostly flat-shaded with surfaces distinguished by pastel background tints rather than borders or heavy elevation. The single soft lavender-tinted shadow (rgba(205,208,223,0.4) 0 2px 48px) lifts cards just enough to read as elevated without introducing the 'skeuomorphic card stack' look. Buttons are fully filled (no outline-first patterns) and rely on the pill radius for personality. The visual density is low — generous internal padding (24px in cards, 13–16px in buttons) and 64px between sections — making the system feel like a spacious workshop rather than a dense dashboard.
