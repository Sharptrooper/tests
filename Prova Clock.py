def add_time(start, duration, day=False):
    # dict to correlate days of the week to a number
    dicio = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 0
    }

    # Checking which day of the week was inputted and giving it a numerical value for later math.

    currentDay = 0

    if day is not False:
        aux = day.lower()
        if aux in dicio:
            currentDay = dicio[aux]

    # Breaking apart the time input into useful individual values
    aux = start.split()
    basePeriod = aux[1]
    aux = aux[0].split(":")
    baseHour = int(aux[0])
    baseMinute = int(aux[1])

    aux = duration.split(":")
    increaseHour = int(aux[0])
    increaseMinute = int(aux[1])

    # Adding minutes up, making sure to add the zero before the digit if needed
    daycount = 0
    totalMinute = baseMinute + increaseMinute
    switch = False

    if totalMinute >= 60:
        baseHour = baseHour + 1
        totalMinute = totalMinute - 60
        if baseHour == 12:
            if basePeriod == "AM":
                basePeriod = "PM"
            else:
                basePeriod = "AM"
                daycount = daycount + 1
            if 0 < increaseHour < 12:
                switch = True

    if totalMinute < 10:
        totalMinute = "0" + str(totalMinute)

    # Finding how many days are covered by the period

    totalHour = baseHour + increaseHour

    while totalHour > 12:
        if switch:
            switch=False
        else:
            if basePeriod == "AM":
                basePeriod = "PM"
            else:
                basePeriod = "AM"
                daycount = daycount + 1

        totalHour = totalHour - 12

    resultado = str(totalHour) + ":" + str(totalMinute) + " " + basePeriod

    # If a day was input, this calculates which day it'll be after it's all done and concatenates it
    if day is not False:
        currentDay = (currentDay + daycount) % 7
        for key, value in dicio.items():
            if value == currentDay:
                currentDay = key
                resultado = resultado + ", " + currentDay.capitalize()

    # Checks if at least day has passed and if so concatenates that info
    if daycount == 1:
        resultado = resultado + " (next day)"
    if daycount >= 2:
        resultado = resultado + " (" + str(daycount) + " days later)"

    return resultado


print(add_time("11:30 AM", "01:34","Friday"))

