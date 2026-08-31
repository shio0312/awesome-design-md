# Superpower — Design System

> **North Star**: Bioluminescent health command center
> **Theme**: light
> **Source**: https://superpower.com
> **Refero Style**: https://styles.refero.design/style/5d34568d-4bdc-445d-a527-c6f5249fa8fb
> **Synced**: 2026-09-01

## Overview

Superpower wraps a serious clinical promise in cinematic, atmospheric UI: full-bleed dark photography heroes transition into crisp white content surfaces, with one vivid sunrise-orange accent pulsing through the system. Typography carries the brand — a proprietary geometric sans at whisper-tight negative tracking, scaling from 11px metadata to 66px display with line-heights that compress as sizes grow (1.00 at display, 1.40–1.50 at body). A floating dark pill navigation bar hovers over imagery, and pill-shaped CTAs create a tension between clinical precision and warm vitality. Surfaces are mostly flat — the system relies on generous white space, hairline zinc dividers, and a single faint shadow pattern rather than heavy elevation. Color is rationed: nearly everything is black, white, or zinc-gray, and the orange appears only as functional punctuation on actions and brand marks.

## Color Palette

- **Sunrise Coral**: `#fc5f2b` — Orange supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Coral Glow**: `#ff8b64` — Gradient endpoint paired with Sunrise Coral for decorative membership card wash [brand]
- **Carbon Black**: `#18181b` — Primary text, floating navigation bar fill, headings, icon strokes [neutral]
- **Pure Black**: `#000000` — Logo wordmark, deep contrast borders [neutral]
- **Zinc Gray**: `#71717a` — Body text, secondary descriptions, muted metadata, helper copy [neutral]
- **Ash Gray**: `#a1a1aa` — Tertiary text, inactive borders, disabled states [neutral]
- **Mist Gray**: `#e4e4e7` — Hairline borders, card outlines, divider lines, button borders [neutral]
- **Fog Gray**: `#f4f4f5` — Subtle surface elevation, muted backgrounds, image overlay scrim base [neutral]
- **Paper White**: `#ffffff` — Page background, card surfaces, text on dark images, button text [neutral]

## Typography

- **NB International Pro**
- **NB International Mono Pro**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.5 |
| body | 15 | — | 1.5 |
| body-lg | 17 | — | 1.4 |
| subheading | 19 | — | 1.4 |
| heading-sm | 22 | — | 1.25 |
| heading | 30 | — | 1.2 |
| heading-lg | 45 | — | 1.13 |
| display | 66 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 19px
- **Element Gap**: 11px
- **Section Gap**: 75px
- **Border Radius**: {'cards': '15px', 'icons': '7.5px', 'pills': '9999px', 'navBar': '15px', 'buttons': '9999px', 'smallCards': '5px'}

## Surfaces / Elevation

- **Page Canvas**
- **Card Surface**
- **Muted Surface**
- **Floating Nav**

**Shadow tokens:**

## Imagery

Full-bleed cinematic photography dominates the hero — a person silhouetted against a deep teal-blue sky, the image intentionally dark and moody to create emotional weight and counterpoint the clinical health promise. Secondary imagery uses tight, contained product-style crops (the marbled orange membership card, app screenshots) rather than lifestyle photography. No illustrations, no 3D renders, no abstract graphics — the photographic contrast IS the visual identity. The membership card features an organic marbled/lava-lamp pattern in Sunrise Coral tones, the only decorative visual element. Icons are line-based with a 7.5px radius (soft squircle), using thin strokes in Carbon Black.

## Design Principles

### Do

