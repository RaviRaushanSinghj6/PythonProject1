from functools import reduce
list_1 = [1 ,2, 3, 4, 5, 6, 7, 8, 9,10 ]
num = reduce(lambda x,y:x+y, list_1)
print(num)
