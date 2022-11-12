# list1 = ["CSE","ECE","EEE","IT"]
# for item in list1:
#   print(item)

list2 = [["Ravi", 4], ["Rahul", 5], ["Rohit", 6]]
# for item, Grade in list2:
#   print(item,"and grade is",Grade)

Kosh = dict(list2)
for item, grade in Kosh.items():
    print(item, grade)

a = ["Ravi", "Rohan", "Sonu", int, float, 2, 4, 6, 345, 57, 78, 34, 68]
for item in a:
    if str(item).isnumeric() and item > 6:
        print(item)
