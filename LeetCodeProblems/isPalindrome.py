"""
-
"""


def isPalindrome(x: int) -> bool:
    new_x = str(x)
    left = 0
    right = len(new_x)-1
    
    while left < right:
        if new_x[left] == new_x[right]:
            left += 1
            right -= 1
            print(left)
            print(right)
        else:
            return False
    return True
    
    # if new_x == new_x[::-1]:
    #     return True
    # else:
    #     return False

x = 12345
print(isPalindrome(x))

x = 12321
print(isPalindrome(x))

x = 9
print(isPalindrome(x))