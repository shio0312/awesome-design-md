# Design System Inspiration of Spindle (Ameba Design)

## 1. Visual Theme & Atmosphere

Spindle's design system embodies a refined, professional aesthetic that balances Japanese design sensibilities with modern web standards. The interface presents itself as a clean, systematic documentation platform — methodical yet approachable, with a distinctly Japanese attention to detail and hierarchy.

The design philosophy centers around clarity and accessibility, using a neutral color palette anchored by a sophisticated dark navy (`rgb(8, 18, 26)`) as the primary text color against clean white backgrounds. This creates high contrast for excellent readability while maintaining a professional, enterprise-grade appearance suitable for design system documentation.

What sets Spindle apart is its thoughtful typography system that accommodates both Japanese and English content seamlessly. The font stack prioritizes Japanese fonts (Meiryo, Yu Gothic Medium) before falling back to system fonts, ensuring optimal rendering across different languages and platforms. The generous letter-spacing of `1.6px` creates breathing room that enhances readability, particularly important for mixed-language content.

The visual language emphasizes structure and organization through consistent spacing, subtle borders, and a grid-based layout system. Component cards use gentle border-radius values (`16px`) and soft borders to create definition without harsh lines, reflecting a modern, friendly approach to technical documentation.

**Key Characteristics:**
- Clean, documentation-focused aesthetic with Japanese design sensibilities
- High-contrast neutral palette with sophisticated dark navy primary text
- Mixed-language typography system optimized for Japanese and English
- Generous letter-spacing (`1.6px`) for enhanced readability
- Soft, rounded component styling with `16px` border-radius
- Grid-based layout with systematic spacing
- Professional yet approachable tone suitable for design system documentation

## 2. Color Palette & Roles

### Primary
- **Spindle Navy** (`rgb(8, 18, 26)` / `#08121a`): The primary text color — a sophisticated dark navy that provides excellent contrast while being softer than pure black. Used for headlines, body text, and primary UI elements.
- **Pure White** (`rgb(255, 255, 255)` / `#ffffff`): Primary background color creating clean, uncluttered surfaces for content.

### Surface & Background
- **Light Gray Surface** (`rgb(239, 239, 239)` / `#efefef`): Used for button backgrounds and secondary surface elements.
- **Secondary Surface** (CSS variable `--color-surface-secondary`): Applied to icon containers and secondary UI elements.

### Border & Emphasis
- **Low Emphasis Border** (CSS variable `--color-border-low-emphasis`): Subtle borders for component separation and definition.
- **High Emphasis Text** (CSS variable `--color-text-high-emphasis`): For primary content and important information.
- **Medium Emphasis Text** (CSS variable `--color-text-medium-emphasis`): For secondary content and descriptions.
- **Low Emphasis Text** (CSS variable `--color-text-low-emphasis`): For captions, labels, and tertiary information.

### Accent & Interactive
- **Accent Primary** (CSS variable `--color-text-accent-primary`): Used for links, primary actions, and brand moments.
- **Focus Clarity** (CSS variable `--color-focus-clarity`): Accessibility-focused color for focus states and interactive feedback.

## 3. Typography Rules

### Font Family Hierarchy
- **Primary Stack**: `Meiryo, "Yu Gothic Medium", system-ui, -apple-system, "system-ui", sans-serif`
- **Japanese Priority**: Meiryo and Yu Gothic Medium prioritized for optimal Japanese character rendering
- **System Fallbacks**: Modern system font stack for cross-platform consistency

### Typography Scale & Hierarchy
- **Headline 5** (CSS variable `--type-headline-5`): Primary page titles and major section headers
- **Headline 6** (CSS variable `--type-headline-6`): Secondary headings and component names
- **Body 4** (CSS variable `--type-body-4`): Primary body text and descriptions
- **Caption EN 3** (CSS variable `--type-caption-en-3`): English captions and labels
- **Caption EN 4** (CSS variable `--type-caption-en-4`): Small labels and metadata

### Specific Measurements
- **Base Font Size**: `16px` for body text
- **Large Headline**: `24px` with `700` weight and `31.2px` line-height
- **Navigation Text**: `14px` with `700` weight and `18.2px` line-height
- **Letter Spacing**: Consistent `1.6px` across most text elements for enhanced readability
- **Line Height Ratios**: Approximately 1.3 for headlines, 1.3 for body text

### Font Weights
- **Regular**: `400` for body text and secondary content
- **Bold**: `700` for headlines, navigation, and emphasis

## 4. Component Stylings

### Buttons
- **Default Button**: 
  - Background: `rgb(239, 239, 239)` (`#efefef`)
  - Text: `rgb(0, 0, 0)` (black)
  - Padding: `1px 6px`
  - Font: `16px` regular weight
  - Line-height: `18.4px`
  - Border-radius: `0px` (minimal styling approach)

### Links (TextLink Component)
- **Primary Links**:
  - Color: CSS variable `--color-text-accent-primary`
  - Font-weight: `bold`
  - Text-decoration: `underline`
  - Border-radius: `4px`
  - Line-height: `1.3`
- **Subtle Links**:
  - Color: CSS variable `--color-text-low-emphasis`
  - Reduced visual emphasis for secondary actions
- **Focus State**:
  - Outline: `2px solid var(--color-focus-clarity)`
  - Outline-offset: `1px`
