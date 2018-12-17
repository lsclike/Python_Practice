def two_sum(nums, target):
    complement_dict = {}
    num_lenth = len(nums)
    for t in range(num_lenth):
        complement = target - nums[t]
        if complement in complement_dict:
            return [complement_dict[complement], t]
        else:
            if nums[t] in complement_dict:
                continue
            complement_dict[nums[t]] = t

if __name__ == '__main__':
    test = [1, 4, 3, 5, 4, 98]
    result = two_sum(test, 100)
    print(result)