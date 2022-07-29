#Given two integers, the task is to find the hamming distance 
#between two integers. Hamming Distance between two integers is the
#number of bits that are different at the same position in both numbers. 
#INPUT- 3 14
#OUTPUT-3
#3 IS EQUIVALENT TO 0011 AND 14 IS FOR 1110 SO PERFORMING XOR OPERATION AND THE NO. OF 1S IN 
#THE RESULTING XOR OPERATION OUTPUT REPRESENTS NO. OF BITS THAT ARE DIFFERENT AT SAME POSITION.
#ON PERFORMING XOR WE GET 1101 NO. OF 1S IS 3 SO OUTPUT IS 3.
#1. Calculate the maximum of both the numbers.
#2.Check the set bits for both at each position.
def hammingDistance(x, y):
   ans = 0
   m = max(x, y)
   while (m):
      c1 = x & 1
      c2 = y & 1
      if (c1 != c2):
         ans += 1
      m = m >> 1
      x = x >> 1
      y = y >> 1
      print(ans)
   return ans
# driver program
n1 = 3  
n2 = 14
hdist = hammingDistance(n1, n2)
print(hdist)
#2ND METHOD
#1)Calculate the XOR of two numbers.
#2)Count the number of set bits.
# Function to calculate hamming distance
def hammingDistance(n1, n2) :
    x = n1 ^ n2 # ^ IS THE XOR OPERATOR.
    setBits = 0
    while (x > 0) :
        setBits += x & 1
        x >>= 1
        print(setBits)
    return setBits
if __name__=='__main__':
    n1 = 3
    n2 = 14
    print(hammingDistance(3, 14))
------------------------------------------------------------------------------------------------------
#Given two integers, the task is to find the hamming distance 
#between two integers. Hamming Distance between two integers is the
#number of bits that are different at the same position in both numbers. 
#1. Calculate the maximum of both the numbers.
#2.Check the set bits for both at each position.
def hammingDistance(x, y):
   ans = 0
   m = max(x, y)
   while (m):
      c1 = x & 1
      c2 = y & 1
      if (c1 != c2):
         ans += 1
      m = m >> 1
      print("m:")
      print(m)
      print("x:")
      x = x >> 1
      print(x)
      print("y:")
      y = y >> 1
      print(y)
      print("ans:")
      print(ans)
   return ans
# driver program
n1 = 3  
n2 = 14
hdist = hammingDistance(n1, n2)
print("The Hamming Distance: ")
print(hdist)
---------------------------------------------------------------------------------------------------------
def hammingDistance(n1, n2) :
    x = n1 ^ n2 # ^ IS THE XOR OPERATOR.
    setBits = 0
    while (x > 0) :
        setBits += x & 1
        x >>= 1
        print("x:")
        print(x)
        print("binary value of x:")
        print(bin(x))
        print("SETBITS:")
        print(setBits)
    return setBits
if __name__=='__main__':
    n1 = 3
    n2 = 14
    print("THE HAMMING DISTANCE IS AT THE LAST LINE: ")
    print(hammingDistance(3, 14))
