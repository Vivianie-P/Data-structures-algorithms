"""
-
"""



def lengthOfLastWord(s: str) -> int:
    current_word_list = []
    new_word_list = []
    new_s = s.strip()
    
    for i, char in enumerate(new_s):
        if i == len(new_s) - 1:
            current_word_list.append(char)
            new_word_list.append("".join(current_word_list))
            print("New Word list: ", new_word_list)
            current_word_list.clear()
        elif char == " ":
            new_word_list.append("".join(current_word_list))
            print("New Word list: ", new_word_list)
            current_word_list.clear()
        else:
            current_word_list.append(char)

    print("\nNew word list: ", new_word_list)
    return len(new_word_list[-1])

    # new_s = s.strip()
    # word_list = new_s.split()
    # return len(word_list[-1])

    # counter = 0
    # for char in reversed(new_s):
    #     if char == ' ':
    #         return counter
    #     else:
    #         counter += 1
    # return counter

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
