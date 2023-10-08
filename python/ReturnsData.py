import pandas as pd 
import numpy as np 
import yfinance as yf 
import datetime
from dateutil.relativedelta import relativedelta
class ReturnsData():

    def __init__(self) -> None:
        print("initialized object")
        # TODO: Put the assets, time horizon, interval, price, etc. in the object 

    def computeLogReturns(self, df:pd.DataFrame, price = "Adj Close") -> pd.DataFrame:
        """
        Computes the log returns of the assets
        """
        df = df[price]
        df = np.log(df) - np.log(df.shift(1)) # computes the log return, shift 
        df = df.dropna() # removes the NaN column 
        return df 



        
    def timeHorizonReturnsData(self, assets:list, T:str, interval:str, price:str = "Adj Close") -> pd.DataFrame:
        """
        generate log return data from T to the present 
        assets: list of ticker names (string)
        T: time horizon (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
        interval: how many reads of stock data per day (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
        """
        # print("Generating log Return Data")
        df = yf.download(assets, period = T, interval = interval) # download tickers 
        return self.computeLogReturns(df, price)


    def dateRangeReturnsData(self, assets:list, start, end,  interval:str = "1d", price:str = "Adj Close") -> pd.DataFrame:
        
        """
        generate log return data for a date range
        assets: list of ticker names (string)
        T: time horizon (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
        interval: how many reads of stock data per day (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
        """
        # print("Generating log Return Data")
        df = yf.download(assets, start = start, end = end, interval = interval) # download tickers 
        return self.computeLogReturns(df, price) 

    def dayReturn(self, assets: list, dateBefore:str, dateAfter:str, interval:str, price:str) -> pd.DataFrame:
        """
        Generate the return for a given day
        """
        # TODO: Write this function
        return pd.DataFrame()


    
    
    def saveReturnsData(self, df: pd.DataFrame, name:str) -> None:
        # print("Saving Data")
        # name convention: assetNames_dateRange.npy
        s = df.to_numpy() # so each column is a stock
        # print("name = ", name)
        with open("../data/" + name + ".npy", "wb") as f:
            np.save(f, s)
        
        


    def generateReturnsSet(self, assets:list, startDate:datetime, T, interval, rebalances, lookback:int, verbose = False):
        dfs = {}
        """
        very sensitive function. Need the numbers to be inputted correctly 
        assets = stock tickers , strings 
        T = horizon. Say 1 year 
        interval = number of returns from each day 
        rebalances - how many rebalances we are going to create. nth rebalance must == T 
        lookback - how far into the past we use for historical data in months

        There is no overlap in the return periods

        TODO: Create a sliding window version of this
        """
        for i in range(rebalances):
            if verbose:
                print("i = ", i)
            startDate = startDate  - relativedelta(months= lookback)
            endDate = startDate + relativedelta(months = lookback) 
            if verbose:
                print("Startdate: ", str(startDate), " endDate: ", str(endDate))
            dfs[rebalances - (i +1)] = self.dateRangeReturnsData(assets,startDate,endDate,interval)
            # print(dfs[i])
            
        
        return dfs 
            