- Use Sunrise Coral (#fc5f2b) exclusively for filled primary action buttons and the brand mark — never for body text, icons, or decorative backgrounds
- Set display headlines at weight 400 with letter-spacing -0.025em and line-height 1.0 — the whisper-weight is the signature
- Float the navigation as a dark pill capsule over imagery, never as a flat top bar
- Use 9999px border-radius for all buttons and nav CTAs to maintain the pill system
- Layer the surface stack as white → mist gray → carbon black — no mid-tone chromatic surfaces
- Use the marbled coral gradient ONLY for the membership visual card — it's a one-of-a-kind brand asset, not a reusable pattern
- Pair every primary CTA with a trust badge row (HSA/FSA, payment icons) directly below at 11-13px Zinc Gray

### Don't

- Don't apply heavy drop shadows — the system uses a single 2px hairline shadow at most, and most cards have no shadow at all
- Don't use weight 700 for display headlines — weight 400 at 56-66px is the rule, 700 is reserved for small labels and button text
- Don't introduce additional chromatic colors — the system is deliberately dichromatic (coral + neutrals)
- Don't use square corners on cards — minimum 5px radius, cards default to 15px
- Don't place body text on the hero image without a dark scrim or sufficient contrast — the hero photo is intentionally dark for text legibility
- Don't use outlined or ghost variants of the coral CTA — it is always a filled pill
- Don't stretch the marbled gradient across backgrounds or section dividers — it belongs only on the membership card artwork

## Components

### Floating Pill Navigation

Dark Carbon Black (#18181b) pill-shaped bar, ~15px radius, floats over hero imagery with generous internal padding (~12px vertical, ~19px horizontal). Logo wordmark left in white, center nav links in white/60 opacity, orange Sunrise Coral CTA button right. The floating pill is a signature element — it never sticks to viewport edges but always appears as a contained capsule.

### Primary Pill CTA

Sunrise Coral (#fc5f2b) fill, white text at 15-17px weight 700, 9999px border-radius, ~15px vertical × ~24-32px horizontal padding. Tight letter-spacing (-0.009em). Right-arrow chevron after label. No drop shadow — relies on color contrast alone.

### Ghost Text Link

No background, no border. White or Carbon Black text at 13-15px weight 400 with tight tracking. Underline appears on hover only. Used for nav items and inline content links.

### Hero Overlay Headline

66px display size, weight 400 (NOT 700 — the whisper-weight is deliberate), line-height 1.0, letter-spacing -0.025em, white (#ffffff) text, centered over full-bleed dark photography. This weight-400-at-display-size choice is the system's most distinctive typographic decision.

### Hero Subhead

17px body-lg, weight 400, Zinc Gray (#71717a) on white sections, white at reduced opacity on dark hero. Centered, max-width ~480px.

### Membership Visual Card

Organic marbled pattern in Sunrise Coral gradient (linear 88deg from #fc5f2b to #ff8b64 fading to white), 15px radius, ~320px wide. Contains 'superpower membership' wordmark top-left and '$17/month' price block bottom-left in white. The only decorative visual on the site.

### Membership Feature List

Vertical list with Sunrise Coral checkmark icons (7.5px radius squircle), 19px body text in Carbon Black, 11px row gap. Checks are filled solid coral, not outlined.

### Section Heading

45-56px heading-lg/display, weight 400, letter-spacing -0.015 to -0.022em, Carbon Black. Generous bottom margin (~30-40px). Left-aligned in content sections, centered over imagery.

### FAQ Item / Read More

Large heading at 30-37px paired with a small ghost-style 'Read more' text link right-aligned. No box, no border — relies on whitespace and type size for separation.

### Trust Badge Row

Horizontal row of small icons and labels at 11-13px, Zinc Gray text, with tiny check or icon glyphs in Carbon Black. Sits directly below primary CTA as a conversion reassurance pattern.

### Photo Thumbnail Strip

Horizontal row of 5-6 small rectangular thumbnails (~80-100px wide), 5px radius, showing app/dashboard screenshots. One thumbnail is active with a Sunrise Coral border.

## Similar Design Systems

- {'why': 'Same full-bleed dark hero photography with a single warm accent color and large whispered-weight display type', 'business': 'Eight Sleep'}
- {'why': 'Dichromatic health-tech palette (neutral + single vivid accent), pill CTAs, and flat-surface card system', 'business': 'Whoop'}
- {'why': 'Compact density, tight negative letter-spacing on display type, and dark floating pill navigation over imagery', 'business': 'Levels'}
- {'why': 'Clinical/wellness tone with full-bleed atmospheric photography and rationed color use', 'business': 'Function Health'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #18181b (Carbon Black)
- background: #ffffff (Paper White)
- border: #e4e4e7 (Mist Gray)
- muted text: #71717a (Zinc Gray)
- accent: #fc5f2b (Sunrise Coral)
- primary action: no distinct CTA color

**3 Example Component Prompts**

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.


3. **FAQ Section**: White background, max-width 1200px centered. 'Frequently Asked Questions' heading at 45px weight 400 #18181b, left-aligned, 75px top margin. FAQ items: 30px question text in #18181b weight 400, 'Read more' ghost text link right-aligned at 13px #71717a. 11px row gap between items, no dividers or borders.
