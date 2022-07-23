#Write a program to reverse the characters in the individual strings.
def reverseWord():
  List = list(input().split(" "))
  updatedList= [x[::-1] for x in List]
  return str(' '.join(updatedList))
print(reverseWord())
