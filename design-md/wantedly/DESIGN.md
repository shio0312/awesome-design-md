# Design System Inspiration of Wantedly

## 1. Visual Theme & Atmosphere

Wantedly's design embodies the philosophy of "共感でつながる" (connecting through empathy) — a professional yet approachable business social network that bridges the gap between corporate formality and human warmth. The interface feels like a modern Japanese office space: clean, organized, and subtly sophisticated without being intimidating.

The design language centers around a carefully balanced neutral palette anchored by a distinctive teal brand color (`#006f8e`) that feels both trustworthy and forward-thinking. Unlike the stark whites of traditional business platforms, Wantedly employs soft, translucent backgrounds (`rgba(0, 0, 0, 0.06)`) that create gentle layering and visual hierarchy without harsh contrasts.

The typography strategy is distinctly international — Poppins for headings brings a friendly, geometric warmth, while the comprehensive Japanese font stack ensures perfect readability across all devices. The generous line-heights (1.5-1.57x) create breathing room that makes dense information feel approachable, reflecting Japanese design principles of negative space and visual comfort.

What sets Wantedly apart is its subtle use of transparency and soft edges. Input fields use translucent black overlays rather than solid colors, buttons have gentle 4px border-radius, and the overall spacing system creates a rhythm that feels both professional and human-centered.

**Key Characteristics:**
- Teal brand identity (`#006f8e`) — professional yet approachable
- Soft transparency system using `rgba(0, 0, 0, 0.06)` for backgrounds
- International typography: Poppins + comprehensive Japanese font stack
- Generous line-heights (1.5-1.57x) for comfortable reading
- Subtle 4px border-radius system for gentle, modern edges
- Neutral-first color palette with strategic brand color usage
- Clean, spacious layouts reflecting Japanese design sensibilities

## 2. Color Palette & Roles

### Primary
- **Wantedly Teal** (`#006f8e` / `rgb(0, 111, 142)`): The core brand color used for links, primary actions, and brand moments. A sophisticated teal that balances professionalism with approachability.
- **Text Primary** (`#24282a` / `rgb(36, 40, 42)`): The main text color — a warm near-black that's easier on the eyes than pure black while maintaining excellent readability.

### Surface & Background
- **Soft Overlay** (`rgba(0, 0, 0, 0.06)`): The signature translucent background used for input fields and subtle surface differentiation. Creates gentle layering without harsh contrasts.
- **Text Overlay** (`rgba(0, 0, 0, 0.84)`): High-contrast text on translucent backgrounds, maintaining readability while preserving the soft aesthetic.
- **Pure Transparent** (`rgba(0, 0, 0, 0)`): Used for button backgrounds and clean surface areas.

### Neutrals & Text
- **Primary Text** (`rgb(36, 40, 42)`): Main body text and headings
- **Link Text** (`rgb(0, 111, 142)`): All interactive text elements and navigation
- **Input Text** (`rgba(0, 0, 0, 0.84)`): Form field text with slight transparency for visual hierarchy

## 3. Typography Rules

### Font Families
- **Headings**: `Poppins, "Helvetica Neue", Helvetica, Arial, "Hiragino Sans", ヒラギノ角ゴシック, "Hiragino Kaku Gothic ProN", "ヒラギノ角ゴ Pro W3", "Noto Sans JP", Roboto, メイリオ, Meiryo, "ＭＳ Ｐゴシック", sans-serif`
- **Body Text**: `"Helvetica Neue", Helvetica, Arial, "Hiragino Sans", ヒラギノ角ゴシック, "Hiragino Kaku Gothic ProN", "ヒラギノ角ゴ Pro W3", Roboto, メイリオ, Meiryo, "ＭＳ Ｐゴシック", sans-serif`
- **Forms**: `Lato, "Helvetica Neue", Helvetica, Arial, "Hiragino Sans", ヒラギノ角ゴシック, "Hiragino Kaku Gothic ProN", "ヒラギノ角ゴ Pro W3", "Noto Sans JP", Roboto, メイリオ, Meiryo, "ＭＳ Ｐゴシック", sans-serif`

### Typography Scale
- **H1 Lead**: 28px / 400 weight / 42px line-height (1.5x) / 88px top margin
- **Body Text**: 14px / 400 weight / 22px line-height (1.57x)
- **Form Inputs**: 16px / 400 weight / 27.36px line-height (1.71x)

### Spacing Rules
- **Letter Spacing**: Normal (no custom tracking)
- **Paragraph Margins**: 0px (controlled by parent containers)
- **Heading Margins**: Large top margins (88px for H1) for section separation

