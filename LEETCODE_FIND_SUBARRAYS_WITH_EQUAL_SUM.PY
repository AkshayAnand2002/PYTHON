'''
Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

Return true if these subarrays exist, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [4,2,4]
Output: true
Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.
Example 2:

Input: nums = [1,2,3,4,5]
Output: false
Explanation: No two subarrays of size 2 have the same sum.
Example 3:

Input: nums = [0,0,0]
Output: true
Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0. 
Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.
'''
'''
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums=set()
        for i in range(len(nums)-1):
            t=nums[i]+nums[i+1]
            if t in sums:
                return True
            else:
                sums.add(t)
        return False
'''
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        all_sums = []
        for i in range(0, len(nums) - 1):
            if nums[i] + nums[i + 1] in all_sums:
                return True
            else:
                all_sums.append(nums[i] + nums[i + 1])
    
        return False

'''
class Solution:
	def findSubarrays(self, nums: List[int]) -> bool:

		dictionary = {}

		for i in range(len(nums) - 1):

			subarray_sum = sum(nums[i:i+2])

			if subarray_sum not in dictionary:

				dictionary[subarray_sum] = nums[i:i+2]
			else:
				return True

		return False
'''
