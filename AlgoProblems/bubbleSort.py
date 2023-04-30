from typing import List

def bubbleSort(array):
    isSorted = False
    swapCounter = 0

    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - swapCounter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        swapCounter += 1

    return array


array = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(array))

array = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]
print (bubbleSort(array))