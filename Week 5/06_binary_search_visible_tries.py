def binary_search(a, x):

    first_pos = 0
    last_pos = len(a) - 1

    tries = []   # store all attempts

    while first_pos <= last_pos:

        mid = (first_pos + last_pos) // 2
        tries.append(a[mid])   # store checked value

        if x == a[mid]:
            print("Number found:", x)
            print("Position:", mid)
            return tries

        elif x < a[mid]:
            last_pos = mid - 1

        else:
            first_pos = mid + 1

    print("Number not found")
    return tries



a = []

for i in range(1,1001):
    a.append(i)


tries = binary_search(a,249)

print("All tries:", tries)
print("Total tries:", len(tries))