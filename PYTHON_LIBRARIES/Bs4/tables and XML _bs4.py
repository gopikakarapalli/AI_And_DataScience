import bs4 as bs
import urllib.request
import sys

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Demographics_of_India').read()
#print(source)
soup = bs.BeautifulSoup(source,'html.parser')# use lxml or html

table = soup.table
table = soup.find('table')
table_rows= table.find_all('tr')

#print(table_rows)

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

print('using pandas')
import pandas as pd

dfs = pd.read_html('https://en.wikipedia.org/wiki/Demographics_of_India',header=0)
for df in dfs:
    print(df)


#xmnls (sitemap):
print('------------------sitemap--------------------------------')


import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source,'xml')

for url in soup.find_all('loc'):
    print(url.text)


