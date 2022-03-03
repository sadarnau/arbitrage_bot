
endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
#   'start':'1',
  'limit':'1000'
#   'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c0f81d55-c4ee-4847-9d78-dfaf952fe10a',
}

session = Session()
session.headers.update(headers)

collection = []
try:
  response = session.get(endpoint, params=parameters)
  data = json.loads(response.text)
  for elem in data['data']:
    if elem['platform'] != None and elem['platform']['symbol'] == 'ETH':
        print(elem)
        collection.append({elem['symbol'], elem['platform']['token_address']})



except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

# curl -X 'GET' \
#   'https://api.coingecko.com/api/v3/coins/polygon-pos/contract/0xc2132d05d31c914a87c6611c10748aeb04b58e8f' \
#   -H 'accept: application/json'
        
print(collection)