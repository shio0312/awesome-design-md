# Henry — Design System

> **North Star**: Gothic broadside poster on warm cream paper. One hundred percent monochrome, no chromatic accent, all visual intensity carried by display type and full-bleed paper-to-ink inversions.
> **Theme**: mixed
> **Source**: https://henry.codes
> **Refero Style**: https://styles.refero.design/style/ff4b9eff-dc0b-4886-bd65-c2f5e9069318
> **Synced**: 2026-09-01

## Overview

Henry Codes reads like an editorial broadside printed in warm ink: near-black headlines carved into cream paper, alternating with full-bleed dark sections where cream serif type glows. The palette is one-hundred-percent warm monochrome — no chromatic accent, no product color, no blue link — every visual move comes from scale, weight, and inversion. Type is the brand: a display serif (Louize) sets poetry and editorial prose, a condensed display sans (Manuka) stamps section headers at 200–370px, and a neo-grotesque (Neue Montreal) carries all UI at 12–24px. The spacing system is austere: 4–32px increments, one radius (12px), no shadows. Sections flip between paper and ink like a broadsheet newspaper, and most screens should be dominated by two or three enormous words rather than illustrated product art.

## Color Palette

- **Paper**: `#fafafa` — Page background, card surfaces, inverted-section type — the cream-white ground that all dark type sits on [neutral]
- **Hairline**: `#eeeeee` — Card and tile borders — only visible against Paper [neutral]
- **Midstone**: `#9f9f9f` — Nav borders, muted borders, light decorative borders on dark sections [neutral]
- **Ash**: `#666666` — Secondary borders, muted UI text, low-emphasis dividers [neutral]
- **Pebble**: `#b3b3b3` — Inactive nav text and borders [neutral]
- **Sepia**: `#3e3b36` — Strong borders, secondary heading text — the warm-brown near-black that flanks Headline Ink [neutral]
- **Headline Ink**: `#2a2722` — Primary text, body ink, dominant borders, nav rules — warm near-black that carries every word on the page [neutral]

## Typography

- **Neue Montreal**
- **Louize Display**
- **Louize**
- **Manuka**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.3 |
| heading-sm | 24 | — | 1.2 |
| heading | 32 | — | 1.1 |
| heading-lg | 77 | — | 0.9 |
| display | 132 | — | 0.8 |
| display-xl | 371 | — | 0.75 |

## Spacing & Layout

- **Card Padding**: 16px
- **Element Gap**: 16px
- **Section Gap**: 64-96px
- **Border Radius**: {'tags': '12px', 'cards': '12px', 'buttons': '12px'}

## Layout

Layout is full-bleed editorial — no max-width container, no sidebar, no card grid in the traditional sense. The page stacks as a sequence of horizontally-bleed sections that alternate Paper and Ink bands. The hero is a split composition: oversized Louize Display headline occupies the left two-thirds with no padding constraint, and a square halftone illustration block anchors the right third. Subsequent sections are centered single-column editorial blocks (the inverted letter) or horizontally-tickered marquee bands. Navigation is a minimal top-left list of uppercase items with no background bar. The page model is zine/broadsheet, not SaaS dashboard: vertical rhythm is loose (64–96px between sections) but each section is internally dense with type. No grids of feature cards, no pricing tables, no comparison blocks — content is delivered as long-form editorial prose and a single works ticker.

## Surfaces / Elevation

- **Paper**
- **Ink**

## Imagery

Imagery is treated as monochrome halftone illustration only — no photography, no product screenshots, no gradients, no color images. The hero uses a square right-side plate showing a black butterfly/moth creature in halftone dots against the cream paper. All imagery is high-contrast black-on-white or white-on-black, sharp square corners, no rounded masks, no overlap with type. Illustrations function as typographic counterweights inside a paper/ink composition rather than as standalone visuals. Iconography is absent from the interface — no system icons, no nav icons, no UI pictograms. Social proof and client logos are rendered as Louize Display wordmarks inside a dark ticker band rather than as image files.

