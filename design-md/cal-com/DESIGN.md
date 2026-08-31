# Cal.com — Design System

> **North Star**: Monochrome Utility, Human Touch. A system that prioritizes clarity and function with a stark black-and-white palette, but softens it with friendly typography and rounded forms.
> **Theme**: light
> **Source**: https://cal.com
> **Refero Style**: https://styles.refero.design/style/5d7aa503-8cfa-49a4-bd3b-0c2f0f075c70
> **Synced**: 2026-09-01

## Overview

The design feels like a pragmatic, high-precision instrument. It's built on a strict and disciplined monochrome palette of black, white, and echelon grays, where color is intentionally excluded from the core UI to emphasize function. The custom font, 'Cal Sans', defines the visual identity with its geometric yet open letterforms, giving headlines a technical but approachable character. Nearly all interactive elements are either solid black or pill-shaped outlines, creating a binary system of action. Cards are the fundamental building block, using soft 8-12px radii and extremely subtle shadows to create a quiet, layered topology on a light gray background.

## Color Palette

- **Ink**: `#101010` — Primary CTAs, primary text, active states. Used as the strongest dark tone, providing maximum contrast and visual weight for key actions. [brand]
- **Action Blue**: `#0099ff` — Tertiary links, informational banner text. A rare, functional splash of color reserved for secondary calls to action and informational highlights. [accent]
- **White**: `#ffffff` — Card backgrounds, text on dark buttons. [neutral]
- **Paper**: `#f4f4f4` — Main page background. [neutral]
- **Graphite**: `#242424` — Headlines, primary body text. [neutral]
- **Slate**: `#6b7280` — Secondary text, descriptive copy, disabled states. [neutral]
- **Stone**: `#898989` — Placeholder text, decorative UI elements. [neutral]
- **Silver**: `#e5e7eb` — Borders, dividers, subtle backgrounds. [neutral]
- **Info Banner BG**: `#eff6fe` — Background for the top-of-page informational banner. [neutral]
- **Google Blue**: `#4285f4` — Integration logos only. [accent]
- **Google Yellow**: `#fbbc04` — Integration logos only. [accent]
- **Google Green**: `#34a853` — Integration logos only. [accent]
- **Google Red**: `#ea4335` — Integration logos only. [accent]

## Typography

- **Cal Sans**
- **Cal Sans UI Variable Light**
- **Inter**
- **Matter**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.4 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.4 |
| heading-sm | 20 | — | 1.3 |
| heading | 24 | — | 1.3 |
| heading-lg | 48 | — | 1.1 |
| display | 64 | — | 1.1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Section Gap**: 96px
- **Border Radius**: {'tags': '9999px', 'cards': '12px', 'inputs': '8px', 'buttons': '9999px (pills), 8px (rectangular)'}

## Layout

The site uses a centered layout within a max-width of 1200px, creating generous breathing room on either side. Sections are clearly demarcated by 96px of vertical space, establishing a calm, deliberate rhythm. The hero combines a large headline stack with a prominent product UI visual. Content below follows a predictable pattern of centered headlines followed by 3-column feature card grids or alternating text-and-visual blocks. This simple, highly structured approach emphasizes clarity and ease of navigation.

## Imagery

The visual language is entirely product-centric and informational. Imagery consists solely of clean, isolated product UI screenshots and the logos of integration partners. There is no lifestyle photography, illustration, or abstract graphics. This choice reinforces the brand's focus on its functional capabilities, letting the product itself be the hero. All visual elements are presented within contained cards, never full-bleed, maintaining the page's orderly, grid-based structure.

## Design Principles

### Do

