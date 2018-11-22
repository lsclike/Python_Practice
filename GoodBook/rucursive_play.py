

def factorial(n):
    if n > 0:
        if n == 1:
            yield 1
        else:
            yield (n * factorial(n-1))
    else:
        yield 'negative'

if __name__ == '__main__':
    for t in factorial(4):
        print(t)
