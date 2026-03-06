import json
import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Load quotes file
with open("data/quotes.json", "r") as file:
    quotes = json.load(file)

motivation_quotes = quotes["motivation"]
love_quotes = quotes["love"]
funny_quotes = quotes["funny"]

print("Quotes Chatbot 🤖")
print("You can ask things like:")
print(" - give me motivation")
print(" - tell me a love quote")
print(" - make me laugh")
print("Type 'exit' to stop\n")

while True:

    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye 👋")
        break

    words = word_tokenize(user_input)

    # Motivation
    if "motivation" in words or "motivate" in words or "inspire" in words:
        print("Bot:", random.choice(motivation_quotes))

    # Love
    elif "love" in words or "romantic" in words:
        print("Bot:", random.choice(love_quotes))

    # Funny
    elif "funny" in words or "joke" in words or "laugh" in words:
        print("Bot:", random.choice(funny_quotes))

    else:
        print("Bot: Sorry, I can give motivation, love, or funny quotes.")
