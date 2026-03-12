def maxProfit(prices):

    min_price = float('inf')
    max_profit = 0


    for price in prices:

        if price < min_price:
            min_price = price
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

# prices = [10,20,30,40,50,60]
prices = [5,3,6,2,1,10]

print("Maximum Profit:", maxProfit(prices))