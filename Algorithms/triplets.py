def compareTriplets(a, b):
    n = len(a)
    result = [0, 0]
    for i in range(n):
        if a[i] < b[i]:
            result[1] += 1
        elif a[i] > b[i]:
            result[0] += 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
