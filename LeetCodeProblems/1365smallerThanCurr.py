"""
- Given a list of integers this function finds out how many numbers in the list are 
smaller than the current number in the list
- Loop through the list the first time to have access to the element that 
you are trying to compare the other numbers in the list to
- Then create another loop to do the comparison to see if the other elements in the
list are smaller than the current number in the list.
- Returned the a differnet list of numbers that represent the amount of numbers that
are less than that number in the given list
- Complexity
    Time - O(n) because it can take n long to iterate through the list twice
    Space - O(n) because there can be n items appended to the new list
"""



def smallerNumbersThanCurrent(nums):
    nums2 = []

    for item in nums:

        count = 0

        for i in range(len(nums)):

            if item > nums[i]:

                count += 1

        nums2.append(count)
        
    return nums2

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))

nums = [7,7,7,7]
print(smallerNumbersThanCurrent(nums))
