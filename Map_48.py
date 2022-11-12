def sq(a):
    return a * a


num = [2, 4, 5, 7, 8, 4, 6, 23, 145, 46, 5, 2]
square = list(map(sq, num))
print(square)

# _______________SECOND______________________#

num2 = [2, 4, 5, 7, 8, 4, 6, 23, 145, 46, 5, 2]
square = list(map(lambda x:x*x, num))
print(square)