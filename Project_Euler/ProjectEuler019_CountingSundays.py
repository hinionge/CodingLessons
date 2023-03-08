# 8.3.2023
# Project Euler 19
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Code works (and the answer is correct) but it's getting late; I'll comment it up in the morning


class date:
    def __init__(self, d, m, y):

        self.d = d
        self.m = m
        self.y = y

d = date(0,0,0)

                            # Minor cheat to get round the headache of zero-indexing -- NB this might MATTER, later
months = [None,31,28,31,30,31,30,31,31,30,31,30,31]

def one_day_after(d):
    day = d.d
    month = d.m
    year = d.y

    day = day + 1


    if day > months[month]:
        day = 1
        month = month + 1

        if month == 13:
            month = 1
            year = year + 1
            months[2] = days_in_february(year)

    d.d = day
    d.m = month
    d.y = year

    return d

def days_in_february(year):
    days = 28
    if year%4 == 0:
        days = 29
        if year%100 == 0:
            days = 28
        if year%400 == 0:
            days = 29
    return days



if __name__ == "__main__":
    d = date(1,1,1900)
    day = 1
    tally = 0

    while d.y < 2001:
        if day == 0:
            print(str(d.d) + " " + str(d.m) + " " + str(d.y) + " -- SUNDAY")
        d = one_day_after(d)
        day = day + 1
        day = day%7

        if d.y > 1900:
            if day == 0:
                if d.d == 1:
                    tally = tally + 1

    print("In the twentieth century, " + str(tally) + " Sundays fell on the first of the month")