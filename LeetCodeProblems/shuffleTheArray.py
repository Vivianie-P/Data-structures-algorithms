from typing import List

"""
-
"""


def shuffle(nums: List[int], n: int) -> List[int]:
    result = []

    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result

nums = [2,5,1,3,4,7] 
n = 3
print(shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))