import array
import sys
# the result is not the expectation
primes = array.array('u', ['a', 'b', 'c'])
test = [['hello'], (1,2,3), 's', 2, 3, 5]

for t in primes:
    print(sys.getsizeof(t), end=' ')

print()

for d in test:
    print(sys.getsizeof(d), end=' ')