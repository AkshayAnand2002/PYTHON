'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:
Input: nums = [2,2,1]
Output: 1
Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
Example 3:
Input: nums = [1]
Output: 1
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}#DICTONARY USED
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        for num in nums:
            if freq[num]==1:
                return num
##########################################################
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc=0 #XOR APPROCAH
        for num in nums:
            acc^=num
        return acc
    #SAME VALUES EXORED GIVE RESULT 0.
    #DIFFERENT VALUES EXORED GIVE THE RESULT AS NO. WHICH IS PRESENT ONCE OR UNIQUE.
