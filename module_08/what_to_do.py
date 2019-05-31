from datetime import datetime

time_now = datetime.now()

if time_now.hour == 0:
    print("Go to bed!")
elif time_now.hour > 0 and time_now.hour < 8:
    print("You should be asleep..")
elif time_now.hour > 8 and time_now.hour < 17:
    print("Why aren't you working??")
elif time_now.hour > 17 and time_now.hour:
    print("Relax!")








"""
def return_what_to_do(time_now):
    if time_now.hour == 0:
        return "Go to bed!"
    elif time_now.hour > 0 and time_now.hour < 8:
        return "You should be asleep.."
    elif time_now.hour > 8 and time_now.hour < 17:
        return "Why aren't you working??"
    elif time_now.hour > 17 and time_now.hour:
        return "Relax!"



if __name__ == "__main__":
    print("Checking what to do...")
    print(return_what_to_do(datetime.now()))
"""

