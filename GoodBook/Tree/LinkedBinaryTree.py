from GoodBook.Tree.BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', '_left', '_right', '_parent'

        def __init__(self, element, left=None, right=None, parent=None):
            self._element = element
            self._left = left
            self._right = right
            self._parent = parent

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('P must be a position object')
        if p._container is not self:
            raise ValueError('P does not belong to the container')
        if p._node._parent is p._node:
            raise ValueError('P is no longer valid')
        return p._node

    def _make_position(self, node):

        return self.Position(self, node) if node is not None else None

    def __init__(self):

        self._root = None
        self._size = 0

    def __len__(self):

        return self._size

    def root(self):
        return self._make_position(self._root)

    def is_leaf(self, p):
        if self.num_children(p) == 0:
            return True
        else:
            return False

    def is_empty(self):
        return self.__len__() == 0

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    def _height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self):
        return self._height(self.root())

    def is_root(self, p):
        return p is self.root()

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def _add_root(self, e):

        if self._root is not None:
            raise ValueError('Root exist')

        self._size = 1
        root = self._Node(e)
        self._root = root
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left exist')

        left = self._Node(e, parent=node)
        node._left = left
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._make_position(p)
        if node._right is not None:
            raise ValueError('Right exist')
        right = self._Node(e, parent=node)
        node._right = right
        self._size += 1
        return self._make_position(node._right)

    def _delete_(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('there are two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = node
        return node._element

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError(' the node is not a leaf')
        if not type(self) is type(t1) is type(t2):
            raise ValueError('not all parameters are tree')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            self._change_parent(node, t1, 'left')
        if not t2.is_empty():
            self._change_parent(node, t2, 'right')

    def _change_parent(self, node, tree, position):

        tree._root._parent = node
        if position == 'left':
            node._left = tree._root
        else:
            node._right = tree._root
        tree._size = 0
        tree._root = None

    def insert(self, e):
        new_node = self._Node(e)
        if self.is_empty():
            self._add_root(e)g
        else:
            current = self._validate(self.root())
            while current is not None:
                parent_node = current
                if current._element < new_node._element:
                    current = current._right
                else:
                    current = current._left
            if parent_node._element < new_node._element:
                parent_node._right = new_node
            else:
                parent_node._left = new_node

            new_node._parent = parent_node


if __name__ == '__main__':
    test_tree = LinkedBinaryTree()
    for t in range(17):
        test_tree.insert(t)

    for t in test_tree.positions():
        print(t.element())




