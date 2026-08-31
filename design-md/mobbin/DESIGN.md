# Mobbin — Design System

> **North Star**: Grayscale specimen board — a printer's proof sheet where typographic weight IS color.
> **Theme**: light
> **Source**: https://mobbin.com
> **Refero Style**: https://styles.refero.design/style/ef44a995-6745-4dc7-86ab-f7227f108f81
> **Synced**: 2026-09-01

## Overview

Mobbin runs on pure achromatic restraint — zero chroma across the entire palette, forcing hierarchy through weight, size, and tone alone. The page is white space interrupted by near-black ink (#141414) at display sizes and warm-gray (#707070, #adadad) for secondary text. The custom 'saans' typeface is the single differentiator: fractional weights (440, 456, 652) that don't exist in any system font, creating headline mass that sits between regular and semibold — typography doing the work of color. 9999px pill shapes appear on every interactive element while card content sits on 16-24px rounded rectangles, making buttons feel like badges in a sea of contained thumbnails. The content itself — mobile app screenshots in grayscale cards — IS the visual texture of the page.

## Color Palette

- **Midnight Ink**: `#141414` — Primary text, headings, filled CTA buttons, nav items, icon strokes — the single chromatic workhorse of an achromatic system [neutral]
- **Pure Canvas**: `#ffffff` — Page background, card surfaces, button text on dark fills [neutral]
- **Graphite**: `#707070` — Body copy, secondary links, descriptive text [neutral]
- **Ash**: `#adadad` — Tertiary text, disabled/muted button borders, placeholder icons [neutral]
- **Fog**: `#ededed` — Dividers, subtle borders, card outlines [neutral]
- **Mist**: `#f2f2f2` — Nav background tint, input fields, inner surface elevation [neutral]
- **Silver**: `#c2c2c2` — Skeleton loaders, inactive UI fills [neutral]
- **Slate Shadow**: `#e0e0e0` — Inset button shadow ring (rgba(64,64,64,0.16) 0px 0px 0px 1px) [neutral]

## Typography

- **saans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 16 |
| body-sm | 14 | — | 20 |
| body | 16 | — | 22 |
| subheading | 20 | — | 28 |
| heading | 32 | — | 42 |
| heading-lg | 56 | — | 63 |
| display | 80 | — | 80 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 16-24px
- **Element Gap**: 8-16px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '9999px', 'cards': '16-24px', 'inputs': '9999px', 'modals': '24px', 'buttons': '9999px', 'thumbnails': '16px'}

## Layout

Max-width centered (~1280px), white background throughout. Hero is vertically centered text stack — large display headline (80px) over a subtitle paragraph over two pill CTAs side by side, with a featured app icon above the headline as a specimen. Below the hero: full-width trust logo bar with muted gray brand logos. The gallery section introduces a sticky secondary nav (app type tabs, search bar, filter row) above a 3-column card grid with comfortable 16-20px gutters. Testimonials section uses a 4-column masonry-style text card grid on white. Navigation is a floating top bar with logo left, text links center, CTA pill right — switches from transparent to white/f2f2f2 on scroll. Section vertical rhythm is consistently 80px between major blocks. No alternating dark/light bands — the entire page is white with card grids providing visual texture.

## Surfaces / Elevation

- **Page**
- **Card**
- **Input / Chip**
- **Overlay Dropdown**

## Imagery

Content IS the imagery: grayscale mobile app screenshots displayed as contained cards in a 3-column grid. Screenshots are cropped to phone frames, placed on white card backgrounds with 16px radius, and rendered in desaturated tones that match the achromatic brand palette — colorful apps appear muted because the surrounding UI demands it. No lifestyle photography, no illustrations, no abstract graphics. Partner/customer logos (Uber, Meta, Airbnb, etc.) appear as flat monochrome SVGs in a trust bar. The Revolut-style app icon in the hero (rounded square, 24px radius, green fill with white symbol) is the only chromatic element on the page — a deliberate specimen of the content being showcased, not a brand choice. Icon style throughout the UI is outlined, thin stroke (~1.5px), monochrome #141414.

## Design Principles

### Do

