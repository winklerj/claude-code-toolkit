---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.

## Design Thinking Phase

Before coding, understand the context and commit to a BOLD aesthetic direction:

### 1. Purpose Analysis
- **Primary user**: Who will use this? Age, profession, context?
- **Emotional goal**: Should it feel trustworthy? Exciting? Calming? Premium?
- **Core action**: What's the ONE thing users need to do here?
- **Brand alignment**: Does this need to match existing visual identity?

### 2. Aesthetic Direction Selection

Pick an extreme and commit to it. Some directions to consider:

| Direction | Characteristics | Best For |
|-----------|-----------------|----------|
| **Brutalist/Raw** | Exposed structure, monospace fonts, harsh contrast, visible system elements | Developer tools, portfolios, art galleries |
| **Luxury/Refined** | Generous whitespace, serif typography, muted palette, restrained animation | Finance, luxury goods, professional services |
| **Playful/Toy-like** | Rounded corners, bright colors, bouncy animations, cartoon elements | Consumer apps, kids products, casual games |
| **Editorial/Magazine** | Strong typography hierarchy, asymmetric grid, large imagery, pull quotes | Media, publishing, portfolio sites |
| **Retro-Futuristic** | Neon accents, gradients, geometric shapes, tech-optimistic vibe | Tech products, games, creative agencies |
| **Organic/Natural** | Soft curves, earth tones, fluid layouts, hand-drawn elements | Wellness, sustainability, food brands |
| **Industrial/Utilitarian** | Exposed mechanics, monochrome, grid systems, technical precision | Enterprise tools, engineering products |
| **Art Deco/Geometric** | Bold lines, symmetry, gold accents, decorative patterns | Events, hospitality, premium products |

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

### 3. Differentiation Question

Ask yourself: "What's the one thing someone will remember about this design?"

If you can't answer specifically, the design isn't distinctive enough.

---

## Typography System

Typography makes or breaks a design. Never settle for generic choices.

### Font Selection Strategy

**Display Fonts (Headlines, Hero Text)**
Choose fonts with character. Consider:
- **Geometric Sans**: Futura, Montserrat, Poppins, Outfit
- **Humanist Sans**: Fira Sans, Source Sans, Open Sans
- **Modern Serif**: Playfair Display, Fraunces, Cormorant
- **Classic Serif**: EB Garamond, Crimson Pro, Libre Baskerville
- **Monospace**: JetBrains Mono, Fira Code, Space Mono, IBM Plex Mono
- **Display/Experimental**: Archivo Black, Big Shoulders Display, Unbounded

**NEVER USE**: Inter, Roboto, Arial, Helvetica for display text. These are acceptable body fonts but make designs look generic at large sizes.

**Body Fonts (Paragraphs, UI Text)**
Prioritize legibility at small sizes:
- Inter, Roboto, Source Sans Pro (functional but common)
- **Better choices**: IBM Plex Sans, DM Sans, Plus Jakarta Sans, Nunito Sans

### Font Pairing Patterns

| Pair Type | Example | Effect |
|-----------|---------|--------|
| Serif + Sans | Playfair Display + DM Sans | Classic editorial feel |
| Geometric + Humanist | Outfit + Source Sans | Modern but approachable |
| Mono + Sans | JetBrains Mono + Inter | Technical, developer-focused |
| Display + Neutral | Big Shoulders + IBM Plex | Bold statements, clean support |

### Typography Scale

Use a consistent mathematical scale:

```css
:root {
  /* Major Third scale (1.250) - balanced, versatile */
  --text-xs: 0.64rem;   /* 10.24px */
  --text-sm: 0.8rem;    /* 12.8px */
  --text-base: 1rem;    /* 16px */
  --text-lg: 1.25rem;   /* 20px */
  --text-xl: 1.563rem;  /* 25px */
  --text-2xl: 1.953rem; /* 31.25px */
  --text-3xl: 2.441rem; /* 39px */
  --text-4xl: 3.052rem; /* 48.83px */
  --text-5xl: 3.815rem; /* 61px */

  /* Line heights per size */
  --leading-tight: 1.1;    /* headlines */
  --leading-snug: 1.3;     /* subheadings */
  --leading-normal: 1.5;   /* body copy */
  --leading-relaxed: 1.75; /* long form */
}
```

