a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))

Maxnum = max (a, b)

while 1:
    if Maxnum % a == 0 and Maxnum % b == 0:
        break
    Maxnum = Maxnum + 1

print("The LCM of {a} and {b} is ", {Maxnum})
