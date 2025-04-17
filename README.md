# VegMeatChef Telegram Bot

![Python Version](https://img.shields.io/badge/python-3.8%252B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Telegram](https://img.shields.io/badge/Telegram-Bot-0088CC)

Ваш персональный кулинарный гид в Telegram! Получайте рецепты для веганов и мясоедов в одном боте 🥦🍗

<div align="center"> <img src="https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif" width="200"> </div>## 🌟 Особенности

* 🥬 **Веганские рецепты** с пошаговыми инструкциями
* 🥩 **Мясные блюда** для настоящих гурманов
* 📱 Удобное меню с кнопками
* 📂 Рецепты хранятся в простом JSON-формате
* 🔄 Автоматическое обновление рецептов без перезапуска бота

## 🚀 Быстрый старт

### Требования

* Python 3.8+
* Аккаунт Telegram
* [Бот-токен](https://t.me/BotFather) от BotFather

### Установка

1. Клонируйте репозиторий:

bash

Copy

```
git clone https://github.com/AnonimPython/VegMeatChef-Telegram-Bot.git
cd chev
```

2. Установите зависимости:

bash

Copy

```
pip install -r requirements.txt
```

Отредактируйте `.env`:

Copy

```
TELEGRAM_BOT_TOKEN=""
```

4. Запустите бота:

bash

Copy

```
python main.py
```

## 🛠 Конфигурация

Добавьте свои рецепты в `recipes.json`:

json

Copy

```
{
  "vegan": {
    "Название блюда": "Пошаговый рецепт...",
    "Смузи из шпината": "1. Смешайте шпинат...\n2. Добавьте банан..."
  },
  "non_vegan": {
    "Стейк из лосося": "1. Маринуйте рыбу...\n2. Жарьте на гриле..."
  }
}
```

## 📂 Структура проекта

Copy

```
vegmeatchef-bot/
├── main.py          # Основной код бота
├── recipes.json     # База рецептов
├── .env             # Конфигурация
├── requirements.txt # Зависимости
└── README.md        # Документация
```

## 🍳 Пример использования

1. Запустите бота командой `/start`
2. Выберите тип питания:
   * 🍏 Веган
   * 🍗 Не веган
3. Выберите рецепт из списка
4. Наслаждайтесь готовкой!

## 📝 Лицензия

Этот проект распространяется под лицензией [MIT](https://license/).
