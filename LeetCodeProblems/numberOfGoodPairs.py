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


def numIdenticalPairs(nums: List[int]) -> int:
    pair_counter = 0
    my_dict = {}
    
    for idx, val in enumerate(nums):
        if val in my_dict:
            pair_counter += my_dict[val]
            print("\n pair counter:", pair_counter)
            my_dict[val] += 1
            print("val in my dictionary", my_dict[val])
        else:
            my_dict[val] = 1
            
    return pair_counter

nums = [1,2,3,1,1,3]
print("\n Test 1:", numIdenticalPairs(nums))

# nums = [1, 1, 1, 1]
# print("Test 2:", numIdenticalPairs(nums))

# nums = [1, 2, 3, 4, 5]
# print("Test 1:", numIdenticalPairs(nums))