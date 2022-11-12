class Employee:
    no_of_leaves = 6

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_str(cls, string):
        # param = string.split("-")
        # return cls(param[0], param[1], param[2])
        # or
        return cls(*string.split("-"))


ravi = Employee("Ravi", 1000, "Engineer")
raushan = Employee("Raushan", 1500, "Developer")
Singh = Employee.from_str("Singh-10000-Dr")

ravi.change_leaves(45)

print(ravi.no_of_leaves)
print(ravi.name)
print(raushan.name)
print(Singh.name)
