# Leetcode Ques : 217 [Contains Duplicate]
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def contains_duplicate(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False

nums = [1,2,3,1]
print(contains_duplicate(nums))

# output : true