'''
TAKE INPUT FROM USER IF IT IS ODD SUBTRACT 1 FROM IT.
ELSE IF EVEN DIVIDE IT BY 2.
CONTINUE TILL THE INPUT NO. REDUCES TO 0.
PRINT THE STEPS IN DOING THE ABOVE PROCESS.
'''
n=int(input("enter number: "))
steps=0
while n!=0:
    if(n%2)==0:
        n=n//2
        steps+=1
    else:
        n=n-1
        steps+=1
print(steps)
