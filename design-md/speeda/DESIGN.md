# DESIGN.md

# SPEEDA Design System "FALCON" v3.0

> A comprehensive design system for SPEEDA — the B2B economic intelligence and corporate data analysis platform. Built for precision, trust, and global scalability.

---

## 1. Visual Theme & Atmosphere

### Design Philosophy

FALCON embodies the essence of professional data intelligence: **precision**, **trust**, and **clarity**. The system draws inspiration from the analytical nature of financial professionals who rely on SPEEDA for critical business decisions.

### Core Visual Principles

| Principle | Description |
|-----------|-------------|
| **Dark-Mode Foundation** | A sophisticated dark interface reduces eye strain during extended analysis sessions and emphasizes data visualization |
| **Geometric Precision** | Clean, geometric shapes convey accuracy and systematic thinking |
| **Noise Texture Accents** | Subtle noise textures add depth without compromising readability |
| **High Contrast Data** | Critical information stands out against the dark canvas |

### Atmosphere Keywords

```
Professional • Authoritative • Data-Driven • Global • Trustworthy • Precise
```

### Visual Hierarchy

1. **Primary Focus**: Data visualizations and key metrics
2. **Secondary Focus**: Navigation and action elements
3. **Tertiary Focus**: Supporting information and metadata

---

## 2. Color Palette & Roles

### 2.1 Primitive Color System

#### Neutral Scale

| Token | Hex | Usage |
|-------|-----|-------|
| `neutral-950` | `#1a1a1a` | Primary background (dark mode) |
| `neutral-800` | `#333333` | Secondary background, cards |
| `neutral-700` | `#555555` | Tertiary surfaces |
| `neutral-500` | `#888888` | Disabled text, placeholders |
| `neutral-400` | `#aaaaaa` | Secondary text |
| `neutral-300` | `#cccccc` | Borders, dividers |
| `neutral-100` | `#eeeeee` | Light borders |
| `neutral-50` | `#f5f5f5` | Light mode background |
| `neutral-0` | `#ffffff` | Primary text (on dark), light surfaces |

#### Brand Red

| Token | Hex | Usage |
|-------|-----|-------|
| `red-600` | `#e53935` | Primary brand, critical actions |
| `red-500` | `#ef5350` | Brand hover states |
| `red-400` | `#ff7961` | Brand active states |
| `red-100` | `#ffcdd2` | Error backgrounds |

#### Blue

| Token | Hex | Usage |
|-------|-----|-------|
| `blue-600` | `#1a5aff` | Primary interactive |
| `blue-500` | `#3d75ff` | Interactive hover |
| `blue-400` | `#6695ff` | Interactive active |
| `blue-300` | `#99b5ff` | Selected states |
| `blue-100` | `#ccdaff` | Focus rings |
| `blue-50` | `#e6edff` | Subtle highlights |

#### Teal

| Token | Hex | Usage |
|-------|-----|-------|
| `teal-700` | `#00796b` | Data emphasis (dark) |
| `teal-600` | `#009688` | Data emphasis (primary) |
| `teal-400` | `#4db6ac` | Data emphasis (light) |
| `teal-100` | `#b2dfdb` | Data backgrounds |

#### Yellow / Amber

| Token | Hex | Usage |
|-------|-----|-------|
| `amber-600` | `#f9a825` | Warning (dark) |
| `amber-500` | `#fbc02d` | Warning (primary) |
| `amber-400` | `#fdd835` | Warning (light) |

#### Sky

| Token | Hex | Usage |
|-------|-----|-------|
| `sky-700` | `#0288d1` | Info (dark) |
| `sky-600` | `#039be5` | Info (primary) |
| `sky-400` | `#29b6f6` | Info (light) |
| `sky-200` | `#81d4fa` | Info backgrounds |

#### Emerald

| Token | Hex | Usage |
|-------|-----|-------|
| `emerald-700` | `#2e7d32` | Success (dark) |
| `emerald-600` | `#388e3c` | Success (primary) |
| `emerald-400` | `#66bb6a` | Success (light) |
| `emerald-200` | `#a5d6a7` | Success backgrounds |

#### Pink

| Token | Hex | Usage |
|-------|-----|-------|
| `pink-700` | `#c2185b` | Accent (dark) |
| `pink-600` | `#e91e63` | Accent (primary) |
| `pink-300` | `#f48fb1` | Accent (light) |
| `pink-50` | `#fce4ec` | Accent backgrounds |

#### Marine

| Token | Hex | Usage |
|-------|-----|-------|
| `marine-700` | `#1565c0` | Chart color 1 |
| `marine-600` | `#1976d2` | Chart color 2 |
| `marine-400` | `#42a5f5` | Chart color 3 |
| `marine-100` | `#bbdefb` | Chart backgrounds |

#### Violet

| Token | Hex | Usage |
|-------|-----|-------|
| `violet-700` | `#6a1b9a` | Chart color 4 |
| `violet-600` | `#7b1fa2` | Chart color 5 |
| `violet-400` | `#ab47bc` | Chart color 6 |
| `violet-100` | `#e1bee7` | Chart backgrounds |

#### Extended Palette (Data Visualization)

| Token | Primary Hex | Usage |
|-------|-------------|-------|
| `cream` | `#fff8e1` | Chart category |
| `lemon` | `#fff59d` | Chart category |
| `purple` | `#9c27b0` | Chart category |
| `bamboo` | `#8bc34a` | Chart category |
| `lime` | `#cddc39` | Chart category |
| `plum` | `#7b1fa2` | Chart category |
| `leaf` | `#4caf50` | Chart category |
| `terracotta` | `#bf360c` | Chart category |
| `viridian` | `#00695c` | Chart category |
| `brown` | `#795548` | Chart category |

### 2.2 Semantic Color System

