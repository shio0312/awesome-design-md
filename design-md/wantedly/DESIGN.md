# DESIGN.md - Wantedly UI Components Design System

## 1. Visual Theme & Atmosphere

### Design Philosophy
Wantedly's design system embodies **"Professional Approachability"** - a balance between business credibility and human warmth that reflects Japan's unique approach to professional networking.

### Core Attributes
- **Clean & Modern**: Minimalist interfaces with purposeful white space
- **Human-Centered**: Emphasis on profile imagery and personal connections
- **Trustworthy**: Professional aesthetics that inspire confidence
- **Warm & Inviting**: Soft colors and rounded elements that feel approachable
- **Story-Driven**: Design that supports narrative and mission-based content

### Visual Characteristics
- Generous use of white space for breathing room
- Soft shadows creating subtle depth
- Rounded corners throughout (never sharp)
- Photography-forward layouts emphasizing people
- Gradient accents for energy and modernity

---

## 2. Color Palette & Roles

### Primary Colors

| Role | Color Name | Hex Code | Usage |
|------|------------|----------|-------|
| Primary | Wantedly Cyan | `#00B4CC` | Primary actions, links, brand elements |
| Primary Dark | Deep Teal | `#0099AD` | Hover states, emphasis |
| Primary Light | Light Cyan | `#E5F7FA` | Backgrounds, highlights |

### Secondary Colors

| Role | Color Name | Hex Code | Usage |
|------|------------|----------|-------|
| Secondary | Ocean Blue | `#0066CC` | Secondary actions, information |
| Accent | Gradient Start | `#00C6D4` | Gradient effects |
| Accent | Gradient End | `#0080CC` | Gradient effects |

### Neutral Colors

| Role | Color Name | Hex Code | Usage |
|------|------------|----------|-------|
| Text Primary | Charcoal | `#1A1A2E` | Headlines, body text |
| Text Secondary | Dark Gray | `#4A4A68` | Secondary text, captions |
| Text Tertiary | Medium Gray | `#8E8EA9` | Placeholder, disabled text |
| Border | Light Gray | `#D1D1E0` | Dividers, borders |
| Background | Off White | `#F5F5FA` | Page backgrounds |
| Surface | Pure White | `#FFFFFF` | Cards, modals |
| Dark Surface | Navy | `#1A1A2E` | Dark sections, footer |

### Semantic Colors

| Role | Color Name | Hex Code | Usage |
|------|------------|----------|-------|
| Success | Green | `#00C853` | Success states, confirmations |
| Warning | Amber | `#FFB300` | Warnings, cautions |
| Error | Red | `#E53935` | Errors, destructive actions |
| Info | Blue | `#2196F3` | Information, tips |

### Color Application Rules
```
Background Hierarchy:
- Level 0 (Base): #FFFFFF
- Level 1 (Subtle): #F5F5FA  
- Level 2 (Emphasis): #E5F7FA
- Level 3 (Dark): #1A1A2E
```

---

## 3. Typography Rules

### Font Family
```css
--font-primary: "Noto Sans JP", "Hiragino Sans", "Hiragino Kaku Gothic ProN", sans-serif;
--font-fallback: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
```

### Type Scale

| Level | Name | Size | Weight | Line Height | Letter Spacing | Usage |
|-------|------|------|--------|-------------|----------------|-------|
| H1 | Display | 32px / 2rem | 700 (Bold) | 1.4 (44.8px) | -0.02em | Page titles |
| H2 | Heading L | 24px / 1.5rem | 700 (Bold) | 1.4 (33.6px) | -0.01em | Section headers |
| H3 | Heading M | 20px / 1.25rem | 600 (SemiBold) | 1.4 (28px) | -0.01em | Card titles |
| H4 | Heading S | 18px / 1.125rem | 600 (SemiBold) | 1.5 (27px) | 0 | Subsections |
| Body L | Body Large | 16px / 1rem | 400 (Regular) | 1.7 (27.2px) | 0.01em | Long-form content |
| Body M | Body Medium | 14px / 0.875rem | 400 (Regular) | 1.6 (22.4px) | 0.01em | Default body text |
| Body S | Body Small | 13px / 0.8125rem | 400 (Regular) | 1.6 (20.8px) | 0.01em | Secondary info |
| Caption | Caption | 12px / 0.75rem | 400 (Regular) | 1.5 (18px) | 0.02em | Labels, timestamps |
| Micro | Micro | 11px / 0.6875rem | 500 (Medium) | 1.4 (15.4px) | 0.03em | Badges, tags |

