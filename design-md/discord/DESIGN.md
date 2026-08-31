# Discord — Design System

> **North Star**: Game world behind a chat bubble — every section is a self-contained environment with its own lighting and cast of characters.
> **Theme**: dark
> **Source**: https://discord.com
> **Refero Style**: https://styles.refero.design/style/faec4b0c-cf93-4150-97de-0a8e7eed1840
> **Synced**: 2026-09-01

## Overview

Deep cosmic blue fills every section like a starfield at 2am — not a background choice but a total environment. The hero plunges into a rich indigo-to-navy gradient populated with 3D characters, product screens, and floating mascots, making the UI feel like a game world rather than a marketing page. Blurple (#5865F2) — Discord's owned hue — appears only on primary CTAs, creating a controlled pop against the blue-black atmosphere. Typography does the heavy lifting: ABC Ginto Nord at weight 800 with tight -0.01em tracking slams headlines into all-caps blocks that feel like stamped metal, while body copy at 16px/1.5 stays conversational. The overall effect is a gaming-native space where every section is its own immersive stage, not a content column.

## Color Palette

- **Blurple**: `#5865f2` — Primary CTA buttons, brand icon, active states — the single chromatic anchor in a near-monochrome blue-black space, creating instant recognition as the only saturated element in the layout [brand]
- **Dark Blurple**: `#3442d9` — Hover state for primary buttons, pressed states [brand]
- **Hover Blurple**: `#8891f2` — Button hover tint, elevated blurple interactions [brand]
- **Spring Green**: `#57f287` — Online status indicators, success states [semantic]
- **Fuchsia**: `#eb459` — Nitro gradient accents, special event highlights [accent]
- **Vivid Cerulean**: `#00b0f4` — Voice/video channel indicators, info states [accent]
- **Ember Orange**: `#fda220` — Quest indicators, achievement highlights [accent]
- **Ekko Red**: `#de2761` — Destructive actions, critical alerts [semantic]
- **Void**: `#000000` — Text on light surfaces, icon fills, overlay backgrounds [neutral]
- **Snow**: `#ffffff` — Primary text on dark backgrounds, button text, nav links, card backgrounds [neutral]
- **Not Quite Black**: `#23272a` — Secondary button text and borders, dark UI surface color [neutral]
- **Dark Charcoal**: `#2c2f33` — App UI chrome surfaces, elevated dark panels [neutral]
- **Graphite**: `#333333` — Tertiary text on light surfaces, image overlays [neutral]
- **Fog**: `#babcd9` — Subdued headings and body text on dark backgrounds — a lavender-tinted neutral that stays on-brand while reducing contrast [neutral]
- **Greyple**: `#99aab5` — Disabled states, placeholder text, muted metadata [neutral]
- **Dim Grey**: `#50555f` — Input borders, dividers, secondary icon fills [neutral]
- **Off White**: `#f6f6f6` — Light section backgrounds, card surfaces in light contexts [neutral]

## Typography

- **ABC Ginto Nord Discord**
- **ABC Ginto Discord**
- **GG Sans**
- **ABC Ginto Normal**

## Type Scale

| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| body | 16 | — | 1.5 |
| body-lg | 20 | — | 1.38 |
| heading-sm | 36 | — | 1.2 |
| heading | 48 | — | 0.93 |
| heading-lg | 56 | — | 0.86 |
| display | 61 | — | 0.86 |

## Spacing & Layout

- **Max Width**: 1200px
- **Card Padding**: 32-48px
- **Element Gap**: 8-16px
- **Section Gap**: 80-120px
- **Border Radius**: {'cards': '16px', 'pills': '104px', 'buttons': '12px', 'buttonsLarge': '16px', 'featurePanels': '24px'}

## Layout

Full-bleed at the page level with no explicit max-width container visible — the deep blue background extends edge-to-edge. Hero is a split composition: text block flush-left with 3D product composite filling the right half, both contained within viewport height. Feature sections below the hero use large-radius cards (~24px) that span 80-90% of the viewport width, each card being a self-contained stage. Within cards, layout is 50/50 split — product screenshot left, headline + body right (or reversed). No alternating light/dark band rhythm — all sections share the same dark background; differentiation comes from card background colors. Navigation is a fixed-top full-width bar with centered link groups. Footer uses a 4-5 column link grid. The page is extremely long (7300px+), with generous inter-section gaps of 80-120px giving each feature room to breathe.

## Surfaces / Elevation

- **Cosmic Page**
- **App Chrome**
- **App Surface**
- **Feature Card**

## Imagery

Entirely 3D illustration and product screenshots — no photography. Characters are rendered in a cartoon-realistic 3D style with soft subsurface lighting, purple-blue-tinted shadows, and saturated clothing colors (orange, lavender, pink hoodie). They're posed mid-gesture and placed off-axis against the page, creating dynamism without a static layout grid. Product screenshots are composited into device frames (monitor bezel, phone outline) rendered in the same 3D style, making the 'product demo' feel like part of the illustration world rather than a flat screen-grab. Feature cards use full-bleed gradient backgrounds (purple-to-magenta, deep green) as the canvas for these screenshot composites — the gradient IS the scene lighting. Floating 3D props (a peach, a crystal, a robot mascot in lime green) appear at section boundaries as scene accessories. Zero photography — the visual world is entirely constructed, reinforcing that Discord is a space you build rather than a place that exists.

## Design Principles

### Do

- Use ABC Ginto Nord 800 in all-caps for all section headlines; letter-spacing must be -0.01em to maintain the compressed rectangular silhouette.
- Keep #5865F2 (Blurple) exclusively on primary CTA buttons and interactive focus states — it is the only saturated color with a guaranteed role on every page.
- Set feature section cards with their own gradient or solid background color (purple-magenta, green, etc.) to differentiate sections, since the global page background never changes.
- Pair the blurple CTA button with a white filled secondary button using padding 15px 24px and radius 12px — never use blurple for both primary and secondary in the same CTA cluster.
- Position 3D characters and mascot assets at card edges, overlapping between sections — the overlap is what creates the immersive environment, not isolated placement.
- Apply 12px border-radius to standard buttons and 16px to the Log In/header button to maintain the subtle size hierarchy between interaction contexts.
- Use the Fog color (#BABCD9) for body text in dark sections where full white (#FFFFFF) would overpower headlines — reserve pure white for headlines and critical UI labels.

### Don't

- Never use a white or light-gray page background — the deep blue-black environment is non-negotiable for the brand atmosphere; even light-themed sections should be contained within cards.
- Never apply ABC Ginto Nord headlines at mixed-case — the all-caps + tight tracking combination is inseparable from the visual identity.
- Never place Blurple as a background color on large areas (sections, cards) — at scale it overwhelms the controlled accent role and collapses contrast with Blurple text.
- Never use gradient text on headlines — the weight and mass of the black-filled letterforms is the visual statement; gradients would undermine the stamped-metal quality.
- Never add drop shadows to feature cards — section identity comes from contrasting card backgrounds, not elevation shadow depth.
- Never reduce button border-radius below 12px — anything sharper breaks the rounded-corner system that softens the otherwise heavy typographic tone.
- Never use Greyple (#99AAB5) or Dim Grey (#50555F) as primary text colors — they are reserved for disabled, muted, and placeholder states only.

## Components

### CTA Button Group

```html
<style>:root{--color-blurple:#5865f2;--color-dark-blurple:#3442d9;--color-snow:#ffffff;--color-not-quite-black:#23272a;--font-abc-ginto-nord-discord:'Nunito',sans-serif;--font-abc-ginto-discord:'Inter',sans-serif;}*{box-sizing:border-box;margin:0;padding:0;}</style><div style="background:linear-gradient(135deg,#0e0f2d 0%,#1a1d5e 50%,#0a0b1e 100%);padding:60px 40px;display:flex;flex-direction:column;align-items:center;gap:32px;font-family:var(--font-abc-ginto-discord);min-height:220px;justify-content:center;"><p style="color:var(--color-snow);font-family:var(--font-abc-ginto-nord-discord);font-size:28px;font-weight:800;letter-spacing:-0.01em;text-transform:uppercase;text-align:center;line-height:1.1;margin-bottom:4px;">YOUR PLACE TO TALK</p><p style="color:rgba(186,188,217,0.9);font-family:var(--font-abc-ginto-discord);font-size:16px;font-weight:400;line-height:1.5;text-align:center;max-width:360px;">Whether you're part of a school club, gaming group, or worldwide community — Discord is your place to talk.</p><div style="display:flex;gap:16px;flex-wrap:wrap;justify-content:center;"><a href="#" style="display:inline-flex;align-items:center;gap:10px;background:var(--color-snow);color:var(--color-not-quite-black);font-family:var(--font-abc-ginto-discord);font-size:16px;font-weight:500;letter-spacing:0.013em;text-decoration:none;padding:15px 24px;border-radius:12px;border:1px solid var(--color-not-quite-black);white-space:nowrap;transition:background 0.2s;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L12 16M12 16L7 11M12 16L17 11" stroke="#23272a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 20H20" stroke="#23272a" stroke-width="2.5" stroke-linecap="round"/></svg>Download for Mac</a><a href="#" style="display:inline-flex;align-items:center;background:var(--color-blurple);color:var(--color-snow);font-family:var(--font-abc-ginto-discord);font-size:16px;font-weight:500;letter-spacing:0.013em;text-decoration:none;padding:19.5px 24px;border-radius:12px;border:none;white-space:nowrap;transition:background 0.2s;">Open Discord in your browser</a></div></div>
```

### Feature Showcase Card — Make Your Group Chats More Fun

```html
<style>:root{--color-snow:#ffffff;--color-fog:#babcd9;--color-blurple:#5865f2;--font-abc-ginto-nord-discord:'Nunito',sans-serif;--font-abc-ginto-discord:'Inter',sans-serif;}*{box-sizing:border-box;margin:0;padding:0;}</style><div style="background:linear-gradient(160deg,#0e0f2d 0%,#1a1060 100%);padding:32px 24px;font-family:var(--font-abc-ginto-discord);"><div style="background:linear-gradient(135deg,#5a1a5a 0%,#8b1a8b 30%,#d91aaa 60%,#e020c0 100%);border-radius:24px;padding:40px 32px;display:flex;flex-direction:column;gap:32px;position:relative;overflow:hidden;"><div style="background:rgba(255,255,255,0.08);border-radius:16px;padding:20px;backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,0.12);"><div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.15);"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M15 19l-7-7 7-7" stroke="rgba(255,255,255,0.7)" stroke-width="2" stroke-linecap="round"/></svg><span style="color:rgba(255,255,255,0.85);font-size:13px;font-weight:500;"># main-chat</span><svg style="margin-left:auto" width="14" height="14" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="rgba(255,255,255,0.7)" stroke-width="2"/><path d="M20 20l-3-3" stroke="rgba(255,255,255,0.7)" stroke-width="2" stroke-linecap="round"/></svg></div><div style="display:flex;flex-direction:column;gap:8px;"><div style="height:10px;background:rgba(255,255,255,0.2);border-radius:6px;width:75%;"></div><div style="height:10px;background:rgba(255,255,255,0.13);border-radius:6px;width:90%;"></div><div style="height:10px;background:rgba(255,255,255,0.17);border-radius:6px;width:60%;"></div><div style="height:10px;background:rgba(255,255,255,0.1);border-radius:6px;width:80%;"></div></div><div style="display:flex;gap:8px;margin-top:16px;"><div style="background:rgba(255,255,255,0.18);border-radius:8px;padding:6px 14px;font-size:12px;color:rgba(255,255,255,0.8);">Send</div><div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:6px 14px;font-size:12px;color:rgba(255,255,255,0.6);">GIFs</div><div style="background:rgba(255,255,255,0.1);border-radius:8px;padding:6px 14px;font-size:12px;color:rgba(255,255,255,0.6);">Stickers</div></div><div style="margin-top:12px;background:rgba(255,255,255,0.08);border-radius:8px;padding:8px 12px;display:flex;align-items:center;gap:8px;"><svg width="12" height="12" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="rgba(255,255,255,0.5)" stroke-width="2"/><path d="M20 20l-3-3" stroke="rgba(255,255,255,0.5)" stroke-width="2" stroke-linecap="round"/></svg><span style="font-size:12px;color:rgba(255,255,255,0.45);">Find an emoji...</span></div><div style="margin-top:10px;"><p style="font-size:11px;color:rgba(255,255,255,0.4);margin-bottom:6px;">Frequently Used</p><div style="display:flex;gap:8px;"><div style="width:28px;height:28px;background:rgba(255,255,255,0.12);border-radius:6px;"></div><div style="width:28px;height:28px;background:rgba(255,255,255,0.12);border-radius:6px;"></div><div style="width:28px;height:28px;background:rgba(255,255,255,0.12);border-radius:6px;"></div><div style="width:28px;height:28px;background:rgba(255,255,255,0.12);border-radius:6px;"></div></div></div></div><div style="display:flex;flex-direction:column;gap:12px;"><h2 style="font-family:var(--font-abc-ginto-nord-discord);font-size:36px;font-weight:800;color:var(--color-snow);text-transform:uppercase;letter-spacing:-0.01em;line-height:1.1;">MAKE YOUR GROUP CHATS MORE FUN</h2><p style="font-family:var(--font-abc-ginto-discord);font-size:16px;font-weight:400;color:var(--color-snow);line-height:1.55;opacity:0.92;">Use custom emoji, stickers, soundboard effects and more to add your personality to your voice, video, or text chat. Set your avatar and a custom status, and write your own profile to show up in chat your way.</p></div></div></div>
```

### Feature Showcase Card — Always Have Something To Do Together

```html
<style>:root{--color-snow:#ffffff;--color-fog:#babcd9;--color-blurple:#5865f2;--font-abc-ginto-nord-discord:'Nunito',sans-serif;--font-abc-ginto-discord:'Inter',sans-serif;}*{box-sizing:border-box;margin:0;padding:0;}</style><div style="background:linear-gradient(160deg,#0e0f2d 0%,#1a1060 100%);padding:32px 24px;font-family:var(--font-abc-ginto-discord);"><div style="background:linear-gradient(145deg,#0d3320 0%,#0f4a28 40%,#155e30 70%,#1a7a3a 100%);border-radius:24px;padding:36px 28px;display:flex;flex-direction:column;gap:28px;"><div style="background:rgba(0,0,0,0.25);border-radius:16px;padding:16px;border:1px solid rgba(255,255,255,0.1);"><div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,0.12);"><div style="display:flex;align-items:center;gap:6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="rgba(255,255,255,0.7)" stroke-width="2" stroke-linecap="round"/></svg><span style="color:rgba(255,255,255,0.85);font-size:13px;font-weight:600;">The Lounge</span><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M6 9l6 6 6-6" stroke="rgba(255,255,255,0.6)" stroke-width="2" stroke-linecap="round"/></svg></div><div style="display:flex;gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5" stroke="rgba(255,255,255,0.6)" stroke-width="2" stroke-linecap="round"/></svg><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="rgba(255,255,255,0.6)" stroke-width="2"/><path d="M15.5 12a3.5 3.5 0 11-7 0 3.5 3.5 0 017 0z" fill="rgba(255,255,255,0.6)"/></svg></div></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;"><div style="background:rgba(60,60,80,0.7);border-radius:10px;height:90px;position:relative;overflow:hidden;"><div style="position:absolute;bottom:6px;left:6px;background:rgba(0,0,0,0.5);border-radius:4px;padding:2px 6px;font-size:11px;color:white;">z_lot</div></div><div style="background:rgba(80,40,80,0.7);border-radius:10px;height:90px;position:relative;overflow:hidden;"><div style="position:absolute;bottom:6px;left:6px;background:rgba(0,0,0,0.5);border-radius:4px;padding:2px 6px;font-size:11px;color:white;">Olive</div></div><div style="background:rgba(40,40,60,0.7);border-radius:10px;height:90px;position:relative;overflow:hidden;"><div style="background:#2a9d3c;border-radius:6px;padding:8px;margin:12px auto;width:calc(100% - 24px);display:flex;align-items:center;gap:6px;"><div style="width:18px;height:14px;background:#ff0000;border-radius:3px;display:flex;align-items:center;justify-content:center;"><svg width="8" height="8" viewBox="0 0 12 12"><polygon points="4,2 10,6 4,10" fill="white"/></svg></div><span style="font-size:10px;font-weight:700;color:white;">YouTube</span></div><div style="position:absolute;bottom:6px;left:6px;background:rgba(0,0,0,0.5);border-radius:4px;padding:2px 6px;font-size:11px;color:white;display:flex;align-items:center;gap:3px;"><svg width="8" height="8" viewBox="0 0 24 24" fill="none"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" stroke="white" stroke-width="2"/><circle cx="9" cy="7" r="4" stroke="white" stroke-width="2"/></svg>1-16</div></div><div style="background:rgba(50,30,70,0.7);border-radius:10px;height:90px;position:relative;overflow:hidden;"><div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;"><div style="background:rgba(255,255,255,0.9);border-radius:8px;padding:5px 9px;display:flex;align-items:center;gap:5px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="18" height="18" rx="3" stroke="#333" stroke-width="2"/><path d="M9 9h6M9 15h6" stroke="#333" stroke-width="2" stroke-linecap="round"/></svg><span style="font-size:10px;font-weight:600;color:#23272a;">Share your screen</span></div></div><div style="position:absolute;bottom:6px;left:6px;background:rgba(0,0,0,0.5);border-radius:4px;padding:2px 6px;font-size:11px;color:white;">moongirl</div></div></div><div style="display:flex;justify-content:center;gap:12px;margin-top:8px;"><div style="width:36px;height:36px;background:rgba(255,255,255,0.15);border-radius:50%;display:flex;align-items:center;justify-content:center;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M15.5 8.5a4 4 0 010 7M19 5a9 9 0 010 14" stroke="white" stroke-width="2" stroke-linecap="round"/></svg></div><div style="width:36px;height:36px;background:rgba(255,255,255,0.15);border-radius:50%;display:flex;align-items:center;justify-content:center;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><line x1="1" y1="1" x2="23" y2="23" stroke="white" stroke-width="2"/><path d="M9 9v3a3 3 0 005.12 2.12M15 9.34V4a3 3 0 00-5.94-.6" stroke="white" stroke-width="2" stroke-linecap="round"/></svg></div><div style="width:36px;height:36px;background:rgba(255,255,255,0.15);border-radius:50%;display:flex;align-items:center;justify-content:center;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" stroke="white" stroke-width="2" stroke-linecap="round"/></svg></div><div style="width:36px;height:36px;background:#ed4245;border-radius:50%;display:flex;align-items:center;justify-content:center;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11" stroke="white" stroke-width="2.5" stroke-linecap="round"/></svg></div></div></div><div style="display:flex;flex-direction:column;gap:12px;"><h2 style="font-family:var(--font-abc-ginto-nord-discord);font-size:34px;font-weight:800;color:var(--color-snow);text-transform:uppercase;letter-spacing:-0.01em;line-height:1.1;">ALWAYS HAVE SOMETHING TO DO TOGETHER</h2><p style="font-family:var(--font-abc-ginto-discord);font-size:16px;font-weight:400;color:var(--color-snow);line-height:1.55;opacity:0.9;">Watch videos, play built-in games, listen to music, or just scroll together and spam memes. Seamlessly text, call, video chat, and play games, all in one group chat.</p></div></div></div>
```

### Primary CTA Button (Blurple Filled)

backgroundColor #5865F2, color #FFFFFF, borderRadius 12px, padding 19.5px 24px. No border visible — the blurple fill is self-contained. Hover shifts to #3442D9. The 19.5px vertical padding makes this the tallest button variant on the page — physically dominant in the CTA pair.

### Secondary CTA Button (White Filled)

backgroundColor #FFFFFF, color #23272A, borderRadius 12px, padding 15px 24px. A clean white pill against the dark background — high contrast without blurple. Border is #23272A at 1px. The softer padding (vs primary) visually subordinates it as the secondary choice.

### Ghost Navigation Button (Transparent Outlined)

backgroundColor transparent, color #FFFFFF, border 1px solid #FFFFFF, borderRadius 12px, padding 10px 16px. Used for nav menu items with dropdown arrows. The all-white outline on dark keeps it visible without competing with blurple.

### Log In Button (White Outlined)

backgroundColor #FFFFFF, color #000000, border 1px solid #000000, borderRadius 16px, padding 10px 16px. Uses a larger 16px radius than other buttons — matches the pill-like header style. Appears on the light/frosted header strip, making the filled white surface legible against the nav background.

### Feature Showcase Card

Large rounded containers with 24px+ radius, set against the page's deep blue background. Each card uses its own gradient or solid background (purple-to-magenta for 'Group Chats', green for 'Watch Together') — section identity is expressed through the card background color, not the page background. Content splits 50/50: product screenshot left, text right. Cards span full viewport width on mobile, max ~1100px on desktop.

### 3D Character Float

Not interactive UI — these are 3D-rendered PNG/WebP assets positioned absolutely at section boundaries, overlapping card edges. Sizes range from ~100px to ~300px. They exit and enter sections unpredictably, creating the 'world' atmosphere. No background, no border, no radius — raw edge compositing into the page.

### Product Screen Mock-up

Screenshots of the actual Discord app rendered inside feature cards with 12-16px radius. They float slightly off-center with a subtle drop shadow. Mobile frames shown as phone outlines. Desktop frames shown as monitor bezels. The mock-ups use the real Discord dark UI (#2C2F33 surface, #23272A sidebar), grounding marketing claims in the actual product.

### Navigation Bar

Fixed header spanning full viewport width. Background is semi-transparent over the hero image — appears near-white/frosted. Contains Discord wordmark left, text nav links center (16px ABC Ginto, #FFFFFF or #000000 depending on scroll state), and 'Log In' button far right. Dropdown triggers use the ghost outlined button variant. No visible shadow — floats as a flat strip.

### Hero Section

Full-bleed dark indigo background (#0E0F2D to near-black gradient implied). Headline in ABC Ginto Nord 800 at 56-61px, color #FFFFFF, all-caps, line-height 0.86, crammed into the left 50% of the viewport. Body copy at 16px ABC Ginto 400, color #FFFFFF, max-width ~380px. CTA pair (white + blurple buttons) sits below body. Right 50% holds the product mock-up composite with 3D characters overlapping both halves.

### Footer Navigation

Dark background (#23272A or #000000). Multi-column link grid with group headings in 16px ABC Ginto 500 + positive letter-spacing. Link text at 16px/1.5 weight 400, color #BABCD9 (Fog) on dark. Discord wordmark and social icons top-left. No dividers — columns separated by gap only.

## Similar Design Systems

- {'why': 'Same all-caps heavy display type + 3D character mascots as primary visual storytelling, placed loosely against colored environments', 'business': 'Roblox'}
- {'why': 'Deep purple-dominant dark theme with a single vivid brand accent color reserved for CTAs, gaming-community audience', 'business': 'Twitch'}
- {'why': 'Full-bleed dark environments, product screenshot composites inside illustrated frames, large-type section headers in white on near-black', 'business': 'Epic Games Store'}
- {'why': 'Saturated gradient card backgrounds as section differentiators within an otherwise monochromatic dark page structure', 'business': 'Spotify (gaming campaigns)'}
- {'why': '3D cartoon characters with subsurface-lit rendering, posed dynamically at section edges, overlapping layout containers', 'business': 'Supercell'}

## Agent Prompt Guide

**Quick Color Reference**
- Page background: #0E0F2D (deep indigo)
- Primary headline text: #FFFFFF
- Body text on dark: #BABCD9 (Fog)
- Primary CTA: #5865F2 (Blurple), white text
- Secondary CTA: #FFFFFF background, #23272A text
- Nav links: #FFFFFF
- Border / UI outlines: #FFFFFF (on dark) or #23272A (on light)

**Example Component Prompts**

1. **Hero Section**: Full-bleed background #0E0F2D. Left 50%: headline 'GROUP CHAT THAT'S ALL FUN & GAMES' in ABC Ginto Nord 800, 56px, #FFFFFF, all-caps, letter-spacing -0.56px, line-height 0.86. Subtext 16px ABC Ginto 400, #FFFFFF, max-width 380px, line-height 1.5. Below: two buttons — white filled (#FFFFFF bg, #23272A text, 12px radius, 15px 24px padding) + blurple filled (#5865F2 bg, #FFFFFF text, 12px radius, 19.5px 24px padding), gap 16px. Right 50%: product screen composite with 3D character overlaps.

2. **Feature Section Card** (purple variant): Card background linear-gradient from #8B31A0 to #E040A0, border-radius 24px, width 90vw centered, padding 48px. Left: Discord app screenshot in phone/desktop frame. Right: headline 'MAKE YOUR GROUP CHATS MORE FUN' in ABC Ginto Nord 800, 48px, #FFFFFF, all-caps, letter-spacing -0.48px. Body text 16px ABC Ginto 400, #FFFFFF, line-height 1.5, max-width 360px.

3. **Navigation Bar**: Full-width fixed bar, semi-transparent background. Left: Discord logo + wordmark. Center: text links in ABC Ginto 400 16px, #FFFFFF, gap 4-8px. Dropdown triggers as ghost buttons (transparent bg, #FFFFFF border 1px, 12px radius, 10px 16px padding). Far right: 'Log In' button (#FFFFFF bg, #000000 text, 16px radius, 10px 16px padding).

4. **Primary CTA Button**: backgroundColor #5865F2, color #FFFFFF, border none, borderRadius 12px, padding 19.5px 24px, font ABC Ginto 500 16px, letter-spacing 0.016em. Hover state: backgroundColor #3442D9.

5. **Footer Link Column**: Dark background #23272A. Column heading: ABC Ginto 500, 16px, #FFFFFF, letter-spacing 0.013em. Links: ABC Ginto 400, 16px, #BABCD9, line-height 1.5, gap 8px between items. 4-5 columns in a row, gap 32px between columns.

## Brand Color System

Discord's color palette is a deliberate two-tier system: a near-monochromatic dark environment (indigo-black page, white text, charcoal UI) plus a single owned hue — Blurple (#5865F2). Every other color (Spring Green for online, Fuchsia for Nitro, Cerulean for voice) appears only in contextual UI states or seasonal campaigns. This means new page designs should default to white text on dark backgrounds with Blurple as the ONLY chromatic element in the layout chrome. The extended palette (Fuchsia, Yellow, Orange, Green) is available for in-product UI mock-ups, illustration coloring, and special campaign moments — not for general page components.
