def insertionSort(a):

    for k in range(1, len(a)):
        cur = a[k]
        j = k
        while j > 0 and a[j-1] > cur:
            a[j] = a[j-1]
            j -= 1
        a[j] = cur

    return a

if __name__=='__main__':
    test = [3,2,1,5,6,4]
    for k in insertionSort(test):
        print(k, end=' ')