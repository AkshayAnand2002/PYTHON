#Liitle Jill jumbled up the order of letters in our dictionary. Now Jack uses this 
#list to find smallest lexicogrtaphical string that can be made out of this 
#new order. You are given a string P that denotes the new order of letters
#in English dictionary which was changed or jumbled by Jill.
#You need to print the smallest lexicographic string made from the given
#string s.
#input format- 1st line contains no. of test cases.
#second line has string P.
#third line has string s.
#input provided as---
#1
#polikujmnhytgbvfredcxswqaz
#abcd
#output expected--
#bdca
#Method-1:
test = int(input())
while (test > 0):
    P = input()
    S = input()
    list1 = []
    for i in S:
        list1.append(P.find(i))#find-used to find index of letters of string S in string P.
    list1.sort()
    for i in list1:
        print(P[i], end='')#used to print the letters at the index i that is same as that i which stores index of letters of string S in string P.
    if test > 1:
        print()#acts as newline character of c language ,moves to next line.
    test -= 1
#Method-2:
t=int(input())
while t>0:
    P=input()
    S=input()
    for i in P:
        if i in S:
            print(i, end='')
    print()
    t-=1
