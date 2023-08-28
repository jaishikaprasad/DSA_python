# Leetcode Ques : 88 [Merge Sorted Array]

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

def merge_Sorted_array(nums1, m, nums2, n):
    i = m-1
    j = n-1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

print(merge_Sorted_array(nums1, 3, nums2, 3))

# Output : [1, 2, 2, 3, 5, 6]