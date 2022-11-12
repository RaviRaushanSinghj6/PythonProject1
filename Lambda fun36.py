# Lambda is just a normal function written in 1 line
add = lambda a, b: a + b

print(add(2, 3))

B = [[23, 34], [345, 3456], [21, 553]]
B.sort(key=lambda x: x)
print(B)
