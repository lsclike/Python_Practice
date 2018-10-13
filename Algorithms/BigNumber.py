import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    print(len(ar))
    for i in range(len(ar)):
        if  i < len(ar)-1:
            ar[0] += ar[i+1]

    return ar[0]

if __name__ == '__main__':
    print(aVeryBigSum([1,2,3,4,5]))