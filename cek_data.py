import pandas as pd 

df = pd.read_csv("dfTransjakarta.csv", sep=',')

print(df.shape)
print(df.head())

#cek kesehatan data
df.info()
