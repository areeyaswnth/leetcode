
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max=-2147483648
        nums.sort()
        ls=[nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1]]
        if(ls[0]>ls[1]):
            return ls[0]
        else:
            return ls[1]
