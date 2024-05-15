def isLeapYear(year):
    if (year % 4 != 0):
        return False
    elif (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    else:
        return True


year = 2024

if(isLeapYear(year)):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")