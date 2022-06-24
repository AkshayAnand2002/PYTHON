#SEE QUESTION FROM C--
s = input("Enter any string to remove all vowels from it: ")
vowels = ('aeiou')  
s = s.lower()
for x in s:
   if x in vowels:
       s = s.replace(x, "")   # Replacing the vowels with ‘’
print(s)
