import pandas as pd
print('spread row into column with pivot')
#========================================

df1=pd.read_csv('.\pivot.csv')

df2=df1.pivot(index='data',
              columns='type',
              values='value')
print(df1,'\n',df2)

print('stack / unstack')# it displayes like dict 
#=======================

df3=df1.stack() # gives all data in Data form wrt columns labels
print(df3)
print()
df3=df1.unstack()# gives all data in Data form wrt row index labels
print(df3)


print('melt')
#============

df4=pd.melt(df1,
            id_vars=['data'],
            value_vars=['type','value'],
            value_name='observation')
print(df4)


