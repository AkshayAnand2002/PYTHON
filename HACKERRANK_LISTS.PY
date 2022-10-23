# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    N = int(input())
    v= []
    for i in range (N):
        com = input().split()
        if com[0]=='insert':
            v.insert(int(com[1]),int(com[2])) # 1ST IS INDEX, 2ND IS NO TO BE INSERTED. 
        if com[0]=='print':
            print(v)
        if com[0]=='remove':
            v.remove(int(com[1]))
        if com[0]=='append':
            v.append(int(com[1]))
        if com[0]=='sort':
            v.sort()
        if com[0]=='pop':
            v.pop()
        if com[0]=='reverse':
            v.reverse()
