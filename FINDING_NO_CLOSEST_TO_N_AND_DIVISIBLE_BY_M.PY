# Python 3 implementation to find
# the number closest to n
# Function to find the number closest
# to n and divisible by m
def closestNumber(n, m) :
	# Find the quotient
	q = int(n / m)
	# 1st possible closest number
	n1 = m * q
	# 2nd possible closest number
	if((n * m) > 0) :
		n2 = (m * (q + 1))
	else :
		n2 = (m * (q - 1))
	# if true, then n1 is the required closest number
	if (abs(n - n1) < abs(n - n2)) :
		return n1
	# else n2 is the required closest number
	return n2
# Driver program to test above
n = 10; m = 4
print(closestNumber(n, m))
n = -15; m = 6
print(closestNumber(n, m))
n = 0; m = 8
print(closestNumber(n, m))
n = 18; m = -7
print(closestNumber(n, m))
