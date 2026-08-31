# Portrait — Design System

> **North Star**: polaroid memory wall on cream paper. A bright, off-white scrapbook where deep-navy ink provides the only text, the only structural lines, and the only border color — with a single hand-drawn rainbow that appears once, on the Sign up button and on the italicized word forever, and never again.
> **Theme**: light
> **Source**: https://portrait.so
> **Refero Style**: https://styles.refero.design/style/6b51388b-d00f-4b22-8297-68fb9fc00bc7
> **Synced**: 2026-09-01

## Overview

Portrait is a sunlit, deeply personal canvas for identity: a near-white page where a single deep-navy ink carries almost all text and structural lines, and color appears only as warm pastel surface washes or a signature rainbow that bleeds through italicized words, button borders, and small decorative strokes. The type system is two-voice — Switzer for steady UI, Basier Circle for giant display headlines that compress tight against each other — and the geometry favors generous rounding (24px cards, 28px pill buttons) with barely-there shadows that let content float rather than stamp itself. Everything reads like a scrapbook: scattered tilted photo cards, mint and peach and sky-blue tints, a thin rainbow border around the Sign up button, and a sticky pill nav that hovers above the page with a whisper of elevation. The overall density is comfortable, the rhythm is calm, and the brand voice is warm but restrained — let the user be loud, keep the frame quiet.

## Color Palette

- **Portrait Ink**: `#08304c` — Primary text, heading strokes, outlined action borders — the single deep navy that holds the entire type and structural line system [brand]
- **Nautical Teal**: `#084e72` — Secondary brand ink for nav strokes, icons, and accent text where Ink feels too heavy [brand]
- **Rainbow Spectrum**: `#26c0ff` — Supporting palette color for small decorative accents when the core palette needs contrast. Do not promote it to the primary CTA color [accent]
- **Lavender Violet**: `#8e51ff` — Decorative spectrum color — appears only as part of the rainbow gradient, never as a standalone fill [accent]
- **Cobalt Pop**: `#3b82f6` — Decorative spectrum color — appears only as part of the rainbow gradient composition [accent]
- **Grape Vibrant**: `#ad46ff` — Decorative spectrum color — appears only as part of the rainbow gradient composition [accent]
- **Cherry Red**: `#ff4940` — Decorative spectrum color — appears only as part of the rainbow gradient composition [accent]
- **Tangerine Warm**: `#ffa130` — Decorative spectrum color — appears only as part of the rainbow gradient composition [accent]
- **Sunflower Yellow**: `#ffc837` — Decorative spectrum color — appears only as part of the rainbow gradient composition [accent]
- **Leaf Green**: `#00cc3d` — Decorative spectrum color — appears only as part of the rainbow gradient composition [accent]
- **Charcoal Outline**: `#353535` — Universal stroke and heavy text color — every hairline border, icon outline, and default UI line lives here [neutral]
- **Graphite Body**: `#2c2c2c` — Body text and icon strokes where Portrait Ink feels too cool — slightly warmer reading tone [neutral]
- **Slate Helper**: `#797979` — Muted helper text, secondary nav text, and decorative borders that should recede behind primary ink [neutral]
- **Iron Quiet**: `#585858` — Quiet icon strokes and low-emphasis nav accents [neutral]
- **Ash Divider**: `#dedede` — Light dividers and structural hairlines on neutral surfaces [neutral]
- **Fog Edge**: `#c7c7c7` — Disabled state borders and placeholder strokes [neutral]
- **Mist Hairline**: `#eeeeee` — Card surface tint and the lightest possible structural divider [neutral]
- **White Canvas**: `#ffffff` — Page background and the universal surface above which all color floats [neutral]
- **Mint Wash**: `#d7ffe2` — Soft pastel surface tint used on badge chips and small highlighted areas [accent]
- **Sky Wash**: `#e8f1ff` — Soft section background, alternate surface, and quiet card fill [accent]
- **Peach Wash**: `#ffebd6` — Soft pastel surface tint used on warm-accent chips and highlighted areas [accent]

