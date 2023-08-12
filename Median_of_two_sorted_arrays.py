# Leetcode ques: 4 [Median of 2 Sorted arrays]
# Return the median of the two sorted arrays.

def median_of_two_sorted_arrays(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)

    if n1 > n2 :
        return median_of_two_sorted_arrays(nums2, nums1)
    
    low = 0
    high = n1

    int_min = -2**64
    int_max = 2**64

    while high >= low:
        cut1 = (low + high) // 2
        cut2 = ((n1 + n2 + 1)//2) - cut1

        left1 = nums1[cut1-1] if cut1 > 0 else int_min
        right1 = nums1[cut1] if cut1 < n1 else int_max
        left2 = nums2[cut2-1] if cut2 > 0 else int_min
        right2 = nums2[cut2] if cut2 < n2 else int_max

        if right2 >= left1 and left2 <= right1:
            if (n1 + n2) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            else:
                return max(left1, left2)
        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1

    return 0.0

nums1 = [1,2]
nums2 = [3,4]
print(median_of_two_sorted_arrays(nums1, nums2))

# Output = 2.5
