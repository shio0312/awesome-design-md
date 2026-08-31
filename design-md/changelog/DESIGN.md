# Changelog — Design System

> **North Star**: observatory console behind dark glass.
> **Theme**: dark
> **Source**: https://linear.app/changelog
> **Refero Style**: https://styles.refero.design/style/a5cc9b0f-d274-458a-b990-d18482b70838
> **Synced**: 2026-09-01

## Overview

Linear operates in a deep-space monochrome: a near-black canvas (#08090a) layered with whisper-quiet neutral surfaces, hairline borders at 4–5px radius, and almost no chromatic presence. The entire interface reads as machined precision — Inter Variable at custom weights (400, 500, 510, 590) with negative tracking, and Berkeley Mono reserved for inline code references. Elevation is implied by stacked grays and 1px strokes, never by drop shadows. Buttons are pill-shaped (9999px) outlined in white, never filled with brand color — confidence comes from contrast and restraint, not from accents. The result feels like an engineering control surface: dense, calm, and information-first.

## Color Palette

- **Onyx Canvas**: `#08090a` — Page background, primary surface [neutral]
- **Carbon Surface**: `#141516` — Elevated card, input field, subtle surface layer [neutral]
- **Graphite Surface**: `#1c1c1f` — Mid-elevation panels, nested surfaces [neutral]
- **Smoke Surface**: `#23252a` — Hover state, deeper card, button surface tone [neutral]
- **Iron Surface**: `#2d2e31` — Pressed/active surface, highest tier elevation [neutral]
- **Ash Border**: `#34343a` — Primary hairline border — dividers, table rows, list separators [neutral]
- **Ferrite Border**: `#3e3e44` — Inner shadow stroke, focus-adjacent borders, subtle 1px outlines [neutral]
- **Steel Text**: `#62666d` — Tertiary text, icon muted state, low-emphasis helper text [neutral]
- **Pewter Text**: `#7f7f80` — Disabled text, placeholder-tier secondary content [neutral]
- **Fog Text**: `#8a8f98` — Muted body text, metadata, timestamps, nav sub-items [neutral]
- **Mist Text**: `#d0d6e0` — Secondary text, descriptions, list body, paragraph fallback [neutral]
- **Chalk Border**: `#e4e5e9` — Light icon accent, rare light-tone dividers [neutral]
- **Snow**: `#f7f8f8` — Primary text, headings, logo, pill button border — the only near-white [neutral]
- **Void**: `#030404` — Deepest recess, box-shadow tint, absolute dark accent [neutral]

## Typography

- **Inter Variable**
- **Berkeley Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.6 |
| body | 15 | — | 1.5 |
| heading-sm | 24 | — | 1.33 |
| heading | 32 | — | 1.2 |
| display | 48 | — | 1.13 |

## Spacing & Layout

- **Max Width**: 1080px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 48px
- **Border Radius**: {'nav': '9999px', 'tags': '4px', 'cards': '8px', 'icons': '4.4625px', 'inputs': '4px', 'buttons': '9999px'}

## Layout

Full-bleed dark canvas with a max-width content column (~640–720px) centered for prose, expanding to ~1080px for wider sections. The page is single-column changelog: a sticky top nav, then a large section title ('Now') with inline tab nav, followed by dated entries stacked vertically with generous 48px section gaps. Each entry uses a left-aligned date marker and right-flowing content. No multi-column grids in the main flow — the icon grid is the only matrix layout, centered as a contained block. Navigation is minimal: a single top bar with logo, 6 text links, and a outlined pill CTA. No sidebar, no mega-menu, no footer in viewport.

## Surfaces / Elevation

- **Onyx Canvas**
- **Carbon**
- **Graphite**
- **Smoke**
- **Iron**

## Imagery

Visual language is UI-dominant with minimal decorative imagery. The page features inline product screenshots and app connector icon grids — small rounded squares (8px radius) showing brand glyphs in white on dark surfaces. Product illustrations are contained, not full-bleed, and sit within the content column at modest sizes. The only gradient is a subtle horizontal shimmer (#e4e5e9 → #9c9da1) likely used on the logo or a brand mark. No lifestyle photography, no abstract atmospheric renders — the interface itself is the visual.

## Design Principles

### Do

- Use 9999px radius for all action buttons, nav items, and tag pills — pill-shaped controls are the signature geometry.
- Set primary text and borders to #f7f8f8 against #08090a canvas — the near-white-on-near-black contrast is the entire brand.
- Use Inter Variable at weight 510 for headings and 590 for emphasis — avoid 600/700 bold, the half-step weights are the signature.
- Apply negative letter-spacing across all sizes: -0.010em for body, scaling to -0.022em at display 48px.
- Layer surfaces with the gray stack: #08090a → #141516 → #1c1c1f → #23252a → #2d2e31. Each level is exactly one step lighter.
- Use 1px hairline borders in #23252a or #34343a for all dividers, card edges, and input frames — never use drop shadows for separation.
- Reserve Berkeley Mono for inline code references and command examples only — it should appear sparingly as a technical accent.

### Don't

- Do not introduce chromatic brand colors, accent fills, or gradient CTAs — the 3% colorfulness is a discipline, not a limitation.
- Do not use 600/700 font weights for headings — Linear's typographic voice is weight 510/590, not bold.
- Do not apply drop shadows to cards or panels — use surface-level gray shifts instead. The only shadow is the 1px stroke pattern.
- Do not use filled buttons with solid backgrounds for primary actions — outlined pill buttons (1px #f7f8f8 border) are the only action style.
- Do not break the compact 4px base spacing rhythm with large gaps — section gaps stay at 48px, element gaps at 6–8px.
- Do not use rounded corners larger than 8px on cards or images — 4–5px and 8px are the only card radii; 9999px is pill-only.
- Do not use 600/700 bold for inline emphasis in body text — use weight 590 or rely on color shift to #f7f8f8 for highlight.

## Components

### Top Navigation Bar

Sticky header, full-bleed, background #08090a with 1px bottom border #23252a. Height ~56px. Logo (Linear mark + wordmark in #f7f8f8) left-aligned, nav links (Product, Resources, Customers, Pricing, Now, Contact) in #8a8f98 weight 510, right-aligned controls with vertical separator and ghost Login + outlined Sign Up pill.

### Outlined Pill Button

9999px radius. Border 1px solid #f7f8f8, background transparent, text #f7f8f8 at 14px weight 510, padding 8px 16px. No fill state, no shadow — confidence comes from the white outline against near-black. Used for 'Sign up' and key conversion actions.

### Ghost Text Button

No border, no background. Text at 14px weight 510, color #8a8f98. Hover state transitions text color to #f7f8f8. 8px horizontal padding. Used for 'Log in', top-nav links, and inline link buttons.

### Search Input

Dark surface #141516 with 1px border #23252a, radius 4px. Height ~32px, padding 8px 12px. Placeholder text 'Search...' in #8a8f98. Magnifying glass icon left-aligned in #8a8f98. No focus ring — just border color shift to #34343a.

### Section Tab Nav

Horizontal row below page title. Active tab ('Changelog') in #f7f8f8 weight 510, inactive tabs in #8a8f98. Tabs separated by 16px gap, no underline indicator. Sits at 14px, left-aligned.

### Date Marker

Small inline label with a 6px dot (chromatic accent, subtle orange/red #e4e5e9 or warm gray) and date text 'April 23, 2026' at 13px weight 400 in #8a8f98. Left-aligned to the entry, marks temporal grouping on the changelog timeline.

### Changelog Entry Heading

24px–32px Inter Variable weight 510, color #f7f8f8, letter-spacing -0.012em to -0.013em. Anchored to the left content column. Optional hash-anchor link icon (#8a8f98) appears on hover, positioned right of the text.

### App Connector Icon Grid

3-row grid of rounded squares (border-radius 8px, ~64px size), dark surface #1c1c1f with 1px border #23252a. Each tile holds a brand glyph in #f7f8f8. Subtle 1px inner stroke. Grids centered or left-aligned within content column, used to illustrate MCP connector ecosystem.

### Inline Product Reference List

Unordered list with 6–8px row gap, 4px left padding. Bullet character default #62666d. Body text at 15px weight 400, color #d0d6e0. Inline product names (e.g., 'Granolio', 'Glean', 'Notion', 'PostHog') bolded to weight 590 in #f7f8f8 — no underlines, no links, just typographic weight shift.

### Command Reference Card

Dark surface #1c1c1f with 1px border #23252a, radius 4px. Padding 12px 16px. Contains a small source label ('Granolio - create issues from my last meeting') in Berkeley Mono 15px, color #f7f8f8. Optional icon cluster on right (status dots, action buttons) in #8a8f98. Mimics a code comment or terminal snippet.

### Sub-section Divider Heading

20–24px Inter Variable weight 510, color #f7f8f8, with 16px top margin. Followed by a single-sentence preamble at 15px weight 400 in #d0d6e0. Used to break long changelog entries into scannable sub-sections.

### Body Paragraph

15–16px Inter Variable weight 400, line-height 1.5–1.6, color #d0d6e0. Max-width constrained to ~640px within content column. Links inline at weight 510 color #f7f8f8 with no underline (underline appears on hover).

### Hash Anchor Link

Small '#' icon at 16px, color #8a8f98, appears 12px to the right of headings on hover. Subtle, functional, not decorative.

## Similar Design Systems

- {'why': 'Same near-black canvas, monochrome palette, pill-shaped outlined CTAs, and hairline-border surface treatment with no drop shadows.', 'business': 'Vercel'}
- {'why': 'Dark-mode product UI with 9999px pill buttons, compact density, and Inter-based typography with custom weight steps.', 'business': 'Raycast'}
- {'why': 'Developer-tool aesthetic with stacked gray surfaces, minimal chromatic accent, and typographic discipline over decorative imagery.', 'business': 'Cursor'}
- {'why': 'Restrained dark UI with subtle surface elevation via gray shifts, though Notion uses more whitespace and less density.', 'business': 'Notion'}

## Agent Prompt Guide



**Quick Color Reference**
- Text primary: #f7f8f8
- Text secondary: #d0d6e0
- Text muted: #8a8f98
- Background: #08090a
- Border: #23252a
- primary action: no distinct CTA color

**Example Component Prompts**

1. *Changelog entry heading*: 32px Inter Variable weight 510, color #f7f8f8, letter-spacing -0.416px, left-aligned with 48px top margin. Hash anchor icon in #8a8f98 appears on hover.

2. *Outlined pill button*: 9999px radius, 1px solid #f7f8f8 border, transparent background, 14px Inter Variable weight 510 in #f7f8f8, padding 8px 16px. No fill, no shadow.

3. *App connector icon tile*: 64×64px, border-radius 8px, background #1c1c1f, 1px border #23252a, centered white brand glyph at 32px. Arranged in 3-row grid with 16px gap.

4. *Date marker*: 6px filled dot in warm accent color followed by 'April 23, 2026' at 13px weight 400 in #8a8f98, left-aligned to content column.

5. *Inline product reference list*: Bulleted list with 8px row gap, 15px Inter Variable weight 400 in #d0d6e0, inline product names bolded to weight 590 in #f7f8f8 (no underline).



## Typographic Voice

Linear's typography is its loudest signal. The use of Inter Variable with custom half-step weights (510 for headings, 590 for emphasis) avoids the generic 400/600/700 triad that dominates SaaS. The result: headings feel precise rather than bold, emphasis feels intentional rather than heavy. Negative letter-spacing tightens the rhythm at every size — -0.010em for body, -0.022em for display 48px. Font features 'cv01' (curved alternates) and 'ss03' (stylistic set 3) further differentiate the typeface from stock Inter. Berkeley Mono appears only in code-adjacent contexts, acting as a technical whisper rather than a stylistic flourish.
