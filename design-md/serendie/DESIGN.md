# Design System Analysis: Serendie Design System

## 1. Visual Theme & Atmosphere

Serendie Design System embodies a sophisticated, enterprise-grade aesthetic that balances Japanese design sensibilities with modern digital accessibility. The system presents itself as a mature, professional design language built for complex business applications while maintaining visual warmth and approachability.

The signature characteristic is its deep navy foundation (`#073265` / `rgb(7, 49, 101)`) paired with a clean, systematic approach to typography and spacing. Unlike many corporate design systems that feel sterile, Serendie maintains personality through its thoughtful color theming system (konjo, asagi, tsutuji, kurikawa, sumire) that allows for contextual brand expression while preserving consistency.

The typography strategy is distinctly international, combining Roboto's technical clarity with Noto Sans JP for Japanese text, creating a bilingual-first design approach. The custom SerendieOfficeVF variable font adds a unique brand touch while maintaining the system's professional demeanor.

What sets Serendie apart is its systematic approach to interaction states and component behavior. Every element follows consistent patterns for hover, focus, and disabled states, with sophisticated color mixing functions that create natural state transitions rather than jarring color jumps.

**Key Characteristics:**
- Deep navy primary (`#073265`) creating trust and stability
- Bilingual typography system (Roboto + Noto Sans JP + SerendieOfficeVF)
- Theme-based color system with 5 distinct personality modes
- Systematic 8px-based spacing grid
- Enterprise-grade accessibility with consistent focus rings
- Sophisticated color mixing for interaction states
- Clean, geometric component styling with subtle rounded corners

## 2. Color Palette & Roles

### Primary Colors
- **Serendie Navy** (`#073265` / `rgb(7, 49, 101)`): Primary text color and brand foundation - a deep, trustworthy navy that anchors the entire system
- **Primary Blue** (`#0650A0` / `rgb(6, 80, 160)`): Primary action color for buttons and key interactive elements
- **Pure White** (`#FFFFFF`): Primary contrast color for text on dark surfaces and button labels

### Theme Colors (Dynamic System)
- **Konjo Theme** (Default): Purple-based (`--sd-reference-color-scale-purple-400`)
- **Asagi Theme**: Green-based (`--sd-reference-color-scale-green-500`)
- **Tsutuji Theme**: Blue-based (`--sd-reference-color-scale-blue-400`)
- **Kurikawa Theme**: Yellow-based (`--sd-reference-color-scale-yellow-400`)
- **Sumire Theme**: Blue variant (`--sd-reference-color-scale-blue-400`)

### Surface & Background
- **Primary Background**: `#EFF2FC` (theme-color meta value) - a subtle blue-tinted white
- **Component Surface**: Defined through CSS custom properties with theme variations
- **Outline Color**: System-defined component outline color for borders and dividers

### Interaction States
- **Hover**: `color-mix(in srgb, var(--primary), var(--black-1000) 20%)` - sophisticated color mixing
- **Focus Ring**: Primary color with thick border weight
- **Disabled**: System-defined disabled colors with reduced opacity
- **Selection**: Primary impression color with white text

## 3. Typography Rules

### Font Families
- **Primary**: `Roboto, "Noto Sans JP", sans-serif` - International text system
- **Brand**: `SerendieOfficeVF` - Custom variable font for brand moments
- **Weight**: Variable font weight of 50 for SerendieOfficeVF

### Typography Scale
- **Title Large Expanded**: 18px / 700 weight / 28.8px line-height / 0.48px letter-spacing
- **Body Text**: 16px / 400 weight / 24px line-height / 0.48px letter-spacing
- **Navigation**: 16px / 700 weight / 24px line-height / 0.48px letter-spacing
- **Button Text**: 16px / 400 weight / 25.6px line-height / 0.48px letter-spacing

### Typography Hierarchy
- **H1 Elements**: Use `textStyle_sd.system.typography.title.large_expanded` class
- **Body Text**: Default 16px with 1.5 line-height ratio
- **Interactive Elements**: Consistent 700 weight for navigation and key actions
- **Letter Spacing**: Consistent 0.48px across all text sizes for improved readability

## 4. Component Stylings

### Buttons
**Primary Button:**
- Background: `rgb(6, 80, 160)` (Primary Blue)
- Text: White (`rgb(255, 255, 255)`)
- Border Radius: `9999px` (fully rounded)
- Padding: `0px 12px 0px 16px` (asymmetric for icon accommodation)
- Height: `40px`
- Font Weight: 400

