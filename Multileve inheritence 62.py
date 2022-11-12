class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def dance(self):
        return f"Yeas I dance {self.dance} no of times"


class Grandson(Son):
    dance = 6
    study = 5

    def dance(self, a):
        # self.dance = a
        return f"hello!" \
               f"I am a dancer, i dance {self.dance} no of times"


D = Dad()
S = Son()
G = Grandson()

print(G.basketball)
print(G.dance)
print(G.study)
print(G.dance(8))


# class Employees():
#
#     def Name(self):
#         print("Employee Name: Khush")
#
#
# class salary(Employees):
#     def Salary(self):
#         print("Salary: 10000")
#
#
# class Designation(salary):
#     def desig(self):
#         print("Designation: Test Engineer")
#
#
# call = Designation()
# call.Name()
# call.Salary()
# call.desig()