- Use #141414 as the only 'color' — every UI accent, icon, filled button, and active state is this near-black, never a chromatic hue.
- Apply 9999px radius to every interactive pill element: buttons, tags, search inputs, filter chips. Non-interactive content containers use 16–24px radius.
- Set display headlines (56–80px) at saans weight 600–652 with letter-spacing -0.007em to -0.011em and lineHeight 1.00–1.13.
- Use font-feature-settings: '"calt" 0, "dlig", "ss07"' on all saans text to activate the custom ligature and stylistic set that distinguish it from fallback sans-serifs.
- Differentiate card elevation with 1px solid #ededed borders only — never box-shadow on cards. Reserve box-shadow exclusively for floating dropdowns.
- Use fractional saans weights: 440 for UI labels/nav, 456 for mid-emphasis body, 652 for hero numerics — never round to 400/500/600 at sizes where the fractional weight is available.
- Maintain 80px vertical section rhythm between major content blocks, with 24px internal card padding as the baseline.

### Don't

- Never introduce a chromatic accent color — not blue for links, not green for success states, not any hue. The entire brand palette is achromatic.
- Never use box-shadow on cards or gallery thumbnails — borders do that work; shadows on content cards would compete with the screenshot imagery inside them.
- Never use font-weight 700 or 800 — the heaviest weight is 652. Heavier weights would break the typographic restraint that defines the system.
- Never use radius values other than 9999px (interactive), 24px (large containers), 16px (cards/images), or 8px (inline badges) — arbitrary intermediate values destroy the shape vocabulary.
- Never place colored backgrounds behind sections — alternating band layouts should use #ffffff vs #f2f2f2 at most, never tinted or chromatic fills.
- Never left-align hero headlines — the centered display type at 80px/56px is the layout anchor; shifting it breaks the symmetry that makes the screenshot grid feel organized.
- Never remove letter-spacing from display type — at 80px, the -0.88px tracking is what makes saans feel like a custom typeface rather than a generic web font.

## Components

### Button Group — Primary, Outlined & Muted

```html
<style>
  :root {
    --color-midnight-ink: #141414;
    --color-pure-canvas: #ffffff;
    --color-graphite: #707070;
    --color-ash: #adadad;
    --color-fog: #ededed;
    --color-mist: #f2f2f2;
    --color-silver: #c2c2c2;
    --font-saans: 'Inter', sans-serif;
    --shadow-subtle: rgba(64, 64, 64, 0.16) 0px 0px 0px 1px inset;
  }

  .btn-group-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 32px;
    padding: 48px 40px;
    background: var(--color-pure-canvas);
    font-family: var(--font-saans);
    width: 600px;
    box-sizing: border-box;
  }

  .btn-group-label {
    font-size: 12px;
    font-family: var(--font-saans);
    font-weight: 400;
    color: var(--color-ash);
    letter-spacing: 0.2px;
    text-transform: uppercase;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
    align-self: flex-start;
  }

  .btn-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
    width: 100%;
  }

  .btn-primary {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 12px 20px;
    background: var(--color-midnight-ink);
    color: var(--color-pure-canvas);
    border: none;
    border-radius: 9999px;
    font-family: var(--font-saans);
    font-size: 15px;
    font-weight: 600;
    line-height: 1.4;
    letter-spacing: 0.1px;
    cursor: pointer;
    text-decoration: none;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
    transition: box-shadow 0.15s ease;
  }

  .btn-primary:hover {
    box-shadow: var(--shadow-subtle);
  }

  .btn-outlined {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 12px 20px;
    background: transparent;
    color: var(--color-midnight-ink);
    border: 1px solid var(--color-midnight-ink);
    border-radius: 9999px;
    font-family: var(--font-saans);
    font-size: 15px;
    font-weight: 440;
    line-height: 1.4;
    letter-spacing: 0.1px;
    cursor: pointer;
    text-decoration: none;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .btn-outlined svg {
    flex-shrink: 0;
  }

  .btn-muted {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 14px;
    background: transparent;
    color: var(--color-ash);
    border: 1px solid var(--color-ash);
    border-radius: 9999px;
    font-family: var(--font-saans);
    font-size: 14px;
    font-weight: 400;
    line-height: 1.4;
    letter-spacing: 0.1px;
    cursor: pointer;
    text-decoration: none;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .btn-active-filter {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 14px;
    background: var(--color-midnight-ink);
    color: var(--color-pure-canvas);
    border: none;
    border-radius: 9999px;
    font-family: var(--font-saans);
    font-size: 14px;
    font-weight: 440;
    line-height: 1.4;
    cursor: pointer;
    text-decoration: none;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .divider {
    width: 100%;
    height: 1px;
    background: var(--color-fog);
  }

  .section-title {
    font-size: 11px;
    font-family: var(--font-saans);
    font-weight: 400;
    color: var(--color-silver);
    letter-spacing: 1px;
    text-transform: uppercase;
    align-self: flex-start;
    margin-bottom: -20px;
  }
</style>

<div class="btn-group-wrapper">
  <span class="section-title">CTA Buttons</span>
  <div class="btn-row">
    <a href="#" class="btn-primary">Join for free</a>
    <a href="#" class="btn-outlined">
      See our plans
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M2.5 7H11.5M7.5 3L11.5 7L7.5 11" stroke="#141414" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </a>
  </div>

  <div class="divider"></div>

  <span class="section-title">Filter Tabs</span>
  <div class="btn-row">
    <a href="#" class="btn-active-filter">Latest</a>
    <a href="#" class="btn-outlined" style="font-size:14px;font-weight:440;padding:8px 14px;">Most popular</a>
    <a href="#" class="btn-muted">Top rated</a>
  </div>

  <div class="divider"></div>

  <span class="section-title">Platform Tabs</span>
  <div class="btn-row">
    <a href="#" class="btn-outlined" style="font-size:14px;font-weight:440;padding:8px 14px;">iOS</a>
    <a href="#" class="btn-active-filter">Web</a>
    <a href="#" class="btn-muted">Android</a>
  </div>
</div>
```

