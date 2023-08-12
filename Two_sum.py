# Leetcode Ques:1 [TWO SUM]
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

def two_Sum(nums, target):
    d = dict()
    for i in range(len(nums)):
        d[nums[i]] = i
    for i in range(len(nums)):
        need = target - nums[i]
        if need in d.keys() and d[need] != i:
            return i, d[need]
        
nums = [2,7,11,15]
target = 9
print(two_Sum(nums, target))

# output = (0,1)