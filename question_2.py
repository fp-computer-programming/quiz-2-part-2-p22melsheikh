# MEE 12/09/21

sentence = input(" enter a positive or negative sentence: ")

s1 = sentence
s1.lower()

if "not" not in s1:
    print("You're not " + s1 + ". Now SCRAM!")
elif "not" in s1:
    if "not" == s1: 
        print("can you say anything other than not" )
    else:
        print(sentence)