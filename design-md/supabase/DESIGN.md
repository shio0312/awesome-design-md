# Design System Inspiration of Supabase

## 1. Visual Theme & Atmosphere

Supabase's design is a developer's command center reimagined as a sleek, modern workspace — dark, focused, and unapologetically technical. The entire experience is built on a deep charcoal canvas (`#121212`) that creates an immersive coding environment, deliberately evoking the feeling of a premium IDE rather than a typical web interface. Where most developer tools feel sterile or overwhelming, Supabase's design radiates professional confidence with subtle emerald accents that hint at growth and vitality.

The signature move is the custom Circular typeface — a clean, geometric sans-serif with excellent readability that gives every interface element the precision of well-crafted code. Combined with strategic use of emerald green (`#3ECF8E`) for brand moments and a sophisticated neutral palette, the visual language says "powerful yet approachable" rather than "complex and intimidating." The typography breathes at comfortable line-heights (1.5 for body text, 1.2 for headings), creating a rhythm that feels more like reading documentation than navigating a dense interface.

What makes Supabase's design truly distinctive is its dark-first approach with warm undertones. Every surface has been carefully considered to reduce eye strain during long coding sessions. The primary background (`#121212`) is a rich near-black, while elevated surfaces use subtle variations (`#1a1a1a`, `#2a2a2a`) to create depth without harsh contrasts. The emerald brand color (`#3ECF8E`) appears sparingly but memorably, creating moments of energy against the sophisticated dark palette.

**Key Characteristics:**
- Deep charcoal canvas (`#121212`) optimized for extended development sessions
- Circular typeface family: clean, geometric sans-serif for maximum code readability
- Emerald brand accent (`#3ECF8E`) — vibrant, growth-oriented, developer-friendly
- Sophisticated dark theme with warm undertones throughout
- Code-first iconography and technical illustrations
- Subtle elevation system using surface color variations rather than heavy shadows
- Developer-centric pacing with dense information architecture and clear hierarchy

## 2. Color Palette & Roles

### Primary
- **Supabase Dark** (`#121212`): The primary background color — a rich, warm near-black that serves as the foundation for the entire dark theme experience.
- **Emerald Brand** (`#3ECF8E`): The core brand color — a vibrant emerald green used for primary CTAs, brand moments, and key interactive elements. Represents growth and developer success.
- **Foreground Light** (`#fafafa`): Primary text color on dark surfaces — a warm white that provides excellent contrast while being gentle on the eyes.

### Secondary & Accent
- **Brand Link** (`#10b981`): A deeper emerald variant for links and secondary brand moments — maintains brand consistency while providing hierarchy.
- **Surface 100** (`#1a1a1a`): Elevated surface color for cards and containers — subtle lift from the base background.
- **Surface 200** (`#2a2a2a`): Higher elevation surfaces for modals, dropdowns, and interactive elements.
- **Surface 300** (`#3a3a3a`): Hover states and active surfaces — provides clear interaction feedback.

### Functional Colors
- **Border Default** (`#2a2a2a`): Standard border color that provides subtle definition without harsh lines.
- **Border Strong** (`#404040`): Emphasized borders for focus states and important boundaries.
- **Foreground Lighter** (`#a3a3a3`): Secondary text color for descriptions and less important content.
- **Warning** (`#f59e0b`): Amber warning color for caution states and important notices.
- **Error** (`#ef4444`): Red error color for destructive actions and error states.
- **Success** (`#22c55e`): Green success color for positive feedback and completed actions.

### Surface & Background
- **Background Alternative** (`#0f0f0f`): Deeper background for high-contrast sections and code blocks.
- **Background Overlay** (`rgba(0, 0, 0, 0.8)`): Semi-transparent overlay for modals and dropdowns.

## 3. Typography Rules

### Font Family
- **Primary**: Circular, custom-font, "Helvetica Neue", Helvetica, Arial, sans-serif
- **Monospace**: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace

### Type Scale & Hierarchy
- **Display Large**: 48px / 52px (1.08) — Hero headlines and major section titles
- **Display Medium**: 36px / 40px (1.11) — Page titles and primary headings
- **Heading 1**: 30px / 36px (1.2) — Section headings
- **Heading 2**: 24px / 30px (1.25) — Subsection headings
- **Heading 3**: 20px / 26px (1.3) — Component titles
- **Body Large**: 18px / 28px (1.56) — Important body text and descriptions
- **Body Regular**: 16px / 24px (1.5) — Standard body text
- **Body Small**: 14px / 20px (1.43) — Secondary text and captions
- **Code**: 14px / 20px (1.43) — Code snippets and technical content
- **Caption**: 12px / 16px (1.33) — Labels and fine print

