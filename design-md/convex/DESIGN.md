# Convex — Design System

> **North Star**: Cream paper engineering notebook
> **Theme**: mixed
> **Source**: https://convex.dev
> **Refero Style**: https://styles.refero.design/style/f71e92b0-d7a5-4203-b975-394f185218c2
> **Synced**: 2026-09-01

## Overview

Convex presents a warm cream-paper technical workspace: a desaturated beige canvas (#f6f6f6 to #f7f1ff) hosts both product UI and product screenshots, while dark code surfaces (#141414, #292929) carry TypeScript and dashboard previews with syntax-highlight punctuation in pink, violet, green, and yellow. GT America grotesque at whisper-weights creates a calm, editorial engineering voice — tight negative tracking on 40-56px headlines compresses the wordmark into confident, compact blocks. Components are squared and compact: 8-12px radii, thin charcoal borders, and minimal padding produce a blueprint-like density that reads more like a developer's notebook than a marketing site.

## Color Palette

- **Ink Black**: `#141414` — Primary text, dark card surfaces, code editor backgrounds, filled neutral buttons — the dominant dark across the site [neutral]
- **Paper White**: `#ffffff` — Light supporting surface for subtle backgrounds and section separation. Do not promote it to the primary CTA color [neutral]
- **Cream Surface**: `#f6f6f6` — Page canvas and section backgrounds — warm off-white that distinguishes Convex from cold-white SaaS [neutral]
- **Lilac Wash**: `#f7f1ff` — Subtle tinted background panels, icon wash areas, soft section dividers [neutral]
- **Charcoal Surface**: `#292929` — Secondary dark surfaces, navigation pills, dark-mode code block frames [neutral]
- **Graphite Border**: `#38383a` — Borders on dark surfaces, dividers within code blocks, outlined button strokes on dark fills [neutral]
- **Slate Text**: `#4f4f52` — Secondary body text, nav metadata, subdued labels [neutral]
- **Fog Text**: `#6d6d70` — Muted helper text, tertiary nav items, breadcrumb-style labels [neutral]
- **Ash Text**: `#a9a9ac` — Placeholder text, disabled labels, very low-emphasis metadata [neutral]
- **Mist Divider**: `#e5e5e5` — Hairline dividers, input borders on light surfaces, table row separators [neutral]
- **Signal Blue**: `#69bee2` — Blue supporting accent for decorative details and low-frequency emphasis. Do not promote it to the primary CTA color [accent]
- **Plum Button**: `#8d2676` — Alternative filled button accent on specific marketing sections — rich magenta against cream [brand]
- **Ember Orange**: `#de5d33` — Highlight accent on specific CTAs or callout chips — warm complement to the cool blues [brand]
- **Hot Pink**: `#fc618d` — Red supporting accent for decorative details and low-frequency emphasis [accent]
- **Iris Violet**: `#948ae3` — Violet supporting accent for decorative details and low-frequency emphasis [accent]
- **Mint Green**: `#7bd88f` — Green supporting accent for decorative details and low-frequency emphasis [accent]
- **Canary Yellow**: `#f8e67a` — Yellow supporting accent for decorative details and low-frequency emphasis [accent]
- **Dusk Gradient**: `#221f1d` — Dark section background gradient — diagonal fade from warm near-black through charcoal to a cool blue haze [neutral]

## Typography

- **GT America**
- **ui-monospace / monospace**
- **monospace**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.25 |
| body | 14 | — | 1.5 |
| body-lg | 16 | — | 1.5 |
| subheading | 20 | — | 1.38 |
| heading | 36 | — | 1.25 |
| heading-lg | 40 | — | 1.25 |
| display | 56 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 12px
- **Section Gap**: 64px
- **Border Radius**: {'nav': '12px', 'tags': '4px', 'cards': '12px', 'inputs': '4px', 'buttons': '8px'}

## Layout

Max-width 1200px centered container with 24px gutter. Hero is a two-column split: left third holds headline + CTAs + feature accordion, right two-thirds stacks two dark product preview cards (code editor on top, dashboard below) with a slight overlap. Sections alternate between cream-light and dark-gradient full-bleed bands with 64px vertical padding. The LLM section uses a two-column text-left/visual-right pattern with the pixel art on a cream background and a dark chat card overlapping the visual. Navigation is a fixed white top bar with left-aligned logo, center-left nav links, and right-aligned GitHub pill + auth buttons. Component density is compact — feature cards stack tightly with 12-16px gaps rather than generous whitespace.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Tinted Panel**
- **Dark Code**
- **Dark Section**

## Imagery

Convex uses dark product UI screenshots (code editor, dashboard) as the primary visual content — these are the hero elements, not stock photography. The code editor card shows a real TypeScript file with syntax-colored tokens, and the dashboard card shows a live todo app. The only illustrative element is a pixel-art style block grid used in the LLM section, rendered in a retro 8-bit aesthetic with charcoal and accent-color blocks on cream. No lifestyle photography, no abstract 3D renders. Icon style is minimal mono line icons (copy, GitHub octocat) at 1-1.5px stroke weight. Imagery serves as product demonstration rather than decoration — every visual is something a developer would actually see in the product.

## Design Principles

### Do

- Use GT America at weight 400/500 for body and 700 for emphasis; never introduce a secondary sans-serif
- Apply -0.05em letter-spacing only at 56px display, -0.025em at 40-36px headings, and 0.025-0.05em on 10-12px uppercase eyebrow labels
- Use 8px radius for buttons and 12px radius for cards and nav pills; reserve 4px for tags and small chips
- Keep dark code blocks on #141414 with monospace 13px and syntax colors from the accent palette
- Use the cream #f6f6f6 canvas as the default page background; only switch to dark sections for explicit product or gradient hero moments
- Use 12px for element gaps within cards, 24px for card internal padding, and 64px between major sections
- Prefer hairline #e5e5e5 borders over shadows for card separation on light surfaces

### Don't

- Do not add drop shadows to cards or buttons — separation comes from color and 1px borders only
- Do not use the syntax highlight colors (pink, violet, green, yellow) outside code blocks — they are semantic, not decorative
- Do not use #69bee2 (signal blue) as a filled CTA on light/cream sections — reserve it for dark-section actions only
- Do not introduce gradients on UI elements other than the documented dusk-gradient dark section background
- Do not use pure black #000000 for large text or backgrounds; #141414 is the darkest allowed tone
- Do not use border radii above 16px — the system is squared and compact, not soft and rounded
- Do not set body text below 14px or above 18px — GT America is tuned for a narrow mid-range scale

## Components

### Top Navigation Bar

White (#ffffff) background, 12px radius on dropdown pills, GT America 14px/500 for links in #141414, GitHub stars pill with #292929 dark fill and white star count text. Height ~64px, horizontal padding 24px.

### Ghost Navigation Button (Log in)

White fill, 1px #d7d7d7 border, 8px radius, GT America 14px/500 in #141414, 8px 16px padding. No shadow, flat appearance.

### Filled Light CTA (Start building)

White (#ffffff) fill, #141414 text, GT America 15px/500, 8px radius, 10px 20px padding. Sits on cream canvas and reads as the highest-contrast action available.

### Filled Dark CTA (Learn more)

#141414 fill, white text, GT America 15px/500, 8px radius, 10px 20px padding. The default filled CTA across most content sections.

### Blue Signal CTA (Learn more on dark)

#69bee2 fill, #141414 text, GT America 15px/500, 8px radius, 10px 20px padding. The only chromatic filled button; reserved for dark-section hero actions.

### Code Editor Card

#141414 background, 12px radius, 1px #38383a border, three macOS-style traffic-light dots top-left, file tab strip in #292929, monospace 13px code with syntax colors (hot pink keywords, iris violet types, mint green booleans, canary yellow constants).

### Dashboard Preview Card

Light card surface #ffffff with #e5e5e5 hairline border, 12px radius, 24px padding. Header bar shows domain (.convex.dev) in #6d6d70 12px, table rows alternate white/#f6f6f6 with 1px #e5e5e5 dividers, blue #69bee2 'Add' button at 8px radius.

### Command Snippet Card (npm create convex)

#292929 dark fill, 8px radius, monospace 13px white text, trailing copy icon in #a9a9ac. Sits inline beside the light CTA in the hero.

### Feature Section Card

No explicit background (sits on cream canvas), 0 border, GT America 18px/700 heading in #141414, body 15px/400 in #4f4f52, 24px gap between heading and body.

### Dark Gradient Hero Banner

Background is the 135deg dusk gradient (#221f1d → #38383a → rgba blue haze), 12px radius for any contained cards, centered GT America 40px/700 white headline, small 'PRODUCT' eyebrow tag in 12px/500 uppercase with 0.05em tracking inside a 1px #38383a pill at 4px radius.

### Chat Prompt Card

Dark #292929 background, 12px radius, white monospace 13px prompt text, bottom-right 'Try Convex with Chef' CTA where 'Chef' is set in a custom decorative red serif/wordmark.

### GitHub Stars Pill

White fill, 1px #e5e5e5 border, 8px radius, GitHub octocat icon + '260350 stars' in GT America 13px/500 #141414. Star count separated by hairline divider.

### Code Token

No background, monospace 13px, color picks from the accent palette: keywords #fc618d, types #948ae3, booleans #7bd88f, constants #f8e67a, strings default #e3d0df.

### Pixel Art Illustration

Blocky pixel grid on cream #f6f6f6 background, scattered #292929 blocks forming a loose maze/character pattern, accent blocks in #de5d33 and #69bee2. 16px corner radius on the container.

## Similar Design Systems

- {'why': 'Same ultra-tight grotesque typography with negative tracking at large sizes, minimal use of shadows, dark product UI screenshots as hero content, and a calm monochrome palette punctuated by one accent color', 'business': 'Linear'}
- {'why': 'Identical developer-tool DNA: cream/off-white canvas, monospace code blocks front and center, GT America-adjacent geometric sans, and product-preview cards doing the work that photography would do on a consumer site', 'business': 'Vercel'}
- {'why': 'Same dark code-block hero treatment paired with a light content surface, squared 8-12px radii throughout, and a compact density that reads more like documentation than marketing', 'business': 'Supabase'}
- {'why': 'Similar warm-neutral page surfaces, terminal/code-first visual language, and a restrained accent palette that appears only on interactive elements and syntax tokens', 'business': 'Railway'}
- {'why': 'Same editorial engineering aesthetic — tight grotesque type, cream backgrounds, dark product previews, and minimal decorative chrome that lets the product screenshots breathe', 'business': 'Render'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #141414
- background: #f6f6f6 (cream canvas) / #ffffff (card)
- border: #e5e5e5 (light) / #38383a (dark)
- accent: #69bee2 (Signal Blue — dark sections only)
- primary action: no distinct CTA color

**Example Component Prompts**

1. Build a hero headline: GT America 56px/700, #141414, letter-spacing -2.8px, line-height 1.0. Subline at 18px/400 in #4f4f52. Below it, a white filled button 'Start building' at 8px radius, GT America 15px/500, #141414 text, 10px 20px padding. Beside it, a dark command card #292929 at 8px radius, monospace 13px white text showing '> npm create convex' with a copy icon in #a9a9ac.

2. Build a code editor card: #141414 background, 12px radius, 1px #38383a border, three 8px traffic-light dots (#fc618d, #f8e67a, #7bd88f) top-left. File tab bar in #292929 height 32px. Monospace 13px code body with line-height 1.4. Keywords in #fc618d, type annotations in #948ae3, booleans in #7bd88f, constants in #f8e67a, comments in #6d6d70.

3. Build a dashboard preview card: #ffffff background, 12px radius, 1px #e5e5e5 border, 24px padding. Header row shows domain label at GT America 12px/500 in #6d6d70. Table rows alternate #ffffff and #f6f6f6 with 1px #e5e5e5 bottom borders. Right-aligned 'Add' button: #69bee2 fill, #141414 text, GT America 14px/500, 8px radius, 8px 16px padding.

No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

5. Build a feature accordion row: no background, sits on cream canvas. Heading GT America 18px/700 in #141414 with a trailing chevron icon in #4f4f52. When expanded, body text 15px/400 in #4f4f52 with 12px gap to heading. 1px #e5e5e5 bottom divider between rows.

## Syntax Highlight System

Inside code blocks, Convex uses a deliberate four-color syntax palette that makes TypeScript scannable at a glance. This is a semantic system, not a decorative one: keywords (export, import, const) are hot pink #fc618d, type annotations and interfaces are iris violet #948ae3, booleans and true/false values are mint green #7bd88f, and constants or string literals canary yellow #f8e67a. String interpolation falls to a desaturated lavender #e3d0df. Default code text is #d7d7d7 on the #141414 editor background, with comments in #6d6d70. Never reuse these colors for UI buttons, tags, or accents — they are reserved exclusively for code semantics.
