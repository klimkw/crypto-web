from flask import Flask
import requests, json

app = Flask(__name__)
KRAKEN_API_ENDPOINT = 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'
GEMINI_API_ENDPOINT = 'https://api.gemini.com/v1/pubticker/btcusd'

def process_kraken(json):
    return {
        "bid": json['result']['XXBTZUSD']['b'][0],
        "ask": json['result']['XXBTZUSD']['a'][0]
    }

def process_gemini(json):
    return {
        "bid": json["bid"],
        "ask": json["ask"]
    }

@app.route('/')
def chain():
    kraken_json = requests.get(KRAKEN_API_ENDPOINT).json()
    gemini_json = requests.get(GEMINI_API_ENDPOINT).json()
    k = process_kraken(kraken_json)
    g = process_gemini(gemini_json)

    return """
    block my chain!<br>
    kraken bid price: {}&nbsp;
    kraken ask price: {}<br>
    gemini bid price: {}&nbsp;
    gemini ask price: {}
    """.format(k['bid'], k['ask'], g['bid'], g['ask'])