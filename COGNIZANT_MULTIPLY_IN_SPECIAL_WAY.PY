#GIVEN AN INTEGER ARRAY NUMS PRINT AN ARRAY
#SUCH THAT ANSWER[i] = PRODUCT OF ALL ELEMENT OF NUMS EXCEPT NUMS[i].
#YOU MUST WRITE AN ALGO WITHOUT USING DIVISION OPERATION.
#INPUT-
#4
#1 2 3 4
#OUTPUT-
#24 12 8 6
def multiply(l):
    result=1
    for i in l:
        result=result*i
    return result
n=int(input())
l=list(map(int,input().split()))
answer=[]
for i in range(n):
    l1=l[:]
    l1.pop(i)#IT REMOVES 0TH INDEX,1ST INDEX ,... ELEMENTS IN EACH ITERATION.
    #print(l1)
    answer.append(multiply(l1))
print(answer)
