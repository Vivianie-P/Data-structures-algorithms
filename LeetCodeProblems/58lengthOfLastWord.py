"""
- Given a string of words this function finds thw lengt5h of the last 
word in the string.
- Two lists were made; one to hold the the current word in the string
and the other list is used to get the length of the last word in the
string
- An edgecase is accounted for if the sring has multiple spaces at the 
beginning & end of the string.
- This function has a loop that checks if the element is the last 
element in the string if it is then the element is being counted and
being added to an empty list to then be returned. 
- There are also two other solutions to this question commented out this
summary is of the burte force solution
- Complexity
    Time - O(n) where n is the length of the given string
    Space - O(n) where n is the amount of elements in the new list
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
