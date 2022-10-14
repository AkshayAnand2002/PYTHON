'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"  
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #if length of the s is less than the k then all letters will get reversed
        if len(s)<k:
            return s[::-1]
        
        i=0 #the left pointer which will everytime will be the first character of the 2k length substring
        j=0 #the right pointer which will check if the 2k length substring present in the s or not
        st="" #the result string
        
        #the loop will work if the k length substring will be present in the string s
        while i<len(s) and i+k-1<len(s):
            #joining the k length substring after reversing
            st=st+"".join(reversed(s[i:i+k]))
            #pointer j (right side) will get updated to the 2k characters ahead in the s
            j+=2*k
            #if the pointer j gets equal or bigger to the indeces of string then end the process
            #as it may not have k total length characters in the s anymore (must be less than k)
            if j>=len(s):
                break 
            #otherwise the substring which is being skipped after every 2k elements need to be appended
            #to the string st as it is (should not reversed)
            st=st+s[i+k:j]
            #and then the i will also get ahead of 2k elements
            i=j 
            
        #if fewer elements are still remaining in the s (which is less than the next 2k charcters)
        #means the string would have finished before the next i can go to the next 2k character
        #in short neither i is present nor j in s (if r!=0)
        r=len(s)-len(st)
        
        #this is the condition if the i would have reached to the first character of the 2k length 
        #substring but not having the total 2k length of the substring , means i present under the
        # length of s but j would be greater than the length of s 
        #in short i is present but not j in s , so from ith index remaining characters will get reversed
        
        if len(s)-i<k:
            return st+"".join(reversed(s[i:i+k]))
        
        #if r not 0 then all the characters will be appended to the st as it is
        elif r:
            st=st+s[len(s)-r:]
        
        return st  
