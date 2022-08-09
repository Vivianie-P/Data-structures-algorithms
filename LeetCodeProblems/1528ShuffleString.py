from typing import List

"""
-
"""

def restoreString(s: str, indices: List[int]) -> str:
    # hashmap = {}
    # for i in s:
    #     hashmap[i] = 1
    #     print(hashmap)
    answer = ""

    for i in range(len(indices)):
        print(i)
        answer += s[indices.index(i)]
    return answer


s = "codeleet" 
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))
