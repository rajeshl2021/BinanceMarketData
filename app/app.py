from flask import Flask, render_template, jsonify, request
from binance.binance_market_data import BinanceMarketData
import json
import getopt

binance_base_endpoint = 'https://api.binance.com/api/v3'
mdQuery = BinanceMarketData(binance_base_endpoint);

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 
    
@app.route('/symbols')
def exchange_symbols():
    exchange_symbols = mdQuery.get_exchange_symbols()
    #send  ',' seperated symbol string
    return ','.join([str(sym) for sym in exchange_symbols])


@app.route('/book')
def marketdata_book():
    all_args = request.args.to_dict()
    
    if 'symbol' in all_args:
        symbol = all_args['symbol']
    else:
        print ("ERROR: Symbol not provided in request!!")
        return {}
    
    limit = 10
    if 'limit' in all_args:
        limit = int(all_args['limit'])

    return mdQuery.get_marketdata_book_snapshot(symbol, limit)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
