from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app)

# Load quotes
with open("data/quotes.json", "r") as file:
    quotes = json.load(file)

motivation_quotes = quotes["motivation"]
love_quotes = quotes["love"]
funny_quotes = quotes["funny"]

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_input = data["message"].lower()

    if "motivation" in user_input:
        response = random.choice(motivation_quotes)

    elif "love" in user_input:
        response = random.choice(love_quotes)

    elif "funny" in user_input or "joke" in user_input:
        response = random.choice(funny_quotes)

    else:
        response = "Sorry, I can give motivation, love, or funny quotes."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)