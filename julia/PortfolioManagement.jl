# using COSMO, JuMP, LinearAlgebra

println("Hello World")

assets = ["MSFT", "NVDA", "GOOGL"]
T = "1y"
interval = "1d"

"""
Outline:

1. Read data generated from Python 

2. Do the portfolio analytics and generate results 

3. Delete the data generated from python
    To save the space on my computer 

"""