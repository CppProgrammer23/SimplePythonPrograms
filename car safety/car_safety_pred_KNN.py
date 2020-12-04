from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model, preprocessing
from sklearn.model_selection import train_test_split as tts
import pandas as pd
#import sys

my_data=pd.read_csv('car.data')

#Convert mixed data to numeric data
to_numeric = preprocessing.LabelEncoder()
buy=to_numeric.fit_transform(list(my_data['buying']))
mnt=to_numeric.fit_transform(list(my_data['mnt']))
door=to_numeric.fit_transform(list(my_data['door']))
per=to_numeric.fit_transform(list(my_data['persons']))
lb=to_numeric.fit_transform(list(my_data['lug_boot']))#0 for big, 1 for med and 2 for small
saf=to_numeric.fit_transform(list(my_data['safety']))
cls=to_numeric.fit_transform(list(my_data['class'])) #1 for good, 3 for vgood, 2 for unacc and 0 for acc

X=list(zip(buy,mnt,door,per,lb,saf))
y=list(cls)
X_train, X_test, y_train, y_test=tts(X,y,test_size=0.2)

my_model=KNeighborsClassifier()

my_model.fit(X_train,y_train)
my_pred=my_model.predict(X_test) #all the data
#print(my_pred)


pred=my_model.predict([[3,3,0,2,1,0]]) #a sample of prediction
print(pred)

#print(sys.getsizeof(y_test),sys.getsizeof(X_test),sys.getsizeof(my_pred))

for i in range(len(my_pred)):
    print('Predicted data: ',my_pred[i],' Data: ',X_test[i],' Actual: ',y_test[i])

#Accuracy
print('The accuracy is: {0:.2f}%'.format(my_model.score(X_test,y_test)*100))
