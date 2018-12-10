from GoodBook.Tree.TreeTravel import postOrder,levelOrder
class BinarySearchTree:
    class _Node:
        __slots__ = 'key', 'value', 'left', 'right', 'number'

        def __init__(self, key, value, left=None, right=None, n=None):
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
            return 0

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if not node:
            return None
        else:
            if key < node.key:
                return self._get(node.left, key)
            elif key > node.key:
                return self._get(node.right, key)
            else:
                return node.value

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if not node:
            return self._Node(key, value, n=1)
        else:
            if key < node.key:
                node.left = self._put(node.left, key, value)
            elif key > node.key:
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

    def selection(self, k):
        return self._selection(self.root, k)

    def _selection(self, node, k):
        if not node:
            return None
        size = self._size(node.left)
        if size < k:
            return self._selection(node.right, k - size - 1)
        elif size > k:
            return self._selection(node.left, k)
        else:
            return node

    def rank(self, key):
        return self._rank(key, self.root)

    def _rank(self, key, node):
        if node is None:
            return 0
        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return self._size(node.left) + 1 + self._rank(key, node.right)
        else:
            return self._size(node.left)


if __name__ == '__main__':
    testTree = BinarySearchTree()
    testTree.put(50, 'first')
    testTree.put(40, 'second')
    testTree.put(30, 'third')
    testTree.put(60, 'fourth')
    testTree.put(70, 'fifth')
    levelOrder(testTree.root)

