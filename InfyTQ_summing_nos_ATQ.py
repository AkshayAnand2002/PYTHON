#A strong of comma separated values given such that the numbers 4 and 7 are already present 
#in the list . Assume 7 always come after 4 in the given string.
#case1-num1 = add all nos which don't lie between 4 and 7 excluding 4 and 7. 
#case2-num2 = nos. formed by concatenating all nos between 4 and 7 including 4 and 7.
#output-sum of num1 and num2.
#eg-3,1,6,4,2,3,7,2
#num1=3+1+6+2=12
#num2='4'+'2'+'3'+'7'='4237'
#output=4237+12=4249
#Method-1:
num_list=input().split(",")
length=len(num_list)
index_4=num_list.index('4')
index_7=num_list.index('7')
num1=0
num2=""
for i in range(0,length):
    if(i<index_4 or i>index_7):
        num1+=int(num_list[i])
for i in range(index_4,index_7+1):
    num2+=num_list[i]
print(num1+int(num2))
#Method-2:
L1=list(map(int,input().split(",")))
num1=sum(L1[:L1.index(4)])+sum(L1[L1.index(7)+1:])
LST=L1[L1.index(4):L1.index(7)+1]
num2=""
for i in LST:
    num2+=str(i)
print(int(num2)+num1)
