# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #result = [[i, j, k] for i in range(1+x) for j in range(1+y) for k in range(z+1) if sum([i, j, k]) != n]
    res=[[i,j,k] for i in range(x+1)for j in range(y+1)for k in range(z+1) if i+j+k!=n]
    print(res)  
    #print(result)

'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    res=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k !=n:
                    res.append([i,j,k])
    print(res)
'''
