def add_time(start, duration, day=None):
    start_split = start.replace(":", " ").split()
    
    if start_split[2] == "AM":
        start_mins = (int(start_split[0]) * 60) + int(start_split[1])
    else:
        start_mins = (int(start_split[0]) * 60) + int(start_split[1]) + 720

    duration_split = duration.split(":")
    duration_mins = (int(duration_split[0]) * 60) + int(duration_split[1])

    total_mins = start_mins + duration_mins

    num_hours = (total_mins // 60) % 12
    if num_hours == 0:
        num_hours = 12
    num_mins = total_mins % 60

    finish_time = f"{num_hours}:{num_mins:02d}"

    am_pm = None

    if (total_mins % 1440) < 720:
        am_pm = "AM"
    else:
        am_pm = "PM"

    plus_days = (duration_mins // 1440)

    until_midnight = 1440 - start_mins


    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day:
        no_of_day = weekdays.index(day.capitalize())
        if (duration_mins % 1440) > until_midnight:
            no_of_day += 1
        no_of_day += (duration_mins // 1440)
        no_of_day = no_of_day % 7
        if no_of_day == 7:
            no_of_day = 0
        day_name = weekdays[no_of_day]
    else:
        day_name = ""


    if (duration_mins % 1440) > until_midnight:
        plus_days += 1
    
    if plus_days == 0:
        plus_days = ""
    elif plus_days == 1:
        plus_days = "(next day)"
    else:
        plus_days = f"({plus_days} days later)"


    if not day:
        if plus_days == "":
            new_time = f"{finish_time} {am_pm}"
        else: 
            new_time = f"{finish_time} {am_pm} {plus_days}"
    else:
        if plus_days == "":
            new_time = f"{finish_time} {am_pm}, {day_name}"
        else:
            new_time = f"{finish_time} {am_pm}, {day_name} {plus_days}"

    return new_time