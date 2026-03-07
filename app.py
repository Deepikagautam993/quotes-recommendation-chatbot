from flask import Flask, request, jsonify, send_from_directory
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/style.css")
def css():
    return send_from_directory("frontend", "style.css")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.json["message"]
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
