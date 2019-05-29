import json
from difflib import SequenceMatcher
from difflib import get_close_matches

file = json.load(open("data.json"))

def explain(word):
    w = word.lower()
    if w in file:
        return file[w]
    elif len(get_close_matches(w, file.keys(), 1))>0:
        confirmation = input("Did you mean %s ? Type y/n: " % get_close_matches(w, file.keys(), 1)[0])
        if confirmation == "y":
            return file[get_close_matches(w, file.keys())[0]]
        elif confirmation == 'n':
            return 'Okay.'
        else:
            return 'I do not understand your input.'
    else:
        return 'Word is not in dictionary, please double check.'

word = input("Enter word: ")

print(explain(word))