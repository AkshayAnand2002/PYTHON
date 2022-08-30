'''
PROGRAM TO SORT CHARACTERS AND NOS. SO THAT FIRST ALPHABETS 
AND THEN NOS. ARE PRINTED.
'''
str1=input("ENTER A STRING IN THE FORMAT[A2B5V7]: ")
alphabets=[]
numbers=[]
for ch in str1:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numbers.append(ch)
final_list=sorted(alphabets)+sorted(numbers)
output=''.join(final_list)
print(output)
