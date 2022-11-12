def Fun(x, *asd, **asdf):
    print(x)
    for i in asd:
        print(i)
    for key, value in asdf.items():
        print(f"{key} for {value}")


a = "Apple"
name = ["a", "b", "c", "...."]
kw = {"aa": "Aam", "bb": "Ball", "cc": "Cat"}
Fun(a, *name, **kw)