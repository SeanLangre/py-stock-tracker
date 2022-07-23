class CalcMean:
    def MeanHigherThanCurrent(histClose):
        mean = histClose.mean()
        lastClose = histClose.iloc[-1]
        bufferedLastClose = lastClose + (mean*0.1)  # +10%
        print('---mean ' + str(mean))
        print('---bufferedMean ' + str(bufferedLastClose))
        print('---lastClose ' + str(lastClose))
        return mean > bufferedLastClose
