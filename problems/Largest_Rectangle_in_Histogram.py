

# Brute Force - Time Limit Exceed
# def largest_Rectangle_Area(heights):
#     result = 0
#     for i in range(len(heights)):
#         curr = heights[i]
#         breadth = 1
#         for j in range(i+1,len(heights)):
#             if heights[j] > curr:
#                 breadth += 1
#             else:
#                 break

#         for j in range(i-1, -1,-1):
#             if heights[j] > curr:
#                 breadth += 1
#             else:
#                 break
#         area = curr * breadth
#         result = max(result, area)
#     return result
# heights = [2,1,5,6,2,3]
# print(largest_Rectangle_Area(heights))
        
