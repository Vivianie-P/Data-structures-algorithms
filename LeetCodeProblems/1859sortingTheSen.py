"""
-
"""

def sortSentence(s: str) -> str:
    new_s = s.split(" ")
    output = ""
    
    for i in range(len(new_s)):
        min_idx = i 
        for j in range( i+1, len(new_s)):
            if new_s[j][-1] < new_s[min_idx][-1]:
                min_idx = j
        if i != min_idx:
            new_s[min_idx], new_s[i] = new_s[i], new_s[min_idx]
        output += new_s[i][:-1] + ' '
    return (output)

    


s = "is2 sentence4 This1 a3"
print(sortSentence(s))

s = "dogs4 love2 I1 all3"
print(sortSentence(s))