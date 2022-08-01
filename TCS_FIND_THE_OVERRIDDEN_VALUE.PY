#GIVEN AN ARRAY OF SIZE N. IDEALLY IT SHOULD CONTAIN 1 TO N NOS.(IN PARTICULAR ORDER)
#BUT 1 NUMBER IS OVERRIDDEN BY ANY OTHER VALUE. RETURN THE NO. WHICH IS OVERRIDDEN.
#INPUT- 1ST LINE HAS VALUE OF N. THEN N NEXT LINES WHERE EACH LINE WILL HAVE +VE INTEGER.
#OUTPUT-PRINT THE NO. WHICH IS OVERRIDDEN.
#EXAMPLE-- INPUT-
#5
#2 1 100 5 3
#OUTPUT-4
#SINCE N=5 NOS. IN ARRAY MUST BE 1,2,3,4,5 BUT 4 IS OVERRIDDEN BY 100.
N=int(input("Enter the size of array: "))
arr=[]
for i in range(1,N+1):
    ele=int(input())
    arr.append(ele)
print("INPUT ARRAY: ")
print(arr)
a=sorted(arr)
print("SORTED INPUT ARRAY:")
print(a)
for i in a:
    if(a[i]==i+1):#if at 0th index 1 is present , 1st index- 2 , ...
    #then continue as we need to find the overridden value.
        continue
    else:
        print("Missing Or Overridden number is: ",i+1)
        #this value at ith index is not = arr[i] so the value i+1 is 
        #overridden as we already sorted the array.
        break
    #as ATQ, only one overridden value is possible, if we found one
    #then we can break out of the loop.
