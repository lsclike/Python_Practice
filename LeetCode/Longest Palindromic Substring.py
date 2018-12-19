def longest_palindromic(s):
    length = len(s)
    substrings = []
    for n in range(length):
        repeated_substring(s, n, substrings)
    return substrings


def repeated_substring(s, i, strings):
    seen = set()
    for t in range(i, len(s)):
        if s[t] not in seen:
            seen.add(s[i])
        else:
            strings.append(s[i:t+1])
            return None
        strings.append(s[i:len(s)])
        return None

if __name__ == '__main__':
    test = 'avabgb'
    print(longest_palindromic(test))