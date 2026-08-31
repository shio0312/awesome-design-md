# Grove AI — Design System

> **North Star**: clinical journal in morning light — a single green word anchors a page of measured prose
> **Theme**: light
> **Source**: https://www.grovetrials.com
> **Refero Style**: https://styles.refero.design/style/7f7d3ff7-7a74-40f1-9098-a946ce53d4d4
> **Synced**: 2026-09-01

## Overview

Grove AI uses a clinical-credibility language: bright white canvas, restrained forest-green accents, and a deliberate typographic contrast between an editorial serif (Libre Caslon Text) for hero-level storytelling and a precise grotesque (Geist) for body and interface. The brand voice lives in a single green word — "Grace" — set in the serif and dropped into an otherwise monochrome headline, so the AI agent reads as the personality of the product rather than a feature. Surfaces are flat with a single light-gray card layer; elevation comes from soft inset shadows and hairline borders, never from heavy drop shadows. Component weight is lightweight: pill buttons, ghost controls, thin outlined tags, and tight small-caps section labels. Overall the system feels like a well-funded medical journal that also happens to be a product page — clinical authority expressed through restraint, not decoration.

## Color Palette

- **Forest Grove**: `#0b835c` — Primary brand color — used for the logo mark, the signature word in serif headlines, accent borders on tags and announcement pills, and small icon highlights. A deep, slightly desaturated green that reads as clinical and trustworthy rather than energetic [brand]
- **Pine Shadow**: `#1c2b27` — Secondary dark surface — a near-black green-tinted shade for inverted buttons and dark surface moments where #000 would feel too harsh against the green accent [brand]
- **Ink Black**: `#1c1c1e` — Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color [neutral]
- **Graphite**: `#303033` — Secondary text and dividers — a mid-dark gray for body copy de-emphasis, subtle borders, and metadata [neutral]
- **Slate Mid**: `#676768` — Muted helper text, inactive labels, and tertiary metadata — sits at a comfortable AA contrast against white [neutral]
- **Mist Gray**: `#eff1f6` — Card surface and the only neutral fill color in the system. Creates a single elevated tier above the white canvas without introducing a new hue [neutral]
- **Pure White**: `#ffffff` — Page canvas, card-internal backgrounds, and inverse text on dark fills [neutral]
- **Shadow Smoke**: `#bfbfbf` — Box-shadow base color for the soft elevation that sits behind cards and the floating product mockup on the right side of the hero [neutral]

## Typography

- **sans-serif**
- **Libre Caslon Text**
- **Geist**
- **Geist Mono**
- **Geist Medium**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 12 | — | 1.5 |
| body-sm | 14 | — | 1.5 |
| body | 16 | — | 1.5 |
| subheading | 20 | — | 1.25 |
| heading-sm | 24 | — | 1.25 |
| heading | 32 | — | 1.2 |
| heading-lg | 40 | — | 1.2 |
| display | 92 | — | 1.2 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 24px
- **Element Gap**: 10px
- **Section Gap**: 80px
- **Border Radius**: {'tags': '9999px', 'cards': '20px', 'icons': '12px', 'inputs': '8px', 'buttons': '9999px', 'largeCards': '24px', 'testimonialCards': '20px'}

## Layout

Page model is centered max-width 1200px with generous side margins. The hero is a two-column split: left column holds the announcement pill, serif headline, subhead, and supporting meta, while the right column carries a tall floating product mockup card that breaks the container and extends slightly beyond. Below the hero, the page stacks single-column sections: a 3-up stat row, a 2-up results block with big numbers, a centered testimonial carousel, a CTA pair centered, and a partner logo strip. Section gaps are large (80px+) to maintain editorial breathing room. Navigation is a single sticky white bar at the top with horizontal links and a ghost pill "Sign In" on the right. The overall rhythm is white-on-white bands with one Mist Gray section per page; there is no alternating dark/light pattern.

## Surfaces / Elevation

- **Canvas**
- **Card**
- **Inverted Dark**
- **Brand Accent**

**Shadow tokens:**

