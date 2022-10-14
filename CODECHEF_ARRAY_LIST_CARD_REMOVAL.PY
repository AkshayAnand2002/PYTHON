'''
https://www.codechef.com/submit/REMOVECARDS?tab=statement
'''
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))# taking list or array input.
    b=[0]*101 # initializing array elements by 0.
    for i in a:
        b[i]+=1 # counting occurence of each elem of array a.
    print(n-max(b)) #this gives min no. of moves so that all remaining cards on table
    #have same no. written on it.
