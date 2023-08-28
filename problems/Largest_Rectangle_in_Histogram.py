# Leetcode Ques : 84 [Largest Rectangle in Histogram]
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.

# optimized Approach

# Find the smallest from right side by start comparing from the end
def right_small(heights):
    stack = []
    n = len(heights)
    right = [-1]*n
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    return right

# Find the smllest from the left side by comparing from start
def left_small(heights):
    stack = []
    n = len(heights)
    left = [-1]*n
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    return left

def largest_rectangle_area(heights):
    left = left_small(heights)
    right = right_small(heights)
    max_area = 0
    for i in range(len(heights)):
        length = heights[i]
        if right[i] == -1:
            right[i] = len(heights)
        breadth = right[i] - left[i] - 1
        area = length * breadth
        max_area = max(max_area, area)
    return max_area


# Brute Force - Time Limit Exceed

def largest_Rectangle_Area(heights):
    result = 0
    for i in range(len(heights)):
        curr = heights[i]
        breadth = 1
        for j in range(i+1,len(heights)):
            if heights[j] > curr:
                breadth += 1
            else:
                break

        for j in range(i-1, -1,-1):
            if heights[j] > curr:
                breadth += 1
            else:
                break
        area = curr * breadth
        result = max(result, area) 
    return result

heights = [2,1,5,6,2,3]
print(largest_rectangle_area(heights))

# Output : 10
        
