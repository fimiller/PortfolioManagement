# using COSMO, JuMP, LinearAlgebra
using NPZ
using LinearAlgebra
using Plots, Dates 
# TODO get the optimization imports working (COSMO, JuMP, Mosek, ...)

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

# TODO organize the julia side of things. Core data types / objects that I will use

# TODO figure out analysis script ideas beyond plotting a time series 

# TODO strategies: 1 / n weights , just the S&P 500, Markowitz ( no risk free asset), Markowitz (with risk free), minimizing against VaR and CVaR (expected shortfall)
# Peng & Linetsky approach, see UsefulLinks.txt for paper link

function executeWeightsPortfolio(w, data)
    """
    generates a time series of returns for the total portfolio

    w: vector of weights for asset i. size n * 1 (n = total assets)
    data: set of returns for testing the portfolio, m * n (m rows for returns 1 to m, n columns for asset 1 to n)

    note: will not automatically incorporate a risk free rate 

    """
    return data * w 
end

function plotTotalReturns(returns, dateRange,strategyNames, initInvestment)
    """
    plots the cumulative sum of returns 

    returns: matrix of returns over the time horizon (m rows for dates 1 to m, p columns for strategies 1 to p)

    date range: string that contains the dates of investment 
    
    strategyNames: a list of strategy names 
    initInvestment: initialInvestment Quantity
    """
    # TODO change x axis to be dates ,  use #  xlims = Dates.value.([min_date, max_date])
    realDollars =  initInvestment * (exp.(cumsum(returns, dims = 1))) # add in log returns as they are additive 
    # TODO decide if you need to do initInvestment * (exp.(cumsum(returns, dims = 1)) .- 1) instead. need to figure out if it is right 
    display(plot!(realDollars, legend=:bottomright, label = strategyNames))
    title!("Returns for " * dateRange)
    xlabel!("Time Step")
    ylabel!("Real Dollars (Portfolio Value)")
    
    ylims!(minimum(realDollars) - 25, maximum(realDollars) + 25) # might want to log plot instead, TODO: fix this line, make 25 a parameter
end

function executeWeightsAsset(w, asset)
    """
    generates a time series of returns of a weight float w and a given asset 
    """
end

function equalWeights(data)
    """
    execute portfolio with equal weights strategy 


    TODO figure out how this will be done. 

    Will all the datasets be given here? or just each time step individually
    """
    n = size(data)[2] # total number of assets 

    w = ones(n) / n 

    return executeWeightsPortfolio(w, data)

end


