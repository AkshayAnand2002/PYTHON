'''
 You are required to implement the following Function 


def LargeSmallSum(arr)

The function accepts an integers arr of size ’length’ as its arguments
you are required to return the sum of second largest largest element from
the even positions and second largest from the odd position of given ‘arr’

Assumption:

    All array elements are unique
    Treat the 0th position a seven

note

    Return 0 if array is empty
    Return 0, if array length is 3 or less than 3

Example
----------------------------------------------
Please enter a number and array7
1 8 0 2 3 5 6 
[0, 1, 3, 6]
[2, 5, 8]
3
5
8
----------------------------------------------
Input

arr:3 2 1 7 5 4

Output

7

Explanation

    Second largest among even position elements(1 3 5) is 3
    Second largest among odd position element is 4
    Thus output is 3+4 = 7

'''
def LargeSmallSum(arr):
    even_arr=[]
    odd_arr=[]
    for i in range(0,len(arr)):
        if i%2==0:
            even_arr.append(arr[i])
        else:
            odd_arr.append(arr[i])
    even_arr=sorted(even_arr)
    odd_arr=sorted(odd_arr)
    print(even_arr)
    print(odd_arr)
    print(even_arr[len(even_arr)-2])
    print(odd_arr[len(odd_arr)-2])
    return (even_arr[len(even_arr)-2]+odd_arr[len(odd_arr)-2])

if __name__=='__main__':
    length=int(input("Please enter a number and array"))
    arr=list(map(int,input().split()))
    b=LargeSmallSum(arr)
    print(b)
#if __name__ == “main”: is used to execute some code only if the
#file was run directly, and not imported.
