#GIVEN AN ARRAY OF T LENGTH. EACH INDEX CONTAINS ARRAY OF 2 BINARY STRINGS
#YOUR TASK IS TO RETURN THEIR MAXIMUM SUM(WHICH IS ALSO A BINARY STRING.)
#1ST LINE CONTAINS T ARRAY LENGTH, NEXT N LINES CONTAIN 2 STRINGS WHICH 
#SHOWS BINARY SPACE SEPARATED m,n
#FIND THE SUM OF m,n IN BINARY AND PRINT THE MAXIMUM BINARY SUM FROM THE 
#ARRAY ELEMENTS.
#INPUT
#3
#101 100
#110 10
#1000 11
#OUTPUT
#1011
#STEPS-CONVERT INTO INTEGER , ADD THEM AND FIND THE MAXIMUM.
#AGAIN CONVERT THE MAXIMUM VALUE INTO BINARY.
t=int(input())
ans=[]
for i in range(t):
    A,B=input().split()
    a=int(A,2)#converting binary to integer by int(A,2)
    b=int(B,2)
    temp=a+b
    ans.append(temp)
print(ans)#to print whole list.
print(max(ans))#print maximum element of answer list.
print(bin(max(ans)))
final=bin(max(ans))
print(final[2:])
