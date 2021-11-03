from flask import Flask
import requests

app = Flask(__name__)
KRAKEN_API_ENDPOINT = 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'
GEMINI_API_ENDPOINT = 'https://api.gemini.com/v1/pubticker/btcusd'


def process_kraken(json):
    return {
        "name": "kraken",
        "bid": '{:0.2f}'.format(float(json['result']['XXBTZUSD']['b'][0])),
        "ask": '{:0.2f}'.format(float(json['result']['XXBTZUSD']['a'][0]))
    }


def process_gemini(json):
    return {
        "name": "gemini",
        "bid": '{:0.2f}'.format(float(json["bid"])),
        "ask": '{:0.2f}'.format(float(json["ask"]))
    }


@app.route('/prices')
def prices():
    list_of_exchanges = []

    kraken_json = requests.get(KRAKEN_API_ENDPOINT).json()
    gemini_json = requests.get(GEMINI_API_ENDPOINT).json()

    k = process_kraken(kraken_json)
    list_of_exchanges.append(k)

    g = process_gemini(gemini_json)
    list_of_exchanges.append(g)

    # Structured as such to allow for scalability (more exchanges or different data)
    return {"exchanges": list_of_exchanges}
