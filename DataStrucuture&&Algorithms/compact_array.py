import array
import sys
# the result is not the expectation
primes = array.array('i', [2232, 5, 4, 2, 3, 5])
test = [['hello'], 5, 4, 2, 3, 5]

for t in test:
    print(sys.getsizeof(t))