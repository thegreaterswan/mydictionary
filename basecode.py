import json #import json module
from difflib import get_close_matches

data = json.load(open("PythonMegaCourse/dictionary/data.json")) #loads json file into data variable 
#this json file is a list of all of the keys in a dictionary

def translate(w): #setting up a whole function block to complete the desired task
    w = w.lower() #puts w in lower case and reassigns it to the variable w
    matches = get_close_matches(w, data.keys(),n=999,cutoff=0.5) #putting the matches into a data set

    if w in data:
        return data[w]  #have to use [] instead of () or you will get an error

    elif w.title() in data: #checks to see if the upper case version is in the dictionary
        return data[w.title()]
    
    elif w.upper() in data: #capitalizes the entire word and checks it 
        return data[w.upper()]

    elif len(matches) > 0: #determines that if there is a list of like words at all
        yn = ''
        x = 0

        while yn != "Y": #settign up a conditional loop so we can cycle through all the words until we find the one is most similar
            yn = input(f"Did you mean {matches[x]}? ") #pulls the most statistically similar words in order of similarity
            yn = yn.upper() #upper cases

            if yn == "Y":
                return data[matches[x]] 

            else: 
                x = x + 1 #go onto next possible option
                continue

    else: #if none of the conditions above fix the problem it exits the program gracefully and tells the user they are dumb
        return "the word doesnt exist please double check."

word = input("enter word: ")

output = translate(word)

if type(output) == list:#this block is making sure it can properly print the output in a good format
        for item in output:
            print(item)

else:
    print(output)

