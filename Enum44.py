List1 = ["a", "b", "c", "d"]

i = 1
for item in List1:
    if i % 2 != 0:
        print(f"the alphabet is :{item}\n")
    i = i + 1

# Using Enum
for index, item in enumerate(List1):
    if index % 2 == 0:
        print(f"The alphabet is : {item}")
