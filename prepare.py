import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # import needed for the train, test, split functions.

# Function for cleaning Iris Database data
def prep_iris(df):
    ''' 
        This functions cleans the data by dropping unnecesssary columns, simplifying column names,
        creating dummy columns, and concatenating the dummy df to the main df.
    '''
    df = df.drop(['measurement_id', 'species_id'], axis=1)
    df = df.rename(columns={'species_name': 'species'})
    the_dummy = pd.get_dummies(df[['species']], dummy_na=False, drop_first=False)
    df = pd.concat([df, the_dummy], axis=1)
    return df

# Function for cleaning Titanic data
def prep_titanic(titanic):
    ''' 
        This functions cleans the data by dropping unnecesssary columns, filling null values,
        creating dummy columns, and concatenating the dummy df to the main df.
    '''
    titanic= titanic.drop(['class', 'deck','age', 'passenger_id','embarked'], axis=1)
    titanic['embark_town'] = titanic['embark_town'].fillna(value='Southhampton')
    them_dummies = pd.get_dummies(titanic[['sex', 'embark_town']], dummy_na=False)
    titanic = pd.concat([titanic, them_dummies], axis=1)
    return titanic

# Function for cleaning Telco data
def prep_telco(telco):
    ''' 
        This functions cleans the data by dropping dupes, dropping unnecesssary columns,
         simplifying column names, creating dummy columns, and concatenating 
         the dummy df to the main df.
    '''
    telco = telco.drop_duplicates()
    telco = telco.drop(['customer_id','payment_type_id','internet_service_type_id', 'contract_type_id'], axis=1)
    telco_dummies = pd.get_dummies(telco[['contract_type','internet_service_type','payment_type']], dummy_na=False, drop_first=True)
    telco = pd.concat([telco, telco_dummies], axis=1)
    return telco





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
