# # lisst =[]
# # for i in range(100):
# #     if i %3 == 0:
# #         lisst.append(i)
# #print(lisst)
#
# listt = [i for i in range(100) if i%3 ==0]
# print(listt)
#


# dict1 = { i: f"item{i}" for i in range(100) if i%3==0}
dict1 = {i: f"item{i}" for i in range(10)}
dict2 = {value: key for key, value in dict1.items()}
print(dict1, "\n", dict2)

ravii = {ravi for ravi in ["ravi1", "ravi2",
                           "ravi1", "ravi2", "ravi1"]}
print(type(ravii))
