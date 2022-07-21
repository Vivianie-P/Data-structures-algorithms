"""

"""



def smallerNumbersThanCurrent(nums):
    output = []

    for item in nums:

        count = 0

        for i in range(len(nums)):

            if item > nums[i]:

                count += 1

        output.append(count)
        
    return output

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))


