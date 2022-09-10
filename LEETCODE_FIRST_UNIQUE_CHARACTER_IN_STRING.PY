'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_dict={}
        for ch in s:
            if ch not in str_dict:
                str_dict[ch]=True
            else:
                str_dict[ch]=False
        for i,c in enumerate(s):
            if str_dict[c]:
                return i
        return -1
            
