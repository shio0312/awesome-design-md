# Karl — Design System

> **North Star**: Pop-up storybook diorama on a sunny afternoon
> **Theme**: light
> **Source**: https://karlgonsalves.com
> **Refero Style**: https://styles.refero.design/style/dd8b7191-a992-4dab-88f8-f67e8819b461
> **Synced**: 2026-09-01

## Overview

Karl's site is a motion-designer portfolio told entirely through hand-illustrated cartoon scenes — Dutch canal houses wrapping around a blue globe, white clouds drifting across a bright yellow sky, curved display text orbiting the composition. The chrome around the illustration is intentionally minimal: a single row of centered uppercase nav links in Arial, and one custom display face (Changa One) that carries every headline with stacked, almost overprinted weight. Surfaces are flat and saturated rather than shaded or elevated; the 1440px border-radius is used as a compositional device to carve circular/oval focal elements out of the yellow canvas, not as a card radius. The whole experience reads like a pop-up storybook spread — flat color, no shadows, no gradients, no UI density — where the illustration IS the interface and text is laid on top as playful signage.

## Color Palette

- **Signal Yellow**: `#ffe600` — Full-bleed page and section background — the unbroken sunny sky that fills every viewport and frames all illustration. The yellow IS the canvas, not a surface sitting on a white page [brand]
- **Globe Azure**: `#007fff` — Hero focal surface — the spherical focal element rising from the bottom of the viewport, and any large circular/oval composition element. White text sits directly on this blue [brand]
- **Roof Coral**: `#ef3b2c` — Illustrated house roofs and accent fills within the hand-drawn scenes — decorative, never used on UI chrome [accent]
- **Charcoal Ink**: `#333333` — All body text, nav link text, nav link borders, and the thin linework inside the illustrations. The single dark value the entire UI runs on [neutral]
- **Cloud White**: `#ffffff` — Display text overlaid on the blue globe, scattered cloud illustrations across the yellow sky, and window fills inside the house artwork. The only light value used structurally [neutral]

## Typography

- **Changa One**
- **Arial**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 20 |
| body | 14 | — | 20 |
| subheading | 20 | — | 25 |
| heading-sm | 32 | — | 32 |
| heading | 50 | — | 40 |
| display | 75 | — | 54 |

## Spacing & Layout

- **Card Padding**: 0px
- **Element Gap**: 20px
- **Section Gap**: 45px
- **Border Radius**: {'cards': '0px', 'globe': '1440px', 'pills': '0px', 'buttons': '0px'}

## Layout

Full-bleed viewport-height sections, no max-width container, no centered column. Each section of the page is its own illustrated scene filling the screen, with text overlaid as signage rather than inside a content column. The hero is a full-viewport illustration with a blue globe rising from the bottom and curved white display text on top. The nav sits at the very top, centered, as a single thin row with no background. Section transitions are hard cuts from one illustrated scene to the next — no dividers, no bands of contrasting neutral color, no breathing whitespace between sections. There is no traditional content grid, no card row, no feature columns; the page is a vertical scroll through a sequence of full-bleed illustrations with floating text.

## Surfaces / Elevation

- **Sunny Sky**
- **Globe Sphere**

## Imagery

The site has no photography and no conventional product imagery. Every visual is a single hand-drawn illustration per viewport — flat vector cartoon style with chunky outlines, simple geometric Dutch canal houses, puffy white clouds, and a stylized blue globe. The palette inside the artwork is limited to coral red for roofs, muted grays for house walls, white for windows and clouds, and dark ink for linework. Illustrations are full-bleed (edge-to-edge of the viewport), unrounded, and unbordered. Icons in the nav and chrome are absent — text is the only iconography. The illustrations function as both atmosphere and content; no section uses a real photo or screenshot.

## Design Principles

### Do

