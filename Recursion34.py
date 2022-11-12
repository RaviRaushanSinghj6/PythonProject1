# # Iterative
def FactIterative(num1):
    fac = 1
    for i in range(num1):
        fac = fac * (i + 1)
    return fac
    pass


# Recursive
def FactRecursive(n):
    if n == 0:
        return 1
    else:
        return n * FactRecursive(n - 1)

    pass


num = input("Enter the number to find factorial")


def Fun():
    print("Factorial = ", FactRecursive(int(num)))
    print("Factorial = ", FactIterative(int(num)))
    # z = int(input("Do you want to calculate factorial again press 1 for yes 0 for no"))
    # if z == 1:
    #     print(Fun(int(input("Enter the number"))))


Fun()


def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 25:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    pass


print(Fibonacci(int(input("Enter a number"))))
