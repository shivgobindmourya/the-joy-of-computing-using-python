def magic_square(n):

    if n % 2 == 0:
        print("Magic Square works only for odd numbers!")
        return

    magic = [[0 for _ in range(n)] for _ in range(n)]

    num = n * n
    count = 1

    i = n // 2
    j = n - 1

    while count <= num:

        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if magic[i][j] != 0:
            j -= 2
            i += 1
            continue
        else:
            magic[i][j] = count
            count += 1

        i -= 1
        j += 1

    print("\nMagic Square:\n")
    for row in magic:
        for value in row:
            print(value, end="\t")
        print()

    print("\nMagic Sum =", n * (n*n + 1) // 2)


# Input from user
n = int(input("Enter an odd number: "))
magic_square(n)
