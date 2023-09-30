import sqlite3
import random
import requests
import aiogram

from bs4 import BeautifulSoup
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '5964835227:AAGW5OphRCNEXREHcfvMY_16N7AoXsZJ1XE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# parser website
def parse_facts(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    facts = [p.text for p in paragraphs]

    file_path = "true_facts.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        for fact in facts:
            file.write(fact + "\n")

    return facts

parse_facts("https://www.thefactsite.com/1000-interesting-facts/")

# opening file
def get_fake_facts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()

    if sentences:
        random_fake_sentence = random.choice(sentences).strip()
        return random_fake_sentence
    else:
        return "The file is empty or does not contain any sentences.lol"

# opening file1
def get_true_facts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()

    if sentences:
        random_true_sentence = random.choice(sentences).strip()
        return random_true_sentence
    else:
        return "The file is empty or does not contain any sentences.lol"

# opening file2
def get_true_facts2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()

    if sentences:
        random_true_sentence = random.choice(sentences).strip()
        return random_true_sentence
    else:
        return "The file is empty or does not contain any sentences.lol"

def shuffle_facts():
    fake_facts = get_fake_facts('fake_facts.txt') 
    true_facts = get_true_facts('true_facts.txt')
    true_facts2 = get_true_facts2('true_facts.txt')

    bingo = [fake_facts, true_facts, true_facts2]
    random.shuffle(bingo)

    return bingo

bingo = shuffle_facts()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    global bingo
    # Shuffle the facts whenever the /start command is received
    bingo = shuffle_facts()

    # Create the inline keyboard
    keyboard = InlineKeyboardMarkup(row_width=1)
    
    # Add each fact to the keyboard as a button
    for index, fact in enumerate(bingo):
        button_text = f"Fact {index + 1}"
        callback_data = f"fact_{index}"
        keyboard.add(InlineKeyboardButton(button_text, callback_data=callback_data))
    
    await message.reply(f"Hello there, I am a bot-game Two Truth and one Lie.😊\n"
                        "Shall I send you some facts?\n"
                        f"Here are they:", reply_markup=keyboard)

# Add a callback query handler to handle button presses
@dp.callback_query_handler(lambda query: query.data.startswith("fact_"))
async def process_fact_callback(query: types.CallbackQuery):
    global selected_fact
    fact_index = int(query.data.split("_")[1])
    if 0 <= fact_index < len(bingo):
        selected_fact = bingo[fact_index]
        await query.answer(f"Selected fact: {selected_fact}")
        # Send the fact in the current message
        await send_selected_fact(query.message)
    else:
        await query.answer("Invalid selection")

# Function to send the selected fact
async def send_selected_fact(message: types.Message):
    global selected_fact
    if selected_fact is not None:
        is_true_fact = selected_fact != fake_facts
        await message.answer(f"Here is the fact you selected:\n{selected_fact}")
        if is_true_fact:
            await message.answer("This fact is true!")
        else:
            await message.answer("This fact is false (the fake one). Try again!")
        selected_fact = None  # Reset the selected fact after sending

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
