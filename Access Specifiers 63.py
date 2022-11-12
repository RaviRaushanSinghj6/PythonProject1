# Public -
# Protected - "_"
# Private -  "__"

class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __pr = 98

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole


emp = Employee("harry", 343, "Programmer")
print(emp._Employee__pr)
print(emp._protec)
print(emp.name)
print(emp.role)
print(emp.salary)
