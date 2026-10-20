def maxProfit(prices):
    maxProfit=0
    minprice=prices[0]

    for i in range(1,len(prices)):
        profit=prices[i]-minprice
        maxProfit=max(profit,maxProfit)
        minprice=min(prices[i],minprice)
    return maxProfit

prices=[7,1,5,3,6,4]
print(maxProfit(prices))

        