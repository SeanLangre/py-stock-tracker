import asyncio
import shutil
import stat
import time
import matplotlib.pyplot as plt
import pandas as pd
import os

from dotenv import load_dotenv
from matplotlib import dates

# my classes
from calc import CalcMean
from fetcher import fetcher
from ImageSender import ImageSender


def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)


def GetIsBiggerSymbol(open, close):
    if close > open:
        return ":green_circle:"
    return ":red_circle:"


def GetDailyDiff(open, close):
    diff = close - open
    diff = round(diff, 2)
    print(diff)
    return str(diff)


async def StartStockApp():
    load_dotenv()
    # csv
    tickerDatas = pd.read_csv(os.getenv("DATA_PATH"))
    # fetch data
    stocks = await fetcher.getData(tickerDatas)
    #
    for x, stock in enumerate(stocks):
        if not stock:
            print("yes! the var is null")

        ticker = stock[0]
        info = ticker.info
        histOpen = stock[1]["Open"]
        histHigh = stock[1]["High"]
        histLow = stock[1]["Low"]
        histClose = stock[1]["Close"]
        # symbol = info["symbol"]
        # print("{} ({})".format(symbol, x))
        result = CalcMean.MeanHigherThanCurrent(ticker)
        #
        if result:
            shortName = ticker.ticker
            axs = histClose.plot(figsize=(15, 7), title=" | " + shortName)
            # axs = histClose.plot(figsize=(15, 7), title=symbol + " | " + shortName)
            roundedLastOpen = round(histOpen.iloc[-1], 2)
            roundedLastHigh = round(histHigh.iloc[-1], 2)
            roundedLastLow = round(histLow.iloc[-1], 2)
            roundedLastClose = round(histClose.iloc[-1], 2)
            title = (
                ""
                + GetIsBiggerSymbol(roundedLastOpen, roundedLastClose)
                + " "
                + GetDailyDiff(roundedLastOpen, roundedLastClose)
                + " "
                + " | "
                + shortName
                + " | Op: "
                + str(roundedLastOpen)
                + " Hi: "
                + str(roundedLastHigh)
                + " Lo: "
                + str(roundedLastLow)
                + " Cl: "
                + str(roundedLastClose)
            )
            axs.set_title(title)
            axs.xaxis.set_major_locator(dates.MonthLocator(interval=4))
            plt.axvline(["2020-02-21"], linestyle="dotted", color="tab:red")
            plt.tight_layout()
            # plt.show()
            now = time.strftime("%Y%m%d-%H%M%S")
            folder = "pics"
            filename = shortName + "_" + str(now) + "_saved_figure-50pi.png"
            imagePath = folder + "/" + filename
            plt.savefig(imagePath, dpi=50)
            plt.close()  # or fig.clear()
            sendToDiscord = os.getenv("SEND_TO_DISCORD")
            if sendToDiscord == "True":
                ImageSender.SendImage(imagePath, os.getenv("DISCORD_URL"), title)
        else:
            plt.close()  # or fig.clear()
    if os.getenv("REMOVE_PICS") == "True":
        # remove dir
        shutil.rmtree(folder, onerror=remove_readonly)
        # create dir
        os.mkdir(folder)


asyncio.run(StartStockApp())