```css
/* Brand */
--color-brand-primary: #e53935;
--color-brand-secondary: #ef5350;
--color-brand-tertiary: #ff7961;

/* Interactive */
--color-interactive-primary: #1a5aff;
--color-interactive-hover: #3d75ff;
--color-interactive-active: #6695ff;
--color-interactive-disabled: #888888;

/* Feedback */
--color-success: #388e3c;
--color-warning: #fbc02d;
--color-error: #e53935;
--color-info: #039be5;

/* Surface (Dark Mode) */
--color-surface-primary: #1a1a1a;
--color-surface-secondary: #333333;
--color-surface-tertiary: #555555;
--color-surface-elevated: #444444;

/* Surface (Light Mode) */
--color-surface-light-primary: #ffffff;
--color-surface-light-secondary: #f5f5f5;
--color-surface-light-tertiary: #eeeeee;

/* Text (Dark Mode) */
--color-text-primary: #ffffff;
--color-text-secondary: #cccccc;
--color-text-tertiary: #aaaaaa;
--color-text-disabled: #888888;

/* Text (Light Mode) */
--color-text-light-primary: #1a1a1a;
--color-text-light-secondary: #555555;
--color-text-light-tertiary: #888888;

/* Border */
--color-border-default: #555555;
--color-border-subtle: #333333;
--color-border-strong: #888888;

/* Highlight */
--color-highlight-primary: rgba(26, 90, 255, 0.15);
--color-highlight-brand: rgba(229, 57, 53, 0.15);

/* Chart Scale (12-color categorical) */
--color-chart-1: #1976d2;
--color-chart-2: #009688;
--color-chart-3: #e53935;
--color-chart-4: #7b1fa2;
--color-chart-5: #f9a825;
--color-chart-6: #388e3c;
--color-chart-7: #e91e63;
--color-chart-8: #00796b;
--color-chart-9: #1565c0;
--color-chart-10: #6a1b9a;
--color-chart-11: #bf360c;
--color-chart-12: #795548;
```

---

## 3. Typography Rules

### Font Stack

```css
/* Primary (UI) */
--font-family-primary: "Noto Sans JP", "Noto Sans SC", "Noto Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

/* Monospace (Data/Code) */
--font-family-mono: "JetBrains Mono", "Noto Sans Mono", "SF Mono", Consolas, monospace;

/* Numeric (Tables/Charts) */
--font-family-numeric: "Tabular Nums", "Noto Sans JP", sans-serif;
```

### Type Scale

| Token | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| `display-xl` | 48px | 56px (1.17) | 700 | Hero headlines |
| `display-lg` | 36px | 44px (1.22) | 700 | Page titles |
| `display-md` | 28px | 36px (1.29) | 600 | Section headers |
| `heading-xl` | 24px | 32px (1.33) | 600 | Card titles |
| `heading-lg` | 20px | 28px (1.40) | 600 | Subsection titles |
| `heading-md` | 18px | 26px (1.44) | 600 | Element titles |
| `heading-sm` | 16px | 24px (1.50) | 600 | Small headings |
| `body-lg` | 16px | 24px (1.50) | 400 | Primary body text |
| `body-md` | 14px | 22px (1.57) | 400 | Secondary body text |
| `body-sm` | 13px | 20px (1.54) | 400 | Compact body text |
| `caption-lg` | 12px | 18px (1.50) | 400 | Labels, captions |
| `caption-md` | 11px | 16px (1.45) | 400 | Small labels |
| `caption-sm` | 10px | 14px (1.40) | 500 | Micro text, badges |

### Font Weights

| Token | Value | Usage |
|-------|-------|-------|
| `regular` | 400 | Body text, descriptions |
| `medium` | 500 | Emphasized text, labels |
| `semibold` | 600 | Headings, buttons |
| `bold` | 700 | Display text, strong emphasis |

### Letter Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `tight` | -0.02em | Display text |
| `normal` | 0 | Body text |
| `wide` | 0.02em | Uppercase labels |
| `wider` | 0.04em | Small caps, badges |

### Numeric Typography

```css
/* Tabular figures for data alignment */
.numeric {
  font-feature-settings: "tnum" 1, "lnum" 1;
  font-variant-numeric: tabular-nums lining-nums;
}

/* Proportional figures for prose */
.prose-numeric {
  font-feature-settings: "pnum" 1, "onum" 1;
}
```

### Multi-language Considerations

| Language | Primary Font | Fallback |
|----------|--------------|----------|
| Japanese (JPN) | Noto Sans JP | Hiragino Sans |
| Chinese Simplified (CHS) | Noto Sans SC | PingFang SC |
| English (ENG) | Noto Sans | SF Pro Text |

---

## 4. Component Stylings

### 4.1 Button

#### Variants

| Variant | Description |
|---------|-------------|
| `Button/Liquid` | Width adapts to content |
| `Button/Fixed` | Fixed width (min-width: 120px) |
| `Button/Destructive/Liquid` | Destructive action, fluid width |
| `Button/Destructive/Fixed` | Destructive action, fixed width |
| `Button/Icon` | Icon-only button |

#### Sizes

| Size | Height | Padding (H) | Font Size | Icon Size |
|------|--------|-------------|-----------|-----------|
| `xlarge` | 40px | 20px | 14px | 20px |
| `large` | 36px | 16px | 14px | 18px |
| `medium` | 32px | 14px | 13px | 16px |
| `small` | 28px | 12px | 12px | 14px |
| `xsmall` | 24px | 10px | 11px | 12px |

#### States & Styles

