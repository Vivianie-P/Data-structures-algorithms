from typing import List

"""
- Given an list of integers this function is returning the amount of 
possible pairs in the list.
- Used a hashmap to store the number in the list(key) and its occurances(value)
- The occurance and the counter variable are incremented each time they are 
seen 
- Once the loop is completed the counter variable is returned.
- Complexity:
    Time - O(n) because each element in the listed has to be visted
    Space - O(n) because each element can be added to the hashmap n times
"""


def numIdenticalPairs(self, nums: List[int]) -> int:
    pair_counter = 0
    my_dict = {}
    
    for idx, val in enumerate(nums):
        if val in my_dict:
            pair_counter += my_dict[val]
            my_dict[val] += 1
        else:
            my_dict[val] = 1
            
    return pair_counter