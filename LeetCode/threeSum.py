def two_sum(arr, target, start):
    complement_dict = {}
    length = len(arr)
    for t in range(length):
        complement = target - arr[t]
        if complement in complement_dict:
            return [complement_dict[complement], t + start]
        else:
            if arr[t] in complement_dict:
                continue
            complement_dict[arr[t]] = t + start

def three_sum(arr, target):
    length = len(arr)
    result_list = []
    for t in range(length-1):
        remain = target - arr[t]
        remainSum = two_sum(arr[t+1:], remain, t+1)
        if remainSum:
            remainSum.append(t)
            result_list.append(remainSum)
        else:
            continue
        return result_list

if __name__ == '__main__':
    test = [1,2,3,4,5,100]
    # two_sum_result = two_sum(test, 5)
    result = three_sum(test, 10)
    # print(two_sum_result)
    print(result)