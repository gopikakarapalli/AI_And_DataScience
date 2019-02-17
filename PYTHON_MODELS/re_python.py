'''
 Regular expression (re) :
 =========================
--> This module provides regular expression matching operations similar to
 those found in Perl. Both patterns and strings to be searched can be
 Unicode strings as well as 8-bit strings
-->Python’s raw string notation for regular expression patterns;
    backslashes are not handled in any special way in a string literal
    prefixed with 'r'. So r"\n" is a two-character string containing '\' and 'n',
    while "\n" is a one-character string containing a newline.
-->ually patterns will be expressed in Python code using this raw string notation
'''
import re
import sys
print(r"gopi \n kakarapall") # backslashes are not handled in any special  way in a string literal prefixed with 'r'
text_to_search ='''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
abc
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T \n

'''
count=0 
pattern = re.compile(r'abc')#(r'start', re.I)re.I=re.IGNORECASE it 's ignore case apl
#pattern = re.compile(r'cab')# in cass no match thre is no error
matches = pattern.finditer(text_to_search)#(sentence)-->to find the spen index[start : end-1]

for match in matches:
       count+=1
       print(match)#returns spen index(start ,end-1)
       print("start index",match.start())#gives start index
       print("end-1 index",match.end())#gives end-1 index
       print("start index",match.group())# ti returent which match group
print(match.span())
print('no.of times',count)# gives no.of times
print(text_to_search[1:4])
print(text_to_search[match.start():match.end()])

print('.---------------------------------------------------------------------')

pattern = re.compile(r'.')#(Dot). In the default mode, this matches any character except \n
matches = pattern.finditer(text_to_search)#
for match in matches:
       print(match)

print('\.--------------------------------------------------------------------')
       
pattern = re.compile(r'\*')# \  it matchs escapes special characters
matches = pattern.finditer(text_to_search)#
for match in matches:
       print(match)



print("------------------findin spen index (predefind character class)------")
# note:
'''
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)
'''
pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)#
for match in matches:
       print('check',match)

print('-----------finding span index of boundarys--------------------------')
'''

\b      - Word Boundary (not end pattern) 
\B      - Not a Word Boundary (end pattern)
^       - Beginning of a String
$       - End of a String
---------------------(character class)------------------------------
[]      - Matches Characters in brackets 
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

'''
pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
for match in matches:
       print('check boundarys',match)

sentence = 'start a setence and then bring it an end'

pattern = re.compile(r'^start')
matches = pattern.finditer(sentence)
for match in matches:
       print('setence boundarys',match)

pattern = re.compile(r'^it')# it s not match because it is not a Beginning of sring
matches = pattern.finditer(sentence)
for match in matches:
       print('string boundarys',match)

pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches:
       print('string boundarys',match)
print('---------------------forming pattern----------------------------')

pattern=re.compile(r'\d\d\d')
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)
print('-----------------------------------------------------------------------------')

pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d')
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)
print('----------------------[Matches Characters in brackets] -------------------------')

pattern=re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d')
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)

#EX 2:
pattern=re.compile(r'[89]00[-]\d\d\d[-]\d\d\d')
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)
#EX 3:
pattern=re.compile(r'[A-D]')# RETURN in b/w [range] range like a-b,A-Z,0-9, a-bA-Z0-9 
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)
print('---------------------[Matches Characters not in brackets] ---------------------')

pattern=re.compile(r'\d\d\d[^-]\d\d\d[^-]\d\d\d')
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)
#Ex2:

pattern=re.compile(r'[^c]at')
matches=pattern.finditer('cat bat rat')
print(pattern)
for match in matches:
        print(match)


print('--------------------------  Quantifiers  --------------------------------')
'''
Quantifiers:used to specify the no.of occurrences to match
*       - 0 or More
+       - 1 or More
?       - 0 or One (optional)
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
'''
#no1
pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)
#no2
pattern=re.compile(r'Mr\.')
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)

#no3
pattern=re.compile(r'Mr\.?')# how many pattern
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)

#no4
pattern=re.compile(r'Mr\.?\s[A-Z]')# how many pattern
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)

#no4
pattern=re.compile(r'Mr\.?\s[A-Z]\w+')# how many pattern
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)

#no5
pattern=re.compile(r'Mr\.?\s[A-Z]\w*')# how many pattern
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)

#no6
pattern=re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')# how many pattern
matches=pattern.finditer(text_to_search)
print(pattern)
for match in matches:
        print(match)
print('---------------------email pro-----------------------------------------')
#ex :1
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
print('-------------------------- group -----------------------------------------')
#ex :2
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # ? it saw optional
matches = pattern.finditer(urls)#(group 0)(G1)( G2)
for match in matches:
     print(match)
     print('match group ->',match.group(2))

print('---------------------------  sub & subn -----------------------------------------')
    
subbed_urls = pattern.sub(r'\3\2', urls)#it returns sub pattern(r'\required sub group,source file)

print('sub group : ',subbed_urls)
#                       -------  or    ------
s=re.sub('\d','##','a7d7d8f9')#(pattern,replace,target)it replace required value or pattern
                               # it returns only result
print(s)

s=re.subn('\d','##','a7d7d8f9')#(pattern,replace,target)it replace required value or pattern
#                            and returns tupul with (result,no.of times replace)
print(s)
print(type(s))
print('---------------------match function-----------------------------------')

sentence=('match function match only in Beginning ')
pattern= re.compile(r'match')
matches=pattern.match(sentence)
print(matches)
pattern= re.compile(r'only')
matches=pattern.match(sentence)
print('not begin word',matches)

print('---------------------fullmatch function---------------------------')

sentence=('full match function find totall given match matched or not')
matches=re.fullmatch(sentence,
              'full match function find totall given match matched or not')
print(matches)
print('---------------------search function-----------------------------')

sentence=('search function to search a pattern inenter string ')
pattern= re.compile(r'string')
matches=pattern.search(sentence)
print(matches)

re.search('string',sentence)
print(matches)

pattern= re.compile(r'no word')
matches=pattern.search(sentence)
print('no word in string',matches)


print('---------------------------- findall --------------------------------')
nameage='''
Gopi is 26 and Orggopi is 27 Kgopl is 28 Satya is 29 and Anu is 26
'''
ages =re.findall(r'\d{1,3}',nameage)
names=re.findall(r'[A-Z][a-z]*',nameage)
agedict={}
x=0
for eachname in names:
        agedict[eachname]=ages[x]
        x+=1
print(agedict)
print('------------------    split   -----------------------')
l=re.split('-','10-04-2018')#  split the data with wrt pttern
print(l)
print('------------------    flgs   -----------------------')
sentence=('search function to search a pattern inenter string ')
pattern= re.compile(r'STRing',re.IGNORECASE)#re.IGNORECASE IT 's ignore case apl
matches=pattern.search(sentence)
print(matches)

import pandas
df=pandas.DataFrame(list(range(10)))

i='''
27-07-1992
27-07-1992
27-07-1995
27-07-1994
27-07-1993'''


P=re.compile(r'(\d\d)\-([0|0-9]\d)\-(d\d\d\d)')
df['fd']= P.sub(r'\1\2',i)
print(df['fd'])



'''
match()
fullmatch()
search()
findall()
finditer()
sub()
sudn()
split()
compile()
'''


