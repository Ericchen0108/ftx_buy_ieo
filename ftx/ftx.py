from api import FtxClient
import datetime
client = FtxClient()
#change the ieo time to correct time
ieo_sell_time = datetime.datetime(2020, 9, 12, 22, 3, 0, 0)
situation = True

while situation == True:
    if datetime.datetime.now() > ieo_sell_time:
        #change the price and size to hedget
        print(client.place_order('BTC/USD', 'buy',price = 100, size=0.0001, type='limit'))
        break
    else:
        print("Not have the order")

        

