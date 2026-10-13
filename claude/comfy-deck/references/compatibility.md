# Environment and renderer compatibility

## Codex

Use the installed presentation workflow for local PowerPoint output and its renderer. For an existing native Google Slides deck, use the connected Google Drive/Slides workflow when available. Keep the requested native format; do not substitute a local PPTX unless needed and explained.

Resolve bundled logo paths from the installed skill directory. Do not depend on a specific plugin version, one user's home directory, or PptxGenJS being installed. The brand skill does not install packages, create cloud accounts, or grant connector access.

## Claude, Cowork, and Claude Code

Use Claude's available PowerPoint/document skill for `.pptx` generation and rendering, together with these brand rules. In Claude Code, use the project's available presentation toolchain. Load supporting references relative to this skill's directory; no Codex-specific API is required for the brand rules.

For Claude web/desktop and Cowork, the upload archive contains exactly `comfy-deck/SKILL.md`, `comfy-deck/references/`, and `comfy-deck/assets/`. For local Claude Code, install the prepared `claude/comfy-deck/` folder in the user or project skills directory. Detailed installation instructions are in the repository README, outside the uploaded skill.

## Native Google Slides

Use authenticated connectors for the selected deck. Copy the source once when requested; preserve its native text, list formatting, evidence, links, notes, slide order, and media proportions while applying the brand changes.

- A specified font family can render through a fallback for only some characters. In the October 2026 test, Arial Black rendered Latin/numerals but Ukrainian headings used a serif fallback. Montserrat 900 rendered those headings correctly. Check the current renderer instead of declaring Arial Black universally unsupported.
- Keep Arial Black/Montserrat primary. Additional COMFY fonts may not be available in the native font menu; do not set an unknown family name and claim that the original font is applied. Use supported primary fonts and explain a material limitation. Keep narrative text editable.
- Set the intended font family, weighted family, and bold state together where the API requires it. Changing only the family can alter existing weights; preserve mixed runs and paragraph roles.
- A duplicated image may have normalized intrinsic `size`. Derive transform scale from the returned dimensions rather than resetting `scaleX/scaleY` to 1. Use one uniform scale to preserve artwork proportions.
- Prefer an existing native object when updating content or logos. If a broken image still does not render after replacement, use the original asset in a correctly sized image object and verify the output.
- Export and inspect every slide. Reuse unchanged source snapshots and renders; perform new verification when a concrete repair or structural change invalidates them.

## Font and asset fallback

For local output, inspect actual font metadata, glyph coverage, and the rendered result. Use Montserrat ExtraBold/Black for affected headings when Arial Black is unavailable or substitutes the required language. Calibri is the body fallback if Montserrat cannot be used. Retain the primary fonts as the default rather than changing the entire deck to COMFY faces.

Prefer original SVG logos and modules where the toolchain supports them. Use the bundled PNG logos or proportionally rendered originals for platforms that require raster images. Do not convert narrative text or native data tables into pictures.
