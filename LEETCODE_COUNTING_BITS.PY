'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans= [0]*(n+1)
        for i in range(0,n+1):
            halfpos=math.floor(i/2)
            if i%2==1:
                ans[i]=ans[halfpos]+1 #using fact that no. of 1s is 1 more than floor
                                      # of i/2 for odd nos. i is the no in decimal system.
            else:                     # for even nos. no. of 1s is i/2 i is the no
                                      # in decimal system.
                ans[i]=ans[halfpos]
        return ans
