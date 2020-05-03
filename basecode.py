import json #import json module
from difflib import get_close_matches

data = json.load(open("course/dictionary/data.json")) #loads json file into data variable 
#this json file is a list of all of the keys in a dictionary
def translate(w):
    w = w.lower() #puts w in lower case and reassigns it to the variable w
    matches = get_close_matches(w, data.keys(),n=7,cutoff=0.5)
    if w in data:
        return data[w]  #have to use [] instead of () or you will get an error
    elif len(matches) > 0: #determines that if there is a list of like words at all
        yn = input(f"Did you mean {matches[0]} instead? ") #pulls the most statistically similar word
        yn = yn.upper #upper cases
        if yn == "Y":
                return data[matches[0]] 
        else:
            yn2 = input(f"Did you mean {matches[1]} instead? ") #goes to second most like word
            yn2 = yn2.upper()
            if yn2 == "Y":
                return data[matches[1]]
    else:
        return "the word doesnt exist please double check."

word = input("enter word: ")

output = translate(word)
if type(output) == list:#this block is making sure it can properly print the output in a good format
        for item in output:
            item.capitalize()
            print(item)
else:
    print(output)
