'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals=[chr(x) for x in range(ord('A'),ord('Z')+1)]
        result=[]
        while columnNumber>0:
            result.append(capitals[(columnNumber-1)%26])
            columnNumber=(columnNumber-1)//26
        result.reverse()
        return ''.join(result)
      # https://www.youtube.com/watch?v=8XV3HMG5KwI&list=PL14c5UWFp9tQVNk8qtbpc_UFvhidOSopT&index=39
