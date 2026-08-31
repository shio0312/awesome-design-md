# monopo saigon — Design System

> **North Star**: Liquid iridescence behind editorial silence — a monochrome editorial gallery floating on molten light.
> **Theme**: light
> **Source**: https://monopo.vn
> **Refero Style**: https://styles.refero.design/style/3e52dd36-6ab1-48c6-bc40-47ef6d33abc2
> **Synced**: 2026-09-01

## Overview

Monopo Saigon runs on radical monochrome discipline: pure black and white with whisper-thin grays, wrapped around massive Roobert typography that breathes across full-bleed canvases. The signature contrast lives between austere editorial restraint (sharp 0px corners on navigation and text links, generous whitespace, 4px-based rhythm) and a single expressive gesture — full-pill 75px-radius buttons that float like liquid over imagery. Hero environments lean into iridescent, fluid, chromatic atmospheres (greens dissolving into amber into deep oxblood) while the interface itself never picks up a hue, creating the feeling of a black-and-white editorial gallery floating on a river of liquid light. Type sets the temperature: weight 300 at 78px whispers, weight 400 at 225px fills the viewport, and weight 400 at 11px labels everything else with confident minimalism. Motion is expressive but patient — cubic-bezier(0.19, 1, 0.22, 1) ease curves stretching up to 1.25s transform transitions, letting elements glide rather than snap.

## Color Palette

- **Obsidian**: `#000000` — Primary text, SVG strokes, overlay fills — pure black carries all foreground information and graphic marks [neutral]
- **Paper**: `#ffffff` — Light text on dark surfaces, inverse labels, and high-contrast captions. Do not promote it to the primary CTA color [neutral]
- **Inkstone**: `#181818` — Footer body copy and secondary headings — softened black for long-form reading blocks [neutral]
- **Felt Gray**: `#6d6d6d` — Muted helper text, address blocks, legal copy — quiet annotations that recede without disappearing [neutral]
- **Slate Pill**: `#636363` — Filled neutral button background — the only solid fill used for actions like Accept [neutral]
- **Ash Mist**: `#9a9a9a` — Mid-tone neutral for disabled or low-contrast surfaces in the surface stack [neutral]
- **Pewter**: `#808080` — Secondary mid-tone neutral for hover or muted state layers [neutral]
- **Iridescent Fade**: `#a02d25` — Chromatic accent appearing only inside the hero gradient wash — molten oxblood anchor of the iridescent atmosphere, not used in interface controls [brand]

## Typography

- **Roobert**
- **Raleway**
- **system-ui**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.19 |
| body-sm | 16 | — | 1.15 |
| body | 18 | — | 1.21 |
| subheading | 39 | — | 1.19 |
| subheading-lg | 45 | — | 1.15 |
| heading-sm | 54 | — | 1.39 |
| heading | 78 | — | 1.1 |
| heading-lg | 94 | — | 0.76 |
| display | 225 | — | 1.25 |

## Spacing & Layout

- **Max Width**: 1078px
- **Card Padding**: 34px
- **Element Gap**: 14px
- **Section Gap**: 46px
- **Border Radius**: {'tags': '75px', 'cards': '0px', 'images': '0px', 'inputs': '0px', 'buttons': '75px'}

## Layout

Layout is max-width contained at 1078px, centered, with full-bleed dark hero sections breaking the container. The hero is full-viewport: centered monumental headline (Un i ted, Unbound) floating over iridescent media, minimal navigation floating at top, single rotating badge at bottom-left. Body sections follow a spacious editorial rhythm — generous 46px section gaps create breathing room between blocks, alternating between white and dark (black with white type) bands. Content arrangement is asymmetric: text-left/image-right and image-left/text-right alternations dominate, with no centered stacks outside the hero. Card grids appear as single-column project lists rather than multi-column grids — each project gets the full width with its image and title. Navigation is a transparent top bar with logo left, locale center, menu right — no sticky color shift, no shadow, just invisible persistence. The footer is a compact three-column address block (Tokyo, Saigon, London) with quiet 11px copy. Overall: editorial magazine pacing in a digital frame.

## Surfaces / Elevation

- **Paper**
- **Slate Pill**
- **Obsidian**
- **Ash Mist**

## Imagery

