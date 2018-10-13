import math
import os
import random
import re
import sys

def staircase(n):
    result=[]
    leng = n-1
    for i in range(n):
        result.append([])


    for i in range(n):
        for j in range(n):
            if i + j >= leng:
                result[i].append('#')
            else:
                result[i].append(' ')


    return result


if __name__ == '__main__':
    n = int(input())
    # build_matrix(3)
    result = staircase(n)
    for i in result:
        for j in range(n):
            print(i[j], end='')
            if j == n-1 :
                print("\n", end='')

