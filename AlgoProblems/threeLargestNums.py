# This function is simpler way to slove the same problem with finding
# the three largest numbers with the mindset to remove the largest
# numbers from the given array as you loop through and then 
# append throse values to the output array and then return it. 
#def findThreeLargestNumbers(array):
#     output = []

#     for i in range(0, 3):
#         output.insert(0, max(array))
#         array.remove(max(array))
#     return output

def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

# the idx in this function is the set indexes from the updateLargest function;
# the 0, 1, 2 are indexes of the threeLargest array we created in the 
# findThreeLargestNumbers func. We are passing in the idx so we can
# actually shift the numbers. 
def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1] 


array = [141, 1 ,17, -7, -17, 18, 8, 10, 541]
print(findThreeLargestNumbers(array))