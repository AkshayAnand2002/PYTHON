#Problem
#You are given two arrays each of size ,  and  consisting of the first  positive integers each exactly once, that is, they are permutations. 
#Your task is to find the minimum time required to make both the arrays empty. The following two types of operations can be performed any number of times each taking 1 second:
#In the first operation, you are allowed to rotate the first array clockwise.
#In the second operation, when the first element of both the arrays is the same, they are removed from both the arrays and the process continues.
#Input format
#The first line contains an integer , denoting the size of the array.
#The second line contains the elements of array .
#The third line contains the elements of array .
#Output format
#Print the total time taken required to empty both the array.
#Constraints
#Sample Input
#3
#1 3 2
#2 3 1
#Sample Output
#6
#Time Limit: 1
#Memory Limit: 256
#Source Limit:
#Explanation
#Perform operation 1 to make a = 3, 2, 1
#Perform operation 1 to make a = 2, 1, 3
#Now perform operation 2 to make a = 1, 3 and b = 3, 1
#Perform operation 1 to make a = 3, 1
#Now perform operation 2 to make a = 1 and b =  1
#Now perform operation 2 to make a = {} and b =  {}
n = int(input("Enter the no. of elements in array: "))
a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
count = 0
while a:
    if a[0]==b[0]:
        del a[0],b[0]
        count+=1
    else:
        a=a[1:]+a[:1]##used for cyclic rotation where first element moves to last.
        ##other elements move to front. eg- ban changes to anb for 1st iteration.
        count+=1
print(count)
