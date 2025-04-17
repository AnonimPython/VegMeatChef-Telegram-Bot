import os
import json
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

def init_recipes():
    default = {
        "vegan": {
            "Пример веганского": "Рецепт здесь...",
            "Другой рецепт": "Шаги приготовления..."
        },
        "non_vegan": {
            "Пример невеганского": "Рецепт здесь...",
            "Мясное блюдо": "Шаги приготовления..."
        }
    }
    
    if not os.path.exists('recipes.json'):
        with open('recipes.json', 'w', encoding='utf-8') as f:
            json.dump(default, f, ensure_ascii=False, indent=4)
        return default
    else:
        try:
            with open('recipes.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return default

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('🍏 Веган', '🍗 Не веган')
    markup.row('❓ Помощь')
    return markup

def recipes_menu(is_vegan):
    recipes = init_recipes()
    category = 'vegan' if is_vegan else 'non_vegan'
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for recipe in recipes[category]:
        markup.row(recipe)
    markup.row('🔙 Назад')
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "👨🍳 Привет! Я бот-шеф. Выбери тип рецептов:",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: m.text in ['🍏 Веган', '🍗 Не веган'])
def show_recipes(message):
    is_vegan = message.text == '🍏 Веган'
    recipes = init_recipes()
    category = 'vegan' if is_vegan else 'non_vegan'
    
    if not recipes[category]:
        bot.send_message(message.chat.id, "😢 Рецептов пока нет")
    else:
        bot.send_message(
            message.chat.id,
            f"Вот {'веганские' if is_vegan else 'невеганские'} рецепты:",
            reply_markup=recipes_menu(is_vegan)
        )

@bot.message_handler(func=lambda m: m.text in init_recipes()['vegan'] | init_recipes()['non_vegan'])
def show_recipe(message):
    recipes = init_recipes()
    for category in ['vegan', 'non_vegan']:
        if message.text in recipes[category]:
            bot.send_message(
                message.chat.id,
                f"🍳 {message.text}:\n\n{recipes[category][message.text]}",
                reply_markup=recipes_menu(category == 'vegan')
            )

@bot.message_handler(func=lambda m: m.text == '🔙 Назад')
def back(message):
    send_welcome(message)

@bot.message_handler(func=lambda m: m.text == '❓ Помощь')
def help(message):
    bot.send_message(
        message.chat.id,
        "Просто выбери категорию и получи рецепт!\n\n" 
        "Если файл recipes.json отсутствует, бот создаст его автоматически",
        reply_markup=main_menu()
    )

if __name__ == '__main__':
    init_recipes()  # Инициализация при запуске
    print("✅ Бот запущен!")
    bot.infinity_polling()