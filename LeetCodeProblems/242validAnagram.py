"""
*An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once*

- Given two strings s and t, this func returns true if t is an anagram of s, 
and false otherwise.
- A conditional is made to chack the length of each string because if the 
strings aren't equal t isn't an anagram of s.
- Two hasmaps are created to hold the elements from each string as the key
and their occurences as the value
- The first for loop is adding the elemets to their specific hashmaps
- Then the second for loop is comparing the elements in each hasmap to see
if the strings t is anagram of s.
- A boolean value is returned 
- Complexity
    Time - O(n + m) becuase both of the strings have to iterated through
    Space - O(n + m) because each hashmap can potenially go up the amount of 
    elements in the strings.
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