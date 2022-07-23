import asyncio
import os 
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import pandas as pd
from calc import CalcMean
from fetcher import fetcher

async def StartStockApp():
    load_dotenv()
    # csv
    tickerDatas = pd.read_csv(os.getenv('DATA_PATH'))
    # fetch data
    stocks = await fetcher.getData(tickerDatas)
    #
    for x, stock in enumerate(stocks):
        if not stock:
            print("yes! the var is null")

        ticker = stock[0]
        if not 'shortName' in ticker.info:
            print("shortName is null")
        else:
            histClose = stock[1]
            symbol = ticker.info['symbol']
            print("{} ({})".format(symbol, x))
            result = CalcMean.MeanHigherThanCurrent(histClose)
            #
            if result:
                shortName = ticker.info['shortName']
                axs = histClose.plot( figsize=(15, 7), title=symbol+' | '+shortName)
                axs.set_title(symbol+' | '+shortName)
                plt.axvline(['2020-02-21'])
                # axs.plot(0,['2020-02-21','2020-02-22'], marker="o", label="points")
                plt.show()
            else:
                plt.close()  # or fig.clear()

asyncio.run(StartStockApp())
