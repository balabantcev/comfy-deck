---
name: comfy-deck
description: "Create PowerPoint presentations in the Comfy brand style. Use when the user asks for Comfy-style slides, a Comfy deck, branded Comfy presentation formatting, or explicitly invokes $comfy-deck. Applies Comfy visual identity: green primary (#2ABD13), orange accent (#FC5E0F), Montserrat body text, Arial Black headings, and bundled Comfy logo assets."
---

# Comfy Deck

Create `.pptx` presentations that follow Comfy's brand identity. Use this skill alongside the normal presentation-generation workflow when producing PowerPoint files; follow the standard render-and-verify process for slide QA.

## Brand Tokens

Use these colors without `#` when working with PowerPoint/PptxGenJS APIs:

```javascript
const BRAND = {
  primary: "2ABD13",
  secondary: "FC5E0F",
  white: "FFFFFF",
  lightBg: "F5F5F5",
  darkText: "1A1A1A",
  midText: "555555",
  lightGreen: "E8F8E5",
  chartGrey: "94A3B8",
  chartLightGrey: "CBD5E1",
};
```

- Use `primary` for title slide backgrounds, section headers, key accents, and CTA shapes.
- Use `secondary` for accent highlights, callout numbers, badges, and selected chart series.
- Use `white` for most content slide backgrounds.
- Use `lightBg` for supporting, context, or alternating slides.
- Use `darkText` for body text on light backgrounds.
- Use `midText` for secondary text, captions, and labels.

## Typography

- Use **Arial Black** for headings, slide titles, large numbers, and section numbers.
- Use **Montserrat** for body text, bullets, captions, labels, and subtitles.
- Use Calibri only as a fallback if Montserrat is unavailable.
- Do not introduce other fonts unless the user explicitly asks.

Suggested scale:

| Element | Font | Size | Color |
|---|---:|---:|---|
| Slide title on white/light background | Arial Black | 36-40pt | `1A1A1A` |
| Slide title on green/dark background | Arial Black | 36-44pt | `FFFFFF` |
| Section label / eyebrow | Montserrat uppercase | 12pt | `2ABD13` or `FFFFFF` |
| Body text | Montserrat | 14-16pt | `1A1A1A` |
| Bullet text | Montserrat | 13-15pt | `333333` |
| Large stat / number | Arial Black | 48-72pt | `2ABD13` or `FC5E0F` |
| Caption / label | Montserrat | 10-11pt | `555555` |
| Subtitle on white slide | Montserrat | 18-22pt | `555555` |

## Slide System

Choose backgrounds by slide type:

| Slide type | Background |
|---|---|
| Title / cover | Primary green `2ABD13` |
| Section divider | Primary green `2ABD13` or dark `1A1A1A` |
| Content slides | White `FFFFFF` |
| Supporting / context slides | Light grey `F5F5F5` |
| Closing / CTA | Primary green `2ABD13` |

Never put dark body text directly on primary green. Use white text on green or dark slides.

## Layout Patterns

Vary layouts across the deck. Avoid repeating the same layout twice in a row.

### Title Slide

- Use full green background `2ABD13`.
- Add company/project name in white Arial Black, large, center or left aligned.
- Add subtitle in white Montserrat around 20pt.
- Add a small orange accent shape or a thin white rule if the slide needs visual balance.
- Place the white logo in a corner with clear margin.

### Section Divider

- Use a full green or dark background.
- Add a large section number in orange `FC5E0F`, Arial Black, around 64pt.
- Add section title in white Arial Black, around 36pt.
- Add short descriptor in white Montserrat, around 16pt.

### Two-Column Content

- Put title and body or bullets on the left.
- Put image, chart, diagram, or visual element on the right.
- Add a thin green left-border accent to anchor the text column.

### Stat Callout Cards

- Use white or light grey cards with subtle shadow.
- Use 2-3 cards per row for comparison.
- Put the stat in Arial Black, 56-72pt, green or orange.
- Put the label below in Montserrat, 12pt, grey.

