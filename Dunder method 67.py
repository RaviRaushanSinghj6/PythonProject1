# class String:
#
#     def __init__(self, string):
#         self.string = string
#
#
# if __name__ == '__main__':
#     string1 = String('Hello')
#
#     print(string1)


class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name} Salary is {self.salary} Role is{self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee(self.name),(self.salary),(self.role)"


emp1 = Employee("Harry", 234, "Eng")
emp2 = Employee("Larry", 234, "Bowler")
print(emp1 + emp2)
print(emp1 / emp2)
print(emp1.printdetails())