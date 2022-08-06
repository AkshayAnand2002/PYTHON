'''
Write a program to calculate and return the sum of absolute difference between 
the adjacent number in an array of positive integers from the position entered by the user.
Note : You are expected to write code in the findTotalSum function only 
which receive three positional arguments:
1st : number of elements in the array
2nd : array
3rd : position from where the sum is to be calculated
Example
Input
input 1 : 7
input 2 : 11 22 12 24 13 26 14
input 3 : 5
Output
25
Explanation
The first parameter 7 is the size of the array. Next is an array of integers 
and input 5 is the position from where you have to calculate the Total Sum. 
The output  is 25 as per calculation below. 
| 26-13 | = 13
| 14-26 | =  12
Total Sum = 13 + 12 = 25
'''
def findTotalSum(n,numbers,pos):
    total=0
    for i in range(pos-1,n-1):
        total+=abs(numbers[i]-numbers[i+1])
    return total
n=int (input())
numbers=list(map(int,input().split()))
pos=int(input())
print(findTotalSum(n,numbers,pos))
