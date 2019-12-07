'''
seaborn:
--------
-> seaborn is a statistical plotting library in python programming language.
   it has beautiful default styles and it also works well with pandas data
   frame objects.like dist ploat,joint ploat,pair plot,rug plot..,
-> to install seaborn:--> conda instal seaborn (or)
             type in cmd---> pip install seaborn
'''
import seaborn as sns
import pandas as pd

df = pd.read_csv("./battles.csv")
#print(df.info)
#print(df.head(4))
#print(df.dtypes)

#sns.set_style("whitegrid")

bar = sns.barplot(x="year",y="major_death",data=df)

