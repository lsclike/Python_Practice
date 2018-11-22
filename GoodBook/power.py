def power1(x, n):

    if n == 0:
        return 1
    else:
        partial = power1(x, n //2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


if __name__ == '__main__':
    result = power1(5, 2)
    print(result)