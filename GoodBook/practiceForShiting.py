

def shiftMethod(a, length, times):
    realtime = times%length

    if realtime <= length // 2:
        for k in range(length):
            if length - k > realtime:
                if k - realtime < 0:
                    a[k], a[length + (k - realtime)] = a[length +(k - realtime)], a[k]
                elif k - realtime >= 0:
                    a[k], a[k - realtime] = a[k - realtime], a[k]

    else:
        righttimes = length - realtime
        for k in range(length):
            if length - k > righttimes:
                if k - righttimes < 0:
                    a[k], a[righttimes] = a[righttimes], a[k]
                else:
                    a[k], a[k-righttimes] = a[k - righttimes], a[k]



    return a

if __name__=='__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = shiftMethod(a, n, d)
    for t in result:
        print(t, end=' ')