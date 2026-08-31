# Resend — Design System

> **North Star**: black velvet with violet neon
> **Theme**: dark
> **Source**: https://resend.com
> **Refero Style**: https://styles.refero.design/style/0d914ef0-fa84-4c60-a9aa-cef0b5eb6e5d
> **Synced**: 2026-09-01

## Overview

Resend lives in a near-total darkness — pure black canvas, hairline graphite borders, and white-on-black typography that feels like reading text printed on matte glass. The hero is anti-decorative: a single large serif headline at 96px Domaine next to a 3D black cube, with no gradient wash and no marketing illustration. The brand mark is a tight violet (#9281f7) that appears in email-address strings, status icons, and code samples — never on buttons. A monospaced font (Commit Mono) carries the developer identity through every code block, badge, and inline label, making the page read like a terminal wrapped in a luxury interface. Components are sharp-cornered or gently rounded (6px / 16px), low-elevation, and rely on 1px borders rather than shadows to separate layers. Motion is restrained but expressive: fade-and-slide hero text, subtle WebGL rotation on the hero cube, and short 150ms ease-out transitions on hover.

## Color Palette

- **Void Black**: `#000000` — Page background, card surfaces, overlay scrims — the entire canvas [neutral]
- **Graphite Hairline**: `#292d30` — 1px borders on cards, inputs, buttons, code blocks, dividers — defines every layer separation [neutral]
- **White**: `#ffffff` — Primary headings, hero text, button labels, icon fills on dark surfaces [neutral]
- **Bone White**: `#f0f0f0` — Body text, secondary headings, stroke outlines on icons — the primary reading color [neutral]
- **Ash Gray**: `#a1a4a5` — Muted body text, badge labels, icon strokes — third-tier text and metadata [neutral]
- **Smoke Gray**: `#abafb4` — Link color, inactive button text, supporting captions — fourth-tier text [neutral]
- **Iron**: `#6e727a` — Subtle decorative strokes, disabled states, low-emphasis borders [neutral]
- **Charcoal**: `#464a4d` — Inline code text, muted labels — text that should disappear into the surface [neutral]
- **Iris Violet**: `#9281f7` — Violet text accent for links, tags, and emphasized short phrases; Diagonal violet-to-magenta gradient on icon containers and brand badges [brand]
- **Iris Violet Glow**: `#baa7ff` — Violet text accent for links, tags, and emphasized short phrases [brand]
- **Signal Blue**: `#3b9eff` — Blue action color for filled buttons, selected navigation states, and focused conversion moments. [accent]
- **Sky Blue**: `#70b8ff` — Blue text accent for links, tags, and emphasized short phrases [accent]
- **Pulse Green**: `#3ad389` — Green text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Alarm Red**: `#ff9592` — Red text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Crimson**: `#ff6465` — Red wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]
- **Amber**: `#ffca16` — Yellow text accent for links, tags, and emphasized short phrases. Use as a supporting accent, not as a status color [accent]
- **Amber Glow**: `#ffd60a` — Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]
- **Surface Gradient**: `#0b0e14` — Subtle card-to-canvas surface lift — used in edge fades and elevated panels [neutral]

## Typography

- **Inter**
- **Domaine**
- **aBC Favorit**
- **Commit Mono**
- **Helvetica**
- **-apple-system**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.33 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1 |
| heading-sm | 24 | — | 1.5 |
| heading | 56 | — | 1.2 |
| heading-lg | 77 | — | 1 |
| display | 96 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 16px
- **Section Gap**: 96px
- **Border Radius**: {'cards': '16px', 'badges': '6px', 'inputs': '6px', 'buttons': '6px', 'large-panels': '24px'}

## Surfaces / Elevation

- **Void**
- **Graphite**
- **Surface Lift**
- **Backdrop Blur**

## Imagery

Imagery is almost entirely WebGL-rendered 3D objects (black cube in hero, rotating geometric forms) and inline product UI screenshots shown inside dark code windows. No photography, no illustrations, no lifestyle imagery. Logos in the trust bar are inline SVGs at native colors. Icons are 1px-1.5px stroke outlines in #f0f0f0 or #a1a4a5. The visual language is: black canvas, 3D object as hero anchor, dark code windows as product proof, white SVG logos as social proof. Nothing decorative — every visual element is either structural (cube) or demonstrative (code window, logo).

## Design Principles

### Do

