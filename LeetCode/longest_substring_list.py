from LeetCode.isPalindrome import isPalindrome


def longest_substring_without_repeating(string):
    result_list = []
    for i in range(len(string)):
        helper(string, i, result_list)

    palindromic_result = filtering_palindromic(result_list)
    final_result = max(palindromic_result, key=len)
    return final_result

def helper(string, start, result_list):
    seen = set()
    for i in range(start, len(string)):
        if string[i] not in seen:
            seen.add(string[i])
        else:
            if string[start] == string[i]:
                result_list.append(string[start:i+1])



def filtering_palindromic(repeated_substrings):
    result = []
    for string in repeated_substrings:
        if isPalindrome(string):
            result.append(string)

    return result

if __name__ == '__main__':
    test= "abcdedcbaaba"
    result = longest_substring_without_repeating(test)
    print(result)