**Button States:**
- **Hover**: `color-mix(in srgb, var(--primary), var(--black-1000) 20%)`
- **Focus**: Thick ring (`sd.system.dimension.border.thick`) in primary color
- **Disabled**: System disabled colors with `cursor: not-allowed`

### Interactive Elements
**Focus System:**
- Ring Width: `sd.system.dimension.border.medium` (default) / `thick` (focus)
- Ring Color: Primary impression color
- Outline Style: Solid

**Navigation Links:**
- Color: Serendie Navy (`rgb(7, 49, 101)`)
- Transition: `color 0.3s` smooth transition
- Hover: Primary impression color

## 5. Layout Principles

### Spacing System
- **Extra Large**: `sd.system.dimension.spacing.extraLarge`
- **Three Extra Large**: `sd.system.dimension.spacing.threeExtraLarge`
- **Medium**: `sd.system.dimension.spacing.medium` (16px)
- **Small**: `sd.system.dimension.spacing.small` (12px)
- **Mobile Override**: 24px horizontal padding on mobile (`mdDown:px_24px`)

### Container System
- **Header**: Fixed positioning with 100% width and z-index 100
- **Max Width**: 100% container width with centered content
- **Grid System**: CSS Grid with `1fr auto` template columns for flexible layouts

### Border System
- **Medium Border**: `sd.system.dimension.border.medium`
- **Thick Border**: `sd.system.dimension.border.thick` (for focus states)
- **Radius**: `sd.system.dimension.radius.full` for buttons, subtle rounding elsewhere

## 6. Depth & Elevation

### Shadow System
- **Primary Approach**: Ring-based depth using outline properties rather than box-shadow
- **Focus Rings**: Solid outline style with system-defined widths
- **Component Elevation**: Achieved through border and background color relationships

### Visual Hierarchy
- **Mix Blend Modes**: `multiply` for background shapes (normal for kurikawa/sumire themes)
- **Z-Index System**: Header at z-index 100, systematic layering
- **Opacity**: Strategic use for disabled states and loading animations

## 7. Do's and Don'ts

### Do's
- ✅ Use the systematic spacing values (`sd.system.dimension.spacing.*`)
- ✅ Implement consistent focus rings on all interactive elements
- ✅ Leverage the theme system for brand personality while maintaining consistency
- ✅ Use color-mix functions for natural hover state transitions
- ✅ Maintain bilingual typography support (Roboto + Noto Sans JP)
- ✅ Follow the 8px spacing grid system
- ✅ Use semantic color tokens rather than hardcoded values

### Don'ts
- ❌ Don't use box-shadow for primary depth - use the ring system instead
- ❌ Don't hardcode color values - use CSS custom properties
- ❌ Don't ignore the theme system - ensure components work across all themes
- ❌ Don't break the consistent letter-spacing (0.48px) across text elements
- ❌ Don't use inconsistent border radius values - stick to system tokens
- ❌ Don't forget disabled and focus states for interactive elements

## 8. Responsive Behavior

### Breakpoints
- **Mobile Down**: `mdDown:` prefix for mobile-specific styles
- **Mobile Padding**: 24px horizontal padding override on mobile devices

### Responsive Strategy
- **Header**: Maintains fixed positioning across all screen sizes
- **Spacing**: Reduces from `threeExtraLarge` to 24px on mobile
- **Typography**: Maintains consistent sizing across breakpoints
- **Grid**: Flexible grid system adapts to container width

### Mobile Considerations
- Touch-friendly button heights (40px minimum)
- Adequate spacing for finger navigation
- Maintained readability with consistent typography scale

## 9. Agent Prompt Guide

### Quick Reference for AI Agents

**Color Tokens:**
```
Primary: rgb(7, 49, 101) / #073265
Action: rgb(6, 80, 160) / #0650A0  
Background: #EFF2FC
White: #FFFFFF
```

**Typography:**
```
Font: Roboto, "Noto Sans JP", sans-serif
Sizes: 16px body, 18px titles
Weights: 400 body, 700 headings/nav
Letter-spacing: 0.48px consistent
```

**Spacing:**
```
System: sd.system.dimension.spacing.*
Mobile: 24px horizontal padding
Grid: 8px-based system
```

### Recommended Prompts

**For Component Creation:**
"Create a [component] using Serendie Design System with navy primary color (#073265), Roboto font family, system spacing tokens, and ring-based focus states."

**For Layout Design:**
"Design a layout following Serendie's 8px spacing grid, using sd.system.dimension.spacing tokens, with bilingual typography support and theme-aware color system."

**For Interactive Elements:**
"Build an interactive element with Serendie's color-mix hover states, thick focus rings in primary color, and consistent 0.48px letter-spacing."