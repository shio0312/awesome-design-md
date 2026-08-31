# v0 by Vercel — Design System

> **North Star**: A Machinist's Blueprint. Precision and function are paramount, with every element serving a clear purpose on a clean, technical surface.
> **Theme**: light
> **Source**: https://v0.dev
> **Refero Style**: https://styles.refero.design/style/50aa2b8e-4760-4379-a3c1-59b65d8576a7
> **Synced**: 2026-09-01

## Overview

The design feels like a functional schematic on a stark white drafting table. Its nearly monochrome palette — #FFFFFF, #FAFAFA, #EAEAEA, #171717 — creates a utility-first atmosphere where user input is the only source of color. Typography is the main architectural element; a custom sans-serif is used everywhere, with tight negative letter-spacing at large sizes creating dense, impactful headlines. The UI is built from simple primitives: solid black CTAs with an 8px radius and subtly bordered white chips, distinguishing primary commands from secondary suggestions.

## Color Palette

- **Paper White**: `#ffffff` — Text on dark buttons, pill button backgrounds. [neutral]
- **Canvas**: `#fafafa` — Primary page background. [neutral]
- **Line**: `#eaeaea` — Borders for headers, ghost buttons, and dividers. [neutral]
- **Subtext**: `#666666` — Secondary text, navigation links, placeholder text. [neutral]
- **Icon**: `#7d7d7d` — Inactive icons and tertiary UI elements. [neutral]
- **Ink**: `#171717` — Primary text, headlines, and primary button backgrounds. [neutral]
- **Onyx**: `#000000` — Logo, icons, highest contrast text. [neutral]

## Typography

- **GeistSans**
- **GeistMono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.5 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.56 |
| heading-sm | 20 | — | 1.25 |
| heading | 24 | — | 1.33 |
| heading-lg | 32 | — | 1.17 |
| display | 48 | — | 1 |

## Spacing & Layout

- **Max Width**: 1440px
- **Card Padding**: 16px
- **Element Gap**: 8px
- **Section Gap**: 96px
- **Border Radius**: {'cards': '12px', 'pills': '9999px', 'inputs': '12px', 'buttons': '8px'}

## Layout

