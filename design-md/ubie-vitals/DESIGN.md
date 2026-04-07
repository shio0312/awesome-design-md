# Design System Documentation: Ubie Vitals

## 1. Visual Theme & Atmosphere

Ubie Vitals embodies a clinical precision meets approachable healthcare design philosophy. The interface feels like a modern medical facility — clean, trustworthy, and professionally warm. Unlike typical tech design systems that lean heavily into bright blues or stark minimalism, Ubie Vitals creates a healthcare-focused aesthetic that balances medical authority with human accessibility.

The design language is built around a sophisticated neutral foundation with strategic red accents that serve as both brand identity and functional emphasis. The primary typeface is a carefully chosen sans-serif stack (`"Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif`) that ensures excellent readability across both Western and Japanese text, reflecting Ubie's international healthcare focus.

What sets Ubie Vitals apart is its thoughtful approach to healthcare UX — every element feels considered for both medical professionals and patients. The red accent color (`rgb(57, 89, 204)` for links, with stronger reds for emphasis) creates a visual hierarchy that guides users through complex medical information without feeling overwhelming.

**Key Characteristics:**
- Clean white canvas (`rgb(255, 255, 255)`) with sophisticated neutral text (`rgb(50, 53, 58)`)
- Strategic use of Ubie red (`--color-ubie-red-600`) for critical actions and brand moments
- International typography stack optimized for multilingual healthcare content
- Systematic spacing using CSS custom properties (`--size-spacing-*`)
- Border-based component definition with subtle radius (`--radius-sm`)
- Healthcare-appropriate color psychology balancing trust and urgency

## 2. Color Palette & Roles

### Primary
- **Ubie Black** (`rgb(50, 53, 58)` / `--color-text-main`): Primary text color — a warm charcoal that's easier on the eyes than pure black while maintaining excellent readability for medical content.
- **Ubie Red 600** (`--color-ubie-red-600`): Core brand color used for critical actions, required field indicators, and primary emphasis. Designed to convey medical urgency without alarm.
- **Link Blue** (`rgb(57, 89, 204)`): Standard link color providing clear interactive affordance while remaining accessible.

### Secondary & Accent
- **Ubie Black 600** (`--color-ubie-black-600`): Secondary text color for table headers and less prominent content.
- **Text Sub** (`--color-text-sub`): Subdued text color for optional field labels and secondary information.

### Surface & Background
- **Pure White** (`rgb(255, 255, 255)`): Primary background color creating a clean, clinical foundation.
- **Background Black Darken** (`--color-background-black-darken`): Subtle background tint for table headers and section differentiation.

### Borders & Structure
- **Border Black** (`--color-border-black`): Primary border color for tables, cards, and component boundaries.

### Functional Colors
- **Required Red** (`--color-ubie-red-600`): Used for required field indicators and critical form elements.
- **Error States**: Leveraging the red palette for validation and error messaging.

## 3. Typography Rules

### Font Family
**Primary Stack**: `"Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif`
- Optimized for international healthcare content
- Excellent readability in both Latin and Japanese scripts
- Professional, medical-grade typography

### Typography Scale
- **Body Text**: `16px` base size with `27.2px` line-height (1.7 ratio)
- **Body Small**: `--text-body-sm-size` with `--text-body-sm-narrow-line`
- **Note Medium**: `--text-note-md-size` with `--text-note-md-line`

### Font Weights
- **Regular**: `400` for body text and standard content
- **Bold**: `700` for navigation links, table row headers, and emphasis

### Line Height System
- **Standard**: `27.2px` (1.7) for optimal reading comfort
- **Narrow**: `--text-body-sm-narrow-line` for compact layouts
- **Note**: `--text-note-md-line` for smaller text elements

## 4. Component Stylings

### Navigation Links
```css
.link {
  font-weight: 700;
  border-radius: 4px;
  padding: 8px 16px;
  display: inline-flex;
  gap: var(--size-spacing-xxs);
  align-items: center;
}
```

### Tables
```css
.tableWrapper {
  border: 1px solid var(--color-border-black);
  border-radius: var(--radius-sm);
}

thead > tr {
  background-color: var(--color-background-black-darken);
}

th, td {
  padding: var(--size-spacing-sm);
  font-size: var(--text-body-sm-size);
  line-height: var(--text-body-sm-narrow-line);
}
```

