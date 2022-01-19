year = 31536000
day = 86400
hour = 3600
minute = 60

def checkPlural(time):
    if time >= 2:
        return 's'
    else:
        return ''
    
def format_duration(seconds):
    yearDuration = ''
    dayDuration = ''
    hourDuration = ''
    minuteDuration = ''
    secondDuration = ''
    
    if(seconds > 0):
        yearFormat = '{yrs:0.0f} year'
        if(seconds / year >= 1):
            pluralYears = checkPlural(seconds//year)
            yearDuration = yearDuration + yearFormat.format(yrs = seconds//year) + pluralYears
        dayFormat = '{days:0.0f} day'
        if(seconds % year / day >= 1):
            pluralDays = checkPlural(seconds%year//day)
            dayDuration = dayDuration + dayFormat.format(days = seconds%year//day) + pluralDays
        hourFormat = '{hrs:0.0f} hour'
        if(seconds % year % day / hour >= 1):
            pluralHours = checkPlural(seconds%year%day//hour)
            hourDuration = hourDuration + hourFormat.format(hrs = seconds%year%day//hour) + pluralHours
        minuteFormat = '{mins:0.0f} minute'
        if(seconds % year % day % hour / minute >= 1):
            pluralMinutes = checkPlural(seconds%year%day%hour//minute)
            minuteDuration = minuteDuration + minuteFormat.format(mins = seconds%year%day%hour//minute) + pluralMinutes
        secondFormat = '{secs:0.0f} second'
        if(seconds % year % day % hour % minute >= 1):
            pluralSeconds = checkPlural(seconds%year%day%hour%minute)
            secondDuration = secondDuration + secondFormat.format(secs = seconds%year%day%hour%minute) + pluralSeconds
            
    else:
        return 'now'
    
    presentDurations = []
    durationsString = ''
    durations = [yearDuration, dayDuration, hourDuration, minuteDuration, secondDuration]
    for d in durations:
        if d != '':
            presentDurations.append(d)
            
    if(len(presentDurations) > 2):
        for i in range(len(presentDurations) - 2):
            durationsString = durationsString + presentDurations[i] + ', '
        durationsString = durationsString + presentDurations[-2] + ' and ' + presentDurations[-1]
    elif(len(presentDurations) == 2):
        durationsString = presentDurations[0] + ' and ' + presentDurations[1]
    else:
        durationsString = presentDurations[0]

    return durationsString