### Font Weights
- **Regular**: 400 — Standard body text
- **Medium**: 500 — Button text and emphasized content
- **Semibold**: 600 — Headings and important labels
- **Bold**: 700 — Strong emphasis and brand moments

### Letter Spacing
- **Tight**: -0.025em — Large headings and display text
- **Normal**: 0em — Body text and standard content
- **Wide**: 0.05em — Small caps and button text

## 4. Component Stylings

### Buttons
**Primary Button:**
- Background: `#3ECF8E` (emerald brand)
- Text: `#121212` (dark)
- Padding: `12px 24px`
- Border-radius: `6px`
- Font: 14px/16px, weight 500
- Hover: Background `#2dd4bf`
- Focus: 2px ring `#3ECF8E` with 2px offset

**Secondary Button:**
- Background: `transparent`
- Border: `1px solid #2a2a2a`
- Text: `#fafafa`
- Padding: `12px 24px`
- Hover: Background `#2a2a2a`

**Ghost Button:**
- Background: `transparent`
- Text: `#fafafa`
- Padding: `8px 16px`
- Hover: Background `#1a1a1a`

### Form Elements
**Input Fields:**
- Background: `#1a1a1a`
- Border: `1px solid #2a2a2a`
- Text: `#fafafa`
- Padding: `12px 16px`
- Border-radius: `6px`
- Focus: Border `#3ECF8E`, ring `2px #3ECF8E`

**Select Dropdowns:**
- Background: `#2a2a2a`
- Border: `1px solid #404040`
- Max-height: `200px`
- Item padding: `8px 12px`
- Hover: Background `#3a3a3a`

### Cards & Containers
**Standard Card:**
- Background: `#1a1a1a`
- Border: `1px solid #2a2a2a`
- Border-radius: `8px`
- Padding: `24px`
- Box-shadow: `0 1px 3px rgba(0, 0, 0, 0.2)`

**Elevated Card:**
- Background: `#2a2a2a`
- Border: `1px solid #404040`
- Box-shadow: `0 4px 12px rgba(0, 0, 0, 0.3)`

### Navigation
**Header Navigation:**
- Height: `64px`
- Background: `rgba(18, 18, 18, 0.8)` with backdrop-blur
- Border-bottom: `1px solid #2a2a2a`
- Link padding: `8px 16px`
- Link hover: Color `#3ECF8E`

## 5. Layout Principles

### Grid System
- **Container max-width**: 1200px
- **Grid columns**: 12-column system
- **Gutter width**: 24px
- **Breakpoints**:
  - Mobile: 0-640px
  - Tablet: 641-1024px
  - Desktop: 1025px+

### Spacing Scale
- **4px**: Micro spacing for tight elements
- **8px**: Small spacing for related items
- **16px**: Medium spacing for component padding
- **24px**: Large spacing for section gaps
- **32px**: XL spacing for major sections
- **48px**: XXL spacing for page sections
- **64px**: Hero spacing for major breaks
- **96px**: Maximum spacing for page divisions

### Content Width
- **Reading width**: 65ch maximum for optimal readability
- **Form width**: 400px maximum for form containers
- **Card width**: 320px standard card width
- **Sidebar width**: 280px for navigation sidebars

### Alignment
- **Text alignment**: Left-aligned for all body text
- **Center alignment**: Only for hero sections and call-to-action blocks
- **Button alignment**: Left-aligned in forms, center in hero sections

## 6. Depth & Elevation

### Shadow System
**Level 1 (Cards):**
- Box-shadow: `0 1px 3px rgba(0, 0, 0, 0.2)`
- Use: Standard cards, form elements

**Level 2 (Elevated):**
- Box-shadow: `0 4px 12px rgba(0, 0, 0, 0.3)`
- Use: Hover states, active elements

**Level 3 (Floating):**
- Box-shadow: `0 8px 24px rgba(0, 0, 0, 0.4)`
- Use: Modals, dropdowns, tooltips

**Level 4 (Modal):**
- Box-shadow: `0 16px 48px rgba(0, 0, 0, 0.5)`
- Use: Modal dialogs, overlays

### Surface Hierarchy
- **Base**: `#121212` — Page background
- **Raised**: `#1a1a1a` — Cards and containers
- **Elevated**: `#2a2a2a` — Interactive elements
- **Overlay**: `#3a3a3a` — Hover and active states

### Z-Index Scale
- **Base**: 0 — Standard content
- **Dropdown**: 10 — Dropdown menus
- **Sticky**: 20 — Sticky navigation
- **Modal**: 30 — Modal dialogs
- **Tooltip**: 40 — Tooltips and popovers

## 7. Do's and Don'ts

