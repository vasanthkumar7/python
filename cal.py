import calendar
year=int(input('enter the year: '))
mon=int(input('enter the month: '))
da=int(input('enter the day: '))
pi=calendar.monthcalendar(year,mon)
for i in pi:
    l=0
    for j in i:
        l=l+1
        if(j==da):
            if(l==1):
                print("monday")
            if(l==2):
                print("tuesday")
            if(l==3):
                print("wednesday")
            if(l==4):
                print("thursday")
            if(l==5):
                print("friday")
            if(l==6):
                print("saturday")
            if(l==7):
                print("sunday")
            
    print('')

