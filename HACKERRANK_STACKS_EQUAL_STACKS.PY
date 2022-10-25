# https://www.hackerrank.com/challenges/equal-stacks/problem?isFullScreen=true
def equalStacks(s1, s2, s3):
    h1, h2, h3 = sum(s1), sum(s2), sum(s3)
    minh = min(h1, h2, h3)
    while minh > 0:
        while h1 > minh:
            h1 -= s1.pop(0)
        while h2 > minh:
            h2 -= s2.pop(0)
        while h3 > minh:
            h3 -= s3.pop(0)
        if h1 == h2 and h2 == h3:
            break
        minh = min(h1, h2, h3)
    return minh
