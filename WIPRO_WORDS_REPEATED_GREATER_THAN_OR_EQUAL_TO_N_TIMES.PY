'''
PROGRAM TO DISPLAY WORDS THAT ARE REPEATED >= N TIMES IN 
TEXT.
'''
str=input("ENTER A STRING: ")
n=int(input("ENTER A COUNT: "))
str1=str.split(" ")
counts=dict()
for word in str1:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
word_list=[]
for key in counts:
    if counts[key]>=n:
        word_list.append(key)
if len(word_list)>0:
    print(word_list)
else:
    print("NOT AVAILABLE.")
