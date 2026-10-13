---
name: comfy-deck
description: "Create and restyle presentations in the Comfy brand style, including PowerPoint and native Google Slides when connected tools are available. Use for Comfy decks, branded slide formatting, or an explicit comfy-deck request. Keep Arial Black and Montserrat primary; add optional COMFY fonts and apply the 2026 brandbook with original logo, texture, and modular-block resources."
metadata:
  version: "1.2.0"
---

# Comfy Deck

Apply Comfy's visual identity to new presentations or existing decks in Codex, Claude, Cowork, or Claude Code. Follow the user's requested format, content, slide count, and editing scope. Use the presentation workflow and tools available in the current environment; this skill supplies brand decisions rather than a fixed rendering library.

## Choose the relevant rules

- For every deck, use the palette, primary typography, and logo rules below.
- For plush graphics, Пуш, thematic blocks, retail offers, КРАЩ, installments, or seasonal material, read [references/brandbook-2026.md](references/brandbook-2026.md).
- To obtain original fonts or artwork, read [references/resources.md](references/resources.md). Additional fonts and artwork are linked resources; only logos are bundled.
- For native Google Slides, unavailable fonts, or platform-specific setup, read [references/compatibility.md](references/compatibility.md).

User instructions take precedence over this skill. Preserve the meaning and evidence in an existing deck while changing its design. If a copy is requested, copy once and edit that copy. Do not add retail prices, credit characters, or seasonal decorations to analytical slides merely to demonstrate branding.

## Palette

| Role | HEX | Use |
|---|---|---|
| Primary green | `#2ABD13` | Cover/closing backgrounds and main brand accents |
| Orange | `#FC5E0F` | Secondary accents and benefit messages |
| Yellow | `#FFFF00` | Selective emphasis with a legible foreground |
| White | `#FFFFFF` | Content backgrounds and text on primary green |
| Pink | `#FEA1D0` | Supporting information blocks |
| Purple | `#64328A` | Supporting blocks and contrasting labels |
| Light green | `#85F574` | Supporting information blocks |
| Dark green | `#1E9F0A` | Supporting blocks and darker green accents |

Green leads the overall identity; orange and the additional colors support it. Use white text on primary green and dark backgrounds. Check contrast on other fills. Do not use the unresolved light-blue token from brandbook slide 34 until its conflicting HEX/RGB values have been reconciled.

For analytical presentations, retain useful neutral tokens: `#F5F5F5` background, `#1A1A1A` main text, `#555555` secondary text, `#94A3B8` / `#CBD5E1` chart support. These are presentation conventions, not additional official brandbook colors. Use brand colors in charts and keep labels, units, axes, and source notes intact.

## Typography

**The primary system remains unchanged:** Arial Black for headings and large numbers; Montserrat for body text, lists, subtitles, captions, and labels. Calibri is a fallback when Montserrat is unavailable.

COMFY fonts are **additional choices**, not replacements for the primary system:

| Optional font | Role |
|---|---|
| COMFY Semi-Bold | Selected brand messages and accent headings |
| COMFY Bold | Supporting text, numbers, and details within a COMFY brand composition |
| COMFY Ultra-Condensed | Accent numbers and short phrases only |

Use optional fonts when appropriate to the requested design and when their original files render correctly. Keep long prose in the primary system. For COMFY brand messages, the brandbook recommends uppercase, tracking −5%, and line spacing 80%; supporting COMFY text must not exceed the main message in size. These settings do not apply automatically to Arial Black or Montserrat.

Verify language coverage in the final renderer. If Arial Black substitutes Ukrainian characters or looks inconsistent, use Montserrat ExtraBold/Black for the affected headings and retain Arial Black where it renders correctly. Briefly disclose a material font substitution. Do not rasterize editable text to hide missing glyphs.

For a new standard widescreen deck, a useful starting scale is 36–44 pt titles, 14–18 pt body, 10–12 pt captions, and 48–72 pt key numbers. Adjust for page size and density; preserve a supplied template's readable sizes and mixed text roles. Keep body text subordinate to the main message.

## Logos

Use original files from `assets/logos/`; SVG is preferred where supported, PNG otherwise.

| Asset | Background |
|---|---|
| `logo-white.svg` / `.png` | Primary green, dark backgrounds, or photo/video where the white base gives contrast |
| `logo-green.svg` / `.png` | White, light colored backgrounds, and black where the green-base original remains legible |
| `logo-mono.svg` / `.png` | When a full-color original is technically impossible |

Keep a logo on cover and closing slides; use a consistent, uncluttered placement on other slides when appropriate to the deck. For a new widescreen layout, approximately 1.5–2 inches wide and 0.3 inches from the edge is a starting convention, not a verified brandbook measurement. Derive height from the intrinsic aspect ratio.

Never change the logo's colors, lettering, proportions, element positions, base shape, or corner radii. Do not tilt, stretch, outline, redraw, or add effects. Resolve asset paths relative to the installed skill directory rather than hardcoding one user's filesystem.

## Composition

Use a green cover/closing, white content backgrounds, and optional neutral supporting slides as a starting system. A supplied reference may define a different suitable arrangement. Use clear hierarchy and whitespace, and repeat a layout when it helps compare related content.

- Keep each message block focused on one idea with a short readable message.
- Prefer original thematic modules when that visual language fits; preserve their proportions and intended joins. Do not redraw them as generic decorated cards.
- Place original plush artwork where it supports the composition without covering narrative text or evidence. Do not deform characters or invent unofficial poses.
- Keep charts, tables, diagrams, native lists, notes, and links editable where supported. Preserve evidence images without stretching or cropping away meaningful content.
- For product advertising, use the dedicated price and benefit hierarchy in the brandbook reference. Financial forecasts and KPI values are not retail prices.

## Output checks

Render every delivered slide with the target workflow and inspect text fit, glyphs, font weights, contrast, logos, media proportions, and module geometry. Compare the final content and slide order with the source when restyling. Fix concrete defects and verify the affected output. A font name in the API or file is not proof that the renderer used that font for every glyph.

Deliver the requested editable file or verified native presentation link. Mention limitations that affect use; do not claim to have opened the result in an application that was not inspected.
