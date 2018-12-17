def longest_substring_without_repeating(string):
    max_length = 0
    for i in range(len(string)):
        max_length = max(max_length, helper(string, i))

    return max_length


def helper(string, start):
    seen = set()
    for i in range(start, len(string)):
        if string[i] not in seen:
            seen.add(string[i])
        else:
            return i - start
    return len(string) - start

if __name__ == '__main__':
    result_length = longest_substring_without_repeating('abcdee')
    print(result_length)