# Valo — Design System

> **North Star**: noir observatory at midnight — weight-300 typography floats on pure black while a single teal-violet gradient passes through like a laser line across the room.
> **Theme**: dark
> **Source**: https://www.valohealth.com
> **Refero Style**: https://styles.refero.design/style/f65c3888-2eb3-41a1-87b3-f410b667097e
> **Synced**: 2026-09-01

## Overview

Valo runs on a noir observatory aesthetic: deep-black canvas, a single custom serif-less voice at whisper weight (300), and one luminous blue-teal-violet gradient used as deliberate punctuation rather than decoration. Typography does the heavy lifting — 100px display headlines with tight negative tracking feel like illuminated ink on obsidian, while the rest of the interface stays nearly invisible. The gradient appears in exactly three roles: a single accent word inside a headline, a thin floating ring/torus visual, and a wash at the page foot — never as a button fill or panel background. Components are flat, hairline-bordered, and borderless where possible; interaction is signaled by circular arrow buttons and numbered sequencing, not by color or shadow. Every screen should feel like a page torn from a dark scientific monograph: quiet, confident, with one moment of light.

## Color Palette

- **Void**: `#000000` — Page canvas, hero background, all primary surface area. Sets the dark-stage tone for every screen [neutral]
- **Bone**: `#e5e7eb` — Hairline borders, dividers, and muted secondary text. The workhorse neutral that defines edges without adding visual weight [neutral]
- **Paper**: `#ffffff` — Primary headings, body text, nav links, and icon strokes. Maximum contrast against Void for clear information hierarchy [neutral]
- **Graphite**: `#4d4d4d` — Subtle nav borders and disabled/inactive state lines. Sits between Void and Bone for low-emphasis structural lines [neutral]
- **Spectrum Wash**: `#1b66f8` — Hero accent gradient — applied to a single headline word and the floating torus visual. Cool blue midpoint of the signature violet→blue→teal→lavender ramp [brand]
- **Deep Field**: `#1e233c` — Footer band gradient origin — near-black indigo transitioning into brand blue. Defines the bottom-of-page atmospheric shift [accent]
- **Atmospheric Fade**: `#1951a2` — Secondary gradient — blue-to-mint wash used in supporting visuals and transitional bands. Cooler, more subdued than the hero spectrum [accent]

## Typography

- **Valo**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.4 |
| body | 15 | — | 1.63 |
| subheading | 18 | — | 1.4 |
| heading-sm | 24 | — | 1.33 |
| heading | 38 | — | 1.2 |
| heading-lg | 60 | — | 1.2 |
| display | 100 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Element Gap**: 18-20px
- **Section Gap**: 45px
- **Border Radius**: {'icons': '9999px', 'links': '9999px', 'buttons': '9999px'}

## Layout

Max-width 1200px centered content column on a full-bleed #000000 canvas. Hero is left-aligned: large display headline (100px) over a 15px subhead paragraph, all flush to the content column's left edge with generous left padding. Below the hero, sections alternate between text-only blocks and paired text+visual layouts — the gradient torus sits to the left of a two-column content block containing subheading, numbered items, and a circle-arrow link. Section rhythm is set by 45px+ vertical gaps and the occasional hairline divider; no banding colors, no card grids. Navigation is a single top bar with logo left and links right. The page closes with a full-bleed gradient footer band containing footer links — the only moment the canvas shifts from pure black to color.

## Surfaces / Elevation

- **Void Canvas**
- **Gradient Footer Band**

## Imagery

Imagery is minimal and geometric: a single large gradient-stroke torus/ring floats on the hero of feature sections, and a full-bleed gradient band closes the page. No photography, no illustration beyond the ring, no product screenshots. The gradient itself is the visual content — a teal-to-blue-to-violet-to-lavender sweep used as both text fill (on one headline word) and as a thin stroke (on the ring). Iconography is restricted to a single white right-arrow glyph inside circular buttons. Every other visual element is type, hairline, or empty canvas.

## Design Principles

### Do

