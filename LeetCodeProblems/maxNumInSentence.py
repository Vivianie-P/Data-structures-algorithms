from typing import List

"""
- Given a string of sentences this function finds the senstence with the largest
amount of words and returns that amount
- An empty variable is made then a Loop was made to go through the string of 
sentences 
- Then a space is added at the end of the sentence to get the amount of words 
in the sentence
- Once the amount of words is found the empty variable is updated with the max method 
to then find the maximum number from the amount of words it was given
- Finally, the maximum number is returned
- Complexity
    Time - O(n) because the string sentences can have n elements to iterate through
    Space - O(1) because nothing is taking up any memeory in this function

"""

def mostWordsFound(self, sentences: List[str]) -> int:
        max_word = 0
        for i in sentences:
            word = (i.count(" "))+1       
            max_word = max(max_word,word)
        return max_word


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))

sentences = ["please wait", "continue to fight", "continue to win"]
print(mostWordsFound(sentences))
