import time
second = 0
minute = 0
hours = 0
while True:
    print(hours, ":", minute, ":", second)
    time.sleep(1)
    second += 1
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        hours += 1