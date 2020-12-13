import pandas as pd
import operator

data=pd.read_csv('marks.csv')


#find the best mark in OOP
bestOOP=data['OOP'].max()
print(bestOOP)
#find the less mark in maths
minMATH=data['maths'].min()
print(minMATH)
#how many student get 16 in electrics
elec16=data[['name','electrics']][data.electrics==16]
print(elec16)
#how many subjects are present in the table
nbrSubj=data.iloc[0,1:].count()
print(nbrSubj)

###print the average of each student
#get the row's number
row,col = data.shape #it returns a tuple

#
dataName=data['name']
dataSub=data.drop(columns=['name'])

def studentInfo():
    temp=0
    dicAve=dict()
    for i in range(0,row):
        l=dataSub.iloc[i].tolist()
        
        for mark in l:
            temp+=mark
        print(data['name'][i],': {0:.2f}'.format(temp/nbrSubj))
        dicAve.update({data['name'][i]:float(temp/nbrSubj)})
        temp=0


    print ('the best average is: {0:.2f} '.format(max(dicAve.items(),key=operator.itemgetter(1))[1]),'got by {}'.format
                                                                                            (max(dicAve,key=dicAve.get)))
    print ('the best average is: {0:.2f} '.format(max(dicAve.items(),key=operator.itemgetter(1))[1]),'got by {}.'.format(max(dicAve.items(),
                                                                                                     key=operator.itemgetter(1))[0]
                                                                                                     ))

studentInfo()