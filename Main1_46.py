def Fun(string):
    return f"Goodbye World!!{string}"


def add(num1, num2):
    return num1 + num2


print("And the name is:", __name__)
if __name__ == '__main__':
    print(Fun("Hello"))
    print(Fun("Bye"))
    sum = add(5, 6)
    print(sum)
