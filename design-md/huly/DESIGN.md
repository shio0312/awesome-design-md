# Huly — Design System

> **North Star**: Aurora through a midnight observatory — the hero is a vertical beam of violet melting into coral, and every quiet section below it borrows that same two-color story told at lower volume.
> **Theme**: mixed
> **Source**: https://huly.io
> **Refero Style**: https://styles.refero.design/style/d018e81d-6bb6-4445-86d7-39fd6be7e74d
> **Synced**: 2026-09-01

## Overview

Huly projects a cosmic-workspace atmosphere: near-black canvas with a single violet-to-amber aurora slicing through the hero, then a quieter productivity grid below. The system lives in a narrow chromatic band — one electric iris blue and one ember coral do all the brand work against layered graphite surfaces, so the dark mode never feels neutral. Typography is Inter for everything functional, with a custom display face (Esbuild) reserved for hero moments at 80–84px with aggressive negative tracking. Components lean pill-shaped: 9999px radii on controls, 12px on cards, minimal shadow, and glowing gradient strokes as the primary decoration. The page alternates between full-bleed dark spectacle and calm light sections, so any new screen must decide which mode it's in before picking colors.

## Color Palette

- **Obsidian Canvas**: `#303236` — Page background, dominant surface — near-black with a whisper of warmth, the default stage for all content [neutral]
- **Void**: `#090a0c` — Deepest surface layer for hero gradients, modal backdrops, and borders that need to disappear into the canvas [neutral]
- **Charcoal Card**: `#111111` — Elevated card and panel surfaces sitting one step above the canvas [neutral]
- **Slate Edge**: `#4a4b50` — Hairline borders and dividers on dark surfaces [neutral]
- **Iron Veil**: `#6b6c6d` — Muted backgrounds for tags, list-item fills, and disabled state washes [neutral]
- **Smoke**: `#95979e` — Icon strokes, secondary text, and inactive controls — the workhorse mid-gray [neutral]
- **Ash**: `#a9a9aa` — Tertiary text and subtle body borders in content-heavy lists [neutral]
- **Frost**: `#d1d1d1` — Light-mode borders, input fields, and secondary CTA borders [neutral]
- **Linen**: `#e5e5e7` — Light-mode surface tint and subtle section dividers in white backgrounds [neutral]
- **Snow**: `#ffffff` — Hairline borders, dividers, input outlines, and card edges on light surfaces. Do not promote it to the primary CTA color [neutral]
- **Electric Iris**: `#5683da` — Primary action background, active nav indicator, hero aurora cool stop — vivid violet-blue against charcoal reads as switched-on, not corporate [brand]
- **Ember Pulse**: `#ff8964` — Secondary accent, hero aurora warm stop, notification dot, illustration highlight — the amber that breaks the blue's composure and gives the beam its heat [brand]
- **Molasses**: `#5a250a` — Deep ember tone for dark-context borders, icon strokes, and tag fills when coral would be too bright [accent]

## Typography

- **Inter**
- **Esbuild**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.38 |
| body | 14 | — | 1.5 |
| body-lg | 16 | — | 1.5 |
| subheading | 18 | — | 1.5 |
| heading-sm | 22 | — | 1.25 |
| heading | 24 | — | 1.25 |
| display-sm | 32 | — | 1 |
| display | 80 | — | 0.9 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 12px
- **Section Gap**: 96px
- **Border Radius**: {'tags': '9999px', 'cards': '12px', 'inputs': '4px', 'panels': '30px', 'buttons': '9999px'}

## Layout

Full-bleed hero with a vertical aurora beam and headline left-aligned, product screenshot floating bottom-right. Below the hero, a max-width 1200px content area alternates dark and light bands. Each section is a single vertical block: heading + 3-column or 4-column card grid, separated by 96px gaps. The 'MetaBrain' section breaks the grid with a centered display heading and a mixed-size card mosaic (large featured card + smaller supporting cards). The page is content-dense by SaaS standards but uses the dark/light band alternation to give each section room to breathe. Navigation is a single transparent top bar that becomes opaque on scroll.

## Surfaces / Elevation