### Search Input with Filter Pills

```html
<style>
  :root {
    --color-midnight-ink: #141414;
    --color-pure-canvas: #ffffff;
    --color-graphite: #707070;
    --color-ash: #adadad;
    --color-fog: #ededed;
    --color-mist: #f2f2f2;
    --font-saans: 'Inter', sans-serif;
  }

  .search-section {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding: 32px 32px;
    background: var(--color-pure-canvas);
    font-family: var(--font-saans);
    width: 600px;
    box-sizing: border-box;
  }

  .search-bar {
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--color-mist);
    border-radius: 9999px;
    padding: 10px 16px;
    width: 100%;
    box-sizing: border-box;
  }

  .search-icon {
    flex-shrink: 0;
    color: var(--color-ash);
  }

  .search-input {
    flex: 1;
    border: none;
    background: transparent;
    outline: none;
    font-family: var(--font-saans);
    font-size: 14px;
    font-weight: 400;
    color: var(--color-midnight-ink);
    letter-spacing: 0.13px;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .search-input::placeholder {
    color: var(--color-ash);
  }

  .search-toggle {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: var(--color-pure-canvas);
    border-radius: 9999px;
    padding: 4px 10px;
    font-family: var(--font-saans);
    font-size: 12px;
    font-weight: 400;
    color: var(--color-graphite);
    letter-spacing: 0.2px;
    flex-shrink: 0;
    cursor: pointer;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .filter-row {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }

  .filter-label {
    font-size: 12px;
    font-family: var(--font-saans);
    font-weight: 400;
    color: var(--color-ash);
    letter-spacing: 0.2px;
    margin-right: 4px;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .pill-active {
    display: inline-flex;
    align-items: center;
    padding: 6px 14px;
    background: var(--color-midnight-ink);
    color: var(--color-pure-canvas);
    border: none;
    border-radius: 9999px;
    font-family: var(--font-saans);
    font-size: 13px;
    font-weight: 440;
    cursor: pointer;
    text-decoration: none;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .pill-inactive {
    display: inline-flex;
    align-items: center;
    padding: 6px 14px;
    background: transparent;
    color: var(--color-midnight-ink);
    border: 1px solid var(--color-fog);
    border-radius: 9999px;
    font-family: var(--font-saans);
    font-size: 13px;
    font-weight: 400;
    cursor: pointer;
    text-decoration: none;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .pill-muted {
    display: inline-flex;
    align-items: center;
    padding: 6px 14px;
    background: transparent;
    color: var(--color-ash);
    border: 1px solid var(--color-fog);
    border-radius: 9999px;
    font-family: var(--font-saans);
    font-size: 13px;
    font-weight: 400;
    cursor: pointer;
    text-decoration: none;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .secondary-nav {
    display: flex;
    align-items: center;
    gap: 0;
    border-bottom: 1px solid var(--color-fog);
    padding-bottom: 16px;
    margin-bottom: 0;
  }

  .snav-item {
    font-family: var(--font-saans);
    font-size: 14px;
    font-weight: 440;
    color: var(--color-graphite);
    text-decoration: none;
    padding: 6px 14px;
    border-radius: 9999px;
    background: transparent;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
    cursor: pointer;
  }

  .snav-item.active {
    color: var(--color-midnight-ink);
    border-bottom: 2px solid var(--color-midnight-ink);
    border-radius: 0;
    padding-bottom: 16px;
    margin-bottom: -17px;
  }
</style>

<div class="search-section">
  <div class="secondary-nav">
    <a href="#" class="snav-item active">Apps</a>
    <a href="#" class="snav-item">Sites</a>
  </div>

  <div class="search-bar">
    <svg class="search-icon" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="7" cy="7" r="5" stroke="#adadad" stroke-width="1.5"/>
      <path d="M11 11L14 14" stroke="#adadad" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
    <input class="search-input" type="text" placeholder="Search on iOS..." />
    <div class="search-toggle">
      <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
        <rect x="1" y="2" width="10" height="1.5" rx="0.75" fill="#707070"/>
        <rect x="1" y="5.25" width="10" height="1.5" rx="0.75" fill="#707070"/>
        <rect x="1" y="8.5" width="10" height="1.5" rx="0.75" fill="#707070"/>
      </svg>
      Text in Screenshot
    </div>
  </div>

  <div class="filter-row">
    <span class="filter-label">Filter:</span>
    <a href="#" class="pill-active">Latest</a>
    <a href="#" class="pill-inactive">Most popular</a>
    <a href="#" class="pill-muted">Top rated</a>
    <a href="#" class="pill-inactive">Finance</a>
    <a href="#" class="pill-inactive">Login</a>
    <a href="#" class="pill-muted">Onboarding</a>
  </div>
</div>
```

