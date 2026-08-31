# Origin Financial — Design System

> **North Star**: midnight gallery of quiet wealth. A hushed, near-black room where oversized serif whispers and a few luminous color panels make finance feel like curated art.
> **Theme**: dark
> **Source**: https://www.useorigin.com
> **Refero Style**: https://styles.refero.design/style/c60f05ff-2420-4a24-92db-80c4b6a74683
> **Synced**: 2026-09-01

## Overview

Origin presents personal finance as a nocturnal gallery: near-black canvases, whisper-weight serif display headlines at 80-96px (Lyon Display at weight 300), and chromatic feature cards that hover like illuminated color panels. Most surfaces stay quiet and monochromatic, with saturated color appearing only as full-bleed category tiles for spending, investing, and forecasting modules, and as data signals (chart lines, sparklines). Typography splits into three distinct voices: a high-contrast serif for emotive statements, a neo-grotesque sans for UI, and a monospace for uppercase technical labels and data, producing an editorial-meets-precision feel. White-on-black is the only primary action; the rest of the interface recedes into the dark.

## Color Palette

- **Iris Gleam**: `#847dff` — Primary chromatic accent for feature category cards — the signature violet that appears most often across module tiles [brand]
- **Cyan Signal**: `#00b3dd` — Data accent — chart lines, sparkline strokes, and forecasting indicators on dark surfaces [accent]
- **Pale Iris**: `#d1c9ff` — Light variant of the brand violet for softer category panels and background washes [accent]
- **Deep Iris**: `#4b49aa` — Dark variant of the brand violet for shaded category panels and hover states [accent]
- **Orchid Bloom**: `#dd90d8` — Pink category card for lifestyle/spending modules — warm contrast against the cool palette [accent]
- **Periwinkle**: `#90b8f0` — Soft blue category card for advisory or couples modules [accent]
- **Obsidian**: `#0f1011` — Page canvas — the dominant dark surface that everything floats on [neutral]
- **Abyss**: `#090a0b` — Slightly deeper than Obsidian for subtle stacked sections and shadow tone [neutral]
- **Graphite**: `#2e2e2e` — Mid-dark card surface for elevated modules and data panels [neutral]
- **Steel**: `#3f4041` — Hover/pressed surface for interactive elements and secondary raised panels [neutral]
- **Silver**: `#cacaca` — Light card surface for inverted panels, stat blocks, and testimonial cards [neutral]
- **Fog**: `#6a6b6b` — Muted text and disabled-link color [neutral]
- **Ash**: `#9f9fa0` — Body text, descriptions, and secondary links — never full white [neutral]
- **Cloud**: `#f5f5f7` — Heading text variant for softer white display where #ffffff feels too sterile [neutral]
- **Pure**: `#ffffff` — Primary text, primary action fill, and nav icon strokes — the brightest element in the system [neutral]
- **Void**: `#000000` — Icon fills, button text on white fills, and input backgrounds [neutral]

## Typography

- **Suisseintltrial**
- **Lyon Display**
- **Suisse Int'l**
- **Suisse Int'l Trial**
- **Roboto Mono**
- **Suisseintl**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| mono-label | 12 | — | 2 |
| body-sm | 14 | — | 1.67 |
| body | 16 | — | 1.5 |
| subheading | 18 | — | 1.5 |
| heading-lg | 38 | — | 0.9 |
| display-sm | 80 | — | 1 |
| display | 96 | — | 0.9 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32px
- **Element Gap**: 12px
- **Section Gap**: 80px
- **Border Radius**: {'cards': '16px', 'inputs': '8px', 'buttons': '8px', 'navItems': '8px', 'statBlocks': '16px', 'pillButtons': '9999px', 'featureCards': '30px', 'categoryTiles': '30px'}

## Layout

Full-bleed dark canvas (max-width 1200px content container, but sections break to edge). The page rhythm alternates: (1) atmospheric photo hero with centered headline and inline AI prompt, (2) full-bleed #0f1011 module sections, (3) light #cacaca inverted stat blocks for contrast, (4) product mockup bands with 90px internal padding. Headlines are always center-aligned; feature category cards are arranged in a 3-column grid with 12-15px gaps. Vertical section spacing ranges 24-80px, creating generous breathing room between modules. The navigation is a sticky top bar with glassmorphism (backdrop-filter blur(24px)) containing a logo mark, 3 nav items as ghost buttons, 'Log In' as text link, and a white 'Get Started' primary CTA flush right.

## Surfaces / Elevation

- **Obsidian Canvas**
- **Abyss**
- **Graphite Card**
- **Steel Hover**
- **Silver Inverted**

## Imagery

