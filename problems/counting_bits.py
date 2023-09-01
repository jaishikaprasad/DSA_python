def counting_bits(n):
    dp = [0]
    for i in range(1, n+1):
        if i % 2 == 0:
            dp.append(dp[i//2])
        else:
            dp.append(dp[i//2] + 1)
    return dp

# Brute Force Approach - O(nlog)
# def counting_bits(n):
#     result = []
#     for i in range(n+1):
#         binary = bin(i)
#         ones = binary.count("1")
#         result.append(ones)

#     return result

print(counting_bits(5))
