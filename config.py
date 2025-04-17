import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    ADMIN_ID = os.getenv('ADMIN_ID')
    
    # Food options
    VEGAN_OPTIONS = [
        "Tofu Scramble",
        "Chickpea Curry",
        "Vegan Burger",
        "Lentil Soup",
        "Avocado Toast"
    ]
    
    NON_VEGAN_OPTIONS = [
        "Grilled Chicken",
        "Beef Steak",
        "Fish Tacos",
        "Pork Chops",
        "Cheese Platter"
    ]