'''
You are required to implement the following function.

Int NumberOfCarries(int num1 , int num2);

The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

Assumption: num1, num2>=0

Example:

Input
Num 1: 451
Num 2: 349
Output
2
Explanation:

Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.

Sample Input

Num 1: 23

Num 2: 563

Sample Output

0
'''
def NumbersofCarries(n1,n2):
    count=0
    carry=0
    while (n1!=0) and (n2!=0):
        p=(n1%10)#(451%10=1)
        #step 2:(45%10=5)
        q=(n2%10)#(349%10=9)
        #step2:(34%10=4)
        sum=carry+p+q #10
        #step2:Present carry =1 total=(4+5+1=10)
        if sum>9:
            carry=1
            count=count+1

        else:
            carry=0
        n1=n1/10 #(451/10=45)
        n2=n2/10 #(349/10=34)
    return count


n1=int(input())
n2=int(input())
print(NumbersofCarries(n1,n2))
