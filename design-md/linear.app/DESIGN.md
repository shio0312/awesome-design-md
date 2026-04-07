# Design System Inspiration of Linear

## 1. Visual Theme & Atmosphere

Linear's interface is a masterclass in engineering minimalism — a dark, precise workspace that feels more like a professional IDE than a traditional project management tool. The entire experience is built on a near-black canvas (`#08090a`) that creates an immersive, distraction-free environment where content and functionality take absolute precedence.

The signature aesthetic is "ultra-minimal precision" — every element is stripped to its essential function, with generous whitespace and surgical typography creating a sense of calm focus. The custom Inter Variable typeface provides perfect optical clarity at all sizes, with carefully tuned weights (400 for body, 510 for emphasis) that maintain readability in the dark interface without feeling heavy.

What makes Linear truly distinctive is its restrained use of the signature purple accent (`#5e6ad2`) — appearing only for critical interactive elements like primary buttons and focus states. This creates a visual hierarchy where the purple becomes a beacon of actionability in an otherwise monochromatic landscape. The warm white text (`#f7f8f8`) provides excellent contrast against the dark backgrounds while feeling softer than pure white.

The design language speaks "professional tool for serious work" — every border is precisely 1px, every radius is mathematically consistent (4px for small elements, 6px for larger ones), and spacing follows a strict 8px grid system. This systematic approach creates an interface that feels both human-crafted and algorithmically perfect.

**Key Characteristics:**
- Near-black primary surface (`#08090a`) creating an immersive, IDE-like environment
- Inter Variable as the sole typeface — engineered for maximum clarity and consistency
- Signature purple (`#5e6ad2`) used sparingly for maximum impact on key interactions
- Surgical precision in spacing, sizing, and alignment following strict 8px grid
- Warm neutrals (`#8a8f98`, `#f7f8f8`) preventing the harshness of pure grayscale
- Minimal visual noise — borders, shadows, and decorative elements used only when functionally necessary
- Engineering-first aesthetic that prioritizes clarity and efficiency over visual flourish

## 2. Color Palette & Roles

### Primary
- **Linear Black** (`#08090a`): The primary background color — a near-black that's warm enough to prevent eye strain during long work sessions while maintaining the professional dark theme aesthetic.
- **Linear Purple** (`#5e6ad2`): The signature brand color used exclusively for primary actions, focus states, and key interactive elements. A carefully balanced purple that's vibrant without being overwhelming.
- **Warm White** (`#f7f8f8`): Primary text color — a slightly warm white that provides excellent contrast against dark surfaces while being gentler than pure white.

### Secondary & Accent
- **Neutral Gray** (`#8a8f98`): Secondary text color and muted interface elements — a warm-toned gray that maintains hierarchy without disappearing into the background.
- **Focus Blue** (`#5e6ad2`): Used for focus rings and active states — actually the same as Linear Purple, showing the consistency of the minimal palette.

### Surface & Background
- **Primary Surface** (`#08090a`): The main background color used throughout the interface.
- **Secondary Surface** (`rgba(0, 0, 0, 0)`): Transparent overlays and secondary backgrounds that allow the primary surface to show through.

### Interactive States
- **Hover Purple** (`#6b77d9`): A slightly lighter version of the brand purple for hover states.
- **Active Purple** (`#5459c7`): A slightly darker version for active/pressed states.
- **Disabled Gray** (`#4a4f58`): Muted gray for disabled interactive elements.

### Semantic Colors
- **Success Green** (`#00d26a`): For positive states and success messages.
- **Warning Orange** (`#ff6b35`): For warnings and caution states.
- **Error Red** (`#ff5c5c`): For error states and destructive actions.

## 3. Typography Rules

### Font Family
- **Primary**: Inter Variable — A single, highly optimized variable font that handles all typographic needs from body text to headlines.
- **Fallback Stack**: "SF Pro Display", -apple-system, "system-ui", "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif

### Font Weights
- **400 (Regular)**: Body text, descriptions, secondary content
- **510 (Medium)**: Emphasized text, button labels, form labels
- **600 (Semi-bold)**: Headings, important labels, navigation items

### Type Scale
- **Display Large**: 48px / 56px line-height, weight 600, -0.02em letter-spacing
- **Display Medium**: 36px / 44px line-height, weight 600, -0.01em letter-spacing
- **Heading 1**: 28px / 36px line-height, weight 600, normal letter-spacing
- **Heading 2**: 24px / 32px line-height, weight 600, normal letter-spacing
- **Heading 3**: 20px / 28px line-height, weight 510, normal letter-spacing
- **Body Large**: 16px / 24px line-height, weight 400, normal letter-spacing
- **Body Medium**: 14px / 21px line-height, weight 400, normal letter-spacing
- **Body Small**: 13px / 19.5px line-height, weight 400, normal letter-spacing
- **Caption**: 12px / 18px line-height, weight 400, 0.01em letter-spacing

