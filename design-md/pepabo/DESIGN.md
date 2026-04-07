# Design System of Pepabo Design (GMO Pepabo)

## 1. Visual Theme & Atmosphere

Pepabo Design embodies a clean, professional design system philosophy that balances corporate reliability with approachable warmth. The interface presents itself as a sophisticated documentation platform — methodical, well-structured, and quietly confident. Built around a pristine white canvas with carefully orchestrated shadows and subtle color accents, the design language communicates "systematic excellence" rather than flashy innovation.

The signature approach is the multi-layered typography system using Open Sans and Noto Sans JP — a deliberate choice that bridges Western and Japanese design sensibilities. The interface breathes through generous whitespace and a restrained color palette dominated by sophisticated grays (`#393c41`, `#585c63`) that create hierarchy without visual noise. The design philosophy clearly prioritizes content accessibility and systematic consistency over decorative elements.

What makes Pepabo's design distinctive is its shadow-driven depth system. Rather than relying on borders or color variations, the interface uses a sophisticated multi-layer shadow system (`rgba(0, 0, 0, 0.12) 0px 0px 4px 0px, rgba(0, 0, 0, 0.12) 0px 4px 6px -2px`) that creates subtle elevation while maintaining the clean, borderless aesthetic. This creates a sense of floating panels and cards that feel both modern and trustworthy.

The overall atmosphere is that of a premium design system documentation — every element feels intentionally placed, every spacing decision feels systematic, and every interaction feels predictable in the best possible way. This is design for designers who value consistency and clarity above all else.

**Key Characteristics:**
- Pure white primary surface (`#ffffff`) with sophisticated shadow-based elevation
- Bilingual typography system: Open Sans + Noto Sans JP for global accessibility
- Restrained neutral palette with warm undertones in secondary colors
- Shadow-driven depth system replacing traditional borders
- Systematic 4px-based spacing grid
- Corporate-friendly color palette with subtle brand accents
- Documentation-first layout prioritizing content hierarchy and readability

## 2. Color Palette & Roles

### Primary
- **Charcoal Primary** (`#393c41`): The primary text color — a sophisticated dark gray with subtle warm undertones, used for main headings and primary content. Softer than pure black while maintaining excellent readability.
- **Medium Gray** (`#585c63`): Secondary text color used for navigation links, subheadings, and less prominent content. Creates clear hierarchy while remaining highly legible.

### Secondary & Accent
- **Pure White** (`#ffffff`): Primary background color and surface color for cards, headers, and main content areas.
- **Transparent Base** (`rgba(0, 0, 0, 0)`): Used extensively for transparent backgrounds, allowing the shadow system to create depth without color interference.

### Surface & Background
- **White Surface** (`#ffffff`): The primary surface color used for headers, cards, and elevated elements. Creates clean, professional appearance.
- **Transparent Overlay** (`rgba(0, 0, 0, 0)`): Used for button backgrounds and overlay elements, maintaining the clean aesthetic.

### Neutrals & Text
- **Primary Text** (`#393c41`): Main content text color — warm-toned dark gray
- **Secondary Text** (`#585c63`): Navigation and secondary content
- **Interactive Text** (`#585c63`): Link colors and interactive elements
- **Inverted Text** (`#ffffff`): Text on dark backgrounds or accent elements

### System Colors
- **Shadow Primary** (`rgba(0, 0, 0, 0.12)`): Used in the sophisticated multi-layer shadow system
- **Focus/Interaction**: Subtle state changes using opacity and shadow variations

## 3. Typography Rules

### Font Families
- **Primary Stack**: `"Open Sans", "Noto Sans JP", apple-system, "system-ui", Roboto, "Lucida Grande", Helvetica, Arial, sans-serif`
- **Fallback Strategy**: Comprehensive fallback chain ensuring consistent rendering across all platforms and languages

### Typography Hierarchy
- **H1 Brand Title**: 21px, Font-weight 700, Line-height 24px (1.14)
- **Body Text**: 16px, Font-weight 400, Line-height normal
- **Navigation Links**: 16px, Font-weight 400, Line-height 24px (1.5)
- **Interactive Elements**: 16px, Font-weight 400, Line-height 24px

### Typography Characteristics
- **Letter Spacing**: Normal (0) across all elements — clean, unmodified spacing
- **Font Weights**: 400 (regular) and 700 (bold) — minimal weight variation for clarity
- **Line Height Strategy**: Tight for headings (1.14), comfortable for body text (1.5)
- **Language Support**: Explicit Noto Sans JP inclusion for Japanese text rendering

## 4. Component Stylings

### Buttons
- **Navigation Toggle Button**:
  - Color: `#585c63`
  - Background: `transparent`
  - Border-radius: `4px`
  - Padding: `0px` (custom internal spacing)
  - Font-size: `16px`, Line-height: `24px`

### Links
- **Primary Links** (`.brand-link`):
  - Color: `#393c41`
  - Font-weight: `700`
  - Font-size: `21px`
  - Background: `transparent`
  - Border-radius: `0px`

