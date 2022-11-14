import json
import os
import requests
from flask import Flask
from flask import flash, render_template, request, redirect
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

app = Flask(__name__)

@app.route("/")
def main():
    crypto_prices = cg.get_search_trending()
    crypto_prices = crypto_prices['coins']
    print(crypto_prices[0])
    return render_template('index.html', crypto_prices=crypto_prices)

if __name__ == '__main__':
   app.run()
