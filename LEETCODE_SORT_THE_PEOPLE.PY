'''
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
'''
#2 METHODS DONE BELOW ------>
# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         for i in range(len(heights)):
#             tall_index = heights.index(max(heights[i:]))
#             names[i], names[tall_index] = names[tall_index], names[i]
#             heights[i], heights[tall_index] = heights[tall_index], heights[i]
#         return names
#-----------------------------------------------------------------------------------------------------
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        y = list(zip(names,heights))#making name,height together as a single entity.
        z = []
        y.sort(key = lambda x:x[1],reverse = True)#for descending order of heights use lambda function.
        for i in y:
            z.append(i[0])
        return z  
