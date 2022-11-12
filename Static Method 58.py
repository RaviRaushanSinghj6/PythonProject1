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
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)


ravi = Employee("Ravi", 1000, "Engineer")
raushan = Employee("Raushan", 1500, "Developer")
Singh = Employee.from_str("Singh-10000-Dr")

print(ravi.no_of_leaves)
Singh.printgood("Hello")
