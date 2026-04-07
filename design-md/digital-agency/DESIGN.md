# Design System of Digital Agency Japan (DADS)

## 1. Visual Theme & Atmosphere

The Digital Agency Design System (DADS) embodies the essence of modern Japanese governmental digital transformation — clean, accessible, and purposefully understated. Built on a foundation of trust and clarity, the design language prioritizes function over form while maintaining a distinctly Japanese sensibility through its careful attention to spacing, typography, and subtle visual hierarchy.

The interface breathes with generous whitespace and employs a restrained color palette dominated by sophisticated grays and a singular, authoritative blue accent. Unlike flashy tech startups, DADS communicates governmental reliability through its conservative yet modern approach — every element serves a clear purpose, and visual noise is eliminated in favor of content clarity.

The typography system centers around Noto Sans and Noto Sans JP, Google's comprehensive font family designed specifically for multilingual harmony. This choice reflects the system's commitment to accessibility and international compatibility while maintaining excellent Japanese character rendering. The careful balance between Latin and Japanese typography creates a seamless reading experience that feels native to both languages.

**Key Characteristics:**
- Governmental authority expressed through restrained, professional aesthetics
- Noto Sans family ensuring perfect Japanese-Latin typography harmony
- Minimal color palette with strategic blue accent (`#00118f`) for interactive elements
- Generous spacing system promoting content clarity and accessibility
- Mobile-first responsive approach with backdrop-blur navigation
- Focus on accessibility with proper contrast ratios and semantic structure

## 2. Color Palette & Roles

### Primary
- **Authority Blue** (`#00118f`): The primary interactive color used for links, focus states, and primary actions. A deep, trustworthy blue that conveys governmental authority while maintaining excellent accessibility contrast.
- **Text Primary** (`#333333`): The main text color — a warm dark gray that's easier on the eyes than pure black while maintaining excellent readability.

### Surface & Background
- **Pure White** (`#ffffff`): Primary background color for content areas and cards
- **Backdrop Blur** (`rgba(255, 255, 255, 0.85)`): Semi-transparent white used for the mobile header with backdrop blur effect, creating depth while maintaining readability

### Interactive States
- **Link Blue** (`#00118f`): Used for all text links and interactive elements
- **Focus Ring**: Blue-based focus indicators for keyboard navigation accessibility

### Neutrals & Text
- **Primary Text** (`#333333`): Main body text and headings
- **Secondary Text**: Inherited from primary with reduced opacity for hierarchy

## 3. Typography Rules

### Font Family
```css
font-family: "Noto Sans", "Noto Sans JP", "Noto Sans-147b475a14d9aa26", "Noto Sans JP-b6e5b2158d9e0a83", -apple-system, "system-ui", sans-serif
```

### Typography Scale
- **H1 (Mobile Header Logo)**: 20px, weight 700, line-height 30px (1.5), letter-spacing 0.4px
- **H2 (Section Headers)**: 24px, weight 700, line-height 40.8px (1.7), letter-spacing 0.32px
- **Body Text**: 17px, weight 400, line-height 28.9px (1.7), letter-spacing 0.34px
- **Navigation Text**: 16px, weight 400, line-height 27.2px (1.7), letter-spacing 0.32px
- **Menu Items**: 16px, weight 400, line-height 20.8px (1.3), letter-spacing normal
- **Button Text**: 16px, weight 400, line-height 16px (1.0), letter-spacing 0.32px

### Typography Principles
- Generous line-heights (1.5-1.7) for improved readability
- Subtle letter-spacing for better character definition
- Weight 700 for headings, 400 for body text
- Consistent 16-17px base sizes for optimal mobile readability

## 4. Component Stylings

### Buttons
```css
/* Primary Button (Skip Nav) */
.dads-skip-nav__link {
  font-weight: 700;
  color: #00118f;
  border-radius: 6px;
  padding: 0px;
  margin: -1px;
}

/* Icon Buttons (Search, Menu) */
.dads-mobile-header__search-button,
.dads-hamburger-menu-button {
  font-size: 16px;
  border-radius: 6px;
  padding: 4px 8px 6px;
  background: transparent;
  color: #333333;
}
```

