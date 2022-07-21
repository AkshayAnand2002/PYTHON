#Write a program to find the average of the first P multiples of an integer N.
#Input Format For Custom Testing
#The first line contains an integer, N, denoting the integer.
#The next line contains an integer, P, denoting the number of multiples to consider.
#INPUT -
#6
#5 
#OUTPUT- 18
#AVERAGE OF 1ST 5 MULTIPLES OF 6 I.E. (6+12+18+24+30)/5 = 18.
def average():
  sum=0
  n=int(input())
  p=int(input())
  for i in range(n,(n*p+1),n):
    sum=sum+i
  return int(sum/p)
print(average())
 # for i in range(n,(n*p+1),n): #USED TO FIND FIRST p MULTIPLES OF n
  #    print(i)
   #   print()
