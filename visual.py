import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pydataset import data
from scipy import stats

#--------------------------------------------------------------------------------------------------

def dist_sales(df):

    '''
    Plots distribution of Sale Amount and Item Price. Sample = 10k
    '''
    
    # Plot Sale Amount
    sns.histplot(x ='sale_amount', data= df.sample(10000))
    plt.show()

    # Plot Item Price
    sns.histplot(x ='item_price', data= df.sample(10000))
    plt.show()

#--------------------------------------------------------------------------------------------------

def dist_ops(df):

    '''
    Plots distribution of consumption, wind, solar, and wind+solar.
    '''

    # Consumption
    sns.histplot(x='consumption', data=ops)
    plt.show()

    # Wind
    sns.histplot(x='wind', data=ops)
    plt.show()
    
    # Solar
    sns.histplot(x='solar', data=ops)
    plt.show()
    
    # Wind and Solar
    sns.histplot(x='wind_solar', data=ops)
    plt.show()

#--------------------------------------------------------------------------------------------------