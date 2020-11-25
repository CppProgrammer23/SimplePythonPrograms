from datetime import datetime, timedelta
import calendar
import time
from dateutil.relativedelta import relativedelta

################## Time And Date ##########
#print current time
#print(datetime.now())
######################################
#convert string into a datetime object
dt_string="Nov 25 2020 3:55PM"
dt = datetime.strptime(dt_string, '%b %d %Y %I:%M%p')
#print(dt)
########################################

#Subtract a week ( 7 days)  from a given date
d=datetime(2020,11,9)
d = d - timedelta(days=14)
#print(d)
########################################

#Print a date in a given format
form = '%A %m %B %Y'
d=datetime(2020,11,25,16,16,15)
#print(d.strftime(form))
######################################

#Find the day of week of a given date
date= datetime(2020,11,25)
s=date.weekday()
#print(date.strftime('%A'))
#print(calendar.day_name[date.weekday()])
###################################

# Add week ( 7 days) and 12 hours to a given date
date = datetime(2020,11,25,16,25,12)
date = date+timedelta(7,hours=12)
#print(date)
####################################

#Print current time in milliseconds
#print(time.time()*1000)
####################################

#Convert following datetime instance into string format
date=datetime(2020,11,25,16,33,14)
#print(date.strftime('%Y-%m-%d %H:%M:%S'))
##################################

#Calculate the date 4 months ahead from the current date
date=datetime(2020,11,30).date()
date=date + relativedelta(months=4)
#print(date)
######################################

#Calculate number of days between two given dates
date=datetime(2020,11,25).date()
date1=datetime(2020,12,4).date()
if date>date1:
    d = date-date1
else:
    d = date1-date
print('days between are: ', d.days)