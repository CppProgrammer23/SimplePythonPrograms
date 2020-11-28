##### calculate the sum of 1/i! where i=0 to n ###
import time

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
print(swap(1,4)[0])
############################
def sort_(l):
    myL=[]
    while l!=[]:
        myL.append(min(l))
        l.remove(min(l))
    return myL
#print(sort_([9,5,7,3,4]))
