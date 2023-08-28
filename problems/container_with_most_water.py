# Leetcode Ques : 11 [container with most water]

# You are given an integer array height of length n. There are n vertical lines drawn such that the two 
# endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

def max_water(height):
    area = 0
    low = 0
    high = len(height) -1

    while high > low:
        i = height[low]
        j = height[high]

        if i > j :
            water = j* (high - low)
            high -= 1
        else:
            water = i*(high - low)
            low += 1

        if water > area:
            area = water

    return area

height = [1,8,6,2,5,4,8,3,7]
print(max_water(height))

# Output : 49
