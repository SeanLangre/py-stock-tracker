class CalcMean:
    def MeanHigherThanCurrent(hist):
        mean = hist['Close'].mean()
        lastClose = hist.iloc[-1]['Close']
        print('mean ' + str(mean))
        print('lastClose ' + str(lastClose))
        return mean > lastClose