- Set all display and body text in Valo weight 300 — the whisper-weight is the brand voice, not a fallback
- Apply the Spectrum Wash gradient to exactly one word per headline maximum — chromatic type is punctuation, not paint
- Use 9999px radius for every interactive element (buttons, link icons, tags) — circles are the only geometric interaction shape in the system
- Set display headlines at -2.7px letter-spacing (100px) and -0.78px (60px) — the negative tracking tightens large type to feel carved rather than typed
- Use 0.1em letter-spacing on all small-caps labels, nav items, and numbered prefixes — the wide tracking signals scientific precision
- Anchor every section with the uppercase Section Label Tag at 10px — the typographic flag gives pages a magazine-like structure
- Use the 01, 02 numbered pattern for sequential content blocks — sequencing reads as methodical, fitting the discovery narrative

### Don't

- Don't use weight 700 for body copy or long-form paragraphs — the voice is light; 700 belongs to subheadings and micro-labels only
- Don't apply the Spectrum Wash gradient to button backgrounds, panel fills, or large-area surfaces — it belongs on text accents, ring strokes, and the footer band only
- Don't introduce card surfaces, drop shadows, or elevated panels — the canvas stays flat; depth comes from type scale, not from z-axis
- Don't use borders thicker than 1px — the entire system runs on hairlines (Bone at 1px); anything heavier breaks the editorial register
- Don't add a chromatic brand color outside the violet→blue→teal→lavender ramp — the system is intentionally near-monochrome with one gradient family
- Don't center body text or multi-line content — the layout is left-aligned and the measure should align with the headline edge
- Don't use stock photography, emoji, or decorative illustration — visuals are limited to the gradient torus and the footer wash; everything else is type and whitespace

## Components

### Top Navigation Bar

