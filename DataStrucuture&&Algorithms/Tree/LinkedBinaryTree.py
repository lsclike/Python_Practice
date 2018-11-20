from .BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_left', '_right', '_parent'

        def __init__(self, element, left, right, parent):
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
