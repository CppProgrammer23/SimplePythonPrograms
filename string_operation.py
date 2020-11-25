#--no-warn-script-location

########### STRINGS #############
import math
import re
import string

def midStr(s):
    print('the original string is: '+s)
    print('the new substring is: '+s[len(s)//2 -1 : (len(s)//2 -1)+3])


#midStr('JhonDipPeta')

def apTwoStr(s,s1):
    print('the append string is: '+s[0:len(s)//2]+s1+s[len(s)//2+1:len(s)])
#apTwoStr('Hello', 'World')

def fMe(s,s1):
    print('the new string is: '+s[0]+s1[0]+s[len(s)//2]+s1[len(s1)//2]+s[len(s)-1]+s1[len(s1)-1])
#fMe('America', 'Japan')

def lowFirst(s):
    sLow=''
    sUp=''
    for i in s:
        if (i<'z' and i>'a'):
            sLow+=i
        else:
            sUp+=i
    print('the new word is: '+sLow+sUp)
#lowFirst('eRiuTP')

def charSymbolDigits(s):
    cChars=0
    cDigits=0
    cSymbol=0
    for i in s:
        if i.islower() or i.isupper():
            cChars+=1
        elif i.isnumeric():
            cDigits+=1
        else:
            cSymbol+=1
    print('This string contains: ',cChars,' characters, ',cDigits,' digits and ',cSymbol,' Symbols')
#charSymbolDigits('aehf88461%@')


def mixedStr(s,s1):
    s1=s1[::-1]
    sRes=''
    if len(s)>len(s1):
        for i in range (0,len(s1)):
            sRes+=s[i]+s1[i]

    print('the result is: ',sRes)
#mixedStr('Abc', 'Xyz')


def bal(s,s1):  #psition doesn't matter here
    c=0
    if len(s)>len(s1):
        print('Cannot do the job')
    else:
        for i in s:
            for j in s1:
                if i==j:
                    c+=1
    if c==len(s):
       return True
    return False

#print(bal('ui','gruiz'))


#############################################
def occUsa(s):
    sRes=''
    c=0
    for i in range (0,len(s)):
        if (s[i]=='U' or s[i]=='u'):
            sRes+=s[i:i+3]
            if(sRes.lower()=='usa'):
                c+=1
                sRes=''
    print('the ocuurance of USA is/are: ',c)
#occUsa('Hello USA, so usa is great, right?')
def ocUs(s):
    substr='USA'
    c = s.lower().count(substr.lower())
    print('the oc are: ',c)
#ocUs('Hello USA, so usa is great, right?')
###############################################

def findDigit(s):
    sum=0
    ave=0.0
    markList=[int(n) for n in re.findall(r'\b\d+\b',s)]
    for i in markList:
        sum+=i
    ave = sum/len(markList)
    print('the sum is: ',sum,' and the average is: ',ave)
#findDigit('English = 78 Science = 83 Math = 68 History = 65')

def ocWord(s):
    cDict=dict()
    for i in s:
        c = s.count(i)
        cDict[i]=c
    print(cDict)
#ocWord('Apple')

def revStr(s):
    s = s[::-1]
    print('the reversed string is: ',s)
#revStr('Hello')

def indxEmma(s):
    index = s.rfind('Idris')
    return index
#print(indxEmma('Idris is a data scientist who knows Python. Idris works at google.'))

def splStr(s):
    s = s.split(' ')
    print(s)
#splStr('Idris is a data scientist')

l=['str', 'Idris', 'er','', 'mimo','',None]
new_l=list(filter(None, l))
#print(new_l)


s = '@/Idris is @ a developer0'
z=string.punctuation
s = s.translate(s.maketrans('','',z))
#s = re.sub(r'[0-9]',r'',s)
s = s.translate(s.maketrans('','',string.digits))
#print(s)


s = 'I am 25 years and 10 months old'
s = re.sub(r'[^0-9]',r'',s)
#print(s)


s = 'Idris25 is Data scientist50 and AI Expert'
myList=[]
temp=s.split()
for i in temp:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        myList.append(i)
#print(myList)

str1 = '@/Idris is @ a developer0'
for i in string.punctuation:
    str1 = str1.replace(i, '#')
for i in string.digits:
    str1 = str1.replace(i,'#')
print(str1)