from requests import get
import json
import websocket as ws
from time import sleep
import asyncio


seconds_in_day = 86400.0
snapshot_endpoint = 'https://www.cryptocompare.com/api/data/coinsnapshot/?fsym={}&tsym={}'
crypto_websocket = 'wss://streamer.cryptocompare.com'
#format: {SubscriptionId}~{ExchangeName}~{FromSymbol}~{ToSymbol}
#0 is id for a trade
subscription_string = '{}~{}~{}~{}'

def get_coin_snapshot(coin_symbol ='BTC',conversion_coin_symbol='USD'):
    endpoint = snapshot_endpoint.format(coin_symbol,conversion_coin_symbol)
    print(endpoint)
    response = get(endpoint)
    return response

#get relevant coin information from the response returned from the api get request.
def response_to_dictionary(response):
    coin_json = response.text
    coin_json = json.loads(coin_json)
    return coin_json
#coin_name = coin_json['Data']['FromSymbol']
#get a list of all the big exchanges that deal with crypto currency trading.
def extract_data(coin_symbol = 'BTC'):
    response = get_coin_snapshot(coin_symbol)
    coin_json = response_to_dictionary(response)
    return coin_json['Data']['Exchanges']
def parse_exchange(exchange):
    market = exchange['MARKET']
    price = exchange['PRICE']
    last_volume = exchange['LASTVOLUME']
    last_volume_to = exchange['LASTVOLUMETO']
    lv_24_hr = float(exchange['VOLUME24HOUR'])
    lv_24_hr_to = float(exchange['VOLUME24HOURTO'])
    open_24_hr = exchange['OPEN24HOUR']
    open_24_high = exchange['HIGH24HOUR']
    open_24_low = exchange['LOW24HOUR']
    #print('\n'.join([market,price,lv_24_hr,lv_24_hr_to]))
    print(market)
    print('price ratio: {}'.format(lv_24_hr_to/seconds_in_day))

    print('quantitiy ratio: {}'.format(lv_24_hr/seconds_in_day))

def subscribe(exchange_name,from_symbol = 'BTC',to_symbol='USD'):
    return subscription_string.format(0,exchange_name,from_symbol,to_symbol)
def subscribe_to_all_exchanges(exchanges):
    socket = ws.create_connection(crypto_websocket)
    print('good')
    #sleep(100)
    #subs = [subscribe(exchange) for exchange in exchanges]
    #print('data')
    #socket.send('SubAdd', {'subs': subs} )
    #sleep(60)
    #socket.send('SubRemove',{'subs':subs})
    #print(socket.recv())
    #socket.close()

def parse_coin(past_snapshot,coin_info_dict):
    coin_info_dict['Data']['Exchanges']