```css
/* Primary Button */
.btn-primary {
  background: var(--color-interactive-primary);  /* #1a5aff */
  color: var(--color-text-primary);              /* #ffffff */
  border: none;
  border-radius: 4px;
  font-weight: 600;
  transition: all 150ms ease-out;
}

.btn-primary:hover {
  background: var(--color-interactive-hover);    /* #3d75ff */
}

.btn-primary:focus {
  background: var(--color-interactive-primary);
  box-shadow: 0 0 0 3px var(--color-highlight-primary);
  outline: none;
}

.btn-primary:active,
.btn-primary.selected {
  background: var(--color-interactive-active);   /* #6695ff */
}

.btn-primary:disabled {
  background: var(--color-surface-tertiary);     /* #555555 */
  color: var(--color-text-disabled);             /* #888888 */
  cursor: not-allowed;
}

/* Outline Button */
.btn-outline {
  background: transparent;
  color: var(--color-interactive-primary);
  border: 1px solid var(--color-interactive-primary);
  border-radius: 4px;
}

.btn-outline:hover {
  background: var(--color-highlight-primary);
  border-color: var(--color-interactive-hover);
}

/* Destructive Button */
.btn-destructive {
  background: var(--color-brand-primary);        /* #e53935 */
  color: var(--color-text-primary);
  border: none;
}

.btn-destructive:hover {
  background: var(--color-brand-secondary);      /* #ef5350 */
}

/* Icon Button */
.btn-icon {
  width: 32px;
  height: 32px;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
}
```

### 4.2 Form Elements

#### TextField

| Property | Value |
|----------|-------|
| Height | 36px (default), 40px (large) |
| Padding | 12px horizontal |
| Border Radius | 4px |
| Border | 1px solid `#555555` |
| Background | `#333333` |
| Font Size | 14px |

```css
.textfield {
  height: 36px;
  padding: 0 12px;
  background: var(--color-surface-secondary);
  border: 1px solid var(--color-border-default);
  border-radius: 4px;
  color: var(--color-text-primary);
  font-size: 14px;
  transition: border-color 150ms ease-out, box-shadow 150ms ease-out;
}

.textfield:hover {
  border-color: var(--color-border-strong);
}

.textfield:focus {
  border-color: var(--color-interactive-primary);
  box-shadow: 0 0 0 3px var(--color-highlight-primary);
  outline: none;
}

.textfield:disabled {
  background: var(--color-surface-tertiary);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}

.textfield.error {
  border-color: var(--color-error);
  box-shadow: 0 0 0 3px rgba(229, 57, 53, 0.15);
}
```

#### TextArea

| Property | Value |
|----------|-------|
| Min Height | 80px |
| Padding | 12px |
| Line Height | 22px |

#### Select / Dropdown

```css
.select {
  height: 36px;
  padding: 0 36px 0 12px;
  background: var(--color-surface-secondary);
  border: 1px solid var(--color-border-default);
  border-radius: 4px;
  appearance: none;
  background-image: url("chevron-down.svg");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 16px;
}

.dropdown-menu {
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border-default);
  border-radius: 4px;
  box-shadow: var(--elevation-3);
  padding: 4px 0;
  min-width: 180px;
}

.dropdown-item {
  height: 36px;
  padding: 0 12px;
  display: flex;
  align-items: center;
  font-size: 14px;
  color: var(--color-text-primary);
  cursor: pointer;
}

.dropdown-item:hover {
  background: var(--color-highlight-primary);
}
```

#### Field Label

```css
.field-label {
  font-size: 12px;
  font-weight: 500;
  color: var(--color-text-secondary);
  margin-bottom: 6px;
  letter-spacing: 0.02em;
}

.field-label.required::after {
  content: "*";
  color: var(--color-error);
  margin-left: 4px;
}
```

#### Checkbox

```css
.checkbox {
  width: 18px;
  height: 18px;
  border: 2px solid var(--color-border-strong);
  border-radius: 3px;
  background: transparent;
  transition: all 150ms ease-out;
}

.checkbox:checked {
  background: var(--color-interactive-primary);
  border-color: var(--color-interactive-primary);
}

.checkbox:focus {
  box-shadow: 0 0 0 3px var(--color-highlight-primary);
}

.checkbox-label {
  font-size: 14px;
  margin-left: 8px;
  color: var(--color-text-primary);
}
```

#### Radio Button

```css
.radio {
  width: 18px;
  height: 18px;
  border: 2px solid var(--color-border-strong);
  border-radius: 50%;
  background: transparent;
}

.radio:checked {
  border-color: var(--color-interactive-primary);
  background: radial-gradient(
    circle,
    var(--color-interactive-primary) 40%,
    transparent 40%
  );
}
```

### 4.3 Table

#### Structure

| Element | Height | Padding | Font Size |
|---------|--------|---------|-----------|
| `th` (header) | 40px | 12px 16px | 12px |
| `td` (cell) | 44px | 12px 16px | 14px |
| `td` (compact) | 36px | 8px 12px | 13px |
| `td` (comfortable) | 52px | 16px 16px | 14px |

```css
.table {
  width: 100%;
  border-collapse: collapse;
  font-variant-numeric: tabular-nums;
}

.table th {
  height: 40px;
  padding: 12px 16px;
  background: var(--color-surface-tertiary);
  border-bottom: 1px solid var(--color-border-default);
  font-size: 12px;
  font-weight: 600;
  text-align: left;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.table td {
  height: 44px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--color-border-subtle);
  font-size: 14px;
  color: var(--color-text-primary);
}

.table tr:hover td {
  background: var(--color-highlight-primary);
}

.table td.numeric {
  text-align: right;
  font-family: var(--font-family-mono);
}

/* Sortable Header */
.table th.sortable {
  cursor: pointer;
  user-select: none;
}

.table th.sortable:hover {
  background: var(--color-surface-secondary);
}

.table th.sorted-asc::after,
.table th.sorted-desc::after {
  margin-left: 8px;
  opacity: 0.7;
}
```

### 4.4 Navigation

#### Global Header

