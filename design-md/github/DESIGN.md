# GitHub — Design System

> **North Star**: cosmic command deck with bioluminescent waypoints — a dark, atmospheric workspace where a single green glow marks the path forward
> **Theme**: dark
> **Source**: https://github.com
> **Refero Style**: https://styles.refero.design/style/c3ceca5c-d329-4559-b947-016172941ba2
> **Synced**: 2026-09-01

## Overview

GitHub operates as a deep-space developer observatory: near-black canvas layered with translucent glass surfaces, bathed in violet radial atmosphere, and punctuated by a single warm-green CTA that reads like a terminal cursor brought into the UI. Mona Sans carries the voice — weight 425 at 64px with -0.035em tracking makes display copy feel engineered rather than marketed, while body text sits at 400/16px with generous 1.5 line-height for code-adjacent readability. Surfaces float through subtle rgba whites (0.06, 0.15, 0.2) rather than raised shadows; borders do the elevation work at #21262d. Pill-shaped navigation and tag elements at 60px radius contrast with the 6px sharp-rectangle buttons, creating a deliberate two-shape vocabulary. Color is used surgically: violet/blue/purple gradients generate ambient depth behind hero sections, bright green signals the one action that matters, and the rest of the page recedes into grayscale.

## Color Palette

- **Deep Void**: `#0d1117` — Page canvas, section backgrounds, footer — the absolute darkness that lets all other layers float [neutral]
- **Abyss**: `#000000` — Hero section canvas, deepest background layer, terminal/code surfaces [neutral]
- **Carbon**: `#090d0a` — Button surface, near-black accent fill [neutral]
- **Obsidian**: `#151a22` — Elevated button surface, card depth, input fields on dark canvas [neutral]
- **Slate Edge**: `#21262d` — Hairline borders, card outlines, divider rules — the primary border that does elevation work [neutral]
- **Iron**: `#3d4145` — Card surface background, subtle elevated panel [neutral]
- **Fog**: `#484f58` — Secondary borders, stronger dividers between content blocks [neutral]
- **Mercury**: `#818b98` — Muted borders, inactive form outlines [neutral]
- **Ash**: `#9ea0a2` — Mid-gray borders, icon strokes at reduced contrast [neutral]
- **Pearl**: `#a4aea6` — Body text, secondary copy, muted nav labels, icon fills at 183 instances — the workhorse neutral [neutral]
- **Moss**: `#7c8980` — Tertiary headings, low-emphasis section titles that should recede [neutral]
- **Snow**: `#ffffff` — Primary headings, primary text, button text, nav labels — the foreground voice [neutral]
- **Terminal Green**: `#08872b` — Primary CTA fill (Sign up for GitHub) — the one warm color in the system, deliberately evokes a terminal cursor [brand]
- **Phosphor**: `#5fed83` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color [brand]
- **Canopy**: `#0d3024` — Gray wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Use as a supporting accent, not as a status color [accent]
- **Ultraviolet**: `#8c93fb` — Featured card border accent — signals the selected or highlighted card in a grid [accent]
- **Sky**: `#8dd6ff` — Body text accent, icon fills, link text — the cool companion to warm green, 73 instances making it the second-most-present chromatic color [accent]
- **Cobalt**: `#1f6feb` — Link/button accent at low frequency, icon-secondary token — reserved for marketing moments [accent]

## Typography

- **Mona Sans**
- **Mona Sans Mono**
- **Mona Sans VF**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| body-lg | 18 | — | 1.5 |
| subheading | 22 | — | 1.4 |
| heading-sm | 24 | — | 1.5 |
| heading | 40 | — | 1.2 |
| heading-lg | 48 | — | 1 |
| display | 64 | — | 1.08 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 16-24px
- **Section Gap**: 64-96px
- **Border Radius**: {'tags': '9999px', 'cards': '24px', 'images': '16px', 'inputs': '6px', 'buttons': '6px', 'pillButtons': '60px'}

## Layout

Full-bleed dark page with no max-width constraint on the canvas itself; content blocks center within ~1200px. Hero is a centered headline (64px display) over a violet radial gradient halo, with an inline email-capture form (input + green CTA + ghost button) as the only action surface. Below the fold, sections alternate: centered icon + headline + body text (header pattern), then 3-column card grids with translucent surfaces, then tabbed content areas with pill-tab navigation. Vertical rhythm runs at 64–96px section gaps. Navigation is a slim top bar (~64px) with logo, dropdown menus, search field, and ghost sign-in/up buttons. Footer is a multi-column link grid in 4 columns. Z-pattern reading flow: hero CTA → feature tabs → customer logos → secondary CTA → footer.

## Surfaces / Elevation

