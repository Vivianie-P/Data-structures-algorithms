class Solution:
    def smallerNumbersThanCurrent(self, nums):
        output = []

        for item in nums:

            count = 0

            for i in range(len(nums)):

                if item > nums[i]:

                    count += 1

            output.append(count)
            
        return output

func = Solution()
nums = [8,1,2,2,3]
print(func.smallerNumbersThanCurrent(nums))