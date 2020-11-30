from matplotlib import pyplot as plt
import pandas as pd


#x=[1,2,3,4,5,6]
#y=[7,8,4,6,3,1]
#plt.plot(x,y,'y*')
#plt.show()

#Read Total profit of all months and show it using a line plot
my_data=pd.read_csv('company_sales_data.csv')
tp = my_data['total_profit'].tolist()
mn= my_data['month_number'].tolist()

#plt.xlabel('Month')
#plt.ylabel('Total profit')
#plt.title('Company sales data of last year')
#plt.plot(mn,tp,color='g',linewidth=3,linestyle='--',marker='o',markerfacecolor='k',label='Profit data of last year')
#plt.legend(loc='upper left')
#plt.show()

#Read all product sales data and show it using a multiline plot
fc=my_data['facecream'].tolist()
fw=my_data['facewash'].tolist()
tpaste=my_data['toothpaste'].tolist()
bs=my_data['bathingsoap'].tolist()
sh=my_data['shampoo'].tolist()
ms=my_data['moisturizer'].tolist()
#plt.ylabel('Sales unit in numbers')
#plt.plot(mn,fc,color='r',marker='o',label='Facemask')
#plt.plot(mn,fw,color='g',marker='o',label='Facewash')
#plt.plot(mn,tpaste,color='b',marker='o',label='Toothpaste')
#plt.plot(mn,bs,color='y',marker='o',label='Bathingsaop')
#plt.plot(mn,sh,color='m',marker='o',label='Shampoo')
#plt.plot(mn,ms,color='bisque',marker='o',label='Moisturizer')
#plt.legend(loc='upper left')
#plt.show()

#Read toothpaste sales data of each month and show it using a scatter plot
#plt.scatter(mn,tpaste,label='Tooth paste sales')
#plt.grid(linestyle='-')
#plt.legend(loc='upper left')
#plt.show()

#Read face cream and facewash product sales data and show it using the bar chart

#plt.bar([a-0.1 for a in mn],fc,label='Face cream sales',width=-0.25)
#plt.bar([a+0.1 for a in mn],fw,label='Face wash sales',width=0.25)
#plt.grid(linestyle='--')
#plt.legend(loc='upper left')
#plt.show()

#Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
#plt.bar(mn,bs,color='g')
#plt.title('Bathing soap Sales')
#plt.savefig('Your_directory\\bathing soap.png',dpi=200)
#plt.show()

#Calculate total sale data for last year for each product and show it using a Pie chart

#fc1=my_data['facecream'].sum()
#fw1=my_data['facewash'].sum()
#tpaste1=my_data['toothpaste'].sum()
#bs1=my_data['bathingsoap'].sum()
#sh1=my_data['shampoo'].sum()
#ms1=my_data['moisturizer'].sum()
#myLabel=['Face cream sales','Face wash sales','Tooth paste sales','bathingsoap sales','Shampoo sales','moisturizer sales']
#myData=[fc1,fw1,tpaste1,bs1,sh1,ms1]
#plt.pie(myData,labels=myLabel,autopct='%1.1f%%')
#plt.axis('equal')
#plt.legend(loc='lower right')
#plt.show()

#Read Bathing soap facewash of all months and display it using the Subplot
#f, arr = plt.subplots(2,sharex=True)
#arr[0].set_title('Face wash data')
#arr[0].plot(mn,fw,marker='o',color='g')
#arr[1].set_title('Bathing soap data')
#arr[1].plot(mn,bs,marker='o',color='b')
#plt.show()

#Read all product sales data and show it using the stack plot
plt.title('All products')
plt.plot([],[],color='m', label='face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)
plt.stackplot(mn,fc,fw,tpaste,bs,sh,ms,colors=['m','c','r','k','g','y'])
plt.grid(linestyle='--')
plt.legend(loc='upper left')
plt.show()