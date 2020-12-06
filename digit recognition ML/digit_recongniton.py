import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
import numpy as np


my_data=pd.read_csv('train.csv')


X=my_data.drop(columns=['label'])
y=my_data['label']

X_train,X_test, y_train,y_test=tts(X,y,test_size=0.2)


def models(X_t,y_t,X_test,select=1):
    #Linear Regression
    X_test=np.array(X_test)
    X_test.reshape(-1,1)
    ### ###
    my_model=LinearRegression()
    my_model.fit(X_train,y_train)
    pred=my_model.predict([X_test[1]])
    print('the digit to predict is: ',int(pred[0]))
    print('the accuracy of Linear Regression is: {0:.2f}%'.format(my_model.score(X_train,y_train)*100))
    if select==1:
        fig=[X_test[1]]
        img=np.array(fig,dtype=int)
        X_test.reshape(-1,1)
        pxl=img.reshape(28,28)
        plt.title('Linear Regression')
        plt.imshow(pxl)
        plt.show()

    #Random Forest
    my_model=RandomForestClassifier()
    my_model.fit(X_t,y_t)
    pred=my_model.predict([X_test[1]])
    print('the digit to predict is: ',pred[0])
    print('the accuracy of Random Forest Classifier is: {0:.2f}%'.format(my_model.score(X_t,y_t)*100))
    if select==2:
        fig=[X_test[1]]
        img=np.array(fig,dtype=int)
        X_test.reshape(-1,1)
        pxl=img.reshape(28,28)
        plt.title('Random Forest Classifier')
        plt.imshow(pxl)
        plt.show()

    #Logistic Regression
    my_model=LogisticRegression()
    my_model.fit(X_t,y_t)
    pred=my_model.predict([X_test[1]])
    print('the digit to predict is: ',pred[0])
    print('the accuracy of Logistic Regression is: {0:.2f}%'.format(my_model.score(X_t,y_t)*100))
    if select==3:
        fig=[X_test[1]]
        img=np.array(fig,dtype=int)
        X_test.reshape(-1,1)
        pxl=img.reshape(28,28)
        plt.title('Logistic Regression')
        plt.imshow(pxl)
        plt.show()
         
    #Decision Tree Classifier
    my_model=DecisionTreeClassifier()
    my_model.fit(X_train,y_train)
    #X_test=np.array(X_test)
    #X_test.reshape(-1,1)
    pred=my_model.predict([X_test[1]])
    print('the digit to predict is: ',pred[0])
    print('the accuracy of Decision Tree Classifier is: {0:.2f}%'.format(my_model.score(X_t,y_t)*100))
    if select==4:
        fig=[X_test[1]]
        img=np.array(fig,dtype=int)
        pxl=img.reshape(28,28)
        plt.imshow(pxl)
        plt.show()
    
models(X_train,y_train,X_test,select=4)