```css
.global-header {
  height: 56px;
  background: var(--color-surface-primary);
  border-bottom: 1px solid var(--color-border-subtle);
  display: flex;
  align-items: center;
  padding: 0 24px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.global-header-logo {
  height: 28px;
  margin-right: 32px;
}

.global-header-nav {
  display: flex;
  gap: 4px;
}

.global-header-nav-item {
  height: 40px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text-secondary);
  border-radius: 4px;
  transition: all 150ms ease-out;
}

.global-header-nav-item:hover {
  color: var(--color-text-primary);
  background: var(--color-highlight-primary);
}

.global-header-nav-item.active {
  color: var(--color-interactive-primary);
  background: var(--color-highlight-primary);
}
```

#### Global Navigation (Sidebar)

```css
.global-nav {
  width: 240px;
  background: var(--color-surface-secondary);
  border-right: 1px solid var(--color-border-subtle);
  height: 100vh;
  position: fixed;
  left: 0;
  top: 56px;
  overflow-y: auto;
  padding: 16px 0;
}

.global-nav-section {
  padding: 8px 16px;
}

.global-nav-section-title {
  font-size: 11px;
  font-weight: 600;
  color: var(--color-text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 8px;
}

.global-nav-item {
  height: 36px;
  padding: 0 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  color: var(--color-text-secondary);
  border-radius: 4px;
  margin: 2px 0;
}

.global-nav-item:hover {
  background: var(--color-highlight-primary);
  color: var(--color-text-primary);
}

.global-nav-item.active {
  background: var(--color-interactive-primary);
  color: var(--color-text-primary);
}
```

#### Local Navigation

```css
.local-nav {
  display: flex;
  gap: 2px;
  border-bottom: 1px solid var(--color-border-subtle);
  padding: 0 24px;
}

.local-nav-item {
  height: 44px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text-secondary);
  border-bottom: 2px solid transparent;
  margin-bottom: -1px;
  transition: all 150ms ease-out;
}

.local-nav-item:hover {
  color: var(--color-text-primary);
}

.local-nav-item.active {
  color: var(--color-interactive-primary);
  border-bottom-color: var(--color-interactive-primary);
}
```

#### Tab

```css
.tab-group {
  display: flex;
  gap: 4px;
  background: var(--color-surface-tertiary);
  padding: 4px;
  border-radius: 6px;
}

.tab {
  height: 32px;
  padding: 0 16px;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text-secondary);
  border-radius: 4px;
  transition: all 150ms ease-out;
}

.tab:hover {
  color: var(--color-text-primary);
}

.tab.active {
  background: var(--color-surface-primary);
  color: var(--color-text-primary);
  box-shadow: var(--elevation-1);
}
```

### 4.5 Card

```css
.card {
  background: var(--color-surface-secondary);
  border: 1px solid var(--color-border-subtle);
  border-radius: 8px;
  overflow: hidden;
}

.card-header {
  padding: 16px 20px;
  border-bottom: 1px solid var(--color-border-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-title {
  font-size: 16px;
  font-weight: 600;
  color: var(--color-text-primary);
}

.card-body {
  padding: 20px;
}

.card-footer {
  padding: 12px 20px;
  border-top: 1px solid var(--color-border-subtle);
  background: var(--color-surface-tertiary);
}

/* Card Comment Variant */
.card-comment {
  padding: 16px;
  background: var(--color-surface-tertiary);
  border-left: 3px solid var(--color-interactive-primary);
}

/* Card List Variant */
.card-list {
  display: flex;
  flex-direction: column;
  gap: 1px;
  background: var(--color-border-subtle);
}

.card-list-item {
  padding: 12px 16px;
  background: var(--color-surface-secondary);
}
```

### 4.6 Feedback Components

#### Notification Bar

```css
.notification-bar {
  padding: 12px 20px;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
}

.notification-bar.info {
  background: rgba(3, 155, 229, 0.15);
  color: var(--color-info);
  border-left: 4px solid var(--color-info);
}

.notification-bar.success {
  background: rgba(56, 142, 60, 0.15);
  color: var(--color-success);
  border-left: 4px solid var(--color-success);
}

.notification-bar.warning {
  background: rgba(251, 192, 45, 0.15);
  color: var(--color-warning);
  border-left: 4px solid var(--color-warning);
}

.notification-bar.error {
  background: rgba(229, 57, 53, 0.15);
  color: var(--color-error);
  border-left: 4px solid var(--color-error);
}
```

#### Snackbar

```css
.snackbar {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  min-width: 320px;
  max-width: 560px;
  padding: 14px 20px;
  background: var(--color-surface-elevated);
  border-radius: 6px;
  box-shadow: var(--elevation-4);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  font-size: 14px;
  color: var(--color-text-primary);
  z-index: 1000;
}

.snackbar-action {
  font-weight: 600;
  color: var(--color-interactive-primary);
  cursor: pointer;
}
```

#### Tooltip

```css
.tooltip {
  position: absolute;
  padding: 8px 12px;
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border-default);
  border-radius: 4px;
  box-shadow: var(--elevation-3);
  font-size: 12px;
  color: var(--color-text-primary);
  max-width: 280px;
  z-index: 1100;
}

.tooltip::before {
  content: "";
  position: absolute;
  width: 8px;
  height: 8px;
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border-default);
  transform: rotate(45deg);
}
```

### 4.7 Additional Components

#### Tag

```css
.tag {
  display: inline-flex;
  align-items: center;
  height: 24px;
  padding: 0 10px;
  font-size: 12px;
  font-weight: 500;
  border-radius: 4px;
  gap: 6px;
}

.tag.default {
  background: var(--color-surface-tertiary);
  color: var(--color-text-secondary);
}

.tag.primary {
  background: var(--color-highlight-primary);
  color: var(--color-interactive-primary);
}

.tag.success {
  background: rgba(56, 142, 60, 0.15);
  color: var(--color-success);
}

.tag.warning {
  background: rgba(251, 192, 45, 0.15);
  color: #b8860b;
}

.tag.error {
  background: rgba(229, 57, 53, 0.15);
  color: var(--color-error);
}
```

#### Searchbox

