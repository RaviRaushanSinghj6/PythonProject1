import random

rannum = random.randint(0, 1)
rand = random.random() * 100
print(rand)

list1 = [12, 32, 2543, 4123, 5, 2, 13, 2, 51, 2, 543, 4]
choice = random.choice(list1)
print(choice)

list1.sort()
print(list1)


def a():
    list2 = [13, 23, 24, 34, 5, 32]
    list2.sort()
    return list2

# 😊😊😊😊😊
# print(a())
# import datetime
# x = datetime.datetime.now()
# print(x)
