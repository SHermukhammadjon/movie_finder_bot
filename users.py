from datetime import  datetime

def now():
    now = datetime.now()
    return now.strftime("%d.%m.%Y/%H:%M")

