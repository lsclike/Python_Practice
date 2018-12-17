def longest_substring_without_repeating(string):
    result_diction = []
    for i in range(len(string)):
        result_diction.append(helper(string, i, result_diction))

    longest_start_point = result_diction.index(max(result_diction))
    longest_substring = []
    for i in range(longest_start_point, longest_start_point + max(result_diction)):
        longest_substring.append(string[i])
    return ''.join(longest_substring)


def helper(string, start, diction):
    seen = set()
    for i in range(start, len(string)):
        if string[i] not in seen:
            seen.add(string[i])
        else:
            diction[i - start] = i
            return
    diction[len(string) - start] = start
    return

if __name__ == '__main__':
    result_length = longest_substring_without_repeating('abcdee')
    print(result_length)