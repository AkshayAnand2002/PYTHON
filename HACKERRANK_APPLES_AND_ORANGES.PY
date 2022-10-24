#https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count_apple=0
    count_orrange=0
    ans=[]
    for i in apples:
        index=i+a
        if index>=s and index<=t:
            count_apple+=1
    ans.append(count_apple)
    for j in oranges:
        index1=j+b
        if index1>=s and index1<=t:
            count_orrange+=1
    ans.append(count_orrange)
    for i in ans:
        print(i)
