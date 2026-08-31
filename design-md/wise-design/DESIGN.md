# Wise Design — Design System

> **North Star**: Neon market stall on a global street — electric lime signage that shouts across a crowded marketplace, then polished product UI slips in behind it.
> **Theme**: mixed
> **Source**: https://wise.design
> **Refero Style**: https://styles.refero.design/style/c5326639-873a-4257-ad1a-7da9111e9286
> **Synced**: 2026-09-01

## Overview

Wise Design hits like a silk-screened protest poster — electric lime green (#87ea5c) floods the hero at full saturation, then dark forest ink (#083400) type slams across it at display scale. The palette is deliberately non-fintech: vivid yellow (#ffea4b), peach (#ffbd89), cotton candy pink (#ffd5f0), and deep aubergine (#2a0831) coexist like a global currency collection. Wise Sans at weight 900 with 0.85 line-height is the signature — letterforms stack so tightly they almost collide, creating billboard compression at digital scale. Pills (9999px radius) are the only rounded UI element, while large content blocks use generous 86px radii creating soft-edged cards that contrast the aggressive type. The design system oscillates between screaming and whispering — massive stacked display type then a single quiet midsize line on white.

## Color Palette

- **Lime Volt**: `#87ea5c` — Hero backgrounds, pill button fill, category tag backgrounds — the single most identifiable brand signal; vivid green against dark ink creates energy no fintech blue could achieve [brand]
- **Forest Ink**: `#083400` — Primary text, dark headlines on lime, nav links, icon fills — deep forest green instead of black keeps everything on-brand even at body size [brand]
- **Volt Yellow**: `#ffea4b` — Accent headlines, decorative text color on dark backgrounds — electric yellow that pairs with deep burgundy for maximum punch [accent]
- **Papaya**: `#ffbd89` — Warm accent card backgrounds, decorative section highlights [accent]
- **Cotton Candy**: `#ffd5f0` — Soft accent backgrounds, section highlights in the mosaic grid [accent]
- **Aubergine Night**: `#2a0831` — Dark card backgrounds, high-contrast panels in the content grid — deep purple-black that isn't neutral [accent]
- **Crimson Depth**: `#370305` — Dark editorial backgrounds, heading color on light panels — near-black red that reads as richly dark without being neutral [accent]
- **Fog**: `#58717a` — Secondary body text, border colors, UI chrome [neutral]
- **White**: `#ffffff` — Page backgrounds, card surfaces, section backgrounds between color blocks [neutral]
- **Positive**: `#008026` — Success states, positive transaction indicators [semantic]
- **Negative**: `#cf2929` — Error states, negative transaction indicators [semantic]
- **Accent Blue**: `#0097c7` — Interactive accent links, focus states [semantic]
- **Warning**: `#9a6500` — Warning states, attention-needed transaction labels [semantic]

## Typography

- **Inter**
- **Wise Sans**
- **Zen Kaku Gothic New**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| body-sm | 16 | — | 1.5 |
| body | 18 | — | 1.44 |
| subheading | 22 | — | 1.25 |
| heading-sm | 25 | — | 1.25 |
| heading | 45 | — | 1.17 |
| heading-lg | 58 | — | 1.03 |
| display | 72 | — | 1 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 24px
- **Element Gap**: 12px
- **Section Gap**: 80-120px
- **Border Radius**: {'body': '1440px', 'tags': '9999px', 'cards': '86px', 'buttons': '9999px', 'contentBlocks': '86px'}

## Layout

Full-bleed sections with no max-width constraint on hero and color blocks; content sections use ~1152-1440px max-width centered. Hero is full-viewport lime green with Wise Sans stacked display type, no image — the type IS the visual. Navigation merges seamlessly with hero background (same #87ea5c), creating a single unbroken color field from top of page through hero. Section rhythm alternates: massive color hero → white editorial pause → full-bleed photography → mosaic card grid → white section → dark panel → repeat. No decorative dividers — color is the divider. The mosaic grid uses 3-column irregular tile layout where tiles vary in height and background color, creating a collage effect. Individual content sections use centered single-column for editorial statements and 2-column for feature explanations. Spacious vertical breathing room (80-120px) between major sections ensures each color block reads as a distinct visual beat.

## Imagery

Three distinct visual modes coexist in the system. First: full-bleed real-world photography (street scenes with flags, city imagery) used full-width with no border-radius — raw, unmasked, documentary in feel, treated as atmospheric section dividers rather than product illustration. Second: product UI screenshots (transaction cards, app interfaces) contained within 86px-radius white cards, floating against colored backgrounds — the UI is the product showcase. Third: a mosaic of color-block tiles containing flags (circular crop), paper airplane illustrations, currency symbols, and illustrated characters — these are flat, graphic, brand-colored, and decorative. Icons visible in transaction UI are outlined stroke-style at ~1.5px weight, monochrome #083400. The overall density is image-heavy in the mosaic zones but text-dominant in editorial sections — the system alternates between visual feast and typographic silence.

## Design Principles

### Do

- Use Wise Sans weight 900 with lineHeight 0.85 for all hero display text — lines must stack tightly, almost touching, at 288px minimum
- Fill entire hero and nav sections with #87ea5c — the lime is a background, not a highlight; it should dominate, not accent
- Pair #083400 (Forest Ink) as the primary text color on lime and white backgrounds — never use pure black (#000000) anywhere in the system
- Assign 86px border-radius to content cards and mosaic tiles; reserve 9999px exclusively for pill buttons and tags
- Use the full accent palette (#ffea4b, #ffbd89, #ffd5f0, #2a0831, #370305) as full-bleed card backgrounds — each color is a distinct 'room', not a subtle tint
- Apply Inter font-feature-settings: "calt", "ss01" — the ss01 variant alternates specific letterforms that are part of the typographic identity
- Maintain negative letter-spacing on Inter at all display sizes: -2.16px at 72px, scaling to -0.08px at 16px

### Don't

- Never use #87ea5c as a small accent detail — it must be used at large scale (full backgrounds, full buttons) or not at all
- Do not use weight 700 for body text — Inter weights are strictly 400 (body) and 600 (labels/subheadings)
- Never apply drop shadows or elevation effects — the system uses color contrast and scale for hierarchy, not shadow depth
- Do not use rectangular (0px radius) cards — content blocks must use either 86px radius or 9999px pill; sharp corners are absent from the system
- Never use conventional fintech blue as a primary brand color — #0097c7 exists only for semantic accent links and focus states, never as primary CTA or brand expression
- Do not place Wise Sans at sizes below 187px — it is a display-only typeface; Inter handles all UI and body text
- Never mix multiple chromatic background colors in a single section — each panel is monochromatic, switching color only at full section breaks

## Components

### Category Navigation Pills

```html
<style>
  :root {
    --color-lime-volt: #87ea5c;
    --color-forest-ink: #083400;
    --color-volt-yellow: #ffea4b;
    --color-papaya: #ffbd89;
    --color-cotton-candy: #ffd5f0;
    --color-aubergine-night: #2a0831;
    --color-white: #ffffff;
    --color-fog: #58717a;
    --font-inter: 'Inter', system-ui, -apple-system, sans-serif;
  }
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
</style>
<div style="background: var(--color-lime-volt); padding: 48px 40px; font-family: var(--font-inter); display: flex; flex-direction: column; gap: 32px; border-radius: 86px; max-width: 560px; margin: 0 auto; box-sizing: border-box;">
  <p style="font-family: var(--font-inter); font-size: 16px; font-weight: 400; color: var(--color-forest-ink); letter-spacing: -0.08px; margin: 0; line-height: 1.5;">Explore the design system</p>
  <div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <a href="#" style="display: inline-flex; align-items: center; background: var(--color-forest-ink); color: var(--color-lime-volt); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; text-decoration: none; line-height: 1;">Design at Wise</a>
    <a href="#" style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; text-decoration: none; line-height: 1;">Foundations</a>
    <a href="#" style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; text-decoration: none; line-height: 1;">Components</a>
    <a href="#" style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; text-decoration: none; line-height: 1;">Patterns</a>
    <a href="#" style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; text-decoration: none; line-height: 1;">Resources</a>
  </div>
  <div style="display: flex; flex-wrap: wrap; gap: 10px; padding-top: 8px; border-top: 1px solid rgba(8,52,0,0.18);">
    <span style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; line-height: 1; border: 1.5px solid rgba(8,52,0,0.25);">Flags</span>
    <span style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; line-height: 1; border: 1.5px solid rgba(8,52,0,0.25);">Components</span>
    <span style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; line-height: 1; border: 1.5px solid rgba(8,52,0,0.25);">Tone of voice</span>
    <span style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; line-height: 1; border: 1.5px solid rgba(8,52,0,0.25);">Typography</span>
    <span style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; line-height: 1; border: 1.5px solid rgba(8,52,0,0.25);">Colour</span>
  </div>
</div>
```

### Transaction Card (Product UI)

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
  :root {
    --color-lime-volt: #87ea5c;
    --color-forest-ink: #083400;
    --color-white: #ffffff;
    --color-fog: #58717a;
    --color-positive: #008026;
    --color-warning: #9a6500;
    --color-accent-blue: #0097c7;
    --font-inter: 'Inter', system-ui, -apple-system, sans-serif;
  }
</style>
<div style="background: #f2f2ee; padding: 32px; border-radius: 86px; max-width: 560px; margin: 0 auto; box-sizing: border-box; font-family: var(--font-inter);">
  <div style="background: var(--color-white); border-radius: 24px; padding: 24px; box-sizing: border-box;">
    <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 16px; border-bottom: 1px solid rgba(88,113,122,0.18); margin-bottom: 4px;">
      <span style="font-family: var(--font-inter); font-size: 16px; font-weight: 400; color: var(--color-fog); letter-spacing: -0.08px;">Transactions</span>
      <a href="#" style="font-family: var(--font-inter); font-size: 16px; font-weight: 600; color: var(--color-positive); letter-spacing: -0.08px; text-decoration: underline;">See all</a>
    </div>
    <div style="display: flex; align-items: center; gap: 16px; padding: 16px 0; border-bottom: 1px solid rgba(88,113,122,0.12);">
      <div style="width: 44px; height: 44px; border-radius: 9999px; background: var(--color-lime-volt); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#083400" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 013 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
      </div>
      <div style="flex: 1;">
        <div style="font-family: var(--font-inter); font-size: 16px; font-weight: 600; color: var(--color-forest-ink); letter-spacing: -0.08px; line-height: 1.4;">Sophie Beck</div>
        <div style="font-family: var(--font-inter); font-size: 14px; font-weight: 400; color: var(--color-warning); letter-spacing: -0.06px; line-height: 1.4; margin-top: 2px;">Needs attention</div>
      </div>
      <div style="font-family: var(--font-inter); font-size: 16px; font-weight: 600; color: var(--color-forest-ink); letter-spacing: -0.08px; white-space: nowrap;">102.32 GBP</div>
    </div>
    <div style="display: flex; align-items: center; gap: 16px; padding: 16px 0;">
      <div style="width: 44px; height: 44px; border-radius: 9999px; background: #f2f2ee; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#083400" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
      </div>
      <div style="flex: 1;">
        <div style="font-family: var(--font-inter); font-size: 16px; font-weight: 600; color: var(--color-forest-ink); letter-spacing: -0.08px; line-height: 1.4;">Sainsbury's</div>
        <div style="font-family: var(--font-inter); font-size: 14px; font-weight: 400; color: var(--color-fog); letter-spacing: -0.06px; line-height: 1.4; margin-top: 2px;">Spent · Tue</div>
      </div>
      <div style="font-family: var(--font-inter); font-size: 16px; font-weight: 600; color: var(--color-forest-ink); letter-spacing: -0.08px; white-space: nowrap;">8.90 GBP</div>
    </div>
  </div>
  <div style="margin-top: 20px; display: flex; justify-content: flex-start;">
    <span style="display: inline-flex; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 11px 24px; font-family: var(--font-inter); font-size: 16px; font-weight: 400; letter-spacing: -0.08px; line-height: 1;">Components</span>
  </div>
</div>
```

### Mosaic Design System Cards

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
  :root {
    --color-lime-volt: #87ea5c;
    --color-forest-ink: #083400;
    --color-volt-yellow: #ffea4b;
    --color-papaya: #ffbd89;
    --color-cotton-candy: #ffd5f0;
    --color-aubergine-night: #2a0831;
    --color-crimson-depth: #370305;
    --color-white: #ffffff;
    --font-inter: 'Inter', system-ui, -apple-system, sans-serif;
  }
</style>
<div style="max-width: 600px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: auto auto; gap: 12px; padding: 16px; box-sizing: border-box; background: var(--color-white); font-family: var(--font-inter);">

  <!-- Lime type card -->
  <div style="background: var(--color-forest-ink); border-radius: 52px; padding: 32px 28px; display: flex; flex-direction: column; justify-content: space-between; min-height: 200px; overflow: hidden; position: relative;">
    <div style="font-family: 'Inter', system-ui, sans-serif; font-size: 72px; font-weight: 900; color: var(--color-lime-volt); line-height: 0.85; letter-spacing: -2px; font-feature-settings: 'ss01','calt'; user-select: none;">WISE<br>SANS</div>
    <span style="display: inline-flex; align-self: flex-start; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 8px 18px; font-family: var(--font-inter); font-size: 13px; font-weight: 400; letter-spacing: -0.06px; line-height: 1; margin-top: 24px;">Typography</span>
  </div>

  <!-- Cotton candy card with editorial text -->
  <div style="background: var(--color-cotton-candy); border-radius: 52px; padding: 32px 28px; display: flex; flex-direction: column; justify-content: space-between; min-height: 200px;">
    <div style="font-family: var(--font-inter); font-size: 32px; font-weight: 600; color: var(--color-crimson-depth); line-height: 1.1; letter-spacing: -0.5px;">Tone<br>of voice</div>
    <span style="display: inline-flex; align-self: flex-start; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 8px 18px; font-family: var(--font-inter); font-size: 13px; font-weight: 400; letter-spacing: -0.06px; line-height: 1; margin-top: 24px;">Tone of voice</span>
  </div>

  <!-- Lime card with stats -->
  <div style="background: var(--color-lime-volt); border-radius: 52px; padding: 32px 28px; display: flex; flex-direction: column; justify-content: space-between; min-height: 180px;">
    <div>
      <div style="font-family: var(--font-inter); font-size: 13px; font-weight: 400; color: var(--color-forest-ink); opacity: 0.7; letter-spacing: -0.06px; margin-bottom: 8px;">Design system sections</div>
      <div style="font-family: var(--font-inter); font-size: 52px; font-weight: 900; color: var(--color-forest-ink); line-height: 1; letter-spacing: -1.5px;">5</div>
    </div>
    <span style="display: inline-flex; align-self: flex-start; align-items: center; background: var(--color-forest-ink); color: var(--color-lime-volt); border-radius: 9999px; padding: 8px 18px; font-family: var(--font-inter); font-size: 13px; font-weight: 400; letter-spacing: -0.06px; line-height: 1; margin-top: 24px;">Foundations</span>
  </div>

  <!-- Papaya card with flag placeholder -->
  <div style="background: var(--color-papaya); border-radius: 52px; padding: 32px 28px; display: flex; flex-direction: column; justify-content: space-between; min-height: 180px;">
    <div style="width: 80px; height: 80px; border-radius: 9999px; background: #1a873a; display: flex; align-items: center; justify-content: center; overflow: hidden;">
      <svg width="80" height="80" viewBox="0 0 80 80">
        <circle cx="40" cy="40" r="40" fill="#009c3b"/>
        <polygon points="40,14 66,40 40,66 14,40" fill="#fedf00"/>
        <circle cx="40" cy="40" r="14" fill="#002776"/>
      </svg>
    </div>
    <span style="display: inline-flex; align-self: flex-start; align-items: center; background: var(--color-lime-volt); color: var(--color-forest-ink); border-radius: 9999px; padding: 8px 18px; font-family: var(--font-inter); font-size: 13px; font-weight: 400; letter-spacing: -0.06px; line-height: 1; margin-top: 24px;">Flags</span>
  </div>

</div>
```

### Lime Pill Button

backgroundColor: #87ea5c (display-p3), color: #083400, borderRadius: 9999px, paddingTop: 11px, paddingBottom: 11px, paddingRight: 24px, paddingLeft: 24px. Font: Inter 400 16px. No border — the lime fill IS the button. Used for 'Components', 'Flags', 'Tone of voice' category navigation.

### Ghost Pill Button

backgroundColor: transparent, color: #083400, borderRadius: 9999px, paddingTop: 11px, paddingBottom: 11px, paddingRight: 24px, paddingLeft: 24px. No visible border. Appears on same lime background surfaces where the lime fill would be redundant.

### Hero Display Block

backgroundColor: #87ea5c, full-width. Wise Sans weight 900 at 288–562px, color: #083400, lineHeight: 0.85. Text is centered and stacked — 2 lines maximum, each word or pair filling near full width. No padding reduction at any viewport — the type fills edge-to-edge aggressively.

### Navigation Bar

backgroundColor: #87ea5c (matches hero, seamless), logo left-aligned with Wise wordmark in #083400. Nav links center-right: 'Design at Wise', 'Foundations', 'Components', 'Patterns', 'Resources' in Inter 400 16px #083400 with -0.08px letter-spacing. Search icon (magnifier) far right. No divider between nav and hero — intentionally merged.

### Mosaic Content Card

Variable backgroundColor per tile: #87ea5c, #ffd5f0, #ffbd89, #2a0831, #370305, #ffffff. borderRadius: 86px. Contains either large display type (Wise Sans 900), illustration, photography, or product UI at full bleed within the rounded card bounds. Each tile is a self-contained visual story for a design system section.

### Editorial Subheading

Inter 600 45px, color: #083400, lineHeight: 1.17, letterSpacing: -0.5px. Displayed on #ffffff background with generous whitespace above and below (80px+). Used for statements like 'Made for the world' — single short line, centered or left-aligned.

### Typography Specimen Card

backgroundColor: #083400 (dark forest), borderRadius: 86px. Wise Sans weight 900 at 288px+, color: #87ea5c, lineHeight: 0.85. 'WISE SANS' stacked display — lime text on forest card. Demonstrates the inverse colorway from the hero.

### Category Label Tag

Same as Lime Pill Button — backgroundColor: #87ea5c, color: #083400, borderRadius: 9999px, padding: 11px 24px, Inter 400 16px. Positioned floating at bottom edge of mosaic section to label content category ('Flags', 'Components', 'Tone of voice').

## Similar Design Systems

- {'why': 'Coral/hot pink dominant brand color on fintech product — single saturated hue flooding UI that defies category conventions', 'business': 'Monzo'}
- {'why': 'Vivid lime/green as primary brand color with dark-on-bright type treatment and ultra-rounded pill buttons at 9999px', 'business': 'Duolingo'}
- {'why': 'Design system documentation with color-block mosaic tiles, each tile a distinct hue showcasing system components', 'business': 'Figma (brand site)'}
- {'why': 'Same lime-green brand color in fintech context, pill buttons, and dark forest-green text on bright backgrounds', 'business': 'Cash App'}
- {'why': 'Bold editorial display type (ultra-heavy, stacked) on vivid brand-colored backgrounds as primary hero treatment', 'business': 'Mailchimp'}

## Agent Prompt Guide

**Quick Color Reference**
- Text (primary): #083400 (Forest Ink)
- Background (hero/brand): #87ea5c (Lime Volt)
- Background (page): #ffffff
- Secondary text / borders: #58717a (Fog)
- CTA button fill: #87ea5c with #083400 text
- Dark panel: #2a0831 (Aubergine Night) or #370305 (Crimson Depth)
- Accent yellow: #ffea4b

**Example Component Prompts**

1. **Hero Section**: Full-bleed #87ea5c background, no padding. Wise Sans (substitute: Obviously or Impact) weight 900, color #083400, lineHeight 0.85, two stacked lines at ~288px each filling near-full width. Nav bar same #87ea5c background, Wise logo left, Inter 400 16px #083400 links centered-right, letterSpacing -0.08px.

2. **Category Tag**: backgroundColor #87ea5c, color #083400, borderRadius 9999px, padding 11px 24px, Inter 400 16px, no border. Use for labels like 'Components', 'Flags', 'Tone of voice'.

3. **Transaction Card**: backgroundColor #ffffff, borderRadius 86px, padding 24px. Header row: 'Transactions' Inter 600 16px #083400 left, 'See all' Inter 400 16px #083400 underlined right. Two transaction rows: 32px circular outlined icon, name Inter 600 16px #083400, amount Inter 600 16px #083400 right-aligned, status + day Inter 400 14px #58717a below name.

4. **Typography Specimen Card (dark)**: backgroundColor #083400, borderRadius 86px, full card. Wise Sans weight 900, color #87ea5c, lineHeight 0.85, stacked text at 288px+. This is the inverse hero — lime on forest.

5. **Editorial Section**: backgroundColor #ffffff, paddingTop 80px, paddingBottom 80px. Single centered line: Inter 600 45px #083400 letterSpacing -0.5px lineHeight 1.17. No decorative elements — the weight and scale carry the section.

## Wise Sans Usage Rules

Wise Sans is a custom typeface used exclusively for display-scale brand moments. It must not appear at sizes below 187px. Its defining characteristic is the 0.85 lineHeight — never increase this on display headlines or the stacked compression effect is lost. The two weights (400, 900) serve different roles: weight 900 for hero stacked headlines in the lime-on-forest or forest-on-lime colorways; weight 400 for secondary display moments. The 'ss01' OpenType feature must be enabled. When Wise Sans is unavailable, use a heavy-weight condensed grotesque (Obviously, Neue Haas Grotesk Display 900, or Anton) — the compression and weight are non-negotiable.

## Color Block System

The palette functions as a set of 'rooms' rather than a hierarchy. Each major section picks one background color from the set and fills the entire viewport width. The six primary backgrounds are: #87ea5c (Lime Volt), #ffffff (White), #083400 (Forest Ink), #2a0831 (Aubergine Night), #370305 (Crimson Depth), #ffbd89 (Papaya), #ffd5f0 (Cotton Candy). Text on dark backgrounds (#083400, #2a0831, #370305) uses #ffffff or #ffea4b. Text on light/lime backgrounds uses #083400. Never use more than one background color within a single section band. Transitions between sections are hard cuts — no gradients, no blends.
