def printWords(s):
    s = s.split(' ')##splitting words about spaces
    for word in s:
        if len(word)%2==0:
            print(word)
s = input()
printWords(s)
