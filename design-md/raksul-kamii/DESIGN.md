# Design System Documentation: kamii | Raksul Design System

## 1. Visual Theme & Atmosphere

Kamii represents Raksul's approach to design system documentation — clean, systematic, and professionally understated. Built on zeroheight's platform, the interface prioritizes clarity and accessibility over visual flourish, creating an environment that feels more like a technical reference manual than a marketing showcase.

The design philosophy centers on functional minimalism with a crisp white canvas (`#ffffff`) as the primary surface, allowing content and components to take center stage. Unlike many contemporary design systems that lean into bold brand expressions, Kamii maintains a neutral, documentation-focused aesthetic that emphasizes usability and readability above visual drama.

The typography system is anchored by DM Sans — a geometric sans-serif that strikes a balance between technical precision and human warmth. At 13px base size with normal line-height, the text maintains excellent readability while feeling compact and efficient. Navigation elements scale up to 16px with 24px line-height and medium weight (500), creating clear hierarchy without overwhelming the interface.

What distinguishes Kamii from other design systems is its restraint. The color palette is deliberately minimal, relying primarily on standard web colors (`rgb(0, 0, 238)` for links, `rgb(33, 33, 33)` for interactive elements) rather than custom brand colors. This creates a sense of reliability and familiarity — the design system feels like a trusted tool rather than a branded experience.

**Key Characteristics:**
- Pure white background (`#ffffff`) creating maximum contrast and readability
- DM Sans typography system with systematic scaling (13px base, 16px navigation)
- Minimal color palette emphasizing standard web conventions
- Clean border system with subtle dividers for content organization
- Functional navigation with clear hierarchy and state management
- Documentation-first approach prioritizing content over decoration

## 2. Color Palette & Roles

### Primary
- **Pure White** (`#ffffff`): Primary background color creating maximum contrast and clean canvas for content
- **Deep Black** (`rgb(0, 0, 0)`): Primary text color for body content and main typography
- **Standard Link Blue** (`rgb(0, 0, 238)`): Traditional web link color used for navigation and interactive text elements

### Secondary & Accent
- **Raksul Pink** (`rgb(197, 29, 84)`): Brand accent color used sparingly for skip links and accessibility features
- **Charcoal Gray** (`rgb(33, 33, 33)`): Secondary text color for interactive elements and buttons
- **Transparent** (`rgba(0, 0, 0, 0)`): Used extensively for clean, borderless backgrounds

### Surface & Background
- **Pure White** (`#ffffff`): Primary page background and card surfaces
- **Border Gray** (implied): Subtle border color for dividers and content separation
- **Transparent Overlays** (`rgba(0, 0, 0, 0)`): Clean, invisible backgrounds for navigation and interactive elements

### Functional Colors
- **Focus States**: Likely using standard browser focus colors for accessibility
- **Hover States**: Subtle variations of primary colors for interactive feedback

## 3. Typography Rules

### Font Family
- **Primary**: `"DM Sans", "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif`
- **Fallback Stack**: Comprehensive system font fallbacks ensuring consistency across platforms

### Typography Scale
- **Body Text**: 13px, font-weight 400, line-height normal
- **Navigation Links**: 16px, font-weight 500, line-height 24px (1.5)
- **Skip Links**: 13px, font-weight 700 (accessibility feature)

### Typography Hierarchy
- **H1-H6**: Likely following systematic scaling (not visible in current data)
- **Body**: 13px regular for optimal reading density
- **UI Elements**: 16px medium for clear interactive hierarchy
- **Emphasis**: Font-weight 700 for important accessibility features

### Line Height System
- **Compact**: Normal line-height for body text (approximately 1.2-1.3)
- **Comfortable**: 24px (1.5) for navigation elements ensuring touch-friendly targets
- **Consistent**: Systematic approach to vertical rhythm

## 4. Component Stylings

### Navigation Components
- **Tab Links**: 16px DM Sans medium (500), 24px line-height, standard link blue
- **Search Button**: Charcoal gray (`rgb(33, 33, 33)`), transparent background, clean styling
- **Skip Links**: High contrast white on Raksul pink (`rgb(197, 29, 84)`), 3px border-radius, bold weight

