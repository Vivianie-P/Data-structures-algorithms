# This method makes more sense to me while reading it
# and is the solution I was thinking but couldn't code 
# note wrtten: 03/03/2023
# def tandemBicycle (redShirtSpeeds, blueShirtSpeeds,fastest):
#     redShirtSpeeds.sort()
#     blueShirtSpeeds.sort(reverse = True)
#     maximum = []
#     minimum = []

#     for i in range(len(redShirtSpeeds)):
#         maximum.append(max(redShirtSpeeds[i], blueShirtSpeeds[i]))
#     blueShirtSpeeds.sort()

#     for i in range(len(blueShirtSpeeds)):
#         minimum.append(max(redShirtSpeeds[i], blueShirtSpeeds[i]))

#     if fastest == True:
#         return sum(maximum)
#     else:
#         return sum(minimum)
    

# This code sloution is the one given 
def tandemBicycle (redShirtSpeeds, blueShirtSpeeds,fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        redShirtSpeeds.sort(reverse = True)

    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
        totalSpeed += max(rider1, rider2)
    
    return totalSpeed


redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
fastest = True
print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))