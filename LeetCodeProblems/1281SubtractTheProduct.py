"""
- Given an integer this function is finding the multiplication total and sum of 
the indivdual numbers within the integer and returning the difference of those
totals
- Created some variables that are being used to hold the multipl. total and the 
sum
- The integer gets changed to a string to become an iterable
- Looped through to get the multipl. total and the sum of the numbers.
- The returned value is the difference between the totals.
- Complexity
    Time - O(n) where n represents the amount of elements in the string
    Space - O(1) because nothing is taking up enough space to change the memory 
"""

def subtractProductAndSum(n: int) -> int:
    prodTotal = 1
    sumTotal = 0
    numbers = str(n)
    
    for i in numbers:
        prodTotal *= int(i)
        print("multiplication total: ", prodTotal)
        sumTotal += int(i)
        print("addition total: ",sumTotal)
    return prodTotal - sumTotal

n = 234
print(subtractProductAndSum(n))