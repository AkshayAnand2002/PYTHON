#https://leetcode.com/contest/weekly-contest-324/problems/count-pairs-of-similar-strings/
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count=0
        for i in range(0,len(words)-1):
            for j in range(i+1,len(words)):
                if set(words[i])==set(words[j]):
                    count+=1
        return count
