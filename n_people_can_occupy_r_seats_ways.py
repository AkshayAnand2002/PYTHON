#n people can occupy r seats in how many ways. 
def fact(x):
    if(x==0 or x==1):
        return 1
    else:
        return (x*fact(x-1))
n=int(input("ENTER NO. OF PEOPLE: "))
r=int(input("ENTER NO. OF SEATS: "))
p=fact(n)/fact(n-r)
print("REQ. NO. OF WAYS: ",p)
