# Design System Inspiration of Cohere

## 1. Visual Theme & Atmosphere

Cohere's interface is a data-driven command center reimagined as an approachable enterprise platform — vibrant yet professional, dynamic yet trustworthy. The entire experience is built on a clean white canvas (`rgb(255, 255, 255)`) that serves as a neutral foundation for the signature vibrant gradients and data visualizations. Where most enterprise AI platforms lean into sterile corporate aesthetics, Cohere's design radiates energy and innovation through its bold use of color and modern typography.

The signature move is the custom "Unica77 Cohere Web" typeface — a clean, geometric sans-serif that balances technical precision with human readability. Combined with strategic use of vibrant gradients, data-rich dashboard components, and carefully orchestrated white space, the visual language says "powerful yet accessible" rather than "complex and intimidating." The typography system breathes with comfortable line-heights (1.4–1.6), creating a rhythm that feels both professional and engaging.

What makes Cohere's design truly distinctive is its sophisticated gradient system and data-centric aesthetic. The interface employs vibrant color transitions that suggest AI processing and data flow, while maintaining enterprise-grade professionalism. Navigation elements use precise spacing (`padding: 16px 40px`) and the color system alternates between pure white backgrounds and inverse dark surfaces, creating clear visual hierarchy and focus areas.

**Key Characteristics:**
- Clean white primary canvas (`rgb(255, 255, 255)`) with strategic dark inverse surfaces
- Custom Unica77 Cohere Web typeface family with Inter fallback for maximum compatibility
- Vibrant gradient system suggesting data flow and AI processing
- Data-rich dashboard aesthetic with emphasis on information density
- Precise spacing system with consistent padding (16px, 40px) and responsive breakpoints
- High contrast color inversions for focus and hierarchy
- Enterprise-grade professionalism balanced with approachable modern design

## 2. Color Palette & Roles

### Primary
- **Pure White** (`rgb(255, 255, 255)`): The primary background color and light-theme surface — clean, professional, and providing maximum contrast for content readability.
- **Pure Black** (`rgb(0, 0, 0)`): Primary text color on light surfaces — sharp, readable, and providing maximum accessibility contrast.
- **Inverse Surface** (`bg-surface-inverse`): Dark background surfaces that create focus areas and visual hierarchy breaks.

### Secondary & Accent
- **Neutral 50** (`text-neutral-50`): Secondary text color used for eyebrow text and less prominent content — likely a mid-gray tone.
- **Pure White on Dark** (`rgb(255, 255, 255)` on dark surfaces): Text and UI elements on inverse/dark backgrounds.

### Functional Colors
- **Border Pure White** (`border-pureWhite`): Border color for elements on dark surfaces, creating subtle definition.
- **Gradient Accents**: Vibrant gradient system (specific values not captured but evident in design description) used for brand moments and data visualization.

### Surface & Background
- **Primary Background** (`rgb(255, 255, 255)`): Main page background providing clean, professional foundation.
- **Inverse Background** (`bg-surface-inverse`): Dark surface areas for contrast and visual hierarchy.

## 3. Typography Rules

### Font Stack
**Primary**: `"Unica77 Cohere Web", Inter, Arial, ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"`

### Type Scale & Usage
- **Headline Large** (`text-web3-24`): 24px, line-height: 31.2px (1.3) — Major section headings
- **Headline Medium** (`text-web3-20`): 20px, responsive to 24px on large screens — Secondary headings
- **Body Text** (`text-web3-16`): 16px, line-height: 22.4px (1.4) — Primary body content
- **Small Text** (`text-web3-14`): 14px, line-height: 19.6px (1.4) — Secondary content, captions
- **Eyebrow Text** (`text-web3-14-eyebrow`): 14px, uppercase, font-family: eyebrow variant — Category labels, metadata

### Typography Principles
- **Weight**: Consistent 400 (regular) weight across all text elements
- **Letter Spacing**: Normal spacing maintained for optimal readability
- **Line Height**: Comfortable 1.3-1.4 ratio for excellent readability
- **Case**: Strategic use of uppercase for eyebrow/category text
- **Responsive**: Text scales appropriately (20px → 24px on large screens)

## 4. Component Stylings

### Navigation
```css
nav {
  padding: 16px 40px;
  background: rgb(255, 255, 255);
  position: fixed;
  z-index: nav-level;
  transition: all 300ms ease-in-out;
}

@media (max-width: 768px) {
  nav { padding: 16px 24px; }
}

@media (max-width: 919px) {
  nav { padding: 16px 16px; }
}
```

### Buttons
```css
button {
  transition: all 300ms;
  font-size: 16px;
  line-height: 24px;
}

button:hover {
  transform: rotate(90deg); /* Specific to nav toggle */
}
```

### Links
```css
a {
  color: inherit;
  text-decoration: none;
  border-bottom: 1px solid currentColor; /* On dark surfaces */
  transition: all 300ms;
}
```

### Cards & Containers
- Clean white backgrounds with subtle shadows
- Consistent internal padding following 16px/40px system
- Responsive margin and padding adjustments

## 5. Layout Principles

### Grid System
- **Container Max Width**: Responsive with breakpoints at 768px, 919px
- **Horizontal Padding**: 
  - Desktop (>919px): 40px
  - Tablet (768px-919px): 24px  
  - Mobile (<768px): 16px

