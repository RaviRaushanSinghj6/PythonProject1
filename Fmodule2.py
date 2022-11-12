z = 54
print("Value of Z is", z)


def addition(a: object, b: object) -> object:
    print("The sum of", {a}, "and", {b}, "is:\n", a + b)
    # print(sum(a,b))


x = int(input("Enter a value"))
y = int(input('Enter b value'))
addition(x, y)
