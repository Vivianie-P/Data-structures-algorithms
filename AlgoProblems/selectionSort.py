from typing import List

def selectionSort(array):
    currentIdx = 0
# this while loop is bringing the currentIdx to the len of the array - 1 
# because once our currentIdx gets to the last idx in the list there
# would be no more swaps to make because that last number will be in it's
# final position.
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        # swap(currentIdx, smallestIdx, array)
        array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
        currentIdx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    # array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]

array = [8, 5, 2, 9, 5, 6, 3]
print(selectionSort(array))