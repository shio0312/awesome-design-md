# Scheduling — Design System

> **North Star**: Editorial ink on cream paper
> **Theme**: light
> **Source**: https://glossgenius.com
> **Refero Style**: https://styles.refero.design/style/7ad5549e-9baa-4fda-ac43-79d568a86b98
> **Synced**: 2026-09-01

## Overview

GlossGenius operates in a near-monochrome editorial register: a warm-black ink (#17150e) stamped onto white and a faint mint-cream (#f0f7f6) canvas, with a single chartreuse-yellow (#cccc25) that functions like a highlighter pen — appearing sparingly on primary CTAs, metric callouts, and decorative washes. The typography is the brand's loudest element: a custom Basel pairing where the grotesque Grotesk handles UI and body while Classic — a sharper, slightly serifed display face — drops in only at 96–144px for editorial statements, tightened to 0.8–0.95 line-height so letterforms stack like vinyl. Components are deliberately lightweight: flat 8px-radius cards, no shadows, pill-shaped buttons at 1440px, and 1.5px hairline dividers. Sections breathe generously (80–120px gaps) and alternate between pure white and the mint tint, creating the cadence of a magazine spread rather than a product dashboard.

## Color Palette

- **Gloss Black**: `#17150e` — Primary text, dark card surfaces, footer background, pill button fill — a warm near-black that reads softer than pure #000 and makes the large display type feel printed rather than digital; 1.5px borders and dividers — uses the same warm-black as text to keep all structural lines tonally unified [brand]
- **Gloss White**: `#f0f7f6` — Page tint sections, card surfaces, badge fills, button text on dark — a barely-green-tinted off-white that warms the interface and creates gentle contrast bands against pure white [neutral]
- **Pure White**: `#ffffff` — Primary page canvas, card surface, dark-button text, nav link color — used wherever maximum contrast is needed without any color temperature [neutral]
- **Solar Yellow**: `#cccc25` — Yellow action color for filled buttons, selected navigation states, and focused conversion moments; Soft yellow-to-pale-yellow gradient used as decorative wash behind hero copy and section transitions [brand]
- **Soft Charcoal**: `#272b30` — Secondary dark surface, deep section backgrounds — cooler alternative to Gloss Black for variant cards and panels [neutral]
- **Mid Grey**: `#949494` — Muted helper text, secondary labels — reserved for non-essential copy where readability is still required [neutral]
- **Light Coral**: `#ff7780` — Accent tint for decorative illustrations and marketing gradient washes — never used for UI states [accent]
- **Apricot**: `#ffe5d6` — Soft accent fill for illustration blocks and feature card backgrounds in the marketing surface [accent]
- **Apricot Glow**: `#ffb36a` — Warm illustration accent — pairs with Light Coral in editorial gradient compositions [accent]
- **Lavender Mist**: `#c0c8f6` — Cool illustration accent balancing the warm Coral/Apricot pair in product showcase gradients [accent]
- **Periwinkle Fade**: `#9fa6ff` — Periwinkle-to-lavender gradient used in product feature illustrations and decorative dividers [accent]

## Typography

- **Basel Grotesk Book**
- **Basel Classic Book**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 14 | — | 1.4 |
| body | 16 | — | 1.5 |
| subheading | 22 | — | 1.2 |
| heading-sm | 32 | — | 1.1 |
| heading | 40 | — | 1 |
| heading-lg | 72 | — | 0.97 |
| display | 96 | — | 0.95 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 16px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '8px', 'badges': '8px', 'inputs': '12px', 'buttons': '1440px', 'containers': '24px', 'largeCards': '16px'}

## Layout

Max-width 1200px centered content frame, with full-bleed sections (photo hero, dark cards, gradient washes) breaking out to viewport edges. The page model is a vertical stack of sections that alternate between white and mint-tint backgrounds, creating the cadence of a printed spread. The hero is a full-bleed dark photograph with left-aligned white headline overlay (not centered) and a single yellow CTA + ghost button stack positioned in the lower-left. Feature sections use a two-column pattern: large left-aligned heading with a 3-column card grid or single product mockup on the right. The stats band is a 3-column horizontal grid on a mint background with oversized numbers dominating. Navigation is a minimal top bar — text links left, three-button cluster right (ghost login, ghost demo, dark pill start trial) — with no sticky behavior on the hero. Section gaps are 80–120px, generous enough to feel editorial rather than dense.

