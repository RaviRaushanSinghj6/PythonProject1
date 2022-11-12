class A:
    def meth(self):
        print("This is from A")


class B(A):
    def meth(self):
        print("This is from B")


class C(A):
    def meth(self):
        print("This is from C")


class D(B, C):
    pass


a = A()
b = B()
c = C()
d = D()

d.meth()
