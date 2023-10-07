import pandas as pd 
import numpy as np 
import yfinance as yf 
class ReturnsData():

    def __init__(self) -> None:
        print("initialized object")

    def computeLogReturns(self, df:pd.DataFrame, price = "Adj Close") -> pd.DataFrame:
        """
        Computes the log returns of the assets
        """
        df = df[price]
        df = np.log(df) - np.log(df.shift(1)) # computes the log return, shift 
        df = df.dropna() # removes the NaN column 
        return df 



        
    def TimeHorizonReturnsData(self, assets:list, T:str, interval:str, price:str = "Adj Close") -> pd.DataFrame:
        """
        generate log return data from T to the present 
        assets: list of ticker names (string)
        T: time horizon (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
        interval: how many reads of stock data per day (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
        """
        # print("Generating log Return Data")
        df = yf.download(assets, period = T, interval = interval) # download tickers 
        return self.computeLogReturns(df, price)


    def dateRangeReturnsData(self, assets:list, start:str = "", end:str = "",  interval:str = "1d", price:str = "Adj Close") -> pd.DataFrame:
        
        """
        generate log return data for a date range
        assets: list of ticker names (string)
        T: time horizon (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
        interval: how many reads of stock data per day (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
        """
        # print("Generating log Return Data")
        df = yf.download(assets, start = start, end = end, interval = interval) # download tickers 
        return self.computeLogReturns(df, price) 

    
    def saveReturnsData(self, df: pd.DataFrame) -> None:
        print("Saving Data")
        

