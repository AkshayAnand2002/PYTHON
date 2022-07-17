#Given a string s, find the length of the longest prefix, which is also a suffix. The prefix and suffix should not overlap.
#Simple Solution: Since overlapping prefixes and suffixes is not allowed, we break the string from the middle and start matching left and right strings. If they are equal return size of one string, else they try for shorter lengths on both sides.
# Python3 program to find length
# of the longest prefix which
# is also suffix
def longestPrefixSuffix(s) :
    n = len(s)
     
    for res in range(n // 2, 0, -1) :
         
        # Check for shorter lengths
        # of first half.
        prefix = s[0: res]
        suffix = s[n - res: n]
         
        if (prefix == suffix) :
            return res
            
    # if no prefix and suffix match
    # occurs
    return 0
     
# Driver Code
if __name__ == "__main__":
    s = "aabcdaabc"
    print(longestPrefixSuffix(s))
#OUTPUT IS 4 AS AABC IS SAME ON 2 SIDES OF THE LETTER D. 
