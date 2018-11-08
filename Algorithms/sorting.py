# 3 partition quick sort

def quick_sort_3partition(arr, left, right):
    if left >= right:
        return
    a = i = left
    b = right
    pivot = arr[left]
    while i <= b:
        if arr[i] < pivot:
            arr[i], arr[a] = arr[a], arr[i]
            i += 1
            a += 1
        elif arr[i] > pivot:
            arr[i], arr[b] = arr[b], arr[i]
            b -= 1
        else:
            i += 1

    quick_sort_3partition(arr, left, a-1)
    quick_sort_3partition(arr, b+1, right)


# merge sort
def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or ( i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1


def merge_sort(S):
    n = len(S)
    if n < 2:
        return

    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)

# selecting sort
def selectingSort(S):
    for k in range((len(S) - 1)):
        mins = k
        for t in range(k+1, len(S)):
            if S[t] < S[mins]:
                mins = t
        S[k], S[mins] = S[mins], S[k]


# Insertion test left move array
def insertionSort(S):
    for k in range(len(S) - 1, 0, -1):
        cur = S[k]
        j = k

        while j < len(S)-1 and S[j + 1] > cur:
            S[j] = S[j + 1]
            j += 1
        S[j] = cur



if __name__ == '__main__':
    test = [123,6,2,4,2]
    quick_sort_3partition(test, 0, 4)
    for t in test:
        print(t, end=' ')