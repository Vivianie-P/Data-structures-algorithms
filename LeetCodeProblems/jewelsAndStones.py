"""
- Given two strings jewels and stones. This function is checking how many jewels are 
in the stones string
- Used a hashmap to store all of the element of jewels
- Then checked if the string stones has any jewels in it
- Complexity
    Time - O(n + m) because when dealing with two for loops they get added up 
    Space - O(n) becuase jewels is being added to the hashmap which can be n elements
"""

def numJewelsInStones(jewels: str, stones: str) -> int:
        your_jewels = 0
        hashmap = {}
        
        for x in jewels:
            hashmap[x] = True
        
        for i in stones:
            if i in hashmap:
                your_jewels += 1
        return your_jewels



jewels = "aA" 
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))

jewels = "z"
stones = "ZZ"
print(numJewelsInStones(jewels, stones))