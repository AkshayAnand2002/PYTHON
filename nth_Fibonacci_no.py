def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(9))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(4))
print(Fibonacci(-1))
print(Fibonacci(5))
