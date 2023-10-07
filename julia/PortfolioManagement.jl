# using COSMO, JuMP, LinearAlgebra
using NPZ

println("Hello World")

assets = ["MSFT", "NVDA", "GOOGL"]
T = "1y"
interval = "1d"

data = npzread("AAPL_MSFT_GOOGL_2020-11-03_2020-11-30.npy")
"""
Outline:

1. Read data generated from Python 

2. Do the portfolio analytics and generate results 
    1. Using the first dataset, generate the weights
    2. Using the next dataset, multiply the weights by sum of each asset's returns that month 
        2a. keep that as a time series for each day's returns 
        2b. rebalance the weights using that month's worth of data 
    3. repeat 2 with the next dataset 

3. Delete the data generated from python
    To save the space on my computer 

"""