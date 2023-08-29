# Leetcode Ques : 283 [Move zeroes]

# Given an integer array nums, move all 0's to the end of it while maintaining the 
# relative order of the non-zero elements.


def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

nums = [0,1,0,3,12]
print(move_zeroes(nums))