```css
.searchbox {
  position: relative;
  width: 100%;
  max-width: 400px;
}

.searchbox-input {
  width: 100%;
  height: 40px;
  padding: 0 16px 0 44px;
  background: var(--color-surface-secondary);
  border: 1px solid var(--color-border-default);
  border-radius: 6px;
  font-size: 14px;
  color: var(--color-text-primary);
}

.searchbox-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  color: var(--color-text-tertiary);
}

.searchbox-input:focus {
  border-color: var(--color-interactive-primary);
  box-shadow: 0 0 0 3px var(--color-highlight-primary);
}
```

#### Segmented Control

```css
.segmented-control {
  display: inline-flex;
  background: var(--color-surface-tertiary);
  border-radius: 6px;
  padding: 4px;
}

.segmented-control-item {
  height: 28px;
  padding: 0 14px;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text-secondary);
  border-radius: 4px;
  transition: all 150ms ease-out;
}

.segmented-control-item.active {
  background: var(--color-surface-primary);
  color: var(--color-text-primary);
  box-shadow: var(--elevation-1);
}
```

#### Pager

```css
.pager {
  display: flex;
  align-items: center;
  gap: 4px;
}

.pager-item {
  min-width: 32px;
  height: 32px;
  padding: 0 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-text-secondary);
  border-radius: 4px;
}

.pager-item:hover {
  background: var(--color-highlight-primary);
  color: var(--color-text-primary);
}

.pager-item.active {
  background: var(--color-interactive-primary);
  color: var(--color-text-primary);
}

.pager-item:disabled {
  color: var(--color-text-disabled);
  cursor: not-allowed;
}
```

#### Accordion

```css
.accordion {
  border: 1px solid var(--color-border-subtle);
  border-radius: 6px;
  overflow: hidden;
}

.accordion-item {
  border-bottom: 1px solid var(--color-border-subtle);
}

.accordion-item:last-child {
  border-bottom: none;
}

.accordion-header {
  height: 48px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--color-surface-secondary);
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text-primary);
  cursor: pointer;
}

.accordion-header:hover {
  background: var(--color-surface-tertiary);
}

.accordion-content {
  padding: 16px;
  background: var(--color-surface-primary);
}
```

---

## 5. Layout Principles

### 5.1 Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `space-0` | 0px | Reset |
| `space-1` | 4px | Tight spacing, icon gaps |
| `space-2` | 8px | Compact spacing |
| `space-3` | 12px | Default element spacing |
| `space-4` | 16px | Standard spacing |
| `space-5` | 20px | Comfortable spacing |
| `space-6` | 24px | Section padding |
| `space-8` | 32px | Large spacing |
| `space-10` | 40px | Extra large spacing |
| `space-12` | 48px | Section gaps |
| `space-16` | 64px | Major section gaps |
| `space-20` | 80px | Page-level spacing |
| `space-24` | 96px | Hero spacing |

### 5.2 Grid System

#### Container Widths

| Breakpoint | Container Max-Width | Margin |
|------------|---------------------|--------|
| `xs` (0-599px) | 100% | 16px |
| `sm` (600-899px) | 100% | 24px |
| `md` (900-1199px) | 100% | 32px |
| `lg` (1200-1439px) | 1136px | auto |
| `xl` (1440-1919px) | 1376px | auto |
| `xxl` (1920px+) | 1680px | auto |

#### Column Grid

```css
.grid {
  display: grid;
  gap: var(--space-6);  /* 24px */
}

/* 12-column grid */
.grid-12 {
  grid-template-columns: repeat(12, 1fr);
}

/* Common layouts */
.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }
.grid-6 { grid-template-columns: repeat(6, 1fr); }

/* Responsive */
@media (max-width: 899px) {
  .grid-4, .grid-3 { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 599px) {
  .grid-4, .grid-3, .grid-2 { grid-template-columns: 1fr; }
}
```

