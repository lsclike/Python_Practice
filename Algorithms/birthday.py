def birthdayCakeCandles(ar):
    theNumber = len(ar) - 1
    times = 0
    for i in ar:
        if i == theNumber:
            times += 1

    print(times)


if __name__ == '__main__':
    birthdayCakeCandles([3,3,2,1])