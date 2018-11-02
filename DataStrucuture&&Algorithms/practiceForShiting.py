def shiftMethod(arr, times):
    realtime = times%len(arr)


    while realtime > 0:
        for j in range(len(arr)-1, -1, -1):
            arr[j], arr[-1] = arr[-1], arr[j]

        realtime -= 1
    return arr


if __name__=='__main__':
    result = shiftMethod([1,2,3,4,5,6], 6)
    for t in result:
        print(t, end=' ')