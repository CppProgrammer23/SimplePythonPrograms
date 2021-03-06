from statistics import mean
import matplotlib.pyplot as plt
class student:
    def __init__(self, name, age, iden, lMark):
        self.name=name
        self.age=age
        self.iden=iden
        self.lMark=lMark
    def calcAve(self):
        return mean(self.lMark)
    def disInfo(self, obj):
        print("the name is: ",obj.name)
        print("the age is: ",obj.age)
        print("the identity is: ",obj.iden)
        print("the marks are: ", *self.lMark) #*[i for i in obj.lMark]
    def addStudent(self, n, a, i, l):
        ob=student(n,a,i,l)
        ls.append(ob)
        return True
    def searchStudent(self, _val):
        for i in range (len(ls)):
            if ls[i].age==_val:
                return i
    def removeStudent(self, _val):
        i = self.searchStudent(_val)
        del ls[i]
    def showResult(self):
        for i in range (len(ls)):
            lis=[]
            for j in range(1,len(self.lMark)+1):
                lis.append(j)
            plt.scatter(lis,ls[i].lMark, label=ls[i].name)
            plt.legend()
            #plt.plot(self.calcAve())
            #plt.axis("tight")
            #plt.ylabel(ls[i].name)
            #plt.show()
    def passOrFail(self, obj):
        if obj.calcAve()>=10:
            print("The student "+obj.name+" passes")
        else:
            print("The student "+obj.name+" fails")

ls=[]
s=student("Paul", 23,14, [15,16,17,20,12])
ls.append(s)
added = s.addStudent("Van", 20, 12, [12,18,14,16])
if added:
    print("added success")
print("the student num: ",s.searchStudent(23)+1, " was found")
s.showResult()
plt.show()
for i in range (len(ls)):
    print(ls[i].calcAve())
for i in range(len(ls)):
    s.disInfo(ls[i])
for i in range (len(ls)):
    s.passOrFail(ls[i])
print("after deletion: ")
s.removeStudent(20)
for i in range (len(ls)):
    s.disInfo(ls[i])
