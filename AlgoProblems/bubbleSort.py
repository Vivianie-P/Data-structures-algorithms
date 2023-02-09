from typing import List

def bubbleSort(array):
    isSorted = False

    while not isSorted:
        isSorted = True
        for x in range(len(array) - 1):
            if array[x] > array[x+1]:
                array[x], array[x+1] = array[x+1], array[x]
                isSorted = False
    return array


array = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(array))

array = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]
print (bubbleSort(array))