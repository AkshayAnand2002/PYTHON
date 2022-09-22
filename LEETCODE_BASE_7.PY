'''
Given an integer num, return a string of its base 7 representation.
Example 1:
Input: num = 100
Output: "202"
Example 2:
Input: num = -7
Output: "-10"
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        result=''
        n=num
        num=abs(num)
        if(num==0):return '0'
        while(num>0):
            rem=num%7
            result+=str(rem)
            num=num//7
        if(n<0):
            return '-'+result[::-1]
        else:
            return result[::-1]