- **Icon Links**:
  - Display: `inline-flex` with `align-items: center`
  - Icon spacing: `4px` margin

### Cards & Panels
- **Panel Navigation Items**:
  - Border: `1px solid var(--color-border-low-emphasis)`
  - Border-radius: `16px`
  - Padding: `24px`
  - Background: Transparent with hover states
- **Icon Containers**:
  - Size: `80px × 80px`
  - Border-radius: `16px`
  - Background: CSS variable `--color-surface-secondary`
  - Border: `1px solid var(--color-border-low-emphasis)`
  - Icon size: `40px × 40px` or `20px` font-size

### Navigation
- **Header Navigation**:
  - Font-size: `14px`
  - Font-weight: `700`
  - Letter-spacing: `1.6px`
  - Color: Primary navy (`rgb(8, 18, 26)`)

## 5. Layout Principles

### Spacing System
- **Micro Spacing**: `4px` for icon margins and small gaps
- **Small Spacing**: `8px` for component internal spacing
- **Medium Spacing**: `12px`, `16px`, `20px` for component margins
- **Large Spacing**: `24px`, `32px` for section separation
- **XL Spacing**: `44px`, `48px`, `80px` for major layout divisions

### Grid System
- **Icon Grid**: `repeat(auto-fill, minmax(80px, 1fr))` with `48px 32px` gap
- **Two-Column Layout**: `1fr 1fr` for panel navigation items
- **Gap Values**: `32px 24px` for card grids, `48px 32px` for icon grids

### Container & Content Width
- **Content Padding**: `44px` left padding for main content areas
- **Panel Margins**: `80px` top margin for major sections
- **Responsive Behavior**: Grid collapses to single column on mobile with `24px` vertical spacing

## 6. Depth & Elevation

### Shadow System
- **Minimal Shadows**: The design system favors borders over shadows for a clean, flat aesthetic
- **Border-based Depth**: Uses `1px solid` borders with low-emphasis colors for subtle separation
- **Focus Rings**: `2px solid` outlines for accessibility and interaction feedback

### Layering Approach
- **Surface Hierarchy**: Achieved through background color variations rather than shadows
- **Border Emphasis**: Different border colors (`--color-border-low-emphasis`) create visual hierarchy
- **Color-based Depth**: Text emphasis levels (high, medium, low) create information hierarchy

## 7. Do's and Don'ts

### Do's
- **Maintain Consistent Letter-spacing**: Always use `1.6px` letter-spacing for optimal Japanese/English mixed content
- **Use Semantic Color Variables**: Leverage CSS custom properties for consistent theming
- **Prioritize Accessibility**: Implement proper focus states and high contrast ratios
- **Follow Grid Systems**: Use established spacing values (24px, 32px, 48px, 80px)
- **Respect Typography Hierarchy**: Use defined type scales for consistent information architecture

### Don'ts
- **Avoid Pure Black**: Use the sophisticated navy (`#08121a`) instead of `#000000`
- **Don't Mix Spacing Systems**: Stick to the 4px-based spacing scale
- **Avoid Heavy Shadows**: The system favors clean borders over drop shadows
- **Don't Override Font Stack**: Maintain Japanese font priority in typography
- **Avoid Inconsistent Border Radius**: Use `16px` for cards, `4px` for interactive elements

## 8. Responsive Behavior

### Breakpoints
- **Mobile Breakpoint**: `max-width: 768px`
- **Desktop-first Approach**: Default styles target desktop, with mobile overrides

### Mobile Adaptations
- **Grid Collapse**: Two-column grids become single-column stacks
- **Spacing Reduction**: Maintains `24px` vertical spacing between stacked elements
- **Navigation Adaptation**: Header navigation likely collapses (based on button presence)

### Layout Adjustments
- **Content Padding**: Reduced left padding on mobile devices
- **Grid Gaps**: Simplified gap structure for smaller screens
- **Typography**: Maintains same font sizes across breakpoints for consistency

## 9. Agent Prompt Guide

### Quick Reference for AI Agents

When building interfaces inspired by Spindle's design system, use these key parameters:

**Color Prompt**: "Use a sophisticated dark navy (#08121a) for text on white backgrounds, with light gray (#efefef) for secondary surfaces. Implement a CSS variable system for text emphasis levels."

**Typography Prompt**: "Apply Meiryo and Yu Gothic Medium for Japanese text support, with 1.6px letter-spacing throughout. Use 16px base size, 24px for headlines, 14px for navigation, all with appropriate line-heights."

**Component Prompt**: "Create clean cards with 16px border-radius, 1px subtle borders, and 24px internal padding. Use 80px square icons with 16px border-radius. Implement bold links with underlines and 4px border-radius focus states."

**Layout Prompt**: "Follow a 4px-based spacing system with key values: 24px, 32px, 48px, 80px. Use CSS Grid with auto-fill patterns and collapse to single columns on mobile (768px breakpoint)."

**Interaction Prompt**: "Implement 2px focus outlines with 1px offset, hover states that remove underlines from text links, and maintain accessibility with high contrast ratios."

### Recommended Implementation Approach
1. Start with the neutral color palette and CSS variables
2. Implement the Japanese-priority font stack
3. Build components using the 16px border-radius and border-based depth
4. Apply the systematic spacing scale
5. Add responsive behavior with grid collapse patterns