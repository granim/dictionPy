import json

data = json.load(open("data.json"))


def read_data(word):
    for key, value in data.items():
        if word == key:
            print(value)


while True:
    word = input("Please input a word, To Stop the program type Stop This: ")
    read_data(word)
    if word == "Stop This":
        break
    continue