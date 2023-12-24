hours_current_time_world_usa_kosovo=input("chas= ")
minutes_current_time_world_usa_kosovo=input("minutes= ")
try:
    hours_current_time_world_usa_kosovo=int(hours_current_time_world_usa_kosovo)
    minutes_current_time_world_usa_kosovo=int(minutes_current_time_world_usa_kosovo)
except ValueError:
    exit()
dayintheworldhowmuch=23
minuteshowmuchisit= 60
dayhours=dayintheworldhowmuch-hours_current_time_world_usa_kosovo
minutesshit=minuteshowmuchisit-minutes_current_time_world_usa_kosovo // 1
print(dayhours," часов ", minutesshit, " минут")