### Color Usage
**Do:**
- Use emerald (`#3ECF8E`) sparingly for maximum impact
- Maintain high contrast ratios (4.5:1 minimum) for accessibility
- Use warm undertones in grays to maintain brand consistency
- Test colors in both light and dark environments

**Don't:**
- Use pure black (`#000000`) — always use the warmer `#121212`
- Overuse the brand color — reserve for primary actions and key moments
- Mix cool and warm grays within the same interface
- Use low-contrast color combinations

### Typography
**Do:**
- Use consistent line-heights across similar content types
- Maintain clear hierarchy with size and weight variations
- Use monospace fonts for all code and technical content
- Keep line lengths between 45-75 characters for optimal readability

**Don't:**
- Use more than 3 font weights in a single interface
- Set body text smaller than 14px
- Use all-caps for more than 3 words
- Mix different font families within the same content block

### Layout & Spacing
**Do:**
- Use the 8px spacing scale consistently
- Align elements to a clear grid system
- Provide adequate touch targets (44px minimum)
- Group related elements with consistent spacing

**Don't:**
- Use arbitrary spacing values outside the scale
- Center-align large blocks of body text
- Create layouts narrower than 320px
- Stack more than 3 levels of nested containers

### Interactive Elements
**Do:**
- Provide clear hover and focus states for all interactive elements
- Use consistent button sizing and padding
- Include loading states for async actions
- Make clickable areas large enough for easy interaction

**Don't:**
- Use hover effects on touch devices
- Create buttons smaller than 32px in height
- Remove focus indicators for keyboard navigation
- Use disabled states without clear explanation

## 8. Responsive Behavior

### Breakpoint Strategy
**Mobile First Approach:**
- Base styles target mobile (320px+)
- Progressive enhancement for larger screens
- Touch-optimized interactions on mobile

**Breakpoint Definitions:**
- **sm**: 640px — Large mobile/small tablet
- **md**: 768px — Tablet portrait
- **lg**: 1024px — Tablet landscape/small desktop
- **xl**: 1280px — Desktop
- **2xl**: 1536px — Large desktop

### Component Adaptations
**Navigation:**
- Mobile: Hamburger menu with full-screen overlay
- Tablet: Collapsed navigation with visible logo
- Desktop: Full horizontal navigation

**Typography:**
- Mobile: Reduce heading sizes by 20-30%
- Tablet: Standard sizing with adjusted line-heights
- Desktop: Full scale with optimal line-lengths

**Cards & Layout:**
- Mobile: Single column, full-width cards
- Tablet: 2-column grid with 16px gutters
- Desktop: 3-4 column grid with 24px gutters

**Buttons:**
- Mobile: Full-width primary buttons, 48px height
- Tablet: Auto-width buttons, 44px height
- Desktop: Compact buttons, 40px height

### Touch Considerations
- Minimum touch target: 44px × 44px
- Adequate spacing between interactive elements (8px minimum)
- Swipe gestures for carousel and navigation components
- Long-press interactions for contextual menus

## 9. Agent Prompt Guide

When creating interfaces in the Supabase design system, use this prompt structure:

**Base Prompt:**
"Create a [component/page] using Supabase's dark emerald design system. Use the deep charcoal background (#121212), Circular font family, and emerald brand color (#3ECF8E) sparingly for primary actions. Maintain the developer-focused, professional aesthetic with warm undertones throughout."

**Color Specifications:**
"Use these exact colors: Background #121212, elevated surfaces #1a1a1a and #2a2a2a, text #fafafa, emerald brand #3ECF8E for CTAs only, borders #2a2a2a, and secondary text #a3a3a3."

**Typography Instructions:**
"Use Circular font family with these sizes: headings 24-48px with 1.1-1.2 line-height, body text 16px with 1.5 line-height, small text 14px. Font weights: 400 regular, 500 medium for buttons, 600 semibold for headings."

**Layout Guidelines:**
"Follow 8px spacing scale, use 24px gutters, max content width 1200px. Cards use #1a1a1a background with 1px #2a2a2a borders and 8px border-radius. Buttons are 6px border-radius with 12px vertical padding."

**Component Behavior:**
"Buttons: Primary uses #3ECF8E background with #121212 text, secondary uses transparent background with #2a2a2a border. Hover states use surface-300 (#3a3a3a). Focus rings are 2px #3ECF8E with 2px offset."

**Responsive Notes:**
"Mobile-first approach: full-width elements on mobile, reduce heading sizes by 25%, use 48px button heights on touch devices, maintain 44px minimum touch targets."

**Brand Voice:**
"Maintain developer-focused, professional tone. The design should feel like a premium development tool - sophisticated, powerful, but approachable. Think 'GitHub meets modern SaaS' rather than 'consumer app'."