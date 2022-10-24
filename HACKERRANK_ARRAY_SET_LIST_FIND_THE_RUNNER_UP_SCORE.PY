# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(sorted(set(sorted(arr))))
    print(arr[-2])
'''
Converting an array to a set changes the order type, so you need to apply sorted function again.
'''
