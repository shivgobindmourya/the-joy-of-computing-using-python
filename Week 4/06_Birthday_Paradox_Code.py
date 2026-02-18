import random
import datetime

birthday = []

i = 0
while i < 50:

    year = random.randint(1895, 2017)

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = 1
    else:
        leap = 0

    month = random.randint(1,12)

    if month == 2 and leap == 1:
        day = random.randint(1,29)
    elif month == 2 and leap == 0:
        day = random.randint(1,28)
    elif month in [1,3,5,7,8,10,12]:
        day = random.randint(1,31)
    else:
        day = random.randint(1,30)

    date = datetime.date(year, month, day)
    day_of_year = date.timetuple().tm_yday

    birthday.append(day_of_year)
    i += 1

birthday.sort()

print("Day of Year List:")
print(birthday)

print("\nCollisions:")
for i in range(len(birthday)-1):
    if birthday[i] == birthday[i+1]:
        print("Collision at day:", birthday[i])

