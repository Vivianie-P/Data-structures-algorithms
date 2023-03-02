def generateDocument(characters, document):
    charactersHash = {}

    for char in characters:
        if char not in charactersHash:
            charactersHash[char] = 1
        else:
            charactersHash[char] += 1
            
    for char in document:
        if char not in charactersHash or charactersHash[char] == 0:
            return False
        
        charactersHash[char] -= 1
    
    return True


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
print(generateDocument(characters, document))

