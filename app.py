from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    return "OK"

@app.route("/tv", methods=["POST"])
def tv():
    data = request.get_json(force=True)

    # Lấy message từ TradingView
    msg = data.get("message", "No message from TradingView")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    requests.post(url, json=payload)
    return {"ok": True}
