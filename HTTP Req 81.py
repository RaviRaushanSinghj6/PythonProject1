import requests

r = requests.get("Google.com")


def print(text):
    pass


print(r.text)