### Navigation
```css
/* Mobile Header */
.dads-mobile-header {
  background-color: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur();
}

/* Menu Items */
.dads-menu-list__item {
  padding: 10px 16px;
  font-size: 16px;
  line-height: 20.8px;
  color: #333333;
}
```

### Cards & Containers
- Clean white backgrounds with subtle shadows
- Consistent padding using 8px grid system
- Rounded corners at 6px for interactive elements

## 5. Layout Principles

### Spacing System
- **Base Unit**: 4px grid system
- **Common Spacings**: 4px, 8px, 10px, 16px, 19.92px (calculated margin)
- **Button Padding**: 4px 8px 6px (asymmetric for visual balance)
- **Menu Item Padding**: 10px 16px

### Grid System
- Mobile-first responsive approach
- Flexible container widths
- Content-driven breakpoints

### Container Principles
- Generous margins for content breathing room
- Consistent horizontal padding across components
- Vertical rhythm maintained through calculated line-heights

## 6. Depth & Elevation

### Shadow System
- **No Visible Shadows**: The system relies on subtle borders and background changes rather than drop shadows
- **Backdrop Blur**: `rgba(255, 255, 255, 0.85)` with blur for floating navigation
- **Layering**: Z-index based layering for navigation overlays

### Visual Hierarchy
- Typography weight and size for primary hierarchy
- Color contrast for secondary emphasis
- Spacing for content separation

## 7. Do's and Don'ts

### Do's
- ✅ Use the Noto Sans family for consistent Japanese-Latin typography
- ✅ Maintain generous line-heights (1.5-1.7) for readability
- ✅ Apply the 4px grid system for consistent spacing
- ✅ Use the authority blue (`#00118f`) sparingly for maximum impact
- ✅ Ensure proper contrast ratios for accessibility
- ✅ Implement proper focus states for keyboard navigation

### Don'ts
- ❌ Don't use colors outside the defined palette
- ❌ Don't reduce line-heights below 1.3 for body text
- ❌ Don't use decorative fonts or excessive font weights
- ❌ Don't create visual noise with unnecessary shadows or effects
- ❌ Don't ignore mobile-first responsive principles
- ❌ Don't compromise accessibility for visual appeal

## 8. Responsive Behavior

### Mobile-First Approach
- Base styles optimized for mobile devices
- Progressive enhancement for larger screens
- Touch-friendly interactive elements (minimum 44px touch targets)

### Navigation Strategy
- Hamburger menu for mobile navigation
- Backdrop blur header for visual hierarchy
- Drawer-style navigation panel

### Typography Scaling
- Consistent font sizes across breakpoints
- Maintained line-heights for readability
- Responsive letter-spacing adjustments

## 9. Agent Prompt Guide

### Quick Reference for AI Agents

**Color Palette:**
- Primary Blue: `#00118f`
- Text: `#333333`
- Background: `#ffffff`
- Backdrop: `rgba(255, 255, 255, 0.85)`

**Typography:**
- Font: Noto Sans + Noto Sans JP
- Body: 17px/28.9px, weight 400
- Headings: 20-24px, weight 700
- Buttons: 16px, weight 400

**Spacing:**
- Grid: 4px base unit
- Padding: 4px, 8px, 10px, 16px
- Border-radius: 6px for interactive elements

### Recommended Prompts

**For Component Creation:**
```
"Create a [component] using DADS principles: Noto Sans typography, #00118f for interactive elements, #333333 for text, 6px border-radius, and 4px grid spacing."
```

**For Layout Design:**
```
"Design a mobile-first layout following DADS guidelines: generous whitespace, 17px body text with 1.7 line-height, and minimal color palette with strategic blue accents."
```

**For Accessibility:**
```
"Ensure DADS accessibility standards: proper contrast ratios, keyboard navigation with blue focus states, semantic HTML structure, and touch-friendly interactive elements."
```