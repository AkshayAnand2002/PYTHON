#Given 2 integers n1 and n2 select 2 integers a an b such as to solve the equation
#n1 * a + n2 * b = x But there is a catch , x is the smallest positive integer 
#which satisfies the equation. 
#INPUT- 1st line contains no. of test cases T. Next T lines contain 2 space
#separated integers n1 and n2.
#OUTPUT-Print the value of x.
#CONCEPT-- EUCLIDEAN ALGORITHM FOR GCD---
#x and y are results for input a and b, ax+by=gcd
#for above a = n1, x=a , b=n2 and y=b then gcd=x.
#So to get smallest x value we need to find gcd of a and b.
def gcd(a, b):
	# Everything divides 0
	if (b == 0):#base condition
		return a
	return gcd(b, a % b)#recursive call.
#Above is the function for calc gcd of 2 nos.
t = int(input())
result = []
for i in range (t):
	a,b = [int(x) for x in input().split(',')]
	result.append(gcd(a,b))
for i in result:
    print(i, end =' ')
#Input-
#1
#34818 45632
#Output-
#2