## Imagery

Imagery is documentary and human-centered, not abstract. The hero is anchored by a real photograph of a clinician/researcher with a green color wash, layered with chat UI bubbles to show the AI in conversation. There are no decorative illustrations, 3D renders, or abstract graphics anywhere — the brand communicates clinical reality rather than tech spectacle. Logo strips (press mentions, partner organizations, advisor brands) are treated as grayscale wordmarks at reduced contrast, sitting directly on white without frames. Icons are line-based, minimal stroke weight, and almost always colored Forest Grove when present. The visual density is low: large white expanses, one photograph, and restrained logo rows.

## Design Principles

### Do

- Set the hero headline in Libre Caslon Text 92px, reserving the green #0b835c for the single product name (e.g. "Grace") while the rest of the headline stays #1c1c1e.
- Use 9999px radius on all buttons, tags, and pills to keep the interaction language soft and pill-shaped throughout.
- Reserve the forest green #0b835c for three jobs only: the brand word in serif headlines, small-caps section labels, and icon/directional accents (arrows, lightning). Never use it as a solid button fill or large background surface.
- Pair a Filled Dark Button (#1c1c1 fill, white text) with an Outlined Button (transparent, #1c1c1 border) as the canonical CTA pair on any page section.
- Use Mist Gray (#eff1f6) as the only card surface color; cards are never white-on-white when they need to group content.
- Type all small-caps category labels at 12px Geist with 0.1em tracking — the wide tracking is what makes them read as clinical-trial section headers.
- Keep body copy left-aligned and capped at ~520px width to maintain the editorial reading column.

### Don't

- Do not use Geist or any sans-serif for the hero headline — the serif Libre Caslon Text is the brand's signature and must stay in the display slot.
- Do not apply drop shadows greater than 1–2px of blur; the system rejects heavy elevation in favor of hairline halos.
- Do not introduce new accent colors; the palette is monochrome plus one green, and adding blue/red/purple would dilute the clinical authority.
- Do not use #0b835c for filled buttons — the dark filled button is always #1c1c1, and green is reserved for accent and small-caps labels.
- Do not center-align body paragraphs; the system reads as an editorial layout and left-alignment is non-negotiable below the hero.
- Do not use radii between 14px and 18px — the system commits to either 8/12px (tight elements), 20/24px (cards), or 9999px (pills), with nothing in between.
- Do not pair the serif with bright or saturated colors other than #0b835c; any other chromatic color on the serif text breaks the signature.

## Components

### Top Announcement Banner

Background #0b835c, white text, Geist 12–14px, 4px vertical padding. Centered single line of text with a trailing arrow indicator. No border, no radius.

### Sticky Navigation Bar

White background with a subtle bottom border (1px #1c1c1 at 0.1 opacity implied). Logo on left (grove + green leaf icon), horizontal nav links centered/right in Geist 14px, "Sign In" as a ghost pill button on far right. Padding 16px vertical.

### Announcement Pill

Transparent background with a 1px #0b835c border, 9999px radius, Geist 12px uppercase with 0.1em tracking, #0b835c text, 8px 16px padding. Reads as a medical or editorial tag.

### Hero Headline

Libre Caslon Text 92px, weight 400, line-height 1.2, letter-spacing -0.011em. The word "Meet" is set in #1c1c1 and the product name "Grace" is set in #0b835c — same serif, color carries the brand. No other treatment; no gradient, no decoration.

### Hero Subhead

Geist 18–20px, weight 500, #1c1c1e. Tight leading (1.25), left-aligned, no wider than 520px.

### Floating Product Mockup Card

Tall card with 20px radius, 1px hairline shadow (0px 0px 1px rgba(0,0,0,0.35) + 1px 2px inset), white internal surface. Chat bubbles overlay the image: green pill for greeting, white outlined pill for status, and a prominent question bubble in Geist 18px.

### Filled Dark Button

Background #1c1c1, white text, Geist 14px medium, 9999px radius, 12px 24px padding. Carries a subtle inset white highlight (rgba 0.75) and 1px outer shadow. Used for "Read Case Studies" and similar high-intent actions.

### Outlined Button

Transparent background, 1px border #1c1c1, #1c1c1 text, Geist 14px medium, 9999px radius, 12px 24px padding. No fill on hover in screenshots — stays as a clean ghost. "Explore Products" uses this variant.

### Stat Card

Mist Gray (#eff1f6) background, 20px radius, 24px padding. Big number in Geist 40px weight 600 #1c1c1, label below in Geist 14px #303033.

### Small-Caps Section Label

Geist 12px, letter-spacing 0.1em, uppercase, #0b835c or #676768. Sets a clinical-trial-report tone and provides color-coded category anchors.

### Big Stat Block with Icon

Large number in Geist 40px weight 600 #1c1c1, preceded by a small icon (upward arrow or lightning bolt) in #0b835c. The green icon + small-caps green label + dark number forms the brand's proof-point formula.

### Testimonial Card

White background, 20px radius, generous 32px padding, thin shadow halo. Brand logo in green at top-left, quote in Geist 18–20px regular, author photo (40px circle) + name (Geist 14px medium) + role (Geist 14px #676768) at bottom-left.

### Press / Partner Logo Strip

Grayscale logos in Geist or custom sans, #1c1c1 at reduced opacity, evenly spaced with 40–60px gaps. No background container — logos sit directly on the white canvas.

## Similar Design Systems

- {'why': 'Same clinical-AI positioning, identical forest-green accent on a white canvas, and the same pattern of green-serif signature words in otherwise monochrome headlines.', 'business': 'Hippocratic AI'}
- {'why': "Healthcare AI with a light-mode interface, one restrained accent color, serif-meets-sans typographic contrast, and proof-point stat sections that echo Grove's formula.", 'business': 'Abridge'}
- {'why': 'Clinical documentation AI with flat white surfaces, pill-shaped CTAs, and a single accent color used sparingly for labels and icons rather than fills.', 'business': 'DeepScribe'}
- {'why': 'Life-sciences brand using editorial serif headlines on a white canvas with a single signature accent, medical-journal layout rhythm, and minimal drop-shadow elevation.', 'business': 'Verily (Alphabet)'}

## Agent Prompt Guide

**Quick Color Reference**
- text: #1c1c1e
- background: #ffffff
- card: #eff1f6
- border: #1c1c1e (at low opacity) or #303033
- accent: #0b835c (Forest Grove)
- primary action: #0b835c (filled action)

**Example Component Prompts**

1. **Hero Headline**: White canvas. Display text in Libre Caslon Text 92px, weight 400, line-height 1.2, letter-spacing -0.011em. The word "Meet" in #1c1c1e, the word "Grace" in #0b835c — same font, color carries the brand. Subhead below in Geist 20px weight 500, #1c1c1e, max-width 520px.

2. **Announcement Pill**: Transparent background, 1px border #0b835c, 9999px radius. Text in Geist 12px uppercase, 0.1em letter-spacing, #0b835c color. Padding 8px 16px. Sit it 24px above the hero headline.

3. **Stat Card**: Mist Gray (#eff1f6) fill, 20px border-radius, 24px padding. Number in Geist 40px weight 600 #1c1c1e. Label in Geist 14px #303033 directly below, single line.

4. **Testimonial Card**: White background, 20px radius, 32px padding, hairline shadow (0 0 1px rgba(0,0,0,0.35) + 0 1px 2px rgba(0,0,0,0.25) inset). Brand logo in green at top-left, quote in Geist 18px regular #1c1c1e, 40px circular author photo + name/role at bottom.

5. Create a Primary Action Button: #0b835c background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

## Signature Formula — Proof Point

Every numerical result on the site follows the same construction: small-caps green label (Geist 12px, 0.1em tracking, #0b835c) → small green directional icon (up-arrow or lightning) → big dark number (Geist 40px weight 600, #1c1c1e) → single-line caption (Geist 14px, #303033). This formula is the brand's proof language and should be reused for any metric, stat, or KPI on any new page.
