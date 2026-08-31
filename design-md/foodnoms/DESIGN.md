# Foodnoms — Design System

> **North Star**: Sunlit fruit market on white porcelain — warm orange, fresh green, and generous rounded forms
> **Theme**: light
> **Source**: https://foodnoms.com
> **Refero Style**: https://styles.refero.design/style/1e7dae3b-cb34-4fcf-8c32-051152aebbab
> **Synced**: 2026-09-01

## Overview

Foodnoms presents a sunlit nutrition-tracker marketing language: pure white canvas, oversized phone mockups as the visual anchor, and a playful chromatic vocabulary where color codes nutrients and progress. The two-tone headline convention (one color for the win word, dark graphite for the rest) makes the value proposition scannable in a glance. The system leans on a single custom display face (Aquawax Pro) with a distinctly rounded, geometric character that softens the dense data-heavy app screens. Most surfaces are flat and shadowless; a uniform 26px corner radius gives buttons, cards, and tags a friendly, pillow-like feel that makes health tracking feel approachable rather than clinical.

## Color Palette

- **Ember Orange**: `#ff5406` — Orange supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [brand]
- **Verdant Green**: `#00b33f` — Green supporting accent for decorative details and low-frequency emphasis [accent]
- **Signal Red-Orange**: `#ff3400` — Secondary warm accent visible in app screen UI elements and supporting brand moments. Sits one step hotter than Ember Orange for emphasis on selected or active app states [accent]
- **Sky Blue**: `#00a9dd` — Cool counter-accent for app-internal data categories (carbs/protein/other nutrient groupings). Balances the warm-dominant palette inside phone mockups [accent]
- **Mist Blue**: `#72a2c5` — Muted cool accent — softens Sky Blue for secondary data labels and chart backgrounds inside the app surfaces [accent]
- **Sunset Orange**: `#ff6d00` — Warm accent for secondary headings and emphasis text within the marketing pages [accent]
- **Amber**: `#945300` — Deep warm accent for data-heavy text and chart labels in the app's nutrition displays [accent]
- **Alert Red**: `#ff001e` — Red supporting accent for decorative details and low-frequency emphasis [accent]
- **Plum**: `#bd4be5` — Accent for the carbs/protein/fat macro rings and category tags inside the app interface [accent]
- **Iris**: `#5856de` — Accent for headings and emphasis text on supporting pages, and for specific data categories inside the app [accent]
- **Electric Blue**: `#0099f9` — Accent for bold headings and highlighted text on supporting pages [accent]
- **Graphite**: `#2f2f2f` — Primary text, dark buttons (App Store badge), and icon strokes. The dominant non-white color in headings and body copy [neutral]
- **Charcoal**: `#000000` — Maximum-emphasis text and icon fills. Used sparingly — reserved for the darkest typographic moments and SVG icon details [neutral]
- **Fog**: `#f5f5f5` — Alternate canvas for cards, feature sections, and soft UI containers. Distinguishes elevated content blocks from the white page [neutral]
- **Paper White**: `#ffffff` — Dominant page background, button text, and card surfaces. The base layer of the entire visual system [neutral]

## Typography

- **Aquawax Pro Medium**
- **Aquawax Pro**
- **System sans-serif**
- **Aquawax Pro DemiBold**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| tiny | 12 | — | 1.2 |
| caption | 14 | — | 1.2 |
| body-sm | 16 | — | 1.4 |
| subheading | 20 | — | 1.8 |
| heading-sm | 22 | — | 1.2 |
| heading | 30 | — | 1.2 |
| display | 60 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 20px
- **Section Gap**: 96px
- **Border Radius**: {'tags': '26px', 'cards': '26px', 'inputs': '26px', 'buttons': '26px'}

## Layout

The page is a single-column, centered max-width layout (~1200px) with generous vertical rhythm. The header is a thin top bar with logo left, nav center, and filled orange action button right. The hero is a centered stack: two-tone display headline, single-line subhead, App Store badge, then a row of 3–5 phone mockups fanned across the full width. Below the hero, a centered 'As Featured By' press logo section in a 2×3 grid. Feature sections follow in a repeating pattern: two-column text + phone mockup, alternating sides, with section accent headings in orange/green. The final element before the footer is a full-width download CTA card. Section gaps are large (96px) creating a spacious, gallery-like feel. The navigation is a minimal top bar — no sidebar, no mega-menu.

