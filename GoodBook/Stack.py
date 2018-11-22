class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self.__len__() == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is emplty')

        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('empty')

        return self._data.pop()


class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, e, n):
            self._element = e
            self._next = n

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.__len__() == 0

    def push(self, e):
        new_head = self._Node(e, self._head)
        self._head = new_head
        self._size += 1

    def pop(self):
        removed = self.top()
        self._head = self._head._next
        self._size -= 1
        return removed

    def top(self):

        if self.is_empty():
            raise Exception('Stack is empty')

        return self._head._element


if __name__=='__main__':
    test = [1,2,3,4]
    node = LinkedStack()
    resut = []
    for t in test:
        node.push(t)

    while not node.is_empty():
        resut.append(node.pop())


    for k in resut:
        print(k ,end=' ')