### 5.3 Page Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│  Global Header (56px)                                       │
├──────────────┬──────────────────────────────────────────────┤
│              │  Page Title Area (64px)                      │
│   Global     ├──────────────────────────────────────────────┤
│   Navigation │  Local Navigation (44px)                     │
│   (240px)    ├──────────────────────────────────────────────┤
│              │                                              │
│              │  Main Content Area                           │
│              │  (padding: 24px)                             │
│              │                                              │
│              │                                              │
│              │                                              │
├──────────────┴──────────────────────────────────────────────┤
│  Global Footer (48px)                                       │
└─────────────────────────────────────────────────────────────┘
```

### 5.4 Content Spacing Guidelines

| Context | Spacing |
|---------|---------|
| Between form fields | 16px |
| Between form sections | 32px |
| Card internal padding | 20px |
| Between cards | 16px |
| Section title to content | 16px |
| Between sections | 48px |
| Page title to content | 24px |
| Table cell padding | 12px 16px |

### 5.5 Z-Index Scale

| Layer | Z-Index | Usage |
|-------|---------|-------|
| `base` | 0 | Default content |
| `dropdown` | 100 | Dropdowns, popovers |
| `sticky` | 200 | Sticky headers |
| `fixed` | 300 | Fixed navigation |
| `modal-backdrop` | 400 | Modal overlays |
| `modal` | 500 | Modal dialogs |
| `toast` | 600 | Snackbars, toasts |
| `tooltip` | 700 | Tooltips |
| `max` | 9999 | Emergency overrides |

---

## 6. Depth & Elevation

### Elevation System

FALCON uses a 5-level elevation system to create visual hierarchy and indicate interactive states.

| Level | Box Shadow | Usage |
|-------|------------|-------|
| `elevation-0` | none | Flat elements, inline content |
| `elevation-1` | `0 1px 2px rgba(0,0,0,0.3), 0 1px 3px rgba(0,0,0,0.15)` | Cards, raised buttons |
| `elevation-2` | `0 2px 4px rgba(0,0,0,0.3), 0 3px 6px rgba(0,0,0,0.15)` | Hover states, active cards |
| `elevation-3` | `0 4px 8px rgba(0,0,0,0.3), 0 6px 12px rgba(0,0,0,0.15)` | Dropdowns, popovers |
| `elevation-4` | `0 8px 16px rgba(0,0,0,0.3), 0 12px 24px rgba(0,0,0,0.15)` | Modals, dialogs |
| `elevation-5` | `0 16px 32px rgba(0,0,0,0.3), 0 24px 48px rgba(0,0,0,0.15)` | Full-screen overlays |

### CSS Variables

```css
:root {
  --elevation-0: none;
  --elevation-1: 0 1px 2px rgba(0, 0, 0, 0.3), 0 1px 3px rgba(0, 0, 0, 0.15);
  --elevation-2: 0 2px 4px rgba(0, 0, 0, 0.3), 0 3px 6px rgba(0, 0, 0, 0.15);
  --elevation-3: 0 4px 8px rgba(0, 0, 0, 0.3), 0 6px 12px rgba(0, 0, 0, 0.15);
  --elevation-4: 0 8px 16px rgba(0, 0, 0, 0.3), 0 12px 24px rgba(0, 0, 0, 0.15);
  --elevation-5: 0 16px 32px rgba(0, 0, 0, 0.3), 0 24px 48px rgba(0, 0, 0, 0.15);
}
```

### Elevation Usage Guidelines

| Component | Default | Hover | Active |
|-----------|---------|-------|--------|
| Card | elevation-1 | elevation-2 | elevation-1 |
| Button (raised) | elevation-1 | elevation-2 | elevation-0 |
| Dropdown menu | elevation-3 | — | — |
| Modal | elevation-4 | — | — |
| Tooltip | elevation-3 | — | — |
| Snackbar | elevation-4 | — | — |
| Navigation (fixed) | elevation-2 | — | — |

### Surface Colors by Elevation

```css
/* Dark mode surfaces gain brightness with elevation */
--surface-elevation-0: #1a1a1a;
--surface-elevation-1: #242424;
--surface-elevation-2: #2e2e2e;
--surface-elevation-3: #383838;
--surface-elevation-4: #424242;
--surface-elevation-5: #4c4c4c;
```

### Overlay System

```css
/* Modal backdrop */
.overlay-backdrop {
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
}

/* Scrim (lighter overlay) */
.overlay-scrim {
  background: rgba(0, 0, 0, 0.4);
}
```

---

## 7. Do's and Don'ts

### Color Usage

#### ✅ Do's

- Use brand red (`#e53935`) sparingly for primary CTAs and critical actions
- Maintain minimum 4.5:1 contrast ratio for body text
- Use semantic colors consistently (success = emerald, error = red, warning = amber)
- Apply teal for data emphasis and positive metrics
- Use the chart color palette in sequence for data visualization

#### ❌ Don'ts

- Don't use brand red for non-critical UI elements
- Don't combine multiple bright colors in close proximity
- Don't use pure white (`#ffffff`) text on colored backgrounds without checking contrast
- Don't create custom colors outside the defined palette
- Don't use color as the only means of conveying information

### Typography

#### ✅ Do's

