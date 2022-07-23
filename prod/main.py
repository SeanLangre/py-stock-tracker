import asyncio
import os
from turtle import color 
from dotenv import load_dotenv
from matplotlib import dates
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
            result = CalcMean.MeanHigherThanCurrent(ticker)
            #
            if result:
                shortName = ticker.info['shortName']
                axs = histClose.plot( figsize=(15, 7), title=symbol+' | '+shortName)
                roundedLastClose = round(histClose.iloc[-1], 2)
                axs.set_title(symbol+' | '+shortName+' | '+str(roundedLastClose))
                axs.xaxis.set_major_locator(dates.MonthLocator(interval=4))
                plt.axvline(['2020-02-21'], linestyle='dotted', color='tab:red')
                plt.tight_layout()
                plt.show()
            else:
                plt.close()  # or fig.clear()

asyncio.run(StartStockApp())