- Use pure #000000 as the page canvas — never off-black or tinted dark grays for the background.
- Separate all UI layers with 1px borders in #292d30, not shadows. Cards, inputs, code blocks all rely on hairline borders against the black canvas.
- Use Commit Mono for any code, email address, or developer-facing string. Keep Inter for prose and UI chrome.
- Keep buttons ghost/outlined: transparent fill, 1px border, white text. Never use a filled colorful button as the primary CTA.
- Use 6px radius for buttons, badges, inputs. Use 16px radius for cards and code windows. Never mix — the radius scale is two values.
- Let Iris Violet (#9281f7) mark code strings and developer identifiers. It is the only brand color and should feel like syntax highlighting, not decoration.
- Apply tight -0.05em letter-spacing at 56px display sizes and -0.01em at 96px hero sizes. The compressed tracking is what makes the headlines feel confident.

### Don't

- Don't add gradients, glows, or chromatic washes to the hero or section backgrounds. The canvas is flat black.
- Don't use filled accent-color buttons (blue, violet, green) as primary actions. Buttons stay ghost or white-text-on-black.
- Don't use multiple border radii on a single surface. Cards are 16px, buttons/badges/inputs are 6px — pick one per component.
- Don't introduce colored card backgrounds. Cards sit on black with hairline borders; no #292d30 fills.
- Don't use shadows for elevation. The design relies on 1px borders and subtle backdrop blurs, not drop shadows.
- Don't pair Iris Violet with large type as a decorative heading color. It belongs to code and developer identifiers only.
- Don't break the monochrome-with-one-violet discipline by adding multiple accent hues to UI chrome. The status colors (green, blue, red, amber) are reserved for data/status indicators.

## Components

### Primary Button (Ghost on Black)

Transparent background, 1px border in #292d30, white text (#ffffff), 6px radius, 12px 16px padding. Hover increases border opacity to white. This is the signature button — never filled, never colorful.

### Nav Link Button

Transparent background, no border, text color #f0f0f0 at 14px Inter weight 400, 0px padding. Underline or color shift on hover to #ffffff.

### Text Link with Chevron

No background, no border, white or #f0f0f0 text at 16px Inter, trailing chevron icon in same color. Restrained, terminal-like.

### Hero Announcement Pill

Transparent fill, 1px border in #292d30, #f0f0f0 text at 14px Inter, 9999px (pill) radius, 6px 12px padding. Small chromatic accent chevron.

### Section Card

Black background (#000000), 1px border in #292d30, 16px radius, 32px padding, no shadow. Cards rely on the border to separate from the black canvas.

### Testimonial Card

Black background, 1px #292d30 border, 16px radius, 24px padding. Contains quoted text at 16px Inter, avatar (32px circle), name at 14px weight 500 in #f0f0f0, role/title in #a1a4a5.

### Code Block / Terminal Window

Black background, 1px #292d30 border, 16px radius, Commit Mono at 12-14px. Syntax highlighting uses #9281f7 for strings/keywords, #3b9eff for filenames, #3ad389 for success values, #ff9592 for errors. Optional traffic-light dots in top-left for terminal aesthetic.

### Logo Grid

Inline-display logos at their native colors on black canvas, centered in a 4-column grid with 60px row gap. No card wrappers, no labels — just the marks breathing against black.

### Status Indicator Dot

2-3px diameter filled dot, no border, paired with label text in Commit Mono. Colors map to semantics: #3ad389 delivered, #70b8ff opened, #baa7ff clicked, #ff9592 bounced, #ffca16 complained.

### Email Address Badge

No background, Commit Mono at 12-14px, text color #9281f7 (Iris Violet). The violet-on-black makes email identifiers the most readable code element — a deliberate developer-UX choice.

### Icon Container

32x32 or 48x48 rounded square (16px radius), subtle gradient fill (oklab violet→magenta), white or violet stroke icon inside. Creates the only chromatic surface on the page.

### 3D Hero Cube

Full-opacity black cube with subtle edge highlights in #292d30, rotating slowly. No glow, no color — a sculptural object that anchors the right side of the hero against the black canvas.

### Footer Link Row

Two text links ('Privacy', 'Terms') at 14px Inter in #a1a4a5, separated by space, no decorative elements. Footer is intentionally minimal — no logo, no columns.

## Similar Design Systems

- {'why': 'Same black-canvas, hairline-border aesthetic with restrained chromatic accents and sharp typography', 'business': 'Linear'}
- {'why': 'Near-identical pure-black backgrounds with white typography and minimal border-based elevation', 'business': 'Vercel'}
- {'why': 'Dark-mode developer-tool identity with monospaced code emphasis and single-accent palette', 'business': 'Plaid'}
- {'why': 'Black canvas with terminal-style code windows as the primary product showcase', 'business': 'Railway'}
- {'why': 'Editorially confident display type on black with hairline borders and ghost buttons', 'business': 'Stripe (dark mode)'}

## Agent Prompt Guide

Quick Color Reference:
- text/heading: #ffffff
- text/body: #f0f0f0
- text/muted: #a1a4a5
- background/canvas: #000000
- border/hairline: #292d30
- accent/code: #9281f7
- primary action: #3b9eff (filled action)

3-5 Example Component Prompts:

1. Create a section headline: 'Integrate tonight' at 56px aBCFavorit weight 400, color #ffffff, letter-spacing -2.8px, line-height 1.2. Below it, body copy at 18px Inter weight 400, color #a1a4a5. Section sits on a #000000 canvas with no border.

2. Create a code terminal window: #000000 background, 1px border in #292d30, 16px radius, padding 24px. Content in Commit Mono at 14px. Email address strings colored #9281f7, keywords colored #f0f0f0, success values colored #3ad389. Optional 3 traffic-light dots (8px circles) in top-left.

3. Create a navigation bar: transparent background, Resend wordmark logo on left (white), nav items ('Features', 'Company', 'Resources') in Inter 14px weight 400, color #f0f0f0. On the right, a 'Get started' button — transparent fill, 1px border in #292d30, white text, 6px radius, 8px 16px padding. The bar sits on #000000 with no separator.

4. Create a testimonial card: #000000 background, 1px border in #292d30, 16px radius, 32px padding. Quote text in Inter 16px weight 400, color #f0f0f0. Below: 32px circular avatar, name in Inter 14px weight 500 #f0f0f0, role/title in #a1a4a5. No shadow.

5. Create a status indicator row: inline pill with a 2px circle dot in #3ad389 followed by 'Delivered' label in Commit Mono 12px, color #a1a4a5. Dot indicates email event status. No background, no border, sits inline within a dark code window.
