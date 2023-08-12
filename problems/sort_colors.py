#  Leetcode problem ques : 75 [sort colours]
# Given an array nums with n objects colored red, white, or blue, sort them in-place 
# so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while high >= mid:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

nums = [2,0,1,2,0,0,1,2]
print(sort_colors(nums))