- **Obsidian Canvas**
- **Void**
- **Charcoal Card**
- **Light Canvas**
- **Linen**

**Shadow tokens:**

## Imagery

Hero is pure aurora gradient — no photography. All feature illustrations are real product UI screenshots (dark-mode kanban, inbox, calendar) wrapped in card frames, functioning as both evidence and decoration. No lifestyle photography, no stock imagery, no 3D renders. The only non-UI visual element is the warm radial sunburst glow at the base of the aurora, painted as a CSS gradient. Icons are monochrome line icons in #95979 or white, never multicolor. The system treats its own dark UI as the hero asset — the product is the photography.

## Design Principles

### Do

- Use 9999px radius for all buttons, tags, and pill controls — pill geometry is the system's signature shape
- Reserve Esbuild for display moments (28px and up); never use it for body, nav, or anything below 22px
- Pick a background mode first: dark (#303236 canvas) for product-heavy screens, white (#ffffff) for editorial sections — never blend them in one component
- Use Electric Iris (#5683da) for the single most important action per screen; let Ember Pulse (#ff8964) appear as warm punctuation in tags, dots, and gradient stops
- Apply the aurora gradient (iris → ember → white) as a narrow vertical or radial beam, never as a full background fill
- Set body text to 14px / line-height 1.5 / -0.14px tracking, and increase tracking compression proportionally with size (to -4px at 80px display)
- Stack dark and light sections as alternating bands with 96px vertical gaps to create the page's signature rhythm

### Don't

- Don't use sharp corners (0–8px) on buttons or tags — the system is pill-first
- Don't pair Inter display weights with the custom Esbuild; they fight each other at large sizes
- Don't apply the aurora gradient as a full-surface background — it loses its impact when it covers everything
- Don't introduce a third accent color; the iris/ember pair is the entire chromatic vocabulary
- Don't use shadows for elevation on dark cards — the system prefers borders (#4a4b50) and color contrast over drop shadows
- Don't use Esbuild below 28px or in body copy — it was designed for headlines, and its tight tracking crushes readability at small sizes
- Don't put white text on a white section, or #303236 text on the dark canvas without checking contrast — the dark palette has narrow readable bands

## Components

### Primary Pill Button

Filled #5683da, white text, Inter 14px weight 500, 9999px radius, 12px 24px padding. Inherits Electric Iris glow on hover. Uppercase or sentence-case tracking at -0.01em.

### Ghost Pill Button

Transparent background, 1px #303236 border on dark surfaces, white text, Inter 14px weight 500, 9999px radius, 10px 20px padding. Becomes solid white-on-charcoal on hover.

### White Pill Button

Solid #ffffff fill with dark text (#090a0c), 9999px radius, 12px 24px padding. This is the hero — 'SEE IN ACTION →' — and the one place white earns its weight as a foreground, not background.

### Feature Card

Dark card on #111111 or gradient-tinted surface, 12px radius, 24px padding, optional 1px #4a4b50 border. Some variants carry a radial coral-to-amber glow behind the card edge.

### MetaBrain Card

Deep card (#0e0e10 base) with 12px radius, 16–20px padding, containing an Esbuild 32px heading in white. Many carry a soft radial gradient bleed in the corner — warm amber or cool iris — as the visual hook.

### Product Screenshot Frame

Dark UI surface (matching the real product) wrapped in a 12px radius frame with a soft black shadow (rgba(0,0,0,0.5) 0 6px 25px). Floats above the aurora background as the hero's evidence.

### Top Navigation Bar

Transparent over the hero, sticks with a slight backdrop blur on scroll. Huly logo mark on the left, Inter 14px nav items in the center, 'Star Us' link + outlined 'Sign In' + filled 'Sign Up' pill on the right.

### Aurora Hero Background

Vertical light beam on #090a0c: linear gradient from Electric Iris (#5683da at ~60% opacity) through Ember Pulse (#ff8964) to white, painted as a narrow vertical streak. Radial sunburst glow at the base in warm amber.

### Tag/Chip

Small pill (9999px radius), 4px 10px padding, 11px Inter weight 500, text colored to match category — Medium (iris), Marketing (ember), Done (ash), Medium with custom hex variants. Background is the category color at 12% opacity.

### Stat Counter

Large Esbuild numeral (80px) in white inside a 30px-radius circle, with a + button below. The oversized number in a circle is the section's visual signature.

### Light Section Band

White (#ffffff) or warm linen (#f6f6f6) background, Esbuild display heading in #050506, Inter body in #303236. The contrast flip from dark hero to light band is the page's structural rhythm.

### Kanban Board Preview

Mini dark-mode kanban with columns (BACKLOG, TO DO, IN PROGRESS) rendered in-product, wrapped in a 12px card with subtle shadow. Shows tags and avatars at real product scale.

### Inbox/Chat Panel

Dark panel with avatar circles, 12px radius, user names in Inter 14px weight 500 white, message previews in #a9a9aa. Includes 'Unread' pills and status dots in iris blue.

## Similar Design Systems

- {'why': 'Same dark-canvas productivity app aesthetic with a single vivid accent (Linear uses purple, Huly uses iris-blue), pill-shaped controls, and product-UI-as-hero photography', 'business': 'Linear'}
- {'why': 'Same dramatic gradient hero treatment (vertical beam on near-black) and display-headline-at-80px approach with tight letter-spacing', 'business': 'Vercel'}
- {'why': 'Same dark-mode-first product UI with warm-to-cool gradient washes and pill geometry on controls', 'business': 'Arc Browser'}
- {'why': 'Same alternating dark/light section rhythm, minimal shadow approach, and 9999px button radii as a brand signature', 'business': 'Resend'}
- {'why': 'Same use of gradient hero beams and product screenshots floating over atmospheric backgrounds, with Inter as the workhorse UI face', 'business': 'Stripe'}

## Agent Prompt Guide

primary action: #5683da (filled action)
Create a Primary Action Button: #5683da background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
## Quick Color Reference
- Canvas (dark): #303236
- Canvas (light): #ffffff
- Primary text on dark: #ffffff
- Primary text on light: #050506
- Border dark: #4a4b50
- Border light: #d1d1d1
- Accent: #5683da (Electric Iris) for primary actions
- Warm accent: #ff8964 (Ember Pulse) for highlights, tags, gradient stops

## Example Component Prompts


2. **Feature card grid**: 4-column grid on white (#ffffff) section. Each card: #111111 background, 12px radius, 24px padding, 1px #4a4b50 border. Card heading: Esbuild 28px weight 500, #ffffff. Card body: Inter 14px weight 400, #a9a9aa. Optional radial gradient bleed in corner (rgba(255,137,100,0.15) fading to transparent).

3. **Product screenshot frame**: In-app dark UI screenshot wrapped in a 12px-radius container with shadow rgba(0,0,0,0.5) 0 6px 25px. Floats over the aurora background at the bottom of the hero.

4. **Tag chip**: 9999px radius, 4px 10px padding, Inter 11px weight 500. Background: category color at 12% opacity. Text: category color at full saturation (e.g., #5683da text on rgba(86,131,218,0.12) background).

5. **Top navigation**: Transparent over hero. Huly logo left (interlocking shapes mark). Center: Inter 14px weight 400, #ffffff, 24px gaps. Right: 'Star Us' text link + outlined 'Sign In' ghost pill (1px #303236 border, 9999px radius) + filled 'Sign Up' pill (#5683da, white text, 9999px radius, 10px 20px padding).

## Gradient System

Two gradient families serve distinct purposes:

**Aurora beam** (hero only): linear-gradient(180deg, Electric Iris → Ember Pulse → white) painted as a narrow vertical streak, 15–25% page width. This is the brand's signature visual — it should appear once per page, not repeated.

**Radial sunburst** (feature card glows): radial-gradient from warm amber (#ffaa81) through soft yellow (#ffda9f) to transparent. Painted as a 200–400px circle bleeding from a card corner, at 30–50% opacity. Provides warmth without competing with the hero aurora.

**Section transitions** (rare): linear-gradient from white to soft violet-tint (#d5d8f6) for the MetaBrain section's light-to-product bridge.

Never stack two full-opacity gradients in the same viewport.
