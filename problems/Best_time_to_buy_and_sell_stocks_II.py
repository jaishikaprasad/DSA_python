# Leetcode Ques : 122 [Best Time to Buy and Sell Stock II]

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

def maxprofit(prices):
    max_profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]

    return max_profit

prices = [7,1,5,3,6,4]
print(maxprofit(prices))

# output : 7