Imagery is theatrical and singular: one massive iridescent fluid texture dominates the hero — organic greens dissolving through amber into oxblood like oil on water or molten glass. It reads as full-bleed atmospheric media, possibly video or shader-driven canvas, and occupies the entire viewport as a singular sensory moment rather than a repeated pattern. Project showcases use contained editorial photography (tight product crops, campaign stills) presented without frames or borders — the image is the content. No illustration, no icons beyond tiny UI glyphs, no decorative shapes. Iconography is minimal or absent; the rotating circular text badge functions as the system's only typographic ornament. Overall density: text-dominant with one hero-sized visual gesture, then long quiet editorial stretches of typography and product imagery.

## Design Principles

### Do

- Set display headlines at 225px Roobert weight 400 and let them own the viewport — never crowd them with subheads or CTAs
- Use the 75px pill radius exclusively for buttons and tags — keep all other elements (cards, images, inputs) at 0px radius for sharp editorial contrast
- Reserve color for one iridescent hero backdrop per page — keep all interface text, borders, and fills strictly in the black/white/gray scale
- Use weight 300 at 78px for manifesto and atmospheric headlines to create whisper authority — never push above weight 400 at this scale
- Set line-height to 0.70–0.76 on display sizes above 78px to let lines lock together as typographic art objects
- Apply cubic-bezier(0.19, 1, 0.22, 1) easing to transform and color transitions with durations of 0.8–1.25s for patient, gliding motion
- Keep all interactive text links at 0px radius with no underlines — let spacing, color, and context signal affordance

### Don't

- Never introduce a chromatic UI color — black, white, and gray are the interface palette; the iridescent gradient is media only
- Never use box-shadow or elevation on cards, buttons, or images — the system relies on flat surfaces and hairline 1px borders
- Never set border-radius between 1px and 74px — the system jumps from sharp 0px to full 75px pill, no intermediate rounding
- Never use bold or heavy weights (600+) above 45px — large sizes should whisper at 300 or speak at 400, never shout
- Never center-align body copy in address blocks, lists, or project descriptions — left-align with 8–14px line gaps for editorial flow
- Never add gradients to buttons, badges, or UI controls — gradients belong only in the hero atmospheric media
- Never use Raleway for body or navigation — it is a heading accent only, and even there it appears sparingly
- Never fill the canvas with imagery — the system is text-dominant with one hero-sized visual gesture per page

## Components

### Ghost Pill Button (Dark Surface)

Transparent background, 1px solid rgba(255,255,255,0.3) border, #ffffff text, 75px border-radius (full pill), 11px vertical and 33px horizontal padding, Roobert 16px weight 400. The translucent border dissolves into the iridescent background while the pill silhouette stays unmistakable.

### Ghost Pill Button (Light Surface)

Transparent background, 1px solid #000000 border, #000000 text, 75px border-radius, 11px vertical and 33px horizontal padding, Roobert 16px weight 400. Mirrors the dark-surface variant — same geometry, inverted palette.

### Filled Neutral Pill