## Typography

- **Switzer**
- **Basier Circle**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 10 | — | 1.5 |
| body | 16 | — | 1.5 |
| body-lg | 18 | — | 1.45 |
| subheading | 20 | — | 1.43 |
| heading-sm | 31 | — | 1.1 |
| heading | 44 | — | 1.08 |
| heading-lg | 49 | — | 1.04 |
| display | 76 | — | 1 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 16px
- **Element Gap**: 16px
- **Section Gap**: 80px
- **Border Radius**: {'nav': '28px', 'tags': '9999px', 'cards': '24px', 'images': '24px', 'inputs': '16px', 'buttons': '28px'}

## Layout

Centered, max-width 1200px contained layout with generous breathing room. The hero is a single centered stack: eyebrow text → 2–3 line display headline with one rainbow-italicized word → subtext paragraph → domain search input with embedded rainbow CTA → login link. Tilted photo cards scatter around the hero edges, partially cropped by the viewport, as if pinned to a wall. Below the hero, a profile card grid (masonry-like, 2–4 columns) shows the user's tiles at varied aspect ratios — portrait photos, horizontal link cards, article snippets. Sections are separated by 80px vertical gaps with no dividers or alternating background bands; the entire page is one continuous white canvas. A sticky floating pill nav hovers at the top, centered, with a soft drop shadow. A final 'Portrait Wallet' promotion card sits centered at the bottom of the page as a standalone product teaser. Navigation is the pill nav only — no sidebar, no mega-menu, no footer beyond minimal links.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Sticky Nav**
- **Tinted Wash**

**Shadow tokens:**

## Imagery

Imagery is photographic, full-bleed inside Polaroid-style cards, and treated as personal memorabilia rather than product shots: outdoor portraits, candid smiles, golden retriever in a meadow, friends at a restaurant, a person on a cliffside, gap-year Indonesia travel, smoothies in a green cup. Every photo is cropped tight on its subject, sits inside a 24px-radius card with a 1px hairline outline, and floats at a slight rotation in the hero collage. No illustrations, no 3D renders, no abstract graphics. The only product visual is the orange leather wallet card mock in the Wallet section. Color treatment is natural and unfiltered — slightly warm, slightly soft, with the kind of color cast you get from a phone camera in golden hour. The orange wallet and the dark green smoothie are the only images that carry strong saturated color; everything else is desaturated enough to recede behind the rainbow accent.

## Design Principles

### Do

