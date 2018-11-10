def findNumbers(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr2[j] > arr1[i]:
            i += 1

        else:
            if arr2[j] < arr1[i]:
                print(arr2[j], end=' ')
            j += 1

if __name__ == '__main__':
    test = [1, 2, 4, 7]
    test1 = [6, 3, 2, 1]
    findNumbers(test, test1)

