import math
def primebyseive(n):
    seive=[]
    for i in range(0,n+1):
        seive.append(0)
    seive[0]=1
    seive[1]=1
    for i in range(2,int(math.sqrt(n+1))):
        if seive[i]==0:
            for j in range(2*i,n+1,i):
                seive[j]=1
    for i in range(2,n+1):
        if seive[i]==0:
            print(i)
primebyseive(100)
'''
OUTPUT:-
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
'''
