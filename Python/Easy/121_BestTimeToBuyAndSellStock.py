"""

"""

arr = [2,4,1]

def test(prices):
    buy = prices[0]
    sell = 0

    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        
        profit = prices[i] - buy

        if profit > sell:
            sell = profit

    print(sell)
    return sell

test(arr)