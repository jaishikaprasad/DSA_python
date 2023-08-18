# Leetcode Ques : 70 [climbing Stairs]

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Optimized Approach
def climbing_stairs(n):
    prev1 = 0
    prev2 = 1
    for i in range(1,n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    return curr
print(climbing_stairs(3))

# output : 3

# Recursion - Time Limit Exceed
# def climbing_stairs(n):
#     if n == 1 or n==2:
#         return n
#     return climbing_stairs(n-1) + climbing_stairs(n-2)


# Tabulation
# def climbing_stairs(n):
#     if n == 1:
#         return 1
#     dp = [0]*(n+1)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2]

#     return dp[n]
