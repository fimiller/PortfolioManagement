import ReturnsData
import datetime

print("Imports done")
if __name__ == "__main__":
    print("Hello World \n")
    assets = ["AAPL", "MSFT", "GOOGL"]
    T = "1y"
    interval = "1d"
    returnsDownload = ReturnsData.ReturnsData()

    # df = returnsDownload.timeHorizonReturnsData(assets, T, interval )
    # print(df)
    # df = returnsDownload.dateRangeReturnsData(assets, start = "2021-01-01",end = "2021-12-31")
    # print(df)
    rebalances = 12 
    lookback = 2
    dfs = returnsDownload.generateReturnsSet(assets, datetime.datetime(2021,1,1), T, interval, rebalances, lookback) 
    print(dfs.keys())
    for i in range(rebalances):
        print("i = ", i)
        print(dfs[i].head())
        print(dfs[i].tail())
        print("-----------------")
