#Program to reverse a string after removing duplicates.
#input-infosys 
#output-ysofni
#METHOD-1:
input_str=input()
output_str=""
for i in input_str:
    if i not in output_str:#FOR REMOVING DUPLICATES
        output_str+=i
print(output_str[::-1])#REVERSE
#METHOD-2:
string=input()
d=list(dict.fromkeys(string))#helps in keeping each string letter as unique.
d.reverse()
print("".join(d))
#dict.fromkeys(keys,value)#value is optional to give
#list1=[1,2,3,4]
#{
 #1:none,
 #2:none,
 #3:none,
 #4:none
#}
