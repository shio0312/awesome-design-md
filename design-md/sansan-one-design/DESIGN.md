# Design System Documentation: One UI - Sansan Design System

## 1. Visual Theme & Atmosphere

One UI presents itself as a refined, professional design system that embodies Japanese minimalism with enterprise-grade sophistication. Built on Storybook's foundation, the interface radiates clean efficiency while maintaining warmth through its carefully curated neutral palette and thoughtful typography choices.

The design philosophy centers around clarity and accessibility, using a light-first approach with a primary background of soft gray-blue (`#f7f7fc`) that feels more welcoming than stark white. The interface employs subtle layering through gentle shadows and borders, creating depth without visual noise. Every element feels purposeful and uncluttered, reflecting Sansan's business-focused approach to design.

The signature element is the consistent use of **Nunito Sans** throughout the interface — a humanist sans-serif that brings approachability to what could otherwise feel corporate. The typography hierarchy is restrained but effective, with careful attention to readability and scanning patterns. Color usage is disciplined, relying primarily on a sophisticated range of blue-grays with strategic accent colors for interactive elements.

What distinguishes One UI from other enterprise design systems is its balance between professionalism and approachability. The interface feels trustworthy and stable without being cold, using warm undertones in its grays and thoughtful micro-interactions that suggest careful craftsmanship.

**Key Characteristics:**
- Soft gray-blue canvas (`#f7f7fc`) creating a calm, professional atmosphere
- Nunito Sans typography system providing humanist warmth to enterprise UI
- Sophisticated blue-gray neutral palette with warm undertones
- Subtle layering system using gentle shadows and 1px borders
- Clean, uncluttered layouts emphasizing content hierarchy
- Japanese-influenced minimalism with enterprise functionality

## 2. Color Palette & Roles

### Primary
- **Charcoal Text** (`#151518`): The primary text color — a near-black with subtle warmth, used for headings and primary content
- **Medium Gray** (`#2e3338`): Secondary text color for less prominent content and UI labels
- **Soft Gray** (`#5c6570`): Tertiary text color for metadata, captions, and disabled states

### Secondary & Accent
- **Link Blue** (`#246bfd`): Primary interactive color for links and call-to-action elements
- **Focus Blue** (`#4285f4`): Used for focus states and active interactive elements
- **Success Green** (`#00c851`): For positive feedback and success states
- **Error Red** (`#ff4444`): For error states and destructive actions

### Surface & Background
- **Primary Background** (`#f7f7fc`): The main page background — a soft gray-blue that's easier on the eyes than pure white
- **Card Surface** (`#ffffff`): Clean white for content cards and elevated surfaces
- **Secondary Surface** (`#f6f9fc`): Subtle gray-blue for secondary backgrounds and input fields
- **Border Light** (`#d9e5f2`): Light border color for subtle divisions and input outlines

### Neutrals & Text
- **Border Medium** (`#c4d3e0`): Medium border color for more prominent divisions
- **Disabled Gray** (`#8892a0`): For disabled text and inactive elements
- **Placeholder Gray** (`#a8b2c0`): For placeholder text and subtle UI elements
- **Divider Gray** (`#e8ecf0`): For subtle dividers and background elements

## 3. Typography Rules

### Font Family
- **Primary**: "Nunito Sans" — A humanist sans-serif providing excellent readability
- **Fallback Stack**: -apple-system, ".SFNSText-Regular", "San Francisco", "system-ui", "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif

### Typography Hierarchy
- **H1 Headlines**: 32px, font-weight: 400, line-height: normal
- **H2 Subheadings**: 24px, font-weight: 400, line-height: normal
- **Body Text**: 16px, font-weight: 400, line-height: normal
- **UI Labels**: 14px, font-weight: 700, line-height: normal
- **Small Text**: 13px, font-weight: 400, line-height: normal
- **Micro Text**: 12px, font-weight: 700, line-height: 12px

### Font Weights Available
- **Regular**: 400 (normal and italic)
- **Bold**: 700 (normal and italic)

### Letter Spacing
- All text uses `letter-spacing: normal` for optimal readability
- No custom letter spacing adjustments across the system

## 4. Component Stylings

### Buttons
**Primary Button**:
- Background: `#246bfd`
- Color: `#ffffff`
- Font: 12px, weight 700
- Padding: 0px 9px
- Border-radius: 4px
- Box-shadow: none

**Secondary Button**:
- Background: `rgba(0, 0, 0, 0)` (transparent)
- Color: `#5c6570`
- Font: 12px, weight 700
- Padding: 0px 7px
- Border-radius: 4px
- Box-shadow: none

