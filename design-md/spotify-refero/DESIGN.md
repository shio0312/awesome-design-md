# Spotify — Design System

> **North Star**: Darkened record store at midnight — every surface recedes so the album art can glow.
> **Theme**: dark
> **Source**: https://www.spotify.com
> **Refero Style**: https://styles.refero.design/style/cc59e195-fed0-4928-96d1-303752786073
> **Synced**: 2026-09-01

## Overview

Spotify operates as a darkened cinema for music: a near-black canvas lets album artwork and artist photography supply all the color, while the chrome itself stays nearly monochrome to keep focus on the content. The interface is compact, information-dense, and built around horizontal scrolling rails of square album cards and circular artist portraits. One signature vivid green (#1ed760) punctuates the system for primary actions, play states, and brand identity, while a purple-to-blue gradient appears only in premium promotional banners. Buttons are fully pill-shaped (9999px), cards carry a modest 6px radius with a generous drop shadow, and typography is a tight, geometric sans-serif that speaks at conversational volumes — never shouting, always functional.

## Color Palette

- **Void Black**: `#000000` — Primary canvas, page background — deepest layer of the dark surface stack [neutral]
- **Obsidian**: `#121212` — Card surfaces, raised panels, modal backgrounds — one step up from the canvas [neutral]
- **Graphite**: `#1f1f1f` — Elevated controls, hover surfaces, filled button backgrounds — the interactive surface tier [neutral]
- **Ash Gray**: `#333333` — Input borders, subtle dividers, inactive control outlines [neutral]
- **Steel Mist**: `#767676` — Muted text, secondary nav, disabled labels — text that fades into the background [neutral]
- **Cloud Gray**: `#b3b3b3` — Secondary body text, metadata, timestamps — readable but never competing with content [neutral]
- **Pure White**: `#ffffff` — Primary text, headings, light icon fills, pill button fills — the highest-contrast element on the dark canvas [neutral]
- **Spotify Green**: `#1ed760` — Green wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the primary CTA color [brand]
- **Premium Magenta**: `#af2896` — Gradient anchor for premium promotional banners, subscription upsell surfaces [brand]
- **Premium Cobalt**: `#509bf5` — Gradient terminus for premium promotional banners, feature callouts on subscription screens [brand]
- **Amber Glow**: `#a16b1b` — Decorative warmth — album artwork occasionally carries this tonal range [accent]

## Typography

- **SpotifyMixUI**
- **SpotifyMixUITitle**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| caption | 11 | — | 1.33 |
| body | 14 | — | 1.5 |
| heading | 24 | — | 1.2 |

## Spacing & Layout

- **Card Padding**: 12px
- **Element Gap**: 12px
- **Section Gap**: 32px
- **Border Radius**: {'tags': '9999px', 'cards': '6px', 'inputs': '4px', 'buttons': '9999px', 'artistImages': '9999px'}

## Layout

The page uses a two-column layout: a fixed left sidebar (~340px) for 'Your Library' and navigation, and a flexible main content area that scrolls independently. The main area is organized as vertically stacked horizontal rails — each rail is a section heading (24px left-aligned, 'Show all' right-aligned) followed by a horizontally scrolling row of cards. Cards are uniform-width within each rail (albums: 180px squares, artists: 180px circles). Spacing between rails is 32px; between cards within a rail is 16px. The top bar is a full-width navigation strip with left-cluster icons/search and right-cluster text links and action buttons. A full-width gradient premium banner is sticky at the bottom of the viewport. There are no section dividers, background color changes, or visual separators between rails — the surface stays uniformly #000000, and hierarchy comes from typography and spacing alone.

## Surfaces / Elevation

- **Void Canvas**
- **Obsidian Card**
- **Graphite Control**

**Shadow tokens:**

## Imagery

Imagery IS the product. The interface is a frame for user-consumed content: square album covers, circular artist portraits, and playlist cover art. Treatment is clean, uncropped (except to square or circle), no filters or overlays on content imagery. Card shadows (0px 8px 24px rgba(0,0,0,0.5)) give artwork dimensional lift off the void canvas. No illustrations, no abstract graphics, no lifestyle photography in the UI itself — the page is a gallery. Icons are minimal, monochromatic, and outlined or filled in white at reduced opacity. The only branded graphic element is the gradient premium banner.

## Design Principles

### Do

- Use 9999px border-radius for every button, tag, and search field — the pill shape is non-negotiable for Spotify's identity.
- Apply 6px radius to all square content cards (albums, playlists) and 9999px for circular artist portraits — never mix radii within the same card type.
- Reserve #1ed760 for the single most important action per screen — log in, play, confirm. Never use it for secondary links, metadata, or decorative elements.
- Keep all text between 11px and 24px. The system is compact; no body copy should exceed 16px, and only section headings reach 24px.
- Use #000000 for the page canvas, #121212 for content cards, and #1f1f1f for interactive controls — maintain this three-tier surface hierarchy on every screen.
- Apply the 0px 8px 24px rgba(0,0,0,0.5) shadow only to content cards lifted off the canvas, never to navigation, buttons, or inputs.
- Let album artwork and artist photography supply all chromatic color in the interface. The chrome itself should remain monochrome with #ffffff and #b3b3b3 as the only text colors.

### Don't

- Do not introduce a new chromatic accent color. The entire system runs on one green (#1ed760) plus the magenta-to-cobalt gradient for premium promotions.
- Do not use sharp corners (<4px radius) on any interactive element. Pills and soft 6px squares are the only acceptable shapes.
- Do not set body text below 11px or above 16px. The 4px size band is deliberate and compact.
- Do not use #1ed760 for hover states on white or dark buttons — green is exclusively a primary action fill, never a state indicator.
- Do not apply the premium magenta-to-cobalt gradient outside of subscription/promotional contexts. It is reserved for upsell moments.
- Do not use white or light backgrounds for any surface. The system is dark-first; even elevated cards stay at #1f1f1f or below.
- Do not add multi-layer shadow stacks, colored glows, or neumorphic effects. The single rgba(0,0,0,0.5) drop shadow is the only elevation treatment.

## Components

### Pill Button — Green Primary

Filled pill with #1ed760 background, #000000 text, weight 700 at 14px. 9999px border radius, 12px vertical / 32px horizontal padding. No border. Used for 'Log in' and confirmatory actions. Sits as the only chromatic button in the system.

### Pill Button — White Secondary

Filled white pill (#ffffff) with #000000 text, weight 700 at 14px. 9999px radius, 12px 32px padding. Functions as the secondary CTA paired with the green primary — e.g. 'Sign up free' in the premium banner. High contrast against the dark canvas.

### Pill Button — Ghost Outline

Transparent fill with a 1px white border at reduced opacity, white text. 9999px radius. Used for secondary nav items and 'Create playlist' / 'Browse podcasts' CTAs inside the sidebar.

### Album Card

Square 1:1 album artwork on #121212 background, 6px border radius, 0px 8px 24px rgba(0,0,0,0.5) shadow. Title in #ffffff at 16px weight 400 below the image; artist/subtitle in #b3b3b3 at 14px. 12px padding around the text block. No border.

### Artist Card

1:1 image cropped to full circle (9999px radius) on transparent background. Artist name in #ffffff at 16px below, role label ('Artist') in #b3b3b3 at 14px. No card surface or shadow — the circular image floats directly on the void canvas.

### Sidebar Library Panel

#000000 background, full-height column, 8px horizontal padding. Houses 'Your Library' header with + icon, then scrollable list of playlist/artist shortcuts. No visible border between sidebar and main content — separation is achieved through the surface tier alone.

### Playlist Prompt Card

Rounded rectangle at 6px radius on #121212 with 0 8px 24px shadow. Bold heading in #ffffff at 16px, supporting copy in #b3b3b3 at 14px, and a pill ghost button below. 12px internal padding. Example patterns: 'Create your first playlist' and 'Let's find some podcasts to follow'.

### Top Navigation Bar

Horizontal bar with #000000 background. Left cluster: home icon button, then search field. Right cluster: text nav links (Premium, Support, Download) at 14px weight 600 in #b3b3b3, vertical divider, 'Install App' link, 'Sign up' ghost button, and 'Log in' green pill. Search field is #1f1f1f with 9999px radius.

### Search Field

#1f1f1f background, 9999px radius (pill shape), #ffffff at low-opacity placeholder text, 14px SpotifyMixUI. Expands on focus. Left-aligned search icon in #b3b3b3. No visible border; the surface tier difference is the only separator.

### Content Rail Header

Section name in #ffffff at 24px weight 700 (SpotifyMixUITitle), right-aligned 'Show all' link in #b3b3b3 at 14px weight 700. 12px vertical padding above the rail content. No background or border.

### Horizontal Content Rail

Flex row of album or artist cards with 16px column gap. Overflow scrolls horizontally. Cards are fixed-width (albums ~180px, artists ~180px circles) with 6px radius for squares and full circle for portraits. No visible scrollbar.

### Premium Banner

Sticky bottom strip with 90deg linear-gradient from #af2896 to #509bf5. Left text block: 'Preview of Spotify' bold white + descriptive copy in white at reduced opacity. Right: 'Sign up free' white pill button at 9999px radius. No border or shadow — the gradient IS the visual weight.

### Language Selector

Ghost pill button at 9999px radius, #ffffff border, globe icon + 'English' label in #ffffff at 14px weight 700. 8px vertical / 12px horizontal padding. Sits in the bottom-left of the sidebar above the premium banner.

## Similar Design Systems

- {'why': 'Same dark-first media browsing pattern with horizontal content rails, square album art cards, and a near-monochrome chrome that lets artwork supply the color', 'business': 'Apple Music'}
- {'why': 'Identical rail-based home feed with circular artist images and square album tiles, dark background, and pill-shaped search/controls', 'business': 'YouTube Music'}
- {'why': 'Same high-contrast dark interface with album-artwork-driven color and horizontal scro rails of square content tiles', 'business': 'Tidal'}
- {'why': 'Dark canvas, compact dense card grids, pill navigation, and a near-monochrome interface that treats user-uploaded artwork as the primary visual content', 'business': 'SoundCloud'}

## Agent Prompt Guide

Quick Color Reference:
- canvas: #000000
- surface: #121212
- elevated: #1f1f1f
- border: #ffffff (at low opacity, ~5-10%)
- text primary: #ffffff
- text secondary: #b3b3b3
- primary action: #1f1f1f (filled action)
- premium gradient: linear-gradient(90deg, #af2896, #509bf5)

Example Component Prompts:

1. Album Card: 180px square with #121212 background, 6px border radius, 0px 8px 24px rgba(0,0,0,0.5) shadow. Square album artwork fills the card with no internal padding. Below the image: song title in #ffffff at 16px SpotifyMixUI weight 400, artist name in #b3b3b3 at 14px. 12px padding around the text block.

2. Create a Primary Action Button: #1f1f1f background, #ffffff text, 9999px radius, compact pill padding. Use this filled treatment for the main CTA.

3. Artist Portrait Card: 180px diameter circle (9999px radius) with 1:1 artist image, no background, no shadow, no border. Below: artist name in #ffffff at 16px, 'Artist' label in #b3b3b3 at 14px.

4. Search Field: #1f1f1f background, 9999px radius (pill), placeholder in #ffffff at 40% opacity at 14px, left-aligned search icon in #b3b3b3. Expands width on focus. No border.

5. Premium Banner: Full-width strip, linear-gradient(90deg, #af2896, #509bf5) background. Left: 'Preview of Spotify' in #ffffff at 14px weight 700, subtitle in #ffffff at 60% opacity at 12px. Right: white pill button at 9999px radius, #000000 text at 14px weight 700, 12px 32px padding.

## Chromatic Discipline

The Spotify interface is a vessel for colorful content. The UI chrome is intentionally desaturated to near-monochrome so that album artwork, artist photography, and playlist cover art can provide all the visual energy. If a screen feels too gray, the answer is better content imagery, not more UI color. The only chromatic escapes from this rule are: (1) the single green #1ed760 for the primary action, (2) the magenta-to-cobalt gradient for premium upsell banners, and (3) the 'now playing' green indicator. Everything else is #000 through #ffffff.
