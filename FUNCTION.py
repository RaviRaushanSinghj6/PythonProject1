# a = 23
# b = 45
# c = sum((a, b))    # built in
# print(c)

# def Ravi():
# print("Good Bye World")
#  print("Function")
#   print("Now call the function")
# Ravi()

def Add(a, b):
    print("Addition is", a + b)


Add(2, 4)


def hello(a, b, c):
    """"This is a function which will calculate average of 3 numbers"""
    avg = (a + b + c) / 3
    return avg


# A = hello(34, 46, 78)
# print(A)
print(hello.__doc__)
