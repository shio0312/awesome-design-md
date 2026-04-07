# Design System Inspiration of Vercel

## 1. Visual Theme & Atmosphere

Vercel's design embodies the philosophy of "black and white precision" — a stark, minimalist aesthetic that prioritizes clarity and performance above all else. The interface feels like a perfectly calibrated instrument, where every pixel serves a purpose and nothing is ornamental. Built on a foundation of near-white (`#fafafa`) and deep charcoal (`#171717`), the design creates an environment that feels both futuristic and timeless.

The signature element is the Geist font family — a custom sans-serif designed specifically for Vercel that balances technical precision with human readability. Geist appears in three variants (Sans, Mono, and Display) across the interface, creating typographic consistency that reinforces the brand's commitment to developer tools that "just work." Headlines breathe with generous line-heights (1.2-1.4), while body text maintains optimal readability at 16px base size.

What sets Vercel apart is its surgical use of color. In a world of vibrant gradients and rainbow palettes, Vercel's restraint is radical. The primary brand blue (`#0072f5`) appears sparingly — only for critical actions and focus states — making every instance feel intentional and important. Grays are perfectly neutral without warm or cool undertones (`#4d4d4d`, `#666666`, `#999999`), creating a backdrop that never competes with content.

**Key Characteristics:**
- Monochromatic foundation: near-white (`#fafafa`) to deep charcoal (`#171717`)
- Custom Geist font family optimizing for developer-focused readability
- Surgical color usage — blue (`#0072f5`) reserved for critical interactions
- Perfect neutral grays without temperature bias
- Minimal border radius (6px standard) for clean, technical aesthetic
- Subtle shadow system emphasizing elevation over decoration
- Grid-based layouts with consistent 24px padding and 12px/16px spacing units

## 2. Color Palette & Roles

### Primary
- **Vercel Black** (`#171717`): Primary text color and dark surfaces — a true neutral black that anchors the entire system without feeling harsh.
- **Vercel Blue** (`#0072f5`): The sole brand color, used exclusively for primary CTAs, links, and focus states. Every instance carries weight and intention.
- **Pure White** (`#ffffff`): Clean surface color for cards, modals, and content areas requiring maximum contrast.

### Secondary & Neutral
- **Background Gray** (`#fafafa`): The primary page background — a barely-there gray that's warmer than pure white but maintains neutrality.
- **Medium Gray** (`#666666`): Secondary text color for descriptions, labels, and less critical information.
- **Light Gray** (`#999999`): Tertiary text for timestamps, metadata, and placeholder content.
- **Border Gray** (`#e5e5e5`): Subtle borders and dividers that separate content without visual weight.

### Functional
- **Success Green** (`#00a86b`): Confirmation states, success messages, and positive indicators.
- **Warning Orange** (`#f5a623`): Caution states and important notices requiring attention.
- **Error Red** (`#e00`): Error states, destructive actions, and critical alerts.
- **Focus Blue** (`#0072f5`): Identical to brand blue — focus rings and interactive state indicators.

### Surface & Elevation
- **Card White** (`#ffffff`): Elevated content areas, form inputs, and interactive surfaces.
- **Hover Gray** (`#f5f5f5`): Subtle hover states for interactive elements.
- **Active Gray** (`#e5e5e5`): Pressed states and active selections.

## 3. Typography Rules

### Font Family
- **Primary**: Geist Sans — custom typeface optimized for UI and body text
- **Monospace**: Geist Mono — for code, technical data, and developer-focused content
- **Fallback**: Arial, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"

### Scale & Hierarchy
- **Display Large**: 48px / 1.2 line-height / 600 weight — Hero headlines and major page titles
- **Display Medium**: 36px / 1.3 line-height / 600 weight — Section headers and feature titles
- **Heading 1**: 32px / 1.25 line-height / 600 weight — Primary content headings
- **Heading 2**: 24px / 1.33 line-height / 600 weight — Secondary headings
- **Heading 3**: 20px / 1.4 line-height / 500 weight — Tertiary headings
- **Body Large**: 18px / 1.44 line-height / 400 weight — Emphasized body text
- **Body**: 16px / 1.5 line-height / 400 weight — Standard body text and UI elements
- **Body Small**: 14px / 1.43 line-height / 400 weight — Secondary information, captions
- **Caption**: 12px / 1.33 line-height / 400 weight — Metadata, timestamps, fine print

### Letter Spacing
- **Display sizes**: -0.02em — Tighter spacing for large text
- **Body sizes**: 0em — Default spacing for optimal readability
- **Small sizes**: 0.01em — Slightly expanded for legibility

### Color Applications
- **Primary text**: `#171717` on light backgrounds
- **Secondary text**: `#666666` for supporting information
- **Tertiary text**: `#999999` for metadata and timestamps
- **Interactive text**: `#0072f5` for links and actionable elements

