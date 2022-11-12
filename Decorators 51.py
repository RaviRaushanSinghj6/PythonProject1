# Printing a function after deleting it

# def function1():
#     print("Good bye world")
#
#
# func2 = function1
# del function1
# # func2()


# Returning a function by function
# def func(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return int
#
#
# a = func(0)
# print(a)

# # Function as an argument
# def execute(function):
#     function("Ravi")
#
#
# execute(print)


def dec1(fun1):
    def nowexec():
        print("Executing now")
        fun1()
        print("Executed")

    return nowexec


def myfun():
    print("I am a coder")


myfun = dec1(myfun)
myfun()