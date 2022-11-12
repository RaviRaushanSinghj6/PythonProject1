# Writing
f = open("Raushan2.txt","w")
f.write("GoodBye World\n")
f.write("Have a good day\n")
f.close()

# Appending
f = open("Raushan2.txt","a")
f.write("Appending Text\n")
f.write(">>>>>>......\n")
a= f.write("Thank you Harry")
print(a)
f.close()
