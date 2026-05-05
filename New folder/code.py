import pandas as pd 
#df=pd.read_csv("Dataset.csv",usecols=["City","Restaurant ID"])
df=pd.read_csv("Dataset.csv")
# print(df.isna())
# #print(df.head())

# print(df.isna().sum())

print(df[df["City"]=="Makati City"])

