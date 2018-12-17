def longest_substring_without_repeating(string):
    result_diction = {}
    result = []
    for i in range(len(string)):
        helper(string, i, result_diction)
    length = max(result_diction.keys())
    for i in range(result_diction[length], result_diction[length] + length):
        result.append(string[i])

    return ''.join(result)


def helper(string, start, diction):
    seen = set()
    for i in range(start, len(string)):
        if string[i] not in seen:
            seen.add(string[i])
        else:
            diction[i - start] = start
            return None
    diction[len(string) - start] = start
    return None

if __name__ == '__main__':
    result_length = longest_substring_without_repeating('abcdee')
    print(result_length);