#FIBONACCI SERIES PRINT NTH FIBONACCI NO. WITH EG. INPUTS
#INPUT-2 OUTPUT-1
#INPUT-9 OUTPUT-34
def Fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    a=[0]*(n+1)
    a[0]=0
    a[1]=1
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a,a[n]
print(Fib(9))
