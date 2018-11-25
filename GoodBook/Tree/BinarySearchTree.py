class BinarySearchTree:
    class _Node:
        __slots__ = 'key', 'value', 'left', 'right', 'number'

        def __init__(self, key, value, left, right, n):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
            self.number = n

    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node:
            return node.number
        else:
            return None

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if not node:
            return None
        else:
            if key < node.key:
                return self._get(node.left, key)
            else:
                return self._get(node.right, key)

    def put(self, key, value):
        self._put(self.root, key, value)

    def _put(self, node, key, value):
        if not node:
            return self._Node(key, value, n=1)
        else:
            if key < node.value:
                node.left = self._put(node.left, key, value)
            elif key > node.value:
                node.right = self._put(node.right, key, value)
            else:
                node.value = value
            node.number = self._size(node.left) + self._size(node.right) + 1
            return node

    def min(self):
        return self._min(self.root)

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def max(self):
        return self._max(self.root)

    def _max(self, node):
        if node.right is None:
            return node
        return self._max(self._max(node.right))

    def floor(self, key):
        result = self._floor(key, self.root)
        if result is None:
            return None
        return result.key

    '''modifyng the code for flooring'''
    def _floor(self, node, key):
        if node is None:
            return None
        if node.key is key:
            return node
        elif node.key < key:
            if node.right is None:
                return node
            else:
                return self._floor(node.right, key)
        else:
            return self._floor(node.left, key)

    def ceiling(self, key):

        result = self._ceiling(self.root, key)
        if result is None:
            return None
        else:
            return result.key

    def _ceiling(self, node, key):
        if node is None:
            return None
        if node.key is key:
            return node
        elif node.key > key:
            return self._ceiling(node.right, key)
        else:
            if node.left is None:
                return node
            else:
                return self._ceiling(node.left, key)

    def selection(self, key):
        return self._selection(self.root, key)

    def _selection(self, node, key):
        if not node:
            return None
        size = self._size(node.left)
        if size < key:
            return self._selection(node.right, key - size - 1)
        elif size > key:
            return self._selection(node.left, key)
        else:
            return node




