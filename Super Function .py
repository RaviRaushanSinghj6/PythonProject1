class A:
    classvar1 = "I am in class A"

    def __int__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Inside var in class A"
        self.special = "Special"


class B(A):
    classvar1 = "I am in class B"
    def __int__(self):
        #super().__int__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        #super().__int__()


a = A()
b = B()

print(b.var1, b.classvar1)
# b.special
