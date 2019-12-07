import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")
print(df.head())
df.to_csv("WIKI_GOOGL.csv")
