import json
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = '7749707303:AAEbSEOBTYL9X1duov32DnDh9PZ1MPJ7lHM'
CHAT_ID = '@ChiyangiBot'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # Format the signal message
    ticker = data.get('ticker', 'Unknown')
    message = data.get('message', 'New Signal')
    full_message = f"📡 ICT Signal Alert\n\n{message}\n\nAsset: {ticker}"

    # Send to Telegram
    send_message(full_message)
    return {'status': 'ok'}

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'Markdown'
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)