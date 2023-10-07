# this file is to make sure that testing from main works 
import numpy as np 
# opening a file 
with open("../data/AAPL_MSFT_GOOGL_2020-11-03_2020-11-30.npy", "rb") as f:
    print(np.load(f)[0])