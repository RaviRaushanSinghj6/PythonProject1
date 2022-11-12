x = int(input("Enter no of rows you want to print"))
y = bool(input("Enter 1 for upward and 0 for downward"))


def Star(x, y):
    if y == True:

        count = 0
        while count <= x:
            print("*" * count)
            count = count + 1
    else:
        while x > 0:
            print("*" * x)
            x = x - 1


Star(x, y)
