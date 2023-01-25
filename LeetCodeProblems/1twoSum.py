from typing import List

"""
- Given a list and a target value this function finds the two elements in the
list that are equal to the target value. 
- Create a dictionary to hold the list with their index being the key and the number (or num) being the value. 
- Loop through entire list keeping track of index and value
- Check the dictionary for the difference of the target and each element
- If the difference is found in the dictionary, return list of the diff's index from hashmap and current index.
- If not found, store element in the hashmap
- Complexity: 
    Time - O(n) where n is the length of the list 
    Space - O(n) because at worst case the hashmap can take up the size of given list
"""

def twoSum(nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        # this is loop is looping through the entire list
        # keeping track of the index and the value of each num
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            
        return

nums = [2,7,11,15] 
target = 9
print("Test 1 Output: ", twoSum(nums, target))


nums = [3,2,4] 
target = 6
print("Test 2 Output: ", twoSum(nums, target))


