# Leetcode Ques : 121 [Best Time to Buy and Sell Stock]

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in 
# the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxprofit(prices):
    min_price = prices[0]
    max_profit = 0

    for stock in prices:
        if stock < min_price:
            min_price = stock
        if stock - min_price > max_profit:
            max_profit = stock - min_price
            
    return max_profit

prices = [7,1,5,3,6,4]
print(maxprofit(prices))

# output : 5