Atmospheric photography anchors the hero (a full-bleed cloud-and-sky photograph with a desaturated cool treatment that reads as aspirational open sky rather than literal weather). Product visualization is delivered through tilted iPhone renders of the Origin app on near-black backgrounds — the device is the hero, with a subtle volumetric glow rather than screen-glare effects. There are no illustrations, no abstract graphics, and no lifestyle photography. Icons are minimal, line-weight monoline SVGs rendered in white or as silhouette marks. The overall ratio is heavily text-dominant: typography carries ~80% of the visual weight, imagery is reserved for hero atmosphere and product proof.

## Design Principles

### Do

- Set all display headlines in Lyon Display (or DM Serif Display substitute) at weight 300 — never bold the display
- Use 8px radius for all buttons, inputs, and nav items; 16-30px for cards; 9999px only for true pill chips
- Reserve chromatic colors (Iris Gleam, Cyan Signal, Orchid Bloom, etc.) exclusively for full-bleed feature category tiles — never as inline accents or borders
- Use white-on-black (#ffffff fill, #000000 text) as the only primary action; contrast ratio is 21:1
- Apply Roboto Mono uppercase at 10-12px with tracking 0.016-0.182em for all labels, badges, and data annotations
- Maintain line-height 0.9 on Lyon Display 96px headlines — tight leading is a signature
- Differentiate surfaces by color step (#0f1011 → #2e2e2 → #cacaca), not by shadow

### Don't

- Do not bold Lyon Display — weight 300 is the system's defining tension
- Do not apply drop shadows to cards; the system is intentionally flat
- Do not use chromatic accent colors on text smaller than 18px — they vibrate against dark backgrounds
- Do not set body text at full #ffffff white — use #9f9fa0 (Ash) for descriptions and #f5f5f7 (Cloud) for headings instead
- Do not break the three-voice typography system: serif display for emotion, sans for UI, mono for data
- Do not add decorative gradients to UI surfaces — the only legitimate gradient is the dark chrome one (rgb(43,43,44) → rgb(19,19,19))
- Do not use #00b3dd (Cyan Signal) for body color or large fills — it is reserved for data signals and chart lines

## Components

### Primary CTA Button

White fill (#ffffff), black text (#000000), 8px border-radius, 12px vertical / 18px horizontal padding, Suisse Int'l 16px weight 400. Always paired with a right-arrow icon (→). The brightest element on screen — uses the highest contrast pair in the system (21:1 AAA).

### Ghost Outline Button

Transparent background with 1px white border (rgb(255,255,255)), white text, 8px radius, 12px/18px padding, Suisse Int'l 16px. Used in nav bar for 'PRODUCTS', 'FOR EMPLOYERS', 'RESOURCES'.

### Nav Glass Button

Background rgba(255,255,255,0.1), 1px white border, 8px radius, 9px/12px padding. Sits inside a nav bar with backdrop-filter blur(24px) over the Obsidian canvas — frosted glass over dark.

### Pill Badge Button

White 20% fill (rgba(255,255,255,0.2)), 1px white border, 100% radius (pill shape), 1px/6px padding. Icon-only or short text. Used for floating action affordances.

### Pill Chip Label

Background rgba(255,255,255,0.12), 1px border at rgba(255,255,255,0.15), 1440px border-radius (full pill), 10px/32px padding, white text #fafafa at 10-11px. Promotional messaging like the $1 promo.

### Feature Category Card

One of six chromatic backgrounds (Iris Gleam, Cyan Signal, Pale Iris, Deep Iris, Orchid Bloom, or Periwinkle), 30px border-radius, 32px padding on all sides, white or near-white text. Holds an icon, title (Lyon Display 38px/300), and short Suisse Int'l description. Color is the only differentiator between categories — no icons or labels needed for grouping.

### Stat / Inverted Card

Background #cacaca (Silver), 30px border-radius, 32px padding. Dark text #000000 inside. Breaks the dark-only rhythm — used sparingly to spotlight a single piece of content.

### Phone Mockup Module

Graphite background #2e2e2, 16px border-radius, 90px padding on all sides (dramatic breathing room). Contains a tilted iPhone render of the Origin app on Obsidian canvas. The largest padding value in the system — signals premium product framing.

### AI Prompt Input

Black background (#000000), near-white text #fafafa, 8px border-radius, 8px vertical / 22px left padding (asymmetric: generous left padding for the cursor). Suisse Int'l 14-16px. Paired with a circular submit button (100% radius, white 20% fill, arrow icon). Placeholder: 'Where am I overspending this month?'

### Promo Eyebrow Badge

White 12% background, 1px white 15% border, 1440px radius, 10px/32px padding. Roboto Mono 12px weight 500, uppercase, white. Text examples follow the pattern: '$1 FOR 1 YEAR — LIMITED TIME'.

### Award Laurel Badge

Transparent background, white SVG laurel-wreath icon flanking publication name (Forbes, Fast Company) in Lyon Display 18px weight 300, with Roboto Mono 10-12px uppercase sub-text. Sits centered as social proof.

### Display Headline

Lyon Display at weight 300, sizes 80-96px, line-height 0.9, color #ffffff or #f5f5f7. Italic word ('Own', 'Simplify') is mixed with roman to create editorial tension within a single headline. The whisper-weight at 96px is anti-convention — most fintech sites use 600-700, this achieves authority through restraint.

### Section Subhead

Suisse Int'l 18px weight 300 (echoing the display voice), line-height 1.5, color #ffffff for card titles or #9f9fa0 for body descriptions. The 300 weight on body is deliberate — creates vertical harmony with the 300 display.

## Similar Design Systems

- {'why': 'Same dark-canvas approach with whisper-quiet serif headlines and full-bleed feature category cards distinguished by color alone', 'business': 'Wealthfront'}
- {'why': 'Identical near-black surface palette, neo-grotesque sans + monospace label system, and white-on-black single primary action', 'business': 'Mercury'}
- {'why': 'Same ultralight display weight anti-convention, flat elevation philosophy (color steps over shadows), and monospace micro-labels', 'business': 'Linear'}
- {'why': 'Editorial-meets-precision typography split (serif display + sans body + mono data) applied to a dark financial interface', 'business': 'Fidelity Spire'}
- {'why': 'App-first dark product UI with full-bleed phone mockup bands and chromatic accent tiles per feature module', 'business': 'Copilot Money'}

## Agent Prompt Guide

**Quick Color Reference**
- Text primary: #ffffff
- Text body: #9f9fa0
- Text heading variant: #f5f5f7
- Background canvas: #0f1011
- Surface elevated: #2e2e2e
- Inverted surface: #cacaca
- primary action: #ffffff (filled action)
- Accent (data/charts): #00b3dd

**Example Component Prompts**

1. **Hero Section**: Obsidian canvas #0f1011 full-bleed. Centered Lyon Display 80px weight 300, #ffffff, line-height 1.0, with the first word in italic. Subhead in Suisse Int'l 18px weight 300, #9f9fa0, line-height 1.5, max-width 560px. Primary CTA below: white #ffffff fill, #000000 text, 8px radius, 12px/18px padding, arrow icon trailing.

2. **Feature Category Card**: Full-bleed Iris Gleam #847dff background, 30px border-radius, 32px padding. Lyon Display 38px weight 300 white headline. Suisse Int'l 16px weight 400 white description below at 1.5 line-height. No border, no shadow — color carries the entire card identity.

3. **AI Prompt Input**: Obsidian background #0f1011, 8px radius, 8px top/bottom and 22px left padding, 1px solid rgba(255,255,255,0.1) border. Placeholder text 'Ask anything…' in Ash #9f9fa0, Suisse Int'l 16px weight 400. Circular submit button: 100% radius, rgba(255,255,255,0.2) fill, white arrow icon.

4. Create a Primary Action Button: #ffffff background, #000000 text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

5. **Stat Inverted Card**: Silver #cacaca background, 30px border-radius, 32px padding. Lyon Display 38px weight 300 black #000000 headline, Suisse Int'l 16px weight 400 #000000 body. Used to break the dark rhythm — maximum 1-2 per page.

## Gradient System

The system uses exactly two gradients, both subtle and structural — never decorative:

1. **Dark Chrome** — linear-gradient(135deg, rgb(43,43,44), rgb(19,19,19)): applied to product device frames and elevated chrome surfaces. Reads as machined metal in low light.

2. **Sky Atmosphere** — linear-gradient(rgb(15,16,17), rgb(19,29,39) 18%, rgb(26,71,136) 37%, rgb(64,138,193) 69%, rgb(64,138,193) 102%): used behind the hero photograph to deepen the horizon and separate the cloud layer from the page canvas.

Never apply gradients to text, buttons, or feature cards. Never use radial or conic gradients.

## Motion Philosophy

Motion is restrained and confident, not decorative. Three patterns define the system:

- **Quick state transitions**: 0.2s ease on background-color and opacity for all hover/focus states
- **Long atmospheric reveals**: 2.5s with cubic-bezier(0.455, 0.03, 0.515, 0.955) — used for hero text fade-ins and product mockup entrance
- **Border trace**: named animation 'borderTurn' that animates a 1px stroke around hexagonal or circular frames, typically for feature highlights

The 800× prevalence of plain 'ease' timing for short transitions confirms the system values predictability over spectacle. No bouncy springs, no overshoots, no parallax.
