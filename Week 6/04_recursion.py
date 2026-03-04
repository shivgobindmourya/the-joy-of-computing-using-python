def factorial(n):

    if n == 0:        # base case
        return 1

    else:
        return n * factorial(n-1)
    
n = int(input("Enter a positive number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of", n, "is", factorial(n))