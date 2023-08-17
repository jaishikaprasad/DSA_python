#  Leetcode Ques : Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from 
# the very left of the array to the very right. You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position.
# Return the max sliding window

# optimized Approach
import collections
def sliding_max_window(nums, k):
    # store the indeces of elements
    q = collections.deque()
    result = []
    # remove from right side until a smaller element occurs
    for i in range(len(nums)):
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        q.append(i)

         # if window is not full continue
        if i+1 < k:
            continue
        # if the window exceeds remove the extra items from left
        if q[0] < i-k+1:
            q.popleft()
        # at deque front max element will be there
        result.append(nums[q[0]])
    return result
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sliding_max_window(nums,k))

# output = [3, 3, 5, 5, 6, 7]  

# # Brute Force Approach - gives Time Limit Exceed
# def sliding_max_window(nums, k):
#     left = 0
#     right = k
#     result = []
#     while right <= len(nums):
#         maximum = -2**64
#         for i in range(left, right):
#             if nums[i] > maximum:
#                 maximum = nums[i]

#         result.append(maximum)
#         left += 1
#         right += 1

#     return result
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# print(sliding_max_window(nums,k))