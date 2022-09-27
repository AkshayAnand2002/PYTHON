'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht=dict()#dictionary key as num as value as no. of times which changes
        for num in nums1:
            if num in ht:
                ht[num]+=1
            else:
                ht[num]=0
                ht[num]+=1
        result=[]
        for num in nums2:
            if num in ht and ht[num]>0:
                ht[num]-=1 #to keep check of count of num if nums2 has more than that of nums1 
                #so intersection will contain of no of times that is present in nums1.
                result.append(num)
        return result
