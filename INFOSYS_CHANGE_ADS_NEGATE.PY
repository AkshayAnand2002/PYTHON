'''
AN E-COMMERCE WEBSITE HAS A SERIES OF ADS TO DISPLAY.
ADS ARE DISPLAYED OR NOT IS BASED ON BIT POSITION IN A NO.
THE SEQUENCE OF ADS CAN BE DISPLAYED AS BINARY VALUE.
WHERE 1 MEANS AD IS DISPLAYED AND 0 MEANS AD NOT DISPLAYED.
THE AD SHOULD ROTATE.
INPUT-50
OUTPUT-13
EXPLAINED- 50 IS 110010 NEGATE EACH BIT TO GET 001101=13.
1ST,2ND AND 2ND LAST DISPLAYED ON 1ST PAGE.
ATQ, SAME AD SHOULD NOT BE DISPLAYED ON 2ND PAGE.
SO NEGATE TO GET 13 AS OUTPUT.
'''
def changeads(num):
    b=bin(num)#b is a string. OUTPUT-0b10..something
    b=b[2:len(b)]#to remove 0b we apply indexing.
    b1=""
    for bit in b:
        if bit =='1':
            b1=b1+'0'
        else:
            b1=b1+'1'
    sum1=0
    for i in range(len(b1)):
        sum1=sum1+(int(b1[i])*(2**(len(b1)-(i+1))))
    return sum1
print(changeads(50)) 
