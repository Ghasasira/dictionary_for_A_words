import json
from difflib import SequenceMatcher as match
from difflib import get_close_matches as near


file=json.load(open("DA.json","r"))

def checkingDictionary(userdata):
    userdata=userdata.upper()
    if userdata in file:

        return file[userdata]

    elif len(near(userdata,file.keys())) >0:
        print( "did you mean %s instead \n enter y for yes and n for no" %near(userdata,file.keys())[0])
        response = input("(y/n: )").lower()
        if response == "y":
             return file[(near(userdata,file.keys())[0])]
        else:
            return "word dont exist"

    else:
        #near(Searchedword, [file.keys()])
        return "word none Existant \n Double check it Please"


print("Welcome")
word = input("enter your word: ")
results=checkingDictionary(word)


if type(results) == dict:
    for key,value in results.items():
        print(key, ':' ,value)

else:
    print(results)