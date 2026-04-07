# Design System Inspiration of Cursor

## 1. Visual Theme & Atmosphere

Cursor's interface embodies the aesthetic of a premium developer tool — sleek, minimal, and unapologetically modern. Built on a warm off-white canvas (`#f7f7f4`), the design strikes a balance between approachable warmth and technical precision. This isn't the sterile white of typical SaaS products, but a carefully chosen cream tone that reduces eye strain during long coding sessions.

The signature element is the custom CursorGothic typeface — a clean, geometric sans-serif that maintains excellent readability at all sizes while projecting technical competence. The typography system is complemented by Berkeley Mono for code display and JJ Annon for editorial content, creating a sophisticated hierarchy that serves both marketing and product contexts.

Cursor's visual language centers around subtle gradients and refined shadows that create depth without distraction. The interface uses a restrained color palette dominated by warm neutrals (`#262520` for text, `#f7f7f4` for backgrounds) with strategic accent colors that appear in CTAs and interactive elements. Every element feels purposefully placed, with generous whitespace and precise alignment creating a sense of premium craftsmanship.

The overall atmosphere is one of quiet confidence — this is a tool built by developers, for developers, with an aesthetic that respects the user's intelligence while remaining visually appealing to a broader audience.

**Key Characteristics:**
- Warm off-white primary background (`#f7f7f4`) — softer than pure white, easier on developer eyes
- Custom CursorGothic typeface system with Berkeley Mono for code and JJ Annon for editorial
- Restrained neutral palette with warm undertones throughout
- Subtle gradient treatments and refined shadow systems
- Generous whitespace and precise geometric alignment
- Premium button styling with rounded corners (`33554400px` border-radius for pill shapes)
- Clean, minimal iconography with consistent stroke weights

## 2. Color Palette & Roles

### Primary
- **Cursor Dark** (`#262520`): Primary text color — a warm, dark brown-black that's softer than pure black while maintaining excellent contrast. Used for body text, headings, and primary UI elements.
- **Cursor Background** (`#f7f7f4`): Primary page background — a warm off-white with subtle cream undertones that reduces eye strain and creates a premium feel.
- **Cursor White** (`#f7f7f4`): Used for button text on dark backgrounds and inverted UI elements.

### Interactive & Accent
- **Button Dark** (`#262520`): Primary CTA background color, creating strong contrast against the light background.
- **Link Blue** (inherited): Standard link color for navigation and interactive text elements.
- **Focus States**: Subtle outline treatments for accessibility compliance.

### Surface & Background
- **Header Background** (`#f7f7f4`): Consistent with page background for seamless integration.
- **Card Surfaces**: Subtle variations of the primary background for layered content.
- **Transparent Overlays**: `rgba(0, 0, 0, 0)` used for hover states and transitions.

### Typography Colors
- **Primary Text** (`#262520`): Main content and headings — warm dark with excellent readability.
- **Secondary Text**: Lighter variations for supporting content and metadata.
- **Inverted Text** (`#f7f7f4`): White text for dark backgrounds and primary buttons.

### System Colors
- **Border Subtle**: Light variations for minimal visual separation.
- **Shadow Base**: Transparent blacks for depth without harshness.
- **Hover States**: Subtle opacity changes and color shifts for interactivity.

## 3. Typography Rules

### Font Families
- **CursorGothic**: Primary UI font — custom geometric sans-serif for headings, navigation, and interface elements
- **Berkeley Mono**: Code display font — monospace typeface optimized for programming contexts
- **JJ Annon**: Editorial font — serif typeface for longer-form content and marketing materials
- **System Fallback**: `system-ui, "Helvetica Neue", Helvetica, Arial, sans-serif`

### Font Sizes & Hierarchy
- **Body Text**: `16px` / `24px` line-height — comfortable reading size with generous leading
- **Small Text**: `14px` / `21px` line-height — used for navigation, captions, and secondary content
- **Button Text**: `14px` / `14px` line-height — compact for UI elements
- **Large Headlines**: Scaled proportionally using the type system

### Font Weights
- **Regular**: `400` — primary weight for body text and most UI elements
- **Medium**: Used selectively for emphasis and hierarchy
- **Bold**: Reserved for strong emphasis and primary headings

### Letter Spacing
- **Default**: `normal` — no additional tracking for most text
- **UI Elements**: `0.14px` — subtle positive tracking for small interface text
- **Headlines**: Varies by size, generally tighter for larger text

### Line Height Rules
- **Body Text**: `1.5` (24px/16px) — generous leading for comfortable reading
- **UI Text**: `1.5` (21px/14px) — consistent ratio across interface elements
- **Compact Elements**: `1.0` (14px/14px) — tight leading for buttons and labels
- **Headlines**: `1.1-1.3` — tighter leading for display text

## 4. Component Stylings

### Buttons
- **Primary Button**: 
  - Background: `#262520`
  - Text: `#f7f7f4`
  - Border-radius: `33554400px` (pill shape)
  - Padding: `5.6px 10.5px 5.88px` (small), scaled proportionally for larger sizes
  - Font: CursorGothic, 14px, weight 400
  - Hover: Subtle opacity or color shift

