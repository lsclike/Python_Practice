def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        a[min], a[i] = a[i], a[min]

    return a

if __name__=='__main__':
    test = [3,2,5,6,12,6]
    for k in selectionSort(test):
        print(k, end=' ')
