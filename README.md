# THIS IS NOT FINANCIAL ADVICE. 
I do **not** endorse using these strategies with any of your actual money. Please consult a professional.

# Portfolio Management

This is a repository where I am investigating quantitative portfolio management strategies using mathematical optimization techniques. This is a hobby project of mine.

## Strategies Present 
This is in Julia 
## Data Collection Done 
This is in python. Currently do not have sliding windows of data. 
## Analysis of Results 

### TODO

1. Sliding windows for data collection instead of distinct windows to test results 
2. Implement strategies in Julia 
     - $\frac{1}{n}$ weights, 
     - Markowitz (with and without a risk free asset)
        - Value at Risk as a risk measure instead of variance
        - Expected Shortfall as a risk measure instead of variance 
        - Adding upper and lower investment limits ($\ell_{i} \leq w_i \leq u_{i} \forall i \in \{1,\dots,n \}$)
    - Peng & Linetsky "Portfolio Selection: A Statistical Learning Approach" paper for inspiration firstly 
3. Portfolio Analytics in Julia 
    - Time series of results 
    - Sharpe and Sortino Ratio
    - Maximum Drawdown 