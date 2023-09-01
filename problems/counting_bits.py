# Leetcode Ques : 338 [Counting Bits]

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

# Dynamic Programming
def counting_bits(n):
    dp = [0]
    for i in range(1, n+1):
        if i % 2 == 0:
            dp.append(dp[i//2])
        else:
            dp.append(dp[i//2] + 1)
    return dp

# Brute Force Approach - O(nlog)
def counting_bits(n):
    result = []
    for i in range(n+1):
        binary = bin(i)
        ones = binary.count("1")
        result.append(ones)

    return result

print(counting_bits(5))

# Output : [0, 1, 1, 2, 1, 2]
