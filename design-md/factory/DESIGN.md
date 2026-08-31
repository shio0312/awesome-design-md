# Factory — Design System

> **North Star**: Terminal war room at midnight. Factory is a stark black control surface where a single white card lands like a flashlit dispatch — the only object in the room is the work itself.
> **Theme**: dark
> **Source**: https://factory.ai
> **Refero Style**: https://styles.refero.design/style/13d6fc89-eba2-4724-ac37-20f4f2e5efec
> **Synced**: 2026-09-01

## Overview

Factory operates as a terminal war room: deep black canvas, weight-400 Geist type pressed tight with negative tracking, and generous negative space that lets two functional accents — signal orange and metric green — speak above the noise. The signature move is the light card floating on near-black ground (#eeeeee panels on #101010 canvas), creating stark figure/ground contrast rather than soft elevation. Almost all interaction is carried by monochrome surfaces; chromatic color is reserved for live data states and status pulses, never decoration. Components sit flat with minimal radii, thin 1px borders, and zero shadow dependency — the design earns its depth through contrast and spacing rhythm, not blur or glow.

## Color Palette

- **Obsidian Canvas**: `#101010` — Page background, footer base — the void everything else is measured against [neutral]
- **Carbon Lift**: `#1d1a18` — Raised dark surfaces, nav wells, button fills — one step up from canvas for interactive depth [neutral]
- **Ash Stroke**: `#3d3a39` — Hairline borders, ghost button outlines, separator lines [neutral]
- **Graphite Mid**: `#4d4947` — Mid-tone fills for chart bodies, secondary surfaces, neutral data visualization [neutral]
- **Warm Granite**: `#8a8380` — Muted body text, secondary copy, inactive labels — warm gray to soften the black [neutral]
- **Pale Stone**: `#b8b3b0` — Tertiary text, section eyebrows, subdued supporting copy [neutral]
- **Bone**: `#eeeeee` — Primary text, light card surfaces, the single bright figure on dark ground [neutral]
- **Chalk**: `#fafafa` — High-emphasis light button fill, log-in button, elevated neutral surface [neutral]
- **Signal Orange**: `#ee6018` — Orange decorative accent for icons, marks, and small graphic details [accent]
- **Metric Green**: `#a0ca92` — Green decorative accent for icons, marks, and small graphic details [accent]

## Typography

- **Geist**
- **Geist Mono**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1 |
| body-sm | 14 | — | 1.43 |
| body | 16 | — | 1.5 |
| heading | 36 | — | 1.1 |
| heading-lg | 44 | — | 1.12 |
| display | 72 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 24px
- **Section Gap**: 96px
- **Border Radius**: {'nav': '3px', 'cards': '10px', 'buttons': '3px', 'largePanels': '20px'}

## Layout

Full-bleed #101010 canvas at all times — no light body background. Max content width ~1200px, centered. Hero is a 2-column split: left third holds the headline + supporting copy + button row, right two-thirds holds the dashboard screenshot at near-1:1 scale. Section rhythm: dark band → logo strip → dark band with feature cards → dark band with CTA card. Vertical spacing between sections is 96px+ — the page breathes. Cards in grid layouts are separated by 24px gaps, never touching. Navigation is a single sticky top bar, no sidebar, no mega-menu — the surface stays uncluttered.

## Surfaces / Elevation

- **Obsidian Canvas**
- **Carbon Lift**
- **Bone Card**
- **Chalk Elevated**

## Imagery

Imagery is minimal and product-led. The dominant visual is a photorealistic macOS dashboard screenshot serving as the hero — a real-feeling terminal panel with traffic-light chrome, monospaced column headers, and live sparklines in orange and green. There is no lifestyle photography, no people, no abstract gradients. Decorative texture on light cards is a subtle film-grain noise overlay, not an illustration. Logos in the trust bar are rendered as monochrome wordmarks, not as color photos. The brand relies on UI-in-UI: showing the product is the imagery.

## Design Principles

### Do

- Keep the canvas #101010 on every section. Light cards (#eeeeee) are the only objects allowed to be bright.
- Use Geist 400 for everything. Reach for weight 500 only when a label must dominate a dense surface (footer headings, key CTAs).
- Apply negative letter-spacing proportionally to size: -0.04em at 72px, -0.025em at 44px, -0.02em at 12px. Display type earns its weight through tightness, not boldness.
- Reserve #ee6018 for live status, build-state indicators, and accent strokes in data charts. Never use it as a button fill.
- Set border-radius to 3px on buttons and nav elements, 10px on cards, 20px on the largest panels. Do not round corners more than this — the system is not soft.
- Build depth through #eeeeee-on-#101010 contrast and 96px+ section gaps. Do not introduce drop shadows or blur to fake elevation.
- Use Geist Mono 12px uppercase for eyebrows, status labels, and column headers. This is the system's secondary voice and the fastest way to signal 'instrument, not marketing'.

### Don't

- Do not introduce additional accent colors. The palette is two neutrals (#101010, #eeeeee), one warm gray for muted text (#8a8380), and two functional accents (#ee6018, #a0ca92). Anything else is noise.
- Do not use weight 600+ or bold for headings. The system speaks at weight 400 with tight tracking — bolding breaks the voice.
- Do not put #ee6018 or #a0ca92 on button backgrounds, card surfaces, or large text fills. They are data-voice colors, not chrome colors.
- Do not use line-height above 1.5. Display sizes use lh=1; body sits at 1.5. Anything looser makes the page feel editorial rather than technical.
- Do not add drop shadows, glows, or blurs to cards, buttons, or modals. The system's elevation is contrast, not depth-of-field.
- Do not mix in serif typefaces or display fonts. Geist and Geist Mono only.
- Do not fill buttons with brand color. The primary action is a neutral dark fill (#1f1d1c) or a neutral light fill (#fafafa) — chromatic CTAs would break the monochrome chrome.

## Components

### Top Navigation Bar

Transparent over #101010 canvas. Height ~64px. Left-aligned wordmark 'FACTORY' in #eeeeee, 12px Geist Mono uppercase, letter-spacing wide. Nav links (Product, Enterprise, Pricing, News, Company, Careers) in #eeeeee at 14px Geist weight 400, uppercase. Log In = #fafafa fill, 3px radius, #101010 text, 0 14px padding. Contact Sales = ghost text link with arrow, transparent fill, 1px #3d3a39 border, 0px radius, 24px vertical padding.

### Dark Filled Button

Background #1f1d1c, text #eeeeee, 3px border-radius, 0 14px padding, Geist 14px weight 400. No border. Used for actions that commit within a dark surface.

### Light Filled Button (Log In)

Background #fafafa, text #eeeeee (note: on the light fill, text is inverted to dark in practice — #101010), 3px border-radius, 0 14px padding. The only chromatic-contrast button in the system; appears once in the nav.

### Ghost Text Link

Transparent background, 1px #3d3a39 border, 0px radius (flat), 24px vertical padding, #eeeeee text. Behaves like a typographic button — no fill ever appears on hover, only text/border color shift to #fafafa.

### Light Surface Card

Background #eeeeee, 10px border-radius, 24px padding all sides, no shadow. Contains dark text (#101010 or #060505) inside. Often carries a subtle grain/noise texture overlay. This is the system's primary way to create visual hierarchy on dark pages.

### Dashboard Frame

macOS window chrome (traffic-light dots) on a #0d0d0d panel with 10px radius. Internal content is a dark grid of metric tiles with 1px #1d1a18 dividers. Header bar: dark fill, Geist Mono 12px uppercase for window title, status dot in #ee6018.

### Metric Tile

No background, 1px #1d1a18 hairline divider, 20px padding. Label: Geist Mono 12px uppercase #b8b3b0, tracking -0.24px. Value: Geist 36px weight 400, #eeeeee, tracking -1.12px. Sparkline below: 40px tall, 1px stroke in #ee6018 or #a0ca92.

### CTA Section Card

Light card (#eeeeee) ~480px wide, 10px radius, 24px padding, optional grain texture. Eyebrow: Geist Mono 12px uppercase, #ee6018 dot + #101010 text. Headline: Geist 36px weight 400, #101010. CTA: dark filled button using #101010 fill, #eeeeee text, 3px radius.

### Status Pulse

6px filled circle in #ee6018 with optional 1px stroke. Sits immediately before label text. No animation required, but pairs with marquee/animation in the marquee logo strip.

### Logo Strip (Trust Bar)

Single row of partner wordmarks on #101010 canvas, all rendered in #8a8380 at consistent visual weight. No card backgrounds, no dividers — just the wordmarks floating in negative space. Separated from surrounding sections by 96px vertical breathing room.

### Feature Card Row

Dark cards (transparent on #101010) with 1px #1d1a18 hairline border, 10px radius, 20px padding. 'Read More →' ghost link in footer. No card background fill — the card is implied by the border, not the surface.

### Footer

Background #101010, 96px+ vertical padding. Headings: Geist Mono 12px uppercase #eeeeee. Links: 14px Geist weight 400 #8a8380. No dividers between columns — generous column gap (24–36px) does the separation.

## Similar Design Systems

- {'why': "Same monochrome-dark canvas, weight-400 display type with tight negative tracking, and one restrained accent (Linear's purple vs Factory's orange) reserved for state and status, never decoration.", 'business': 'Linear'}
- {'why': 'Identical figure/ground strategy: pitch-black canvas, one bright card or screenshot as hero, Geist-family type at flat weight, no drop shadows — depth earned through contrast.', 'business': 'Vercel'}
- {'why': 'Shares the terminal-warm aesthetic — warm grays (#8a8380 class) instead of cold, Geist Mono labels, minimal radii (3–10px), and chromatic accents used only as functional signal in product UI.', 'business': 'Resend'}
- {'why': 'Developer-tool dark surface with Geist-weight typography, dashboard hero pattern showing the product in a windowed UI, and a single warm accent for active states.', 'business': 'Cursor'}
- {'why': 'Same instrument-panel sensibility — dark canvas, monospaced eyebrows, metric tiles with live data, and an anti-decorative stance that treats color as data not chrome.', 'business': 'Railway'}

## Agent Prompt Guide

**Quick Color Reference**
- canvas: #101010
- text: #eeeeee
- muted text: #8a8380
- card surface: #eeeeee
- accent (live status / data signal): #ee6018
- accent (positive metric / trend): #a0ca92
- primary action: #1d1a18 (filled action)

**Example Component Prompts**
1. *Hero section*: Full-bleed #101010 background, max-width 1200px centered. Headline at 72px Geist weight 400, #eeeeee, letter-spacing -2.88px, line-height 1. Supporting copy at 16px Geist weight 400, #8a8380. Two buttons inline: a dark filled button (#1f1d1c, #eeeeee text, 3px radius, 0 14px padding) followed by a ghost link with arrow (transparent, 1px #3d3a39 border, 0px radius, 24px vertical padding).
2. Create a Primary Action Button: #1d1a18 background, #eeeeee text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.
3. *Dashboard metric tile*: no background, 1px #1d1a18 bottom border, 20px padding. Label: Geist Mono 12px uppercase #b8b3b0. Value: Geist 36px weight 400, #eeeeee, letter-spacing -1.12px. Sparkline: 40px tall, 1px stroke, color #ee6018 (negative trend) or #a0ca92 (positive trend).
4. *Trust logo strip*: full-width #101010 band, 96px vertical padding, single row of 8 partner wordmarks rendered in #8a8380, evenly distributed with 24px+ gaps. No card backgrounds, no dividers.
5. *Top nav bar*: transparent on #101010, ~64px tall. Wordmark left: 'FACTORY' Geist Mono 12px uppercase #eeeeee. Nav center/right: Product, Enterprise, Pricing, News, Company, Careers in Geist 14px weight 400 #eeeeee uppercase. Log In button: #fafafa fill, #101010 text, 3px radius. Contact Sales: ghost text link with arrow.

## Motion Philosophy

Transitions are short and mechanical: 0.15s–0.2s with cubic-bezier(0.4, 0, 0.2, 1) easing — the feel of a CLI tool, not a marketing site. Color, background-color, border-color, and stroke all transition together so state changes feel like a single switch flipping, not a layered animation. Named motion (marquee-scroll, sfDashboardFrameIn) appears sparingly: a slow logo marquee and a single dashboard entrance. Avoid spring physics, parallax, or scroll-driven effects — the surface should feel still and precise.

## Voice & Type Treatment

Two voices, one family. Geist 400 carries all marketing and body copy — flat, calm, undecorated. Geist Mono 12px uppercase carries all instrument labels: column headers, status tags, 'BUILD WITH US', nav items. This split is structural: when a user sees Mono, they know they are looking at a system surface, not a page surface. Maintain this discipline even when extending the product.
