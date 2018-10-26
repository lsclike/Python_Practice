def listFactor(number):
    test = [k for k in range(1, number+1) if number % k == 0]
    return test

if __name__ == '__main__':
    result = listFactor(123)
    for k in result:
        print(k, end=' ')