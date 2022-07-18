#TO INCREASE READING HABIT CLASS TEACHER DECIDED TO EXCHANGE THE BOOKS EVERY WEEK
#SO THAT EVERYONE WILL HAVE DIFFERENT BOOK TO READ.
#IF Bi IS THE BOOK OF ith STUDENT AND AFTER EXCHANGE HE SHOULD GET A DIFFERENT BOOK.
#I.E. AFTER EVERY EXCHANGE FOR EVERY STUDENT BOOK SHOULD NOT BE REPEATED.
#INPUT-ONE LINE WITH N INDICATING NO. OF BOOKS AND NO. OF STUDENTS.
#OUTPUT-ANSWER modulo 1000000007
#HERE WE CAN USE DERANGEMENT THEORY SUCH THAT NO BOOK RETURNED TO THE STUDENT WHO
#ALREADY READ IT.
#D(n)=(n-1)(D(n-1)+D(n-2))
#0 BOOK-1 ARRANGEMENT ; 1 BOOK- 0 ARRANGEMENT ; 2 BOOKS-1 ARRANGEMENT
 #RECURSIVE 
def D(n):
    #BASE CONDITIONS
    if(n==1):
         return 0
    if(n==0):
         return 1
    if(n==2):
         return 1
    # D(n)=(n-1)(D(n-1)+D(n-2))
    return (n-1)*(D(n-1)+D(n-2))
n=int(input())
print(D(n)%1000000007)
#DYNAMIC PROGRAMMING
def countDer(n):
    D=[0 for i in range(n+1)]
    #BASE CONDITIONS
    D[0]=1
    D[1]=0
    D[2]=1
    for i in range(3,n+1):
        D[i]=(i-1)*(D[i-1]+D[i-2])
    return D[n]
n=int(input())
print(countDer(n)%1000000007)
#Dynamic programming approach is similar to divide and conquer in breaking down 
#the problem into smaller and yet smaller possible sub-problems. But unlike, 
#divide and conquer, these sub-problems are not solved independently.
#There are three steps in finding a dynamic programming solution to a problem: 
#(i) Define a class of subproblems, (ii) give a recurrence based on solving each 
#subproblem in terms of simpler subproblems, and (iii) give an algorithm for 
#computing the recurrence.
