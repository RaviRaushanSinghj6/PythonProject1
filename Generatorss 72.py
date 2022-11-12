""""
Iterable == __iter__() or __getitem__()
Iterator == __next__()
Iteration ==
"""


def gen(n):
    for i in range(n):
        yield i

g = gen(5)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

for i in g:
    print(i)

R = "ravi"
ier = iter(R)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for char in R:
#     print(char)