- Use the full-spectrum linear-gradient (blue → magenta → red → orange → yellow → green at 90deg) as a 1.5px outline on at most one CTA per view, and on at most one italicized word per headline.
- Set body type in Switzer 400 at 16–18px with 1.45–1.5 line-height; reserve Basier Circle for display sizes 31px and above.
- Pull the headline tracking tight: -4.25px at 76px, -1.96px at 49px, -1.15px at 44px. The compression is what makes the display feel sculptural.
- Use Portrait Ink (#08304c) as the single text and structural-line color across the entire interface; switch to Graphite Body (#2c2c2c) only for body copy that sits on a warm or pastel background.
- Cap every shadow at 8% black opacity, and stack 3–6 thin layers with negative offsets rather than a single heavy drop. Add a 1px oklab hairline at 4–10% opacity instead of a shadow when the surface needs separation.
- Use 24px radius for cards, 28px radius for buttons, 9999px for tags and small chips. The card/button differential is deliberate — buttons are slightly rounder than the cards they sit on.
- Keep the page canvas pure white (#ffffff) and let color appear only as soft pastel washes on small surfaces, never as a full section background.

### Don't

- Do not introduce a new brand hue — the palette is two navy inks plus a single rainbow gradient. Any additional chromatic color dilutes the signature.
- Do not use filled colored buttons. The primary action is always a rainbow-outlined pill; secondary actions are ghost text only.
- Do not add heavy drop shadows. A shadow darker than rgba(0,0,0,0.1) breaks the paper-on-paper language.
- Do not set body or display type in the rainbow gradient. The gradient is reserved for borders and one italicized word per headline — full-text rainbow reads as a different brand entirely.
- Do not mix Switzer and Basier Circle at the same size. Switzer owns 10–24px, Basier Circle owns 31px and up. Same-size mixing looks like a font fallback error.
- Do not use a sans-serif fallback for Basier Circle's negative tracking. The compression is the brand — only a geometric humanist with matching proportions should substitute.
- Do not center-align body paragraphs longer than three lines; the centered hero subtext is a one-off compositional choice, not a layout default.

## Components

### Floating Pill Nav

White pill-shaped bar, 28px radius, floating centered above the page with a soft 6-layer shadow. Contains the Portrait wordmark with a tiny rainbow square icon, a center 'New — Introducing Portrait Wallet' announcement pill, and Login + Sign up actions on the right. Height approximately 56px, horizontal padding 20px.

### Rainbow Outline CTA

Pill button, 28px radius, transparent fill, 1.5px rainbow-gradient border (blue → magenta → red → orange → yellow → green at 90deg). Text in Portrait Ink (#08304c), 16px Switzer 500, 16px horizontal padding by 10px vertical. The most visible branded element on the page.

### Ghost Text Button

No background, no border. Text in Portrait Ink, 14–16px Switzer 500. Used for Login and 'Already have a Portrait? Login'. Sits quietly next to the rainbow CTA.

### Domain Search Input

Large pill input, ~9999px radius, white fill with a very faint border. 60–64px tall, ~600px wide. Contains light gray 'portrait.so/' prefix text and a darker typed username. Internal border-radius nested with the rainbow CTA inside it, so the two share one continuous border line.

### Photo Profile Card

White card, 24px radius, 1px oklab outline at 4% opacity, optional soft multi-layer shadow. Contains an image area with 24px top radius, a title in Portrait Ink, a short meta line in Slate Helper, and sometimes a small external-link arrow. Padding 16px on text areas. Tiles appear in a varied grid — some taller (2:3 portrait), some wider (16:9).

### Article Snippet Card

White card, 24px radius, 1px outline. Compact horizontal layout: small square thumbnail, a date in Slate Helper at 12px, a two-line headline in Portrait Ink at 14–16px Switzer 500, and a Read more link with an external arrow. Tight 12–16px internal padding.

### Eyebrow Label Pill

Tiny pill, 9999px radius, one of the pastel wash backgrounds (#d7ffe2, #e8f1ff, #ffebd6). Text in matching darker tone, 10–11px Switzer 600 with 0.14em tracking, uppercase. Used for 'New', 'Early access', and category labels. 3px vertical, 8px horizontal padding.

### Wallet Feature Card

Small horizontal card with the wallet card thumbnail on the left, 'Portrait Wallet' title, a 'New' pill in pastel, and 'Get early access now' helper text. Right arrow icon in Charcoal Outline. White background, 16–24px radius, subtle outline.

### Display Headline Block

Basier Circle 600 at 44–76px, line-height 1.0–1.08, negative letter-spacing up to -4.25px. Portrait Ink color. One italicized word inside the headline is filled with the rainbow gradient (currently 'forever' and 'one'). The compression of the type makes the block feel like a single sculptural mass.

### Hero Photo Collage

Individual photo cards at varied sizes, each 24px radius, tilted at 3–6 degrees, partially overlapping page edges. No drop shadow — they read as Polaroids pressed flat against the canvas with the same 1px hairline outline. White background bleeds through any rotation gap.

### Announcement Pill

Small pill inside the floating nav, sky-blue (#e8f1ff) background, 'New' label in pastel ink, followed by 'Introducing Portrait Wallet' in Portrait Ink, and a tiny down-arrow icon. 6–8px vertical padding, 12px horizontal.

### Hero Subtext

Switzer 400 at 18px, line-height 1.45, Portrait Ink or Graphite Body. Centered, max-width approximately 520px, sits 24–32px below the headline block.

## Similar Design Systems

- {'why': 'Same centered hero with a domain-claim input as the primary action, scattered card grid below, and a single CTA on each screen', 'business': 'Linktree'}
- {'why': 'Same scrapbook-card aesthetic with varied tile aspect ratios, tight hairline outlines, and one accent hue driving the brand', 'business': 'Bento'}
- {'why': 'Same restrained two-voice type system, generous card radii, and warm off-white canvas treating the page as a personal portfolio', 'business': 'Read.cv'}
- {'why': 'Same playful use of a single rainbow gradient as the only saturated accent on a calm, light, type-led interface', 'business': 'Candy Mail'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #08304c (Portrait Ink)
- background: #ffffff
- border: #353535 (Charcoal Outline) at 1px, or pastel wash on chips
- accent: rainbow gradient — linear-gradient(90deg, #26c0ff, #e600c2 20%, #ff4940 40%, #ffa130 60%, #ffc837 80%, #00cc3d)
- pastel washes: #d7ffe2, #e8f1ff, #ffebd6
- primary action: #08304c (outlined action border)

**Example Component Prompts**

1. Create a hero headline: 76px Basier Circle weight 600, line-height 1.0, letter-spacing -4.25px, color #08304c. Insert the italicized word 'forever' and fill it with the rainbow linear-gradient(90deg, #26c0ff, #e600c2 20%, #ff4940 40%, #ffa130 60%, #ffc837 80%, #00cc3d). Center the block at max-width 900px.

2. Create a rainbow-outline pill button: 28px border-radius, transparent background, 1.5px border using the full rainbow gradient (90deg, six stops), 16px Switzer 500 text in #08304c, padding 10px 18px. The only saturated UI action in the system.

3. Create a photo profile card: white surface, 24px border-radius, 1px outline in oklab(0 0 0 / 0.04), padding 0 on the image (16px on text), Basier Circle or Switzer 500 title in #08304c at 16px, Slate Helper (#797979) meta line at 12px Switzer 400, optional 10px 16px 14px shadow at rgba(0,0,0,0.04).

4. Create a pastel eyebrow pill: 9999px radius, #e8f1ff background, text 'New' in matching darker tone at 10px Switzer 600 uppercase with 0.14em letter-spacing, 3px vertical and 8px horizontal padding.

5. Create a floating sticky nav: 28px radius, white background, soft 6-layer shadow capped at 3% opacity each, 56px height, 20px horizontal padding. Contains a small rainbow square icon + 'Portrait' wordmark, a center 'New — Introducing Portrait Wallet' pill, and a Login ghost link + a rainbow-outline Sign up pill on the right.

## Gradient System

Portrait uses exactly one signature gradient — the full-spectrum rainbow — and reuses it across three contexts only:

1. A 1.5px border on the primary Sign up button (90deg, evenly spaced from blue to green).
2. A text fill on at most one italicized word per headline (90deg, same stops).
3. A tiny 8–12px square brand icon next to the wordmark (90deg, same stops).

A second, much rarer gradient appears on the Wallet card mock — a 165–170deg spectrum used to simulate light bending across the leather texture, with a dark navy segment splitting the rainbow into two halves. This is product-specific, not a system token.

A single soft radial gradient (lavender at 78% → 44% → transparent) appears once on a hero background, used to create a subtle warm-cool falloff behind the headline. Do not reuse it elsewhere.

## Iconography

Icons are 1.5–2px stroke, rounded line caps, drawn from a single outlined set. Color is Charcoal Outline (#353535) by default, Portrait Ink (#08304c) when sitting on a pastel wash, and white when on a dark surface. No filled icons, no multicolor icons, no icons that mimic the rainbow. The only 'iconic' brand mark is the 8–12px square rainbow gradient swatch used as the Portrait favicon, nav mark, and tab indicator.
