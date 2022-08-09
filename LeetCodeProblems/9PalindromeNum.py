"""
- Given an integer this function checks of the int is a palindrome 
- Because int's are immutable the int is first stringifyed so it can
be iterable
- Then this function has two pointers; one that points to the first 
index and another that point to the last index
- The pointers act as indexes to compare the values at that index and 
to see if we have iterated through the entire string.
- The loop iterates through the string and returns a boolean value to
see if the string is a palindrome or not
- Complexity
    Time - O(n) where n is the number of elements that gets iterated over
    Space - O(1) no extra memory is being used
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