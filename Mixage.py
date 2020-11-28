def fib(x):
    if x==1 or x==0:
        return 1
    else:
        return fib(x-1)+fib(x-2)
#print(fib(6))
myFibList=[]
for i in range(10):
    myFibList.append(fib(i))
#print(myFibList)

###############################################################
#def rmv_dupl(myList):
#    new_list=[]
#    [new_list.append(x) for x in myList if x not in new_list]
#    return new_list
#print(rmv_dupl([1,8,6,3,1,8,4,9,3]))
def rmv_dupl(myList):
    new_list=[]
    for i in myList:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    return new_list
#print(rmv_dupl([1,8,6,3,1,8,4,9,3]))
############################################################

#palindrome
#def is_palindrome(str):
#    l=list()
#    l_rev=list()
#    for i in str:
#        l.append(i)
#    mystr=str[::-1]
#    for i in mystr:
#        l_rev.append(i)
#    for i in range(len(l)):
#        if l[i]!=l_rev[i]:
#            return False
#    return True
def is_palindrome(str):
    l=list()
    l_rev=list()
    for i in str:
        l.append(i)
    mystr=str[::-1]
    for i in mystr:
        l_rev.append(i)
    for i in range(len(l)):
        if l.pop()!=l_rev.pop():
            return False
    return True
#print(is_palindrome('rerer'))
################################################

#in 1 line store the even number of a list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if not x%2]
#print(b)


#reverse a phrase 
def reverse_word(str):
    l=str.split(' ')
    str = ' '.join(l[::-1])
    return str
#print(reverse_word('hello I\'m here'))
#################################################

#
def binary_search(myList,number):
    myList=sorted(myList)
    mid=len(myList)//2
    while mid>=0 and mid<len(myList)-1:
        if number<myList[mid]:
            mid//=2
        elif number>myList[mid]:
            mid+=(len(myList)-mid)//2
        else:
            return True
    return False
#print(binary_search([4,8,6,71,2],5))
##########################################

file = open('name.txt','r')
line = file.readline()
myDict=dict()
myL=[]
while line:
    #line.strip()
    line = line.replace('\n','')
    if line not in myL:
        myL.append(line)
    line=file.readline()
file.close()
with open('name.txt','r') as f:
    linee=f.readline()
    while linee:
        #linee.strip()
        linee = linee.replace('\n','')
        if linee in myDict:
            myDict[linee]+=1
        else:
            myDict[linee]=1
        linee=f.readline()
#print(myL)
#print(myDict)
f.close()
#print(myDict['Lea'].values())
############################################

def maxi(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            if c>b:
                return c
            else:
                return b
    else:
        if b>c:
            return b
        else:
            if a>c:
                return a
            else:
                return c
#print(maxi(7,5,6))
###############################################

#Count elements in a data structure
from collections import Counter
myTuple= 'Jan','Feb','Jan','March','Feb','June','July','Jan','August','Jan','September'
#print(type(myTuple))
dictionary=Counter(myTuple)
print(type(dictionary))
print('there are {} Jan in the tuple'.format(dictionary['Jan']))
#print(dictionary)
############################################

#how to set precision using format, the C-style precision and round function
#f=float(input('input a float: '))
#d=float(input('input a 2nd float: '))
#print('{0:.2f}'.format(f*d))
#print('%.2f'%(f*d))
#print(round(f*d,2))
############################################"

#def count_letter(str):
#    mdict=dict()
#    for i in str:
#        c=str.count(i)
#        mdict[i]=c
#    return mdict
#print(count_letter('hello'))
def count_letter(str):
    mdict=dict()
    for i in str:
        if i in mdict:
            mdict[i]+=1
        else:
            mdict[i]=1
    return mdict
#print(count_letter('hello'))
#############################################

def verify_list_size(l):
    try:
        s=l[0]
    except IndexError as e:
        return True
    else:
        return False
#print(verify_list_size([1]))
#######################################


def not_there(s,s1):
    c=s1.difference(s)
    print(c)
#not_there({'h','y','t','e'},{'p','k','w','y','h'})
#####################################

def trans_to_upper(str):
    s=''
    for i in str:
        if ord(i)<123 and ord(i)>96:
            s+=chr(ord(i)-32)
        else:
            s+=i
    return s
#print(trans_to_upper('hello'))
#######################################

def swapLetter(str):
    s=''
    for i in str:
        if i.isupper():
            s+=i.lower()
        else:
            s+=i.upper()
    return s
#print(swapLetter('HeLlo'))
#print('hEllO'.swapcase()) # in one line
########################################

#extract only words its length is le to 4
def extract(s):
    mList=s.split()
    l=[item for item in mList if len(item)<=4]
    return l
#print(extract('Hello there I\'m waiting for you'))
#########################################

def maxi1(a,b):
    return a if a>b else b
print(maxi1(7,8))