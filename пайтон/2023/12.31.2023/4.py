def turn_seconds_into_time(seconds):
    hours=(seconds//3600)
    minutes=(seconds//60)%60
    seconds=seconds%60
    if hours < 10:
        hours = str(hours)
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
    mesage = template % (hours, minutes, seconds)
    return mesage

print(turn_seconds_into_time(44404))