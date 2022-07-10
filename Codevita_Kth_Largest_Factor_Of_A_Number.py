#Every positive integer k has atleast 2 factors 1 and the no. k itself.
#Given 2 positive integers N and k write a program to print kth largest factor.
#Input-comma separated list of positive integer pairs(N,k)
#Output-The kth largest factor . If N does not have k factors output should be 1.
#THE KTH LARGEST FACTOR WILL BE THE KTH INDEX ELEMENT FROM RIGHT IF LIST IS SORTED
#I.E. INDEX = -k.
from math import sqrt
n,k = [int(x) for x in input().split(",")]
cnt = 0
fact = []
# for i in range(1, n+1):
#     if n % i == 0:
#         fact.append(i)
# print(fact[-k])
#The above approach takes large time to complete. So using below-
for i in range(1, int(sqrt(n)+1)):
    if n%i==0:
        fact.append(i)
        fact.append(n//i)
        cnt += 2
fact.sort()
# print(fact)
if cnt > k :
    print(fact[-k])
else:
    print(1)
