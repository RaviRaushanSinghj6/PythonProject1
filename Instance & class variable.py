class Employee:
    no_of_leaves = 45
    pass


ravi = Employee()
raushan = Employee()

ravi.name = "Ravi"
ravi.salary = 500000
ravi.role = "Engineer"

raushan.name = "Raushan"
raushan.salary = 600000
raushan.role = "S E"

print(ravi.name)
print(Employee.no_of_leaves)
print(ravi.__dict__)