### Testimonial Cards

```html
<style>
  :root {
    --color-midnight-ink: #141414;
    --color-pure-canvas: #ffffff;
    --color-graphite: #707070;
    --color-ash: #adadad;
    --color-fog: #ededed;
    --color-mist: #f2f2f2;
    --color-silver: #c2c2c2;
    --font-saans: 'Inter', sans-serif;
  }

  .testimonials-wrapper {
    width: 600px;
    box-sizing: border-box;
    padding: 40px 32px;
    background: var(--color-pure-canvas);
    font-family: var(--font-saans);
  }

  .testimonials-heading {
    font-family: var(--font-saans);
    font-size: 36px;
    font-weight: 600;
    color: var(--color-midnight-ink);
    line-height: 1.1;
    letter-spacing: -0.5px;
    text-align: center;
    margin: 0 0 32px 0;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .testimonials-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  .tcard {
    background: var(--color-pure-canvas);
    border: 1px solid var(--color-fog);
    border-radius: 20px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .tcard-header {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .tcard-avatar {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: var(--color-mist);
    flex-shrink: 0;
    overflow: hidden;
    position: relative;
  }

  .tcard-avatar-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-saans);
    font-size: 16px;
    font-weight: 600;
    color: var(--color-graphite);
    background: var(--color-mist);
  }

  .tcard-badge {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--color-silver);
    border: 1.5px solid var(--color-pure-canvas);
  }

  .tcard-meta {
    display: flex;
    flex-direction: column;
    gap: 1px;
  }

  .tcard-name {
    font-family: var(--font-saans);
    font-size: 14px;
    font-weight: 600;
    color: var(--color-midnight-ink);
    line-height: 1.3;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .tcard-company {
    font-family: var(--font-saans);
    font-size: 13px;
    font-weight: 400;
    color: var(--color-ash);
    line-height: 1.3;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
  }

  .tcard-body {
    font-family: var(--font-saans);
    font-size: 13px;
    font-weight: 400;
    color: var(--color-graphite);
    line-height: 1.55;
    letter-spacing: 0.1px;
    font-feature-settings: 'calt' 0, 'dlig', 'ss07';
    margin: 0;
  }

  .avatar-bg-a { background: #d9e8ff; color: #4a6fa5; }
  .avatar-bg-b { background: #ffe0d9; color: #a5544a; }
  .avatar-bg-c { background: #d9f5e8; color: #3a7a5a; }
  .avatar-bg-d { background: #f0d9ff; color: #7a4aa5; }
</style>

<div class="testimonials-wrapper">
  <h2 class="testimonials-heading">What our users are saying.</h2>

  <div class="testimonials-grid">
    <div class="tcard">
      <div class="tcard-header">
        <div class="tcard-avatar">
          <div class="tcard-avatar-inner avatar-bg-a">S</div>
          <div class="tcard-badge" style="background:#c2c2c2;"></div>
        </div>
        <div class="tcard-meta">
          <span class="tcard-name">Sebastian Speier</span>
          <span class="tcard-company">Shop</span>
        </div>
      </div>
      <p class="tcard-body">Mobbin is a great resource and it always comes in handy to see what the best practices or standards are for mobile patterns in our current landscape.</p>
    </div>

    <div class="tcard">
      <div class="tcard-header">
        <div class="tcard-avatar">
          <div class="tcard-avatar-inner avatar-bg-b">M</div>
          <div class="tcard-badge" style="background:#5b8fff;"></div>
        </div>
        <div class="tcard-meta">
          <span class="tcard-name">Meng To</span>
          <span class="tcard-company">DesignCode</span>
        </div>
      </div>
      <p class="tcard-body">Mobbin is a game-changer for designers looking to step up their understanding of UX and UI design patterns. It's indispensable in the modern designer's toolbox.</p>
    </div>

    <div class="tcard">
      <div class="tcard-header">
        <div class="tcard-avatar">
          <div class="tcard-avatar-inner avatar-bg-c">T</div>
          <div class="tcard-badge" style="background:#aaa;"></div>
        </div>
        <div class="tcard-meta">
          <span class="tcard-name">Taha Hossain</span>
          <span class="tcard-company">Daybreak</span>
        </div>
      </div>
      <p class="tcard-body">We can't imagine a product design process without Mobbin. The quality, clarity and precision it provides make it just as valuable as it is intuitive.</p>
    </div>

    <div class="tcard">
      <div class="tcard-header">
        <div class="tcard-avatar">
          <div class="tcard-avatar-inner avatar-bg-d">J</div>
          <div class="tcard-badge" style="background:#e05;"></div>
        </div>
        <div class="tcard-meta">
          <span class="tcard-name">John Bai</span>
          <span class="tcard-company">Plaid</span>
        </div>
      </div>
      <p class="tcard-body">All my homies love Mobbin. I finally deleted that folder of 1,866 unorganized screenshots and haven't looked back since. God's work.</p>
    </div>
  </div>
</div>
```

