Problem Description
There is a mess in the parcel section of the Head Office. The parcels that have to be loaded in the vans are lined up in a row randomly. The Head Post Master wants them to order them in the increasing order of their weights, but he wants to keep the heaviest (and presumably the most valuable) parcel nearest to his office.

You and your friend try to arrange these boxes, and you decide to arrange them by interchanging two boxes at a time. Such replacement needs effort equal to the product of the weights of the two boxes which are exchanged. 

The goal is to reposition the boxes as required with minimum effort.

Input
The first line consists of two space-separated positive integers number of boxes (N) and the position of the Head Post Master's office (k), respectively. The value of k represents where the heaviest box should be placed.

The second line contains N space-separated positive integers, i.e., the weights of the boxes. Assume that no two weights are equal.

Output
The output is the minimum total effort taken to get the boxes in sorted order and the heaviest in position k.

Constraints

N<=50

Weights <= 1000

Time Limit (secs)

1

Example 

Input

5 2

20 50 30 80 70

Output

3600
Explanation

There are five boxes (N=5), and the heaviest box should be kept at position 2 (k=2). Now, the final order (sorted, with the heaviest at position 2) will be 20 80 30 50 70. If we look at this order, we notice that only the 50 and the 80 parcels need to be exchanged. As this takes the effort of the product of the weights, the effort is 4000.   

We can further reduce if we use the smallest package (20) as an intermediary package. If we exchange 20 with 50, then with 80, and back with 50 again, the efforts will be 1000,1600, 1000 respectively. The effect will be the same, with a total effort of 3600 (less than the effort obtained by the direct move).

The optimal sequence of exchanges for minimum effort is

50 20 30 80 70

50 80 30 20 70

20 80 30 50 70

As these exchange orders take the minimum effort of 3600, the output is 3600.

Solution
At first, we will take a temp array to store the weight of boxes and arrange the boxes in expected order by sorting them and putting the heaviest block at the kth position.
for each box in the temp array, we will find out where it was initially and then calculate the value of effort to put it at the expected position.
If the actual position is the same as the expected position then there will be no effort.
Otherwise, we will take the minimum weight box as an intermediate for swapping.
After calculation of effort for each swap, we will swap those boxes in the original array.

------------------------------------------------------------------------------
n,k = map(int,input().split())
vec = list(map(int,input().split()))
temp = sorted(vec)
temp[n-1],temp[k-1] = temp[k-1],temp[n-1]
if k < n:
    temp[k:] = sorted(temp[k:])
ans = 0
for i in range(n):
    j = 0
    for j in range(i,n):
        if(temp[i] == vec[j]):
            break
    if(i == j):
        continue
    if(i == 0):
        ans += vec[i]*vec[j]
        vec[i],vec[j] = vec[j],vec[i]
        continue
    ans += 2*min(vec[i],vec[j])*temp[0]+max(vec[i],vec[j])*temp[0]
    vec[i],vec[j] = vec[j],vec[i]
print(ans)
-------------------------------------------------------------------------------------
