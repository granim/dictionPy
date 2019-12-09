import json
from difflib import get_close_matches

data = json.load(open("data.json"))


#My way
def read_data(word):
        if word in data:
            return data[word]
        elif len(get_close_matches(word, data.keys())) > 0:
            return "Did you mean %s instead? " % get_close_matches(word, data.keys())[0]
        else:
            return "The word does not exist"    
            

#The instuctors way
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word does not exist."


while True:
    word = input("Please input a word, To Stop the program type Stop This: ").lower()
    print(read_data(word)) 
    continue