"""
FIZZBUZZ PART 1 (Buggy Logic Version)
"""

for i in range(1, 51):

    if i % 3 == 0:
        print(str(i) + " fizz")

    elif i % 5 == 0:
        print(str(i) + " buzz")

    elif i % 3 == 0 and i % 5 == 0:
        print(str(i) + " fizzbuzz")

    else:
        print(i)
