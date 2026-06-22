---
name: comfy-deck
description: "Create presentations in the Comfy brand style. Use this skill whenever the user asks to create, build, make, or generate a presentation, deck, or slides — even if they don't mention brand or style. This skill ensures every presentation follows Comfy's visual identity: green primary (#2ABD13), orange accent (#FC5E0F), Montserrat body, Arial Black headings. Always use this skill for any slide or deck creation task."
metadata:
  version: "1.0.0"
---

# Comfy Deck Skill

Create `.pptx` presentations that follow Comfy's brand identity. For all technical implementation details (PptxGenJS API, shapes, charts, images, icons, QA) — read the base pptx skill at the path returned by the system, or follow the pptxgenjs patterns you already know.

---

## Brand Tokens

```
PRIMARY   #2ABD13   — Comfy green. Use for: title slide backgrounds, section headers, key accents, CTA shapes.
SECONDARY #FC5E0F   — Comfy orange. Use for: accent highlights, callout numbers, badges, chart accents.
WHITE     #FFFFFF   — Clean slide background for content slides.
LIGHT_BG  #F5F5F5   — Soft grey for alternating or supporting slides.
DARK_TEXT #1A1A1A   — Body text on light backgrounds.
MID_TEXT  #555555   — Secondary text, captions, labels.
```

**Fonts**
- Headings / titles: **Arial Black** — bold, large, commanding
- Body / bullets / captions: **Montserrat** (fallback: Calibri)

**Never** use other fonts unless the user explicitly asks.

---

## Slide System

### Backgrounds by slide type

| Slide type | Background |
|---|---|
| Title / cover | PRIMARY `2ABD13` |
| Section divider | PRIMARY `2ABD13` or DARK `1A1A1A` |
| Content slides | WHITE `FFFFFF` |
| Supporting / context | LIGHT_BG `F5F5F5` |
| Closing / CTA | PRIMARY `2ABD13` |

**Rule:** Never put dark body text directly on the primary green — use white text on green slides.

### Typography scale

| Element | Font | Size | Color |
|---|---|---|---|
| Slide title (white bg) | Arial Black | 36–40pt | `1A1A1A` |
| Slide title (green bg) | Arial Black | 36–44pt | `FFFFFF` |
| Section label / eyebrow | Montserrat | 12pt, uppercase, charSpacing 4 | `2ABD13` or `FFFFFF` |
| Body text | Montserrat | 14–16pt | `1A1A1A` |
| Bullet text | Montserrat | 13–15pt | `333333` |
| Large stat / number | Arial Black | 48–72pt | `2ABD13` or `FC5E0F` |
| Caption / label | Montserrat | 10–11pt | `555555` |
| White slide subtitle | Montserrat | 18–22pt | `555555` |

---

## Layout Patterns

Use varied layouts — never the same layout twice in a row.

### Title slide
- Full green background (`2ABD13`)
- Company/project name in white Arial Black, center or left-aligned, large (44–52pt)
- Subtitle in white Montserrat 20pt
- Optional: thin white horizontal rule or small orange accent shape

### Section divider
- Full green or dark background
- Large section number in orange (`FC5E0F`), Arial Black 64pt
- Section title in white Arial Black 36pt
- Short descriptor in white Montserrat 16pt

### Two-column content
- Left: title + body text / bullets (Montserrat 14pt)
- Right: image, chart, or visual element
- Thin green left-border accent (0.08" wide, full height, `2ABD13`) on text column

### Stat callout card
- White or light grey card with subtle shadow
- Large stat in Arial Black 56–72pt in green or orange
- Label below in Montserrat 12pt grey
- Use 2–3 cards in a row for comparison

### Icon + text rows
- Icon in small green circle (0.5–0.6" diameter)
- Bold header in Arial Black 16pt
- Description in Montserrat 13pt grey
- Stack 3–4 rows vertically

### Full-bleed image
- Image fills entire slide (or left/right half)
- Dark overlay shape at 40–50% opacity for readability
- Title in white Arial Black over the overlay

### Data / chart slide
- White background
- Chart fills 60–70% of slide area
- Chart colors: primary `2ABD13`, secondary `FC5E0F`, supporting greys `94A3B8`, `CBD5E1`
- Title + one-line insight above the chart

---

## Accent Elements

Use these sparingly but consistently:

- **Green left border bar**: `x: 0.4, w: 0.06, h: [full column height], fill: 2ABD13` — use on content slides to anchor the text column
- **Orange badge / pill**: rounded rectangle `FC5E0F`, white text inside — for labels, tags, "NEW", percentages
- **Divider line**: thin horizontal rule `E0E0E0`, 0.5pt — to separate header from body, never use thick decorative lines
- **Stat highlight box**: light green background `E8F8E5` with green border — for key numbers in tables

---

## Charts

Always style charts to match brand:

```javascript
chartColors: ["2ABD13", "FC5E0F", "94A3B8", "CBD5E1"]
chartArea: { fill: { color: "FFFFFF" } }
catAxisLabelColor: "555555"
valAxisLabelColor: "555555"
valGridLine: { color: "E5E7EB", size: 0.5 }
catGridLine: { style: "none" }
dataLabelColor: "1A1A1A"
```

---

## Things to Avoid

- **No accent lines under titles** — use whitespace or a green left-bar instead
- **No default blue** — replace any PowerPoint default blue with brand green or orange
- **No Arial for body** — use Montserrat (or Calibri as fallback only)
- **No equal color weight** — green dominates, orange accents, grey supports
- **No all-text slides** — every slide needs at least one visual element
- **No light text on light backgrounds** — always verify contrast

---

## Logo Assets

Brand logos are bundled in `assets/logos/`. Always place a logo on the title slide and closing slide.

| File | Use when |
|---|---|
| `assets/logos/logo-white.svg` | On green or dark backgrounds (title, section dividers, closing) |
| `assets/logos/logo-green.svg` | On white or light grey backgrounds |
| `assets/logos/logo-mono.svg` | When printing or single-color context |

**Placement:** bottom-left or top-left corner, ~1.5–2" wide, with at least 0.3" margin from edges. Never stretch or recolor the logo.

**In PptxGenJS**, use the absolute path to the bundled asset:
```javascript
// Resolve the skill's assets directory at runtime:
const skillDir = __dirname; // or pass in from skill context
slide.addImage({
  path: path.join(skillDir, "assets/logos/logo-white.svg"),
  x: 0.35, y: 5.12, w: 1.28, h: 0.29
});
```

If SVG causes issues in a specific PowerPoint version, convert to PNG first:
```bash
# Using Inkscape or rsvg-convert
rsvg-convert -w 400 assets/logos/logo-white.svg -o /tmp/logo-white.png
```

---

## Workflow

1. Clarify slide count and content if not provided
2. Plan slide sequence: cover → agenda (optional) → content → closing
3. Generate `.pptx` using PptxGenJS (see pptx skill for full API reference)
4. Add logo to title and closing slides (see Logo Assets above)
5. QA: convert to images, visually inspect each slide
6. Fix issues and re-verify
7. Save final file to the user's workspace folder

File naming: `[ProjectName]-deck.pptx` or as specified by the user.

---

## Quick Color Reference

```javascript
// Use without # prefix in PptxGenJS
const BRAND = {
  primary:   "2ABD13",  // Comfy green
  secondary: "FC5E0F",  // Comfy orange
  white:     "FFFFFF",
  lightBg:   "F5F5F5",
  darkText:  "1A1A1A",
  midText:   "555555",
  lightGreen: "E8F8E5", // tint for highlights
};
```