## Surfaces / Elevation

- **Canvas**
- **Tint**
- **Ink**
- **Highlight**

**Shadow tokens:**

## Imagery

Imagery alternates between two modes: editorial photography and product screenshot capture. The hero is a full-bleed documentary-style photograph of people working at a salon (warm, slightly desaturated, natural lighting, no staged poses) overlaid with white headline type — the photo sets lifestyle context without dominating. Product visuals are tight screen captures of the actual interface (calendar, analytics dashboard, payment flow) presented inside mint-tinted cards with no device frames or mockup chrome. Decorative gradient washes (yellow, periwinkle, green-fade) appear as full-bleed section backgrounds to break the rhythm between content blocks. Icons are minimal — mostly line-weight UI icons in product screenshots rather than illustrative iconography. No 3D renders, no abstract geometric art, no stock photography in feature sections.

## Design Principles

### Do

- Use Basel Classic Book only at 96px+; reserve it for the single biggest statement on a page
- Set all heading line-height to 1.0 or below; the tight stacking is signature and not optional
- Apply -0.03em letter-spacing on any text 40px or larger; 0 tracking at body sizes
- Alternate section backgrounds between #ffffff and #f0f7f6 to create the magazine-spread cadence
- Use #cccc25 (Solar Yellow) for exactly one element per view — hero CTA, a single stat chip, or a gradient wash — never as a general accent
- Set border-radius to 1440px on every button and 8px on every standard card; mixing the two within a component family breaks the system
- Use 1.5px borders (not 1px) for all dividers and ghost elements — the slightly heavier line reads as intentional ink rather than CSS default

### Don't

- Don't introduce drop shadows on standard cards; the system is flat by design and shadows undermine the editorial feel
- Don't use #000000 for text or fills — always warm it to #17150 to preserve the printed-ink quality
- Don't pair Basel Classic with anything below 96px; the contrast in voice collapses at smaller sizes
- Don't place yellow buttons on yellow gradient backgrounds — the CTA loses all emphasis
- Don't add a third display weight (e.g. 600) to either font; the system only uses 400 and 500
- Don't use the decorative illustration colors (Coral, Apricot, Lavender) for UI states, text, or borders — they are gradient art only
- Don't add hover shadows to buttons; use background-color or border-color transitions exclusively

## Components

### Primary Pill Button (Dark)

1440px border-radius (full pill), 12px 24px padding, #17150 fill, #f0f7f6 text, Basel Grotesk 16px weight 500. No border, no shadow. Sits as the rightmost header action on white backgrounds.

### Primary Pill Button (Yellow Accent)

1440px radius, 12px 24px padding, #cccc25 fill, #17150 text, Basel Grotesk 16px weight 500. Used sparingly — appears once per page max, in the hero overlay.

### Ghost Outline Button

1440px radius, 12px 24px padding, transparent fill, 1.5px solid #ffffff border, #ffffff text. Used on the dark hero photo overlay for the secondary 'Start free trial' action.

### Text Nav Link

No background, #17150 text, Basel Grotesk 16px weight 500, 8px horizontal padding, no underline. Hover transitions color only.

### Feature Card (Mint)

#f0f7f6 fill, 8px radius, 16px–24px padding, no shadow, no border. Contains inline product mockup imagery at 100% width with no additional chrome.

### Dark Feature Card

#17150 fill, 16px radius, generous padding (32–48px), white/mint text, no shadow. Creates a visual pause between lighter sections.

### Stat Block

No card chrome. Display number in Basel Classic 96–144px weight 400, #17150, line-height 0.8–0.95, letter-spacing -0.03em. Small superscript '+' in the same style. Caption beneath in Basel Grotesk 16px weight 500, #17150e.

### Filled Badge

