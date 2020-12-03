import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn import linear_model

my_data=pd.read_csv('student-mat.csv',sep=';')
test=my_data[['G1','G2','G3','failures','absences','studytime']]

X = my_data[['G1','G2','failures','absences','studytime']]
row21_25 = test.head(25)
print('#'*10,' Real data ','#'*10)
print(row21_25.tail(5))
print('#'*10,' Machine learning task ','#'*10)
y = my_data['G3']
X_train, X_test, y_train, y_test = tts(X,y,test_size=0.2)
my_model=linear_model.LinearRegression()
my_model.fit(X,y)
pred=my_model.predict([[12,15,0,0,1]])
pred1=my_model.predict([[10,9,0,2,3]])
print('{0:.2f}'.format(pred[0]))
print('%.2f'%pred1[0])

#Accuracy 
my_pred=my_model.predict(X_test)
accuracy=my_model.score(X_test,y_test)
print('the accuracy is: {0:.2f}%'.format(accuracy*100))
#coef and intercept
print('Coef: ',my_model.coef_)
print('Intercept: ',my_model.intercept_)