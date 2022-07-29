#GIVEN THE NUMBER N . FIND THE NUMBER OF PRIMES WHICH ARE LESS THAN N AND DON'T 
#HAVE A DIGIT 0 IN THEM.
#INPUT-4
#OUTPUT-2 (AS 2 AND 3 < 4 AND ARE PRIME)
#INPUT-2
#OUTPUT-1 (AS 2 IS THE PRIME NO.)
#----ABOVE TESTCASE IS IMPORTANT.
def isPrime(x):
    for i in range(2,x//2+1):
        if(x%i==0):
            return False
    return True
n = int(input("Enter the number : "))
lst = []
for i in range(2,n+1):
    if(isPrime(i)==True):
        x=str(i)
        if('0' not in x ):
            lst.append(i)
print(len(lst))
#print(lst)