### Primary Filled Button

Background #141414, text #ffffff, radius 9999px, padding 0px 16px (height set by line-height), font saans weight 600 at 14–16px. Inset shadow ring rgba(64,64,64,0.16) 0px 0px 0px 1px on hover state.

### Outlined Pill Button

Background transparent, text #141414, border 1px solid #141414, radius 9999px, padding 0px 16px. Sits beside primary CTA as a lighter-weight alternative.

### Muted Pill Button

Background transparent, text #adadad, border 1px solid #adadad, radius 9999px, padding 0px 12px. Used for unselected tab filters like 'Most popular', 'Top rated'.

### Inline Underline Link

Background transparent, text #141414, border-radius 0px, padding 2px on all sides. No background, no border — purely typographic. Used for secondary in-text navigation.

### App Screenshot Card

White background, border 1px solid #ededed, radius 16px, padding 16px. Contains a mobile phone screenshot image (radius 12–16px on the image itself), a 'New' or 'Updated' badge (9999px pill, #141414 fill, white text, 12px font), and app name in saans 14px weight 440 #141414.

### Category Navigation Menu

White background, box-shadow rgba(0,0,0,0.04) 0px 8px 40px 0px, radius 24px, padding 24-32px. Four-column grid layout with category labels in saans 12px weight 400 #adadad uppercase, and category items in saans 16px weight 440 #141414.

### Top Navigation Bar

Background #ffffff or #f2f2f2 tint, padding 0 24px, height 60px. Logo left-aligned, nav links (saans 14px weight 440 #141414) center, 'Join for free' filled pill button right. All nav links are plain text — no underline, no border.

### Filter Pill / Tab Row