### Icon + Text Rows

- Use small green circles, about 0.5-0.6 inch diameter, to hold icons.
- Use Arial Black 16pt for row headers.
- Use Montserrat 13pt grey for descriptions.
- Stack 3-4 rows vertically.

### Full-Bleed Image

- Let the image fill the slide or one half of the slide.
- Add a dark overlay at 40-50% opacity for readability.
- Put white Arial Black title text over the overlay.

### Data / Chart Slide

- Use a white background.
- Let the chart occupy about 60-70% of the slide.
- Put title and one-line insight above the chart.
- Use Comfy chart colors: `2ABD13`, `FC5E0F`, `94A3B8`, `CBD5E1`.

## Accent Elements

Use accents sparingly and consistently:

- Green left border bar: `2ABD13`, about 0.06-0.08 inch wide.
- Orange badge or pill: `FC5E0F` with white text, for labels, tags, "NEW", percentages, or status marks.
- Divider line: `E0E0E0`, 0.5pt, for separating header from body.
- Stat highlight box: `E8F8E5` with green border, for key numbers in tables.

Do not use accent lines under titles. Prefer whitespace, hierarchy, or a green left bar.

## Charts

Style charts to match the brand:

```javascript
const chartOptions = {
  chartColors: ["2ABD13", "FC5E0F", "94A3B8", "CBD5E1"],
  chartArea: { fill: { color: "FFFFFF" } },
  catAxisLabelColor: "555555",
  valAxisLabelColor: "555555",
  valGridLine: { color: "E5E7EB", size: 0.5 },
  catGridLine: { style: "none" },
  dataLabelColor: "1A1A1A",
};
```

Avoid PowerPoint default blue. Replace default colors with the brand palette.

## Logo Assets

Bundled logo files live in `assets/logos/`:

| File | Use |
|---|---|
| `assets/logos/logo-white.svg` | Green or dark backgrounds |
| `assets/logos/logo-green.svg` | White or light grey backgrounds |
| `assets/logos/logo-mono.svg` | Single-color or print contexts |
| `assets/logos/logo-white.png` | PNG fallback for green or dark backgrounds |
| `assets/logos/logo-green.png` | PNG fallback for white or light grey backgrounds |
| `assets/logos/logo-mono.png` | PNG fallback for single-color contexts |

Always place a logo on the title slide and closing slide. Prefer SVG. Use PNG if the target workflow cannot render SVG reliably.

Placement:

- Use bottom-left or top-left.
- Use about 1.5-2 inches wide, adjusted to preserve aspect ratio.
- Keep at least 0.3 inch margin from slide edges.
- Never stretch, recolor, crop, or distort the logo.

Resolve logo paths from the skill folder, for example:

```javascript
slide.addImage({
  path: path.join(skillDir, "assets/logos/logo-white.svg"),
  x: 0.35,
  y: 5.12,
  w: 1.28,
  h: 0.29,
});
```

## Workflow

1. Clarify slide count, audience, and source content when missing.
2. Plan a sequence: cover, agenda if useful, content sections, and closing.
3. Generate the `.pptx` using the normal presentation workflow.
4. Apply Comfy colors, typography, layouts, and logo placement.
5. Add at least one visual element to every slide: chart, icon row, image, stat, diagram, table, or shaped callout.
6. Render slides to images and visually inspect each slide.
7. Fix layout, contrast, overflow, alignment, and brand mismatches.
8. Save the final file to the user-facing outputs folder when working in a projectless Codex task.

Use file names like `[ProjectName]-deck.pptx` unless the user specifies a name.

## Avoid

- Do not use default blue.
- Do not use Arial for body text unless forced by environment limitations.
- Do not give green and orange equal visual weight; green dominates, orange accents, grey supports.
- Do not make all-text slides.
- Do not use light text on light backgrounds or dark text on green backgrounds.
- Do not stretch or recolor logos.
- Do not use thick decorative divider lines.
