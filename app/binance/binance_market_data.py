from flask import Flask, render_template, jsonify, request
import requests
import json
import getopt


class BinanceMarketData(object):
    def __init__(self, url):
        self.session = requests.Session()
        self.binance_base_url = url;
        self.HEADER = {"Content-Type": "application/json","Accept": "application/json"}
        self.TIMEOUT = 10 # configure HTTP timeout
        
    def get_marketdata_book_snapshot(self, symbol, limit = 5):
        """
        Queries the market data order book for the selected symbol 
        from Binance for the depth level mentioned as limit
        """
        md_book = {}
        try:
            response = self.session.get('{0}/depth?symbol={1}&limit={2}'
                .format(self.binance_base_url,symbol,limit),
                headers=self.HEADER,
                timeout=self.TIMEOUT)
            if response.status_code != 200 :
                print('ERROR: Status - ', response.status_code, 'Headers:', response.headers,  
                    'Error Response:', response)
                return md_book
            
            # return the json response  
            data = response.json()
            return data              
        except requests.exceptions.RequestException as e:
            print(e)
            return md_book

    def get_exchange_symbols(self):
        """
        Queries the exchange supported symbols from Binance and provides the 
        list of symbols.
        """
        exchange_symbols = []
        try:      
            response = self.session.get('{0}/exchangeInfo'.format(self.binance_base_url),
                headers=self.HEADER,
                timeout=self.TIMEOUT)
            if response.status_code != 200 :
                print('ERROR: Status - ', response.status_code, 'Headers:', response.headers,  
                    'Error Response:', response)
                return ""
            
            # Decode the json response into a dictionary and load symbols 
            data = response.json()
            symbols_list = data['symbols']
            for sym in symbols_list :
                exchange_symbols.append(sym['symbol'])
            
            exchange_symbols.sort(reverse=True)
            return exchange_symbols 
                    
        except requests.exceptions.RequestException as e:
            print(e)
            return exchange_symbols



       






