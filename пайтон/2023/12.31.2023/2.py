def display_time(hours=0, minutes=0, seconds=0):
    if hours > 24:
        measege = "время неправильно"
        return measege
    if minutes or seconds > 60:
        measege = "время неправильно"
        return measege

    if hours < 10:
        hours = str(hours) # без try except потомучто сверху уже проверяеться на это вроде
        hours = "0" + hours
    if minutes < 10:
        minutes = str(minutes)
        minutes = "0" + minutes
    if seconds < 10:
        seconds = str(seconds)
        seconds = "0" + seconds

    if hours == 0:
        hours == "00"
    if minutes == 0:
        minutes == "00"
    if seconds == 0:
        seconds == "00"
    
    template = '%s:%s:%s'
    measege = template % (hours, minutes, seconds)
    return measege
    
print(display_time(12, "сука"))