## Design Principles

### Do

- Use Louize Display at 77px+ for any section-defining headline; below that, the editorial feel collapses into generic web type
- Set body and UI type in Neue Montreal at 12/16/20/24/32px with -0.01em letter-spacing — never let body text breathe wider than 1.5 line-height
- Alternate Paper (#fafafa) and Ink (#2a2722) sections as full-bleed bands; never gradient-blend between them, never place a card that crosses the boundary
- Use 12px as the only border-radius across cards, buttons, and tags — no square corners, no pill shapes (no 9999px)
- Carry all display typography in #2a2722 on Paper or #fafafa on Ink — no third surface color, no shadowed cards, no tinted panels
- Use Manuka only for the largest section mastheads (226–371px) and always in one weight, one case, one color — the type does the work alone
- Let 90% of any page be empty Paper or Ink; dense regions are limited to the brand ticker and the bottom-byline

### Don't

- Never introduce a chromatic accent color — the system is one-hundred-percent warm monochrome, and any blue/red/green breaks the broadside identity
- Never use a filled colored CTA button — the role evidence shows zero action backgrounds; emphasis comes from scale and inversion, not fill
- Never apply box-shadow, drop-shadow, or glow — there are no detected shadows and adding them turns the editorial print feel into generic SaaS card UI
- Never set body copy in Louize Display at 116–132px; the display serif is for headlines only and becomes illegible below 32px on long passages
- Never use a border-radius other than 12px; no sharp 0px, no pills, no asymmetric rounding
- Never break the Paper/Ink binary with a gray panel, a muted surface, or a tinted hero gradient — those don't exist in the token set
- Never center-align body copy in Neue Montreal; only Louize Display/Louize editorial blocks use center alignment, and only inside Ink sections

## Components

### Masthead Display Headline

Louize Display at 116–132px, weight 400, line-height 0.8, color #2a2722 on Paper or #fafafa on Ink. Sometimes intersected with an italic Louize Display phrase at half size set inside the same baseline (e.g. 'of the' italic at 35px set within 'TRUE TERRORS / NEW DARK WEB' at 132px). No tracking, no all-caps, relies on the serif contrast for presence.

### Stamped Display Section Header

Manuka at 226–371px, weight 400, line-height 0.75, uppercase, color #fafafa on #2a2722. Stretches edge-to-edge with a trailing em-dash or rule. Single-weight, single-color — the slab of condensed type is the entire section identity.

### Top Ticker Banner

Neue Montreal 12px, weight 400, letter-spacing -0.12px, color #2a2722, set in uppercase on Paper. Optional horizontal hairline dividers in #2a2722 at 1px above and below. Padding 4–6px vertical, full-bleed.

### Inverted Editorial Letter

Background #2a2722, padding 48–64px vertical, full-bleed. Body text in Louize Display at 32px, weight 400, line-height 1.2, color #fafafa, text-align center. Optional small-caps eyebrow at top and bottom ('A BRIEF LETTER FROM THE EDITOR', 'A LETTER FROM THE WORK DESK') in Neue Montreal 12px, weight 400, letter-spacing -0.12px, color #fafafa, opacity 0.6.

### Nav Link (Uppercase)

Neue Montreal 12–16px, weight 700, uppercase, color #2a2722, letter-spacing -0.12px. No underline, no background. Active state shares the same color but is set in a larger size (16–20px) — emphasis comes from scale, not color or weight shift.

### Section Divider Rule

1px solid #2a2722, full-bleed width, no margin. Used as a typographic break, never decorative.

### Brand Ticker Strip

Full-bleed dark band (#2a2722). Brand names in Louize Display at 24–32px, weight 400, color #fafafa, repeated horizontally with tight gap. Interleaved with a small 'COMING SOON' tag (Neue Montreal 12px, weight 400, uppercase, #fafafa, 12px radius, 4px 8px padding, 1px border #fafafa).

### Coming Soon Tag

Neue Montreal 12px, weight 400, uppercase, color #fafafa, 1px solid #fafafa border, 12px radius, padding 4px 8px. No background fill — outlined ghost variant only.

### Coordinate Footer

Neue Montreal 12px, weight 400, letter-spacing -0.12px, color #2a2722, single-line format '° 43°31'56" N 104° 58' 0.94" (DENVER, COLORADO) — 11:27 PM — ● 48°9 @ N 39°43'31'56" W 104°58' 0.94" (DENVER, COLOR...'. Uppercase with em-dash separators.

### Hero Halftone Plate

Full-height image area (~60% of hero width), no border-radius (square corners), monochrome halftone illustration in Headline Ink on Paper. Functions as typographic counterweight to the display headline — no caption, no label.

### Footnotes / Meta Line

Neue Montreal 12px, weight 400, uppercase, letter-spacing -0.12px, color #2a2722. Used for 'READ THE CASE STUDY ON GODCOMMON.COM'-style attribution lines.

## Similar Design Systems

- {'why': 'Same editorial-broadsheet approach: display serif headlines, paper-white canvas, zero chromatic accent, type as the only visual asset', 'business': 'Pentagram'}
- {'why': 'Same condensed display sans (Druk/Manuka-family) stamped at near-architectural scale for section mastheads, same warm-paper monochrome palette', 'business': 'Manual (manualcreative.com)'}
- {'why': 'Same oversized display-serif hero with italic inline subhead treatment, same full-bleed alternating light/dark editorial bands', 'business': 'Locomotive (locomotive.ca)'}
- {'why': 'Same print-magazine metaphor: cream paper, warm near-black ink, serif display for headlines, no shadows, one radius (12px), zero color accent', 'business': 'Cereal magazine'}
- {'why': 'Same brutalist personal-portfolio instinct: type-only hero, monochrome palette, no CTAs, no product art, the design IS the work', 'business': 'Rauno Freiberg'}

## Agent Prompt Guide

Quick Color Reference:
- text: #2a2722 (Headline Ink) on #fafafa (Paper)
- background: #fafafa (Paper) for default, #2a2722 (Ink) for inverted sections
- border: #2a2722 for strong rules, #9f9f9f for muted, #eeeeee for hairline on cards
- accent: none (system is fully monochrome)
- primary action: no distinct CTA color

3-5 Example Component Prompts:
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
2. Create an inverted editorial section: full-bleed #2a2722 background, padding 64px vertical. Eyebrow 'A BRIEF LETTER FROM THE EDITOR' in Neue Montreal 12px weight 400 uppercase letter-spacing -0.12px color #fafafa centered at top. Body in Louize Display 32px weight 400 line-height 1.2 color #fafafa text-align center, 3–5 short lines. Mirror eyebrow at bottom.
3. Create a stamped section header: full-bleed #2a2722 background, padding 48px vertical. Single line 'SELECTED WORKS' in Manuka 226px weight 400 line-height 0.75 color #fafafa uppercase, with a trailing horizontal white rule extending to the right edge.
4. Create a brand ticker band: full-bleed #2a2722 background, no padding. Louize Display 24px weight 400 color #fafafa brand names ('Stripe', 'YouTube', 'The New York Times', 'Matter', 'Uber Eats x Taco Bell') repeated horizontally at 32px gap, one row. Overlay a 'COMING SOON' ghost tag (Neue Montreal 12px weight 400 uppercase, 1px solid #fafafa border, 12px radius, 4px 8px padding) on selected entries.
5. Create a top nav: Paper (#fafafa) background, no bar. Left-aligned vertical list of Neue Montreal 12px weight 700 uppercase items in #2a2722, 12px row gap. Active item rendered larger (16px) but same color/weight. No underline, no background highlight.
