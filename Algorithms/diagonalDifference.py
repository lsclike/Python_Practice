import math
import os
import random
import re
import sys

def diagonalDifference(arr):
        n = len(arr)
        leftsum = 0
        rightsum = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    leftsum += arr[i][j]
                elif i + j == n-1:
                    rightsum += arr[i][j]
        if not(n%2==0):
            rightsum += arr[n // 2][n // 2]
        print(leftsum)
        print(rightsum)

        return abs(leftsum - rightsum)

if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)