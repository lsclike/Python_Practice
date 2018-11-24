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
            return self._Node(key, value, n = 1)
        else:
            if key < node.value:
                node.left = self._put(node.left, key, value)
            elif key > node.value:
                node.right = self._put(node.right, key, value)
            else:
                node.value = value
            node.number = self._size(node.left) + self._size(node.right) + 1
            return node
