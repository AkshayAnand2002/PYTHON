'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if i in ["(","[","{"]:
                stk.append(i)
            else:
                if len(stk)==0:
                    return False
                ch=stk.pop()
                if (i == ")" and ch=="(") or \
                (i == "]" and ch=="[") or \
                (i == "}" and ch=="{"):
                    continue
                else:
                    return False
        return True if len(stk)==0 else False
