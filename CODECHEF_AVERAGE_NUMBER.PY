'''
https://www.codechef.com/LTIME69A/problems/AVG
'''
t=int(input())
for j in range(t):
    n,k,v=map(int,input().split())
    np=(input().split(" "))
    a=[int(x) for x in np]
    total=(n+k)*v-sum(a)
    ele=total/k
    ele2=total//k
    if ele==ele2 and ele>=1:
        print(ele2)
    else:
        print(-1)
