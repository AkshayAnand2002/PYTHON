'''
Question – :  Some prime numbers can be expressed as a sum of other consecutive prime numbers.

For example
5 = 2 + 3,
17 = 2 + 3 + 5 + 7,
41 = 2 + 3 + 5 + 7 + 11 + 13.
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.

Input Format: First line contains a number N

Output Format: Print the total number of all such prime numbers which are less than or equal to N.

Constraints: 2<N<=12,000,000,000
'''
n = int(input())
arr = []
count = 0

primes = [i for i in range(2,n+1) if all(i%j !=0 for j in range(2,int(i**0.5) + 1))]
#above code to print all prime nos. from 2 to n with n included.

for i in range(2, len(primes)):
    sum = 0
    for j in primes:
        sum += j
        if sum == primes[i]:
            count +=1
            break
        if sum > primes[i]:
            break
print(count)
# Aanchal mam 's video explaining above code --- https://www.youtube.com/watch?v=zuvYZIcqXqg
