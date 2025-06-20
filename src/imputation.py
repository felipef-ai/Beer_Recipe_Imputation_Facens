import pandas as pd
from sklearn.impute import KNNImputer

def imput_boilgravity(df):
    df['BoilGravity'] = df['BoilGravity'].interpolate(method='linear')
    return df

def imput_mashthickness(df):
    df['MashThickness'] = df['MashThickness'].fillna(
        df['MashThickness'].rolling(window=5, min_periods=1).mean()
    )
    df['MashThickness'] = df['MashThickness'].fillna(df['MashThickness'].median())
    return df

def imput_knn(df, cols):
    knn_data = df[cols]
    imputer = KNNImputer(n_neighbors=5)
    result = imputer.fit_transform(knn_data)
    df[cols] = result
    return df

def imput_categorical(df):
    df['Style'] = df['Style'].fillna(method='ffill')
    df['Name'] = df['Name'].fillna(method='ffill')
    df['PrimingMethod'] = df['PrimingMethod'].fillna(method='bfill').fillna('Unknown')
    df['PrimingAmount'] = df['PrimingAmount'].fillna(method='bfill').fillna('0.0')
    return df

def imput_userid(df):
    df['UserId'] = df['UserId'].fillna(method='bfill')
    df['UserId'] = df['UserId'].fillna(df['UserId'].mode().iloc[0])
    return df