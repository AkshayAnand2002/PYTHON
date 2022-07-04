'''
You are given a function,

Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

Assumption: String Contains only lower-case alphabetical letters.

Note:

    Return null if string is null.
    If both characters are not present in string or both of them are same , then return the string unchanged.

Example:

    Input:
        Str: apples
        ch1:a
        ch2:p
    Output:
        Paales

Explanation:

‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales.
'''
def swap (user_input, str1, str2):

    result = ''

    if user_input != None:

        result = user_input.replace(str1, '*').replace(str2, str1).replace('*', str2)

        return result

    return 'Null'

user_input = input()

str1=input()
str2=input()

print(swap(user_input, str1, str2))
