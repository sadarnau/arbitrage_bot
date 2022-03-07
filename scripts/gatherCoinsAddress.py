endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

import sys
from time import sleep
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

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
allCoinsId = []
# try:
#   response = session.get(endpoint, params=parameters)
#   data = json.loads(response.text)
#   for elem in data['data']:
#     if elem['platform'] != None and elem['platform']['symbol'] == 'ETH':
#         # print(elem)
#         collection.append({elem['symbol'], elem['platform']['token_address']})



# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)

destFile = open('allCoinsOnPolygon.txt', 'a')


# def getCoinsInfos(id):
#   resp = session.get('https://api.coingecko.com/api/v3/coins/' + id)
#   while resp.status_code == 429:
#     sleep(61)
#     resp = session.get('https://api.coingecko.com/api/v3/coins/' + id)
#   newdata = json.loads(resp.text)
#   if 'platforms' in newdata:
#     var = newdata['platforms']
#     if 'polygon-pos' in var:
#      # print(id , var['polygon-pos'], file=destFile)
#       print(id , var['polygon-pos'], file=sys.stderr)


source = open('allCoinsGeneral.json')
tst = json.loads(source.read())
print(tst)
# resp = session.get("https://api.coingecko.com/api/v3/coins/list")

# print(json.dumps(resp.text))


# with open('allCoins2.txt', 'r') as allCoins:
#     allCoinsJson = json.loads(allCoins)
#     #print(allCoinsJson)

for elem in tst:
    print(elem)
    # allCoinsId.append(elem['id'])
i = 0

# print(len(allCoinsId))
# for elem in allCoinsId:
#   if i < len(allCoinsId):
#     getCoinsInfos(elem)
#     i += 1
#     print(">", i, file=sys.stderr)

# print('done', file=sys.stderr)