## Surfaces / Elevation

- **Paper White**
- **Fog**
- **Graphite**
- **Ember Orange**

## Imagery

The visual language is dominated by high-fidelity iPhone device-frame mockups showing the live app interface — these are the heroes, not stock photography. The mockups are rendered at near-full opacity, fanned out with slight overlap and gentle rotation, floating directly on white. Inside the mockups, the app's own UI provides all the visual richness: nutrition data, food photos, macro rings, and colorful category tags. The only photographic content is user-submitted food imagery visible within the app's 'Scan Your Food' camera screen. No lifestyle photography, no abstract illustrations, no decorative graphics. The brand identity is carried entirely by the custom typeface, the orange/green/dark color system, and the app's own interface.

## Design Principles

### Do

- Use 26px border-radius on every interactive element and card — this is the system's signature softness
- Apply the two-tone headline pattern: one color for the outcome word, Graphite (#2f2f2f) for the rest
- Use Aquawax Pro Bold at 60px for hero displays and 30px for section headings — never interpolate intermediate sizes
- Pair Verdant Green (#00b33f) with positive/progress data and Signal Red-Orange (#ff3400) with negative/overage data inside app screens
- Use generous 96px section gaps between major page sections to let phone mockups breathe
- Keep all text on white or Fog (#f5f5f5) — never place chromatic text on chromatic backgrounds
- Show 3+ phone mockups side-by-side in the hero, slightly overlapping, to demonstrate the breadth of the app experience

### Don't

- Don't use box-shadows or drop-shadows anywhere — the system is deliberately flat
- Don't use a border-radius other than 26px on buttons, cards, tags, or inputs
- Don't call any color a 'CTA' or 'primary action' in the token system — describe them by their brand role instead
- Don't use Aquawax Pro at sizes below 12px — fall back to system sans-serif for micro UI
- Don't place chromatic text on a chromatic background — always pair color text with white or Fog
- Don't use gradient backgrounds or gradient buttons — the system is solid color only
- Don't introduce new chromatic colors for marketing pages — the warm-primary + cool-accent + app-data palette is complete

## Components

### Brand Wordmark

Logomark: a rounded orange square (color: Ember Orange) containing a white bar-chart icon. Wordmark: 'Foodnoms' in Aquawax Pro Bold, 18px, Graphite (#2f2f2f), sitting to the right of the icon. Total lockup height ~32px.

### Header Filled Button

Filled Ember Orange (#ff5406) background, white text 'Get the App' in Aquawax Pro DemiBold at ~16px, arrow icon after label. 26px border-radius, ~12px vertical padding, ~20px horizontal padding. Sits at the far right of the header.

### Ghost Nav Link

No background, Graphite (#2f2f2f) text, Aquawax Pro Medium ~16–17px, no underline. Hover/active state not detected; default is text-only.

### App Store Badge

Dark Graphite (#2f2f2f) rounded rectangle (~26px radius), Apple logo in white, 'Download on the App Store' text in white Aquawax Pro. ~56px tall. Sits centered beneath the hero subheadline.

### Two-Tone Display Headline

60px Aquawax Pro Bold, line-height 1.2. First phrase ('Lose Weight') in Verdant Green (#00b33f), second phrase ('with Foodnoms') in Graphite (#2f2f2f). Center-aligned, max-width constrained to keep the color split legible.

### Section Accent Heading

30px Aquawax Pro Bold. Often appears in Ember Orange (#ff5406) or a mix of two chromatic colors to maintain the brand's two-tone headline pattern. 'Effortlessly' in one accent, 'Scan Food' in another.

### Phone Mockup Carousel

Full device-frame iPhone renders at ~280px width, fanned out with slight overlap and rotation. No background card — they float directly on the white page. Contain the full app UI including status bar, navigation, and content screens.

### Press Logo Grid

2-row × 3-column grid of grayscale publication logos (MacStories, iMore, 9TO5Mac, POPSUGAR, Good Housekeeping, Prevention). Rendered in Charcoal (#000000) or Graphite (#2f2f2f), evenly spaced with ~64px column gap. Heading 'As Featured By' in Ember Orange above.

### Download CTA Card

White card with subtle Fog (#f5f5f5) background, 26px radius, ~32px padding. Contains a headline ('Get Started with Foodnoms Today'), subtext, and a filled Ember Orange 'Download' button with arrow icon. Sits at the bottom of the page above feature sections.

### App-Internal Data Card

White card with ~26px radius, light gray dividers. Contains large bold metric (e.g. '57g' for fat grams) in Verdant Green or Signal Red-Orange depending on positive/negative status, with secondary label text in Graphite at ~12–14px.

### Macro Category Ring

Circular ring showing progress toward a macro goal (Calories, Carbs, Fat, Protein). Each category has a distinct color: Signal Red-Orange for Calories, Sky Blue for Carbs, Verdant Green for Fat, Plum for Protein. Ring stroke ~8px, centered numeric value inside in Aquawax Pro Bold.

### Food Log Entry Row

White background row with bottom hairline border in Fog (#f5f5f5). Left side: food name in Graphite Aquawax Pro Medium ~17px, with macro subtext below in lighter gray ~14px. Right side: colored dot indicating macro category, with point values in matching color.

### Tab Bar

White bar with three tab icons (Food Log, Insights, Library), separated by thin gray dividers. Active tab indicated by Ember Orange fill/icon color and small dot indicator. Right edge has a floating Ember Orange circular '+' button for adding food.

### Goal Setup Card

White card, 26px radius, ~40px padding. Contains a heading, body text explaining the goal option, and a filled Ember Orange button ('Use Recommended Goal') stacked above a text-style 'Choose a Custom Goal' link. Decorative donut/breakfast icon at top.

## Similar Design Systems

- {'why': 'Same single-column marketing page structure with phone mockup hero rows and two-tone headlines over a white canvas', 'business': 'MyFitnessPal'}
- {'why': 'Similar large rounded display typography and warm-primary + cool-accent color logic for nutrition data dashboards', 'business': 'Cronometer'}
- {'why': 'Same generous 26px+ corner radius treatment and friendly geometric sans-serif display type for health tracking', 'business': 'Yazio'}
- {'why': 'Same flat-shadowless white-canvas approach with colorful accent typography and device-frame product showcases', 'business': 'Notion'}

## Agent Prompt Guide

## Quick Color Reference

- Primary text: #2f2f2f (Graphite)
- Background: #ffffff (Paper White)
- Alternate surface: #f5f5f5 (Fog)
- Brand accent (filled button, logo, heading color): #ff5406 (Ember Orange)
- Achievement accent (headline color, positive data): #00b33f (Verdant Green)
- App-internal cool accent: #00a9dd (Sky Blue)
- primary action: no distinct CTA color

## Example Component Prompts

1. **Hero Section**: White (#ffffff) background. Two-tone headline at 60px Aquawax Pro Bold, line-height 1.2: first phrase in Verdant Green (#00b33f), second phrase in Graphite (#2f2f2f), centered. Subtext in Graphite Aquawax Pro Medium 17px, line-height 1.6. Dark Graphite (#2f2f2f) App Store badge below, 26px radius, ~56px tall. Row of 3–5 iPhone mockups fanned across the width below.

2. **Feature Section Heading**: 30px Aquawax Pro Bold, line-height 1.2, in Ember Orange (#ff5406) for the first word and Graphite (#2f2f2f) for the second word, left-aligned. 96px top padding from previous section.

3. **Filled Brand Button**: Ember Orange (#ff5406) background, white text in Aquawax Pro DemiBold 16px, line-height 1.2, 26px border-radius, 12px vertical padding, 20px horizontal padding, with a small white arrow icon after the label.

4. **Press Logo Grid**: 2 rows × 3 columns of grayscale publication logos in Charcoal (#000000) or Graphite (#2f2f2f), 64px column gap, centered. Heading 'As Featured By' above in Ember Orange (#ff5406) at 20px Aquawax Pro Medium.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

## Two-Tone Headline System

A signature convention across the site: split a headline into two phrases, color the first (the verb/outcome) in a chromatic accent and the second (the object/brand) in Graphite. The accent color signals the *action* or *result*, while the dark second phrase anchors the sentence. Typical pairings: Verdant Green + Graphite for the hero (growth/winning), Ember Orange + Graphite for feature sections (action/enablement), or Ember Orange + Verdant Green for dual-accent section titles like 'Effortlessly Scan Food / Faster with AI'. Never use two chromatic colors as solid blocks of equal weight — the dark phrase is always the longer one.
