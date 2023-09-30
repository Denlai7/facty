import sqlite3
import random
import requests
import aiogram

from bs4 import BeautifulSoup
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

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


# generator
fake_facts = get_fake_facts('fake_facts.txt') 
true_facts = get_true_facts('true_facts.txt')
true_facts2 = get_true_facts2('true_facts.txt')

bingo = [fake_facts, true_facts, true_facts2]
random.shuffle(bingo)
#print(bingo)

for i in bingo:
    print(i)
    if i == fake_facts:
        print("hurraaay")
    

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hello there, I am a bot-game Two Truth and one Lie.😊\n"
                        "Shall I send you some facts?\n"
                        f"Here are they:")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)