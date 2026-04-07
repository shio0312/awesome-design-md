# Design System: OpenCode AI

## 1. Visual Theme & Atmosphere

OpenCode AI embraces a developer-first aesthetic that feels like a premium code editor brought to life as a web platform. The design centers around a warm, off-white canvas (`#fdfdfc`) that provides excellent contrast for code readability while maintaining visual comfort during extended coding sessions. This isn't the stark white of typical SaaS platforms, but rather a carefully calibrated surface that reduces eye strain.

The signature element is the Berkeley Mono typeface — a modern monospace font that bridges the gap between technical precision and visual elegance. Used consistently across the interface at 16px with 24px line-height (1.5), it creates a cohesive experience where every element feels native to a coding environment. The typography hierarchy is subtle but effective, relying on weight variations (400 for body, 500 for emphasis) rather than dramatic size changes.

OpenCode's color philosophy is refreshingly restrained. The palette revolves around warm, muted tones that feel more like a carefully curated terminal theme than typical web colors. The primary text color (`#201d1d`) is a warm near-black that's easier on the eyes than pure black, while secondary text (`#646262`) provides clear hierarchy without harsh contrast jumps. Interactive elements use the same warm dark tone (`#201d1d`) for backgrounds, creating a consistent visual language.

**Key Characteristics:**
- Warm off-white canvas (`#fdfdfc`) optimized for code readability
- Berkeley Mono typeface system creating editor-native feel
- Restrained warm color palette with muted, terminal-inspired tones
- Minimal visual hierarchy relying on typography weight over size
- Developer-centric spacing and proportions
- Subtle 4px border radius for modern but understated interactivity
- Monospace-first design philosophy extending beyond code blocks

## 2. Color Palette & Roles

### Primary
- **Warm Near Black** (`#201d1d`): Primary text color and dark interactive surfaces. A carefully warmed black that's gentler than pure black while maintaining excellent readability.
- **Secondary Warm Gray** (`#646262`): Secondary text, subtle UI elements, and inactive states. Provides clear hierarchy while staying within the warm tonal range.

### Surface & Background
- **Off-White Canvas** (`#fdfdfc`): Primary page background — a warm, slightly cream-tinted white that reduces eye strain during extended coding sessions.
- **Pure White** (`#ffffff`): Used sparingly for highest contrast moments and clean separation.

### Interactive States
- **Warm Dark Background** (`#201d1d`): Primary button backgrounds and active states, creating strong contrast against the light canvas.
- **Light Text on Dark** (`#fdfdfc`): Text color when placed on dark backgrounds, maintaining the warm tonal consistency.

### Typography Hierarchy
- **Primary Text** (`#1d1d1f`): Main body text with slight variation from the primary dark tone.
- **Medium Weight** (500): Used for emphasis and interactive elements like buttons.
- **Regular Weight** (400): Standard body text and most interface elements.

## 3. Typography Rules

### Font Stack
**Primary Monospace**: `"Berkeley Mono", "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`

### Size & Spacing System
- **Base Font Size**: 16px across all elements
- **Line Height**: 24px (1.5 ratio) for optimal code readability
- **Letter Spacing**: Normal (no additional tracking)

### Weight Hierarchy
- **Regular (400)**: Body text, navigation links, standard UI elements
- **Medium (500)**: Buttons, emphasized text, active states

### Typography Applications
- **Navigation**: 16px regular weight, maintaining consistency with body text
- **Buttons**: 16px medium weight for subtle emphasis
- **Body Text**: 16px regular weight with 24px line-height
- **Interactive Elements**: Consistent 16px sizing with weight variations for hierarchy

### Spacing Rules
- **Button Padding**: 8px vertical, 16px horizontal (10px left for visual balance)
- **Consistent Baseline**: All text elements align to the 24px baseline grid
- **No Size Scaling**: Typography hierarchy achieved through weight and color, not size variations

## 4. Component Stylings

### Buttons
```css
/* Primary Button */
background-color: #201d1d;
color: #fdfdfc;
font-weight: 500;
font-size: 16px;
line-height: 24px;
padding: 8px 16px 8px 10px;
border-radius: 4px;
border: none;
```

### Navigation Links
```css
/* Standard Navigation Link */
color: #201d1d;
font-weight: 400;
font-size: 16px;
line-height: 24px;
text-decoration: none;

/* Active State */
color: #201d1d;
font-weight: 400; /* No weight change for active */
```

### Interactive Elements
- **Border Radius**: 4px for subtle modern feel
- **Focus States**: Maintain color consistency with primary palette
- **Hover States**: Subtle opacity or background color shifts within warm tone range

### Container Elements
```css
/* Main Content Area */
background-color: #fdfdfc;
color: #646262;
padding-bottom: 80px;
```

## 5. Layout Principles

### Grid System
- **Flexible Layout**: No rigid grid system, content-driven responsive design
- **Generous Spacing**: 80px bottom padding on main content areas
- **Minimal Constraints**: Layout adapts to content rather than forcing content into rigid columns

### Spacing Scale
- **Micro Spacing**: 4px (border radius)
- **Small Spacing**: 8px (vertical button padding)
- **Medium Spacing**: 16px (horizontal button padding)
- **Large Spacing**: 80px (section bottom padding)

