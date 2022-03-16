import sys
from time import sleep
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint


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


def getPolygonCoinsAddress():
  try:
    resp = session.get( endpoint + "coins/list?include_platform=true")

  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  allCoins = json.loads(resp.text)
  polygonCoinsInfos = {}
  for elem in allCoins:
    if "polygon-pos" in elem["platforms"]:
        polygonCoinsInfos[elem['id']] = elem['platforms']['polygon-pos']
  return polygonCoinsInfos
