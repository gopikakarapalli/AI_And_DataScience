'''
pandas :
--------
-> pandas is a software library written for python programming lanruage for
   for data manipulation and analysis.
-> pands is an open source library built on top of numpy,scipy & matplotlib. it is used for data
   manipulation and analysis.pands is well sited for different kinds of data.
-> it is used for data clening.
-> pandas is well suited for many different kinds of data:
     ->tabular data with heterogeneously type columns.
     ->ordered and unordered time series data.
     ->arbitrary matrix data with data with row and column ladels
     ->any other form of observatiol/ statisitical data sets.the data actually need not be
        labeled at all to be placed into a pandas data structure
-> series is a one dimensional array capable of hold any data type 
-> dataframe is a main object in pandas. it is used to represent data wite rows and columns(2D)
  (tabular or excel spreadsheet like data)
  
->to install: ---> conda install pandas     (or)
    type in cmd--> pip install pandas

                     
''' 
import pandas as pd
#s=pd.series([3,-5,4],index=[0,1,2])
#print(s)

df=pd.DataFrame(
        [['jan',56,56,56,66,00],
         ['feb',56,56,56,66,00],
         ['mar',56,56,56,66,00],
         ['may',56,56,56,66,00],
         ['jun',56,56,56,66,00],
         ['dec',56,56,56,66,00]],index=[0,1,2,3,4,5],
        columns=['mon','tem','p','ws','co','f'])
print(df)

print(type(df))

print('ex 2')       
dataInfo={'day':[1,2,3,4,5,6],'visitors':[100,700,6000,10000,400,350],
          'bounceRate':[20,34,34,34,23,34]}
dataFrame = pd.DataFrame(dataInfo)   # it gives dataFrame py formate

print(dataFrame)
#
print('pandas operations :')
#---------------------------
print('1)slicing or sub seting the dataframe :--------------------------------------------->')

print(dataFrame.head(2),'\n') # to slicing the dataframe top row to downrow (no.of row)

print(dataFrame.tail(3)) # to slicing the dataframe down row to top row (no.of row)
print('each col call :\n',dataFrame['day'])
print('mult col call :\n',dataFrame[['day','visitors']])

#subset=dataFrame[list(range(1,2))]
#print('range call :\n',subset.head(4))
#subset=dataFrame[[1,2]]
#print('sud set with clo indx :\n',subset.head())
#
print('-- Finding data frame properties  of set &subset  ----------')

print('dataFrame \n',dataFrame)
print('shape  :-',dataFrame.shape)
print('to get last row',dataFrame.shape[0])
print('dtype  :-\n',dataFrame.dtypes)# it gives col data type wrt lable
'''
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing
'''
print('loc  :-\n',dataFrame.loc[0])# it gives row porperties [indx of row]
print('iloc  :-\n',dataFrame.iloc[0])# it gives row porperties [indx of row]
print('ix  :-\n',dataFrame.ix[0,1])# it gives row porperties [indx of row, inx col
print('ix 2:-\n',dataFrame.ix[0,'day'])
print('ix 3 :-\n',dataFrame.ix[[0,1,2],['day']])#[[row],[col]
print('to get last row :-\n',dataFrame.loc[dataFrame.shape[0]-1])
                     


print('2)joining and merging :----------------------------------------------->')
#============================
print('joining')
#----------------
df1=pd.DataFrame({'int_rate':[2,1,2,3],'ind_gdp':[50,45,45,70]},
                 index=[2001,2002,2003,2004]) #to give required index
df2=pd.DataFrame({'loe_tire_hpi':[80,90,70,60],'unemploy':[1,2,3,7]},
                  index=[2001,2002,2005,2009])
print('dataframe1 \n',df1)
print('dataframe2 \n',df2)

joined=df1.join(df2)#to join the two dataframe
print('join two dadaframe:\n',joined )


print('merging :')
#-----------------
df1=pd.DataFrame({'hpi':[80,90,70,60],'int_rate':[2,100000,2,3],'ind_gdp':[50,45,45,70]},
                 index=[2001,2002,2003,2004]) #to give required index
df2=pd.DataFrame({'hpi':[80,90,70,60],'int_rate':[2,1,2,3],'ind_gdp':[50,45,45,70]},
                  index=[2005,2006,2007,2009])
print('dataframe1 \n',df1)
print('dataframe2 \n',df2)

merge = pd.merge(df1,df2)#to merge the two dataframe (dataframe 1,dataframe 2,left_on= 'if we required comman lables',right_on=if we required comman keys')
print('merge dataframe \n',merge)

merge = pd.merge(df1,df2,on = 'hpi')
print('merge dataframe with commne keys \n',merge)
#
print('3)changing the index &column headers :-------------------------------->')

df =pd.DataFrame({'day':[2,3,4,5,6],'visi':[30,4,5,6,5],'rate':[2,3,4,5,8]})
print('dataframe \n',df)

df.set_index('day',inplace=True)# index will be replace into your required  colum data
print('changing the index \n',df) #(which lable is relpace , inplace=T\F don't show org index\ show org indxe)

df=df.rename(columns={'visi':'users.no'})#it  will be rename the old  name into new name in the colum{old name:new name}
print('changing column headers :\n',df)
#
print('4)grouping of data sets :------------------------------------------------->')

print('dataframe1 \n',df1,'\n')

print(df1.groupby('hpi')['ind_gdp'].mean())