## 4. Component Stylings

### Buttons
**Primary Button**:
- Background: `#171717`
- Text: `#ffffff`
- Padding: `12px 24px`
- Border-radius: `6px`
- Font: 14px / 500 weight
- Hover: `#333333` background
- Focus: `0 0 0 2px #0072f5` ring

**Secondary Button**:
- Background: `transparent`
- Text: `#171717`
- Border: `1px solid #e5e5e5`
- Padding: `12px 24px`
- Border-radius: `6px`
- Hover: `#f5f5f5` background

**Ghost Button**:
- Background: `transparent`
- Text: `#666666`
- Padding: `8px 12px`
- Border-radius: `6px`
- Hover: `#f5f5f5` background

### Form Elements
**Input Fields**:
- Background: `#ffffff`
- Border: `1px solid #e5e5e5`
- Border-radius: `6px`
- Padding: `12px 16px`
- Font: 16px Geist
- Focus: `#0072f5` border, `0 0 0 2px rgba(0, 114, 245, 0.1)` ring

**Labels**:
- Font: 14px / 500 weight
- Color: `#171717`
- Margin-bottom: `8px`

### Cards
**Standard Card**:
- Background: `#ffffff`
- Border: `1px solid #e5e5e5`
- Border-radius: `8px`
- Padding: `24px`
- Shadow: `0 1px 3px rgba(0, 0, 0, 0.1)`

**Hover Card**:
- Shadow: `0 4px 12px rgba(0, 0, 0, 0.15)`
- Transform: `translateY(-2px)`
- Transition: `all 0.2s ease`

### Navigation
**Header Height**: `64px`
**Logo**: Vercel wordmark in `#171717`
**Nav Links**: 14px / 400 weight / `#4d4d4d` color
**Active State**: `#171717` color
**Mobile Menu**: Full-screen overlay with `#ffffff` background

## 5. Layout Principles

### Grid System
- **Container Max-width**: `1200px`
- **Breakpoints**: 
  - Mobile: `320px - 767px`
  - Tablet: `768px - 1023px`
  - Desktop: `1024px+`
- **Columns**: 12-column grid with 24px gutters
- **Margins**: 24px on mobile, 48px on desktop

### Spacing Scale
- **Base unit**: `4px`
- **Scale**: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- **Section spacing**: 96px between major sections
- **Component spacing**: 24px between related elements
- **Element spacing**: 12px between form elements, 8px for tight groupings

### Content Width
- **Reading width**: Maximum 65 characters (approximately 680px)
- **Form width**: Maximum 480px for optimal completion
- **Card width**: Flexible with 320px minimum, 400px optimal

### Alignment
- **Text alignment**: Left-aligned for all body text and UI elements
- **Center alignment**: Only for hero sections and call-to-action areas
- **Content centering**: Horizontal centering with consistent side margins

## 6. Depth & Elevation

### Shadow System
**Level 1 - Subtle**:
- `box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1)`
- Usage: Cards, form inputs, subtle elevation

**Level 2 - Moderate**:
- `box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15)`
- Usage: Hover states, dropdowns, tooltips

**Level 3 - Prominent**:
- `box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2)`
- Usage: Modals, overlays, important floating elements

**Level 4 - Maximum**:
- `box-shadow: 0 16px 48px rgba(0, 0, 0, 0.3)`
- Usage: Full-screen overlays, critical modals

### Border Strategy
- **Standard borders**: `1px solid #e5e5e5`
- **Focus borders**: `1px solid #0072f5`
- **Divider borders**: `1px solid #f0f0f0`
- **No borders**: Rely on background color contrast and subtle shadows

### Z-Index Scale
- **Base content**: `z-index: 1`
- **Sticky elements**: `z-index: 10`
- **Dropdowns**: `z-index: 100`
- **Overlays**: `z-index: 1000`
- **Modals**: `z-index: 10000`

## 7. Do's and Don'ts

### ✅ Do's
- **Use Geist font family** consistently across all text elements
- **Maintain the monochromatic palette** — let content and functionality drive the experience
- **Apply 6px border-radius** to interactive elements for consistency
- **Use 24px base spacing** for layout consistency and visual rhythm
- **Reserve blue (`#0072f5`)** for critical actions and interactive states only
- **Implement subtle shadows** for elevation rather than heavy borders
- **Keep line-heights generous** (1.4-1.5) for optimal readability
- **Use neutral grays** without warm or cool temperature bias
- **Maintain consistent 16px base font size** for accessibility
- **Apply focus rings** to all interactive elements for keyboard navigation