- **Navigation Links** (`._link`):
  - Color: `#585c63`
  - Font-weight: `400`
  - Font-size: `16px`
  - Border-radius: `4px`
  - Line-height: `24px`

- **External Links** (`._link-external`):
  - Color: `#ffffff` (inverted for dark backgrounds)
  - Background: `transparent`

### Headers
- **Global Header** (`.global-header`):
  - Background: `#ffffff`
  - Box-shadow: `rgba(0, 0, 0, 0.12) 0px 0px 4px 0px, rgba(0, 0, 0, 0.12) 0px 4px 6px -2px`
  - Creates floating header effect with sophisticated multi-layer shadow

### Navigation
- **Header Menu** (`.header-menu`):
  - Background: `transparent`
  - Clean, borderless design relying on spacing and typography for structure

## 5. Layout Principles

### Spacing System
- **Base Unit**: 4px grid system (inferred from border-radius and consistent spacing)
- **Border Radius**: 4px standard for interactive elements
- **Component Spacing**: 0px margins with internal padding systems
- **Consistent Padding**: 0px external, custom internal spacing for precise control

### Grid System
- **Responsive Breakpoint**: 800px (DESKTOP_BREAKPOINT from JavaScript)
- **Mobile-First**: Collapsible sidebar system for responsive behavior
- **Container Strategy**: Full-width containers with internal content constraints

### Content Hierarchy
- **Multi-Pane Layout**: Desktop sidebar + main content area
- **Collapsible Navigation**: Mobile-optimized sidebar system
- **Content-First**: Layout prioritizes readability and content accessibility

## 6. Depth & Elevation

### Shadow System
- **Primary Elevation**: `rgba(0, 0, 0, 0.12) 0px 0px 4px 0px, rgba(0, 0, 0, 0.12) 0px 4px 6px -2px`
  - Multi-layer shadow creating subtle floating effect
  - Used for headers and elevated surfaces
  - Replaces traditional borders for cleaner aesthetic

### Layering Strategy
- **Background Layer**: Pure white base
- **Content Layer**: Transparent backgrounds with shadow elevation
- **Interactive Layer**: Subtle state changes through opacity and shadow variations
- **No Border Philosophy**: Shadows and spacing create separation instead of lines

## 7. Do's and Don'ts

### Do's
- **Use the multi-layer shadow system** for creating depth and hierarchy
- **Maintain the 4px border-radius** for all interactive elements
- **Leverage the bilingual font stack** for international accessibility
- **Use transparent backgrounds** with shadow elevation for clean layering
- **Follow the restrained color palette** — grays and whites with minimal accents
- **Implement responsive sidebar patterns** for mobile optimization

### Don'ts
- **Don't use borders** — the design system relies on shadows and spacing
- **Don't introduce new font weights** — stick to 400 and 700
- **Don't use pure black** — the warm-toned grays are intentional
- **Don't ignore the Japanese typography** — Noto Sans JP is essential
- **Don't break the transparent background pattern** — maintain the layering system
- **Don't add decorative elements** — the system prioritizes functional clarity

## 8. Responsive Behavior

### Breakpoints
- **Desktop Threshold**: 800px and above
- **Mobile Threshold**: Below 800px

### Mobile Strategy
- **Collapsible Sidebar**: Full sidebar collapse with toggle button activation
- **Touch-Friendly Targets**: 24px line-height ensures adequate touch targets
- **Simplified Navigation**: Streamlined mobile navigation with overlay patterns

### Desktop Behavior
- **Multi-Pane Layout**: Persistent sidebar with main content area
- **Hover States**: Subtle interactive feedback on desktop
- **Keyboard Navigation**: Full keyboard accessibility support

## 9. Agent Prompt Guide

### Quick Reference for AI Agents

**Color Palette**: Primary text `#393c41`, secondary text `#585c63`, white backgrounds `#ffffff`, transparent overlays `rgba(0, 0, 0, 0)`

**Typography**: Open Sans + Noto Sans JP stack, 16px base, 21px headings, 400/700 weights only, 24px line-height for interactive elements

**Shadows**: Multi-layer system `rgba(0, 0, 0, 0.12) 0px 0px 4px 0px, rgba(0, 0, 0, 0.12) 0px 4px 6px -2px` for elevation

**Components**: 4px border-radius, transparent backgrounds, shadow-based depth, no borders

### Recommended Prompts

**For Layout**: "Create a clean, documentation-style layout using Pepabo's white background with multi-layer shadows for elevation, 800px responsive breakpoint"

**For Typography**: "Use Open Sans/Noto Sans JP stack, 16px base size, #393c41 for primary text, #585c63 for secondary, maintain 24px line-height for interactive elements"

**For Components**: "Design with transparent backgrounds, 4px border-radius, multi-layer shadow elevation system, no borders, professional gray color palette"

**For Mobile**: "Implement collapsible sidebar pattern with 800px breakpoint, touch-friendly 24px targets, simplified mobile navigation"