import pandas as pd


file1 = "salarios.csv"

df1 = pd.read_csv(file1)

print(df1.head())
