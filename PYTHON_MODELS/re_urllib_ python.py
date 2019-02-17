'''
Web scraping: HTML pages --> web scraping technology --> data file excle
-------------------------
scrap all the phone numbers a webpage using Regular Expressions
urllib is a package that collects several modules for working with URLs:

urllib.request -->for opening and reading URLs
urllib.error   --> containing the exceptions raised by urllib.request
urllib.parse  --> for parsing URLs
urllib.robotparser -->for parsing robots.txt files
to install :pip3 install urllib3
           :apt-get install python3-urllib3
from urllib.request import urlopen
help(urlopen)

'''
import re
'''

import urllib.reguest

url='http://www.summet.com/dmsi/html/codesamples/addresses.html'
response = urllib.request.urlopen(url)
html=response.read()
htmlStr=html.decod()
pdata = findall('\(d{3}\d{3}-\d{4}',htmlStr)

for item in pdata:
        print(item)

'''
import urllib
import urllib.request
print(help(urllib))

url=['http://google.com','http://rediff.com']

for s in url:
        print('searching...',s)
        u=urllib.request.urlopen(s)#to open url
        text=u.read()# to read data
        title=re.findall("<titlt>.*</title>",str(text),re.IGNORECASE)# to get title
        print(title[0])

#------------------------------------------------

url=urllid.request.urlopen("http://www.redbus.in/info/contactus")
text=u.read()
numbers=fe.findall('[0-9]{3}[-][0-9]{8}',str(text))
for n in numbers:
        print(n)
        
#[0-9]{3}[-][0-9]{8} --> 110-111111  or
# [0-9]{3}[-][0-9]   -->110-111111777777..


'''
#----------------------------------------------------------------------------
print('----------------to read file data wrt  patten -------------------------')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
with open('./emaildata.txt','r',encoding='utf-8') as f:#utf-8 is acsii encoder
        contents=f.read()
        matches =pattern.finditer(contents)
for match in matches:
        print(match)
'''
#----------------------------------------- or ----------------------------------
f1=open('./logging_python.txt','r')
f2=open('re_logging_python.txt','wr')
for line in f1:
        list=re.findall('[0-9]',line)
        for numder in list:
                f2.writ(numder,"\n")
f1.close()
f2.close()



