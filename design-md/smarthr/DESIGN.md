# SmartHR Design System

## 1. Visual Theme & Atmosphere

SmartHR Design System embodies a distinctly Japanese approach to enterprise software design — clean, purposeful, and refreshingly human-centered. The interface feels like a well-organized workspace where efficiency meets warmth, avoiding the sterile coldness typical of corporate design systems.

The design philosophy centers on accessibility and clarity, with a sophisticated neutral palette anchored by a distinctive blue (`#0071c1`) that serves as both the primary brand color and the universal link color. Unlike many Western design systems that rely on high contrast and bold statements, SmartHR employs subtle gradations of grays and thoughtful spacing to create hierarchy and breathing room.

The typography system is built around SDSYuGothic, a custom variant of Yu Gothic that provides excellent Japanese and Latin character support. The system demonstrates remarkable restraint — font weights are used sparingly (400 for body, 700 for emphasis), and the generous line-height of 1.75 creates a reading experience that feels unhurried and accessible.

What sets SmartHR apart is its commitment to functional beauty. Every element serves a purpose, from the 12px border-radius that softens edges without being playful, to the carefully calibrated hover states that provide feedback without distraction. The design speaks to professionals who value substance over flash.

**Key Characteristics:**
- Clean, functional aesthetic prioritizing usability over visual drama
- Sophisticated neutral palette with warm undertones (`#23221f`, `#706d65`)
- SDSYuGothic typography system optimized for Japanese/Latin bilingual content
- Consistent 12px border-radius creating gentle, professional edges
- Generous spacing system based on multiples of 8px (24px, 48px sections)
- Accessibility-first approach with high contrast ratios and clear focus states
- Subtle hover animations using cubic-bezier easing for premium feel

## 2. Color Palette & Roles

### Primary
- **SmartHR Blue** (`#0071c1`): The core brand color used for all interactive elements, links, and primary CTAs. A professional blue that maintains accessibility across all backgrounds.
- **Text Black** (`#23221f`): Primary text color — a warm near-black that's easier on the eyes than pure black while maintaining excellent readability.
- **Pure White** (`#ffffff`): Clean background color for cards, headers, and primary surfaces.

### Secondary & Accent
- **SmartHR Blue Dark** (`#0065a9`): Darker variant used in icons and secondary brand moments, providing depth to the blue family.
- **Text Grey** (`#706d65`): Secondary text color for labels, captions, and less prominent information. Warm-toned to complement the overall palette.

### Surface & Background
- **Light Grey 1** (`var(--color-light-grey-1)`): Primary border color and subtle background tints
- **Light Grey 2** (`var(--color-light-grey-2)`): Hover background states and secondary surface color
- **Grey 1** (`var(--color-grey-1)`): Code block borders and structural elements

### Neutrals & System
- **Black** (`#000000`): Used sparingly for high-contrast elements and mobile menu buttons
- **Transparent**: Extensively used for clean layering and subtle state changes

## 3. Typography Rules

### Font Family
- **Primary**: `SDSYuGothic, "Yu Gothic", YuGothic, sans-serif`
- **Fallback**: System sans-serif stack ensuring consistent rendering across platforms

### Typography Hierarchy
- **Body Text**: 16px / 400 weight / 28px line-height (1.75)
- **Small Text**: 12px / 700 weight / 21px line-height
- **Micro Text**: 11.008px / 700 weight / 19.264px line-height
- **Navigation**: 16px / 700 weight / 16px line-height (1.0)
- **Interactive Elements**: 24px / 400 weight / normal line-height

### Key Typography Features
- **Generous Line Height**: 1.75 for body text creates excellent readability
- **Strategic Font Weights**: Only 400 and 700 used, creating clear hierarchy without complexity
- **Consistent Letter Spacing**: Normal spacing throughout, letting the font's natural metrics shine
- **Bilingual Optimization**: SDSYuGothic provides seamless Japanese/Latin character mixing

## 4. Component Stylings

### Buttons
```css
/* Primary Button (Gotcha Button Style) */
.primaryButton {
  background-color: #ffffff;
  color: #23221f;
  font-weight: 700;
  border-radius: 8px;
  font-size: 13.3333px;
  padding: [calculated from context];
  border: 1px solid var(--color-grey-1);
}

/* Icon Button */
.iconButton {
  background: transparent;
  color: #000000;
  font-size: 24px;
  padding: 0;
  border: none;
  cursor: pointer;
}

/* Link Button */
.linkButton {
  color: #0071c1;
  background: transparent;
  text-decoration: underline;
  font-weight: 400;
}
```

### Cards & Containers
```css
.boxLink {
  padding: 24px;
  border: 1px solid var(--color-light-grey-1);
  border-radius: 12px;
  background: #ffffff;
  transition: background-color 1.5s cubic-bezier(0, 0.7, 0, 1);
}

.boxLink:hover {
  background-color: var(--color-light-grey-2);
  border-color: var(--color-text-grey);
  transition: background-color 0.2s;
}
```

