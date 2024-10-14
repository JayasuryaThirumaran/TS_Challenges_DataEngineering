# data_engineering/transform.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def transform_data(df):
    """
    Transforms the extracted data by cleaning and preparing it for loading.

    Parameters:
    - df (pd.DataFrame): Extracted data.

    Returns:
    - pd.DataFrame: Transformed data.
    """
    #TODO
     return df

def handle_missing_values(df):
    """
    Handles missing values in the DataFrame by dropping rows with any missing data.

    Parameters:
    - df (pd.DataFrame): Data to clean.

    Returns:
    - pd.DataFrame: Cleaned data.
    """
    #TODO
     return df

def normalize_data(df, numerical_cols):
    """
    Normalizes specified numerical columns using Min-Max scaling.

    Parameters:
    - df (pd.DataFrame): Data to normalize.
    - numerical_cols (list): List of numerical column names to normalize.

    Returns:
    - pd.DataFrame: Data with normalized columns.
    """
   #TODO
    return df

# Optional: Encode Categorical Columns
def encode_categorical(df, categorical_cols):
    """
    Encodes categorical variables using one-hot encoding.

    Parameters:
    - df (pd.DataFrame): Data to encode.
    - categorical_cols (list): List of categorical column names.

    Returns:
    - pd.DataFrame: Data with encoded categorical variables.
    """
    #TODO
    return df
