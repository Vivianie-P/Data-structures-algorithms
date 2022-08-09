"""
- Given a string of characters '(', ')', '{', '}', '[' and ']' this function determines 
if the input string is valid.
- An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
- This function uses a stack and a for loop to compare if the characters are valid by using multiple
condtional statements
- Once the loop begins the character is checked to see what type of character it is and 
the run the constional statements accorindingly to then return a boolean value 
- Complexity
    Time - O(n) because it can take n times to iterate through the string
    Space - O(1) because of the use of the stack you are only inserting/deleting an
    element once in constant time
"""


def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
                continue
                
            if char == ")":
                if stack != [] and stack[-1] == "(":
                    stack.pop()
                    continue
                else:
                    return False
            
            if char == "]":
                if stack != [] and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False
                
            if char == "}":
                if stack != [] and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False