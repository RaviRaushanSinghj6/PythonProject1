class Employee:
    no_of_leaves = 4

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salry = asalary
        self.role = arole

    # def fun(self):
    #     return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}."


ravi = Employee("Ravi", 1000, "Engineer")
# raushan = Employee()


# ravi.name = "Ravi"
# ravi.salary = 500000
# ravi.role = "Engineer"
#
# raushan.name = "Raushan"
# raushan.salary = 600000
# raushan.role = "SE"

# print(ravi.fun())
print(ravi.no_of_leaves)
print(ravi.name)