- **Secondary Button**:
  - Background: Transparent
  - Border: `1px solid #262520`
  - Text: `#262520`
  - Same border-radius and padding as primary

### Navigation
- **Nav Links**:
  - Font: CursorGothic, 14px, weight 400
  - Color: `#262520`
  - Padding: `5.6px 15px`
  - Line-height: `21px`
  - Letter-spacing: `0.14px`

- **Sub-navigation**:
  - Padding: `4.66667px 0px`
  - Same typography as main nav
  - Subtle hover states

### Header
- **Fixed Header**:
  - Background: `#f7f7f4`
  - Position: Fixed top
  - Z-index: 50
  - Padding: `0px 20px`
  - Height: `52px` (inferred from body padding-top)

### Cards & Containers
- **Content Cards**:
  - Background: Variations of `#f7f7f4`
  - Subtle shadows for depth
  - Rounded corners consistent with button styling
  - Generous internal padding

### Form Elements
- **Input Fields**:
  - Border-radius: `3px` (subtle rounding)
  - Focus states with outline treatment
  - Consistent with overall geometric aesthetic

## 5. Layout Principles

### Grid System
- **Container Padding**: `20px` horizontal (`px-g2` class) — consistent edge spacing across all screen sizes
- **Content Width**: Centered layouts with maximum widths for optimal reading
- **Responsive Breakpoints**: Standard breakpoint system for mobile, tablet, and desktop

### Spacing Scale
- **Base Unit**: Appears to use a systematic spacing scale
- **Vertical Rhythm**: `24px` base line-height creates consistent vertical spacing
- **Component Spacing**: 
  - Small: `4.67px` (sub-nav padding)
  - Medium: `5.6px` (button padding)
  - Large: `15px` (nav link horizontal padding)
  - Extra Large: `20px` (container padding)

### Alignment & Positioning
- **Header Layout**:
  - Logo: Left-aligned with slight offset (`left-[-2px]`, `top-[0.2rem]`)
  - Navigation: Absolutely centered (`absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2`)
  - Actions: Right-aligned (implied)

- **Content Alignment**:
  - Left-aligned text for readability
  - Centered layouts for marketing content
  - Consistent margins and padding throughout

### Z-Index Hierarchy
- **Header**: `z-50` — ensures header stays above all content
- **Overlays**: Higher z-index values for modals and dropdowns
- **Content**: Base layer (z-index: auto)

### Responsive Behavior Preview
- **Mobile-First**: Design scales down gracefully
- **Container Adaptation**: Padding and spacing adjust for smaller screens
- **Navigation**: Likely collapses to hamburger menu on mobile
- **Typography**: Font sizes may scale down for mobile readability

## 6. Depth & Elevation

### Shadow System
- **Subtle Depth**: `box-shadow: none` is used extensively, indicating a flat design approach with depth created through color and spacing rather than shadows
- **Layered Elements**: Header uses fixed positioning and z-index for elevation
- **Interactive Feedback**: Depth changes likely achieved through opacity and color shifts rather than shadow manipulation

### Visual Hierarchy
- **Color Contrast**: Primary depth indicator through `#262520` text on `#f7f7f4` background
- **Typography Scale**: Size and weight variations create hierarchy without relying on shadows
- **Spacing Relationships**: Generous whitespace creates natural separation and depth

### Elevation Levels
1. **Base Layer**: Page background (`#f7f7f4`)
2. **Content Layer**: Text and components on base background
3. **Interactive Layer**: Buttons and links with hover states
4. **Navigation Layer**: Fixed header with `z-50`
5. **Overlay Layer**: Modals and dropdowns (higher z-index)

### Transition & Animation
- **Hover States**: Subtle transitions on interactive elements
- **Focus States**: Accessibility-compliant focus indicators
- **Smooth Interactions**: Implied smooth transitions for state changes

## 7. Do's and Don'ts

### Do's
- **Use the warm off-white background** (`#f7f7f4`) — maintains the premium, eye-friendly aesthetic
- **Stick to CursorGothic for UI elements** — ensures brand consistency and optimal readability
- **Maintain generous whitespace** — follows the clean, uncluttered design philosophy
- **Use pill-shaped buttons** (`border-radius: 33554400px`) — signature design element
- **Keep shadows minimal** — aligns with the flat, modern aesthetic
- **Use consistent 20px container padding** — maintains layout harmony
- **Apply subtle letter-spacing** (`0.14px`) to small UI text for improved readability
- **Maintain the warm neutral color palette** — keeps the sophisticated, developer-focused feel

### Don'ts
- **Don't use pure white backgrounds** — breaks the warm, premium aesthetic
- **Don't add heavy drop shadows** — conflicts with the clean, flat design approach
- **Don't use bright, saturated accent colors** — disrupts the refined neutral palette
- **Don't use system fonts for primary elements** — dilutes brand identity
- **Don't create sharp, angular corners on buttons** — pill shapes are a key brand element
- **Don't use tight line-heights on body text** — reduces readability and comfort
- **Don't center-align body text** — left alignment is better for scanning and reading
- **Don't use pure black text** — the warm `#262520` is more comfortable and on-brand

