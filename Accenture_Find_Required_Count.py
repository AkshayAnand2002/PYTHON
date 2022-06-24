#SEE QUESTION FROM C++ ---
def findCount(n, arr, num, diff):
    count=0
    for i in range(n):
        if(abs(arr[i]-num)<=diff):
            count+=1
 
    if count:
        return count
    return 0
 
n=int(input())
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(findCount(n, arr, num, diff))
