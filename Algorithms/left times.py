def turnleft(arr, time = None):
    length = len(arr)
    first = arr[0]
    for t in range(0, length-1):
        arr[t] = arr[t+1]
        t += 1
    arr[length - 1] = first
    return arr

def findmin(arr):
    length = len(arr)
    min = 0
    for k in range(1, length):
        if arr[k] < arr[min]:
            min = k
    return arr[min]

def insertion(arr):
    length = len(arr)
    for t in range(1, length):
        current = arr[t]
        j = t
        while j > 0 and arr[j - 1] < current:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = current
    return arr


if __name__ == '__main__':
    test = [1, 2, 3, 4]
    result = insertion(test)
    for t in result:
        print(t, end=' ')