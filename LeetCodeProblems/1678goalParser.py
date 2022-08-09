"""
- Given a string that consists of 'G', '()', and/or '(al)' this function 
changes the value of '()' to "o" and '(al)' to "al"
- A variable was made to hold the new value of given string
- Looped through the string to check each element in the string and chnaged
the elements to "o" and "al" 
- Then returned the new string
- Another way of solving this problem is using the .replace() method which is
commented out at the bottom.
- Complexity
    Time - O(n) where n represents the amount of elements in the string
    Space - O(n) where n represents the amount of elements in the new string
- Complexity for the .replace() method
    Time - O(n) where n represents the elements that has to be changed
    Space - O(1) because the .replace method is changing the elements without
    a loop
"""

def interpret(command: str) -> str:
    newStr = ""
    for i in range(len(command)):
        if command[i] == "G":
            newStr += "G"
        elif command[i] == "(":
            if command[i+1] == ")":
                newStr += "o"
            else:
                newStr += "al"
    return newStr


    # command = command.replace('()','o')
    # command = command.replace('(al)','al')
    # return command


command = "G()(al)"
print(command)
