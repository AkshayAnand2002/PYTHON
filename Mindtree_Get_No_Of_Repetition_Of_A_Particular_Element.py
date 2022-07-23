#You are given an integer array containing the IDs of a product. Write a program to calculate the number of repetitions of the given ID in the array and return the count.
#Input Format For Custom Testing:
#The first line contains an integer, n, denoting the number of elements in arr.
#Each line i of the n subsequent lines (where 0 < i < n) contains an integer describing the ids in the array.
#The next line or the last line contains an integer, id, denoting the id to be found.
def getCount():   
  l=[]   
  size=int(input())   
  for i in range(size):       
    c=int(input())       
    l.append(c)   
  ID=int(input())   
return l.count(ID)   
print(getCount())
