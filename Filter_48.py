list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def greater_than_5(num):
    return num > 5


greater_than_5 = list(filter(greater_than_5, list_1))
print(greater_than_5)
