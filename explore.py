import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



def plot_variable_pairs(df):
    
    ''' Function to take in df and do a pair plot using kind=reg'''
    
    sns.pairplot(df.sample(5000), corner=True, kind='reg')
    plt.show()



def plot_categorical_and_continious_vars(df, x='cat feature here', y='cont feature here'):
    
    ''' Takes in df and plots the categorical/discrete and continious features 
        and outputs visuals'''
    
    sns.barplot(x=df[x], y=df[y], data=df)
    plt.show()
    
    sns.swarmplot(x=df[x], y=df[y], data=df)
    plt.show()
    
    sns.boxplot(x=df[x], y=df[y], data=df)
    plt.show()