- Use tabular figures for numeric data in tables
- Maintain consistent heading hierarchy (don't skip levels)
- Use appropriate font weights: 400 for body, 600 for headings
- Apply proper line-height for readability (1.5 for body text)
- Use monospace fonts for code, IDs, and technical data

#### ❌ Don'ts

- Don't use more than 3 font sizes on a single view
- Don't center-align body text or data
- Don't use light font weights (300) for critical information
- Don't exceed 80 characters per line for body text
- Don't use all-caps for more than 2-3 words

### Components

#### ✅ Do's

- Provide clear focus states for all interactive elements
- Use consistent button hierarchy (primary, secondary, tertiary)
- Include loading states for async actions
- Show clear disabled states with reduced opacity
- Group related form fields with proper spacing

#### ❌ Don'ts

- Don't use destructive buttons without confirmation
- Don't disable buttons without explaining why
- Don't hide critical actions in overflow menus
- Don't use more than one primary button per section
- Don't mix button styles inconsistently

### Layout

#### ✅ Do's

- Use the 8px grid for all spacing decisions
- Maintain consistent padding within components
- Align content to the grid
- Use appropriate whitespace to group related content
- Ensure touch targets are at least 44px × 44px

#### ❌ Don'ts

- Don't use arbitrary spacing values
- Don't crowd elements together
- Don't create layouts wider than the maximum container width
- Don't ignore responsive breakpoints
- Don't place interactive elements too close together

### Data Visualization

#### ✅ Do's

- Use the sequential chart palette for ordered data
- Provide clear axis labels and legends
- Include data point tooltips for detailed information
- Use appropriate chart types for data relationships
- Ensure charts are readable at various sizes

#### ❌ Don'ts

- Don't use 3D effects on charts
- Don't truncate axis labels without indication
- Don't use pie charts for more than 5 categories
- Don't rely solely on color to differentiate data series
- Don't animate charts excessively

### Accessibility

#### ✅ Do's

- Provide text alternatives for icons
- Ensure keyboard navigation works logically
- Use ARIA labels for complex components
- Test with screen readers
- Support reduced motion preferences

#### ❌ Don'ts

- Don't remove focus outlines without alternatives
- Don't use color alone to indicate state
- Don't auto-play media without controls
- Don't trap keyboard focus
- Don't use tiny text (below 11px)

---

## 8. Responsive Behavior

### Breakpoint System

| Breakpoint | Range | Target Devices |
|------------|-------|----------------|
| `xs` | 0 – 599px | Mobile phones |
| `sm` | 600 – 899px | Large phones, small tablets |
| `md` | 900 – 1199px | Tablets, small laptops |
| `lg` | 1200 – 1439px | Laptops, desktops |
| `xl` | 1440 – 1919px | Large desktops |
| `xxl` | 1920px+ | Ultra-wide displays |

### CSS Media Queries

```css
/* Mobile first approach */
@media (min-width: 600px) { /* sm */ }
@media (min-width: 900px) { /* md */ }
@media (min-width: 1200px) { /* lg */ }
@media (min-width: 1440px) { /* xl */ }
@media (min-width: 1920px) { /* xxl */ }

/* Targeting specific ranges */
@media (min-width: 600px) and (max-width: 899px) { /* sm only */ }
```

### Navigation Responsive Behavior

| Breakpoint | Global Nav | Local Nav | Header |
|------------|------------|-----------|--------|
| `xs` | Hidden (hamburger) | Scrollable | Compact (48px) |
| `sm` | Hidden (hamburger) | Scrollable | Compact (48px) |
| `md` | Collapsed (icons) | Full | Full (56px) |
| `lg`+ | Full (240px) | Full | Full (56px) |

```css
/* Navigation collapse */
@media (max-width: 899px) {
  .global-nav {
    position: fixed;
    left: -240px;
    transition: left 300ms ease-out;
  }
  
  .global-nav.open {
    left: 0;
  }
  
  .nav-overlay {
    display: block;
    background: rgba(0, 0, 0, 0.5);
  }
}

@media (min-width: 900px) and (max-width: 1199px) {
  .global-nav {
    width: 64px;
  }
  
  .global-nav-item-label {
    display: none;
  }
}
```

### Table Responsive Patterns

```css
/* Horizontal scroll for complex tables */
@media (max-width: 899px) {
  .table-wrapper {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
  
  .table {
    min-width: 800px;
  }
}

/* Card-based layout for simple tables */
@media (max-width: 599px) {
  .table-responsive-cards tr {
    display: block;
    margin-bottom: 16px;
    border: 1px solid var(--color-border-subtle);
    border-radius: 6px;
  }
  
  .table-responsive-cards td {
    display: flex;
    justify-content: space-between;
    padding: 12px 16px;
    border-bottom: 1px solid var(--color-border-subtle);
  }
  
  .table-responsive-cards td::before {
    content: attr(data-label);
    font-weight: 600;
    color: var(--color-text-secondary);
  }
}
```

### Multi-language Support

#### Language-Specific Adjustments

| Language | Font Adjustment | Line Height | Letter Spacing |
|----------|-----------------|-------------|----------------|
| Japanese (JPN) | Base size | 1.7 | 0.02em |
| Chinese (CHS) | Base size | 1.7 | 0.02em |
| English (ENG) | Base size | 1.5 | 0 |

```css
/* Language-specific typography */
[lang="ja"] {
  font-family: "Noto Sans JP", sans-serif;
  line-height: 1.7;
  letter-spacing: 0.02em;
}

[lang="zh-CN"] {
  font-family: "Noto Sans SC", sans-serif;
  line-height: 1.7;
  letter-spacing: 0.02em;
}

[lang="en"] {
  font-family: "Noto Sans", sans-serif;
  line-height: 1.5;
}

/* CJK text wrapping */
[lang="ja"],
[lang="zh-CN"] {
  word-break: break-all;
  overflow-wrap: break-word;
}
```

#### Navigation Language Variants

```css
/* Accommodate longer text in different languages */
.global-nav-item {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Japanese navigation may need more width */
[lang="ja"] .global-nav {
  width: 260px;
}

/* Chinese navigation */
[lang="zh-CN"] .global-nav {
  width: 250px;
}
```

### Touch Optimization

```css
/* Larger touch targets on mobile */
@media (max-width: 899px) {
  .btn {
    min-height: 44px;
    min-width: 44px;
  }
  
  .dropdown-item {
    min-height: 48px;
  }
  
  .checkbox,
  .radio {
    width: 24px;
    height: 24px;
  }
}
```

### Print Styles

```css
@media print {
  .global-header,
  .global-nav,
  .global-footer {
    display: none;
  }
  
  body {
    background: white;
    color: black;
  }
  
  .card {
    border: 1px solid #ccc;
    box-shadow: none;
  }
  
  a[href]::after {
    content: " (" attr(href) ")";
    font-size: 0.8em;
    color: #666;
  }
}
```

---

## 9. Agent Prompt Guide

### Overview

This section provides guidance for AI agents generating UI code using the FALCON design system. Follow these instructions to ensure consistent, accessible, and maintainable output.

### System Context Prompt

```
You are a UI developer working with the SPEEDA FALCON Design System v3.0. 
This is a B2B data analytics platform serving global enterprise clients.

Key characteristics:
- Dark mode primary interface
- Data-dense layouts optimized for analysis workflows
- Multi-language support (Japanese, Chinese, English)
- Professional, trustworthy aesthetic
- High accessibility standards (WCAG 2.1 AA)

Always reference FALCON design tokens and components. Never use arbitrary values.
```

### Component Generation Rules

#### 1. Always Use Design Tokens

```
✅ Correct:
background: var(--color-surface-secondary);
padding: var(--space-4);
font-size: var(--font-size-body-md);

❌ Incorrect:
background: #333;
padding: 16px;
font-size: 14px;
```

#### 2. Include All Interactive States

When generating interactive components, always include:
- Default state
- Hover state
- Focus state (with visible focus ring)
- Active/Pressed state
- Disabled state

```css
/* Example: Complete button states */
.btn {
  /* Default */
  background: var(--color-interactive-primary);
  transition: all 150ms ease-out;
}

.btn:hover {
  background: var(--color-interactive-hover);
}

.btn:focus {
  outline: none;
  box-shadow: 0 0 0 3px var(--color-highlight-primary);
}

.btn:active {
  background: var(--color-interactive-active);
}

.btn:disabled {
  background: var(--color-surface-tertiary);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}
```

#### 3. Semantic HTML Structure

```html
<!-- Use semantic elements -->
<nav aria-label="Main navigation">
<main role="main">
<section aria-labelledby="section-title">
<article>

<!-- Include ARIA attributes -->
<button aria-expanded="false" aria-controls="dropdown-menu">
<input aria-describedby="field-hint" aria-invalid="true">
<div role="alert" aria-live="polite">
```

#### 4. Responsive Considerations

Always generate mobile-first CSS with appropriate breakpoints:

```css
/* Mobile first */
.component {
  padding: var(--space-4);
}

/* Tablet and up */
@media (min-width: 900px) {
  .component {
    padding: var(--space-6);
  }
}
```

### Prompt Templates

#### Template 1: Component Request

```
Generate a [COMPONENT_NAME] component following FALCON design system.

Requirements:
- Variant: [primary/secondary/destructive]
- Size: [small/medium/large]
- States: [list required states]
- Accessibility: Include ARIA labels and keyboard support

Output format: [React/Vue/HTML+CSS]
```

#### Template 2: Layout Request

```
Create a [PAGE_TYPE] layout using FALCON design system.

Structure:
- Header: [requirements]
- Navigation: [sidebar/top/none]
- Main content: [grid columns, spacing]
- Footer: [requirements]

Responsive behavior:
- Mobile: [behavior]
- Tablet: [behavior]
- Desktop: [behavior]

Language support: [JPN/CHS/ENG]
```

#### Template 3: Data Visualization

```
Generate a [CHART_TYPE] component for displaying [DATA_TYPE].

Requirements:
- Color palette: Use FALCON chart colors in sequence
- Accessibility: Include data table alternative
- Interactivity: [hover states, tooltips, click actions]
- Responsive: [behavior at different sizes]
```

### Code Quality Checklist

Before finalizing generated code, verify:

- [ ] All colors use design tokens
- [ ] All spacing uses the 8px grid
- [ ] Typography follows the type scale
- [ ] Interactive elements have all states
- [ ] Focus states are visible
- [ ] ARIA attributes are included
- [ ] Responsive breakpoints are applied
- [ ] Dark mode is properly supported
- [ ] Multi-language text can accommodate expansion

### Common Patterns

#### Data Table with Sorting

```jsx
<Table>
  <TableHeader>
    <TableRow>
      <TableHead sortable sorted="asc">Company Name</TableHead>
      <TableHead sortable>Revenue</TableHead>
      <TableHead sortable>Growth</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    {data.map(row => (
      <TableRow key={row.id}>
        <TableCell>{row.name}</TableCell>
        <TableCell numeric>{formatCurrency(row.revenue)}</TableCell>
        <TableCell numeric trend={row.growth > 0 ? 'up' : 'down'}>
          {formatPercent(row.growth)}
        </TableCell>
      </TableRow>
    ))}
  </TableBody>
</Table>
```

#### Form with Validation

```jsx
<Form onSubmit={handleSubmit}>
  <FormField>
    <FormLabel required>Company Name</FormLabel>
    <TextField 
      name="companyName"
      error={errors.companyName}
      aria-describedby="company-name-error"
    />
    {errors.companyName && (
      <FormError id="company-name-error">
        {errors.companyName}
      </FormError>
    )}
  </FormField>
  
  <FormActions>
    <Button variant="outline" type="button">Cancel</Button>
    <Button variant="primary" type="submit">Save</Button>
  </FormActions>
</Form>
```

#### Modal Dialog

```jsx
<Modal 
  open={isOpen} 
  onClose={handleClose}
  aria-labelledby="modal-title"
>
  <ModalHeader>
    <ModalTitle id="modal-title">Confirm Action</ModalTitle>
    <ModalCloseButton aria-label="Close dialog" />
  </ModalHeader>
  
  <ModalBody>
    <p>Are you sure you want to proceed?</p>
  </ModalBody>
  
  <ModalFooter>
    <Button variant="outline" onClick={handleClose}>Cancel</Button>
    <Button variant="destructive" onClick={handleConfirm}>Delete</Button>
  </ModalFooter>
</Modal>
```

### Error Handling

When generating error states:

```jsx
// Form field error
<TextField 
  error 
  aria-invalid="true"
  aria-describedby="email-error"
/>
<FormError id="email-error" role="alert">
  Please enter a valid email address
</FormError>

// Page-level error
<NotificationBar variant="error" role="alert">
  <NotificationIcon />
  <NotificationContent>
    Failed to load data. Please try again.
  </NotificationContent>
  <NotificationAction onClick={retry}>Retry</NotificationAction>
</NotificationBar>

// Empty state
<EmptyState>
  <EmptyStateIcon name="search" />
  <EmptyStateTitle>No results found</EmptyStateTitle>
  <EmptyStateDescription>
    Try adjusting your search criteria
  </EmptyStateDescription>
  <EmptyStateAction>Clear filters</EmptyStateAction>
</EmptyState>
```

---

## Appendix: Quick Reference

### Token Cheat Sheet

```css
/* Colors */
--color-brand-primary: #e53935;
--color-interactive-primary: #1a5aff;
--color-surface-primary: #1a1a1a;
--color-text-primary: #ffffff;

/* Spacing */
--space-1: 4px;
--space-2: 8px;
--space-4: 16px;
--space-6: 24px;
--space-8: 32px;

/* Typography */
--font-size-body-md: 14px;
--font-size-heading-md: 18px;
--font-weight-regular: 400;
--font-weight-semibold: 600;

/* Elevation */
--elevation-1: 0 1px 2px rgba(0,0,0,0.3);
--elevation-3: 0 4px 8px rgba(0,0,0,0.3);

/* Border Radius */
--radius-sm: 4px;
--radius-md: 6px;
--radius-lg: 8px;

/* Transitions */
--transition-fast: 150ms ease-out;
--transition-normal: 300ms ease-out;
```

### Component Size Reference

| Component | XS | S | M | L | XL |
|-----------|----|----|