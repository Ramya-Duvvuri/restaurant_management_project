from datetime import datetime,time
def is_restaurant_open():
    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()
    weekday_hours = (time(9,0),time(22,0))
    weekday_hours = (time(10,0),time(23,0))

    if current_day <5:
        open_time,close_time = weekday_hours
    else:
        open_time,close_time = weekday_hours
    return open_time <= current_time <=close_time