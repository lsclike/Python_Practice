import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    last = arr.pop()
    first = arr.pop(0)
    middle = 0
    for i in arr:
        middle += i

    result = [middle + first, middle + last]

    for i in result:
        print(i, end=' ')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
