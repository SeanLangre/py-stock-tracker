import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from calc import CalcMean

tickerDatas = pd.read_csv('prod\\tickers.csv')

stocks = []

# get data
# for x, tickerData in enumerate(["0KR.SG", "5J9.F"]):
for tickerData in tickerDatas.values:
    tickerValue = tickerData[0]
    ignore = tickerData[1]
    if ignore == True:
        continue

    print(tickerValue)
    ticker = yf.Ticker(tickerValue)
    stocks.append(ticker)

for x, stock in enumerate(stocks):
    if not stock:
        print("yes! the var is null")

    if not 'shortName' in stock.info:
        print("shortName is null")
    else:
        hist = stock.history(period="5y")
        result = CalcMean.MeanHigherThanCurrent(hist)
        #
        if result:
            shortName = stock.info['shortName']
            symbol = stock.info['symbol']
            print("index " + str(x))
            axs = hist['Close'].plot(figsize=(15, 7), title=symbol+' | '+shortName)
            axs.set_title(symbol+' | '+shortName)
            plt.show()
        else:
            plt.close()  # or fig.clear()
