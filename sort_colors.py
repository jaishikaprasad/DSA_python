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