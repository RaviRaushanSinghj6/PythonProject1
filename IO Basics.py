# File IO Basics
""""
"r"
"w"
"x"
"a"
"t"
"b"
"+"
"""
# File Reading
f = open("Raushan.txt", "rt")
# content = f.read()
# print(content)
# f.close()
# for line in f:
#     print(line)

# print(f.readline())
# print(f.readline())
# print(f.readline())

print(f.readlines())
# print(f.readable())
f.close()