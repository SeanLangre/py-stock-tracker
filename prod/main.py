import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

tickerDatas = pd.read_csv('tickers.csv')

for tickerData in tickerDatas.Ticker:
    # for tickerData in ["VOLV-B.ST", "XACTHDIV.ST"]:
    print(tickerData)
    ticker = yf.Ticker(tickerData)
    if not ticker:
        print("yes! the var is null")

    if not 'shortName' in ticker.info:
        print("shortName is null")
    else:
        shortName = ticker.info['shortName']
        symbol = ticker.info['symbol']
        hist = ticker.history(period="5y")
        hist['Close'].plot(figsize=(15, 7), title=symbol+' | '+shortName)
        plt.show()
