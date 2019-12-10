import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print(len(data),type(data))

#My way
def read_data(word):
    if word in data:
        word.lower()
        if len(data[word]) > 1:
            return ',\n '.join(data[word])
        print(type(data[word]))
        return data[word][0]
    # elif word.capitalize() and data[word].capitalize():
    #     return data[word][0]    
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]    
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(word, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We did not understand your entry. "        
    else:
        return "The word does not exist"    
            

#The instuctors way
# def translate(word):
#     word = word.lower()
#     if word in data:
#         return data[word]
#     elif len(get_close_matches(word, data.keys())) > 0:
#         return "Did you mean %s instead? " % get_close_matches(word, data.keys())[0]    
#     else:
#         return "The word does not exist."


while True:
    word = input("Please input a word, To Stop the program type Stop This: ")
    print(read_data(word)) 
    continue