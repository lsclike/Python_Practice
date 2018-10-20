import os
import sys

def timeConversion(s):

    timecross = s[-2] + s[-1]
    middle = s[0:len(s)-2]
    if timecross == 'AM':
        if int(middle[0:2]) == 12:
            if allZeo(middle):
                return '00:00:00'

def allZeo(middle):
    for i in middle[2:len(middle)]:
        if i != ':' and int(i) in range(1, 10):
            return True

    return False

def timecombine(string):




if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    last2 = s[-2] + s[-1]
    number = len(s)
    print(last2)
    # for i in s:
    #     print(i)
    #
    # result = timeConversion(s)
    #  f.write(result + '\n')

    # f.close()