### Interactive States
- **Default Links**: Standard web blue (`rgb(0, 0, 238)`) maintaining familiar web conventions
- **Hover**: Likely subtle color shifts (not captured in static analysis)
- **Focus**: Standard browser focus indicators for accessibility compliance
- **Active**: Systematic state management across interactive elements

### Layout Components
- **Sidebar**: Fixed positioning with border-right, white background, z-index 4
- **Main Content**: Full-width, full-height flex layout with grow behavior
- **Navigation**: Absolute positioning with systematic spacing

## 5. Layout Principles

### Spacing System
- **Zero Margins**: `margin: 0px` reset across all elements for precise control
- **Zero Padding**: `padding: 0px` base with specific overrides (skip links use `0px 16px`)
- **Systematic Spacing**: 16px horizontal padding for interactive elements

### Grid System
- **Flexbox-Based**: Modern flex layout with full-height containers
- **Responsive Columns**: Sidebar with `wg60` class suggesting 60% width system
- **Full-Width Containers**: Main content areas using `full-width` utility classes

### Container Strategy
- **Full Viewport**: `full-height` classes ensuring complete screen utilization
- **Flexible Growth**: `flex-grow` for adaptive content areas
- **Absolute Positioning**: Strategic use for navigation and overlay elements

## 6. Depth & Elevation

### Shadow System
- **Minimal Shadows**: `box-shadow: none` across most elements maintaining flat design
- **Z-Index Layers**: Systematic layering with `z4` for navigation elements
- **Border-Based Depth**: Subtle borders rather than shadows for component separation

### Layering Strategy
- **Base Layer**: Main content at default z-index
- **Navigation Layer**: `z-index: 4` for sidebar and navigation elements
- **Overlay System**: Absolute positioning for modal and overlay components

## 7. Do's and Don'ts

### Do's
- ✅ Use DM Sans for all typography to maintain consistency
- ✅ Maintain 16px minimum for interactive elements (touch targets)
- ✅ Preserve white background for maximum readability
- ✅ Use standard web colors for familiar user experience
- ✅ Implement proper focus states for accessibility
- ✅ Follow systematic spacing with 16px increments

### Don'ts
- ❌ Don't add unnecessary visual decoration that distracts from content
- ❌ Don't use custom colors without strong justification
- ❌ Don't break the minimal shadow system with heavy drop shadows
- ❌ Don't ignore the systematic font-weight scale (400, 500, 700)
- ❌ Don't compromise the clean, documentation-focused aesthetic

## 8. Responsive Behavior

### Breakpoint Strategy
- **Mobile-First**: Likely responsive design with mobile considerations
- **Sidebar Behavior**: `display-none` class suggests collapsible navigation
- **Flexible Layouts**: Full-width, full-height containers adapting to viewport

### Adaptive Components
- **Navigation**: Collapsible sidebar with responsive behavior
- **Typography**: Consistent sizing across devices with DM Sans web font
- **Touch Targets**: 24px line-height ensuring adequate touch areas

## 9. Agent Prompt Guide

### Quick Reference for AI Agents

**Primary Colors:**
- Background: `#ffffff`
- Text: `rgb(0, 0, 0)`
- Links: `rgb(0, 0, 238)`
- Brand: `rgb(197, 29, 84)`

**Typography:**
- Font: `"DM Sans", system-ui, sans-serif`
- Body: `13px/normal 400`
- Navigation: `16px/24px 500`
- Bold: `weight 700`

**Layout:**
- Spacing: 16px increments
- Borders: Subtle, minimal
- Shadows: None (flat design)
- Z-index: 4 for navigation

### Recommended Prompts

**For Component Creation:**
```
Create a [component] using DM Sans typography, white background, minimal borders, and standard web link colors. Follow the clean, documentation-focused aesthetic of Raksul's Kamii design system.
```

**For Layout Design:**
```
Design a [layout] with full-width containers, flexbox structure, 16px spacing increments, and the systematic approach of Kamii design system. Maintain the clean, functional aesthetic.
```

**For Color Application:**
```
Apply colors from Kamii palette: white backgrounds, black text, standard blue links, and minimal use of Raksul pink accent. Prioritize readability and accessibility.
```