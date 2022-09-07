'''
ACCENTURE->
INPUT: 8 4 5 3 2 6 9 1
OUTPUT- 189 120 90 45 15 9 0 0
EXPLAINED- FOR 8 TAKING SUM OF ALL ELEMENTS < 8 WE GET
4+5+3+2+6+1=21 AND NOW THE SUM OF ELEMENTS > 8 I.E. 9.
PRODUCT OF THE 2 SUMS = 21*9=189.
FOR 4 SUM OF ALL ELEMENTS < 4 WE GET 3+2+1=6 AND 
SUM OF ELEMENTS> 4 5+6+9=20 PRODUCT NOW IS 6*20=120
WE SEE THAT FOR 4 WE DID NOT TAKE 8 .
SIMILARLY FOR 6 SUM OF ELEMS. < 6 IS 1 AND THAT > 6 IS 9.
PRODUCT =9*1=9.
FOR 9 AND 1 IT WILL BE 0. 
SO AS WE MOVE TO THE RIGHT WE CHECK AMONG THE RIGHT ELEMENTS
ONLY. HENCE i in range len(array) and j in range(i+1,len(array)
'''
a=[8,4,5,3,2,6,9,1]
result=[]
for i in range(len(a)):
    sum=max=0
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            sum+=a[j]
        elif(a[i]<a[j]):
            max+=a[j]
    result.append(max*sum)
print(result)
