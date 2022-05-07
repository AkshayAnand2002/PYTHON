#Reverse words in a string .The string may contain any leading / trailing/multiple spaces
#between 2 words. But returned string should only have single space between 2 words.
## initializing the string
string = input()
## splitting the string on space
words = string.split()##this gives list of all elements separated by space.
## reversing the words using reversed() function
words = list(reversed(words))
## joining the words and printing
print(" ".join(words))
