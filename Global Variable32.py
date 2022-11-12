# Fun1
a = 5


def abc(n, m):
    print(n, "I am", m)
    a = 4  # Local variable, Global variable is read only
    a = a + 10
    print(a)


abc("Hii", "joker")
# Fun 2
s = 2


def q():
    # s = s+5     # creates an error, Global can't be modified inside a function
    print(s)


q()
# Fun 3
Gvar = 21


def asd():
    Lvar = 31
    global Gvar
    Gvar = Gvar + 21
    print(Gvar, Lvar)


asd()


# Fun 4
def Outer():
    x = 20

    def Inner():
        global x
        x = 10
        print("Printing x inside inner\n", x)

    print("before calling Inner()\n", x)
    Inner()
    print("before calling Inner()\n", x)


Outer()
