"""
-
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


# command = "G()(al)"
# print(command[4])