### Typography Implementation

```css
/* Headlines: tight, bold, distinctive */
h1 {
  font-family: 'Playfair Display', serif;
  font-size: var(--text-5xl);
  font-weight: 700;
  line-height: var(--leading-tight);
  letter-spacing: -0.02em;
}

/* Body: readable, balanced */
body {
  font-family: 'DM Sans', sans-serif;
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  letter-spacing: 0.01em;
}

/* Accent text: track-wide, uppercase, small */
.label {
  font-family: 'DM Sans', sans-serif;
  font-size: var(--text-xs);
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}
```

---

## Color System

Color creates emotion and hierarchy. Build intentional systems, not random palettes.

### Color Role Definition

Every design needs these colors defined:

```css
:root {
  /* Semantic colors - the "why" */
  --color-surface: /* background of containers */
  --color-surface-elevated: /* cards, modals */
  --color-surface-sunken: /* inputs, code blocks */

  --color-text-primary: /* main content */
  --color-text-secondary: /* labels, captions */
  --color-text-muted: /* placeholders, hints */
  --color-text-inverse: /* text on dark backgrounds */

  --color-border: /* subtle dividers */
  --color-border-strong: /* focused, active states */

  --color-accent: /* primary actions, links */
  --color-accent-hover: /* interactive feedback */

  --color-success: #22c55e;
  --color-warning: #f59e0b;
  --color-error: #ef4444;
}
```

### Palette Strategies

**Monochromatic + Accent**
Base everything on one hue with a contrasting accent:
```css
:root {
  --slate-50: #f8fafc;
  --slate-100: #f1f5f9;
  --slate-200: #e2e8f0;
  --slate-400: #94a3b8;
  --slate-600: #475569;
  --slate-800: #1e293b;
  --slate-900: #0f172a;

  --accent: #3b82f6; /* blue pop */
}
```

**Complementary (High Contrast)**
Two colors opposite on the color wheel:
```css
:root {
  --primary: #1e3a5f;   /* deep blue */
  --complement: #f59e0b; /* amber accent */
}
```

**Analogous (Harmonious)**
Adjacent colors for cohesive feel:
```css
:root {
  --base: #0d9488;    /* teal */
  --shift-1: #059669; /* emerald */
  --shift-2: #0ea5e9; /* sky */
}
```

### Dark Mode Strategy

Don't just invert colors. Rebuild for the context:

```css
[data-theme="dark"] {
  /* Surfaces get darker, not inverted */
  --color-surface: #0f172a;
  --color-surface-elevated: #1e293b;

  /* Text becomes lighter with hierarchy preserved */
  --color-text-primary: #f1f5f9;
  --color-text-secondary: #94a3b8;

  /* Accents may need brightness adjustment */
  --color-accent: #60a5fa; /* brighter blue for dark bg */
}
```

---

## Spatial Composition

Layout creates visual interest. Break free from symmetry.

### Grid Systems

**CSS Grid for Asymmetric Layouts**
```css
.editorial-grid {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 2rem;
}

.feature-offset {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
}

.feature-offset > *:nth-child(even) {
  margin-top: 6rem; /* Create offset rhythm */
}
```

**Overlap and Layering**
```css
.hero-overlap {
  display: grid;
  grid-template-columns: 1fr;
}

.hero-overlap > * {
  grid-area: 1 / 1;
}

.hero-image {
  margin-left: 20%;
}

.hero-text {
  z-index: 10;
  align-self: end;
  max-width: 60%;
  padding: 3rem;
  background: rgba(255, 255, 255, 0.95);
}
```

### Spacing Scale

Use consistent spacing tokens:

```css
:root {
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  --space-12: 3rem;    /* 48px */
  --space-16: 4rem;    /* 64px */
  --space-24: 6rem;    /* 96px */
  --space-32: 8rem;    /* 128px */
}
```

---

## Motion & Animation

Animation should feel intentional, not decorative.

### Page Load Orchestration

Stagger reveals create delight:

```css
@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.stagger-item {
  animation: fadeUp 0.6s ease-out forwards;
  opacity: 0;
}

.stagger-item:nth-child(1) { animation-delay: 0.1s; }
.stagger-item:nth-child(2) { animation-delay: 0.2s; }
.stagger-item:nth-child(3) { animation-delay: 0.3s; }
.stagger-item:nth-child(4) { animation-delay: 0.4s; }
```

### Hover States

Make interactions feel responsive:

```css
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.link {
  position: relative;
}

.link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: currentColor;
  transition: width 0.3s ease;
}

.link:hover::after {
  width: 100%;
}
```

### Micro-interactions (React with Motion)

```tsx
import { motion } from 'framer-motion';

const Button = ({ children }) => (
  <motion.button
    whileHover={{ scale: 1.02 }}
    whileTap={{ scale: 0.98 }}
    transition={{ type: "spring", stiffness: 400, damping: 17 }}
  >
    {children}
  </motion.button>
);
```

---

## Visual Details & Texture

Details elevate design from functional to memorable.

### Background Treatments

**Gradient Mesh**
```css
.hero {
  background:
    radial-gradient(at 40% 20%, #818cf8 0, transparent 50%),
    radial-gradient(at 80% 0%, #22d3ee 0, transparent 50%),
    radial-gradient(at 0% 50%, #fb7185 0, transparent 50%),
    #0f172a;
}
```

**Noise Texture**
```css
.textured {
  position: relative;
}

.textured::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  opacity: 0.05;
  pointer-events: none;
}
```

**Geometric Patterns**
```css
.geometric-bg {
  background:
    linear-gradient(30deg, #1e293b 12%, transparent 12.5%, transparent 87%, #1e293b 87.5%),
    linear-gradient(150deg, #1e293b 12%, transparent 12.5%, transparent 87%, #1e293b 87.5%),
    linear-gradient(30deg, #1e293b 12%, transparent 12.5%, transparent 87%, #1e293b 87.5%),
    linear-gradient(150deg, #1e293b 12%, transparent 12.5%, transparent 87%, #1e293b 87.5%);
  background-size: 80px 140px;
  background-color: #0f172a;
}
```

### Shadow Systems

Define consistent shadow scales:

```css
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);

  /* Colored shadows for depth */
  --shadow-accent: 0 10px 40px -10px var(--color-accent);
}
```

---

## Anti-Patterns to Avoid

**NEVER use these generic AI aesthetics:**

| Pattern | Why It's Bad | Better Alternative |
|---------|-------------|-------------------|
| Inter font everywhere | Overused, invisible | Pick a distinctive display font |
| Purple-blue gradient on white | AI slop signature | Choose context-specific palette |
| Perfect symmetry | Feels templated | Asymmetry creates interest |
| Generic card grid | Zero personality | Varied layouts, overlap, offset |
| System rounded corners (8px) | Default look | Commit to sharp or very round |
| Muted blue for everything | Safe but boring | Bold accent or monochromatic |
| Skeleton loaders only | Missing delight | Stagger animations, shimmers |

---

## Implementation Checklist

Before shipping, verify:

- [ ] **Typography**: Display font is distinctive, body is readable
- [ ] **Color**: System is defined with semantic names
- [ ] **Spacing**: Consistent scale used throughout
- [ ] **Motion**: Page load is orchestrated, interactions feel responsive
- [ ] **Details**: Backgrounds have texture or depth, shadows are consistent
- [ ] **Differentiation**: Can describe the "one memorable thing"
- [ ] **Cohesion**: Every element follows the chosen aesthetic direction

---

Remember: Claude is capable of extraordinary creative work. Don't hold back. Show what can truly be created when thinking outside the box and committing fully to a distinctive vision.
