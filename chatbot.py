import json
import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

with open("data/quotes.json", "r") as file:
    quotes = json.load(file)

motivation_quotes = quotes["motivation"]
love_quotes = quotes["love"]
funny_quotes = quotes["funny"]

def get_response(user_input):

    words = word_tokenize(user_input.lower())

    if "motivation" in words or "inspire" in words:
        return random.choice(motivation_quotes)

    elif "love" in words or "romantic" in words:
        return random.choice(love_quotes)

    elif "funny" in words or "joke" in words or "laugh" in words:
        return random.choice(funny_quotes)

    else:
        return "Sorry, I can give motivation, love, or funny quotes."