### Typography Don'ts
- **Don't mix too many font weights** — the system relies on size and spacing for hierarchy
- **Don't use decorative fonts** — maintains the technical, professional aesthetic
- **Don't set text smaller than 14px** — ensures accessibility and readability
- **Don't use all caps extensively** — reserved for specific UI elements only

### Layout Don'ts
- **Don't create cramped layouts** — generous spacing is core to the design
- **Don't break the grid system** — consistent alignment is crucial
- **Don't use inconsistent padding** — stick to the established spacing scale
- **Don't overcomplicate navigation** — clean, simple structure is key

## 8. Responsive Behavior

### Breakpoint Strategy
- **Mobile First**: Design scales up from mobile base
- **Container Adaptation**: `px-g2` (20px) padding maintained across all breakpoints
- **Flexible Navigation**: Center-positioned nav likely adapts to hamburger menu on mobile
- **Typography Scaling**: Font sizes and line-heights adjust proportionally

### Mobile Adaptations (< 768px)
- **Header Height**: Maintains fixed positioning with adjusted height
- **Navigation**: Collapses to mobile-friendly menu system
- **Button Sizing**: Maintains pill shape with touch-friendly dimensions
- **Typography**: 16px body text ensures readability without zoom
- **Spacing**: Proportional reduction while maintaining visual hierarchy

### Tablet Adaptations (768px - 1024px)
- **Navigation**: Partial collapse or simplified layout
- **Content Width**: Optimized for tablet reading experience
- **Touch Targets**: Maintained button sizing for touch interaction
- **Grid Adaptation**: Content reflows for medium-width screens

### Desktop Adaptations (> 1024px)
- **Full Navigation**: Complete horizontal navigation display
- **Maximum Content Width**: Prevents overly wide text lines
- **Hover States**: Full interactive feedback for mouse users
- **Generous Spacing**: Takes advantage of available screen real estate

### Key Responsive Elements
- **Header**: `fixed top-0 left-0 z-50 w-full` — maintains position across all screens
- **Container**: `px-g2` provides consistent edge spacing
- **Typography**: Scalable font system maintains readability
- **Buttons**: Pill shape and padding scale appropriately
- **Images**: Responsive image loading with multiple size variants

### Performance Considerations
- **Image Optimization**: Multiple srcset variants for different screen densities
- **Font Loading**: Preloaded custom fonts with system fallbacks
- **Critical CSS**: Above-the-fold styling prioritized
- **Progressive Enhancement**: Core functionality works without JavaScript

## 9. Agent Prompt Guide

When implementing Cursor's design system, use this prompt template:

```
You are implementing the Cursor design system. Follow these specifications exactly:

COLORS:
- Primary background: #f7f7f4 (warm off-white)
- Primary text: #262520 (warm dark brown-black)
- Button backgrounds: #262520 with #f7f7f4 text
- Maintain warm undertones throughout

TYPOGRAPHY:
- Primary: CursorGothic with fallback "system-ui, 'Helvetica Neue', Helvetica, Arial, sans-serif"
- Body text: 16px/24px (1.5 line-height)
- UI text: 14px/21px with 0.14px letter-spacing
- Font weight: 400 (regular) for most elements

COMPONENTS:
- Buttons: Pill-shaped (border-radius: 33554400px), padding: 5.6px 10.5px
- Navigation: 14px CursorGothic, padding: 5.6px 15px
- Header: Fixed position, z-index: 50, background: #f7f7f4
- Containers: 20px horizontal padding (px-g2)

LAYOUT:
- Generous whitespace and clean alignment
- Mobile-first responsive approach
- Centered navigation with absolute positioning
- Consistent spacing scale based on typography

AESTHETIC:
- Minimal shadows (prefer flat design)
- Warm neutral palette only
- Clean, geometric shapes
- Premium, developer-focused feel
- Subtle hover states and transitions

Remember: This is a premium developer tool aesthetic — clean, warm, and technically sophisticated. Avoid bright colors, heavy shadows, or overly decorative elements.
```

### Implementation Checklist:
- [ ] Applied warm off-white background (#f7f7f4)
- [ ] Used CursorGothic font family with proper fallbacks
- [ ] Implemented pill-shaped buttons with correct padding
- [ ] Set up fixed header with proper z-index
- [ ] Applied consistent 20px container padding
- [ ] Used warm dark text color (#262520)
- [ ] Maintained generous whitespace throughout
- [ ] Implemented responsive behavior
- [ ] Added subtle hover states
- [ ] Ensured accessibility compliance

### Common Mistakes to Avoid:
- Using pure white instead of #f7f7f4
- Adding heavy drop shadows
- Using bright accent colors
- Making buttons too angular
- Cramping the layout with insufficient spacing
- Using pure black text instead of #262520
- Breaking the pill-shaped button paradigm
- Overcomplicating the navigation structure