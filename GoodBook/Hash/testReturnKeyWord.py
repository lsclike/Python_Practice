def testReture(para1):
    while True:
        if para1:
            while para1 < 100:
                para1 += 1
                return False
            return True


if __name__ == '__main__':
    print(testReture(11))