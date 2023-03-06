def nonConstructibleChange(coins):
    coins.sort()
    minAmtChange = 0
    
    for coin in coins:
        if coin > minAmtChange + 1:
            return minAmtChange + 1
        else:
            minAmtChange += coin
            
    return minAmtChange + 1


coins = [5, 6, 9, 1, 4, 3, 7, 2]
print(nonConstructibleChange(coins))

