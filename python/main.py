import ReturnsData


print("Imports done")
if __name__ == "__main__":
    print("Hello World")
    assets = ["MSFT", "NVDA", "GOOGL"]
    T = "1y"
    interval = "1d"
    returnsDownload = ReturnsData.ReturnsData()

    df = returnsDownload.timeHorizonReturnsData(assets, T, interval )
    print(df)
    df = returnsDownload.dateRangeReturnsData(assets, start = "2021-01-01",end = "2021-12-31")
    print(df)