### Typography Hierarchy
- Headlines use weight 600 with tight letter-spacing for maximum impact
- Body text maintains weight 400 for optimal readability
- Interactive elements use weight 510 to indicate actionability
- All text follows the warm white (`#f7f8f8`) and neutral gray (`#8a8f98`) color system

## 4. Component Stylings

### Buttons
**Primary Button:**
- Background: `#5e6ad2` (Linear Purple)
- Text: `#ffffff` (White)
- Padding: `8px 16px`
- Border-radius: `6px`
- Font: 14px, weight 510
- Hover: `#6b77d9`
- Active: `#5459c7`
- Focus: `0 0 0 2px rgba(94, 106, 210, 0.3)`

**Secondary Button:**
- Background: `transparent`
- Text: `#8a8f98` (Neutral Gray)
- Border: `1px solid rgba(138, 143, 152, 0.2)`
- Padding: `8px 16px`
- Border-radius: `6px`
- Hover: Background `rgba(138, 143, 152, 0.1)`

**Ghost Button:**
- Background: `transparent`
- Text: `#8a8f98`
- Padding: `8px 12px`
- Border-radius: `4px`
- Hover: Background `rgba(138, 143, 152, 0.1)`

### Form Elements
**Input Fields:**
- Background: `rgba(247, 248, 248, 0.05)`
- Border: `1px solid rgba(138, 143, 152, 0.2)`
- Border-radius: `6px`
- Padding: `8px 12px`
- Font: 14px, weight 400
- Focus: Border `#5e6ad2`, box-shadow `0 0 0 2px rgba(94, 106, 210, 0.3)`

### Navigation
**Header Links:**
- Font: 13px, weight 400
- Color: `#8a8f98`
- Padding: `0px 12px`
- Border-radius: `4px`
- Hover: Background `rgba(138, 143, 152, 0.1)`

### Cards & Containers
**Standard Card:**
- Background: `rgba(247, 248, 248, 0.02)`
- Border: `1px solid rgba(138, 143, 152, 0.1)`
- Border-radius: `8px`
- Padding: `16px`
- Box-shadow: None (maintaining minimal aesthetic)

## 5. Layout Principles

### Grid System
- **Base Unit**: 8px — All spacing, sizing, and positioning follows multiples of 8px
- **Container Max-width**: 1200px with 24px horizontal padding
- **Column Grid**: 12-column flexible grid with 24px gutters
- **Breakpoints**: 
  - Mobile: 0-768px
  - Tablet: 768-1024px  
  - Desktop: 1024px+

### Spacing Scale
- **4px**: Tight spacing between related elements
- **8px**: Standard spacing between components
- **16px**: Section spacing and card padding
- **24px**: Large section breaks and container padding
- **32px**: Major section divisions
- **48px**: Page-level spacing
- **64px**: Hero section spacing

### Layout Patterns
**Header:**
- Fixed height: 64px
- Horizontal padding: 24px
- Logo on left, navigation center, actions on right
- Transparent background with backdrop blur on scroll

**Content Areas:**
- Maximum width: 1200px
- Centered with auto margins
- Consistent 24px horizontal padding
- Vertical rhythm based on 8px grid

**Sidebar Navigation:**
- Width: 240px on desktop
- Collapsible to 64px icon-only mode
- Full-width overlay on mobile

### Responsive Behavior
- Mobile-first approach with progressive enhancement
- Navigation collapses to hamburger menu below 768px
- Sidebar becomes full-screen overlay on mobile
- Typography scales down proportionally on smaller screens
- Touch targets minimum 44px on mobile devices

## 6. Depth & Elevation

Linear employs an extremely minimal approach to depth, relying primarily on subtle borders and background variations rather than traditional shadows.

### Elevation System
**Level 0 (Base):**
- Background: `#08090a`
- No shadow or border
- Used for primary page background

**Level 1 (Surface):**
- Background: `rgba(247, 248, 248, 0.02)`
- Border: `1px solid rgba(138, 143, 152, 0.1)`
- Used for cards, panels, and containers

**Level 2 (Elevated):**
- Background: `rgba(247, 248, 248, 0.05)`
- Border: `1px solid rgba(138, 143, 152, 0.15)`
- Used for modals, dropdowns, and overlays

**Level 3 (Floating):**
- Background: `rgba(247, 248, 248, 0.08)`
- Border: `1px solid rgba(138, 143, 152, 0.2)`
- Subtle shadow: `0 4px 12px rgba(0, 0, 0, 0.15)`
- Used for tooltips and floating elements

### Focus & Interaction States
**Focus Ring:**
- `0 0 0 2px rgba(94, 106, 210, 0.3)`
- Applied to all interactive elements
- Consistent 2px width with purple tint

**Hover States:**
- Subtle background color change: `rgba(138, 143, 152, 0.1)`
- No shadow or border changes
- Maintains minimal aesthetic

## 7. Do's and Don'ts