- **Void**
- **Abyss**
- **Carbon**
- **Iron**
- **Glass**
- **Frost**

## Imagery

Illustration and 3D character mascots dominate the visual language: soft, rounded 3D blob creatures in saturated greens, pinks, and purples float in cosmic arrangements against the dark canvas. Product screenshots appear inside device frames (IDE windows, browser chrome) as hero evidence rather than lifestyle photography. Iconography is consistently outlined/stroked at 1.5–2px weight in #a4aea6 or #8dd6ff. Gradient halos (radial purple/violet) sit behind hero illustrations to create depth. No real photography of people or environments — the visual identity stays synthetic and engineered.

## Design Principles

### Do

- Use the 6px radius for all filled buttons (green CTA and outlined variants) and the 60px pill radius for navigation tags and filter chips — never mix these two shape vocabularies within the same component type
- Set body text to Mona Sans 16px/400 at 1.5 line-height — this is the single most-used type setting in the system (402 instances) and defines the reading rhythm
- Use #08872b Terminal Green exclusively for the one primary CTA per screen; never apply it to secondary actions, tags, or decorative elements where it would dilute its terminal-cursor specificity
- Build all cards with rgba(255,255,255,0.06–0.2) fills and 1px borders at rgba(255,255,255,0.1) — never use opaque card backgrounds or drop shadows; the frosted-glass effect is the card identity
- Apply the -0.035em letter-spacing at 64px display size and ease toward 0.01em at 18px body — this tracking curve is what makes Mona Sans feel engineered rather than generic
- Place a radial purple gradient halo (filtered with blur(60px)) behind hero content to create atmospheric depth — the page should never feel like flat black
- Use Mona Sans Mono 12px/500 with uppercase and 0.015em tracking for micro-labels, nav tags, and code-adjacent metadata — this stamps technical credibility onto otherwise plain labels

### Don't

