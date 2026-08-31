# Active Theory — Design System

> **North Star**: cosmic void with a single luminous portal — deep-space command deck where chrome whispers and the rendered world shouts
> **Theme**: dark
> **Source**: https://activetheory.net
> **Refero Style**: https://styles.refero.design/style/3416bd14-96bb-4c23-bd01-b2ea178ba5ce
> **Synced**: 2026-09-01

## Overview

Active Theory operates as a cosmic void stage where the immersive experience is the design and the UI chrome barely exists. The canvas is near-total black (#000000) with UI elements floating as whispered ghost containers — translucent surfaces, hairline borders, and pill-shaped controls that recede into the dark. Typography splits between an architectural geometric sans (nbarchitekt) for navigation and CTAs, and a deliberate editorial serif (Times) for body, creating an unexpected contrast that signals craft over convention. Color is rationed to a single muted violet accent (#343755) and pure white text — the page itself stays monochromatic so the rendered WebGL world carries all chromatic weight. Every UI decision prioritizes invisible-feeling chrome so the 3D scene reads as untethered floating in deep space.

## Color Palette

- **Void Black**: `#000000` — Page canvas, immersive background, card surfaces when stacked on dark — the absence of surface, not a color [neutral]
- **Ghost White**: `#ffffff` — Primary text, icon strokes, high-contrast labels — used at full opacity against pure black [neutral]
- **Ash Border**: `#4d4d4d` — Card borders, divider hairlines — barely-there separator that defines edges without adding visual weight [neutral]
- **Smoke**: `#808080` — Muted borders on ghost buttons, secondary chrome — recedes behind active controls [neutral]
- **Fog**: `#999999` — Medium-contrast borders, control outlines, and structural separators. Do not promote it to the primary CTA color [neutral]
- **Pale Mist**: `#c6c6c6` — Tertiary text, link default state, low-priority metadata — sits between white and gray for gentle hierarchy [neutral]
- **Dusk Violet**: `#343755` — Primary action fill — filled pill buttons, the only chromatic accent in the system; muted indigo reads as electric against void black without competing with the rendered scene [brand]

## Typography

- **nbarchitekt**
- **Times**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.5 |
| body-sm | 12 | — | 1.5 |
| body | 14 | — | 1.5 |

## Spacing & Layout

- **Card Padding**: 28px
- **Element Gap**: 6px
- **Section Gap**: 48px
- **Border Radius**: {'tags': '500px', 'cards': '12px', 'inputs': '5px', 'buttons-pill': '500px', 'buttons-ghost': '5px'}

## Layout

Full-bleed immersive canvas with no max-width constraint — the page is a single viewport of rendered 3D space, not a scrolling document. The nav sits as a floating ghost bar pinned to the top-right, occupying minimal visual real estate. The hero composition is centered (the portal emblem sits at the horizontal and vertical center of the viewport) with the aurora wash creating asymmetric balance from the top-left. No grid is visible in the captured section — content density is near zero because the rendered scene carries the visual load. When more conventional sections appear (work listings, contact), they likely overlay the 3D canvas as translucent panels rather than replacing it.

## Surfaces / Elevation

- **Void Canvas**
- **Translucent Overlay**
- **Dusk Violet Surface**
- **Frosted Glass**

## Imagery

This site is an immersive WebGL experience — the screenshot reveals a deep-space cosmic scene with a circular wireframe portal as the centerpiece, emanating a cyan-to-magenta rim glow with a faceted geometric mark at its core. Particle fields of green, gold, and cyan specks burst downward from the portal like a constellation collapsing into a fountain. A subtle green aurora wash bleeds from the top-left corner, adding atmospheric depth without dominating the composition. There is no photography or traditional illustration — the visual language is entirely rendered/real-time 3D. The UI chrome (top-right nav, cookie banner) is deliberately minimal so the 3D composition remains untouchable. Iconography is line-based and geometric when present, matching nbarchitekt's architectural character.

## Design Principles

### Do

- Use #000000 as the only canvas color — never introduce gray page backgrounds; the void must stay absolute
- Reach for Dusk Violet (#343755) only for singular dominant CTAs — the accent is rationed precisely because it competes with the 3D scene
- Use 500px border radius for all pill controls (buttons, tags) — partial rounding reads as inconsistent against the fully-pill primary
- Set body copy in Times at 16px line-height 1.88 — the serif + generous leading creates editorial breathing room against the dense 3D visuals
- Use 1px borders in #4d4d4d to define cards — never rely on shadows; the void cannot cast them
- Apply backdrop-filter: blur(4px) to any overlay panel — frosted glass is how depth is communicated in this system
- Keep nbarchitekt at 10-12px for nav and 14px weight 700 for button labels — the type scale is deliberately micro so chrome stays invisible

### Don't

- Do not introduce new chromatic accents — the palette is black, white, grays, and one violet; any additional hue will fight the rendered scene
- Do not use box-shadows on any element — elevation must come from translucency stacking and backdrop blur, never projected light
- Do not use solid white or solid gray card backgrounds — all surfaces must be translucent (rgba at 0.1-0.5) so the canvas bleeds through
- Do not set body text in nbarchitekt — Times serif is the deliberate editorial counterpoint; mixing UI sans for prose flattens the voice distinction
- Do not use rounding values between 5px and 500px — buttons are either sharp ghost rectangles (5px) or full pills (500px); intermediate radii look accidental
- Do not add gradients to UI chrome — the 3D scene carries all gradient richness; UI gradients would cheapen the stage
- Do not use light theme components even on bright sections — the system is dark-first; light mode would break the immersive continuity

## Components

### Ghost Navigation Button

Transparent background with 2px hairline border at rgba(255,255,255,0.6). 5px corner radius. 1px vertical / 6px horizontal padding — ultra-compact. Uppercase nbarchitekt 10-12px weight 400, white text. Sits flush right in the top-right corner, almost dissolving into the dark canvas.

### Pill Primary Button (Dusk Violet)

Dusk Violet (#343755) solid fill at full opacity. 500px border radius — fully pill-shaped. 4px vertical / 18px horizontal padding. nbarchitekt 14px weight 700 label in black. The only saturated color in the UI; used sparingly to mark singular actions.

### Pill Primary Button (Void Black)

Black (#000000) at 0.333 opacity over dark backgrounds. 500px border radius. 4px / 18px padding. nbarchitekt 14px weight 700 black text. A tonal alternative to the violet pill — same shape, no chromatic commitment.

### Translucent Cookie Banner

Dark translucent panel (rgba(0,0,0,0.5)) with 12px radius. 16px top / 28px horizontal / 32px bottom padding — generous bottom padding lifts the dismiss actions. No shadow; relies on backdrop-filter blur(4px) to separate from the 3D scene behind. Body copy in Times 16px lh=1.88, white text.

### Ghost Card Container

Pure transparent or near-black fill with 1px Ash Border (#4d4d4d) at 4d4d4d. 12px corner radius. 28px horizontal padding. No elevation shadow — boundaries are communicated by hairline border alone, preserving the floating-in-void feeling.

### Audio Toggle

Minimal icon-only control, likely ghost-button variant with 5px radius and chevron glyph. Positioned to not interfere with the central 3D composition. No text label — iconographic only.

### Navigation Divider Dot

A single small dot or hairline mark between Work and Contact. No fill, just spatial punctuation that avoids a hard line break while keeping the nav visually grouped.

### Hairline Link

Pale Mist (#c6c6c6) text, no underline by default. Times 16px weight 400. Renders at AA contrast against void black — legible but not aggressive, signaling the link is contextual rather than primary.

### Iconic Brand Emblem

Circular wireframe portal with internal geometric mark, rendered in WebGL. Cyan-to-magenta gradient glow rim against pure black. Particle field emanating outward in green/gold specks. Not a UI component per se, but functions as the primary brand mark — it IS the hero.

## Similar Design Systems

- {'why': 'Both are immersive WebGL creative studios whose portfolio sites are full-bleed 3D scenes with ghost UI chrome and near-total dark canvases', 'business': 'Resn'}
- {'why': 'Reference site — the design system described here', 'business': 'Active Theory itself'}
- {'why': 'Same dark-void aesthetic with floating geometric compositions and hairline-border UI; similar whisper-quiet chrome approach', 'business': 'Unseen Studios'}
- {'why': 'Dark immersive agency sites where the 3D work is the hero and UI is reduced to ghost labels and pill buttons', 'business': 'Tool of North America'}
- {'why': 'Both are immersive WebGL creative studios whose portfolio sites are full-bleed 3D scenes with ghost UI chrome and near-total dark canvases', 'business': 'Resn'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff
- background: #000000
- border: #4d4d4d
- accent / link: #c6c6c6
- primary action: #343755 (filled action)

**Example Component Prompts**

1. Create a ghost navigation button: transparent background, 2px solid rgba(255,255,255,0.6) border, 5px radius, 1px top/bottom and 6px left/right padding. Label in nbarchitekt 10px weight 400, uppercase, white. Position flush in the top-right corner over a pure black canvas.

2. Create a filled pill primary action button: #343755 background, 500px border radius, 4px top/bottom and 18px left/right padding. Label in nbarchitekt 14px weight 700, color black. Use this sparingly — only for singular dominant CTAs.

3. Create a translucent cookie banner: rgba(0,0,0,0.5) background with backdrop-filter blur(4px), 12px corner radius, 16px top padding, 28px horizontal padding, 32px bottom padding. No shadow. Body text in Times 16px line-height 1.88, white. Inline link text in #c6c6c6.

4. Create a ghost card for a project tile: no background fill (transparent), 1px solid #4d4d4d border, 12px corner radius, 28px horizontal padding. Content sits inside without elevation shadow. Title in nbarchitekt 14px weight 700, white. Description in Times 16px line-height 1.88, white.

5. Create a full-viewport immersive hero: pure #000000 canvas, centered 3D composition (abstract wireframe portal or geometric form), aurora gradient wash bleeding from one corner at very low opacity. UI chrome must be invisible at rest — nav appears as ghost button only on cursor approach.

## Motion & Atmosphere

Motion timing follows a deliberate cadence: micro-interactions at 0.2-0.4s with ease-out for UI feedback, while scene-level transitions run 0.8-9s with ease or linear for cinematic pacing. The dominant timing function is ease (61 occurrences) — not the modern cubic-bezier() trend, which signals a preference for organic, non-robotic motion curves. A named 'ticker' animation exists for sequential content reveals. Opacity is the primary transition property — UI elements fade in/out rather than sliding or scaling, reinforcing the ethereal floating-in-void metaphor. Any motion added to new pages should feel gravitational and unhurried, not snappy.

## Why So Minimal

Every color except one muted violet is achromatic. Every UI surface is translucent. Every border is a hairline. This is not laziness — it's because Active Theory's portfolio IS the rendered 3D/immersive experience. If the chrome competed with the WebGL scene, the work would be invisible. The design system is engineered to be a black velvet backdrop: the UI exists only to provide navigation and consent, and recedes the moment the user's attention shifts to the rendered world. When generating new pages for this brand, restraint is not a stylistic preference — it is the functional prerequisite for the immersive content to remain the hero.
