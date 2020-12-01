import pandas as pd
from sklearn.tree import DecisionTreeClassifier as dtc #to train the model
from sklearn.model_selection import train_test_split as tts #to split train and test
from sklearn.metrics import accuracy_score as asc #to calculate the accuracy

my_data=pd.read_csv('music.csv')
input=my_data.drop(columns=['genre'])
output=my_data['genre']
X_train, X_test, y_train, y_test = tts(input,output, test_size=0.2) #it returns a tuple of size 4
my_model = dtc()
#my_model.fit(input,output)
my_model.fit(X_train,y_train) #training data
#pred=my_model.predict([[21,1],[34,0]])
print(X_test)
pred=my_model.predict(X_test)

accuracy = asc(y_test,pred)
print(pred)
print('the accurancy is: ',accuracy)