- Do not use 4px or 8px radius on feature cards — the 24px radius is what makes a card read as a GitHub glass panel; smaller radii will make it look like a form field
- Do not introduce blue as a primary action color — GitHub's CTA is the warm green #08872b, a deliberate rejection of the SaaS blue convention
- Do not apply drop shadows to cards or buttons — elevation is expressed through translucency and blur, never through shadow stacks
- Do not set body text below 16px or above 18px for paragraph copy — the type scale is deliberately narrow at the reading range
- Do not use solid purple or violet fills on buttons or large surfaces — violet appears only as a card border accent (#8c93fb) and inside gradient halos, never as a flat background
- Do not mix the display weight 425 with conventional 700 bold — the 425 weight is Mona Sans's variable-axis sweet spot, lighter than bold but with more presence than regular
- Do not use #1f6feb Cobalt for general link text or icons at scale — it is reserved for low-frequency marketing moments; general link/accent text uses #8dd6ff Sky

## Components

### Primary CTA Button (Green)

Fill: #08872b. Text: #ffffff, Mona Sans 16px/400. Border: none. Radius: 6px. Padding: 6px 20px. This is the only chromatic filled button in the system. The warm green deliberately avoids the cool blue convention of SaaS CTAs, reading instead as a terminal-cursor accent. Never use for secondary actions.

### Ghost Button

Fill: transparent. Text/border: #ffffff. Radius: 0px (for icon buttons) or 60px (for text pills). Padding: 8px. Used 15× in the raw data as the dominant button variant — GitHub's default interaction surface is transparent, with border or text doing the signaling.

### Pill Button (Nav Tag)

Fill: transparent. Text: #ffffff. Border: 1px solid #ffffff (or rgba(255,255,255,0.3) at rest). Radius: 60px. Padding: 8px 16px. The 60px radius creates the soft, rounded nav-tab vocabulary seen in the Code/Plan/Collaborate/Automate/Secure tab row.

### Outlined Action Button (Subtle)

Fill: rgba(31, 35, 40, 0.4). Text: #8dd6ff. Border: 1px solid #ffffff. Radius: 6px. Padding: 6px 20px. Pairs with the green CTA as a cooler, less committed alternative. The blue text signals informational rather than transactional intent.

### Email Input Field

Fill: transparent. Text: #000000 (renders on light inline form). Border: 1px solid #21262d. Radius: 8px. Padding: 18px 12px 0 18px (asymmetric top padding suggests floating-label pattern). Placeholder: #a4aea6 at 16px. The 8px radius is slightly softer than the 6px button radius, creating a subtle input/button rhythm.

### Glass Surface Card

Fill: rgba(255, 255, 255, 0.06) to rgba(255, 255, 255, 0.2). Border: 1px solid rgba(255, 255, 255, 0.1). Radius: 24px. Backdrop-filter: blur(20px). No box-shadow. The card sits as a frosted panel on the dark canvas. The 24px radius is the signature card corner — never use 4px or 8px for major cards.

### Featured Card (Violet Border)

Fill: rgba(255, 255, 255, 0.06). Border: 1px solid #8c93fb. Radius: 24px. The violet border signals this card is special — a feature highlight, selected state, or premium tier. Use sparingly (3 instances in the data confirms rarity).

### Top Navigation Bar

Height: ~64px. Fill: transparent over page background. Logo: GitHub octocat (white) at left. Nav items: Mona Sans 16px/400, #ffffff, with dropdown chevrons. Search field: dark fill #151a22, 8px radius, with 

### Section Header Block

Centered stack: optional 3D icon or illustration at top, then headline (Mona Sans 40px/460, #ffffff, 1.2 line-height), then body text (18px/400, #a4aea6, 0.01em tracking, 1.5 line-height, max-width ~640px). The headline uses weight 460 — lighter than conventional bold — giving it a quiet confidence.

### Tab Navigation Row

Horizontal row of pill buttons (60px radius, 1px white border, 8px 16px padding). Active state: white fill or stronger border. Inactive: transparent with faint border. Sits above tab content with 32px gap.

### Hero Gradient Banner

Radial gradient from rgba(167, 162, 255, 0.5) at center to transparent, filtered with blur(60px). Positioned behind hero copy to create a soft purple glow that makes the dark canvas feel inhabited rather than empty. No sharp edges — always diffused.

### IDE/Device Frame Screenshot

Browser-chrome or IDE window with traffic-light dots, tab bar with file names (game.ts, characters.module.css), and a code editor inside. Border-radius: 8px on the outer frame, 6px on internal panels. Sits inside a glass card or floats on a gradient halo.

### Footer Link Grid

Dark background (#0d1117). 4-column grid of link lists, each column headed by Mona Sans 16px/600 #ffffff. Links: 14px/400, #a4aea6, with 12px vertical spacing. Column headers: uppercase or weight-differentiated. No borders between columns — whitespace does the separation.

## Similar Design Systems

- {'why': 'Same dark canvas with frosted glass cards, violet/purple gradient halos behind hero content, and a single warm accent color for CTAs', 'business': 'Vercel'}
- {'why': 'Dark-mode product interface with translucent surfaces, minimal border-based elevation, and a restrained chromatic palette where one accent does the signaling', 'business': 'Linear'}
- {'why': 'Developer-tool dark theme with green accent CTAs, monospaced micro-labels, and the same border-does-the-elevation approach to cards', 'business': 'Supabase'}
- {'why': 'Deep-dark canvas with purple/violet atmospheric gradients and a single functional accent color — same strategy of letting the canvas recede so content leads', 'business': 'Railway'}
- {'why': 'Dark marketing site with glassmorphic cards, centered hero typography at large display sizes, and pill-shaped navigation over translucent surfaces', 'business': 'Resend'}

## Agent Prompt Guide

primary action: #08872b (filled action)
Create a Primary Action Button: #08872b background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

## Gradient System

Gradients are atmospheric tools, not decorative ones. They create depth behind hero content and never appear as fills on buttons, cards, or text. Three families:\n\n1. **Purple Hero Halos** — radial-gradient from rgba(167,162,255,0.5) to transparent, always passed through blur(60px) filter. Position behind centered hero headlines and illustrations.\n\n2. **Violet Beam** — linear-gradient from rgba(120,115,203,0.2) at 60% to rgb(89,147,212) at 100%. Used as section-transition washes where dark content meets dark content but needs visual separation.\n\n3. **Green Trace** — linear-gradient from rgba(39,50,231,0) to rgba(95,237,131,0.5). Rarely used, signals a transition from neutral to action-aligned sections.\n\nAll gradients are heavily diffused (40–60px blur) and never have sharp edges. They sit at 0.3–0.6 opacity maximum and are positioned absolutely behind content.

## Motion Philosophy

Motion is restrained and purposeful. Primary easing is `ease` (cubic-bezier(0.25, 0.1, 0.25, 1)) for the vast majority of transitions. Expressive eases — `cubic-bezier(0.5, 0.16, 0.1, 1)` and `cubic-bezier(0.16, 1, 0.3, 1)` — are reserved for entrance animations and scroll-driven reveals. Durations cluster at 0.2s (44×) for micro-interactions and 0.4s (12×) for larger state changes. Transform and opacity are the most-animated properties (41× and 24×), confirming that motion is about position and visibility, not size or color. Grid-template-rows animations (8×) suggest accordions or expanding content panels. Never animate box-shadow, border-color, or background-color on hover — use opacity or transform instead to stay GPU-friendly.