#f0f7f6 fill, #17150 text, 8px radius, 12px padding, Basel Grotesk 16px weight 500. Inline with adjacent content.

### Ghost Badge

Transparent fill, 1.5px solid #17150 border, #17150 text, 8px radius, 12px padding, Basel Grotesk 16px weight 500. Optionally with 0.063em letter-spacing for label variation.

### Carousel Arrow Control

40×40px square, 1.5px solid #17150 border, no fill, 8px radius, #17150 arrow icon. Sits flush-right of section heading.

### Announcement Bar

Full-width, #17150 fill, #f0f7f6 text, 12px vertical padding, Basel Grotesk 14px weight 500. Contains a single text link with optional chevron.

### Chat Widget

56px circle, #17150 fill, white chat icon, bottom-right fixed position. Subtle drop shadow to lift from page content.

### Metric Chip (Yellow)

#cccc25 fill, #17150 text, 8px radius, 8px 12px padding, Basel Grotesk 14px weight 500. Appears inside the product screenshot to mark actionable items.

## Similar Design Systems

- {'why': 'Same editorial-magazine approach to product UI: oversized display typography, near-monochrome palette with a single saturated accent, flat surfaces with no shadows, and tight letter-spacing on large sizes', 'business': 'Linear'}
- {'why': 'Shares the warm-near-black text (#17150 territory) against white, custom display serif/sans pairing, and confidence to let photography and typography do all the work without chrome', 'business': 'Arc Browser'}
- {'why': 'Same publisher-spread sensibility: large editorial headlines, tight line-heights, minimal UI chrome, and a restrained palette that treats the page as a reading surface', 'business': 'Substack'}
- {'why': 'Pill-shaped buttons at extreme border-radius, gentle alternating surface tints, and flat card system with no shadows — though GlossGenius is far more typographically assertive', 'business': 'Notion'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #17150e (warm near-black)
- background: #ffffff (canvas) / #f0f7f6 (tint sections)
- border: 1.5px solid #17150e
- accent: #cccc25 (Solar Yellow) — charts, metric chips, gradient washes
- card surface: #f0f7f6 with 8px radius, no shadow
- primary action: no distinct CTA color

**Example Component Prompts**
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. **Stat band**: Mint #f0f7f6 section background, 80px vertical padding. Three columns. Each column: display number at 96px Basel Classic weight 400, #17150e, line-height 0.95, letter-spacing -2.88px, with a superscript '+' in the same style. Caption beneath in Basel Grotesk 16px weight 500, #17150e.

3. **Feature card with product mockup**: White section background. Card: #f0f7f6 fill, 8px radius, 24px padding, no shadow, no border. Contains a product screenshot filling 100% card width with 8px radius clip. Heading above card at 40px Basel Classic weight 400, #17150e.

4. **Ghost badge / eyebrow label**: Transparent fill, 1.5px solid #17150e border, 8px radius, 12px padding. Text in Basel Grotesk 16px weight 500, #17150e, letter-spacing 0.063em, uppercase optional.

5. **Carousel navigation**: Two 40×40px square buttons flush-right of section heading. Transparent fill, 1.5px solid #17150e border, 8px radius, #17150e arrow glyph centered. Gap of 4px between arrows.

## Editorial Cadence

The system's defining structural choice is the alternation of #ffffff and #f0f7f6 between sections — never two mint sections adjacent, never two white sections adjacent. This two-tone rhythm does the work that shadows, dividers, or vertical lines would do in a conventional product UI. When designing a new page, sketch the section backgrounds first as a binary pattern before placing any content. Dark (#17150e) sections should appear no more than once per full page scroll-depth and only for emphasis — the announcement bar, the footer, or a single dark feature card.

## Yellow Restraint

Solar Yellow (#cccc25) is rationed. It appears as: (1) exactly one filled pill button in the hero, (2) inline metric chips inside product UI screenshots, (3) full-bleed gradient washes as section transitions, and (4) superscript '+' marks beside stat numbers. It should never appear as a link color, never as a heading color, never on a dark background, and never more than twice in a single viewport. The discipline is what makes it read as 'switched on' rather than decorative.
