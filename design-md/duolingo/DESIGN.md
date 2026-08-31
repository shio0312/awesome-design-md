# Duolingo — Design System

> **North Star**: Playful classroom mascot on white paper
> **Theme**: light
> **Source**: https://duolingo.com
> **Refero Style**: https://styles.refero.design/style/7088d695-362b-4e09-b325-fa8136d4f350
> **Synced**: 2026-09-01

## Overview

Duolingo's interface treats the page like a children's storybook: white paper canvas, chubby rounded display type, and a single saturated green that reads as 'correct answer' the moment it appears. Body copy stays calm in mid-gray so the green and its accent blue can do all the emotional work — green for progress and headings, blue for interactive links and secondary actions. Components are pill-shaped or chunky-rounded with thick 2px borders in black or color, giving every button the feel of a sticker pressed onto the page rather than a flat UI control.

## Color Palette

- **Eager Green**: `#58cc02` — Green text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Storybook Green**: `#d7ffb8` — Soft highlight wash on light surfaces, subtle background tints behind footer navigation labels [brand]
- **Spark Blue**: `#1cb0f6` — Blue text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [accent]
- **Fresh Leaf**: `#a5ed6e` — Green text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [accent]
- **Night Ink**: `#000437` — Violet text accent for links, tags, and emphasized short phrases. [accent]
- **Paper White**: `#ffffff` — Page canvas, card surfaces, button text on green/dark fills [neutral]
- **Charcoal**: `#4b4b4b` — Hero headings and primary body copy — the workhorse dark text that lets colored headings stand out [neutral]
- **Pencil Gray**: `#777777` — Muted body paragraphs, secondary descriptive text — recedes so colored elements lead [neutral]
- **Faded Gray**: `#afafaf` — Disabled or low-emphasis nav labels and button borders [neutral]

## Typography

- **feather**
- **duolingo-sans**
- **duolingo-sans**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 13 | — | 1.23 |
| nav-label | 15 | — | 1.33 |
| body | 17 | — | 1.18 |
| subheading | 19 | — | 1.4 |
| heading-sm | 32 | — | 1.2 |
| heading | 48 | — | 1.2 |
| display | 64 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16-24px
- **Element Gap**: 12px
- **Section Gap**: 80-120px
- **Border Radius**: {'links': '12px', 'buttons': '12px', 'nav-items': '12px'}

## Layout

Single-column full-width sections stacked vertically, each ~800-900px tall. Max content width ~1200px centered. Sections alternate text-left/illustration-right with generous vertical breathing room (80-120px between sections). No card grids or multi-column feature layouts — each section is a single text block paired with one illustration. Navigation is a minimal top bar with logo and language selector, reappearing as a sticky bar between sections. Footer is a full-bleed green band spanning the page width. The rhythm is editorial: headline, paragraph, CTA, illustration, repeat.

## Surfaces / Elevation

- **Paper White**
- **Storybook Green**
- **Eager Green**
- **Night Ink**

## Imagery

Illustration-driven storybook language: flat 2D mascot characters (the owl Duo and diverse human figures) with rounded geometric shapes, bold black outlines, and a secondary palette of pink, purple, yellow, orange, and blue that never appears in the UI chrome itself. Illustrations sit beside text in the right half of each section on pure white, no containers or backgrounds. Photography is absent — the characters are the visual content. Iconography uses thick outlined strokes consistent with the mascot style. Image density is moderate: each section gets one large character illustration, leaving the rest of the page to typography and whitespace.

## Design Principles

### Do

- Use #58cc02 for any heading or CTA that needs to read as 'progress' or 'go' — it is the only saturated color allowed on large display text.
- Set display headlines at 48-64px in feather 700 with -0.0200em letter-spacing; this rounded weight is the brand voice.
- Give every button and pill a 12px border-radius and pair it with a 2px solid border in #afafaf or color — outlined buttons are first-class citizens, not a fallback.
- Reserve uppercase at 15px with 0.0530em tracking for nav labels and language pills; never apply it to body copy.
- Keep body text in #777777 at 17px/500 — mid-gray is the default so colored elements can lead.
- Use #1cb0f6 (Spark Blue) exclusively for interactive links and outlined secondary CTAs; it is the 'curious' companion to the green.
- Build sections as white-on-white with illustrations floating beside text; introduce #58cc02 only at the footer band and within display headings.