Horizontal bar on Void (#000000) background. Wordmark "Valo" at 24px weight 400 Paper (#ffffff) flush left. Nav items (Approach, Company, Partnership, News & Insights, Contact) right-aligned at 13px weight 400 Paper with 27px horizontal spacing. 7px top/bottom padding. No background fill, no border below — the negative space defines the bar.

### Hero Display Headline

100px Valo weight 300 Paper (#ffffff), line-height 1.0, letter-spacing -2.7px. The word "aha" is the only chromatic moment — rendered in the Spectrum Wash gradient (linear 270deg violet→blue→teal→lavender) as inline text. No background, no border. Sets the editorial tone.

### Hero Subhead Paragraph

15px Valo weight 400 Bone (#e5e7eb), line-height 1.63. Max-width constrained to align with headline measure. No label, no link, no decoration — the paragraph is the quiet second beat.

### Section Label Tag

10px Valo weight 400 Paper (#ffffff), letter-spacing 1.0px (0.1em), uppercase. Sits above section content with 18px top padding. Functions as a typographic flag, not a button — no background, no border.

### Gradient Torus Visual

Large thin-stroke ring (approximately 400px diameter) rendered with the Spectrum Wash gradient applied as a stroke. Floats on Void canvas to the left of paired content. The only saturated-color shape on the page — its presence is the page's focal anchor.

### Numbered Content Block

Two-column structure. Left column: 13px Valo weight 400 Bone (#e5e7eb) numeral ("01", "02") at 0.1em tracking. Right column: 18px Valo weight 700 Paper subheading, followed by 15px weight 400 Bone body at line-height 1.63. 14px gap between subheading and body. 23px vertical gap between numbered items.

### Circle Arrow Link Button

48px circular button (9999px radius) with 1px Bone (#e5e7eb) border on Void background. White right-arrow icon (→) centered inside. Paired with a 18px Valo weight 400 Paper text link to its right with 20px gap. The circle is the system's only geometric interaction primitive — used wherever a click is invited.

### Content Section Heading

38px Valo weight 300 Paper (#ffffff), line-height 1.2, letter-spacing -0.49px. Left-aligned, sits 36-45px below the preceding section. No underline, no background — weight 300 is the only emphasis needed.

### Gradient Footer Band

Full-bleed band with the Atmospheric Fade gradient (linear 90deg #1951a2 → #70dab4) transitioning into the Spectrum Wash tones. Contains the Valo wordmark (24px Paper, left) and a row of footer links (13px Paper, right) at 20px gaps: Privacy Policy, Terms & Conditions, Cookie Consent, Preferences, Twitter, LinkedIn, © line. No top or bottom border — the gradient itself defines the zone.

### Hairline Section Divider

1px solid Bone (#e5e7eb) line, full content-width. No other styling. Used sparingly — most sections breathe on whitespace alone.

## Similar Design Systems

- {'why': "Same dark-canvas + weight-light typography + single-hue accent restraint — Linear's dark mode uses one purple accent against near-black surfaces with whisper-weight display type", 'business': 'Linear'}
- {'why': 'Identical minimalist dark aesthetic with a single chromatic gradient moment, ultra-thin display headlines, and the same flat-no-elevation philosophy', 'business': 'Vercel'}
- {'why': 'Editorial dark-mode sensibility with oversized display type set tight, generous negative space, and circular interaction primitives', 'business': 'Arc Browser'}
- {'why': 'Fellow AI-bio company with a comparable scientific-monograph-on-black visual register — large light-weight type, restrained color, and torus/loop motifs in hero illustrations', 'business': 'Recursion'}
- {'why': 'Shares the deep-black canvas, sparse whitespace, and weight-300-400 display typography that reads as engineering-precise rather than marketing-loud', 'business': 'SpaceX'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #ffffff (Paper)
- background: #000000 (Void)
- border: #e5e7eb (Bone), 1px
- accent gradient: linear-gradient(270deg, rgb(158,61,178), rgb(27,102,248), rgb(36,218,217), rgb(179,198,232))
- footer gradient: linear-gradient(90deg, rgb(30,35,60), rgb(10,64,153)) transitioning to the teal-mint wash
- primary action: no distinct CTA color

**Example Component Prompts**

1. Build a hero section on #000000. Headline at 100px Valo weight 300, #ffffff, line-height 1.0, letter-spacing -2.7px. Render the single word "aha" inline using the Spectrum Wash gradient as the text color. Below: 15px Valo weight 400, #e5e7eb, line-height 1.63, max-width matching the headline measure. No buttons, no images.

2. Build a paired text-and-visual section. Left: a 400px-diameter thin ring (2px stroke) filled with the Spectrum Wash gradient as stroke color, centered vertically. Right: a 38px Valo weight 300 #ffffff section heading at line-height 1.2, followed by a 15px #e5e7eb intro paragraph, then a numbered list (01, 02) at 13px #e5e7eb numerals (0.1em tracking) paired with 18px weight 700 #ffffff subheadings and 15px weight 400 #e5e7eb bodies. Close with a 48px circular ghost button (1px #e5e7eb border, white → arrow icon) paired with an 18px #ffffff text link.

3. Build a full-bleed footer band. Background: linear-gradient(90deg, #1e233c, #0a4099) blending into a teal-violet wash. Left: 24px Valo weight 400 #ffffff wordmark. Right: a row of 13px Valo weight 400 #ffffff links at 20px gaps (Privacy Policy, Terms, Cookie Consent, Preferences, Twitter, LinkedIn, © 2026 Valo Health). No top border — the gradient defines the zone.

4. Build a section label. 10px Valo weight 400 #ffffff, uppercase, letter-spacing 1.0px. Place 36px above its parent content block. No background, no border.

5. Build a top navigation bar. Background: #000000 (transparent over canvas). Left: 24px Valo weight 400 #ffffff "Valo" wordmark. Right: 5 nav items at 13px Valo weight 400 #ffffff with 27px horizontal gaps and 7px top/bottom padding. No background fill, no border-bottom.

## Gradient System

Three gradients form the system's chromatic vocabulary, and they share a single hue family (violet → blue → teal → mint → lavender). Usage is strictly rationed: the Spectrum Wash (#9e3db2 → #1b66f8 → #24dad9 → #b3c6e8) lives on exactly one word per page, on the torus stroke, and as the climax of the footer band. The Deep Field (#1e233c → #0a4099) is the footer's opening — near-black indigo easing into brand blue. The Atmospheric Fade (#1951a2 → #70dab4) is a secondary wash for transitional moments. Never stack gradients. Never apply gradients to button fills or panel backgrounds. Treat each gradient use as a budgeted moment — too many, and the system loses its editorial restraint.
