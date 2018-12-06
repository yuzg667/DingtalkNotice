import time
def One2TwoDigit(a):
    a= int(a)
    if a<10:
        a = '0'+str(a)
    else:
        a=a
    return str(a)


def addYear(monthDay):
    monthDay = (time.strftime("%Y")) + str(monthDay)
    return monthDay
