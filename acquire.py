import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

from pydataset import data
from scipy import stats

from env import host, username, password    # import needed for get_connection() to operate

#------------------------------------------------------------------------------------------------------------

# Function to build the connection between notebook and MySql. Will be used in other functions.
# Returns the string that is neccessary for that connection.
def get_connection(db, user = username, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#------------------------------------------------------------------------------------------------------------

def star_wars_api(url):
    
    '''
    Intakes a url string and request data. Then Turns data into a JSON, which is then
    coverted into a dataframe. Dataframe returned. 
    URLs: 'https://swapi.dev/api/planets/'
          'https://swapi.dev/api/people/'
          'https://swapi.dev/api/starships/'
    '''
    
    # URLs: 'https://swapi.dev/api/planets/', 
    
    # Retrieve data
    response = requests.get(url)
    
    # Covert to JSON
    data = response.json()
    
    # Covert to dataframe
    df = pd.DataFrame(data['results'])
    
    while data['next'] != None:
        response = requests.get(data['next'])
        df2 = response.json()
        df2 = pd.DataFrame(df2['results'])
        df = pd.concat([df, df2], axis=0)
        
    return df
    
#------------------------------------------------------------------------------------------------------------

def get_ops():
    filename = "ops.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        
        # Read csv from URL
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        
        # Format date to datetime dtype
        df['Date'] = pd.to_datetime(df.Date)

        # Set date as index
        df = df.set_index('date')
        df = df.sort_index()

        # Create month and year columns
        df['month'] = df.index.month
        df['year'] = df.index.year
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)

        # Return the dataframe
        return df 

# url = get_db_url('db')
# pd.read_sql('Query', url)