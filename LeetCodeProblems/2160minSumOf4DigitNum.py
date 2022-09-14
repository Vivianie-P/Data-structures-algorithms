"""
-
"""

def minimumSum(num: int) -> int:
    lst = []
    nums = str(num)

    for i in range(4):
        lst.append(nums[i])
    
    lst.sort()
    ans1 = str(lst[0]) + str(lst[2])

    ans2 = str(lst[1]) + str(lst[3])
    
    return int(ans1) + int(ans2)

    # num = sorted(str(num))
    # return int(num[0] + num[2]) + int(num[1] + num[3])

    # s = str(num)
    # s = "".join(sorted(s))
    # new1 = s[0] + s[2]
    # new2 = s[1] + s[3]

    # return int(new1)+int(new2)

num = 2932
print(minimumSum(num))

num = 4009
print(minimumSum(num))