### Font Weight Scale
```css
--font-weight-regular: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

### Typography Best Practices
- Japanese text requires 1.6-1.7 line height for readability
- Mix Japanese and English seamlessly with consistent baseline
- Use medium weight (500) for UI labels
- Bold (700) reserved for headlines and emphasis only

---

## 4. Component Stylings

### Button Component

#### Size Variants

| Size | Height | Padding (H) | Font Size | Border Radius | Icon Size |
|------|--------|-------------|-----------|---------------|-----------|
| XL | 56px | 32px | 16px | 12px | 24px |
| L | 48px | 24px | 15px | 10px | 20px |
| M | 44px | 20px | 14px | 8px | 18px |
| S | 40px | 16px | 13px | 6px | 16px |

#### Style Variants

**Colored (Primary - Elevation 4)**
```css
.button-colored {
  background: linear-gradient(135deg, #00C6D4 0%, #00B4CC 100%);
  color: #FFFFFF;
  box-shadow: 0 4px 12px rgba(0, 180, 204, 0.3);
  border: none;
}
.button-colored:hover {
  background: linear-gradient(135deg, #00B4CC 0%, #0099AD 100%);
  box-shadow: 0 6px 16px rgba(0, 180, 204, 0.4);
  transform: translateY(-1px);
}
.button-colored:pressed {
  background: #0099AD;
  box-shadow: 0 2px 8px rgba(0, 180, 204, 0.3);
  transform: translateY(0);
}
.button-colored:disabled {
  background: #D1D1E0;
  color: #8E8EA9;
  box-shadow: none;
}
```

**Base (Elevation 0 - Higher Priority)**
```css
.button-base-high {
  background: #FFFFFF;
  color: #00B4CC;
  border: 2px solid #00B4CC;
}
.button-base-high:hover {
  background: #E5F7FA;
  border-color: #0099AD;
  color: #0099AD;
}
```

**Base (Elevation 0 - Lower Priority)**
```css
.button-base-low {
  background: #FFFFFF;
  color: #4A4A68;
  border: 1px solid #D1D1E0;
}
.button-base-low:hover {
  background: #F5F5FA;
  border-color: #8E8EA9;
}
```

**Clear (Text Button)**
```css
.button-clear {
  background: transparent;
  color: #00B4CC;
  border: none;
  padding-left: 8px;
  padding-right: 8px;
}
.button-clear:hover {
  color: #0099AD;
  background: rgba(0, 180, 204, 0.08);
}
```

#### Button States

| State | Opacity | Transform | Additional |
|-------|---------|-----------|------------|
| Normal | 100% | none | - |
| Hover | 100% | translateY(-1px) | Enhanced shadow |
| Pressed | 100% | translateY(0) | Reduced shadow |
| Focused | 100% | none | 3px cyan outline, 2px offset |
| Disabled | 100% | none | Grayed colors |
| Visited | 100% | none | Subtle color shift |

### Input Component

#### Size Variants

| Size | Height | Padding | Font Size | Border Radius |
|------|--------|---------|-----------|---------------|
| L | 48px | 16px | 15px | 8px |
| M | 44px | 14px | 14px | 6px |
| S | 40px | 12px | 13px | 6px |

#### Input Styles
```css
.input-default {
  background: #FFFFFF;
  border: 1px solid #D1D1E0;
  color: #1A1A2E;
}
.input-default::placeholder {
  color: #8E8EA9;
}
.input-default:hover {
  border-color: #8E8EA9;
}
.input-default:focus {
  border-color: #00B4CC;
  box-shadow: 0 0 0 3px rgba(0, 180, 204, 0.15);
  outline: none;
}
.input-error {
  border-color: #E53935;
  box-shadow: 0 0 0 3px rgba(229, 57, 53, 0.1);
}
.input-disabled {
  background: #F5F5FA;
  border-color: #D1D1E0;
  color: #8E8EA9;
  cursor: not-allowed;
}
```

### Card Component

#### Card Variants

**Standard Card**
```css
.card {
  background: #FFFFFF;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(26, 26, 46, 0.08);
  padding: 24px;
}
.card:hover {
  box-shadow: 0 4px 16px rgba(26, 26, 46, 0.12);
  transform: translateY(-2px);
  transition: all 0.2s ease;
}
```

**Profile Card (SNS-style)**
```css
.card-profile {
  background: #FFFFFF;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(26, 26, 46, 0.1);
  padding: 0;
  overflow: hidden;
}
.card-profile__cover {
  height: 120px;
  background: linear-gradient(135deg, #00C6D4 0%, #0080CC 100%);
}
.card-profile__avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid #FFFFFF;
  margin-top: -40px;
}
```

**Job Card**
```css
.card-job {
  background: #FFFFFF;
  border-radius: 12px;
  border: 1px solid #D1D1E0;
  padding: 20px;
}
.card-job:hover {
  border-color: #00B4CC;
  box-shadow: 0 4px 12px rgba(0, 180, 204, 0.15);
}
```

### Avatar Component

| Size | Dimensions | Border Radius | Border |
|------|------------|---------------|--------|
| XS | 24px | 50% | none |
| S | 32px | 50% | none |
| M | 40px | 50% | none |
| L | 56px | 50% | 2px white |
| XL | 80px | 50% | 3px white |
| XXL | 120px | 50% | 4px white |

### Table Component

```css
.table {
  width: 100%;
  border-collapse: collapse;
}
.table th {
  background: #F5F5FA;
  color: #4A4A68;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid #D1D1E0;
}
.table td {
  padding: 16px;
  border-bottom: 1px solid #E8E8F0;
  color: #1A1A2E;
  font-size: 14px;
}
.table tr:hover td {
  background: #F5F5FA;
}
```

---

## 5. Layout Principles

### Spacing Scale (8px Base Unit)

| Token | Value | Usage |
|-------|-------|-------|
| space-0 | 0px | No spacing |
| space-1 | 4px | Tight inline spacing |
| space-2 | 8px | Icon gaps, tight padding |
| space-3 | 12px | Small component padding |
| space-4 | 16px | Default component padding |
| space-5 | 20px | Medium spacing |
| space-6 | 24px | Card padding, section gaps |
| space-7 | 32px | Large section spacing |
| space-8 | 40px | Section dividers |
| space-9 | 48px | Major section breaks |
| space-10 | 64px | Page section spacing |
| space-11 | 80px | Hero spacing |
| space-12 | 96px | Maximum spacing |

### Grid System

**Desktop (≥1200px)**
```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
}
```

**Tablet (768px - 1199px)**
```css
.container {
  padding: 0 20px;
}
.grid {
  grid-template-columns: repeat(8, 1fr);
  gap: 20px;
}
```

**Mobile (< 768px)**
```css
.container {
  padding: 0 16px;
}
.grid {
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
```

### Common Layout Patterns

**Feed Layout (SNS-style)**
```css
.feed-layout {
  display: grid;
  grid-template-columns: 240px 1fr 300px;
  gap: 24px;
  max-width: 1200px;
}
/* Left: Navigation sidebar */
/* Center: Main feed content */
/* Right: Suggestions/Ads sidebar */
```

**Profile Layout**
```css
.profile-layout {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 32px;
}
```

**Card Grid**
```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}
```

---

## 6. Depth & Elevation

### Elevation Scale

| Level | Name | Box Shadow | Usage |
|-------|------|------------|-------|
| 0 | Flat | none | Inline elements, flat buttons |
| 1 | Raised | `0 1px 3px rgba(26, 26, 46, 0.06)` | Subtle lift, borders |
| 2 | Card | `0 2px 8px rgba(26, 26, 46, 0.08)` | Cards, panels |
| 3 | Dropdown | `0 4px 16px rgba(26, 26, 46, 0.12)` | Dropdowns, popovers |
| 4 | Modal | `0 8px 32px rgba(26, 26, 46, 0.16)` | Modals, dialogs |
| 5 | Toast | `0 12px 48px rgba(26, 26, 46, 0.2)` | Toasts, floating elements |

### Elevation Application
```css
/* Interactive elevation change */
.card {
  box-shadow: var(--elevation-2);
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.card:hover {
  box-shadow: var(--elevation-3);
  transform: translateY(-2px);
}

/* Primary button with colored shadow */
.button-primary {
  box-shadow: 0 4px 12px rgba(0, 180, 204, 0.3);
}
.button-primary:hover {
  box-shadow: 0 6px 20px rgba(0, 180, 204, 0.4);
}
```

### Z-Index Scale

| Layer | Z-Index | Usage |
|-------|---------|-------|
| Base | 0 | Default content |
| Dropdown | 100 | Dropdowns, tooltips |
| Sticky | 200 | Sticky headers |
| Overlay | 300 | Overlay backgrounds |
| Modal | 400 | Modal dialogs |
| Toast | 500 | Toast notifications |
| Maximum | 999 | Critical overlays |

---

## 7. Do's and Don'ts

### ✅ Do's

**Color Usage**
- ✅ Use Wantedly Cyan for primary CTAs and links
- ✅ Apply gradients sparingly for hero sections and primary buttons
- ✅ Maintain sufficient contrast (WCAG AA minimum)
- ✅ Use semantic colors consistently (green=success, red=error)

**Typography**
- ✅ Use proper Japanese line height (1.6-1.7)
- ✅ Limit heading levels to 3-4 per page
- ✅ Use medium weight (500) for UI labels
- ✅ Ensure 14px minimum for body text

**Components**
- ✅ Provide clear hover/focus states for all interactive elements
- ✅ Use rounded corners consistently (6-12px range)
- ✅ Include loading states for async actions
- ✅ Show avatars/profile images to humanize the interface

**Layout**
- ✅ Use 8px grid for all spacing decisions
- ✅ Provide generous white space around content
- ✅ Group related items with consistent spacing
- ✅ Align elements to the grid

### ❌ Don'ts

**Color Usage**
- ❌ Don't use pure black (#000000) for text
- ❌ Don't combine multiple bright colors
- ❌ Don't use gradients for small UI elements
- ❌ Don't use cyan on cyan backgrounds

**Typography**
- ❌ Don't use more than 2 font weights per component
- ❌ Don't go below 11px for any text
- ❌ Don't use all-caps for Japanese text
- ❌ Don't center-align long paragraphs

**Components**
- ❌ Don't use sharp corners (0px radius)
- ❌ Don't remove focus indicators
- ❌ Don't use more than 2 button styles per section
- ❌ Don't disable buttons without explanation

**Layout**
- ❌ Don't use arbitrary spacing values
- ❌ Don't crowd elements together
- ❌ Don't exceed 1200px content width
- ❌ Don't ignore mobile breakpoints

---

## 8. Responsive Behavior

### Breakpoints

| Name | Range | Columns | Gutter | Margin |
|------|-------|---------|--------|--------|
| Mobile S | 0 - 374px | 4 | 16px | 16px |
| Mobile L | 375 - 767px | 4 | 16px | 16px |
| Tablet | 768 - 1023px | 8 | 20px | 20px |
| Desktop | 1024 - 1439px | 12 | 24px | 24px |
| Desktop L | 1440px+ | 12 | 24px | auto (centered) |

### Component Responsive Rules

**Navigation**
```
Desktop: Full horizontal nav with search
Tablet: Condensed nav, icon-based
Mobile: Hamburger menu, bottom nav bar
```

**Cards**
```
Desktop: 3-4 columns grid
Tablet: 2 columns grid
Mobile: Single column, full width
```

**Typography Scaling**
```css
/* Mobile */
h1 { font-size: 24px; }
h2 { font-size: 20px; }
body { font-size: 14px; }

/* Desktop */
h1 { font-size: 32px; }
h2 { font-size: 24px; }
body { font-size: 16px; }
```

**Button Behavior**
```
Desktop: Inline buttons, standard sizes
Mobile: Full-width buttons, larger touch targets (min 44px)
```

**Feed Layout**
```
Desktop: 3-column (sidebar + feed + recommendations)
Tablet: 2-column (feed + sidebar)
Mobile: Single column (feed only, bottom nav)
```

### Touch Considerations
- Minimum touch target: 44px × 44px
- Adequate spacing between touch targets: 8px minimum
- Swipe gestures for card carousels on mobile
- Pull-to-refresh for feed content

---

## 9. Agent Prompt Guide

### For AI/LLM Implementation

When implementing Wantedly's design system, use these guidelines:

#### Component Generation Prompt Template
```
Generate a [component name] following Wantedly UI specifications:
- Use Wantedly Cyan (#00B4CC) as primary color
- Apply 8px spacing grid
- Include border-radius: [6-12px based on size]
- Add elevation-2 shadow for cards
- Ensure Japanese typography support with 1.6+ line-height
- Include hover/focus/disabled states
```

#### Color Selection Logic
```
IF primary action → #00B4CC (Wantedly Cyan)
IF secondary action → #FFFFFF with #00B4CC border
IF destructive action → #E53935 (Error Red)
IF disabled → #D1D1E0 background, #8E8EA9 text
IF success feedback → #00C853
IF warning feedback → #FFB300
```

#### Spacing Decision Tree
```
Inline elements gap → 8px
Component internal padding → 16-24px
Between components → 24px
Between sections → 48-64px
Page margins → 16px (mobile) / 24px (desktop)
```

#### Typography Selection
```
Page title → 32px, Bold (700), Charcoal
Section header → 24px, Bold (700), Charcoal
Card title → 18px, SemiBold (600), Charcoal
Body text → 14px, Regular (400), Dark Gray
Caption/meta → 12px, Regular (400), Medium Gray
Button label → 14px, Medium (500), inherit
```

#### Elevation Assignment
```
Static content → elevation-0
Cards/panels → elevation-2
Dropdowns/popovers → elevation-3
Modals/dialogs → elevation-4
Toasts/notifications → elevation-5
```

#### SNS-Specific Patterns
```
Profile display:
- Always include avatar (circular, with white border)
- Show name prominently (16-18px, SemiBold)
- Include role/company as secondary text
- Use cover image gradients when no image available

Feed items:
- Card-based layout with elevation-2
- Timestamp in caption style (12px, gray)
- Action buttons at bottom (like, comment, share)
- Hover state with elevation-3

Connection/Follow buttons:
- Primary style for "Follow" (not yet following)
- Secondary style for "Following" (already connected)
- Include icon + text combination
```

#### Accessibility Checklist
```
□ Color contrast ratio ≥ 4.5:1 for text
□ Focus indicators visible (3px cyan outline)
□ Touch targets ≥ 44px
□ Alt text for all images
□ Proper heading hierarchy
□ Keyboard navigation support
□ Screen reader labels for icons
```

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────┐
│  WANTEDLY DESIGN SYSTEM - QUICK REFERENCE               │
├─────────────────────────────────────────────────────────┤
│  PRIMARY: #00B4CC    DARK: #0099AD    LIGHT: #E5F7FA   │
│  TEXT: #1A1A2E       GRAY: #4A4A68    BORDER: #D1D1E0  │
├─────────────────────────────────────────────────────────┤
│  SPACING: 4 | 8 | 12 | 16 | 24 | 32 | 48 | 64 | 80     │
│  RADIUS:  6px (S) | 8px (M) | 12px (L) | 16px (XL)     │
├─────────────────────────────────────────────────────────┤
│  BUTTONS: XL=56px | L=48px | M=44px | S=40px           │
│  INPUTS:  L=48px  | M=44px | S=40px                    │
├─────────────────────────────────────────────────────────┤
│  FONT: Noto Sans JP, system-ui                          │
│  SIZES: 32 | 24 | 20 | 18 | 16 | 14 | 13 | 12 | 11     │
│  LINE-HEIGHT: 1.4 (headings) | 1.6-1.7 (body)          │
├─────────────────────────────────────────────────────────┤
│  BREAKPOINTS: 375 | 768 | 1024 | 1440                  │
│  MAX-WIDTH: 1200px                                      │
└─────────────────────────────────────────────────────────┘
```

---

*Last Updated: 2024*
*Version: 1.0*
*Design System: Wantedly UI Components*