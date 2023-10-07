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
    rebalances = 2 
    lookback = 1 # months
    endDateForTest = datetime.datetime(2021,1,1)
    dfs = returnsDownload.generateReturnsSet(assets,endDateForTest , T, interval, rebalances, lookback) 
    print(dfs.keys())
    for i in range(rebalances):
        print("================\n i = ", i)
        print(dfs[i].head())
        print(dfs[i].tail())
        returnsDownload.saveReturnsData(dfs[i],"_".join(assets) + "_" + dfs[i].index[0].strftime("%Y-%m-%d")+ "_" + dfs[i].index[-1].strftime("%Y-%m-%d"))
