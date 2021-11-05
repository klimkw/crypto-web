from flask import Flask
import requests

app = Flask(__name__)
KRAKEN_API_ENDPOINT = 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'
GEMINI_API_ENDPOINT = 'https://api.gemini.com/v1/pubticker/btcusd'

class Prices:
    def __init__(self):
        self.buy_recommendation = (float('inf'), None)
        self.sell_recommendation = (float('-inf'), None)
        self.prices = []

    def process_kraken(self, json):
        name = "kraken"
        bid = float(json['result']['XXBTZUSD']['b'][0])
        ask = float(json['result']['XXBTZUSD']['a'][0])
        self._process_exchange(name, ask, bid)


    def process_gemini(self, json):
        name = "gemini"
        bid = float(json["bid"])
        ask = float(json["ask"])
        self._process_exchange(name, ask, bid)
    

    # Updates recommendations (if neccesary)
    def _process_exchange(self, name, ask, bid):
        if ask < self.buy_recommendation[0]:
            self.buy_recommendation = (ask, name)
        if bid > self.sell_recommendation[0]:
            self.sell_recommendation = (bid, name)
        
        self.prices.append({
            "name": name,
            "bid": '{:0.2f}'.format(bid),
            "ask": '{:0.2f}'.format(ask)            
        })


    def result_return(self):
        # Structured for scalability (more exchanges or different data)
        return {
            "exchanges": self.prices,
            "recommendations": {
                "buy": self.buy_recommendation[1],
                "sell": self.sell_recommendation[1]
            }
        }

@app.route('/prices')
def prices():

    # Get data from exchanges
    kraken_json = requests.get(KRAKEN_API_ENDPOINT).json()
    gemini_json = requests.get(GEMINI_API_ENDPOINT).json()

    # Initialize Prices object
    exchange_prices = Prices()
    exchange_prices.process_gemini(gemini_json)
    exchange_prices.process_kraken(kraken_json)


    return exchange_prices.result_return()
