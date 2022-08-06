'''
Write a program to find the difference between the elements at odd index and even index.
Note : You are expected to write code in the findDifference function only which receive 
the first parameter as the numbers of items in the array and second parameter as the array itself. 
You are not required to take the input from the console.
Example
Input
input 1 : 7
input 2 : 10 20 30 40 50 60 70
Output
40

Explanation
The first parameter 7 is the size of the array. 
Sum of element at even index of array is 10 + 30 + 50 + 70 = 160 
and sum of elements at odd index of array is 20 + 40 + 60 = 120. 
The difference between both is 40.
'''
def findDifference(n,values):
    total=0
    for i in range(n):
        if i%2 == 0:
            total+=values[i]
        else:
            total-=values[i]
    return total
n=int(input())
values=list(map(int,input().split()))
print(findDifference(n,values))