- Use 'Cal Sans' weight 600 exclusively for headings (size 20px and above).
- Employ a strict monochrome palette (Ink, Graphite, Slate, Paper, White) for 99% of the UI.
- Use pill-shaped buttons (9999px radius) for all primary and secondary page CTAs.
- Apply a 12px border radius to all content cards and large containers.
- Use subtle, diffuse shadows (`rgba(36, 36, 36, 0.05) 0px 4px 8px 0px`) for elevation.
- Set body copy in 'Cal Sans UI Variable Light' with tight negative letter-spacing.
- Reserve the single 'Action Blue' (#0099ff) for secondary links or informational highlights.

### Don't

- Do not introduce any new colors to the core UI; confine color to logos and the single blue accent.
- Do not use sharp corners on buttons or cards.
- Do not use font weights heavier than 600.
- Do not use traditional outlined buttons; use either solid 'Ink' or 'ghost' pill buttons.
- Do not use gradients on any buttons or card backgrounds.
- Do not use borders on cards; use shadows for separation.
- Do not set body text in 'Cal Sans'; it is for headlines only.

## Components

### Compliance Info Banner

```html
<div style="--color-ink:#101010;--color-action-blue:#0099ff;--color-white:#ffffff;--color-paper:#f4f4f4;--color-graphite:#242424;--color-slate:#6b7280;--color-stone:#898989;--color-silver:#e5e7eb;--color-info-banner-bg:#eff6fe;--font-cal-sans:'Poppins',sans-serif;--font-inter:system-ui,-apple-system,sans-serif;width:600px;box-sizing:border-box;font-family:var(--font-inter);background:var(--color-info-banner-bg);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px;">
  <div style="display:flex;align-items:center;gap:10px;flex:1;">
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" style="flex-shrink:0;">
      <circle cx="8" cy="8" r="8" fill="#0099ff"/>
      <text x="8" y="12" text-anchor="middle" font-family="system-ui" font-size="10" font-weight="700" fill="white">i</text>
    </svg>
    <span style="font-family:var(--font-inter);font-size:14px;line-height:1.5;color:var(--color-graphite);letter-spacing:-0.2px;">Scheduling software that checks every compliance box: SOC 2 Type II, HIPAA, GDPR, CCPA, ISO 27001 &amp; more.</span>
  </div>
  <a href="#" style="display:inline-flex;align-items:center;gap:6px;background:var(--color-action-blue);color:var(--color-white);font-family:var(--font-inter);font-size:14px;font-weight:500;padding:8px 16px;border-radius:9999px;text-decoration:none;white-space:nowrap;flex-shrink:0;">
    Learn more
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M3 7h8M7 3l4 4-4 4" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </a>
</div>
```

### How It Works — Feature Cards

```html
<div style="--color-ink:#101010;--color-action-blue:#0099ff;--color-white:#ffffff;--color-paper:#f4f4f4;--color-graphite:#242424;--color-slate:#6b7280;--color-silver:#e5e7eb;--font-cal-sans:'Poppins',sans-serif;--font-inter:system-ui,-apple-system,sans-serif;width:600px;box-sizing:border-box;background:var(--color-paper);padding:48px 24px;font-family:var(--font-inter);">

  <!-- Section header -->
  <div style="text-align:center;margin-bottom:36px;">
    <div style="display:inline-flex;align-items:center;gap:8px;background:var(--color-white);border:1px solid var(--color-silver);border-radius:9999px;padding:6px 14px;margin-bottom:20px;">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
        <rect x="1" y="1" width="5" height="5" rx="1" fill="#242424"/>
        <rect x="8" y="1" width="5" height="5" rx="1" fill="#242424"/>
        <rect x="1" y="8" width="5" height="5" rx="1" fill="#242424"/>
        <rect x="8" y="8" width="5" height="5" rx="1" fill="#242424"/>
      </svg>
      <span style="font-family:var(--font-inter);font-size:13px;font-weight:500;color:var(--color-graphite);">How it works</span>
    </div>
    <h2 style="font-family:var(--font-cal-sans);font-size:32px;font-weight:600;color:var(--color-graphite);margin:0 0 12px;line-height:1.15;letter-spacing:0.3px;">With us, appointment<br>scheduling is easy</h2>
    <p style="font-family:var(--font-inter);font-size:15px;color:var(--color-slate);margin:0;line-height:1.5;letter-spacing:-0.19px;">Effortless scheduling for business and individuals,<br>powerful solutions for fast-growing modern companies.</p>
  </div>

  <!-- CTA buttons -->
  <div style="display:flex;justify-content:center;gap:12px;margin-bottom:36px;">
    <a href="#" style="display:inline-flex;align-items:center;gap:8px;background:var(--color-ink);color:var(--color-white);font-family:var(--font-inter);font-size:14px;font-weight:500;padding:11px 22px;border-radius:9999px;text-decoration:none;">
      Get started
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7h8M7 3l4 4-4 4" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </a>
    <a href="#" style="display:inline-flex;align-items:center;gap:8px;background:var(--color-white);color:var(--color-graphite);font-family:var(--font-inter);font-size:14px;font-weight:500;padding:11px 22px;border-radius:9999px;text-decoration:none;border:1px solid var(--color-silver);">
      Book a demo
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M3 7h8M7 3l4 4-4 4" stroke="#242424" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </a>
  </div>

  <!-- Feature cards -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;">
    <!-- Card 1 -->
    <div style="background:var(--color-white);border-radius:12px;padding:20px;box-shadow:rgba(36,36,36,0.05) 0px 4px 8px 0px;">
      <div style="display:inline-flex;align-items:center;justify-content:center;background:var(--color-paper);border-radius:8px;width:36px;height:36px;margin-bottom:14px;">
        <span style="font-family:var(--font-inter);font-size:12px;font-weight:600;color:var(--color-graphite);">01</span>
      </div>
      <h3 style="font-family:var(--font-cal-sans);font-size:15px;font-weight:600;color:var(--color-graphite);margin:0 0 8px;line-height:1.3;">Connect your calendar</h3>
      <p style="font-family:var(--font-inter);font-size:13px;color:var(--color-slate);margin:0;line-height:1.5;letter-spacing:-0.2px;">We'll handle all the cross-referencing, so you don't have to worry about double bookings.</p>
    </div>
    <!-- Card 2 -->
    <div style="background:var(--color-white);border-radius:12px;padding:20px;box-shadow:rgba(36,36,36,0.05) 0px 4px 8px 0px;">
      <div style="display:inline-flex;align-items:center;justify-content:center;background:var(--color-paper);border-radius:8px;width:36px;height:36px;margin-bottom:14px;">
        <span style="font-family:var(--font-inter);font-size:12px;font-weight:600;color:var(--color-graphite);">02</span>
      </div>
      <h3 style="font-family:var(--font-cal-sans);font-size:15px;font-weight:600;color:var(--color-graphite);margin:0 0 8px;line-height:1.3;">Set your availability</h3>
      <p style="font-family:var(--font-inter);font-size:13px;color:var(--color-slate);margin:0;line-height:1.5;letter-spacing:-0.2px;">Want to block off weekends? Set up any buffers? We make that easy.</p>
    </div>
    <!-- Card 3 -->
    <div style="background:var(--color-white);border-radius:12px;padding:20px;box-shadow:rgba(36,36,36,0.05) 0px 4px 8px 0px;">
      <div style="display:inline-flex;align-items:center;justify-content:center;background:var(--color-paper);border-radius:8px;width:36px;height:36px;margin-bottom:14px;">
        <span style="font-family:var(--font-inter);font-size:12px;font-weight:600;color:var(--color-graphite);">03</span>
      </div>
      <h3 style="font-family:var(--font-cal-sans);font-size:15px;font-weight:600;color:var(--color-graphite);margin:0 0 8px;line-height:1.3;">Choose how to meet</h3>
      <p style="font-family:var(--font-inter);font-size:13px;color:var(--color-slate);margin:0;line-height:1.5;letter-spacing:-0.2px;">It could be a video chat, phone call, or a walk in the park!</p>
    </div>
  </div>
</div>
```

### Testimonial Card

```html
<div style="--color-ink:#101010;--color-white:#ffffff;--color-paper:#f4f4f4;--color-graphite:#242424;--color-slate:#6b7280;--color-silver:#e5e7eb;--font-cal-sans:'Poppins',sans-serif;--font-inter:system-ui,-apple-system,sans-serif;width:600px;box-sizing:border-box;background:var(--color-paper);padding:48px 24px;font-family:var(--font-inter);display:flex;justify-content:center;">
  <div style="background:var(--color-white);border-radius:12px;padding:32px;box-shadow:rgba(36,36,36,0.05) 0px 4px 8px 0px;max-width:520px;width:100%;">
    <!-- Stars -->
    <div style="display:flex;gap:4px;margin-bottom:20px;">
      <svg width="18" height="18" viewBox="0 0 18 18" fill="#f59e0b"><path d="M9 1l2.39 4.84 5.34.78-3.87 3.77.91 5.32L9 13.27l-4.77 2.44.91-5.32L1.27 6.62l5.34-.78z"/></svg>
      <svg width="18" height="18" viewBox="0 0 18 18" fill="#f59e0b"><path d="M9 1l2.39 4.84 5.34.78-3.87 3.77.91 5.32L9 13.27l-4.77 2.44.91-5.32L1.27 6.62l5.34-.78z"/></svg>
      <svg width="18" height="18" viewBox="0 0 18 18" fill="#f59e0b"><path d="M9 1l2.39 4.84 5.34.78-3.87 3.77.91 5.32L9 13.27l-4.77 2.44.91-5.32L1.27 6.62l5.34-.78z"/></svg>
      <svg width="18" height="18" viewBox="0 0 18 18" fill="#f59e0b"><path d="M9 1l2.39 4.84 5.34.78-3.87 3.77.91 5.32L9 13.27l-4.77 2.44.91-5.32L1.27 6.62l5.34-.78z"/></svg>
      <svg width="18" height="18" viewBox="0 0 18 18" fill="#f59e0b"><path d="M9 1l2.39 4.84 5.34.78-3.87 3.77.91 5.32L9 13.27l-4.77 2.44.91-5.32L1.27 6.62l5.34-.78z"/></svg>
    </div>
    <!-- Quote -->
    <blockquote style="margin:0 0 24px;padding:0;">
      <p style="font-family:var(--font-cal-sans);font-size:22px;font-weight:600;color:var(--color-graphite);line-height:1.35;margin:0;letter-spacing:0.2px;">&ldquo;Just gave it a go and it&rsquo;s definitely the easiest meeting I&rsquo;ve ever scheduled!&rdquo;</p>
    </blockquote>
    <!-- Author -->
    <div style="display:flex;align-items:center;gap:12px;padding-top:20px;border-top:1px solid var(--color-silver);">
      <div style="width:44px;height:44px;border-radius:9999px;background:var(--color-silver);overflow:hidden;flex-shrink:0;display:flex;align-items:center;justify-content:center;">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <circle cx="12" cy="8" r="4" fill="#898989"/>
          <path d="M4 20c0-4 3.58-7 8-7s8 3 8 7" fill="#898989"/>
        </svg>
      </div>
      <div>
        <div style="font-family:var(--font-inter);font-size:14px;font-weight:600;color:var(--color-graphite);margin-bottom:2px;">Aria Minaei</div>
        <div style="font-family:var(--font-inter);font-size:13px;color:var(--color-slate);">CEO, Theatre.JS</div>
      </div>
    </div>
  </div>
</div>
```

### Primary CTA Button

A pill-shaped button. Background: Ink (#101010). Text: White (#ffffff). Font: Cal Sans UI at 14-16px. Radius: 9999px. Padding: ~12px 24px.

### Secondary Ghost Button

A pill-shaped outline button. Background: transparent or Paper (#f4f4f4). Text: Graphite (#242424). Border: 1px solid Silver (#e5e7eb). Radius: 9999px. Padding: ~12px 24px.

### Header CTA Button

A rectangular button. Background: Ink (#101010). Text: White (#ffffff). Font: Cal Sans UI at 14px. Radius: 8px. Padding: ~8px 16px.

### Tag Button

A small pill button. Background: Paper (#f4f4f4) or Silver (#e5e7eb). Text: Graphite (#242424). Radius: 9999px. Padding: ~4px 12px.

### Scheduling Widget Card

Background: White (#ffffff). Padding: 16px. Radius: 12px. Shadow: `rgba(36, 36, 36, 0.05) 0px 4px 8px 0px`. Contains an interactive calendar UI.

### Navigation Link

Text-only link. Color: Graphite (#242424). Font: Cal Sans UI at 14-16px. No underline.

## Similar Design Systems

- {'why': 'Direct competitor with a similar clean, utility-focused scheduling UI, but uses more color.', 'business': 'Calendly'}
- {'why': 'Shares the disciplined monochrome palette, precision typography, and subtle shadows.', 'business': 'Linear'}
- {'why': 'Similar use of a geometric sans-serif for headlines (Geist) against a stark black-and-white UI.', 'business': 'Vercel'}
- {'why': 'Employs a custom slab-serif for identity and relies on a clean, card-based layout with a primarily B&W palette.', 'business': 'Pitch'}

## Agent Prompt Guide

### Quick Color Reference
- **Page Background:** `#f4f4f4` (Paper)
- **Card Background:** `#ffffff` (White)
- **Headline Text:** `#242424` (Graphite)
- **Body Text:** `#242424` (Graphite)
- **Primary CTA:** `#101010` (Ink) background, `#ffffff` (White) text
- **Borders/Dividers:** `#e5e7eb` (Silver)

### Example Component Prompts
1.  **Hero Section:** "Create a hero section with a `#f4f4f4` background. On the left, add a headline 'The better way to schedule' using 'Cal Sans' at 64px, weight 600, color `#242424`, and line-height 1.1. Below it, add body text using 'Cal Sans UI' at 18px, color `#6b7280'. On the right, place a large card with a white background, 12px radius, and a subtle shadow `rgba(36, 36, 36, 0.05) 0px 4px 8px 0px` to represent a scheduling widget."
2.  **Primary CTA Button:** "Create a button with the text 'Get started'. Make it pill-shaped with a `9999px` radius. Use a `#101010` background color and `#ffffff` text color. The font should be 'Cal Sans UI' at 16px. Use padding of 12px top/bottom and 24px left/right."
3.  **Feature Card:** "Create a feature card with a `#ffffff` background, `24px` padding, a `12px` border radius, and a `rgba(36, 36, 36, 0.05) 0px 4px 8px 0px` box shadow. Inside, add a small numbered tag, a heading 'Connect your calendar' in 'Cal Sans' at 20px, and body text 'We'll handle all the cross-referencing' in 'Cal Sans UI' at 16px."
