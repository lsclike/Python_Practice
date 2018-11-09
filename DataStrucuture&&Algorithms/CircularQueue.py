class CircularQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, e, n):
            self._element = e
            self._next = n

    def __init__(self):

        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.__len__() == 0

    def first(self):
        if self.is_empty():
            raise Exception('the queue is empty')
        head = self._tail._next
        return head._element

    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail= new_node

        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('the Cqueue is empty')
        else:
            removed = self._tail._next
            self._tail._next = removed._next
            self._size -= 1
            return removed._element


    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


if __name__ == '__main__':
    test = 'bilibili'
    time = 100
    Cqueue = CircularQueue()
    for t in test:
        Cqueue.enqueue(t)

    while time > 0:
        print(Cqueue.first(), end=' ')
        Cqueue.rotate()
        time -=1



