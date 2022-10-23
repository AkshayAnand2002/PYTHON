#https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true
def reverseArray(a):
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
    return a
  #a[n-i-1] -> for i=0 is the last element of the array.
