# class A:
#     def demo(self):
#         print(" From class A")
#
#
# class B(A):
#     def demo(self):
#         print(" From class B")
#
#
# class C(A):
#     def demo(self):
#         print(" From class C")
#
#
# # To check MRO
# class D(B, C):
#     def check(self):
#         print("This is an example showing Method Resolution order")
#
#
# obj = D()
# obj.demo()


########## Over Riding a Function ##########


# class A:
#     classvar1 = "Ï am a class variable in class A"
#     def __int__(self):
#         self.var1 = "I am inside class A's constructor"
#         self.classvar1 = "Inside var in class A"
#
# class B(A):
#     classvar1 = "Ï am in class B"
#     def __int__(self):
#         self.var1 = "I am inside class B's constructor"
#         self.classvar1 = "Instance var in cladss B"
#
#
# a  =  A()
# b  =  B()
#
#
# print(b.classvar1)


############# SUPER FUNCTION #############


class A:
    classvar1 = "Ï am a class variable in class A"

    def __int__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Inside var in class A"
        self.special = "Special"


class B(A):
    classvar1 = "Ï am in class B"

    def __int__(self):
        super().__int__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__int__()


a = A()
b = B()

print(b.special)
