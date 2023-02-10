import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # import needed for the train, test, split functions.

#------------------------------------------------------------------------------------------------------------

# Function for Training, Validating, and Testing the data. 
def split_data(df, target= 'enter target column here'):
    ''' 
        This function is the train, validate, test, function.
        1. First we create the TRAIN and TEST dataframes at an 0.80 train_size( or test_size 0.2).

        2. Second, use the newly created TRAIN dataframe and split that at a 0.70 train_size
        ( or test_size 0.3), which means 70% of the train dataframe, so 56% of all the data.

        Now we have a train, validate, and test dataframes

    '''
    train, test = train_test_split(df, train_size=0.8, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123, stratify=train[target])
    return train, validate, test

#------------------------------------------------------------------------------------------------------------

# Function for Training, Validating, and Testing the data for continious data.
def split_data_continious(df):
    ''' 
        This function is the train, validate, test, function.
        1. First we create the TRAIN and TEST dataframes at an 0.80 train_size( or test_size 0.2).

        2. Second, use the newly created TRAIN dataframe and split that at a 0.70 train_size
        ( or test_size 0.3), which means 70% of the train dataframe, so 56% of all the data.

        Now we have a train, validate, and test dataframes

    '''
    train, test = train_test_split(df, train_size=0.8, random_state=123)
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123)
    return train, validate, test

#------------------------------------------------------------------------------------------------------------

# Function for returning scaled data
def get_scaled(train, validate, test):
    
    mm_scaler = MinMaxScaler()

    mm_scaler.fit(train)
    scaled_train = mm_scaler.transform(train)

    mm_scaler.fit(validate)
    scaled_validate = mm_scaler.transform(validate)

    mm_scaler.fit(test)
    scaled_test = mm_scaler.transform(test)
    
    return scaled_train, scaled_validate, scaled_test

#------------------------------------------------------------------------------------------------------------

def prep_sales(df):
    
    '''
    Intakes sales df and preps it by coverting to datetime dtype and setting it as the 
    index. Creates month, day of week, and total sales columns.
    '''
    
    # Converting to datetime type
    df['sale_date'] = pd.to_datetime(df['sale_date'], infer_datetime_format=True)
    
    # Set date as index
    df = df.set_index('sale_date')

    # Creating date columns
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    
    # Total sales column
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df

#------------------------------------------------------------------------------------------------------------

def prep_sales(df):
    
    '''
    Intakes sales df and preps it by coverting to datetime dtype and setting it as the 
    index. Creates month, day of week, and total sales columns.
    '''
    
    # Converting to datetime type
    df['sale_date'] = pd.to_datetime(df['sale_date'], infer_datetime_format=True)
    
    # Set date as index and sort 
    df = df.set_index('sale_date')
    df = df.sort_index()

    # Creating date columns
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_of_week
    
    # Total sales column
    df['total_sales'] = df['sale_amount'] * df['item_price']
    
    return df

#------------------------------------------------------------------------------------------------------------

def prep_ops(df):


    # Format date to datetime dtype
    df['Date'] = pd.to_datetime(df.Date)

    # Set date as index
    df = df.set_index('Date')
    df = df.sort_index()

    # Create month and year columns
    df['month'] = df.index.month
    df['year'] = df.index.year

    return df

#------------------------------------------------------------------------------------------------------------