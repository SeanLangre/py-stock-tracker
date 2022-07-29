class CalcMean:
    def MeanHigherThanCurrent(ticker):
        lastSixMonth = ticker.history(period="6mo")["Close"]  # last 6 months
        mean = lastSixMonth.mean()
        lastClose = lastSixMonth.iloc[-1]
        bufferedLastClose = lastClose + (lastClose * 0.05)  # +5%
        print("---lastClose " + str(lastClose))
        print("---bufferedLastClose " + str(bufferedLastClose))
        print("---mean " + str(mean))
        return mean > bufferedLastClose
