import bs4 as bs
import urllib.request
import sys

source = urllib.request.urlopen('https://stackoverflow.com/questions/24398302/bs4-featurenotfound-couldnt-find-a-tree-builder-with-the-features-you-requeste').read()
#print(source)

soup = bs.BeautifulSoup(source,'lxml')# use lxml or html

# title of the page
print('title',soup.title)# any html tag eg: boby,script,nav,div etc

# get attributes:
print('title name',soup.title.name)

# get values:
print('title string',soup.title.string)#ro text

# beginning navigation:
print('title.parent.name:',soup.title.parent.name)
print('--------------------1------------------------')

# getting specific values:#p =paragraph
print('soup.p',soup.p)

print('find_all (P)',soup.find_all('p'))
print('---------------------2--------------------------')
      
for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))
    #print(str(paragraph.text.strip()))#strip it removies , \n
print('--------------------3---------------------------')    
for url in soup.find_all('a'):#a =all
    print('href :',url.get('href'))


print(soup.get_text())

print('-----------------------div class--------------------')

for div in soup.find_all('div', class_='js-voting-container grid fd-column ai-stretch gs4 fc-black-200'):
    print(div.text)      #  (.div,class_='body')  etc ..


'''
for url in nav.find_all('a'):
    print(url.get('href'))

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)
'''

