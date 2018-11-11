class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, pre, nex):
            self._element = element
            self._prev = pre
            self._next = nex

    def __init__(self):

        self._header = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._header._next = self._tail
        self._tail._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.__len__() == 0

    def _insert_between(self, e, pre, nex):
        new_node = self._Node(e, pre, nex)
        pre._next = new_node
        nex._prev = new_node
        new_node._prev = pre
        new_node._next = nex
        self._size += 1

    def _delete_between(self, node):
        if self.is_empty():
            raise Exception('it\'s empty')

        element = node._element
        previous = node._prev
        successor = node._next
        previous._next = successor
        successor._prev = previous
        node._prev = node._next = node._element = None
        self._size -= 1
        return element