## 4. Component Stylings

### Input Fields
```css
background-color: rgba(0, 0, 0, 0.06);
color: rgba(0, 0, 0, 0.84);
font-family: Lato, [font-stack];
font-size: 16px;
line-height: 27.36px;
border-radius: 4px;
padding: 6px 12px;
margin: 0px;
```

### Buttons (Touch Areas)
```css
color: rgb(0, 111, 142);
background-color: rgba(0, 0, 0, 0);
font-size: 14px;
font-weight: 400;
line-height: 22px;
border-radius: 0px; /* Clean, minimal approach */
padding: 6px 4px;
margin: 1px 0px;
```

### Banner/Card Elements
```css
border-radius: 11.08px; /* Larger radius for card-like elements */
color: rgb(0, 111, 142); /* Brand color for interactive elements */
```

### Links
```css
color: rgb(0, 111, 142);
text-decoration: none; /* Implied from clean appearance */
```

## 5. Layout Principles

### Spacing System
- **Micro Spacing**: 1px margins for fine adjustments
- **Small Spacing**: 4px padding for compact elements
- **Medium Spacing**: 6px padding for form elements
- **Large Spacing**: 12px padding for input fields
- **Section Spacing**: 88px top margins for major sections

### Container Principles
- Clean, minimal margins (mostly 0px with strategic exceptions)
- Consistent 6px vertical padding for interactive elements
- Form elements use 12px horizontal padding for comfortable interaction

### Border Radius System
- **Subtle**: 4px for form inputs and small elements
- **Prominent**: 11.08px for banner/card elements
- **Minimal**: 0px for buttons (clean, modern approach)

## 6. Depth & Elevation

### Shadow System
- **No Shadows**: Wantedly uses a flat design approach with `box-shadow: none` across all elements
- **Depth through Color**: Layering achieved through translucent backgrounds rather than shadows
- **Transparency Layers**: `rgba(0, 0, 0, 0.06)` and `rgba(0, 0, 0, 0.84)` create visual hierarchy

### Layering Philosophy
- Surface differentiation through background transparency
- No traditional elevation shadows
- Clean, flat aesthetic with subtle depth through color opacity

## 7. Do's and Don'ts

### Do's
- Use the translucent overlay system (`rgba(0, 0, 0, 0.06)`) for subtle backgrounds
- Maintain generous line-heights (1.5x+) for readability
- Apply consistent 4px border-radius for form elements
- Use Poppins for headings to maintain international appeal
- Leverage the comprehensive Japanese font stack for localization
- Keep button backgrounds transparent for clean aesthetics

### Don'ts
- Don't use harsh shadows or strong elevation effects
- Don't use pure black text — stick to the warm near-black (`#24282a`)
- Don't ignore the 88px section spacing for major content breaks
- Don't use border-radius on standard buttons (keep them clean at 0px)
- Don't use colors outside the established neutral + teal palette
- Don't compress line-heights below 1.5x

## 8. Responsive Behavior

### Typography Scaling
- Form inputs maintain 16px size for mobile usability
- Body text at 14px provides good density across devices
- Line-heights remain consistent for comfortable reading

### Touch Targets
- Button padding of 6px provides adequate touch area
- 1px margins allow for precise spacing control
- Touch-area class suggests enhanced mobile interaction zones

### Font Loading Strategy
- Progressive font stack ensures immediate rendering
- Poppins loads first for headings, falls back gracefully
- Japanese fonts prioritized in stack for local users

## 9. Agent Prompt Guide

### Quick Reference
```
Brand Color: #006f8e (teal)
Text Color: #24282a (warm near-black)
Background: rgba(0, 0, 0, 0.06) (soft overlay)
Border Radius: 4px (inputs), 11px (cards), 0px (buttons)
Typography: Poppins (headings), Helvetica Neue (body), Lato (forms)
Spacing: 6px padding, 12px input padding, 88px section margins
```

### Recommended Prompts
- "Create a Wantedly-style input field with soft translucent background"
- "Design a clean button with teal text and transparent background"
- "Build a card component with 11px border-radius and generous spacing"
- "Style a form using Lato font with 16px size and comfortable line-height"
- "Create a section header with Poppins font and 88px top margin"

### Component Patterns
- **Forms**: Translucent backgrounds, Lato typography, 4px radius
- **Buttons**: Transparent backgrounds, teal text, minimal styling
- **Cards**: Larger border-radius (11px), brand color accents
- **Typography**: Generous line-heights, international font stacks
- **Layout**: Clean margins, strategic spacing, flat design approach