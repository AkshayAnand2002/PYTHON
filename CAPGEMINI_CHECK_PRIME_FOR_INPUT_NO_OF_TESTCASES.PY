'''
GIVEN AN INTEGER N, CHECK PRIME OR NOT.
INPUT->
1ST LINE HAS INTEGER T DENOTING NO. OF TEST CASES
EACH TESTCASE IS IN A NEW LINE WITH SINGLE INTEGER N.
FOR ANY INVALID INPUT PRINT INVALID.
OUTPUT->
PRINT IF N IS PRIME OR COMPOSITE.
SAMPLE INPUT->
5
SAMPLE OUTPUT-> PRIME
'''
ntestcases=int(input())
for i in range(ntestcases):
    flag=False
    num=int(input())
    if num>1:
        for j in range(2,num):
            if((num%j)==0):
                flag = True
                break
        
    if flag==True:
        print(num,"is composite.")
    else:
        print(num,"is prime.")
