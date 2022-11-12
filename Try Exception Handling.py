number1 = input("Enter the 1st number\n")
number2 = input("Enter the 2nd number\n")

try:
    print("Multiplication of Number1 and Number2 is:\n",
          int(number1)*int(number2))

except Exception as a:     # object
    print(a)

print("This line is very important\n")
print("after exception handling\n")