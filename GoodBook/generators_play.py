def factors(n):
    k = 1

    while k * k < n:
        if n % k == 0:
            yield k
            print('reach there')
            yield n // k
        k += 1

    if k * k == n:
        yield k


if __name__=='__main__':


    for i in factors(25):
        print(i, end=' ')
