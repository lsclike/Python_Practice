class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._tail = 0

    def __len__(self):
        return self._size

    def empty(self):
        return self.__len__() == 0

    def first(self):

        if self.empty():
            raise Exception('Array Queue is empty')
        return self._data[self._front]

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize( 2 * len(self._data))

        # position = (self._front + self._size) % len(self._data)
        # self._data[position] = e
        self._data[self._tail] = e
        self._tail = (self._tail + 1) % len(self._data)
        self._size += 1

    def _resize(self, capital):

        old = self._data
        self._data = [None] * capital
        first = self._front
        for k in range(capital):
            self._data[k] = old[first]
            first = (first + 1) % len(old)

        self._front = 0
        self._tail = len(old)

    def dequeue(self):
        if self.empty():
            raise Exception('the queue is empty')

        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return result


class LinkedQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, e, n):
            self._element = e
            self._next = n

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.__len__() == 0

    def enqueue(self, e):
        if self.is_empty():
            self._head = self._tail = self._Node(e, None)
        else:
            self._tail._next = self._Node(e, None)
            self._tail = self._tail._next
        self._size += 1

    def top(self):
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception('the queue is empty')
        result = self.top()
        self._head = self._head._next
        self._size -= 1
        return result

if __name__ == '__main__':
    test= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    new = ArrayQueue()
    result = []
    for k in test:
        new.enqueue(k)

    while not new.empty():
        result.append(new.dequeue())

    for t in result:
        print(t, end=' ')
