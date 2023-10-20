using LinearAlgebra
using JuMP, COSMO
using Statistics
println("hello world")

n = 3 
data = npzread("AAPL_MSFT_GOOGL_2020-11-03_2020-11-30.npy")
markowitz = Model(COSMO.Optimizer)

@variable(markowitz, x[1:n])





