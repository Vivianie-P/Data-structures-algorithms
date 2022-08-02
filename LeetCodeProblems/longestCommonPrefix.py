from typing import List

"""
- Given a list of strings this function is finding the longest prefix amoungst
a list of strings
- The first for loop is lopping through the index of the first string. The 
second for loop is looping through the string itself. 
- Then you're checking if the index is the same length as the string or if the 
string string's first index isn't the same value as the first element in the list.
- If either of these conditionals are met we return the value in the prefix or we 
get out of the loop and append the letters that make the prefix and return that 
value
- Complexity
    Time - O(n) because the string can have n elements in it 
    Space - O(1) nothing is taking up memory in this function.

"""

def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    
    return prefix


# strs = ["dog","racecar","car"]
# print(longestCommonPrefix(strs))

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

# strs = ["insert", "inspection", "infiltrate"]
# print(longestCommonPrefix(strs))