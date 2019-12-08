import json

data = json.load(open("data.json"))


def read_data(word):
    for key, value in data.items():
        if word == key:
            print(value)


#The instuctors way
def translate(word):
    if word in data:
        return data[word]
    else
        return "The word does not exist."


# My code 
while True:
    word = input("Please input a word, To Stop the program type Stop This: ")
    if read_data(word) != True:
        print("Sorry that word does not exist")
        continue
    read_data(word)
    if word == "Stop This":
        break
    continue