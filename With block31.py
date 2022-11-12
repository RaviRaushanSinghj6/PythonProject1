with open("Raushan.txt") as a:
    file = a.readlines()
    print(file)




a = open("Raushan.txt", "rt")
# print(a.readlines())
# print(a.readline())
# content = a.read()
# print(content)
# print(a)
# print(a.__exit__())
print(a.readline())
a.close()