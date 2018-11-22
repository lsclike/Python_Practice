def revursiveSum(list1, low, high):
    if high - low < 2:
        return list1[low] + list1[high]
    else:
        mid = (low + high) // 2
        return revursiveSum(list1, low, mid-1) + revursiveSum(list1, mid+1, high) + list1[mid]


if __name__ == '__main__':
    print(revursiveSum([1,2,3,4], 0, 3)),