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