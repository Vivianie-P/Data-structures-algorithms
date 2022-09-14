"""
-
"""


def balancedStringSplit(s: str) -> int:
    match = 0
    character = 0
    
    for letter in s:
        if letter == "R":
            character += 1
        if letter == "L":
            character -= 1
        if character == 0:
            match += 1
    return match

s = "RLRRLLRLRL"
print(balancedStringSplit(s))

s = "RLRRRLLRLL"
print(balancedStringSplit(s))