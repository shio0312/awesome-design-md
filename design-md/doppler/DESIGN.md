# Doppler — Design System

> **North Star**: violet-lit vault at midnight. A near-black canvas glows with a single lavender signal and a green confirmation light, every surface rounded just enough to feel handled.
> **Theme**: dark
> **Source**: https://doppler.com
> **Refero Style**: https://styles.refero.design/style/10654184-eb92-4b75-a7af-bd92bc6cdc5c
> **Synced**: 2026-09-01

## Overview

Doppler operates as a dark-mode security console: a near-black violet-tinted canvas (#1c1624) with whisper-thin light borders, one vivid green that signals 'go', and one lavender violet that carries brand voice in headlines and highlights. The interface feels like a vault UI — dense product surfaces, glass-blur header, 20px rounded cards floating on a midnight field. Typography is a single custom geometric sans (Doppler Repro) that tightens aggressively at large sizes (-0.02em) for a compressed, engineered feel. Color is rationed: green appears only where action is requested, violet only where brand voice is needed, everything else is monochrome. The hero headline uses a multi-stop violet gradient to create a single moment of chromatic warmth before the page settles back into its dark security posture.

## Color Palette

- **Midnight Plum**: `#1c1624` — Page canvas, primary dark surface — the near-black with a violet undertone that gives the UI its cool, secure temperature [neutral]
- **Shadow Plum**: `#2d2734` — Elevated card surface, input fields, nested panels — one step lighter than canvas to suggest depth without a shadow [neutral]
- **Bone White**: `#f1f0ec` — Primary text, icon strokes, button labels on dark — warm off-white avoids the sterile feel of pure white against violet-black [neutral]
- **Fog Line**: `#e5e7eb` — Hairline borders, dividers, card outlines — the most-used neutral in the system, defining every container edge [neutral]
- **Ash Veil**: `#d0c9c4` — Muted secondary text, disabled labels, ghost button text — sits between white and mid-gray for tertiary hierarchy [neutral]
- **Mid Ash**: `#a5a2a5` — Muted helper text, placeholder copy, secondary metadata — low-priority text that recedes [neutral]
- **Iron Edge**: `#55505b` — Subtle dividers, input borders in resting state — barely visible structural lines [neutral]
- **Lavender Spark**: `#b997ff` — Violet supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Signal Green**: `#00f575` — Green supporting accent for decorative details and low-frequency emphasis [brand]
- **Neon Violet**: `#6b13f5` — Radial gradient anchor, deep brand violet used in decorative aurora effects behind hero text [brand]
- **Ember Orange**: `#ff5632` — Terminal color in the violet-to-orange hero gradient — adds warmth to the cool palette at the gradient terminus [brand]
- **Plasma Pink**: `#ff9efa` — Radial gradient origin point — the pink hotspot in the aurora glow behind the hero [brand]

## Typography

- **Doppler Repro**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.4 |
| heading-sm | 24 | — | 1.2 |
| heading | 32 | — | 1.15 |
| heading-lg | 48 | — | 1.05 |
| display | 64 | — | 1.05 |
| display-xl | 96 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 16px
- **Section Gap**: 64px
- **Border Radius**: {'cards': '20px', 'pills': '9999px', 'buttons': '12px', 'large-features': '20px', 'small-elements': '8px'}

## Layout

Max-width 1200px centered container with generous side padding. Hero is a 2-column split: headline + CTA on the left (50%), product screenshot on the right (50%), with the radial gradient glow centered behind the screenshot. Below the hero, a 4-column card grid for integrations with 20px gaps. Then a centered section heading followed by a 3-column feature card grid. Navigation is a sticky glass header with centered logo+nav and right-aligned CTA cluster. Vertical rhythm: 64px section gaps, 32px card padding, 16px element spacing. The layout is always symmetric and centered — no asymmetric or off-grid compositions.

## Surfaces / Elevation

- **Canvas**
- **Card Surface**
- **Elevated Panel**

**Shadow tokens:**

## Imagery

Product screenshots are the primary visual element — the Doppler dashboard UI rendered at large scale in the hero and feature sections. These screenshots use the same dark palette as the marketing site, creating visual continuity. Integration partner logos (AWS, Azure, GCP, GitHub, etc.) appear as contained 48-64px marks inside cards. No photography, no lifestyle imagery, no illustrations — the product UI IS the hero. Background atmosphere comes from a soft radial gradient (violet→pink→dark) behind the hero, providing subtle warmth without competing with the product shot.

## Design Principles

### Do

- Use #00f575 only for the single most important action per viewport — it is a rationed resource, not a decorative color
- Apply the 20px radius to all card surfaces, 12px to all buttons, 8px to small inline elements like tags or badges
- Set letter-spacing to -0.02em on any text 48px and above, and 0.03em on any text 12px and below
- Use #b997ff for brand wordmarks, highlighted headline words, and eyebrow labels — never for body text or backgrounds
- Separate surfaces with #e5e7eb at 10-15% opacity borders, not with box-shadows or color fills
- Keep the hero product screenshot at or above 50% viewport width — the product IS the hero
- Use weight 450 as the default body and UI weight — weight 500 for headings, weight 700 only for display-size headlines

### Don't

- Don't add more than one filled green button per viewport — the signal loses meaning with repetition
- Don't use #b997ff or #00f575 for large background fills — these are accent colors, not surface colors
- Don't introduce drop shadows on cards — the system uses surface color steps, not elevation shadows
- Don't use pure white (#ffffff) for text — the warm off-white #f1f0ec is the system standard
- Don't break the single-font rule — Doppler Repro handles everything from captions to displays
- Don't use asymmetric or off-grid layouts — every section is centered and symmetrically balanced
- Don't add photography, lifestyle imagery, or decorative illustrations — product screenshots and logos are the only visual content

## Components

### Primary Action Button

Background #00f575, text #000000, radius 12px, padding 12px 24px, font weight 500 at 15px. The high-contrast green-on-black-text combination is the loudest visual element on any page — it should appear sparingly, no more than 1-2 per viewport. Includes a right arrow icon (→) after the label.

### Ghost Nav Button

Transparent background, 1px border in #55505b or #e5e7eb at 30% opacity, text #f1f0ec, radius 12px, padding 8px 16px, font weight 450 at 14px. Sits next to the green CTA without competing for attention.

### Integration Card

Background #2d2734, 1px hairline border in #e5e7eb at ~15% opacity, radius 20px, padding 32px. Contains a 48-64px brand logo at top, h3 heading at 24px weight 500 in #f1f0ec, body text at 14-15px in #d0c9c4, and a 'Learn More →' link at bottom. Cards sit in a 4-column grid with 16-20px gaps.

### Why-Choose Feature Card

Background #2d2734, border #e5e7eb at low opacity, radius 20px, padding 32px. Contains a mini product screenshot or icon at top, followed by heading and body text. Wider format than integration cards, sometimes 2-column internal layout.

### Glass Header

Background #1c1624 at ~80% opacity with backdrop-filter blur, 1px bottom border in #e5e7eb at 10% opacity. Contains the Doppler wordmark (left), nav links (center-left, weight 450 at 14px), and CTA cluster (right: ghost 'Get Demo' + green 'Start for Free' + ghost 'Sign In'). Padding 16px 32px.

### Hero Headline

Font size 64-96px, weight 700, line-height 1.0-1.05, letter-spacing -0.02em. Text in #f1f0ec with one or two key words in #b997ff or the violet-to-orange gradient. The word 'Keep' in the hero uses a background-clip gradient creating a sunset effect from violet to ember.

### Gradient Highlighted Text

Uses background: linear-gradient(91deg, #855aff, #ff5632) with -webkit-background-clip: text and -webkit-text-fill-color: transparent. Applied to 1-2 key words per headline. The gradient runs left-to-right, warm at the end.

### Product Screenshot Frame

Contained in a dark card surface (#2d2734) with 20px radius, 1px border, and a subtle box-shadow. The product UI itself uses a dark theme with purple accents matching the site. Often shown at slight perspective or with a glow halo.

### Top Banner

Full-width strip at top, background #1c1624 with a slightly lighter tint, padding 6-10px vertical, text centered at 12-14px in #f1f0ec. Contains an inline link in #00f575 or #b997ff. Dismissable with a close button at right.

### Section Heading

Font size 32-48px, weight 500, line-height 1.15, letter-spacing -0.01em, text #f1f0ec. Centered above section content. May be preceded by a small eyebrow label in #b997ff at 12-14px with 0.03em tracking.

### Link / Inline CTA

Color #f1f0ec or #b997ff, weight 500 at 14-15px, followed by a right arrow (→). Underline appears on hover only. No box or background — purely inline.

### Logo Lockup

Asterisk icon in #b997ff (the lavender violet, the brand's chromatic signature), wordmark 'Doppler' in #f1f0ec at weight 500, ~20px. The asterisk is the visual anchor — it appears in the same violet across the brand.

## Similar Design Systems

- {'why': 'Same dark-mode product-UI-as-hero approach, similar geometric sans typography with tight tracking at large sizes, purple-tinted dark canvas with single accent for action', 'business': 'Linear'}
- {'why': 'Dark canvas with rationed color usage, geometric sans at all sizes, product screenshots as primary visual content, minimal decoration', 'business': 'Vercel'}
- {'why': 'Dark purple-tinted canvas, single vivid accent for primary action, product-forward hero with dashboard screenshot, 20px card radii', 'business': 'Railway'}
- {'why': 'Dark mode developer-tool aesthetic with green accent for action, monospace-influenced geometric sans, product UI as hero visual', 'business': 'Supabase'}
- {'why': 'Dark canvas with high-contrast accent color for CTAs, developer-focused density, single custom font handling all type roles, minimal decorative imagery', 'business': 'PlanetScale'}

## Agent Prompt Guide

## Quick Color Reference
- text: #f1f0ec
- background: #1c1624
- border: #e5e7eb (at 15% opacity)
- accent: #b997ff
- primary action: no distinct CTA color

## Example Component Prompts

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Integration Card**: Background #2d2734, border 1px #e5e7eb at 15% opacity, radius 20px, padding 32px. Top: 56px partner logo. Heading 'Doppler + AWS' at 24px weight 500, color #f1f0ec, letter-spacing -0.24px. Body at 15px weight 400, color #d0c9c4, line-height 1.5. Bottom: 'Learn More →' link at 14px weight 500, color #f1f0ec.

3. **Glass Header**: Sticky, full-width, background #1c1624 at 80% opacity with backdrop-filter blur(12px), border-bottom 1px #e5e7eb at 10% opacity. Height ~64px, padding 0 32px. Left: asterisk icon #b997ff + 'Doppler' wordmark in #f1f0ec at 18px weight 500. Center-left: nav links at 14px weight 450, color #f1f0ec, with 24px horizontal gaps. Right cluster: ghost 'Get Demo' button (transparent bg, 1px #55505b border, 12px radius, 8px 16px padding) + filled 'Start for Free' button (#00f575, #000000 text, 12px radius) + ghost 'Sign In' button.

4. **Feature Grid Section**: Background #1c1624, section padding 64px vertical. Centered section heading: 'Why companies choose Doppler' at 48px weight 500, #f1f0ec, letter-spacing -0.96px, max-width 700px. Below: 3-column grid with 20px gaps, each card at #2d2734 with 20px radius and 1px #e5e7eb/15% border, padding 32px. Card content: 120px tall preview area at top, then h3 at 24px weight 500, body at 15px weight 400 in #d0c9c4.

5. **Gradient Highlighted Word**: Inline span within a headline. CSS: background: linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; display: inline-block. Apply to a single word in a 64px+ headline to create the signature warm-cool gradient moment.

## Color Rationing Philosophy

The system uses exactly two chromatic colors with strict role separation: #b997ff (lavender) is for brand voice and identity, #00f575 (green) is for action confirmation. They never overlap in role. Lavender never appears on a button; green never appears in a headline. This creates a visual grammar where users learn: 'if it's green, I can click it; if it's violet, it's speaking to me as the brand.' Every other color is a neutral on the dark canvas. The result is an interface that feels calm and information-dense while still having clear moments of color — but those moments are earned, not decorative.
