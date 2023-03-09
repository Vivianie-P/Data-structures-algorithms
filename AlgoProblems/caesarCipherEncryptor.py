def caesarChipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
        print("this is the new letters array before using the ''.join func: ",newLetters)
        print("this is the new letters array after using the ''.join func: ","".join(newLetters))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    # print("this is the new letter code: ",newLetterCode)
    # print("this is the new letter char: ",alphabet[newLetterCode % 26])
    return alphabet[newLetterCode % 26]




string = "vwxyz"
key = 1
print(caesarChipherEncryptor(string, key))