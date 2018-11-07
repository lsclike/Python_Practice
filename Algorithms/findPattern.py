class stringWithPattern:

    def __init__(self, pattern):
        self.pattern = pattern
        self.time = 0


def findPattern(arr, low, high,pattern):

    if low > high:
        return

    else:
        mid = (low + high) // 2

        if arr[mid] == pattern.pattern:
            pattern.time += 1

        elif