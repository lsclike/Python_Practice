def Factorial(num):
    if (num == 0):
        return 1
    else:
        return num * Factorial(num-1)

if __name__=='__main__':
    print(Factorial(5))