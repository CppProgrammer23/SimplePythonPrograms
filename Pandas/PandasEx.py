import pandas as pd


#creating dataframe
my_data=pd.DataFrame({'company':['HP','Dell','IBM','BMW','MERCEDES','Aston'], 
                      'Place':['Sweden','Japan','USA','Germany','Germany','England'], 
                      'Worth_net':[1400,1410,1395,None,1420,1405]},[i for i in range(1,7)])
#my_data.index=[i for i in range(1,len(my_data)+1)]
#print(my_data.loc[3:5]) #loc works with indices it will show 3,4 and 5
#print(my_data.iloc[5]) #iloc will print the object at that position starting from 0
#print(my_data.index.nunique())
#print(my_data)
#determine from the dataset the column that contains the info about the company name, its place and the row with the name of the company
#print(my_data.iloc[4,0:2])
my_data.Worth_net=my_data.Worth_net.astype(float) #change the type of the given column
#print(my_data)
#print(my_data.index.value_counts()) #by default the count will be in descending mode
my_data.set_index('company',inplace=True) #set company as the index
#print(my_data)
my_data.reset_index(inplace=True) #reset the index
#print(my_data)
my_data = my_data.sort_values('Worth_net',ascending=False)
#print(my_data)
#my_data.columns=['Company','Country','Worth_net']
my_data.rename(columns={'company':'Company','Place':'Country'},inplace=True)
#print(my_data)
#remove a column
#my_data = my_data.drop('Worth_net',1)
#remove a row
my_data=my_data.drop(axis=1,index=4)
#print(my_data)
#add new item
my_data['Gross']=my_data.eval('Worth_net+(Worth_net*0.19)')
#print(my_data)
#print(my_data.describe())
#print(my_data.Gross.min())
#print(my_data.groupby('Company').Gross.min())
#print(my_data.isnull())#verify if a value is missing
#print(my_data.isnull().sum())#returns the number of missing values in each columns
#print(my_data.rank())



###############################################################
###############################################################
###############################################################
###############################################################



#From given data set print first and last five rows
data=pd.read_csv('Automobile_data.csv')
#print(data.head()) #by default 5
#print(data.tail()) #by default 5
######################################

#Clean data and update the CSV file
#Replace all column values which contain ‘?’ and n.a with NaN
df = pd.read_csv('Automobile_data.csv', na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
#print (df)
#df.to_csv('Automobile_data.csv')
##########################################

#Find the most expensive car company name
data=data[['company','price']][data.price==data['price'].max()]
#print(data)

#Print All Toyota Cars details
toyota=df.groupby('company').get_group('toyota')
#print(toyota)
#Print only the price of Toyota cars
t=df.groupby('company').get_group('toyota')['price']
#print the highst car price from toyota
t=df.groupby('company').get_group('toyota')['price'].max()
#print(t)
#Count total cars per company
tc = df['company'].value_counts()
#print(tc)
#print all the company
#print(df.iloc[:,4])


#Find each company’s Higesht price car
hc=df.groupby('company')[['index','price']].max()
#print(hc)

#Find the average mileage of each car making company

ac=df.groupby('company')['average-mileage'].mean()
#print(ac)

#Sort all cars by Price column
df=df.sort_values('price',ascending=False)

#Concatenate two data frames using the following conditions
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

gc = pd.DataFrame.from_dict(GermanCars)
jc = pd.DataFrame.from_dict(japaneseCars)
dRes = pd.concat([gc,jc],keys=['German','Japaneese'])
#print(dRes)

#######################################"
#Merge two data frames
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
pdd=pd.DataFrame.from_dict(Car_Price)
hd=pd.DataFrame.from_dict(car_Horsepower)
nd = pd.merge(pdd,hd,on='Company')
print(nd)