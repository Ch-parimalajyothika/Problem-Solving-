ch = input("Enter an alphabet: ")

if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    if ch in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