rgba(55,55,55,0.78) background (functionally Slate Pill #636363), #ffffff text, 1px solid #ffffff border, 75px border-radius, 11px vertical and 33px horizontal padding. The only solid-filled action in the system — used sparingly for compliance and consent, never for primary marketing CTAs.

### Underline-Free Text Link

No background, no border, 0px radius. Roobert 12–16px weight 400, color shifts between #ffffff (on dark) and #000000 (on light). Underlines are absent — context and weight set the link apart from body copy. Generous line-height (1.36 at 11px, 1.19 at 12px) keeps stacked menus airy.

### Hero Display Headline

Roobert 225px weight 400, line-height 1.25, #ffffff over iridescent dark media. Letter-spacing normal. The headline is the hero — no subhead, no CTA, just one monumental phrase centered in the viewport breathing against fluid light.

### Section Heading (Whisper Weight)

Roobert 78px weight 300, line-height 1.10. The 300-weight at this scale is anti-convention — most sites push 600–700 here. The whisper weight lets the headline feel like it is being spoken, not shouted, giving the editorial chamber its hushed authority.

### Section Heading (Anchor Weight)

Roobert 94px weight 400, line-height 0.76. The tight line-height (0.76) is dramatic — text lines almost touch, creating a dense typographic block that reads as art object. Used for large statement moments where the text itself is visual.

### Project Card / List Row

Transparent background, 0px border-radius, no shadow. Image bleeds full-width within the 1078px container; title sits below in Roobert 16–18px weight 400. No card chrome — the card is content, not a container. Spacing between rows controlled by 14–46px gaps depending on section density.

### Language Switcher

Three inline text links in Roobert 12px weight 400, color #ffffff or #000000 depending on surface, 0px radius, separated by visual whitespace rather than dividers. Active locale carries the same color but slightly heavier visual weight through spacing alone.

### Rotating Scroll Indicator

Circular SVG badge with text tracing the circumference ('SCROLL DOWN · SCROLL DOWN'), rotating continuously at slow tempo. Sits at 0,0 of the bottom-left corner with small offset. Ink black stroke on transparent fill — a typographic punctuation mark, not a button.

### Footer Address Block

Roobert 11px weight 400 line-height 1.36, #6d6d6d Felt Gray text. Tight 8px top margins between lines create a compact address stack that recedes into the page. No dividers or labels — the muted gray does the work.

### Cookie Banner

Fixed bottom bar, rgba(55,55,55,0.78) Slate Pill background, white body text in system-ui 9–16px, paired with Filled Neutral Pill 'Accept' button. Minimal copy, single action, no settings — the banner respects attention by asking for nothing beyond consent.

### Top Navigation Bar

Fixed transparent header 66px tall. Logo wordmark top-left (Roobert 16px weight 400 'monopo saigon'), language switcher centered, menu stack right-aligned (WORK / MANIFESTO / SAIGON SOULS / TEAM / CONTACT at 11–12px weight 400). No background fill — the header is invisible until content scrolls behind it.

### Iridescent Hero Backdrop

Full-viewport organic gradient or video: soft sage green (rgb 160,224,171) dissolving through molten amber (rgb 255,172,46) into deep oxblood (rgb 165,45,37). Applied as a flowing, liquid texture — never as a flat gradient. This is the only chromatic surface in the entire system and exists only behind text, never as UI fill.

## Similar Design Systems

- {'why': 'Same liquid iridescent hero treatment behind monochrome editorial typography and full-pill ghost buttons', 'business': 'Resn'}
- {'why': 'Same immersive full-bleed dark hero with single monumental headline and restrained monochrome chrome around it', 'business': 'Active Theory'}
- {'why': 'Same editorial agency rhythm — oversized whisper-weight headlines, generous 46px+ section gaps, and zero shadow elevation', 'business': 'Locomotive'}
- {'why': "Same austere black-and-white editorial system with sharp 0px corners and custom geometric sans (Roobert echoing Pentagram's house faces)", 'business': 'Pentagram'}

## Agent Prompt Guide

**Quick Color Reference**
- text primary: #000000
- text muted: #6d6d6d
- background: #ffffff
- dark overlay / inverse section: #000000
- border (light surface): #000000
- border (dark surface): rgba(255,255,255,0.3)
- accent: none — the only chromatic color is the iridescent hero gradient, which is media only
- primary action: no distinct CTA color

**3 Example Component Prompts**
No distinct primary action color was observed; use the extracted neutral button treatments instead of inventing a filled CTA color.

2. Build a project list row: transparent background, 0px radius, no shadow. Full-bleed image at the top within the 1078px container, sharp corners. Project title below in Roobert 16px weight 400, color #000000. 46px gap to the next row. No card chrome, no borders, no padding around the content itself.

3. Build a Ghost Pill Button on a light surface: transparent background, 1px solid #000000 border, 75px border-radius, 11px padding-top and padding-bottom, 33px padding-left and padding-right. Label in Roobert 16px weight 400, color #000000. No hover fill — animate border opacity and letter-spacing on transition with cubic-bezier(0.19, 1, 0.22, 1) over 0.8s.

## Motion Personality

Motion is expressive but unhurried — the system treats transitions as slow camera moves rather than UI snaps. The signature curve is cubic-bezier(0.19, 1, 0.22, 1) (a gentle ease-out) applied to transform, color, and opacity at 0.8s and 1.25s durations. Shorter easing uses plain 'ease' at 0.4s for color and opacity micro-transitions. A rotating animation runs continuously on the scroll-indicator badge at slow tempo. Transforms dominate over positional animation — elements glide, slide, and reveal through transform rather than repositioning layout. The 1.25s duration on transforms (69 occurrences) signals that the studio prefers patience over responsiveness; nothing should feel abrupt. Border transitions (6 occurrences) and flex-basis shifts are rare and reserved for layout reveals, not micro-interactions.