### ❌ Don'ts
- **Don't introduce additional colors** beyond the defined palette
- **Don't use decorative elements** or ornamental graphics
- **Don't apply heavy drop shadows** or excessive visual effects
- **Don't use colored text** except for links and interactive elements
- **Don't create inconsistent spacing** — stick to the 4px-based scale
- **Don't use script or decorative fonts** — maintain Geist consistency
- **Don't center-align body text** or form elements
- **Don't use gradients or textures** — maintain flat, clean surfaces
- **Don't create busy layouts** — embrace white space and simplicity
- **Don't ignore hover states** — provide clear interactive feedback

### Typography Don'ts
- **Don't use font weights below 400** or above 600
- **Don't use all-caps** except for small labels or buttons
- **Don't use colored text** for emphasis — use weight and size instead
- **Don't create tight line-heights** below 1.2 for any text size

### Color Don'ts
- **Don't use pure black** (`#000000`) — use Vercel Black (`#171717`)
- **Don't tint grays** with warm or cool undertones
- **Don't use blue** for decorative purposes — only for interactions
- **Don't create low-contrast combinations** — maintain WCAG AA standards

## 8. Responsive Behavior

### Breakpoint Strategy
**Mobile First Approach**:
- Base styles target mobile (`320px+`)
- Progressive enhancement for larger screens
- Fluid typography and spacing between breakpoints

**Key Breakpoints**:
- **Small**: `sm: 640px` — Large mobile, small tablet
- **Medium**: `md: 768px` — Tablet portrait
- **Large**: `lg: 1024px` — Tablet landscape, small desktop
- **Extra Large**: `xl: 1280px` — Desktop
- **2X Large**: `2xl: 1536px` — Large desktop

### Typography Scaling
**Mobile (320px-767px)**:
- Display Large: 32px
- Display Medium: 28px
- Heading 1: 24px
- Body: 16px (maintained)
- Padding: 16px container margins

**Tablet (768px-1023px)**:
- Display Large: 40px
- Display Medium: 32px
- Heading 1: 28px
- Body: 16px (maintained)
- Padding: 32px container margins

**Desktop (1024px+)**:
- Full scale as defined in Typography Rules
- Padding: 48px container margins

### Component Adaptations
**Navigation**:
- Mobile: Hamburger menu with full-screen overlay
- Tablet: Condensed horizontal navigation
- Desktop: Full horizontal navigation with dropdowns

**Cards**:
- Mobile: Single column, full-width cards
- Tablet: 2-column grid with 16px gaps
- Desktop: 3-column grid with 24px gaps

**Forms**:
- Mobile: Full-width inputs, stacked labels
- Tablet: Maintain full-width, increase padding
- Desktop: Optimal 480px width, side-by-side for short inputs

**Buttons**:
- Mobile: Full-width primary buttons, 44px minimum touch target
- Tablet: Inline buttons with adequate spacing
- Desktop: Standard sizing as defined

### Layout Adaptations
- **Mobile**: Single column, 16px side margins, 48px section spacing
- **Tablet**: Flexible columns, 32px side margins, 64px section spacing
- **Desktop**: Multi-column layouts, 48px side margins, 96px section spacing

## 9. Agent Prompt Guide

When creating interfaces in the Vercel design system, use this prompt framework:

**"Create a [component/page] following Vercel's design system with these specifications:**

**Visual Foundation:**
- Use near-white background (`#fafafa`) with pure white cards (`#ffffff`)
- Apply Geist font family throughout (fallback: Arial, system fonts)
- Maintain monochromatic palette with surgical blue (`#0072f5`) for interactions only
- Use Vercel Black (`#171717`) for primary text, medium gray (`#666666`) for secondary

**Typography:**
- 16px base font size with 1.5 line-height for body text
- [Specify heading level]: [size]px / [line-height] / 600 weight
- Maintain generous spacing between text elements (12px-24px)

**Layout:**
- Apply 24px base spacing unit and 6px border-radius consistently
- Use 24px padding for containers, 12px for compact elements
- Implement subtle shadows: `0 1px 3px rgba(0, 0, 0, 0.1)` for basic elevation

**Components:**
- Primary buttons: `#171717` background, white text, 12px vertical padding
- Form inputs: white background, `#e5e5e5` border, `#0072f5` focus ring
- Cards: white background, subtle border, 24px internal padding

**Interactions:**
- Blue (`#0072f5`) only for links, focus states, and primary actions
- Hover states use `#f5f5f5` background for subtle feedback
- Maintain 44px minimum touch targets on mobile

**Responsive:**
- Mobile-first approach with 16px side margins on small screens
- Scale to 48px margins on desktop with max-width 1200px containers
- Stack elements vertically on mobile, allow horizontal layouts on desktop"

**Example Implementation Prompt:**
"Create a pricing card component using Vercel's design system: white background card with subtle shadow, 24px padding, Geist font, primary heading in Vercel Black at 24px/600 weight, secondary text in medium gray at 16px/400 weight, primary button with black background and white text, 6px border radius throughout, and blue focus rings on interactive elements."