### Don't

- Don't put colored text in body paragraphs — body stays in #777777 or #4b4b4b so the green headlines own the page.
- Don't use sharp corners; even small tags and pills use 12px radius.
- Don't introduce gradients, shadows, or glass effects — Duolingo's surfaces are flat sticker-like fills with thick borders.
- Don't use feather at sizes below 48px; it is a display face only. Subheadings 19-32px use duolingo-sans 700.
- Don't place CTA buttons on colored backgrounds without testing contrast — green on green or blue on green will disappear.
- Don't apply the secondary palette (pink, purple, mascot illustration colors) to UI chrome; those colors live only inside character art.
- Don't stretch the green to small UI text; #58cc02 is for headings, CTA fills, and the footer band, not body or link text.

## Components

### Primary CTA Button

Fill #58cc02, white text, duolingo-sans 700 at 15px uppercase with 0.0530em tracking, 12px border-radius, 16px horizontal padding. No border — color alone carries the button. Sits directly on white canvas.

### Outlined Account Button

Transparent fill, text in #1cb0f6, duolingo-sans 700 at 14px, 12px border-radius, 16px horizontal padding, 2px solid border in #afafaf. Pairs with the green CTA as a calm ghost alternative.

### Nav Language Pill

Transparent fill, text in #777777 at 15px uppercase with 0.0530em tracking, 12px border-radius, 10px vertical and 16px horizontal padding, 2px solid border in #afafaf. Behaves like a sticker tag.

### Section Headline

feather 700 at 48-64px, line-height 1.2, letter-spacing -0.0200em, color #58cc02. The signature voice of the brand — large, rounded, unmistakably green.

### Hero Headline

duolingo-sans 700 at 32px, color #4b4b4b (Charcoal). Stays neutral so the green CTA below it carries the color weight.

### Body Paragraph

duolingo-sans 500 at 17px, line-height 1.18, color #777777 (Pencil Gray). Mid-gray intentionally recedes so colored headlines dominate.

### Footer Background

#58cc02 fill, white and #d7ffb8 text labels, generous 48px vertical padding, contains language grid and site links. The colored surface that anchors the page.

### Footer Link Item

duolingo-sans at small sizes, color #a5ed6 (Fresh Leaf) for links, white for section headers. 8px margin between items, stacked vertically.

### Language Flag Pill

Circular flag emoji + language name in duolingo-sans 700 at 15px uppercase, inline arrangement with 10-12px gaps, no background fill.

### App Store Badge

Black rectangular badge with white icon and duolingo-sans text, 4b4b4b text color. Functions as a visual anchor on white sections.

### Section Feature Illustration

Flat colored mascot characters placed in the right half of each section, no container or background. Illustrations carry the secondary palette (pink, purple, yellow, orange) while UI stays green/blue.

## Similar Design Systems

- {'why': 'Same mascot-led illustration system with thick outlines and a single saturated accent color against white canvas', 'business': 'Headspace'}
- {'why': 'Light-mode language-learning landing pages with rounded display type and green as the primary CTA color', 'business': 'Babbel'}
- {'why': 'Flat rounded mascots, playful rounded display headings, and bold sticker-style buttons with thick borders', 'business': 'Khan Academy Kids'}
- {'why': 'Minimal white-canvas marketing pages with one dominant green and casual rounded display typography', 'business': 'Memrise'}
- {'why': 'Playful rounded mascot illustrations, thick outlined UI components, and bright single-accent CTAs on white backgrounds', 'business': 'ClassDojo'}

## Agent Prompt Guide

Quick Color Reference:
- text (heading): #58cc02
- text (body): #777777
- text (hero/heading dark): #4b4b4b
- background (page): #ffffff
- background (footer band): #58cc02
- border (outlined button): #afafaf
- accent (interactive link): #1cb0f6
- primary action: no distinct CTA color

Example Component Prompts:
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.
3. Section Headline: feather 700 at 48px, line-height 1.2, letter-spacing -0.0200em, color #58cc02. Used for 'free. fun. effective.' and similar section titles.
5. Body Paragraph: duolingo-sans 500 at 17px, line-height 1.18, color #777777, max-width ~480px to keep reading comfortable.
