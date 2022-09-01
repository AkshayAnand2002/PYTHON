#CALCULATE NO. OF TRAILING ZEROES IN THE FACTORIAL 
#OF NO. ENTERED BY USER.
n=int(input("enter number: "))
sum=0
while (n>=5):
    n=n//5
    sum=sum+n
print(sum)