Row of pill buttons. Active: background #141414 text #ffffff radius 9999px padding 4px 12px. Inactive: background transparent text #141414 border 1px solid #141414 radius 9999px padding 4px 12px. Font saans 14px weight 440. Gap 8px between pills.

### Search Input

Background #f2f2f2, border none, radius 9999px, padding 8px 16px, placeholder text saans 14px #adadad, input text saans 14px #141414. Search icon left-inset, 'Text in Screenshot' toggle pill right-inset.

### Section Stat Display

Display number at 56–80px saans weight 652, letter-spacing -0.88px, line-height 1.00, color #141414. Label text below at 16–20px weight 440 #707070. Numbers are the visual centerpiece — no decorative elements.

## Similar Design Systems

- {'why': 'Same achromatic gallery-of-screenshots model with white backgrounds and card-border-only elevation', 'business': 'Screenlane'}
- {'why': 'Pill-button navigation and 3-column content grid for design inspiration browsing', 'business': 'Dribbble'}
- {'why': 'Identical concept — no-chroma UI wrapping colorful screenshot content — with similar nav and filter-pill patterns', 'business': 'Lookup.design'}
- {'why': 'Fractional-weight custom typography as the primary brand differentiator in an otherwise near-monochrome system', 'business': 'Linear'}
- {'why': 'App screenshot library with the same white/gray achromatic chrome and pill-shaped filter chips above a grid', 'business': 'Refero.design'}

## Agent Prompt Guide

**Quick Color Reference**
- Text (primary): #141414
- Text (secondary): #707070
- Text (tertiary / disabled): #adadad
- Background: #ffffff
- Surface / input fill: #f2f2f2
- Border / divider: #ededed
- CTA button fill: #141414 → white text
- Active tab: #141414 fill → white text; Inactive tab: transparent → #141414 border + text

**Example Component Prompts**

1. **Hero Section**: White background. App icon specimen (64px rounded square, 24px radius) centered above headline. Headline 'Discover real-world design inspiration.' at 80px saans weight 652, #141414, letter-spacing -0.88px, line-height 1.00, center-aligned. Subtitle at 20px weight 440, #707070, line-height 1.50, center-aligned, max-width 560px. Two pill CTAs side by side: filled (#141414 bg, white text, 9999px radius, 0px 16px padding) and outlined (transparent bg, #141414 border+text, same radius/padding). Vertical gap between elements: 24px.

2. **Screenshot Gallery Card**: White background, border 1px solid #ededed, radius 16px, padding 16px. Phone screenshot image fills upper portion (radius 12px). Bottom row: app icon (24px circle) + app name saans 14px weight 440 #141414, left-aligned. 'New' badge top-left: #141414 fill, white text, saans 12px weight 600, radius 9999px, padding 2px 8px.

3. **Global Nav Bar**: Background #ffffff, height 60px, padding 0 32px. Left: Mobbin logotype saans weight 600 14px #141414. Center: 'Pricing', 'Awards', 'Log in' in saans 14px weight 440 #141414, gap 32px. Right: 'Join for free' pill button — #141414 bg, white text, saans 14px weight 600, radius 9999px, padding 0 16px.

4. **Testimonial Card**: White bg, border 1px solid #ededed, radius 16px, padding 24px. Top row: avatar circle 36px + name saans 14px weight 600 #141414 + company saans 12px weight 400 #707070. Body text saans 14px weight 400 #141414, line-height 1.50. No shadow.

5. **Filter Pill Row**: Horizontal flex row, gap 8px. Active pill: #141414 bg, #ffffff text, saans 14px weight 440, radius 9999px, padding 4px 12px. Inactive pill: transparent bg, #141414 border 1px + text, same sizing. Muted/disabled variant: #adadad border + text.

## Fractional Weight System

Saans exposes five weight stops that map to semantic roles:
- 400: long-form body copy, footnotes
- 440: UI labels, nav links, card metadata, button text on secondary actions
- 456: mid-emphasis body, subheadings, feature descriptions
- 600: headlines, section titles, CTA button text
- 652: hero display numerics, maximum-emphasis headlines at 56–80px

The gap between 440 and 456 is subtle but intentional — 456 is used where 440 reads too light on white at 16–20px, but 600 would feel heavy. Never substitute weight 500 or 700 — no stops exist between 456 and 600 in the intended rendering.
