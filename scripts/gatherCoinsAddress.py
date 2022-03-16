import sys
from time import sleep
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
from getPolygonCoinsAddress import getPolygonCoinsAddress


## CONFIG 
parameters = {
#   'start':'1',
  # 'limit':'1000'
#   'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  # 'X-CMC_PRO_API_KEY': 'c0f81d55-c4ee-4847-9d78-dfaf952fe10a',
}
endpoint = "https://api.coingecko.com/api/v3/"

marketDataParameters = \
"vs_currency=usd\
&category=polygon-ecosystem\
&order=volume_asc\
&per_page=250\
&sparkline=false\
&price_change_percentage=24h"
## CONFIG_END

## INIT
session = Session()
session.headers.update(headers)
## INIT END



def getPolyCoinsMarketData():
  polygonCoinsList = getPolygonCoinsAddress()

  polygonCoinsWithData = {}
  pageNb = 1
  while 1:
    try:
      resp = session.get( endpoint + "coins/markets?" + marketDataParameters + "&page=" + str(pageNb))
      # print(resp, pageNb)
      pageNb += 1
      asObject = json.loads(resp.text)
      if asObject == []:
        print('time to leave') 
        break

      for elem in asObject:
        try:
          if polygonCoinsList[elem['id']] and int(elem['total_volume']) > 50000:
            polygonCoinsWithData[elem['id']] = elem
        except:
          salut = 1 + 1
          # print('not found', elem['id'])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
  print(len(polygonCoinsWithData))

getPolyCoinsMarketData()





