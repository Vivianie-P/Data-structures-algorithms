"""
-
"""


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS = {}
    countT = {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for char in countS:
        if countS[char] != countT.get(char, 0):
            return False
        
    return True

    # return Counter(s) == Counter(t)
    # return sorted(s) == sorted(t)

s = "anagram" 
t = "nagaram"
print(isAnagram(s,t))

s = "rat" 
t = "car"
print(isAnagram(s,t))

s = 'racecar'
t = 'rraacce'
print(isAnagram(s,t))

s = "valid"
t = "salad"
print(isAnagram(s,t))