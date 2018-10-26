def reverseArray(a):
    leng = len(a)
    mid = leng // 2
    for k in range(leng-1, -1, -1):
        a[k], a[leng - 1 - k] = a[leng - 1 - k], a[k]


if __name__ == '__main__':
    test = [1,2,3,4,9,6]
    reverseArray(test)
    print(test)
