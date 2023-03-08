def caesarChipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    print("this is the new letter code: ",newLetterCode)
    print("this is the new letter char: ",alphabet[newLetterCode % 26])
    return alphabet[newLetterCode % 26]




string = "xyz"
key = 2
print(caesarChipherEncryptor(string, key))