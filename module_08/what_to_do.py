from datetime import datetime


time_now = datetime.now()

if time_now.hour == 0:
    print("You should be asleep..")
elif time_now.hour > 8 and time_now.hour < 17:
    print("Why aren't you working??")
elif time_now.hour > 17:
    print("Relax!")

