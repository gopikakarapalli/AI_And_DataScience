'''
read text file into a dataframe
filename='file path'
df=pd.read_csv(filename)==> it reads the data file
print(df)
=> CSV stands for "comma-separated values
=>tSV stands for "tab-separated values
'''
print('5) data reading form file:-')
#==================================
import pandas as pd
df=pd.read_csv('E:\My Learning\Computers & Programming\Python\Mypython\Python Scripts\libs\Pandas_python\pandasdatafile1.csv')
print(df)
#         ---------    both or same      -----------

df1=pd.read_csv('../Pandas_python/pandasdata1.txt',sep=",")# ../ is takes current dir
print(df1)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

print('6) data Munging (data conversion):-')#to convert txt,xhtml,xll,ruby,php,xst,json,py, etc.,,
#=========================================

df2=pd.read_csv('../Pandas_python/pandasdatafile1.csv')
df2.to_html('pandasfile1htmlFile.html')#get html file with file name in current working dir(fillname.formate)
#------------------------------------------------------------------------------------------------------------------------------------------------------------

print('7)concatenation :------------------------------------------------->')
#=======================
df3=pd.read_csv('../Pandas_python/PandaasDatasFile2.csv')
df4=pd.read_csv('../Pandas_python/PandaasDatasFile2.csv')
df5=pd.read_csv('../Pandas_python/PandaasDatasFile2.csv')
print('data set df3=df4=df4 :\n',df3)
row_concat=pd.concat([df3,df4,df5]) # axis = 0\1 ==>row or index\col & default axis=0
print('row concatenation axis=default  :-\n ',row_concat)
col_concat=pd.concat([df3,df4,df5],axis = 1)
print('col concatenation axis=1  :-\n ',col_concat)

print('col_concat[A]:\n',col_concat['A'])
 
col_concat.to_csv('concatenated.csv')# to save concatenated file (fiename.formate)
col_concat.to_csv('concatenated.doc')
#------------------------------------------------------------------------
print('to remove NaN in coming data file')
df6=pd.read_csv('../Pandas_python/PandaasDatasFile3.csv',
                keep_default_na=False,
                na_values=[' '])
print(df6)

print('type casting')
#====================
df7=pd.read_csv('../Pandas_python/pandasdatafile1.csv')
print(df7.dtypes)
print('after type casting')
df7['colul']=df['colu1'].astype(float)
df7['c']=df['colu1'].astype(float)#add new ro with typeecast
print(df7.dtypes)

print('read excel file')

'''
python3 -m pip install xlrd # some time get a error in mult sheet so it required to import
'''
import xlrd # note req for jupyter note,spy,some IDL eyc
import pandas as pd
df8=pd.read_excel('../Pandas_python/pandasdata1.xlsx')
print(df8)
'''
print('read and write  multple file')


df9=pd.ExcelFile('pandasdata1.xlsx')
df10=pd.read_excel(df9,'sheet2')
print(df10)

df10.to_excel('./pandasdata1py.xlsx',sheet_name='writ by py')

'''