### Spacing Scale
- **Micro**: 4px, 8px — Internal component spacing
- **Small**: 16px — Standard padding, small gaps
- **Medium**: 24px — Section spacing, medium gaps
- **Large**: 40px — Major section breaks, container padding
- **XL**: 80px+ — Page-level section spacing

### Responsive Breakpoints
```css
/* Mobile First Approach */
@media (min-width: 768px) { /* Tablet */ }
@media (min-width: 919px) { /* Desktop */ }
@media (min-width: 1200px) { /* Large Desktop */ }
```

### Layout Patterns
- **Flex-based**: Heavy use of flexbox for component layout
- **Gap System**: Consistent 10px, 16px, 24px gaps between elements
- **Alignment**: Strategic use of justify-between, items-center
- **Auto Margins**: `mr-auto` for flexible spacing in navigation

## 6. Depth & Elevation

### Shadow System
- **None**: `box-shadow: none` — Flat elements, clean aesthetic
- **Subtle**: Minimal shadows for card elevation (values not captured)
- **Focus**: Likely ring-based focus indicators for accessibility

### Z-Index Scale
- **Navigation**: `z-nav` (custom property, likely z-index: 100)
- **Overlays**: Higher values for modals, dropdowns
- **Content**: Default stacking context (z-index: auto)

### Elevation Principles
- Minimal shadow usage maintaining clean, flat aesthetic
- Strategic use of background color changes for depth
- Inverse surfaces create natural depth without shadows
- Focus states likely use ring-based elevation

## 7. Do's and Don'ts

### Do's
✅ **Use the complete font stack** — Always include the full Unica77 Cohere Web fallback chain
✅ **Maintain 1.4 line-height** — Ensures optimal readability across all text sizes
✅ **Follow the responsive padding system** — 16px/24px/40px based on breakpoints
✅ **Use inverse surfaces strategically** — Dark backgrounds for focus and hierarchy
✅ **Implement smooth transitions** — 300ms duration for all interactive elements
✅ **Preserve white space** — Clean, uncluttered layouts are core to the aesthetic
✅ **Use uppercase sparingly** — Only for eyebrow/category text
✅ **Maintain high contrast** — Pure black on white, pure white on dark

### Don'ts
❌ **Don't use colored text on white** — Stick to black for maximum readability
❌ **Don't add unnecessary shadows** — The design is intentionally flat and clean
❌ **Don't break the spacing system** — Arbitrary padding/margins disrupt the rhythm
❌ **Don't use multiple font weights** — 400 weight maintains consistency
❌ **Don't ignore responsive breakpoints** — Layout must adapt at 768px and 919px
❌ **Don't overuse gradients** — Reserve for specific brand/data moments
❌ **Don't create low contrast combinations** — Accessibility is paramount
❌ **Don't use rounded corners excessively** — Clean, geometric aesthetic

## 8. Responsive Behavior

### Navigation Adaptation
```css
/* Desktop Navigation */
@media (min-width: 919px) {
  nav { padding: 16px 40px; }
  .nav-items { display: flex; gap: 40px; }
}

/* Tablet Navigation */
@media (max-width: 918px) {
  nav { padding: 16px 24px; }
  .mobile-menu { display: block; }
}

/* Mobile Navigation */
@media (max-width: 767px) {
  nav { padding: 16px; }
  .nav-toggle { display: block; }
}
```

### Typography Scaling
```css
/* Responsive Text Sizes */
.text-responsive {
  font-size: 20px;
  line-height: 28px;
}

@media (min-width: 1024px) {
  .text-responsive {
    font-size: 24px;
    line-height: 31.2px;
  }
}
```

### Layout Adaptations
- **Desktop**: Multi-column layouts, horizontal navigation
- **Tablet**: Reduced padding, simplified navigation
- **Mobile**: Single column, hamburger menu, touch-optimized spacing

### Content Prioritization
- Hero content remains prominent across all sizes
- Secondary content may stack or hide on smaller screens
- Navigation collapses to hamburger menu below 919px
- Maintain readability with consistent line-heights

## 9. Agent Prompt Guide

When creating interfaces in the Cohere design system, use this prompt structure:

**"Create a [component/page] following Cohere's enterprise AI design system:**

**Visual Foundation:**
- Clean white background (`rgb(255, 255, 255)`) with strategic dark inverse surfaces
- Unica77 Cohere Web typography with Inter fallback
- High contrast: pure black text on white, pure white text on dark
- Vibrant gradients for data visualization and brand moments

**Layout & Spacing:**
- Responsive padding: 16px (mobile), 24px (tablet), 40px (desktop)
- Flexbox-based layouts with consistent gaps (10px, 16px, 24px)
- Breakpoints at 768px and 919px
- Clean, geometric spacing following 8px grid

**Typography:**
- 24px headlines (31.2px line-height)
- 16px body text (22.4px line-height)  
- 14px secondary text (19.6px line-height)
- 400 font weight throughout
- Uppercase only for eyebrow/category labels

**Interactions:**
- 300ms transitions on all interactive elements
- Subtle hover states maintaining accessibility
- Ring-based focus indicators
- Smooth state changes

**Data-Rich Aesthetic:**
- Dashboard-style information density
- Strategic use of inverse surfaces for hierarchy
- Gradient accents suggesting AI/data processing
- Professional yet approachable enterprise feel

Make it feel like a sophisticated AI platform that's both powerful and accessible."**