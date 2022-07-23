#You are given a function that takes an integer N. Write a program that returns the sum of all the even numbers which are less than or equal to N.
#INPUT-5 OUTPUT-6 
#INPUT-6 OUTPUT-12
def sumEven():   
  num=int(input())   
  sum=0   
  for i in range(0,num+1,2):       
    sum+=i   
  return sum   
print(sumEven())
