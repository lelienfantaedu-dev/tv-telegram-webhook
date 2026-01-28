from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")


@app.get("/")
def home():
    return "OK"


@app.post("/tv")
def tv():
    # TradingView sẽ gửi JSON: {"message": "..."}
    data = request.get_json(silent=True) or {}
    msg = data.get("message", "No message")

    if not BOT_TOKEN or not CHAT_ID:
        return {"ok": False, "error": "Missing BOT_TOKEN or CHAT_ID env"}, 500

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "HTML"
    }

    r = requests.post(url, json=payload, timeout=10)
    return {"ok": r.ok, "status": r.status_code, "tg": r.text}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
