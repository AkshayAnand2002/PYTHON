N = int(input("Enter value of N: "))
sumVal = 0
for i in range(1, N+1):
    sumVal += (i*i)
print("Sum of squares = ", sumVal)
##2nd approach
sumVal1 =  (int)( (N * (N+1) * ((2*N) + 1))/6 )
print("Sum of squares =",sumVal1)
