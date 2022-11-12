import time
import datetime

initial = time.time()
k = 0
while k < 45:
    print("Goodbye World")
    # time.sleep(2)  # prints after 2 second
    k += 1
print(f"While loop ran in ", time.time() - initial, "seconds")

initial2 = time.time()
for i in range(45):
    print("Goodbye World")
    # time.sleep(2)  # prints after 2 second
print("For loop ran in ", time.time() - initial2, "seconds\n")

# TIME
a = datetime.datetime.now()
print(a)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)


def a():
    for I in range(45):
        print("hii")
        time.sleep(2)


a()
