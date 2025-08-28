def add_time(start, duration, day=''):
    # Split start time
    time, period = start.split()
    hour, minute = map(int, time.split(':'))
    
    # Convert PM to a 24 hour day format
    if period.upper() == 'PM':
        hour += 12
    
    # Split duration time
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add duration time to start time and also any extra hour from the minutes
    minute += dur_minute
    hour += dur_hour + (minute // 60)
    minute %= 60

    # Calculating the number of days and hour
    days = hour // 24
    hour %= 24

    # Convert back to a 12 hour day format and figuring out the period
    if hour == 0:
        display_hour = 12
        period = 'AM'
    elif hour < 12:
        display_hour = hour
        period = 'AM'
    elif hour == 12:
        display_hour = 12
        period = 'PM'
    else:
        display_hour = hour - 12
        period = 'PM'
    
    # Format minutes with leading zero
    new_time = f'{display_hour}:{minute:02d} {period}'

    # Handle optional day
    if day:
        days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = days_of_the_week.index(day.capitalize())
        new_day = days_of_the_week[(day_index + days) % 7]
        new_time += f', {new_day}'
    
    # Handle next day and days later cases
    if days == 1:
        new_time += ' (next day)'
    elif days > 1:
        new_time += f' ({days} days later)'

    return new_time