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
            return binary_search(data, target, mid + 1, high)



if __name__ == '__main__':
    result = binary_search([3, 345, 2334], 2334, 0, 2)
    print(result)