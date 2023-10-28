import datetime
alarmHour = int(input("Enter Hour:"))
alarmMin = int(input("Enter Minuters:"))
alarmAm = input("am / pm:")

if alarmAm=="pm":
    alarmHour+=12
    
while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing..")
        break
