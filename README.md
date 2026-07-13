# comfy-deck

**Skill для Claude / Cowork і Codex** — створює презентації `.pptx` у корпоративному стилі Comfy.

Встановіть скілл один раз, і Claude автоматично робитиме всі презентації в єдиному брендовому стилі: правильні кольори, шрифти, логотип на кожному слайді.

Для Codex у репозиторії є окремий сумісний пакет `codex/comfy-deck`, який не змінює і не ламає Claude / Cowork skill.

---

## Встановлення

### Claude / Cowork

1. Завантажте файл [`comfy-deck.skill`](./comfy-deck.skill) з цього репозиторію
2. Відкрийте його — в Cowork з'явиться кнопка **Save skill**
3. Натисніть **Save skill** — скілл встановлено

> Файл `.skill` — це zip-архів із інструкціями та логотипами. Він не потребує жодної додаткової інфраструктури.

### Codex

Скопіюйте готовий Codex-пакет у локальну папку skills:

```bash
mkdir -p ~/.codex/skills
cp -R codex/comfy-deck ~/.codex/skills/comfy-deck
```

Після цього запускайте Codex із явним викликом:

```text
Use $comfy-deck to create a Comfy-style presentation deck.
```

Codex-пакет містить власний `SKILL.md`, UI-метадані `agents/openai.yaml` і копію логотипів у `assets/logos/`.

---

## Використання

### Claude / Cowork

Після встановлення просто попросіть Claude зробити презентацію:

```
Зроби презентацію про наші плани на Q3
Зроби deck для зустрічі з партнерами
Зроби 5 слайдів про нашу команду
```

Claude автоматично застосує Comfy-стиль — зелений бренд-колір, помаранчевий акцент, правильні шрифти та логотип.

### Codex

Після встановлення попросіть Codex зробити презентацію з явним skill-викликом:

```text
Use $comfy-deck to create a 7-slide presentation about Q3 priorities.
```

Codex застосує ті самі бренд-правила Comfy: зелений primary, помаранчевий accent, Arial Black для заголовків, Montserrat для тексту та логотипи з `assets/logos/`.

---

## Що входить у скілл

### Кольори
| Токен | HEX | Використання |
|-------|-----|--------------|
| Primary | `#2ABD13` | Фон title/closing слайдів, акценти |
| Secondary | `#FC5E0F` | Badges, цифри, кнопки |
| White | `#FFFFFF` | Фон контентних слайдів |
| Light BG | `#F5F5F5` | Альтернативний фон |

### Шрифти
- **Arial Black** — заголовки
- **Montserrat** — основний текст, підписи

### Типи слайдів
- Title / Cover
- Section divider
- Stat callout cards
- Two-column content
- Icon + text rows
- Data / chart slide
- Closing slide

### Логотипи (вбудовані)
- `logo-white` — для зелених/темних слайдів
- `logo-green` — для білих/сірих слайдів
- `logo-mono` — монохромний варіант

---

## Структура репозиторію

```
comfy-deck/
├── SKILL.md              # Інструкції для Claude / Cowork
├── assets/
│   └── logos/
│       ├── logo-white.png
│       ├── logo-green.png
│       └── logo-mono.png
├── codex/
│   └── comfy-deck/
│       ├── SKILL.md          # Інструкції для Codex
│       ├── agents/
│       │   └── openai.yaml   # UI-метадані Codex
│       └── assets/logos/     # Логотипи для Codex skill
├── comfy-deck.skill      # Готовий файл для встановлення
├── CHANGELOG.md          # Історія змін
└── README.md
```

---

## Версійність

Поточна версія: **v1.1.0**

Дивись [CHANGELOG.md](./CHANGELOG.md) для повної історії змін.

При оновленні Claude / Cowork skill:
1. Завантажте новий `.skill` файл
2. Встановіть через **Save skill** — він замінить попередню версію

При оновленні Codex skill:

```bash
rm -rf ~/.codex/skills/comfy-deck
cp -R codex/comfy-deck ~/.codex/skills/comfy-deck
```

Політика версій:

- **MAJOR** — несумісні зміни у структурі або поведінці skill
- **MINOR** — нові можливості або підтримка нових середовищ без ломаючих змін
- **PATCH** — уточнення інструкцій, виправлення документації або дрібні правки

---

## Вимоги

- Claude / Cowork (будь-який план)
- Codex для використання пакета з `codex/comfy-deck`
- `pptxgenjs` встановлюється автоматично при першому використанні

---

## Підтримка

Питання або пропозиції → відкрийте [Issue](../../issues) в цьому репозиторії.
