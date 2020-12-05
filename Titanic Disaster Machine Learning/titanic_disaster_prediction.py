import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler


#my_data_test=pd.read_csv('test.csv')
my_data_train=pd.read_csv('train.csv')
#mod=my_data_train.pivot_table('Survived',index='Sex',columns='Pclass').plot()
#plt.show()
###############
X=my_data_train.drop(columns=['Survived','Name','Cabin']) #we'll drop name and cabin as we don't need to know those info
y=my_data_train['Survived'] #we'll predict for the survived column

#first method to transform into numerics
to_num=preprocessing.LabelEncoder()
sex=to_num.fit_transform(list(my_data_train['Sex']))
emb=to_num.fit_transform(list(my_data_train['Embarked']))
#nam=to_num.fit_transform(list(my_data_train['Name']))
tik=to_num.fit_transform(list(my_data_train['Ticket']))
#cab=to_num.fit_transform(list(my_data_train['Cabin']))
pasId=list(my_data_train['PassengerId'])
cls=list(my_data_train['Pclass'])
age=to_num.fit_transform(list(my_data_train['Age']))
sib=list(my_data_train['SibSp'])
par=list(my_data_train['Parch'])
far=to_num.fit_transform(list(my_data_train['Fare']))

X=list(zip(pasId,cls,sex,age,sib,par,tik,far,emb))
y=list(my_data_train['Survived'])


#print(my_data_train.dtypes)
X_train, X_test, y_train, y_test=tts(X,y,test_size=0.2)
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)
my_model=LogisticRegression()
my_model.fit(X_train,y_train)
#pred=my_model.predict([[1,3,108,1,22,1,0,523,7.25,1,2]])
pred=my_model.predict([[1,3,1,22,1,0,523,7.25,2]])#sample prediction
my_pred=my_model.predict(X_test)
#print(my_pred)

#accuracy
acc=my_model.score(X_train,y_train)
print('the Logistic Regression accuracy is: {0:.2f}%'.format(acc*100))


#find the best algorithm that suited to this application in term of accuracy
def models(X_t,y_t):
    #linear regression
    lr=LinearRegression()
    lr.fit(X_t,y_t)
    scLr=lr.score(X_t,y_t)
    print('the linear regression accuracy is: {0:.2f}%'.format(scLr*100))

    #KNN 
    knn=KNeighborsClassifier()
    knn.fit(X_t,y_t)
    scKnn=knn.score(X_t,y_t)
    print('the KNN algo accuracy is: {0:.2f}%'.format(scKnn*100))

    #GaussianNB
    g=GaussianNB()
    g.fit(X_t,y_t)
    scG=g.score(X_t,y_t)
    print('the Gaussian algo accuracy is: {0:.2f}%'.format(scG*100))

    #Decision Tree Classifier
    dt=DecisionTreeClassifier()
    dt.fit(X_t,y_t)
    scDt=dt.score(X_t,y_t)
    print('the Decision Tree Classifier accuracy is: {0:.2f}%'.format(scDt*100))

    #Random Forest Classifier
    rf=RandomForestClassifier()
    rf.fit(X_t,y_t)
    scRf=rf.score(X_t,y_t)
    print('the Random Forest Classifier accuracy is: {0:.2f}%'.format(scRf*100))
models(X_train,y_train)
