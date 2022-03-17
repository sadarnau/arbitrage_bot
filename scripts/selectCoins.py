from operator import truediv
from getPolyCoinsMarketData import getPolyCoinsMarketData


def isInMedianFork(index, nbItems, width):
    middle = nbItems / 2
    if middle - width / 2 <= index and middle + width / 2 > index:
        return True
    return False

def getPolyShortList(width):
    coinsData = getPolyCoinsMarketData()

    shortList = {}
    index = 0
    nbItems = len(coinsData)
    for elem in coinsData:
        if index <= width or index > nbItems - width or isInMedianFork(index, nbItems, width):
            shortList[elem] = coinsData[elem]
        # else:
            # coinsData.pop(elem)
        index += 1
    print(shortList)

getPolyShortList(50)
