import api
import asyncio
#resp = get('https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=ETH&tsym=BTC')
import os
#print(resp.text)
DEFAULT_DIRECTORY = 'exchanges_per_coin'
#resp = api.get_coin_snapshot(coin_symbol ='ETH')
#api.parse_snapshot_response(resp)
from time import sleep

def get_coin():
   pass
def perform_setup():
    check_for_exchange_directory()

def check_for_exchange_directory():
    if not os.path.isdir(DEFAULT_DIRECTORY):
        os.makedirs(DEFAULT_DIRECTORY)
    else:
        print('Directory Exists')
def check_for_coin_exchange_data(coin_name = 'BTC'):
    coin_file_path = os.path.join(os.getcwd(),DEFAULT_DIRECTORY,coin_name + '_exchanges')
    #if not os.path.isfile(coin_file_path):
    pass


'''
#perform_setup()
exchanges = api.get_list_of_exchanges()
for exchange in exchanges:
    print(exchange)
sleep(10)
print('wait 10 seconds')
api.subscribe_to_all_exchanges(exchanges)
'''
exchange_data = api.extract_data('ETH')
for ex in exchange_data:
    api.parse_exchange(ex)