### Content Organization
- **Header Height**: Minimum 80px with flexbox centering
- **Navigation**: Horizontal layout with consistent spacing
- **Content Flow**: Vertical rhythm based on 24px baseline grid

### Responsive Approach
- **Mobile-First**: Viewport meta tag with width=device-width
- **Flexible Containers**: No fixed widths, content-driven sizing
- **Scalable Typography**: Consistent 16px base across all screen sizes

## 6. Depth & Elevation

### Shadow System
OpenCode AI uses minimal elevation, relying on color contrast and subtle borders rather than dramatic shadows.

- **No Box Shadows**: Clean, flat design aesthetic
- **Border-Based Separation**: Subtle borders and background color changes for depth
- **Color Contrast**: Primary method for creating visual hierarchy and depth

### Layering Hierarchy
1. **Background Layer**: Off-white canvas (`#fdfdfc`)
2. **Content Layer**: Primary text and elements
3. **Interactive Layer**: Dark buttons and active states (`#201d1d`)
4. **Overlay Layer**: Navigation and modal elements (when present)

### Visual Weight
- **Typography Weight**: Primary method for creating emphasis
- **Color Intensity**: Darker colors for higher priority elements
- **Size Consistency**: No size-based hierarchy, maintaining 16px throughout

## 7. Do's and Don'ts

### Do's
✅ **Use Berkeley Mono consistently** — Maintain the monospace aesthetic across all text elements
✅ **Stick to the warm color palette** — Keep all grays and blacks within the warm tonal range
✅ **Maintain 16px font size** — Consistency in sizing creates cohesive developer experience
✅ **Use 4px border radius** — Subtle modern touch without over-styling
✅ **Leverage font weight for hierarchy** — Use 400/500 weight variations for emphasis
✅ **Keep spacing generous** — Allow content to breathe with adequate padding
✅ **Maintain warm undertones** — Even whites and grays should feel warm, not clinical

### Don'ts
❌ **Don't introduce cool colors** — Avoid blues, cool grays, or stark whites
❌ **Don't vary font sizes dramatically** — Maintain the 16px consistency
❌ **Don't use heavy shadows** — Keep the flat, clean aesthetic
❌ **Don't break the monospace system** — Avoid sans-serif or serif fonts
❌ **Don't use pure black** — Stick to the warmed near-black (`#201d1d`)
❌ **Don't over-style interactive elements** — Keep buttons and links minimal
❌ **Don't ignore the baseline grid** — Maintain 24px line-height consistency

## 8. Responsive Behavior

### Breakpoint Strategy
OpenCode AI uses a content-first responsive approach rather than rigid breakpoints:

- **Flexible Containers**: Elements adapt to available space
- **Consistent Typography**: 16px font size maintained across all devices
- **Scalable Spacing**: Proportional padding and margins

### Mobile Adaptations
```css
/* Mobile Navigation */
.nav-toggle {
  display: block; /* Show hamburger on mobile */
  padding: 1px 6px;
  background: transparent;
}

/* Maintained Consistency */
font-size: 16px; /* No mobile font scaling */
line-height: 24px; /* Consistent baseline */
```

### Layout Flexibility
- **Header**: Flexbox centering maintains 80px minimum height
- **Navigation**: Collapses to hamburger menu on smaller screens
- **Content**: Maintains generous spacing proportionally
- **Buttons**: Consistent padding scales appropriately

### Touch Considerations
- **Button Sizing**: 8px vertical padding provides adequate touch targets
- **Spacing**: 16px horizontal spacing ensures comfortable interaction
- **Text Size**: 16px prevents mobile browser zoom

## 9. Agent Prompt Guide

When implementing OpenCode AI's design system, use this prompt template:

```
Create a [component/page] following OpenCode AI's design system:

VISUAL THEME: Developer-centric, warm monospace aesthetic
- Background: Off-white canvas (#fdfdfc) 
- Typography: Berkeley Mono, 16px, 24px line-height
- Palette: Warm near-black (#201d1d), warm gray (#646262)

TYPOGRAPHY RULES:
- Font: Berkeley Mono fallback stack
- Size: 16px consistent across all elements
- Weights: 400 (regular), 500 (emphasis)
- Line-height: 24px (1.5 ratio)

COMPONENT STYLING:
- Buttons: #201d1d background, #fdfdfc text, 500 weight, 8px/16px padding, 4px radius
- Links: #201d1d color, 400 weight, no decoration
- Spacing: 4px/8px/16px/80px scale
- No shadows, minimal borders, flat aesthetic

LAYOUT PRINCIPLES:
- Content-driven responsive design
- Generous spacing (80px section padding)
- Flexbox for alignment
- Mobile-first approach

Keep the warm, terminal-inspired feel while maintaining excellent readability and developer-focused functionality.
```

**Key Phrases for AI Implementation:**
- "Berkeley Mono monospace aesthetic"
- "Warm developer terminal theme"
- "16px consistent typography"
- "Minimal flat design with warm undertones"
- "Code editor inspired interface"
- "Generous spacing, subtle interactions"