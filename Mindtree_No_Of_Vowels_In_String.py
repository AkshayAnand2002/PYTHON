#Write a program to calculate the number of vowels present in the string
def vowels():
  count=0   
  s=input()   
  for i in s:       
    if i in 'aeiou':          
      count+=1   
  return count
print(vowels())
