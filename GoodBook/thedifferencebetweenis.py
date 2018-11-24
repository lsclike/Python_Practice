if __name__ == '__main__':
    test = [[1,2,3],2,3,4]
    result = test

    equal = test == result

    isequal = test is result
    print(equal, isequal)

    test1 = list(test)
    equal = test1 == result
    isequal = test1 is result

    print(f"== result is {equal}, is result is {isequal}")