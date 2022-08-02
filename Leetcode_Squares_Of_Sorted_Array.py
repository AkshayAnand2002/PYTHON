class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[];
        start,end=0,len(nums)-1
        while(start<=end):
            if (nums[start] **2 > nums[end] ** 2):
                result.append(nums[start] ** 2)
                start+=1
            else:
                result.append(nums[right] ** 2)
                end-=1
        return result[::-1]#to get non-decreasing order
#Step1:
#Create an empty array to store the squared values.
#result = []
#Step2:
#Initialize our 2 pointers: left and right, and set them equal to the first and last index
#positions of the array.
#left, right = 0, len(nums) - 1
#Step3:
#We can run a while loop and continue till our left pointer is greater than the right pointer.
#meaning till they cross each other in the array
#while left <= right:
#Step4:
#If the square of the number on the right is greater than the square of the left number then
#append it to the result array and decrease the right pointer
#Or
#append the left square and increase the left pointer.
#           if nums[left] ** 2 < nums[right] ** 2:
 #               result.append(nums[right] ** 2)
  #              right -= 1             
   #         else:
   #             result.append(nums[left] ** 2)
   #             left += 1
#Step5:
#After this we will end up with the result array but it is in descending order.
#To make it in ascending order we can just reverse it like:
#return result[::-1] 
#ANSWER---https://leetcode.com/problems/squares-of-a-sorted-array/discuss/2319821/Python-O(n)-solution-explained
#THE ABOVE CONCEPT IS EXPLAINED IN ->
#https://www.youtube.com/watch?v=93tLZBYb2Po&list=PLnfCacCyFMlaDIwrB5b5akGtrmHvqu4yv&index=3&t=2s