### Do's
✅ **Use the 8px grid system religiously** — All measurements should be multiples of 8px
✅ **Maintain the minimal color palette** — Stick to the defined grays, purple accent, and semantic colors
✅ **Prioritize Inter Variable** — Use the single font family with appropriate weights
✅ **Keep backgrounds dark** — Maintain the `#08090a` primary surface throughout
✅ **Use purple sparingly** — Reserve `#5e6ad2` for primary actions and focus states only
✅ **Embrace whitespace** — Let content breathe with generous spacing
✅ **Follow the type scale** — Use predefined font sizes and line heights
✅ **Maintain consistent border radius** — 4px for small elements, 6px for buttons, 8px for cards

### Don'ts
❌ **Don't add unnecessary visual flourishes** — Avoid gradients, drop shadows, or decorative elements
❌ **Don't use colors outside the defined palette** — No custom colors or brand colors from other systems
❌ **Don't mix font families** — Inter Variable handles all typographic needs
❌ **Don't create inconsistent spacing** — Avoid arbitrary margins or padding values
❌ **Don't overuse the purple accent** — It should feel special and purposeful
❌ **Don't add heavy shadows or effects** — Maintain the flat, minimal aesthetic
❌ **Don't ignore the grid system** — All layouts should follow the 8px base unit
❌ **Don't use pure white or pure black** — Stick to the warm white (`#f7f8f8`) and Linear black (`#08090a`)

## 8. Responsive Behavior

### Breakpoint Strategy
**Mobile First Approach:**
- Base styles target mobile (320px+)
- Progressive enhancement for larger screens
- Touch-optimized interactions on mobile

### Breakpoint Definitions
```css
/* Mobile: 0-767px (base styles) */
/* Tablet: 768px-1023px */
@media (min-width: 768px) { }
/* Desktop: 1024px+ */
@media (min-width: 1024px) { }
/* Large Desktop: 1440px+ */
@media (min-width: 1440px) { }
```

### Layout Adaptations
**Navigation:**
- Desktop: Horizontal navigation bar with full menu
- Tablet: Condensed navigation with some items in overflow menu
- Mobile: Hamburger menu with full-screen overlay

**Typography Scaling:**
- Desktop: Full type scale as defined
- Tablet: 90% scale factor applied to larger headings
- Mobile: 85% scale factor with increased line-height for readability

**Spacing Adjustments:**
- Desktop: Full 8px grid system
- Tablet: Reduced container padding to 16px
- Mobile: Minimum 16px padding, some large spacing reduced by 25%

**Touch Targets:**
- Minimum 44px height for all interactive elements on mobile
- Increased padding on buttons and form elements
- Larger tap areas for navigation items

### Component Responsive Behavior
**Cards:**
- Desktop: Fixed width in grid layout
- Tablet: Flexible width with maintained aspect ratios
- Mobile: Full-width stacked layout

**Forms:**
- Desktop: Multi-column layouts where appropriate
- Tablet: Reduced to 2-column maximum
- Mobile: Single column with full-width inputs

**Data Tables:**
- Desktop: Full table display
- Tablet: Horizontal scroll with sticky first column
- Mobile: Card-based layout or accordion pattern

## 9. Agent Prompt Guide

When creating interfaces in the Linear design system, use this prompt structure:

**System Context:**
"You are designing for Linear, an ultra-minimal project management tool for engineers. The aesthetic is 'surgical precision' — every element serves a function, nothing is decorative. Think professional IDE meets modern design system."

**Visual Foundation:**
"Use the near-black background (`#08090a`) as your canvas. All text should be warm white (`#f7f8f8`) or neutral gray (`#8a8f98`). The signature purple (`#5e6ad2`) is reserved for primary actions and focus states only — use it sparingly to maintain impact."

**Typography Instructions:**
"Use Inter Variable exclusively. Body text is 14-16px at weight 400, interactive elements are weight 510, headings are weight 600. Line heights should be generous (1.4-1.5x) for readability in the dark interface."

**Layout Guidelines:**
"Everything follows an 8px grid. Spacing should be: 8px between related elements, 16px for component spacing, 24px for section breaks. Border radius is 4px for small elements, 6px for buttons, 8px for cards. All borders are 1px solid with rgba opacity."

**Component Behavior:**
"Buttons have 8px vertical padding, 16px horizontal. Form inputs have subtle background tints (`rgba(247, 248, 248, 0.05)`) and focus with purple border. Cards use minimal elevation with subtle borders rather than shadows."

**Interaction States:**
"Hover states use `rgba(138, 143, 152, 0.1)` background overlay. Focus rings are `0 0 0 2px rgba(94, 106, 210, 0.3)`. Active states darken the purple to `#5459c7`. No element should have heavy shadows or gradients."

**Responsive Approach:**
"Mobile-first design. Navigation collapses to hamburger below 768px. Touch targets minimum 44px on mobile. Reduce large spacing by 25% on mobile while maintaining the 8px grid system."

**Quality Checklist:**
"Before finalizing: 1) Is every measurement a multiple of 8px? 2) Is purple used only for primary actions? 3) Does the layout feel spacious and uncluttered? 4) Are all interactive elements clearly identifiable? 5) Does it feel like a tool engineers would want to use daily?"