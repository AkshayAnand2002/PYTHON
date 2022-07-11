#Consider a non-zero positive decimal no. innum,an integer inbase > 1 and 
#print outnum , the max. no. of consecutive set of zeroes after converting innum to
#its inbase notation.print -1 if there exists no zero after converion of innum.
#INPUT-1st line contains innum. 2nd line contains inbase read the input from 
#standard input stream.
def dec_to_base(num,base):
    base_num=""
    while num>0:
        dig=int(num%base)
        if(dig<10):
            base_num+=str(dig)#if remainder is <10 
            #simply add it to output.
        else:
            base_num+=chr(ord('A')+dig-10)
#if we get remainer i.e. dig > 10 eg. 12 we need to convert it 
#into hexadecimal value C we use ord which gives ASCII value
#ord('A')=65 + dig - 10 will give the ASCII value of the 
#character then chr is used to convert ascii value to 
#corresponding character so we finally get 'C'.
        num//=base#for dividing digits continuously by base.
    base_num=base_num[::-1]
#when we get remainders at different steps at last we reverse 
#them to get the answer. eg: in binary when we get the 
#remainders at different steps at last we reverse the string to
#get the final answer.
    return base_num
def array(num,base):
    count=0
    output=dec_to_base(num,base)
    ans=0
    for i in range(len(output)):
        if(output[i] != "0"):
            count=0
        else:
            count+=1
            ans=max(count,ans)
    return ans
num=68
base=2
print(array(num,base))
