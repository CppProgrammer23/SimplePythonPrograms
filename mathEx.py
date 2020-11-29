##### calculate the sum of 1/i! where i=0 to n ###
import time
from collections import deque

def fact(x):
    return 1 if x==0 or x==1 else fact(x-1)*x
def sum(n):
    res=0
    for i in range(n+1):
        res+=1/fact(i)
    return ('{0:.3f}'.format(res))
t_begin=time.perf_counter()
#print(sum(5))
t_end=time.perf_counter()
#print(t_end-t_begin)

######################################"

#sorting in reverse order

def sort_rev(s):
    s=sorted(s,reverse=True)
    return s
#print(sort_rev({1,7,3,4,9}))
#####################################

#search
def search_(l,number):
    if number in l:
        return True
    return False
#print(search_([1,7,3,4],4))
########################################

#binary search
def bin_search(l,number):
    l=sorted(l)
    mid=len(l)//2
    l=len(l)
    while mid>-1 and mid<len(l):
        if number<l[mid]:
            l=mid
            mid//=2
        elif number>l[mid]:
            mid+=(len(l)-mid)//2
        else:
            return True
    return False
#print(bin_search([1,8,7,9,10],5))
#########################################

#sort 
def swap(a,b):
    a,b=b,a
    return a,b
#print(swap(1,4)[0])
############################
def sort_(l):
    myL=[]
    while l!=[]:
        myL.append(min(l))
        l.remove(min(l))
    return myL
#print(sort_([9,5,7,3,4]))
###########################################

#
d=deque()
mDic=dict()
for i in range(10):
    d.append(7)
for i in d:
    c=d.count(i)
    mDic[i]=c
#print(mDic)
#print(d)
#########################################"

#get the min or max from a conatiner
def get_min_or_max(l,max):
    m=l[0]
    for i in range(1,len(l)):
        if not max:
            if l[i]<m:
                m=l[i]
        else:
            if l[i]>m:
                m=l[i]
    return m
#print(get_min_or_max((9,5,7,3,4),False))
#####################################

#Fib
def seq_fib(n):
    l=[1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return l
def fib(x):
    return seq_fib(x+1)[x]
#print(fib(4))
#####################################

#linear: order=1, quadratic: order=2 etc..
import matplotlib.pyplot as pt
def exc(exctractCoord,x):
    if exctractCoord[0]=='x':
        coor=x#*exctractCoord[1]
    elif exctractCoord[0]=='y':
        coor=1/x#extracexctractCoord[1]/x
    else:
        raise AssertionError('not the right key')
    return coor
def equ(n,coef,order,b):
    ln=[]
    lx=[]
    for i in range(n):
        lx.append(coef*i**order+b)
        ln.append(i)
    myPoint=exc(['x',2],coef*2**order+b)
    pt.plot(2,myPoint,'r*')
    pt.plot(ln,lx,'r-')
    pt.show()
#equ(10,2,1,2)
#################################
from itertools import filterfalse
import operator

for i in filterfalse(lambda x:x<4,[1,8,6,2,4,3]):
    print(i)