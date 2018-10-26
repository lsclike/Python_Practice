def shiftMethod(arr):
    for j in range(len(arr)-1, -1, -1):
        if j > 0:
            arr[len(arr) - 1 - j], arr[len(arr) - 1] = arr[len(arr)-1], arr[len(arr) - 1 - j]

    for j in range(len(arr)):
        print(arr[j], end=' ')

if __name__=='__main__':
    shiftMethod([1,2,3,4,5])