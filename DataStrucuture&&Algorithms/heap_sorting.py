def sort(unordered):
    leng = len(unordered)
    k = leng // 2
    while k >= 1:
        sink(unordered, k, leng)
        k -= 1
    while leng > 1:
        exch(unordered, 1, leng)
        leng -= 1
        sink(unordered, 1, leng)


def sink(arr, s, e):
    while 2 * s <= e:
        j = 2 * s
        if ( j < e ) and less(arr, j, j + 1):
            j += 1
        if not less(arr, s, e):
            break
        exch(arr, s, j)
        s = j


def exch(arr, s, e):
    arr[s-1], arr[e-1] = arr[e-1], arr[s-1]


def less(arr, s, e):
    return arr[s-1] < arr[e - 1]

if __name__ == '__main__':
    test = [23434, 23, 44]
    sort(test)
    for t in test:
        print(t, end=' ')