The layout is clean and centered within a generous max-width container (approx. 1440px). The header is full-width with a 1px bottom border. The hero area is a simple centered stack comprising a headline, a large input field, and suggestion chips. Body sections are separated by large vertical whitespace (~96px) on the Canvas (#fafafa) background, creating a spacious rhythm. Content grids, such as the 3-column template gallery, are the primary structure for displaying information.

## Imagery

This design uses no decorative imagery. Visuals are strictly confined to user-generated content previews within the Template Cards. These thumbnails are presented as raw, unstyled content inside a 12px rounded container. The page is UI-dominant, with imagery serving only to showcase product output, not to build atmosphere.

## Design Principles

### Do

- Use GeistSans for all text, without exception.
- Apply aggressive negative letter-spacing to headings 24px and larger.
- Adhere strictly to the achromatic palette; all color comes from content, not chrome.
- Use 8px radius for buttons and 12px for cards and inputs.
- Use 1px solid #eaeaea for all visual dividers.
- Differentiate action hierarchy using fills and borders: solid for primary, bordered for secondary, text-only for tertiary.
- Maintain generous whitespace (min. 96px) between content sections.

### Don't

- Do not introduce any saturated colors to the UI chrome.
- Do not use system fonts or other brand fonts.
- Do not use shadows on interactive elements like buttons or inputs; reserve them for cards.
- Do not use any border-radius values other than 6px, 8px, 12px, or 9999px (for pills).
- Do not use gradients or background images.
- Do not use bold (700+) font weights; rely on 600 weight and size for emphasis.
- Do not create dense layouts; prioritize clarity and space.

## Components

### Main Prompt Input

```html
<div style="--color-paper-white:#ffffff;--color-canvas:#fafafa;--color-line:#eaeaea;--color-subtext:#666666;--color-icon:#7d7d7d;--color-ink:#171717;--color-onyx:#000000;--font-geistsans:'Inter',sans-serif;--font-geistmono:'IBM Plex Mono',monospace; background:var(--color-canvas);padding:48px 32px;display:flex;flex-direction:column;align-items:center;gap:24px;font-family:var(--font-geistsans);box-sizing:border-box;width:600px;"><h1 style="font-family:var(--font-geistsans);font-size:32px;font-weight:600;color:var(--color-ink);letter-spacing:-1.28px;line-height:1.17;margin:0;text-align:center;">What do you want to create?</h1><div style="width:100%;background:var(--color-paper-white);border:1px solid var(--color-line);border-radius:12px;padding:16px;box-sizing:border-box;display:flex;flex-direction:column;gap:24px;"><textarea placeholder="Ask v0 to build…" style="font-family:var(--font-geistsans);font-size:16px;font-weight:400;color:var(--color-ink);background:transparent;border:none;outline:none;resize:none;width:100%;min-height:60px;line-height:1.5;color:var(--color-subtext);box-sizing:border-box;">Ask v0 to build…</textarea><div style="display:flex;align-items:center;justify-content:space-between;"><div style="display:flex;align-items:center;gap:6px;padding:4px 10px;border:1px solid var(--color-line);border-radius:9999px;cursor:pointer;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--color-icon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/></svg><span style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);">v0 Max</span><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--color-icon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div><button style="background:var(--color-ink);border:none;border-radius:8px;width:36px;height:36px;display:flex;align-items:center;justify-content:center;cursor:pointer;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-paper-white)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="22"/></svg></button></div></div><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;"><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-subtext);background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 10px;cursor:pointer;display:flex;align-items:center;gap:6px;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--color-icon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg>Contact Form</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-subtext);background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 10px;cursor:pointer;display:flex;align-items:center;gap:6px;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--color-icon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>Image Editor</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-subtext);background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 10px;cursor:pointer;display:flex;align-items:center;gap:6px;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--color-icon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>Mini Game</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-subtext);background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 10px;cursor:pointer;display:flex;align-items:center;gap:6px;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="var(--color-icon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>Finance Calculator</button><button style="background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 8px;cursor:pointer;display:flex;align-items:center;justify-content:center;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--color-icon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg></button></div></div>
```

### Template Filter Pills

```html
<div style="--color-paper-white:#ffffff;--color-canvas:#fafafa;--color-line:#eaeaea;--color-subtext:#666666;--color-icon:#7d7d7d;--color-ink:#171717;--color-onyx:#000000;--font-geistsans:'Inter',sans-serif; background:var(--color-canvas);padding:40px 32px;font-family:var(--font-geistsans);box-sizing:border-box;width:600px;"><div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;"><h2 style="font-family:var(--font-geistsans);font-size:20px;font-weight:600;color:var(--color-ink);letter-spacing:-0.2px;line-height:1.25;margin:0;">Start with a template</h2><div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;"><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid rgba(0,0,0,0.08);border-radius:9999px;padding:6px 14px;cursor:pointer;display:flex;align-items:center;gap:6px;white-space:nowrap;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 3H8l-2 4h12l-2-4z"/></svg>Apps and Games</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid rgba(0,0,0,0.08);border-radius:9999px;padding:6px 14px;cursor:pointer;display:flex;align-items:center;gap:6px;white-space:nowrap;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/></svg>Landing Pages</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid rgba(0,0,0,0.08);border-radius:9999px;padding:6px 14px;cursor:pointer;display:flex;align-items:center;gap:6px;white-space:nowrap;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>Components</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid rgba(0,0,0,0.08);border-radius:9999px;padding:6px 14px;cursor:pointer;display:flex;align-items:center;gap:6px;white-space:nowrap;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>Dashboards</button><a href="#" style="font-family:var(--font-geistsans);font-size:13px;font-weight:500;color:var(--color-ink);text-decoration:none;display:flex;align-items:center;gap:4px;padding:6px 4px;white-space:nowrap;">Browse all<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg></a></div></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;"><div style="background:var(--color-paper-white);border-radius:12px;overflow:hidden;box-shadow:0px 0px 0px 1px rgba(0,0,0,0.08),0px 2px 1px 0px rgba(0,0,0,0.04);cursor:pointer;"><div style="width:100%;height:140px;background:#111111;display:flex;align-items:center;justify-content:center;"><div style="width:40px;height:22px;border:2px solid #ffffff;border-radius:4px;position:relative;"><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:16px;height:8px;border:2px solid #ffffff;border-radius:2px;"></div></div></div><div style="padding:12px;"><div style="font-family:var(--font-geistsans);font-size:13px;font-weight:500;color:var(--color-ink);margin-bottom:6px;">Nano Banana Pro Playground</div><div style="display:flex;align-items:center;justify-content:space-between;"><div style="display:flex;align-items:center;gap:8px;"><span style="font-family:var(--font-geistmono),'IBM Plex Mono',monospace;font-size:10px;color:var(--color-subtext);">👥 5.3K</span><span style="font-size:10px;color:var(--color-icon);">•</span><span style="font-family:var(--font-geistmono),'IBM Plex Mono',monospace;font-size:10px;color:var(--color-subtext);">♡ 617</span></div><span style="font-family:var(--font-geistsans);font-size:11px;color:var(--color-subtext);">Free</span></div></div></div><div style="background:var(--color-paper-white);border-radius:12px;overflow:hidden;box-shadow:0px 0px 0px 1px rgba(0,0,0,0.08),0px 2px 1px 0px rgba(0,0,0,0.04);cursor:pointer;"><div style="width:100%;height:140px;background:#f5f4f0;display:flex;align-items:center;justify-content:center;"><div style="text-align:center;padding:8px;"><div style="font-size:11px;font-weight:600;color:#111;font-family:serif;letter-spacing:-0.3px;">Effortless custom contract</div><div style="font-size:11px;font-weight:600;color:#111;font-family:serif;letter-spacing:-0.3px;">billing by Brillance</div></div></div><div style="padding:12px;"><div style="font-family:var(--font-geistsans);font-size:13px;font-weight:500;color:var(--color-ink);margin-bottom:6px;">Brillance SaaS Landing Page</div><div style="display:flex;align-items:center;justify-content:space-between;"><div style="display:flex;align-items:center;gap:8px;"><span style="font-family:var(--font-geistmono),'IBM Plex Mono',monospace;font-size:10px;color:var(--color-subtext);">👥 12.3K</span><span style="font-size:10px;color:var(--color-icon);">•</span><span style="font-family:var(--font-geistmono),'IBM Plex Mono',monospace;font-size:10px;color:var(--color-subtext);">♡ 1.8K</span></div><span style="font-family:var(--font-geistsans);font-size:11px;color:var(--color-subtext);">Free</span></div></div></div></div></div>
```

### Button Group — Action Hierarchy

```html
<div style="--color-paper-white:#ffffff;--color-canvas:#fafafa;--color-line:#eaeaea;--color-subtext:#666666;--color-icon:#7d7d7d;--color-ink:#171717;--color-onyx:#000000;--font-geistsans:'Inter',sans-serif; background:var(--color-canvas);padding:48px 32px;font-family:var(--font-geistsans);box-sizing:border-box;width:600px;display:flex;flex-direction:column;gap:32px;"><div style="display:flex;flex-direction:column;gap:8px;"><span style="font-size:11px;font-weight:500;color:var(--color-icon);letter-spacing:0.5px;text-transform:uppercase;">Primary Action</span><div style="display:flex;gap:8px;flex-wrap:wrap;"><button style="font-family:var(--font-geistsans);font-size:14px;font-weight:500;color:var(--color-paper-white);background:var(--color-ink);border:none;border-radius:8px;padding:8px 16px;cursor:pointer;">Sign Up</button><button style="font-family:var(--font-geistsans);font-size:14px;font-weight:500;color:var(--color-paper-white);background:var(--color-ink);border:none;border-radius:8px;padding:8px 16px;cursor:pointer;display:flex;align-items:center;gap:6px;">Get Started<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></button></div></div><div style="height:1px;background:var(--color-line);"></div><div style="display:flex;flex-direction:column;gap:8px;"><span style="font-size:11px;font-weight:500;color:var(--color-icon);letter-spacing:0.5px;text-transform:uppercase;">Secondary / Ghost</span><div style="display:flex;gap:8px;flex-wrap:wrap;"><button style="font-family:var(--font-geistsans);font-size:14px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid var(--color-line);border-radius:8px;padding:8px 16px;cursor:pointer;">Sign In</button><button style="font-family:var(--font-geistsans);font-size:14px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid var(--color-line);border-radius:8px;padding:8px 16px;cursor:pointer;display:flex;align-items:center;gap:6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>New Project</button><button style="font-family:var(--font-geistsans);font-size:14px;font-weight:400;color:var(--color-subtext);background:transparent;border:none;border-radius:8px;padding:8px 12px;cursor:pointer;">Learn more</button></div></div><div style="height:1px;background:var(--color-line);"></div><div style="display:flex;flex-direction:column;gap:8px;"><span style="font-size:11px;font-weight:500;color:var(--color-icon);letter-spacing:0.5px;text-transform:uppercase;">Filter Pills</span><div style="display:flex;gap:8px;flex-wrap:wrap;"><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid rgba(0,0,0,0.08);border-radius:9999px;padding:6px 14px;cursor:pointer;">All</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid rgba(0,0,0,0.08);border-radius:9999px;padding:6px 14px;cursor:pointer;">Landing Pages</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid rgba(0,0,0,0.08);border-radius:9999px;padding:6px 14px;cursor:pointer;">Components</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-ink);background:var(--color-paper-white);border:1px solid rgba(0,0,0,0.08);border-radius:9999px;padding:6px 14px;cursor:pointer;">Dashboards</button></div></div><div style="height:1px;background:var(--color-line);"></div><div style="display:flex;flex-direction:column;gap:8px;"><span style="font-size:11px;font-weight:500;color:var(--color-icon);letter-spacing:0.5px;text-transform:uppercase;">Suggestion Chips</span><div style="display:flex;gap:8px;flex-wrap:wrap;"><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-subtext);background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 10px;cursor:pointer;">Contact Form</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-subtext);background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 10px;cursor:pointer;">Image Editor</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-subtext);background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 10px;cursor:pointer;">Mini Game</button><button style="font-family:var(--font-geistsans);font-size:13px;font-weight:400;color:var(--color-subtext);background:transparent;border:1px solid var(--color-line);border-radius:6px;padding:4px 10px;cursor:pointer;">Finance Calculator</button></div></div></div>
```

### Primary CTA Button

Solid Ink (#171717) background with Paper White (#ffffff) text. Font is 14px GeistSans at 500 weight. Padding is ~8px vertically and 12px horizontally, with an 8px border radius.

### Ghost Navigation Link

Transparent background with Subtext (#666666) text. No border in its default state. Font is 14px GeistSans at 400 weight.

### Prompt Suggestion Chip

Transparent background with a 1px Line (#eaeaea) border. Text is Subtext (#666666) at ~13px. Padding is 4px vertically and 8px horizontally, with a 6px border radius.

### Filter Pill Button

A pill-shaped button (9999px radius) with a Paper White (#ffffff) background and Ink (#171717) text. Features a faint 1px border of `rgba(0, 0, 0, 0.08)`.

### Main Prompt Input

A large input field with a 12px border radius and a subtle 1px Line (#eaeaea) border. Placeholder text is Subtext (#666666). On focus, it gets a subtle outer glow.

### Header Divider

A full-width 1px solid border using the Line color (#eaeaea).

## Similar Design Systems

- {'why': 'Shares the high-contrast, black/white/gray palette and surgically precise typography.', 'business': 'Linear'}
- {'why': 'Similar utilitarian, developer-centric aesthetic with a focus on functional components over decoration.', 'business': 'GitHub'}
- {'why': 'Extreme typography-first approach on a minimal, monochrome canvas.', 'business': 'Read.cv'}
- {'why': 'Clean, high-contrast UI with a similar approach to minimal buttons and inputs.', 'business': 'Height'}

## Agent Prompt Guide

### Quick Color Reference
- **Page Background**: `#fafafa` (Canvas)
- **Primary Text**: `#171717` (Ink)
- **Subtle Text**: `#666666` (Subtext)
- **Border**: `#eaeaea` (Line)
- **CTA Background**: `#171717` (Ink)
- **CTA Text**: `#ffffff` (Paper White)

### Example Component Prompts
1. **Primary Button:** `Create a button with 'Get Started' text. It needs a #171717 background, #FFFFFF text, 8px corner radius, and font size 14px.`
2. **Display Headline:** `Generate a headline 'Start with a template'. Use GeistSans 32px weight 600, color #171717, and letter-spacing of -1.28px.`
3. **Template Card:** `Design a card container with a 12px border-radius, a white background, and a box-shadow of '0px 0px 0px 1px rgba(0,0,0,0.08), 0px 2px 1px 0px rgba(0,0,0,0.04)'.`
