import time


def searcher():
    book = "This is a book of python written by ravi raushan singh"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Text in book")
        else:
            print("Text not in book")


search = searcher()
next(search)
search.send("pyhton")
input("press any key")
search.send("by")
