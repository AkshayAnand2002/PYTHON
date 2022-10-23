#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
if 1 <= n <= 100:
    if n % 2 != 0:
        print ("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
