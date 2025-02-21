import pandas as pd

dataframe=pd.read_csv('nba.csv')
print(dataframe.head())
print("Number of columns",len(dataframe.columns))
print("Number of rows",len(dataframe))
print(dataframe.columns)
array=list()