### Navigation
```css
.navigationLink {
  color: #23221f;
  font-weight: 700;
  font-size: 16px;
  line-height: 16px;
  padding: 10px;
  text-decoration: none;
}

.siteNameLink {
  color: #0071c1;
  padding: 6px 10px;
  font-weight: 400;
}
```

### Interactive States
- **Hover**: Subtle background color changes with 0.2s transition
- **Focus**: Blue focus rings using `#0071c1`
- **Active**: Maintained color consistency with primary palette
- **Disabled**: Reduced opacity maintaining color relationships

## 5. Layout Principles

### Spacing System
- **Base Unit**: 8px
- **Section Spacing**: 48px between major sections
- **Component Spacing**: 24px for card padding and component separation
- **Micro Spacing**: 8px, 16px for internal component spacing
- **Header Padding**: 30px 48px for generous breathing room

### Grid System
- **Container**: Fluid width with consistent horizontal padding
- **Flex Layouts**: Extensive use of flexbox for responsive arrangements
- **Gap System**: 4px, 8px gaps for tight layouts; larger gaps for section separation

### Content Width Strategy
- **Full Width**: Headers and navigation span full viewport
- **Content Width**: Centered content with responsive side margins
- **Component Width**: Cards and components use natural content width with padding

## 6. Depth & Elevation

### Shadow System
SmartHR uses a minimal shadow approach, preferring borders over drop shadows:

```css
/* Primary Elevation - Borders */
.elevated {
  border: 1px solid var(--color-light-grey-1);
}

/* Hover Elevation */
.elevated:hover {
  border-color: var(--color-text-grey);
}

/* Code Blocks */
.codeContainer {
  border: 1px solid var(--color-grey-1);
  background: var(--color-text-black);
}
```

### Layering Philosophy
- **Base Layer**: White backgrounds with subtle borders
- **Interactive Layer**: Hover states change border colors, not shadows
- **Overlay Layer**: Modal and dropdown content uses solid backgrounds
- **Focus Layer**: Blue outline rings for accessibility

## 7. Do's and Don'ts

### Do's
✅ **Use generous spacing** - 24px padding minimum for interactive elements
✅ **Maintain color consistency** - Stick to the defined blue (`#0071c1`) for all interactive elements
✅ **Employ subtle transitions** - Use cubic-bezier(0, 0.7, 0, 1) for smooth, professional animations
✅ **Prioritize accessibility** - High contrast ratios and clear focus states
✅ **Use 12px border-radius** consistently for cards and containers
✅ **Leverage the 1.75 line-height** for excellent readability

### Don'ts
❌ **Don't use drop shadows** - SmartHR prefers clean borders over elevation shadows
❌ **Don't mix font weights** - Stick to 400 and 700 only
❌ **Don't use pure black** - Always use the warm near-black (`#23221f`)
❌ **Don't ignore the spacing system** - Maintain 8px-based spacing consistency
❌ **Don't use bright colors** - The palette is intentionally subdued and professional
❌ **Don't rush transitions** - The 1.5s initial state creates anticipation

## 8. Responsive Behavior

### Breakpoint Strategy
- **Mobile First**: Base styles optimized for mobile viewing
- **Flexible Navigation**: Menu transforms to hamburger on smaller screens
- **Responsive Padding**: Header padding adjusts from 48px to smaller values
- **Flexible Typography**: Font sizes scale appropriately across devices

### Mobile Adaptations
```css
/* Mobile Navigation */
.mobileMenuButton {
  font-size: 24px;
  color: #000000;
  background: transparent;
}

/* Responsive Containers */
.wrapper {
  padding: 30px 48px; /* Desktop */
}

@media (max-width: 768px) {
  .wrapper {
    padding: 20px 24px; /* Mobile */
  }
}
```

## 9. Agent Prompt Guide

### Quick Reference for AI Agents

**Primary Colors**: Use `#0071c1` for all links and interactive elements, `#23221f` for text, `#ffffff` for backgrounds.

**Typography**: SDSYuGothic font family, 16px/28px for body text, 700 weight for emphasis only.

**Spacing**: 24px padding for cards, 48px between sections, 12px border-radius consistently.

**Components**: Clean borders over shadows, subtle hover states, professional blue for all CTAs.

### Recommended Prompts

**For Buttons**: "Create a button using SmartHR blue (#0071c1) with 12px border-radius, 700 font-weight, and subtle hover transition"

**For Cards**: "Design a card with 24px padding, 1px light grey border, 12px border-radius, and gentle hover state changing background to light grey"

**For Typography**: "Use SDSYuGothic font with 1.75 line-height for body text, warm near-black (#23221f) color, and 700 weight only for emphasis"

**For Layout**: "Create sections with 48px vertical spacing, 24px component padding, and clean borders instead of shadows"

**For Interactions**: "Apply SmartHR's signature cubic-bezier(0, 0.7, 0, 1) transition with 1.5s duration for initial states, 0.2s for hover responses"