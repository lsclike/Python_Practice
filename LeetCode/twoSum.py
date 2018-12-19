def two_sum(nums, target):
    complement_dict = {}
    result_array = []
    num_lenth = len(nums)
    for t in range(num_lenth):
        complement = target - nums[t]
        if complement in complement_dict:
            result_array.append([complement_dict[complement], t])
        else:
            if nums[t] in complement_dict:
                continue
            complement_dict[nums[t]] = t
    return result_array

if __name__ == '__main__':
    test = [2, 3, 3, 5, 97, 98]
    result = two_sum(test, 100)
    print(result)

