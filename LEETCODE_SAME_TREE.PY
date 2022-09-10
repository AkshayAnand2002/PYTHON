'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2] #1,2 MEANS 2 IS LEFT CHILD OF 1. 1,NULL,2 MEANS NULL OR NO LEFT CHILD AND 2 IS THE RIGHT CHILD OF 1.
Output: false
Example 3:
Input: p = [1,2,1], q = [1,1,2] #FOR P: 2 IS THE LEFT CHILD OF 1 AND 1 IS RIGHT CHILD OF 1. FOR Q: 1 IS THE LEFT CHILD OF 1 AND 2 IS THE RIGHT CHILD OF 1.
Output: false
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if(p==None and q!=None) or (p!=None and q==None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
