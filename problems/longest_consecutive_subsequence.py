# Leetcode Ques : 128 [Longest Consecutive Subsequence]

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence

# Optimized using Hashset
def longest_consecutive(nums):
    max_length = 0
    hash_set = set(nums)
    for i in hash_set:
    # only if current element is the starting number then check its next consecutive numbers
        if i-1 not in hash_set: 
            cur_num = i
            cur_length = 1
            while cur_num + 1 in hash_set:
                cur_length += 1
                cur_num += 1

            max_length = max(max_length, cur_length)
    return max_length

nums = [100,101,4,200,1,102,103,2, 104, 105]
print(longest_consecutive(nums))

# Brute Force Method - TLE
# def longest_consecutive(nums):
#     max_length = 0
#     for i in nums:
#         curr_num = i
#         curr_length = 1
#         while curr_num + 1 in nums:
#             curr_length += 1
#             curr_num += 1

#         max_length = max(max_length, curr_length)
#     return max_length

