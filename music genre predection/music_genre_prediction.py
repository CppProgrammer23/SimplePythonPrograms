import pandas as pd
from sklearn.tree import DecisionTreeClassifier as dtc

my_data=pd.read_csv('music.csv')
input=my_data.drop(columns=['genre'])
output=my_data['genre']
print(output)
