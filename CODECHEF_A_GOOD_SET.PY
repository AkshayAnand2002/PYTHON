'''
A set of integers is called good if there does not exist three distinct elements a, b, c in it such that a + b = c.

Your task is simple. Just output any good set of n integers. All the elements in this set should be distinct and should lie between 1 and 500, both inclusive.

Input
The first line of the input contains an integer T denoting number of test cases. The descriptions of T test cases follow.
The only line of each test case contains an integer n, denoting the size of the needed good set.
Output
For each test case, output a single line containing n integers denoting the elements of the good set, in any order. There can be more than one possible good set, and you can output any one of them.

Sample 1:
Input
Output
5
1
2
3
4
5
7
1 2
1 2 4
1 2 4 16
3 2 15 6 10
Explanation:
Example 1 and 2. Any set of size less than or equal to 2 is good by definition.

Example 3 onwards. For each pair of elements in the set, you can see that their sum doesn't exist in the set.

EXPLANATION:
Since n is up to 100, one can just output integers from 500-n to 499. Sum of any two such integers is greater than 500 so requirements will be satisfied.
'''
for J in range(int(input())):
    n=int(input())
    for i in range(n):
        print(500-i,end=" ")
    print()
'''
Input
5
1
2
3
4
5
Output
500 
500 499 
500 499 498 
500 499 498 497 
500 499 498 497 496 
'''
