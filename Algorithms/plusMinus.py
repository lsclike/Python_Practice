def plusMinus(arr):
    positive = 0
    negative = 0
    zeo = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zeo +=1

    positiveRatio = format(positive/len(arr), '.6f')
    negativeRatio = format(negative/len(arr), '.6f')
    zeoRatio = format(zeo/len(arr), '.6f')

    result = [positiveRatio, negativeRatio, zeoRatio]
    return result

if __name__ == '__main__':
    test = plusMinus([1, 2 , 3, -2, 3, -4])
    for i in range(len(test)):
        print(test[i])