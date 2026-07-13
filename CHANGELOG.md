# Changelog

Всі значущі зміни до скілу `comfy-deck` документуються тут.

Формат базується на [Keep a Changelog](https://keepachangelog.com/uk/1.0.0/).
Версійність за [Semantic Versioning](https://semver.org/lang/uk/): `MAJOR.MINOR.PATCH`

- **MAJOR** — несумісні зміни в логіці або структурі скілу
- **MINOR** — нові можливості (нові типи слайдів, нові токени) без ломаючих змін
- **PATCH** — виправлення, уточнення інструкцій, дрібні правки

---

## [1.1.0] — 2026-07-13

### Додано
- Окремий Codex-сумісний пакет у `codex/comfy-deck`
- `codex/comfy-deck/SKILL.md` із frontmatter у форматі Codex
- `codex/comfy-deck/agents/openai.yaml` з UI-метаданими для Codex
- Копію бренд-логотипів у `codex/comfy-deck/assets/logos/`
- Інструкції встановлення й оновлення для Codex у README

### Змінено
- Оновлено README: тепер окремо описані сценарії Claude / Cowork і Codex
- Оновлено `VERSION` до `1.1.0`

### Не змінено
- Кореневий `SKILL.md` для Claude / Cowork
- Архів `comfy-deck.skill` для встановлення в Claude / Cowork
- Базові бренд-правила, кольори, шрифти й логіка оформлення слайдів

---

## [1.0.0] — 2026-06-22

### Додано
- Базова система брендових токенів: Primary `#2ABD13`, Secondary `#FC5E0F`
- Шрифтова пара: Arial Black (заголовки) + Montserrat (текст)
- 7 типів слайдів: title, section divider, stat cards, two-column, icon+text, chart, closing
- Правила фону за типом слайду (зелений / білий / сірий)
- Вбудовані логотипи: `logo-white`, `logo-green`, `logo-mono`
- Правила розміщення логотипу (розмір 1.28×0.29", позиція bottom-left)
- Стилізація графіків під бренд (chartColors, gridLines)
- QA-чеклист для перевірки слайдів
- Інструкція конвертації SVG → PNG для сумісності з PptxGenJS
