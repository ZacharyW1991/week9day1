# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
#  with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the sort function!

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# def solution(nums):
#     output=[]
#     for n in nums:
#         if n==0:
#             output.append(n)
#     for n in nums:
#         if n==1:
#             output.append(n)
#     for n in nums:
#         if n==2:
#             output.append(n)
#     return output

def solution(my_arr):
    zeroes = []
    ones = []
    twos = []
    for x in my_arr:
        if x == 0:
            zeroes.append(x)
        elif x == 1:
            ones.append(x)
        elif x == 2:
            twos.append(x)
    full_list = zeroes + ones + twos
    for x in range(len(full_list)):
        my_arr[x] = full_list[x]
    return my_arr