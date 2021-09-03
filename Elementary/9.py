from datetime import date

def checkLeapYear(year):
    isLeapYear = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeapYear = True
        else:
            isLeapYear = True

    return isLeapYear

today = date.today()
print("Current date: ", today)

currentYear = today.year
countLeapYears = 0

lists = []
while True:
    if countLeapYears >= 20:
        break

    if checkLeapYear(currentYear):
        lists.append(currentYear)
        countLeapYears += 1
    currentYear += 1

print(*lists, sep = ", ")

