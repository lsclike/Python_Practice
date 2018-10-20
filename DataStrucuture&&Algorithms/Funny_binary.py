def binary_search(data, target, low, high):

    if low > high:
        return
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid

        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)

        else:
            return binary_search(data, target, mid, high)



if __name__ == '__main__':
    result = binary_search([3,345,2342,234566,43214], 2342, 0, 4)
    print(result)