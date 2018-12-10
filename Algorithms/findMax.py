def findMax(arr):
    themax = 0
    for t in range(1, len(arr)):
        if arr[t] > arr[themax]:
            themax = t
    return arr[themax]


result = findMax([1,2,45,234,431,2])
print(result)