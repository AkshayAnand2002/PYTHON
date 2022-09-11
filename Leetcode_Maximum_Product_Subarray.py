'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max=float(-inf)
        local_max=1
        local_min=1
        for n in nums:
            prev_max=local_max*n
            local_max=max(n,local_max*n,local_min*n)
            local_min=min(n,prev_max,local_min*n)
            global_max=max(global_max,local_max)
        return global_max
