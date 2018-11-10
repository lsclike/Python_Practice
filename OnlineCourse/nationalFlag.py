def binary_search(arr, value, lo, hi):
    if lo > hi:
        return
    else:
        mid = (lo + hi) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            return binary_search(arr, value, mid + 1, hi)
        else:
            return binary_search(arr, value, lo, mid - 1)

def quick_sort(arr, lo, hi):
    if hi < lo:
        return
    a = i = lo
    b = hi
    while i <= b:
        if arr[i] < arr[lo]:
            arr[a], arr[i] = arr[i], arr[a]
            a += 1
            i += 1
        elif arr[i] > arr[lo]:
            arr[i], arr[b] = arr[b], arr[i]
            b -= 1
        else:
            i += 1

        quick_sort(arr, lo, a-1)
        quick_sort(arr, b+1, hi)

def partitionFlag(arr, value):
    arr.sort()
    the_index = binary_search(arr, value, 0, len(arr)-1)
    arr[0], arr[the_index] = arr[the_index], arr[0]
    quick_sort(arr, 0, len(arr) - 1)
    for t in arr:
        print(t, end=' ')

if __name__ == '__main__':
    partitionFlag([34,234,123,543,43, 6, 2, 1], 6)