**Link Button**:
- Background: `#f6f9fc`
- Color: `#2e3338`
- Font: 12px, weight 700
- Line-height: 12px
- Border-radius: 4px
- Box-shadow: `rgb(217, 229, 242) 0px 0px 0px 1px inset`

### Input Fields
- Background: `rgba(0, 0, 0, 0)` (transparent)
- Color: `#151518`
- Font: 13px, weight 400
- Border-radius: 0px
- Box-shadow: none
- Padding: 0px

### Navigation Links
**Active Navigation**:
- Background: `rgba(0, 0, 0, 0)`
- Color: `#ffffff`
- Font: 14px, weight 700
- Padding: 5px 6px 4px 22px
- Border-radius: 4px

**Standard Navigation**:
- Color: `#151518`
- Font: 14px, weight 700
- Padding: 2px 3px
- Border-radius: 3px
- Margin: -3px -4px

## 5. Layout Principles

### Spacing System
Based on analysis of the computed styles, the system appears to use a flexible spacing approach:
- **Micro spacing**: 2px, 3px, 4px for fine adjustments
- **Small spacing**: 5px, 6px, 7px for component internal spacing
- **Medium spacing**: 9px for button padding
- **Large spacing**: 22px for navigation indentation

### Grid System
- Uses CSS Grid and Flexbox for layout
- Container-based approach with sidebar navigation
- Responsive variables: `--nav-width: 300px`, `--right-panel-width: 400px`, `--bottom-panel-height: 300px`

### Container Approach
- Main content areas use semantic containers
- Sidebar navigation with fixed width
- Flexible main content area that adapts to available space

## 6. Depth & Elevation

### Shadow System
The system uses a minimal shadow approach:
- **Inset borders**: `rgb(217, 229, 242) 0px 0px 0px 1px inset` for subtle button borders
- **No drop shadows**: Relies on background color changes and borders for elevation
- **Border-based depth**: Uses 1px borders and background color shifts instead of shadows

### Layering Strategy
- Background layers use subtle color variations
- Interactive elements use background color changes on hover/focus
- Minimal z-index usage, relying on natural document flow

## 7. Do's and Don'ts

### Do's
- Use Nunito Sans for all text content to maintain consistency
- Stick to the established color palette for all UI elements
- Use 4px border-radius for interactive elements like buttons
- Employ subtle background color changes for hover states
- Maintain the established spacing rhythm for consistent layouts
- Use font-weight 700 for UI labels and interactive text

### Don'ts
- Don't use drop shadows — the system relies on borders and background changes
- Don't deviate from the Nunito Sans font family
- Don't use pure black (`#000000`) — use the warmer `#151518` instead
- Don't use bright, saturated colors that clash with the neutral palette
- Don't use custom letter-spacing — keep it at normal
- Don't use font weights other than 400 and 700

## 8. Responsive Behavior

### Breakpoints
Based on the CSS variables and structure:
- **Desktop**: Default layout with 300px sidebar
- **Tablet**: Collapsible sidebar navigation
- **Mobile**: Full-width layout with hidden sidebar

### Adaptive Strategy
- Uses CSS custom properties for dynamic sizing
- Sidebar collapses on smaller screens
- Content reflows naturally using flexbox and grid
- Maintains readability across all device sizes

## 9. Agent Prompt Guide

### Quick Reference for AI Agents

**Color Palette Summary:**
- Primary background: `#f7f7fc`
- Primary text: `#151518`
- Interactive blue: `#246bfd`
- Secondary text: `#2e3338`
- Borders: `#d9e5f2`

**Typography Quick Reference:**
- Font: "Nunito Sans"
- Body: 16px/400
- Labels: 14px/700
- Buttons: 12px/700
- Headings: 24px-32px/400

**Component Patterns:**
- Buttons: 4px border-radius, no shadows
- Spacing: 4px-22px range
- Borders: 1px solid with light colors
- Backgrounds: Subtle color variations, no gradients

### Recommended Prompts

**For creating buttons:**
"Create a button using Nunito Sans 12px bold, 4px border-radius, with background #246bfd and white text, padding 0px 9px"

**For layout components:**
"Design a card component with white background on #f7f7fc base, using subtle #d9e5f2 borders and Nunito Sans typography"

**For navigation elements:**
"Build navigation using #151518 text, 14px bold Nunito Sans, with 4px border-radius hover states and subtle background changes"