- Use Signal Yellow (#ffe600) as the unbroken full-bleed background of every section — never wrap it in a card or sit it on white.
- Use Changa One at 75px, line-height 0.72, for display headlines and let the lines overlap into a stacked/overprinted silhouette.
- Use 1440px border-radius only to produce circles and ovals that act as focal surfaces, not as a card or button radius.
- Place nav links at 14px Arial weight 400 with 10px/20px padding and indicate the active state with a 20px-wide #333333 border-bottom only.
- Lay white (#ffffff) display text directly on the #007fff globe surface and on the #ffe600 yellow sky — no text shadow, no text background.
- Communicate depth through stacked illustration layers (houses over globe over sky), not through box-shadow or opacity.
- Hard-cut between full-bleed illustrated viewports with no dividers, gray bands, or whitespace buffers between scenes.

### Don't

- Don't add a white or neutral page background behind the yellow — the yellow is the canvas, not a surface on a white page.
- Don't apply box-shadow, glow, or blur to any element; the system is intentionally flat.
- Don't use small border-radius values (4px, 8px, 12px) for cards or buttons; the only radius in the system is 1440px for circular framing.
- Don't introduce a second body font, a sans-serif display alternative, or a bold weight of Changa One — Arial handles chrome, Changa One weight 400 handles display, and nothing else appears.
- Don't center body text in a content column or wrap the illustrations in a max-width container; everything is full-bleed and centered to the viewport, not the page.
- Don't use a chromatic fill on the active nav link or a fill on any button; the only interactive-state signal is a 20px #333333 border-bottom on the current nav item.
- Don't use the coral #ef3b2c or any other illustrated-art color on UI chrome, text, or borders — those hues belong inside the artwork only.

## Components

### Top Centered Nav

Single horizontal row of five inline links (HOME, ABOUT, WORK, PLAY, CONTACT), 14px Arial, all caps, color #333333, no background, no underline. Items separated by 20px horizontal padding per link (10px vertical, 20px horizontal). The active page is indicated by a 20px-wide border-bottom on the current item in #333333. Sits at the very top of the viewport on the yellow background, horizontally centered, no container box around it.

### Full-Bleed Illustrated Hero

A viewport-height composition with #ffe600 as the unbroken background. A large illustrated scene (cartoon houses, clouds) arcs around the bottom of the viewport. White display text in Changa One is curved/rotated to follow the arc. No image card, no overlay, no shadow — the illustration sits directly on the yellow.

### Circular Globe Surface

A solid #007fff circle, border-radius 1440px (produces a perfect circle at any size), positioned to rise from the bottom edge of the viewport. Functions as both a graphic element and the background for a white Changa One headline laid on top. The extreme radius value is a signature — it isn't a card, it's a sphere carved out of the composition.

### Curved Display Headline

Two- or three-line Changa One at 75px, white (#ffffff), each line individually rotated to follow the arc of the globe's upper edge. Line-height 0.72 causes the lines to overlap and stack tightly, producing a printed/posterized silhouette. No text shadow, no stroke — pure flat white on flat blue.

### Self-Intro Statement

Changa One at 50px white, laid directly on the #ffe600 background in the upper-right quadrant of a later viewport, rotated slightly to follow the globe arc. No container, no background card, no padding around the text — it floats on yellow as signage would.

### Nav Link (default)

Aria 14px, weight 400, #333333, no background, padding 10px top/bottom and 20px left/right. No underline, no border.

### Nav Link (active)

Same text spec as the default nav link, with a 20px-wide solid #333333 border-bottom centered beneath the word. The border is the ONLY visual indicator of active state — no background fill, no bold weight, no color change.

## Similar Design Systems

- {'why': 'Same flat-saturated single-canvas approach with bold custom display type sitting directly on a bright unbroken background, and minimal nav chrome.', 'business': 'Aaron Draplin (Draplin Design Co.) personal site'}
- {'why': 'Same flat-vector illustration-driven aesthetic with chunky rounded display type and no photographic imagery — the illustration IS the interface.', 'business': 'Kurzgesagt'}
- {'why': 'Same hand-illustrated full-bleed viewport scenes with playful cartoon characters and a custom rounded display face carrying every word.', 'business': 'Yukai Du portfolio'}
- {'why': 'Same motion-studio portfolio grammar — saturated color fields, large custom display headlines floating over illustration, and a near-invisible utilitarian nav.', 'business': 'Buck (buck.co)'}
- {'why': 'Same pop-up-diorama layout logic: full-bleed illustrated scenes, oversized rounded display type, no card UI, no shadows, no content column.', 'business': 'Studio Feixen'}

## Agent Prompt Guide

Quick Color Reference:
- text: #333333 (Charcoal Ink)
- text on globe: #ffffff (Cloud White)
- background (page sky): #ffe600 (Signal Yellow)
- surface (globe): #007fff (Globe Azure)
- border (nav active, illustration linework): #333333 (Charcoal Ink)
- primary action: no distinct CTA color

3-5 Example Component Prompts:

1. Full-bleed illustrated hero. Set the viewport background to #ffe600. Place a solid #007fff circle, border-radius 1440px, anchored so it rises from the bottom edge and occupies the lower-center of the viewport. Lay two lines of 75px Changa One weight 400 white text on top of the blue circle, each line individually rotated to follow the upper arc of the circle, line-height 0.72 so the lines overlap. Add flat cartoon clouds (white #ffffff) and simple vector house shapes in coral #ef3b2c and muted gray scattered along the bottom corners of the viewport.

2. Top centered nav. A single horizontal row, 14px Arial weight 400, color #333333, no background. Five inline links: HOME, ABOUT, WORK, PLAY, CONTACT. Each link gets padding 10px top/bottom and 20px left/right. The active link gets a 20px-wide #333333 border-bottom centered beneath the text. The row sits at the very top of the page, centered, with no surrounding container or background fill.

3. Self-intro text block on yellow. A two-line Changa One statement at 50px weight 400, color #ffffff, placed in the upper-right quadrant of a viewport with a #ffe600 background. Rotate the text block approximately -8° to -12° so it follows a gentle arc. No background card, no border, no shadow — the text sits directly on the yellow field.

4. Section transition. Hard cut from one full-viewport illustrated scene to the next. No dividers, no gray bands, no section padding buffer between scenes. Each new viewport begins immediately at the bottom of the previous one with its own full-bleed illustration on #ffe600.

## Composition Notes

Three signatures define the layout grammar: (1) the 1440px border-radius is never used as a normal card radius — it exists to carve circles and ovals out of the yellow canvas, producing the globe focal element and any circular framing device. (2) Display text is rotated along an arc rather than placed in a straight horizontal line, reinforcing the storybook/poster quality and tying typography to illustration. (3) Changa One's stacked line-heights (0.72 at 75px, 0.80 at 50px) are deliberate — they cause headline lines to visually overlap, mimicking overprinted poster type rather than cleanly separated web type. Any new section should preserve at least one of these three devices; together they are what makes a page feel like Karl's site rather than a generic portfolio.
