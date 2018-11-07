def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
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

class findPattern:
    def __init__(self, pattern):
        self._pattern = pattern
        self._time = 0


    def showPattern(self):
        return self._pattern

    def add_time(self):
        self._time += 1

    def show_time(self):
        return self._time


def try_binary(data, target,low, high):
    if low > high:
        return
    else:
        mid = (low + high) // 2
        if target.showPattern() == data[mid]:
            target.add_time()
            return target
        elif target.showPattern() < data[mid]:
            return try_binary(data, target,low, mid - 1)
        else:
            return try_binary(data, target,mid + 1, high)

if __name__ == '__main__':
    test = ['bac', 'abc', 'abc']
    merge_sort(test)
    query = ['abc', 'bac']
    finalQuery = []
    times = []
    for k in query:
        thequery = findPattern(k)
        finalQuery.append(thequery)


    result = try_binary(test, finalQuery[0], 0, 2)
    print(result.show_time())



