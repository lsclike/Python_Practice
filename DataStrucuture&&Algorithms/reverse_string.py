def reverse(S, start, stop):

    if start < stop -1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)

if __name__ == '__main__':
    test = ['a','b','c','d']
    reverse(test, 0, len(test))
    print(test)