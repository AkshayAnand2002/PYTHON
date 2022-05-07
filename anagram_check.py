#An anagram is a word or phrase formed by rearranging the letters of a
#different word or phrase,typically using all the original letters exactly once.
string1=input("Enter first string:")
string2=input("Enter second string:")
if len(string1) != len(string2):
    print("Strings are not anangrams.")
else:
    string1=sorted(string1)
    string2=sorted(string2)
    if string1 == string2:
        print("Strings are anagrams.")
    else:
        print("Strings are not anagrams.")
        
