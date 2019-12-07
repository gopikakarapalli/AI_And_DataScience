import datetime as dt


Date=dt.date(2018,11,20) #to print date formate
print(Date)

todate=dt.date.today()# it returns current data
print('today date',todate)
print('year:',todate.year)# it returns current year
print('Mon :', todate.month)# it returns current mothe
print('day :',todate.day)# it returns current day

week = todate.weekday # consider mon = 0 : sun=6
isoweek = todate.isoweekday  #consider mon = 1: sun = 7
print(week)
print(isoweek)
print('     -------------     adding    -----------          ')
tdelta = dt.timedelta(days=15)
print(todate + tdelta)

print(todate - tdelta)

print('-------------------------------------------------------------')#------

bday=dt.date(1992,11,27)
present=todate-bday
print(present.days)
print(present.total_seconds())

print('----------time---------------------------')

t= dt.time(3,4,56,1000)#returns time formate (h,m,sec,micosec)
print(t)
print('hour',t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

print('Earliest  :', dt.time.min)
print('Latest    :', dt.time.max)
print('Resolution:', dt.time.resolution)

print('----------------both time & date -------------------------')
DT=dt.datetime(2018,2,2,3,44,56,1000)#both date and time
print(DT)

tdelta = dt.timedelta(hours=6)# to add/sub time
print(DT + tdelta)


DT1=dt.datetime.today()#local time zone
DT2=dt.datetime.now()#(requ time zone ) default is local zone
DT3=dt.datetime.utcnow()#utc time zone
print('loca',DT1)
print('req',DT2)
print('utc',DT3)
'''
# Formatting datetime
print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
print('The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}'.format(dt, "day", "month", "time"))
#Using datetime.strptime()
dt = dt.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)

# Using datetime.timetuple() to get tuple of all attributes
tt = dt.timetuple()
for it in tt:   
   print (it)

print('ordinal:', [time.toordinal()])
'''
print(dir(dt))

# note: pytz lib is used for time zone

# 



