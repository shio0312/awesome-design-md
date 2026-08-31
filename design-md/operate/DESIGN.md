# Operate — Design System

> **North Star**: Botanist's data terminal
> **Theme**: light
> **Source**: https://operate.so
> **Refero Style**: https://styles.refero.design/style/f682f0ea-632d-4d09-bfdf-6a43f5e5a7d8
> **Synced**: 2026-09-01

## Overview

Operate reads like a research instrument placed on a herbarium paper: a muted green-gray canvas hosts data plots, dotted timelines, and axis-labeled diagrams as if the page itself were a botanical scatter chart. Typography is small-set and tight-tracked, with one decorative all-caps face (cinetype) reserved for axis labels, tags, and metadata — the effect is scientific, not promotional. Color is almost entirely a mono-green family: dark forest text on a sage paper background, with a single soft mint (#85c093) for the only filled action and occasional deep-emerald (#007010) for links and borders. Components are flat and hairlined: 4px and 12px radii, 0.5px inset borders instead of drop shadows, and almost no elevation. Density is compact and information-first — the page behaves like a control panel where whitespace is a measured gap, not a luxury.

## Color Palette

- **Forest Ink**: `#09352e` — Primary text, icons, and chart strokes — the load-bearing dark color. Reads near-black but carries a cool green undertone that ties the monochrome system together [neutral]
- **Bone White**: `#ffffff` — Card surfaces, data point fills, and reverse text on dark blocks [neutral]
- **Sage Paper**: `#e0e0e0` — Page canvas and large background fields. A green-tinted light gray that gives the whole surface its herbarium character [neutral]
- **Ash Gray**: `#e5e5e5` — Alternate surface tone for nested blocks, inset panels, and subtle differentiation beneath cards [neutral]
- **Muted Sage**: `#77aa83` — Soft fill washes, scatter plot halos, and decorative surface tints that sit behind darker data marks [neutral]
- **Lichen**: `#cad3d2` — Hairline borders, dotted gridlines, and chart axes. The structural line color when a neutral needs to be present without competing with text [neutral]
- **Slate Smoke**: `#6c7a79` — Secondary metadata, icon strokes, and caption text where the body tone is too heavy [neutral]
- **Charcoal Bark**: `#29211e` — Deep text, heavy borders, and dark surface blocks. Slightly warm-neutral, used for the rare dark panel and strong dividers [neutral]
- **Moss**: `#85c093` — The single filled action color — primary buttons, active state fills, and the rare chromatic surface. A soft, slightly desaturated mint that does not shout against the sage canvas [brand]
- **Deep Fern**: `#007010` — Green text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Pine**: `#117025` — Green text accent for links, tags, and emphasized short phrases. Do not promote it to the primary CTA color [brand]
- **Emerald**: `#008023` — Alternate data-mark fill and emphasis backgrounds, used on scatter plot points and callout chips [brand]
- **Indigo Accent**: `#433787` — A single chromatic exception — used on one special link or annotation to break the green-only system. Employ rarely; treat as a punctuation mark, not a palette member [accent]

## Typography

- **denim**
- **muoto**
- **cinetype**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.38 |
| body | 14 | — | 1.5 |
| body-lg | 16 | — | 1.44 |
| subheading | 18 | — | 1.4 |
| heading-sm | 20 | — | 1.35 |
| heading | 32 | — | 1.17 |
| display | 48 | — | 1.11 |

## Spacing & Layout

- **Max Width**: 1280px
- **Card Padding**: 20px
- **Element Gap**: 8px
- **Section Gap**: 64px
- **Border Radius**: {'tags': '4px', 'cards': '12px', 'buttons': '12px', 'hero-blocks': '24px', 'large-panels': '18px'}

## Layout

The page is a full-bleed sage canvas with no strict container — content sits within an implied 1280px wide working area, but data elements (scatter points, axis labels) are allowed to drift to the canvas edges. The hero is a single oversized scatter plot / timeline that occupies most of the viewport, with a small info card floating in the upper-right quadrant and a round 'What's New?' chip pinned to the lower-left. Sections are separated by hairlines rather than background-color changes, and each section carries bracket-style axis labels at its top and bottom margins ('[ Chaos ]' left, '[ Clarity ]' right). Vertical rhythm is 64px between sections, 8px between inline elements, 20px inside cards. The layout reads as a single instrument panel rather than a stacked page of bands.

## Surfaces / Elevation

- **Sage Paper Canvas**
- **Ash Block**
- **Bone Card**
- **Charcoal Block**

**Shadow tokens:**

## Imagery

Imagery is minimal and scientific — no lifestyle photography, no product screenshots, no human faces. The dominant visual is data-as-illustration: scatter plots of circles, timelines of connected dots, axis brackets, and small hand-drawn wave doodles used as section dividers. When icons appear, they are 1px-stroke line icons in Forest Ink, 16–20px, monoline. The aesthetic borrows from botanical illustration, lab notebook diagrams, and vintage research charts — flat, annotated, and information-first.

## Design Principles

### Do

- Use Moss (#85c093) only for the single most important action per screen — every other action should be outlined, ghost, or text-only.
- Set card radius to 12px and tag radius to 4px consistently; reserve 18–24px exclusively for hero-scale panels.
- Use cinetype with +0.30em letter-spacing for any uppercase label that should feel like a specimen tag or axis title.
- Wrap inline links in square brackets [ like this ] to keep the page's annotation feel consistent.
- Place section titles at the canvas margin with muoto at 12px weight 500 in Forest Ink, preceded by a bracket glyph.
- Keep the canvas at Sage Paper (#e0e0e0) edge-to-edge — do not introduce a white page background anywhere on the layout.
- Use inset 0.5px hairlines in Lichen (#cad3d2) for card borders instead of 1px+ drop shadows.

### Don't

- Do not add a second chromatic action color — if Moss (#85c093) is taken, use an outlined Forest Ink button, not a different fill.
- Do not use cinetype for body copy or long headings — its wide tracking makes it illegible below 14px and above two words.
- Do not introduce drop shadows stronger than 6% opacity — the system is flat, and heavy shadows break the herbarium feel.
- Do not use pure black (#000000) for body text — Forest Ink (#09352e) carries the green undertone that makes the palette cohere.
- Do not put data points on a card — they belong directly on the Sage Paper canvas so the page itself reads as a chart.
- Do not use the Indigo Accent (#433787) more than once per page — it is punctuation, not a palette member.
- Do not use a white page background; the sage canvas is a structural choice, not a fill.

## Components

### Sage Paper Card

Bone White (#ffffff) surface, 12px radius, 20px padding, 0.5px inset hairline border in #cad3d2. No drop shadow. Used for the upper-right info panel and most grouped content blocks. The card should feel like a piece of paper laid on the canvas — flat, slightly lifted only by its white fill.

### Pill Tag (cinetype label)

4px radius, transparent or very-light fill, 1px border in Forest Ink (#09352e) or Lichen (#cad3d2). Text is cinetype at 12px, weight 400, letter-spacing +0.30em, uppercase, color Forest Ink. This is the system's signature decorative element — use for any label that should feel 'stamped' rather than written.

### Filled Mint Button

Background Moss (#85c093), text Forest Ink (#09352e), 12px radius, padding 10px 20px, denim weight 500 at 14px. This is the lone filled button — every other action takes a non-filled variant. The soft mint against dark forest text keeps the button from feeling aggressive against the sage canvas.

### Outlined Button

Transparent background, 0.5px inset border in Forest Ink (#09352e), 12px radius, padding 10px 20px, denim weight 500 at 14px, text Forest Ink. Used for non-primary actions and form submission alternatives.

### Ghost Text Link

No background, no border, denim at 14px weight 500, color Deep Fern (#007010). Often wrapped in square brackets [ like this ] to create the system-wide 'annotation' feel. Underline appears only on hover.

### Scatter Data Point

Two states: hollow circle (stroke Forest Ink 1px, fill transparent, 8px diameter) and filled circle (fill Bone White or Emerald, 6–8px). Optional inner dot for highlighted points. Always sits on the Sage Paper canvas — no card behind it.

### Timeline Node

Bone White (#ffffff) filled circle, 10px diameter, 0.5px Forest Ink border, connected by a 1px Forest Ink hairline path. The timeline reads like a plotted sequence rather than a process diagram.

### Floating Round Chip

Background Forest Ink (#09352e) or Charcoal Bark (#29211e), text Bone White, 9999px radius (pill), padding 6px 12px, muoto at 12px weight 500. Sits absolutely positioned over the data viz.

### Axis Bracket Label

muoto at 12px weight 500, color Forest Ink, with a leading bracket glyph ('[ Chaos ]' / '[ Clarity ]'). Used at the top and bottom of major sections to reinforce the page-as-chart metaphor. Letter-spacing tight (-0.01em).

### Hairline Section Divider

1px line in Lichen (#cad3d2) or 0.5px inset in #cad3d2. No vertical bars or heavy rules — dividers are always one hairline, often dotted.

### Dark Inverse Panel

Background Charcoal Bark (#29211e) or #1a191a, text Bone White, 12px radius, 20px padding. Used only when the design needs to invert — no shadows, just a flat dark fill against the sage canvas.

### Version Stamp (footer)

muoto at 11px, color Forest Ink, rotated 90° (or written vertically), positioned at the extreme left or right margin. Carries build date, section ID, or page version. Pure decoration-as-information.

## Similar Design Systems

- {'why': 'Same mono-accent approach with one vivid color doing the work of ten, plus tight custom-feeling typography and flat surfaces.', 'business': 'Linear'}
- {'why': 'Same hairline-bordered, nearly-shadowless component language and a near-monochrome palette that uses the canvas itself as a color.', 'business': 'Vercel'}
- {'why': 'Treats the page as a data canvas with bracket labels, axis-style annotations, and mono-color chart elements that feel like a research notebook.', 'business': 'Observable'}
- {'why': 'Same small-set UI sans plus decorative tracking-heavy display face pairing, and the same flat hairlined cards on tinted canvas.', 'business': 'Arc'}
- {'why': 'Shares the herbarium/archival aesthetic — muted paper-toned canvas, tiny annotated labels, and a refusal of glossy SaaS conventions.', 'business': 'Are.na'}

## Agent Prompt Guide

Quick Color Reference:
- text: #09352e (Forest Ink)
- background: #e0e0e0 (Sage Paper)
- card surface: #ffffff (Bone White)
- border / hairline: #cad3d2 (Lichen)
- accent: #007010 (Deep Fern) for links and emphasis strokes
- primary action: #85c093 (filled action)

Example Component Prompts:
1. Create a scatter-plot hero section: Sage Paper canvas (#e0e0e0) filling the full width. Scatter 60 hollow circles (1px Forest Ink stroke, 8px diameter) and 8 filled Bone White circles across a 1200×500 area, with no card behind them. Add a top-left bracket label using muoto 12px weight 500 in Forest Ink: '[ Chaos ]', and a top-right bracket label: '[ Clarity ]'.
2. Create a pill tag: 4px radius, 1px border in Lichen (#cad3d2), transparent background, cinetype 12px weight 400 at +0.30em letter-spacing, uppercase, Forest Ink text, padding 4px 10px.
3. Create a Primary Action Button: #85c093 background, #29211e text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
4. Create a Bone Card panel: white (#ffffff) background, 12px radius, 0.5px inset Lichen (#cad3d2) border, 20px padding, no drop shadow. Inside: denim 16px weight 500 heading in Forest Ink, 8px gap to body, denim 14px weight 400 in Charcoal Bark.
5. Create a floating round chip: Forest Ink (#09352e) background, Bone White text, 9999px radius, padding 6px 12px, muoto 12px weight 500. Position absolutely over a data plot in the lower-left quadrant.

## Type Pairing Rules

denim carries everything that is read as information or body content. muoto carries anything that is read as a label, axis tick, tag, or chrome — typically 11–13px, never above 14px. cinetype is reserved exclusively for uppercase decorative labels and is never set in lowercase or sentence case. Never pair cinetype with muoto in the same line; cinetype wants denim or silence around it.

## Chart-as-Page Convention

The page itself is a chart. Major sections should carry bracket axis labels at their top-left and top-right margins using muoto 12px. Data elements (circles, dots, paths) should sit directly on the Sage Paper canvas — never inside a card. Dotted gridlines in Lichen at 0.5px are encouraged as ambient texture even where no chart is drawn.
