# Changelog

Всі значущі зміни до скілу `comfy-deck` документуються тут.

Формат базується на [Keep a Changelog](https://keepachangelog.com/uk/1.0.0/).
Версійність за [Semantic Versioning](https://semver.org/lang/uk/): `MAJOR.MINOR.PATCH`

- **MAJOR** — несумісні зміни в логіці або структурі скілу
- **MINOR** — нові можливості (нові типи слайдів, нові токени) без ломаючих змін
- **PATCH** — виправлення, уточнення інструкцій, дрібні правки

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
