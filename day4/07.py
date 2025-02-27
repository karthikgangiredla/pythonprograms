from datetime import datetime,timedelta
"""
now=datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.year)

now=datetime.now()
print(f"tomorrow:{now+timedelta(days=26)}")
print(f"tomorrow:{now+timedelta(weeks=3)}")
print(f"tomorrow:{now+timedelta(hours=3)}")
print(f"tomorrow:{now+timedelta(minutes=3)}")
print(f"tomorrow:{now+timedelta(seconds=3)}")

now=datetime.now().strftime("%Y-%m-%d") #2025-02-26
now1=datetime.now().strftime("%y-%m-%d") #25-02-26
now3=datetime.now().strftime("%a-%b-%d %H:%M:%S")#Wed-Feb-26 14:55:34
now4=datetime.now().strftime("%A, %dth of %b %Y")#Wednesday, 26th of Feb 2025


def presentage(birthday):
    now = datetime.now()
    currentyear=now.year
    birthyear=birthday.year
    age=currentyear-birthyear
    if(birthday.month>now.month or (birthday.month==now.month and now.day<birthday.day)):
        age-=1
    print(age)
bday=datetime(2003,10,26)
presentage(bday)
"""
#scheduling feature events and calculating time remaining
def timecalculater(event_date):
    now = datetime.now()
    currentyear=now.year
    eventyear=event_date.year
    yearsleft=eventyear-currentyear
    print(yearsleft)
bday=datetime(2026,10,26)
timecalculater(bday)
