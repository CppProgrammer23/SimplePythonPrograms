
######### DATA STRUCTURE #########

################################
#Create a third list by picking an odd-index element from the first list and even index elements from second
l1=[1,8,6,7,3]
l2=[6,5,79,8,12]

l3=l1[1::2] #odd positions
l4=l2[0::2] #even positions

#print(l3+l4)
###############################
#remove the element at index 4 and add it to the 2nd position and also, at the end of the list
myList=[14,8,3,9,10,56,89]
m = myList.pop(4)
myList.insert(2,m)
myList.append(m)
#print(myList)
###############################
#slice a list into a 3 equal chunks and rever each list
lis=[1,8,3,9,7,5,6,15,84]
l1=lis[0:len(lis)//3]
#print(l1); print(l1[::-1])
l2=lis[len(lis)//3:2*len(lis)//3]
#print(l2); print(l2[::-1])
l3=lis[2*len(lis)//3 :]
#print(l3); print(l3[::-1])

###############################
#count the occurrence of each element and create a dictionary to show the count of each element
def ocValue(l):
    myDict=dict()
    for i in l:
        c=l.count(i)
        myDict[i]=c
    print(myDict)
#ocValue([1,8,4,2,9,3,8,4,3,8])
#################################

# create a set such that it shows the element from both lists in the pair

l1=[1,8,3,7,15]
l2=[8,9,4,36,7]
mySet=set(zip(l1,l2))
#print(mySet)
###################################

#find the intersection and remove those elements from the first set
s={4,7,23,9}
s1={4,1,9,3}
sRes=s.intersection(s1)
for i in sRes:
    s.remove(i)
#print(sRes)
#print(s)
#####################################

#Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set
s={4,8,6}
s1={1,3,4,9,6,8,7}
if s.issubset(s1):
    #print('is subset')
    s.clear()
if s1.issuperset(s):
    print('is upperset')
###################################

#if a given element already exists in a dictionary as a key’s value if not delete it from the list

num=[14,25,10,45,19]
myDic={'Jelly':45, 'Paul':10, 'Idris':25}
num[:]=(item for item in num if item in myDic.values())
#print(num)
###################################

#get all values from the dictionary and add it in a list but don’t add duplicates
myDict={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44}
n=[]
[n.append(item) for item in myDict.values() if item not in n]
#print(n)
###################################

#Remove duplicate from a list and create a tuple and find the minimum and maximum number
l=[1,8,6,47,98,8,4,8,2,6]
n=[]
[n.append(item) for item in l if item not in n ]
myTuple=tuple(n)
print(myTuple)
print('min: ',min(myTuple))
print('max: ',max(myTuple))