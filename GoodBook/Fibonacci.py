def good_fibonacci(n):

    if n <=1:
        return (n, 0)

    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, b)


if __name__ == '__main__':

    print(good_fibonacci(12))