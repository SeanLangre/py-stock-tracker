import yfinance as yf

class fetcher:
    async def getData(tickerDatas):
        stocks = []
        for tickerData in tickerDatas.values:
            tickerValue = tickerData[0]
            ignore = tickerData[1]
            if ignore == True:
                continue

            print(tickerValue)
            ticker = yf.Ticker(tickerValue)
            tickerTouple = (ticker, ticker.history(period="5y")['Close'])
            stocks.append(tickerTouple)
        return stocks