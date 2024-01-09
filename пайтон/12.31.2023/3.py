def display_time(hours, minutes, seconds):
    hours = hours * 3600
    minutes = minutes * 60

    result=hours+minutes+seconds
    return result

print(display_time(12, 20, 4))