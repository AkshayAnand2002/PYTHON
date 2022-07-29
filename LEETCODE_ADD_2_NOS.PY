#https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_number(self,arr):
        firstnum=''
        node1 = arr
        while node1:
            firstnum+=str(node1.val)
            node1=node1.next
        firstnum=firstnum[::-1]
        return int(firstnum)
    def create_listnode(self,result):
        lsnode=None
        for i in str(result):
            lsnode=ListNode(val=i,next=lsnode)
        return lsnode
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = self.get_number(l1)
        second = self.get_number(l2)
        result = first+second
        return self.create_listnode(result)