### Buttons
```css
button {
  background-color: transparent;
  border-radius: 0px;
  padding: varies by context;
}
```

### Interactive States
- **Active**: `background-color: #00000026` for pressed states
- **Focus**: Maintained accessibility standards
- **Hover**: Subtle feedback maintaining professional appearance

## 5. Layout Principles

### Spacing System
Based on CSS custom properties with systematic scaling:
- `--size-spacing-xxs`: Minimal spacing for tight layouts
- `--size-spacing-xs`: Small component spacing
- `--size-spacing-sm`: Standard component padding (`var(--size-spacing-sm)`)
- `--size-spacing-md`: Medium section spacing
- `--size-spacing-lg`: Large section breaks
- `--size-spacing-xl`: Major layout spacing
- `--size-spacing-xxl`: Maximum spacing for page sections

### Stack Component
Flexible vertical spacing system:
```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--size-spacing-*);
}
```

### Container Strategy
- Header padding: `28px 32px` for logo areas
- Navigation padding: `0px 8px` for mobile, `0px 16px 24px` for expanded
- Content padding: Systematic use of spacing variables

## 6. Depth & Elevation

### Border System
Primary depth strategy using borders rather than shadows:
- `1px solid var(--color-border-black)` for component boundaries
- Table row separators: `border-top: 1px solid var(--color-border-black)`

### Border Radius
- **Small Radius**: `var(--radius-sm)` for subtle component rounding
- **Button Radius**: `4px` for interactive elements
- **Default**: `0px` maintaining clean, clinical edges

### Layering
Minimal shadow usage, preferring border-based depth for medical clarity.

## 7. Do's and Don'ts

### Do's
- ✅ Use the systematic spacing variables for all layout decisions
- ✅ Maintain the warm charcoal text color for optimal readability
- ✅ Apply Ubie red strategically for required fields and critical actions
- ✅ Ensure international typography support with the full font stack
- ✅ Use border-based component definition for clinical clarity
- ✅ Implement responsive spacing with device-specific classes

### Don'ts
- ❌ Don't use pure black text — always use the warm charcoal (`rgb(50, 53, 58)`)
- ❌ Don't overuse the red accent — reserve for truly important elements
- ❌ Don't ignore the spacing system — arbitrary margins break consistency
- ❌ Don't use heavy shadows — borders provide cleaner medical aesthetic
- ❌ Don't forget mobile navigation patterns for healthcare workflows

## 8. Responsive Behavior

### Breakpoints
- **Mobile**: Base styles (default)
- **Tablet**: `@media (width >= 640px)`
- **Desktop**: `@media (width >= 768px)`

### Responsive Spacing
Dynamic spacing classes for each breakpoint:
```css
.mobileXs { gap: var(--size-spacing-xs); }
.tabletXs { gap: var(--size-spacing-xs); }
.desktopXs { gap: var(--size-spacing-xs); }
```

### Navigation Strategy
- Mobile: Collapsible navigation with toggle button
- Desktop: Expanded horizontal navigation
- Touch-friendly padding: `8px 16px` minimum

## 9. Agent Prompt Guide

### Quick Reference for AI Agents

**Color Palette**:
- Primary text: `rgb(50, 53, 58)`
- Background: `rgb(255, 255, 255)`
- Brand red: `--color-ubie-red-600`
- Links: `rgb(57, 89, 204)`

**Typography**:
- Font: `"Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif`
- Base size: `16px`
- Line height: `27.2px`
- Bold weight: `700`

**Spacing**:
- Use CSS custom properties: `var(--size-spacing-sm)`, etc.
- Responsive classes: `.mobileSm`, `.tabletMd`, `.desktopLg`

### Recommended Prompts

**For Component Creation**:
"Create a healthcare-focused component using Ubie Vitals design system with warm charcoal text (`rgb(50, 53, 58)`), systematic spacing variables, and strategic red accents for critical actions."

**For Layout Design**:
"Design a responsive layout using Ubie's stack component system with device-specific spacing classes and border-based component definition."

**For Form Elements**:
"Build accessible form components with Ubie red required indicators, proper typography hierarchy, and international font support."