# f1 = open("ra.txt")
try:
    f = open("ravi.txt")

except Exception as e:
    print(e)
else:
    print("This will run only if except does not run")

finally:
    print("run this anyway")
    f.close()
    # f1.close()

print("Important")
