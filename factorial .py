def factorial(n):
    if n < 0:
        print("Factorial not defined")
        return
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)

num = int(input("Enter a number: "))
factorial(num)